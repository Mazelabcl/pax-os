import { readMarkdown } from "./markdown";

export interface EpisodioTab {
  /** Identificador único usado en el value de la tab. */
  id: string;
  /** Etiqueta visible en la pestaña. */
  label: string;
  /** Path relativo a `content/`. */
  path: string;
  /** Contenido markdown ya leído (sin frontmatter). */
  content: string;
}

export interface EpisodioData {
  /** Título extraído del script (ej. "The Notebook with the Crack"). */
  title: string | null;
  /** Sinopsis 1-línea (extraída del script si está disponible). */
  synopsis: string | null;
  /** Tabs en orden: guion, beat sheet, storyboard, guion técnico. */
  tabs: EpisodioTab[];
}

const TAB_DEFS = [
  { id: "guion", label: "Guion", file: "script.md" },
  { id: "beat-sheet", label: "Beat sheet", file: "beat-sheet.md" },
  { id: "storyboard", label: "Storyboard", file: "storyboard.md" },
  { id: "guion-tecnico", label: "Guion técnico", file: "technical-script.md" },
] as const;

/**
 * Extrae el título del episodio del primer H1 del script.
 * Ej: `# Pax — Episode 1: "The Notebook with the Crack" (v2 — surgical pass)`
 *     → `The Notebook with the Crack`
 */
function parseEpisodeTitle(content: string): string | null {
  const match = content.match(/^#\s+(.+)$/m);
  if (!match) return null;
  const heading = match[1];
  // Buscar texto entre comillas dobles o simples
  const quoted = heading.match(/["“]([^"”]+)["”]/);
  if (quoted) return quoted[1].trim();
  // Fallback: parte después de "Episode N:"
  const epMatch = heading.match(/Episode\s+\d+\s*[:\-—]\s*(.+?)(?:\s*\(|$)/i);
  if (epMatch) return epMatch[1].trim().replace(/^["“]|["”]$/g, "");
  return heading.trim();
}

export async function getEpisodio1(): Promise<EpisodioData> {
  const tabs: EpisodioTab[] = await Promise.all(
    TAB_DEFS.map(async (t) => {
      const path = `episodio-1/${t.file}`;
      const doc = await readMarkdown(path);
      return {
        id: t.id,
        label: t.label,
        path,
        content: doc.content,
      };
    }),
  );

  const scriptContent = tabs.find((t) => t.id === "guion")?.content ?? "";
  const title = parseEpisodeTitle(scriptContent);

  // Sinopsis: línea de "Tone:" o el primer párrafo no-meta
  const toneMatch = scriptContent.match(/^\*\*Tone:\*\*\s*(.+)$/m);
  const synopsis = toneMatch ? toneMatch[1].split(/\.\s+/)[0].trim() : null;

  return { title, synopsis, tabs };
}

export function tabContentPath(tab: EpisodioTab): string {
  return `content/${tab.path}`;
}
