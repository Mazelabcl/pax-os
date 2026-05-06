import { existsSync } from "node:fs";
import path from "node:path";
import { readMarkdown } from "./markdown";

// =============================================================================
// Tipos
// =============================================================================

export interface EpisodioOutline {
  /** Número del episodio (1..12). */
  numero: number;
  /** Título visible (sin "Episodio N — "). */
  titulo: string;
  /** Logline (1 línea). */
  logline: string;
  /** Tono dominante. */
  tono: string | null;
  /** Locación principal. */
  locacion: string | null;
}

export interface StoryboardShot {
  /** Slug del archivo sin extensión, ej. "cap-1-shot-01-crystal-dimming". */
  slug: string;
  /** Path público a la imagen, ej. "/images/storyboards/cap-1-shot-01-crystal-dimming.png". */
  image: string;
  /** Personajes detectados en frame. */
  personajes: string;
  /** Plano / encuadre / lente — extraído del prompt si es posible. */
  plano: string;
  /** Iluminación / mood — extraído del prompt si es posible. */
  mood: string;
  /** Caption corta (1 línea) para mostrar bajo la imagen. */
  caption: string;
  /** Número del shot (1..N) o null si es un compañero "hero" estilo `cap-1-clan-council`. */
  shotNumber: number | null;
  /** Título humano del companion (de YAML title o derivado). */
  titulo: string;
}

export interface EpisodioDetalle extends EpisodioOutline {
  /** Beat sheet — todos los párrafos parseados del outline. */
  beats: string[];
  /** Hook (intro 0:00-0:08). */
  hook: string | null;
  /** Cliffhanger / gancho próximo cap. */
  cliffhanger: string | null;
  /** Storyboards disponibles para este capítulo, ordenados por shot number. */
  shots: StoryboardShot[];
  /** Imagen "hero" recomendada para el episodio (primera shot disponible). */
  heroImage: string | null;
  /** Página cómic compilada (cap-N-comic-page.png) si existe. */
  comicPage: string | null;
}

// =============================================================================
// Outline parser
// =============================================================================

/**
 * Parsea el archivo `content/episodios-12-outline.md` y devuelve
 * los 12 episodios con título, logline, tono, locación.
 */
export async function listEpisodiosOutline(): Promise<EpisodioOutline[]> {
  const doc = await readMarkdown("episodios-12-outline.md");
  return parseOutline(doc.content);
}

export async function getEpisodioDetalle(
  numero: number,
): Promise<EpisodioDetalle | null> {
  const outline = await listEpisodiosOutline();
  const ep = outline.find((e) => e.numero === numero);
  if (!ep) return null;

  const doc = await readMarkdown("episodios-12-outline.md");
  const { beats, hook, cliffhanger } = parseEpisodioBody(doc.content, numero);
  const shots = await listStoryboardShots(numero);
  const heroImage =
    shots.find((s) => s.shotNumber === null)?.image ?? // companion hero
    shots[0]?.image ??
    null;
  const comicPage = await findComicPage(numero);

  return {
    ...ep,
    beats,
    hook,
    cliffhanger,
    shots,
    heroImage,
    comicPage,
  };
}

function parseOutline(content: string): EpisodioOutline[] {
  const lines = content.split(/\r?\n/);
  const result: EpisodioOutline[] = [];
  let current: Partial<EpisodioOutline> | null = null;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const epHeader = /^##\s+Episodio\s+(\d+)\s*[—\-]\s*(.+)$/.exec(line);
    if (epHeader) {
      if (current && current.numero) {
        result.push(fillDefaults(current));
      }
      current = {
        numero: parseInt(epHeader[1], 10),
        titulo: epHeader[2].trim(),
      };
      continue;
    }
    if (!current) continue;

    const logline = /^\*\*Logline:\*\*\s*(.+)$/.exec(line);
    if (logline) {
      current.logline = logline[1].trim();
      continue;
    }
    const tono = /^\*\*Tono dominante:\*\*\s*(.+)$/.exec(line);
    if (tono) {
      current.tono = tono[1].trim();
      continue;
    }
    const loc = /^\*\*Locación principal:\*\*\s*(.+)$/.exec(line);
    if (loc) {
      current.locacion = loc[1].trim();
      continue;
    }
  }
  if (current && current.numero) {
    result.push(fillDefaults(current));
  }
  return result.sort((a, b) => a.numero - b.numero);
}

