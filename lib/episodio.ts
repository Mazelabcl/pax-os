import { readMarkdown } from "./markdown";

// =============================================================================
// Tipos públicos
// =============================================================================

export interface EpisodioTab {
  id: string;
  label: string;
  path: string;
  content: string;
}

export interface EpisodioData {
  title: string | null;
  synopsis: string | null;
  tldr: string | null;
  pitch: string | null;
  divisionResumen: string | null;
  duracionTotal: string | null;
  cantidadEscenas: number;
  escenas: Escena[];
  storyboard: PromptScene[];
  seedance: PromptScene[];
  styleLock: string;
  /** Tabs históricos: guion, beat sheet, technical-script. */
  tabs: EpisodioTab[];
}

export interface Escena {
  /** Slug del id, ej. "escena-01". */
  id: string;
  /** Solo el número, ej. "01". */
  numero: string;
  /** Heading completo después del em-dash, ej. "Un cristal a punto de apagarse". */
  titulo: string;
  duracion: string | null;
  ubicacion: string | null;
  personajes: string | null;
  mood: string | null;
  beat: string | null;
  descripcion: string | null;
  dialogo: string | null;
}

export interface PromptScene {
  /** Slug derivado del heading, ej. "escena-01". */
  id: string;
  /** Numero como string ("01", "08A", "08B", "14"). */
  numero: string;
  /** Titulo legible, ej. "Un cristal a punto de apagarse". */
  titulo: string;
  /** Beat narrativo (opcional). */
  beat: string | null;
  /** Lista de paths de reference images (relativos a public/). */
  refs: string[];
  /** El primer code block después de "Prompt visual" / "Prompt Seedance". */
  prompt: string;
  /** Code block del negative prompt, sin backticks. */
  negative: string | null;
  /** Notas de dirección (texto libre). */
  notas: string | null;
  /** Bloque "Audio" si existe (Seedance). */
  audio: string | null;
}

// =============================================================================
// Tabs históricos (material original)
// =============================================================================

const TAB_DEFS = [
  { id: "guion", label: "Guion", file: "script.md" },
  { id: "beat-sheet", label: "Beat sheet", file: "beat-sheet.md" },
  { id: "guion-tecnico", label: "Guion técnico", file: "technical-script.md" },
] as const;

export function tabContentPath(tab: EpisodioTab): string {
  return `content/${tab.path}`;
}

// =============================================================================
// Parsing helpers
// =============================================================================

/** Slug GitHub-ish para los IDs. */
function slugify(text: string): string {
  return text
    .toLowerCase()
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .replace(/[^a-z0-9\s-]/g, "")
    .trim()
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-");
}

/** Extrae texto de una sección `## <heading>` hasta el siguiente `## ` o EOF. */
function extractSection(content: string, headingRegex: RegExp): string | null {
  const lines = content.split(/\r?\n/);
  let start = -1;
  for (let i = 0; i < lines.length; i++) {
    if (headingRegex.test(lines[i])) {
      start = i + 1;
      break;
    }
  }
  if (start < 0) return null;
  const out: string[] = [];
  for (let i = start; i < lines.length; i++) {
    if (/^##\s/.test(lines[i])) break;
    out.push(lines[i]);
  }
  return out.join("\n").trim() || null;
}

/** Devuelve los bloques bajo cada `### <heading>` dentro de un texto. */
function splitByH3(content: string): { heading: string; body: string }[] {
  const lines = content.split(/\r?\n/);
  const blocks: { heading: string; body: string[] }[] = [];
  let current: { heading: string; body: string[] } | null = null;
  for (const line of lines) {
    const m = /^###\s+(.+?)\s*$/.exec(line);
    if (m) {
      if (current) blocks.push(current);
      current = { heading: m[1].trim(), body: [] };
    } else if (current) {
      current.body.push(line);
    }
  }
  if (current) blocks.push(current);
  return blocks.map((b) => ({ heading: b.heading, body: b.body.join("\n").trim() }));
}

/** Devuelve los bloques bajo cada `## <heading>` dentro de un texto, ignorando `## ` anteriores al primero. */
function splitByH2(content: string): { heading: string; body: string }[] {
  const lines = content.split(/\r?\n/);
  const blocks: { heading: string; body: string[] }[] = [];
  let current: { heading: string; body: string[] } | null = null;
  for (const line of lines) {
    const m = /^##\s+(.+?)\s*$/.exec(line);
    if (m) {
      if (current) blocks.push(current);
      current = { heading: m[1].trim(), body: [] };
    } else if (current) {
      current.body.push(line);
    }
  }
  if (current) blocks.push(current);
  return blocks.map((b) => ({ heading: b.heading, body: b.body.join("\n").trim() }));
}

/** Extrae el primer code block triple-backtick de un texto. */
function firstCodeBlock(text: string): string | null {
  const match = text.match(/```[a-zA-Z0-9_-]*\n([\s\S]*?)```/);
  return match ? match[1].trim() : null;
}

/** Extrae todos los code blocks triple-backtick. */
function allCodeBlocks(text: string): string[] {
  const blocks: string[] = [];
  const re = /```[a-zA-Z0-9_-]*\n([\s\S]*?)```/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(text)) !== null) {
    blocks.push(m[1].trim());
  }
  return blocks;
}

