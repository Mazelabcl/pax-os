import { promises as fs } from "node:fs";
import path from "node:path";
import matter from "gray-matter";

const CONTENT_ROOT = path.join(/* turbopackIgnore: true */ process.cwd(), "content");

export interface MarkdownDoc<TFrontmatter = Record<string, unknown>> {
  /** Path relativo al directorio `content/` (ej. `lore.md`). */
  relativePath: string;
  /** Path absoluto del archivo en disco. */
  absolutePath: string;
  /** Frontmatter parseado. Vacío si el archivo no tiene. */
  frontmatter: TFrontmatter;
  /** Cuerpo del markdown sin el frontmatter. */
  content: string;
}

/**
 * Lee un archivo markdown del directorio `content/` y devuelve frontmatter + cuerpo.
 * @param relativePath path relativo a `content/` usando forward slashes (ej. `episodio-1/script.md`).
 */
export async function readMarkdown<TFrontmatter = Record<string, unknown>>(
  relativePath: string,
): Promise<MarkdownDoc<TFrontmatter>> {
  const normalized = relativePath.replace(/^[/\\]+/, "");
  const absolutePath = path.join(CONTENT_ROOT, normalized);
  const raw = await fs.readFile(absolutePath, "utf8");
  const parsed = matter(raw);

  return {
    relativePath: normalized,
    absolutePath,
    frontmatter: parsed.data as TFrontmatter,
    content: parsed.content,
  };
}

/**
 * Lista todos los `.md` en un subdirectorio de `content/` (no recursivo).
 * @param subdir subdirectorio relativo a `content/` (ej. `personajes`).
 */
export async function listMarkdownFiles(subdir: string): Promise<string[]> {
  const dir = path.join(CONTENT_ROOT, subdir);
  const entries = await fs.readdir(dir, { withFileTypes: true });
  return entries
    .filter((entry) => entry.isFile() && entry.name.endsWith(".md"))
    .map((entry) => entry.name)
    .sort();
}

export interface TocItem {
  /** Texto visible del heading. */
  text: string;
  /** Slug que debe coincidir con el id generado por rehype-slug. */
  slug: string;
  /** 1-6 según el nivel del heading. */
  level: number;
}

/**
 * Slugify alineado con `github-slugger` (lo que usa rehype-slug por debajo).
 * Implementación mínima: minúsculas, sin acentos, espacios y símbolos a guion.
 */
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

/**
 * Extrae headings ATX (`#`, `##`, …) de un markdown, ignorando los que estén
 * dentro de bloques de código triple-backtick.
 *
 * @param content cuerpo del markdown sin frontmatter.
 * @param maxLevel nivel máximo a incluir (default 3 — solo h1/h2/h3 en TOC).
 */
export function extractToc(content: string, maxLevel = 3): TocItem[] {
  const lines = content.split(/\r?\n/);
  const toc: TocItem[] = [];
  const seen = new Map<string, number>();
  let inCodeBlock = false;

  for (const line of lines) {
    if (/^```/.test(line)) {
      inCodeBlock = !inCodeBlock;
      continue;
    }
    if (inCodeBlock) continue;

    const match = /^(#{1,6})\s+(.+?)\s*#*\s*$/.exec(line);
    if (!match) continue;

    const level = match[1].length;
    if (level > maxLevel) continue;

    const text = match[2].trim();
    let slug = slugify(text);
    if (!slug) continue;

    // github-slugger desambigua agregando -1, -2 … cuando hay duplicados.
    const count = seen.get(slug) ?? 0;
    if (count > 0) slug = `${slug}-${count}`;
    seen.set(slugify(text), count + 1);

    toc.push({ text, slug, level });
  }

  return toc;
}