function fillDefaults(p: Partial<EpisodioOutline>): EpisodioOutline {
  return {
    numero: p.numero ?? 0,
    titulo: p.titulo ?? "",
    logline: p.logline ?? "",
    tono: p.tono ?? null,
    locacion: p.locacion ?? null,
  };
}

/**
 * Extrae los beats principales (lista de párrafos como bullets) +
 * hook y cliffhanger del bloque de un episodio dado.
 */
function parseEpisodioBody(
  content: string,
  numero: number,
): { beats: string[]; hook: string | null; cliffhanger: string | null } {
  const lines = content.split(/\r?\n/);
  let inBlock = false;
  let body: string[] = [];

  for (const line of lines) {
    const epHeader = /^##\s+Episodio\s+(\d+)\s*[—\-]/.exec(line);
    if (epHeader) {
      const n = parseInt(epHeader[1], 10);
      if (inBlock) break;
      if (n === numero) {
        inBlock = true;
        continue;
      }
    }
    if (inBlock) body.push(line);
  }

  const text = body.join("\n");
  const hook = extractFieldBlock(text, /\*\*Hook[^:]*:\*\*\s*([\s\S]*?)(?=\n\*\*|$)/);
  const cliff = extractFieldBlock(
    text,
    /\*\*Cliffhanger[^:]*:\*\*\s*([\s\S]*?)(?=\n\*\*|$)/,
  );

  // Beats principales = bullets bajo "**Beats principales:**" (lista)
  const beatsBlockMatch = text.match(
    /\*\*Beats principales:\*\*\s*\n([\s\S]*?)(?=\n\*\*[A-Z][^*]+\*\*|$)/,
  );
  const beats: string[] = [];
  if (beatsBlockMatch) {
    const beatsRaw = beatsBlockMatch[1];
    const bulletRe = /^\s*-\s+(.+)$/gm;
    let m: RegExpExecArray | null;
    while ((m = bulletRe.exec(beatsRaw)) !== null) {
      beats.push(m[1].trim());
    }
  }

  return { beats, hook, cliffhanger: cliff };
}

function extractFieldBlock(text: string, re: RegExp): string | null {
  const m = text.match(re);
  if (!m) return null;
  return m[1].trim() || null;
}

// =============================================================================
// Storyboards
// =============================================================================

const PUBLIC_DIR = path.join(process.cwd(), "public");
const STORYBOARDS_DIR = path.join(
  process.cwd(),
  "content",
  "storyboards",
);

import { promises as fs } from "node:fs";

/**
 * Lista los shots disponibles para un capítulo. Lee los .png en
 * `public/images/storyboards/cap-N/` (subcarpeta canon) y .md companions
 * en `content/storyboards/cap-N/` para sacar metadatos.
 *
 * Fallback: si la subcarpeta `cap-N/` no existe, lee del dir plano viejo.
 *
 * Ordenamiento estricto: por número de shot ascendente. Los companions sin
 * número (hero, comic-page) van al final.
 */