/**
 * Extrae lista de paths de reference images de un bloque tipo:
 *   1. `public/images/personajes/wiz.png` — character lock
 * o
 *   - **Wiz:** `public/images/personajes/wiz.png`
 * (toma el contenido entre backticks)
 */
function extractRefs(text: string): string[] {
  const refs: string[] = [];
  const re = /`([^`]+\.(?:png|jpg|jpeg|webp))`/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(text)) !== null) {
    let path = m[1].trim();
    // Normalizar: queremos paths relativos a `public/`
    path = path.replace(/^public\//, "");
    if (!refs.includes(path)) refs.push(path);
  }
  return refs;
}

/** Toma una sub-sección dentro de un bloque hasta que aparece otro `**Heading**:` o el final. */
function extractField(body: string, label: string): string | null {
  // Match `- **Label**: valor` o `**Label**: valor` (puede ser multi-line si el siguiente bullet empieza con `- **`)
  const re = new RegExp(
    `(?:^|\\n)-?\\s*\\*\\*${label}\\*\\*\\s*:\\s*([\\s\\S]*?)(?=\\n-\\s*\\*\\*[^*]+\\*\\*\\s*:|\\n###\\s|\\n##\\s|$)`,
    "i",
  );
  const m = body.match(re);
  if (!m) return null;
  return m[1].trim() || null;
}

/** Extrae sección entre **Label** y la próxima `**Otra label**` (para sub-bloques con code blocks). */
function extractLabeledBlock(body: string, label: string): string | null {
  const re = new RegExp(
    `\\*\\*${label}\\*\\*[^\\n]*\\n([\\s\\S]*?)(?=\\n\\*\\*[A-Z][^*]*\\*\\*|\\n##\\s|\\n---|$)`,
    "i",
  );
  const m = body.match(re);
  if (!m) return null;
  return m[1].trim() || null;
}

// =============================================================================
// Parsers de archivos
// =============================================================================

