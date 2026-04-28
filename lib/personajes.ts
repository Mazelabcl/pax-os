import path from "node:path";
import { promises as fs } from "node:fs";
import { listMarkdownFiles, readMarkdown } from "./markdown";

export interface PersonajeFrontmatter {
  name?: string;
  slug?: string;
  image?: string;
  seed?: string | number;
}

export interface PersonajeSummary {
  /** Slug derivado del nombre del archivo (sin `.md`). */
  slug: string;
  /** Nombre visible (frontmatter o capitalizado del slug). */
  name: string;
  /** Path public absoluto a la imagen (ej. `/images/personajes/jiggy.png`). */
  image: string | null;
  /** Descripción corta de 1 línea — primer párrafo de la sección "## Descripción". */
  shortDescription: string;
  /** Frontmatter parseado (todo). */
  frontmatter: PersonajeFrontmatter;
}

export interface PersonajeDetail extends PersonajeSummary {
  /** Markdown crudo (sin frontmatter). */
  content: string;
  /** Path absoluto del archivo. */
  absolutePath: string;
  /** Path relativo a `content/`. */
  relativePath: string;
  /** Texto completo dentro del primer code block después de "Prompt visual". */
  prompt: string | null;
  /** "Rol en la historia" como texto plano. */
  rol: string | null;
  /** "Marca distintiva [visual]" como texto plano. */
  marca: string | null;
  /** "Descripción" completa como texto plano (para detalle). */
  descripcion: string | null;
  /** Seed canónica si existe en frontmatter. */
  seed: string | null;
}

/**
 * Filtra los archivos del directorio `content/personajes/` excluyendo:
 * - Los que arrancan con `_` (canon, notas internas).
 * - `mariela-prompt.md` (prompt auxiliar, no es ficha de personaje).
 */
export async function listPersonajeSlugs(): Promise<string[]> {
  const files = await listMarkdownFiles("personajes");
  return files
    .filter((f) => !f.startsWith("_") && f !== "mariela-prompt.md")
    .map((f) => f.replace(/\.md$/, ""));
}

/**
 * Extrae el cuerpo de una sección por su heading H2 (`## Titulo`).
 * Devuelve el texto plano del primer párrafo (hasta línea en blanco o siguiente heading).
 */
function extractSectionFirstParagraph(
  content: string,
  headingPattern: RegExp,
): string | null {
  const lines = content.split(/\r?\n/);
  let i = 0;
  while (i < lines.length) {
    if (/^##\s+/.test(lines[i]) && headingPattern.test(lines[i])) {
      i++;
      // Saltar líneas en blanco
      while (i < lines.length && lines[i].trim() === "") i++;
      const buf: string[] = [];
      while (
        i < lines.length &&
        lines[i].trim() !== "" &&
        !/^#{1,6}\s+/.test(lines[i])
      ) {
        buf.push(lines[i]);
        i++;
      }
      const text = buf.join(" ").trim();
      return text || null;
    }
    i++;
  }
  return null;
}

/**
 * Extrae todo el cuerpo de una sección H2 (sin incluir el heading) hasta el siguiente
 * heading del mismo o mayor nivel.
 */
function extractSectionBody(
  content: string,
  headingPattern: RegExp,
): string | null {
  const lines = content.split(/\r?\n/);
  let i = 0;
  while (i < lines.length) {
    if (/^##\s+/.test(lines[i]) && headingPattern.test(lines[i])) {
      i++;
      const buf: string[] = [];
      while (i < lines.length && !/^##\s+/.test(lines[i])) {
        buf.push(lines[i]);
        i++;
      }
      return buf.join("\n").trim() || null;
    }
    i++;
  }
  return null;
}

/**
 * Extrae el primer code block (triple backtick) que aparezca después del heading
 * "Prompt visual …". Si no hay heading, intenta el primer code block del documento.
 */
function extractPromptVisual(content: string): string | null {
  // Buscamos a partir del heading "Prompt visual"
  const idx = content.search(/^##\s+Prompt visual/m);
  const slice = idx >= 0 ? content.slice(idx) : content;
  const match = slice.match(/```[a-z]*\s*\r?\n([\s\S]*?)```/);
  return match ? match[1].trim() : null;
}

/**
 * Capitaliza un slug "byte" → "Byte".
 */
function titleFromSlug(slug: string): string {
  return slug.charAt(0).toUpperCase() + slug.slice(1);
}

export async function getPersonajeSummary(
  slug: string,
): Promise<PersonajeSummary | null> {
  try {
    const doc = await readMarkdown<PersonajeFrontmatter>(
      `personajes/${slug}.md`,
    );
    const fm = doc.frontmatter ?? {};
    const name = fm.name ?? titleFromSlug(slug);
    const image = fm.image ?? null;
    const shortDescription =
      extractSectionFirstParagraph(doc.content, /Descripción/i) ?? "";

    return {
      slug,
      name,
      image,
      shortDescription,
      frontmatter: fm,
    };
  } catch {
    return null;
  }
}

export async function getPersonajeDetail(
  slug: string,
): Promise<PersonajeDetail | null> {
  try {
    const doc = await readMarkdown<PersonajeFrontmatter>(
      `personajes/${slug}.md`,
    );
    const fm = doc.frontmatter ?? {};
    const name = fm.name ?? titleFromSlug(slug);
    const image = fm.image ?? null;
    const shortDescription =
      extractSectionFirstParagraph(doc.content, /Descripción/i) ?? "";
    const descripcion = extractSectionBody(doc.content, /Descripción/i);
    const rol = extractSectionBody(doc.content, /Rol en la historia/i);
    const marca = extractSectionBody(
      doc.content,
      /Marca distintiva(?:\s+visual)?/i,
    );
    const prompt = extractPromptVisual(doc.content);
    const seed =
      fm.seed !== undefined && fm.seed !== null ? String(fm.seed) : null;

    return {
      slug,
      name,
      image,
      shortDescription,
      frontmatter: fm,
      content: doc.content,
      absolutePath: doc.absolutePath,
      relativePath: doc.relativePath,
      prompt,
      rol,
      marca,
      descripcion,
      seed,
    };
  } catch {
    return null;
  }
}

export async function listPersonajeSummaries(): Promise<PersonajeSummary[]> {
  const slugs = await listPersonajeSlugs();
  const all = await Promise.all(slugs.map(getPersonajeSummary));
  return all.filter((p): p is PersonajeSummary => p !== null);
}

/**
 * Path relativo (al cwd del repo) del archivo de personaje. Útil para `getLastUpdated`.
 */
export function personajeFilePath(slug: string): string {
  return path.posix.join("content", "personajes", `${slug}.md`);
}

/**
 * Verifica si un archivo en disco existe (path relativo al cwd o absoluto).
 */
export async function fileExists(filePath: string): Promise<boolean> {
  try {
    await fs.access(filePath);
    return true;
  } catch {
    return false;
  }
}
