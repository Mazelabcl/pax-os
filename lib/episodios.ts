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

  return {
    ...ep,
    beats,
    hook,
    cliffhanger,
    shots,
    heroImage,
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
 * Lista los shots disponibles para un capítulo. Lee tanto los .png en
 * `public/images/storyboards/` como los .md companions en `content/storyboards/`
 * para sacar metadatos.
 *
 * Ordenamiento: primero los `cap-N-shot-XX-...` por número de shot,
 * después los companion "hero" sin número (cap-N-hook-..., cap-N-clan-council, etc.).
 */
export async function listStoryboardShots(
  cap: number,
): Promise<StoryboardShot[]> {
  const dir = path.join(PUBLIC_DIR, "images", "storyboards");
  let entries: string[] = [];
  try {
    entries = await fs.readdir(dir);
  } catch {
    return [];
  }

  const prefix = `cap-${cap}-`;
  const png = entries
    .filter((f) => f.toLowerCase().endsWith(".png") && f.startsWith(prefix))
    .sort();

  const shots: StoryboardShot[] = [];
  for (const file of png) {
    const slug = file.replace(/\.png$/i, "");
    const image = `/images/storyboards/${file}`;
    const meta = await readShotMeta(slug);

    // shotNumber: cap-N-shot-XX-...
    const shotMatch = /^cap-\d+-shot-(\d+)-/.exec(slug);
    const shotNumber = shotMatch ? parseInt(shotMatch[1], 10) : null;

    shots.push({
      slug,
      image,
      shotNumber,
      personajes: meta.personajes,
      plano: meta.plano,
      mood: meta.mood,
      caption: meta.caption,
      titulo: meta.titulo,
    });
  }

  // Orden: shots numerados primero por número, luego companions sin número.
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

interface ShotMeta {
  titulo: string;
  caption: string;
  personajes: string;
  plano: string;
  mood: string;
}

async function readShotMeta(slug: string): Promise<ShotMeta> {
  const mdPath = path.join(STORYBOARDS_DIR, `${slug}.md`);
  const fallback: ShotMeta = {
    titulo: slug,
    caption: "",
    personajes: "",
    plano: "",
    mood: "",
  };
  if (!existsSync(mdPath)) return fallback;
  try {
    const raw = await fs.readFile(mdPath, "utf8");
    return parseShotMeta(raw, slug);
  } catch {
    return fallback;
  }
}

function parseShotMeta(raw: string, slug: string): ShotMeta {
  // Frontmatter style (cap-1-hook-..., cap-2-fresco-...)
  const fm = raw.match(/^---\n([\s\S]*?)\n---/);
  let titulo = slug;
  if (fm) {
    const titleMatch = fm[1].match(/^title:\s*"?([^"\n]+)"?/m);
    if (titleMatch) titulo = titleMatch[1].trim();
  } else {
    // Plain markdown (cap-2-shot-XX-..., generated by python script)
    const h1 = raw.match(/^#\s+(.+)$/m);
    if (h1) titulo = h1[1].trim();
  }

  // Personajes: linea "**Personajes en frame:**" o YAML "## Personajes en frame"
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

  // Caption corta = beat narrativo o composición
  const beat = raw.match(
    /##\s+Beat narrativo[^\n]*\n+([^\n]+(?:\n[^\n#]+)?)/,
  );
  let caption = "";
  if (beat) {
    caption = beat[1].split(/\.\s/).slice(0, 1).join(". ").trim();
    if (caption && !caption.endsWith(".")) caption += ".";
  }

  // Plano: extraer "lens"/"angle" desde scene description del prompt o composición
  let plano = "";
  const compoSection = raw.match(
    /##\s+Composición\s*\n+([\s\S]*?)(?=\n##|\n---|$)/,
  );
  if (compoSection) {
    const txt = compoSection[1].trim().split(/\.\s/)[0];
    plano = txt.trim();
    if (plano && !plano.endsWith(".")) plano += ".";
  } else {
    // Try shot files: SCENE: ... lens, angle
    const sceneMatch = raw.match(/SCENE:\s*([^\.\n]+(?:[^\.\n]*lens[^\.\n]*)?)/i);
    if (sceneMatch) plano = sceneMatch[1].trim();
  }

  // Mood: paleta dominante o iluminación
  let mood = "";
  const paletteSection = raw.match(
    /##\s+Paleta dominante\s*\n+([\s\S]*?)(?=\n##|\n---|$)/,
  );
  if (paletteSection) {
    mood = paletteSection[1]
      .replace(/[#`]/g, "")
      .split(/\.\s/)[0]
      .trim();
    if (mood.length > 180) mood = mood.slice(0, 177) + "...";
  } else {
    const moodMatch = raw.match(/Mood:\s*([^.\n]+)/i);
    if (moodMatch) mood = moodMatch[1].trim();
  }

  return { titulo, caption, personajes, plano, mood };
}
