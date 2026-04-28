import { readMarkdown } from "./markdown";

export interface ChangelogEntry {
  /** Heading completo del entry (sin el `## `). */
  heading: string;
  /** Fecha como string (lo que esté antes de "—"), ej. "2026-04-28". */
  date: string | null;
  /** Título de la sesión (lo que esté después de "—"). */
  title: string;
  /** Bullets del entry. */
  bullets: string[];
}

/**
 * Parsea `content/CHANGELOG.md` en entries (cada `## ` arranca uno).
 * Los entries vienen en el orden del archivo (más reciente primero por convención).
 */
export async function getChangelogEntries(): Promise<ChangelogEntry[]> {
  const doc = await readMarkdown("CHANGELOG.md");
  return parseChangelog(doc.content);
}

export function parseChangelog(content: string): ChangelogEntry[] {
  const lines = content.split(/\r?\n/);
  const entries: ChangelogEntry[] = [];
  let current: ChangelogEntry | null = null;

  for (const line of lines) {
    const h2 = /^##\s+(.+?)\s*$/.exec(line);
    if (h2) {
      if (current) entries.push(current);
      const heading = h2[1].trim();
      const sep = heading.match(/^(\S+)\s+[—\-–]\s+(.+)$/);
      current = {
        heading,
        date: sep ? sep[1] : null,
        title: sep ? sep[2] : heading,
        bullets: [],
      };
      continue;
    }
    if (!current) continue;

    const bullet = /^[-*]\s+(.+)$/.exec(line);
    if (bullet) {
      current.bullets.push(bullet[1].trim());
    }
  }
  if (current) entries.push(current);

  return entries;
}