export async function listStoryboardShots(
  cap: number,
): Promise<StoryboardShot[]> {
  const subdir = path.join(PUBLIC_DIR, "images", "storyboards", `cap-${cap}`);
  const flatdir = path.join(PUBLIC_DIR, "images", "storyboards");
  const prefix = `cap-${cap}-`;

  type Entry = { file: string; image: string; mdDir: string };
  const found: Entry[] = [];

  // 1) Preferimos la subcarpeta cap-N/ (canon nuevo).
  try {
    const entries = await fs.readdir(subdir);
    const subMdDir = path.join(STORYBOARDS_DIR, `cap-${cap}`);
    for (const f of entries) {
      if (!f.toLowerCase().endsWith(".png")) continue;
      if (!f.startsWith(prefix)) continue;
      // Excluir comic-page del listado de shots.
      if (/-comic-page\.png$/i.test(f)) continue;
      found.push({
        file: f,
        image: `/images/storyboards/cap-${cap}/${f}`,
        mdDir: subMdDir,
      });
    }
  } catch {
    // sin subcarpeta — fallback al dir plano abajo.
  }

  // 2) Fallback / merge: dir plano (legacy hero companions sueltos).
  //    Solo agregamos los que no estén ya en la subcarpeta y no sean comic-page.
  try {
    const flatEntries = await fs.readdir(flatdir);
    const known = new Set(found.map((e) => e.file));
    for (const f of flatEntries) {
      if (!f.toLowerCase().endsWith(".png")) continue;
      if (!f.startsWith(prefix)) continue;
      if (/-comic-page\.png$/i.test(f)) continue;
      if (known.has(f)) continue;
      // Si ya tenemos shots numerados de la subcarpeta, ignoramos los
      // hero antiguos del dir plano (no son source of truth).
      if (found.length > 0 && /^cap-\d+-shot-\d+-/.test(f)) {
        // imposible — ya estaría en known. defensivo.
        continue;
      }
      found.push({
        file: f,
        image: `/images/storyboards/${f}`,
        mdDir: STORYBOARDS_DIR,
      });
    }
  } catch {
    // ignorar
  }

  const shots: StoryboardShot[] = [];
  for (const entry of found) {
    const slug = entry.file.replace(/\.png$/i, "");
    const meta = await readShotMeta(slug, entry.mdDir);
    const shotMatch = /^cap-\d+-shot-(\d+)-/.exec(slug);
    const shotNumber = shotMatch ? parseInt(shotMatch[1], 10) : null;

    shots.push({
      slug,
      image: entry.image,
      shotNumber,
      personajes: meta.personajes,
      plano: meta.plano,
      mood: meta.mood,
      caption: meta.caption,
      titulo: meta.titulo,
    });
  }

  // Orden: shots numerados ascendente, después companions sin número alfabético.
  shots.sort((a, b) => {
    if (a.shotNumber !== null && b.shotNumber !== null) {
      return a.shotNumber - b.shotNumber;
    }
    if (a.shotNumber !== null) return -1;
    if (b.shotNumber !== null) return 1;
    return a.slug.localeCompare(b.slug);
  });

  return shots;
}

/**
 * Devuelve el path público de la página cómic compilada del cap, si existe.
 * Busca primero en `public/images/storyboards/cap-N/cap-N-comic-page.png`
 * y luego en el dir plano legado.
 */
async function findComicPage(cap: number): Promise<string | null> {
  const subPath = path.join(
    PUBLIC_DIR,
    "images",
    "storyboards",
    `cap-${cap}`,
    `cap-${cap}-comic-page.png`,
  );
  if (existsSync(subPath)) {
    return `/images/storyboards/cap-${cap}/cap-${cap}-comic-page.png`;
  }
  const flatPath = path.join(
    PUBLIC_DIR,
    "images",
    "storyboards",
    `cap-${cap}-comic-page.png`,
  );
  if (existsSync(flatPath)) {
    return `/images/storyboards/cap-${cap}-comic-page.png`;
  }
  return null;
}

interface ShotMeta {
  titulo: string;
  caption: string;
  personajes: string;
  plano: string;
  mood: string;
}

async function readShotMeta(
  slug: string,
  mdDir: string = STORYBOARDS_DIR,
): Promise<ShotMeta> {
  const fallback: ShotMeta = {
    titulo: slug,
    caption: "",
    personajes: "",
    plano: "",
    mood: "",
  };
  // Buscar en el dir indicado, con fallbacks razonables.
  const candidates = [
    path.join(mdDir, `${slug}.md`),
    path.join(STORYBOARDS_DIR, `${slug}.md`),
  ];
  for (const candidate of candidates) {
    if (!existsSync(candidate)) continue;
    try {
      const raw = await fs.readFile(candidate, "utf8");
      return parseShotMeta(raw, slug);
    } catch {
      // continuar con el siguiente candidato
    }
  }
  return fallback;
}

