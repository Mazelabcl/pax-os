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
  conceptArts: ConceptArtsData;
  styleLock: string;
  /** Tabs históricos: guion, beat sheet, technical-script. */
  tabs: EpisodioTab[];
}

/** Slot `@imageN` parseado de la tabla markdown de cada prompt. */
export interface ImageSlot {
  /** Ej. `@image1`. */
  slot: string;
  /** Texto descriptivo del slot (segunda columna de la tabla). */
  descripcion: string;
  /** Path relativo a `public/` si la imagen existe (ej. `images/personajes/wiz.png`). null si TBD. */
  refPath: string | null;
  /** Si TBD, el ID del concept art a generar primero (ej. `concept-cave-wide-dark`). null si refPath está disponible. */
  conceptId: string | null;
  /** Estado de la celda derecha tal como viene del markdown. */
  estadoRaw: string;
  /** Resumen de estado: "available" (tiene PNG) | "tbd" (concept-art a generar) | "unknown". */
  estado: "available" | "tbd" | "unknown";
}

/** Concept art parseado de `concept-arts.md`. */
export interface ConceptArt {
  /** ID estable (ej. `concept-cave-wide-dark`). */
  id: string;
  /** Bloque al que pertenece: A (HEROs) / B (Derivados) / C (First-frames). */
  bloque: "A" | "B" | "C";
  /** Tipo: HERO / DERIVADO / FIRST-FRAME. Derivado del bloque. */
  tipo: "HERO" | "DERIVADO" | "FIRST-FRAME";
  /** Aliases que cubre (de "Aliases que cubre"). */
  aliases: string[];
  /** "Aparece en (storyboard)" texto crudo o vacío. */
  apareceStoryboard: string | null;
  /** "Aparece en (Seedance)" texto crudo. */
  apareceSeedance: string | null;
  /** "Para": (solo first-frames). */
  paraClip: string | null;
  /** "Tipo": tal cual viene del markdown (puede ser más detallado). */
  tipoNota: string | null;
  /** "Deriva de": cuando es derivado (ej. "concept-notebook-hero"). */
  derivaDe: string | null;
  /** Slots `@imageN` requeridos. */
  slots: ImageSlot[];
  /** Prompt Nano Banana (sin style-lock al copiar; ya viene con `[Style-lock pegado arriba]` placeholder). */
  prompt: string;
  /** Negative prompt si se separa explícitamente. Por ahora null — los concept arts traen el negative dentro del mismo bloque. */
  negative: string | null;
  /** Notas de generación (texto libre con bullets de lo que matchear / regenerar). */
  notas: string | null;
}

/** Bloque del orden de generación. */
export interface ConceptArtsBloque {
  letra: "A" | "B" | "C";
  titulo: string;
  descripcion: string;
  /** IDs en orden, tal como aparecen en el archivo. */
  orden: string[];
}