function parseEscenas(content: string): Escena[] {
  // El archivo tiene "## Escenas" como sección y dentro `### Escena XX — título`
  const escenasSection = extractSection(content, /^##\s+Escenas\s*$/i);
  if (!escenasSection) return [];

  const blocks = splitByH3(escenasSection);
  const out: Escena[] = [];
  for (const b of blocks) {
    const m = /^Escena\s+(\d+)\s*[—\-]\s*(.+)$/i.exec(b.heading);
    if (!m) continue;
    const numero = m[1].trim();
    const titulo = m[2].trim();
    const id =
      extractField(b.body, "ID")?.replace(/`/g, "").trim() ||
      `escena-${numero}`;

    out.push({
      id,
      numero,
      titulo,
      duracion: extractField(b.body, "Duración"),
      ubicacion: extractField(b.body, "Ubicación"),
      personajes: extractField(b.body, "Personajes"),
      mood: extractField(b.body, "Mood"),
      beat: extractField(b.body, "Beat narrativo"),
      descripcion: extractField(b.body, "Descripción"),
      dialogo:
        extractField(b.body, "Diálogo / Sonido clave") ||
        extractField(b.body, "Diálogo"),
    });
  }
  return out;
}

function parseTotalDuration(content: string): string | null {
  // Buscar "Catorce escenas, 3:45 minutos en total" o similar dentro de "## Cómo se divide"
  const sec = extractSection(content, /^##\s+Cómo se divide\s*$/i);
  if (!sec) return null;
  const m = sec.match(/(\d+:\d+)\s*minutos?/i);
  return m ? m[1] : null;
}

function parsePromptScenes(content: string, kind: "nano" | "seedance"): PromptScene[] {
  const blocks = splitByH2(content);
  const out: PromptScene[] = [];
  for (const b of blocks) {
    const m = /^Escena\s+(\d+[A-Z]?)\s*[—\-]\s*(.+)$/i.exec(b.heading);
    if (!m) continue;
    const numero = m[1].trim();
    const titulo = m[2].trim();

    // Beat (común a la H2)
    const beatMatch = b.body.match(/\*\*Beat narrativo\*\*\s*:\s*([^\n]+)/i);
    const beat = beatMatch ? beatMatch[1].trim() : null;

    // Refs globales (de los bullets iniciales)
    const refsBlock =
      extractLabeledBlock(b.body, "Reference images") ||
      extractLabeledBlock(b.body, "Reference images globales") ||
      "";
    const globalRefs = extractRefs(refsBlock);

    const notasBlock = extractLabeledBlock(b.body, "Notas de dirección");
    const audioBlock = extractLabeledBlock(b.body, "Audio");

    // Detectar sub-clips por `### Sub-clip ...`
    const subBlocks = splitByH3(b.body);
    const subClipBlocks = subBlocks.filter((s) =>
      /^Sub-?clip/i.test(s.heading),
    );

    if (subClipBlocks.length > 0 && kind === "seedance") {
      // Emitir un PromptScene por cada sub-clip
      for (const sb of subClipBlocks) {
        const subM = /^Sub-?clip\s+escena-(\d+[A-Z]?)/i.exec(sb.heading);
        const subNumero = subM ? subM[1] : `${numero}?`;
        const subTitulo = sb.heading.replace(/^Sub-?clip\s+escena-\d+[A-Z]?\s*[—\-]\s*/i, "").trim();
        const promptBlock = extractLabeledBlock(sb.body, "Prompt Seedance");
        const negativeBlock = extractLabeledBlock(sb.body, "Negative prompt");
        const sceneRefs = extractRefs(sb.body);
        const refs = [...new Set([...sceneRefs, ...globalRefs])];
        const prompt = promptBlock ? firstCodeBlock(promptBlock) : null;
        const negative = negativeBlock
          ? firstCodeBlock(negativeBlock)
          : null;
        if (!prompt) continue;
        out.push({
          id: `escena-${subNumero.toLowerCase()}`,
          numero: subNumero,
          titulo: subTitulo || titulo,
          beat,
          refs,
          prompt,
          negative,
          notas: notasBlock ? notasBlock.trim() : null,
          audio: audioBlock ? audioBlock.trim() : null,
        });
      }
      continue;
    }

    // Caso simple: una sola prompt en la H2
    const codeBlocks = allCodeBlocks(b.body);
    let prompt: string | null = null;
    let negative: string | null = null;

    if (kind === "nano") {
      const promptBlock = extractLabeledBlock(b.body, "Prompt visual");
      const negativeBlock = extractLabeledBlock(b.body, "Negative prompt");
      prompt = promptBlock ? firstCodeBlock(promptBlock) : null;
      negative = negativeBlock ? firstCodeBlock(negativeBlock) : null;
    } else {
      const promptBlock = extractLabeledBlock(b.body, "Prompt Seedance");
      const negativeBlock = extractLabeledBlock(b.body, "Negative prompt");
      prompt = promptBlock ? firstCodeBlock(promptBlock) : null;
      negative = negativeBlock ? firstCodeBlock(negativeBlock) : null;
    }

    // Fallback: si no encontró, tomar el primer/segundo code block
    if (!prompt && codeBlocks.length > 0) prompt = codeBlocks[0];
    if (!negative && codeBlocks.length > 1) negative = codeBlocks[1];

    if (!prompt) continue;

    out.push({
      id: `escena-${numero.toLowerCase()}`,
      numero,
      titulo,
      beat,
      refs: globalRefs,
      prompt,
      negative,
      notas: notasBlock ? notasBlock.trim() : null,
      audio: audioBlock ? audioBlock.trim() : null,
    });
  }
  return out;
}

function parseStyleLock(styleGuideContent: string): string {
  // Tomar el primer code block dentro de "## Bloque de estilo reutilizable"
  const sec = extractSection(
    styleGuideContent,
    /^##\s+Bloque de estilo reutilizable\s*$/i,
  );
  if (sec) {
    const block = firstCodeBlock(sec);
    if (block) return block;
  }
  // Fallback: cualquier code block del style-guide
  const any = firstCodeBlock(styleGuideContent);
  return any ?? "";
}

// =============================================================================
// API pública
// =============================================================================

export async function getEpisodio1(): Promise<EpisodioData> {
  const [escenasDoc, storyboardDoc, seedanceDoc, styleDoc, ...tabDocs] =
    await Promise.all([
      readMarkdown("episodio-1/escenas.md"),
      readMarkdown("episodio-1/storyboard-nano.md"),
      readMarkdown("episodio-1/seedance-prompts.md"),
      readMarkdown("style-guide.md"),
      ...TAB_DEFS.map((t) => readMarkdown(`episodio-1/${t.file}`)),
    ]);

  const escenas = parseEscenas(escenasDoc.content);
  const storyboard = parsePromptScenes(storyboardDoc.content, "nano");
  const seedance = parsePromptScenes(seedanceDoc.content, "seedance");
  const styleLock = parseStyleLock(styleDoc.content);

  // TLDR + pitch
  const tldr = extractSection(escenasDoc.content, /^##\s+TLDR\s*$/i);
  const pitch = extractSection(escenasDoc.content, /^##\s+El pitch\s*$/i);
  const divisionResumen = extractSection(
    escenasDoc.content,
    /^##\s+Cómo se divide\s*$/i,
  );

  const duracionTotal = parseTotalDuration(escenasDoc.content);

  // Título: usar frontmatter de escenas si tiene, si no parsear del script
  const fmTitle =
    (escenasDoc.frontmatter as { title?: string } | undefined)?.title ?? null;
  const scriptContent =
    tabDocs.find((_, i) => TAB_DEFS[i].id === "guion")?.content ?? "";
  let title: string | null = null;
  const scriptH1 = scriptContent.match(/^#\s+(.+)$/m);
  if (scriptH1) {
    const heading = scriptH1[1];
    const quoted = heading.match(/["“]([^"”]+)["”]/);
    if (quoted) title = quoted[1].trim();
  }
  if (!title && fmTitle) title = fmTitle.replace(/^Episodio\s+\d+\s*[—\-:]\s*/i, "");

  const tabs: EpisodioTab[] = TAB_DEFS.map((t, i) => ({
    id: t.id,
    label: t.label,
    path: `episodio-1/${t.file}`,
    content: tabDocs[i].content,
  }));

  return {
    title,
    synopsis: tldr ? tldr.split(/\n\n/)[0].trim() : null,
    tldr,
    pitch,
    divisionResumen,
    duracionTotal,
    cantidadEscenas: escenas.length,
    escenas,
    storyboard,
    seedance,
    styleLock,
    tabs,
  };
}

/** Helper standalone para `/estilo`. */
export async function getStyleGuide(): Promise<{
  content: string;
  styleLock: string;
}> {
  const doc = await readMarkdown("style-guide.md");
  const styleLock = parseStyleLock(doc.content);
  return { content: doc.content, styleLock };
}

/** Helper standalone para landing: solo tldr. */
export async function getEpisodio1Tldr(): Promise<string | null> {
  const doc = await readMarkdown("episodio-1/escenas.md");
  return extractSection(doc.content, /^##\s+TLDR\s*$/i);
}

/**
 * Arma el bloque copy-friendly: style-lock + refs + prompt + negative.
 * Esto se exporta para los componentes client de copia.
 */
export function buildFullPrompt(
  scene: PromptScene,
  styleLock: string,
): string {
  const parts: string[] = [];
  if (styleLock) {
    parts.push(`# Style lock\n${styleLock}`);
  }
  if (scene.refs.length > 0) {
    parts.push(
      `# Reference images\n${scene.refs.map((r) => `- public/${r}`).join("\n")}`,
    );
  }
  parts.push(`# Prompt\n${scene.prompt}`);
  if (scene.negative) {
    parts.push(`# Negative\n${scene.negative}`);
  }
  return parts.join("\n\n");
}