function parseShotMeta(raw: string, slug: string): ShotMeta {
  // Frontmatter style (cap-1-shot-XX-..., cap-1-hook-..., cap-2-fresco-...)
  const fm = raw.match(/^---\n([\s\S]*?)\n---/);
  let titulo = slug;
  if (fm) {
    const titleMatch = fm[1].match(/^title:\s*"?([^"\n]+)"?/m);
    if (titleMatch) {
      titulo = titleMatch[1].trim();
    } else {
      // shot YAML sin title: tomar el H1 que sigue al frontmatter.
      const h1 = raw.match(/^#\s+(.+)$/m);
      if (h1) titulo = h1[1].trim();
    }
  } else {
    // Plain markdown (cap-2-shot-XX-..., generated by python script)
    const h1 = raw.match(/^#\s+(.+)$/m);
    if (h1) titulo = h1[1].trim();
  }

  // Personajes: línea "**Personajes en frame:**" o sección "## Personajes en frame"
  let personajes = "";
  const persLine = raw.match(/\*\*Personajes en frame:\*\*\s*(.+)/);
  if (persLine) {
    personajes = persLine[1].trim().replace(/[()]/g, "").trim();
  } else {
    const persSection = raw.match(
      /##\s+Personajes en frame\s*\n([\s\S]*?)(?=\n##|\n---|\n```|$)/,
    );
    if (persSection) {
      personajes = persSection[1]
        .split(/\r?\n/)
        .map((l) => l.replace(/^[-*]\s+/, "").trim())
        .filter(Boolean)
        .join(", ");
    }
  }

  // Caption corta = "Accion principal" (cap-1) o primera oración tras SCENE: (cap-2).
  let caption = "";
  const accionSection = raw.match(
    /##\s+Acci[oó]n principal\s*\n+([\s\S]*?)(?=\n##|\n---|$)/i,
  );
  if (accionSection) {
    caption = firstSentence(accionSection[1]);
  } else {
    const beat = raw.match(
      /##\s+Beat narrativo[^\n]*\n+([^\n]+(?:\n[^\n#]+)?)/,
    );
    if (beat) caption = firstSentence(beat[1]);
  }
  // Cap-2: extraer del SCENE dentro del prompt si todavía no tenemos caption.
  if (!caption) {
    const scene = raw.match(/SCENE:\s*([^\n]+)/i);
    if (scene) caption = firstSentence(scene[1]);
  }

  // Plano: cap-1 tiene "## Plano y camara" con bullets; cap-2 trae "SCENE: ...".
  let plano = "";
  const planoSection = raw.match(
    /##\s+Plano y c[aá]mara\s*\n+([\s\S]*?)(?=\n##|\n---|$)/i,
  );
  if (planoSection) {
    // Concatena los bullets "Plano:", "Angulo:", "Lente:" en una línea legible.
    const bullets = planoSection[1]
      .split(/\r?\n/)
      .map((l) => l.replace(/^[-*]\s+/, "").trim())
      .filter(Boolean);
    const useful = bullets.filter((b) =>
      /^(plano|[aá]ngulo|lente|movimiento)\b/i.test(b),
    );
    plano = (useful.length ? useful : bullets).slice(0, 3).join(" · ");
  }
  if (!plano) {
    const compoSection = raw.match(
      /##\s+Composici[oó]n\s*\n+([\s\S]*?)(?=\n##|\n---|$)/i,
    );
    if (compoSection) {
      plano = firstSentence(compoSection[1]);
    }
  }
  if (!plano) {
    // Cap-2 estilo SCENE.
    const sceneMatch = raw.match(/SCENE:\s*([^\.\n]+\.?)/i);
    if (sceneMatch) plano = sceneMatch[1].trim();
  }

  // Mood: "## Tono" (cap-1), "## Paleta dominante" (alt), o fallback "Mood:".
  let mood = "";
  const tonoSection = raw.match(
    /##\s+Tono\s*\n+([\s\S]*?)(?=\n##|\n---|$)/i,
  );
  if (tonoSection) {
    mood = firstSentence(tonoSection[1]);
  }
  if (!mood) {
    const paletteSection = raw.match(
      /##\s+Paleta dominante\s*\n+([\s\S]*?)(?=\n##|\n---|$)/i,
    );
    if (paletteSection) {
      mood = paletteSection[1].replace(/[#`]/g, "").split(/\.\s/)[0].trim();
    }
  }
  if (!mood) {
    const moodMatch = raw.match(/Mood:\s*([^.\n]+)/i);
    if (moodMatch) mood = moodMatch[1].trim();
  }
  if (mood.length > 200) mood = mood.slice(0, 197) + "…";

  return { titulo, caption, personajes, plano, mood };
}

function firstSentence(block: string): string {
  const txt = block.trim().replace(/\s+/g, " ");
  if (!txt) return "";
  const m = txt.match(/^(.+?[\.!?])(?:\s|$)/);
  const out = m ? m[1] : txt;
  return out.length > 240 ? out.slice(0, 237) + "…" : out;
}