export interface ConceptArtsData {
  /** Bullets del header "Cómo usar este archivo". */
  comoUsar: string[];
  /** Bloques de orden de generación con IDs. */
  bloques: ConceptArtsBloque[];
  /** Total de assets a generar. */
  total: number;
  /** Lista plana de concept arts. */
  items: ConceptArt[];
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
  /** Slots `@imageN` parseados de la tabla markdown del prompt. */
  slots: ImageSlot[];
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

/**
 * Parsea la tabla markdown `| @imageN | descripción | path/estado |` que se
 * encuentra al inicio de cada prompt (storyboard, seedance y concept-arts).
 *
 * Formato esperado (después del heading "Reference images requeridas"):
 *
 *     | Slot | Imagen | Path / Estado |
 *     |------|--------|---------------|
 *     | `@image1` | Mood ref … | `public/images/portadas/portada2.png` ✓ |
 *     | `@image2` | Concept art … | **TBD — Nano Banana** (`concept-cave-fading-crystals`) |
 *
 * Devuelve [] si no se encuentra una tabla con header `Slot | Imagen | …`.
 */
function parseImageSlotsTable(body: string): ImageSlot[] {
  // Buscar la línea con header de la tabla.
  const lines = body.split(/\r?\n/);
  let headerIdx = -1;
  for (let i = 0; i < lines.length; i++) {
    const l = lines[i].trim().toLowerCase();
    // Tres variantes que aparecen en los .md.
    if (
      /^\|\s*slot\s*\|\s*imagen\s*\|\s*(path\s*\/\s*estado|path)\s*\|$/.test(l)
    ) {
      headerIdx = i;
      break;
    }
  }
  if (headerIdx < 0) return [];

  // Línea siguiente debe ser separador `|---|---|---|`. Saltarla.
  const sepIdx = headerIdx + 1;
  if (sepIdx >= lines.length || !/^\|[-\s|:]+\|$/.test(lines[sepIdx].trim())) {
    return [];
  }

  const slots: ImageSlot[] = [];
  for (let i = sepIdx + 1; i < lines.length; i++) {
    const line = lines[i].trim();
    if (!line.startsWith("|")) break;
    if (!line.endsWith("|")) break;
    // Splitear por `|` quitando primero y último vacío.
    const cells = line
      .slice(1, -1)
      .split("|")
      .map((c) => c.trim());
    if (cells.length < 3) continue;
    const slotCell = cells[0];
    const descCell = cells[1];
    const estadoCell = cells.slice(2).join(" | ").trim();

    // Slot: `@imageN` entre backticks. Si la celda dice "ninguna" o "—", lo descartamos.
    const slotMatch = slotCell.match(/`?(@image\d+)`?/i);
    if (!slotMatch) continue;
    const slot = slotMatch[1].toLowerCase();

    // Path disponible: cualquier `public/...` con `.png|jpg|jpeg|webp` y un ✓ visible.
    let refPath: string | null = null;
    let conceptId: string | null = null;
    let estado: ImageSlot["estado"] = "unknown";

    const pngMatch = estadoCell.match(/`?(public\/[^\s`]+\.(?:png|jpg|jpeg|webp))`?/i);
    const hasCheck = /[✓✔]/.test(estadoCell);
    if (pngMatch && hasCheck) {
      refPath = pngMatch[1].replace(/^public\//, "");
      estado = "available";
    } else {
      // Buscar concept ID entre backticks o como nombre suelto:
      //  - `concept-…` / `first-frame-…` / `last-frame-…` en cualquier celda.
      // En concept-arts.md, la descripcion suele decir directamente
      // "concept-cave-wide-dark" y el estado solo "(generar primero)".
      // Por eso buscamos primero en la celda de estado y como fallback en la
      // descripción.
      const conceptIdRe =
        /`?\b((?:concept|first-frame|last-frame)-[a-z0-9-]+)\b`?/i;
      const matchInEstado = estadoCell.match(conceptIdRe);
      const matchInDesc = descCell.match(conceptIdRe);
      const conceptMatch = matchInEstado ?? matchInDesc;
      const looksTbd = /tbd|generar/i.test(estadoCell);
      if (conceptMatch) {
        conceptId = conceptMatch[1];
        estado = "tbd";
      } else if (looksTbd) {
        estado = "tbd";
      } else if (pngMatch) {
        // PNG sin checkmark (raro, pero lo tratamos como disponible).
        refPath = pngMatch[1].replace(/^public\//, "");
        estado = "available";
      }
    }

    slots.push({
      slot,
      descripcion: descCell.replace(/`/g, ""),
      refPath,
      conceptId,
      estadoRaw: estadoCell,
      estado,
    });
  }

  return slots;
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
        // Slots: primero buscamos en el sub-clip; si no, fallback a la H2 padre.
        const subSlots = parseImageSlotsTable(sb.body);
        const slots = subSlots.length > 0 ? subSlots : parseImageSlotsTable(b.body);
        out.push({
          id: `escena-${subNumero.toLowerCase()}`,
          numero: subNumero,
          titulo: subTitulo || titulo,
          beat,
          refs,
          slots,
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

    const slots = parseImageSlotsTable(b.body);

    out.push({
      id: `escena-${numero.toLowerCase()}`,
      numero,
      titulo,
      beat,
      refs: globalRefs,
      slots,
      prompt,
      negative,
      notas: notasBlock ? notasBlock.trim() : null,
      audio: audioBlock ? audioBlock.trim() : null,
    });
  }
  return out;
}

/**
 * Parsea `concept-arts.md` y devuelve los 30 concept-arts como datos
 * estructurados, junto con el header "Cómo usar" y el orden de generación.
 */
function parseConceptArts(content: string): ConceptArtsData {
  // 1. "Cómo usar este archivo" → bullets.
  const comoUsarSec =
    extractSection(content, /^##\s+Cómo usar este archivo\s*$/i) ?? "";
  const comoUsar = comoUsarSec
    .split(/\r?\n/)
    .map((l) => l.replace(/^[-*]\s+/, "").trim())
    .filter((l) => l.length > 0)
    .slice(0, 8); // tope sano para UI

  // 2. "Orden de generación recomendado" → 3 sub-bloques A/B/C.
  const ordenSec =
    extractSection(content, /^##\s+Orden de generación recomendado\s*$/i) ?? "";
  const ordenBlocks = splitByH3(ordenSec);
  const bloques: ConceptArtsBloque[] = [];
  for (const b of ordenBlocks) {
    const m = /^Bloque\s+([A-C])\s*[—\-]\s*(.+)$/i.exec(b.heading);
    if (!m) continue;
    const letra = m[1].toUpperCase() as "A" | "B" | "C";
    const titulo = m[2].trim();
    // Primer texto no-lista como descripción.
    const ordenIds: string[] = [];
    const descLines: string[] = [];
    for (const rawLine of b.body.split(/\r?\n/)) {
      const line = rawLine.trim();
      if (!line) continue;
      // Buscar items numerados con backticks: "1. `concept-…`"
      const item = line.match(/^\d+\.\s+`([^`]+)`/);
      if (item) {
        ordenIds.push(item[1]);
      } else if (descLines.length === 0 && !/^\d+\./.test(line)) {
        // tomamos la primera línea como descripción
        descLines.push(line);
      }
    }
    bloques.push({
      letra,
      titulo,
      descripcion: descLines.join(" ").trim(),
      orden: ordenIds,
    });
  }

  // 3. Items: bajo cada `# Bloque X — …`, cada `## \`concept-…\`` es un item.
  const items: ConceptArt[] = [];
  // Particionar el contenido por `# Bloque ` (H1, no H2) — pero el archivo usa
  // `# Bloque A — HEROs reusables` como H1. Más fácil: recorrer todos los H2
  // que matchean concept IDs y deducir el bloque más cercano del último H1.
  const lines = content.split(/\r?\n/);
  let currentBloque: "A" | "B" | "C" | null = null;
  type Block = { id: string; bloque: "A" | "B" | "C"; body: string[] };
  const rawBlocks: Block[] = [];
  let current: Block | null = null;

  const idRe = /^##\s+`((?:concept|first-frame|last-frame)[a-z0-9-]+)`/i;

  for (const line of lines) {
    // Detectar H1 "# Bloque X"
    const h1Match = /^#\s+Bloque\s+([A-C])\s*[—\-]/i.exec(line);
    if (h1Match) {
      currentBloque = h1Match[1].toUpperCase() as "A" | "B" | "C";
      if (current) rawBlocks.push(current);
      current = null;
      continue;
    }
    // Detectar H2 con concept ID.
    const idMatch = idRe.exec(line);
    if (idMatch && currentBloque) {
      if (current) rawBlocks.push(current);
      current = { id: idMatch[1], bloque: currentBloque, body: [] };
      continue;
    }
    // Detectar próximo H2 que NO es concept (ej. apéndice) → cerrar.
    if (/^##\s/.test(line) && !idMatch) {
      if (current) rawBlocks.push(current);
      current = null;
      continue;
    }
    // Detectar próximo H1 (ej. "# Apéndice") → cerrar y resetear bloque.
    if (/^#\s/.test(line) && !h1Match) {
      if (current) rawBlocks.push(current);
      current = null;
      currentBloque = null;
      continue;
    }
    if (current) current.body.push(line);
  }
  if (current) rawBlocks.push(current);

  for (const rb of rawBlocks) {
    const body = rb.body.join("\n");

    // Aliases: `**Aliases que cubre**: `concept-x`, `concept-y``
    const aliasField = extractField(body, "Aliases que cubre");
    const aliases: string[] = [];
    if (aliasField) {
      const re = /`([^`]+)`/g;
      let m: RegExpExecArray | null;
      while ((m = re.exec(aliasField)) !== null) aliases.push(m[1]);
    }

    const apareceStoryboard = extractField(body, "Aparece en \\(storyboard\\)");
    const apareceSeedance = extractField(body, "Aparece en \\(Seedance\\)");
    const paraClip = extractField(body, "Para");
    const tipoNota = extractField(body, "Tipo");
    const derivaDeRaw = extractField(body, "Deriva de");
    let derivaDe: string | null = null;
    if (derivaDeRaw) {
      const m = derivaDeRaw.match(/`([^`]+)`/);
      derivaDe = m ? m[1] : derivaDeRaw;
    }

    const slots = parseImageSlotsTable(body);

    // Prompt: dentro de "Prompt Nano Banana".
    const promptBlock = extractLabeledBlock(body, "Prompt Nano Banana");
    const prompt = promptBlock ? firstCodeBlock(promptBlock) : null;
    if (!prompt) continue;

    // Notas (texto libre con bullets).
    const notas = extractLabeledBlock(body, "Notas");

    // Tipo final: HERO / DERIVADO / FIRST-FRAME — derivado del bloque.
    const tipo: ConceptArt["tipo"] =
      rb.bloque === "A" ? "HERO" : rb.bloque === "B" ? "DERIVADO" : "FIRST-FRAME";

    items.push({
      id: rb.id,
      bloque: rb.bloque,
      tipo,
      aliases,
      apareceStoryboard,
      apareceSeedance,
      paraClip,
      tipoNota,
      derivaDe,
      slots,
      prompt,
      negative: null,
      notas: notas ? notas.trim() : null,
    });
  }

  return {
    comoUsar,
    bloques,
    total: items.length,
    items,
  };
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
  const [escenasDoc, storyboardDoc, seedanceDoc, conceptArtsDoc, styleDoc, ...tabDocs] =
    await Promise.all([
      readMarkdown("episodio-1/escenas.md"),
      readMarkdown("episodio-1/storyboard-nano.md"),
      readMarkdown("episodio-1/seedance-prompts.md"),
      readMarkdown("episodio-1/concept-arts.md"),
      readMarkdown("style-guide.md"),
      ...TAB_DEFS.map((t) => readMarkdown(`episodio-1/${t.file}`)),
    ]);

  const escenas = parseEscenas(escenasDoc.content);
  const storyboard = parsePromptScenes(storyboardDoc.content, "nano");
  const seedance = parsePromptScenes(seedanceDoc.content, "seedance");
  const conceptArts = parseConceptArts(conceptArtsDoc.content);
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
    conceptArts,
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

/**
 * Arma el bloque copy-friendly para un concept art:
 *   - Sustituye el placeholder `[Style-lock pegado arriba]` por el style-lock real.
 *   - Lista paths de slots disponibles arriba.
 *   - Si hay slots TBD, los flagea como "@imageN: GENERAR PRIMERO (concept-…)".
 */
export function buildConceptArtFullPrompt(
  art: ConceptArt,
  styleLock: string,
): string {
  const parts: string[] = [];
  if (styleLock) {
    parts.push(`# Style lock\n${styleLock}`);
  }
  if (art.slots.length > 0) {
    const lines = art.slots.map((s) => {
      if (s.estado === "available" && s.refPath) {
        return `- ${s.slot}: public/${s.refPath} (${s.descripcion})`;
      }
      if (s.estado === "tbd" && s.conceptId) {
        return `- ${s.slot}: GENERAR PRIMERO -> ${s.conceptId} (${s.descripcion})`;
      }
      return `- ${s.slot}: ${s.descripcion} [${s.estadoRaw}]`;
    });
    parts.push(`# Reference image slots\n${lines.join("\n")}`);
  }
  // Sustituir el placeholder en el prompt.
  const promptCleaned = art.prompt.replace(
    /\[Style-lock pegado arriba\]\s*\n?/i,
    "",
  );
  parts.push(`# Prompt\n${promptCleaned}`);
  return parts.join("\n\n");
}
