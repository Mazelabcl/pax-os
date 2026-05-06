import { exec } from "node:child_process";
import { promisify } from "node:util";
import path from "node:path";

const execAsync = promisify(exec);

const REPO_ROOT = /* turbopackIgnore: true */ process.cwd();

const MESES_ES = [
  "ene",
  "feb",
  "mar",
  "abr",
  "may",
  "jun",
  "jul",
  "ago",
  "sep",
  "oct",
  "nov",
  "dic",
];

/**
 * Obtiene la fecha del último commit que tocó el archivo dado, formateada en español.
 * Devuelve `null` si el archivo no está trackeado o si git no está disponible.
 *
 * @param filePath path absoluto o relativo al cwd del proceso.
 * @returns string como `12 abr 2026` o `null`.
 */
export async function getLastUpdated(filePath: string): Promise<string | null> {
  try {
    const absolute = path.isAbsolute(filePath)
      ? filePath
      : path.join(REPO_ROOT, filePath);

    // ISO date para no depender de locale del sistema. La traducimos abajo.
    const { stdout } = await execAsync(
      `git log -1 --format=%cI -- "${absolute}"`,
      { cwd: REPO_ROOT },
    );

    const iso = stdout.trim();
    if (!iso) return null;

    const date = new Date(iso);
    if (Number.isNaN(date.getTime())) return null;

    const dia = date.getDate();
    const mes = MESES_ES[date.getMonth()];
    const anio = date.getFullYear();

    return `${dia} ${mes} ${anio}`;
  } catch {
    return null;
  }
}

/**
 * Obtiene la fecha del último commit que tocó cualquier archivo bajo el path dado
 * (ej. un directorio con `content/personajes` cubre todos los `.md` y assets relacionados
 * dentro). Devuelve string formateado en español o `null`.
 */
export async function getLastUpdatedAny(
  paths: string[],
): Promise<string | null> {
  if (paths.length === 0) return null;
  try {
    const quoted = paths
      .map((p) => {
        const absolute = path.isAbsolute(p) ? p : path.join(REPO_ROOT, p);
        return `"${absolute}"`;
      })
      .join(" ");

    const { stdout } = await execAsync(
      `git log -1 --format=%cI -- ${quoted}`,
      { cwd: REPO_ROOT },
    );

    const iso = stdout.trim();
    if (!iso) return null;

    const date = new Date(iso);
    if (Number.isNaN(date.getTime())) return null;

    const dia = date.getDate();
    const mes = MESES_ES[date.getMonth()];
    const anio = date.getFullYear();

    return `${dia} ${mes} ${anio}`;
  } catch {
    return null;
  }
}

// =============================================================================
// Recent commits — para sección "Actos de la tribu" en la home
// =============================================================================

export type CommitKind = "feat" | "fix" | "chore" | "other";

export interface RecentCommit {
  /** Hash corto (7 chars). */
  hash: string;
  /** Tipo extraído del prefix conventional commits. */
  kind: CommitKind;
  /** Subject sin el prefix (ej. "agrega sección X"). */
  subject: string;
  /** Subject capitalizado para mostrar como título. */
  title: string;
  /** Fecha relativa en español (ej. "hace 2 horas"). */
  relative: string;
  /** Frase narrativa Pax-themed (ej. "alguien donó atención y mejoró X"). */
  narrative: string;
  /** ISO date para sort/debug. */
  isoDate: string;
}

/**
 * Lista los últimos commits del repo, filtrando merges y commits "wip".
 * Devuelve cada commit enriquecido con su narrativa Pax-themed.
 *
 * @param limit cantidad máxima a retornar (default 15).
 */
export async function getRecentCommits(
  limit = 15,
): Promise<RecentCommit[]> {
  try {
    // Formato: hash corto | iso date | subject completo
    // Separador unicode poco común para evitar conflicto con texto del subject.
    const SEP = "␟"; // unit separator visible
    const fetchCount = limit * 3 + 5; // sobre-piditmos para filtrar despues
    const { stdout } = await execAsync(
      `git log -n ${fetchCount} --no-merges --format=%h${SEP}%cI${SEP}%s`,
      { cwd: REPO_ROOT },
    );

    const lines = stdout.split(/\r?\n/).filter(Boolean);
    const commits: RecentCommit[] = [];

    for (const line of lines) {
      const [hash, iso, subjectRaw] = line.split(SEP);
      if (!hash || !iso || !subjectRaw) continue;

      const subjectClean = subjectRaw.trim();
      // Filtrar wip / drafts.
      if (/^wip\b/i.test(subjectClean)) continue;
      if (/^draft\b/i.test(subjectClean)) continue;

      const { kind, subject } = parseConventional(subjectClean);
      // Solo mostramos feat / fix / chore. "other" lo saltamos para mantener el
      // muro narrativo (no caer en housekeeping casual).
      if (kind === "other") continue;

      const date = new Date(iso);
      const relative = formatRelative(date);
      const title = capitalize(subject);
      const narrative = buildNarrative(kind, subject);

      commits.push({
        hash,
        kind,
        subject,
        title,
        relative,
        narrative,
        isoDate: iso,
      });

      if (commits.length >= limit) break;
    }

    return commits;
  } catch {
    return [];
  }
}

/**
 * Parsea un subject con prefix conventional commits ("feat:", "fix:", "chore:").
 * Si no hay prefix reconocido, retorna kind "other" con el subject íntegro.
 */
function parseConventional(raw: string): {
  kind: CommitKind;
  subject: string;
} {
  const m = /^(feat|fix|chore|docs|refactor|perf|test|build|ci|style)(?:\([^)]*\))?:\s*(.+)$/i.exec(
    raw,
  );
  if (!m) {
    return { kind: "other", subject: raw };
  }
  const prefix = m[1].toLowerCase();
  const subject = m[2].trim();
  if (prefix === "feat") return { kind: "feat", subject };
  if (prefix === "fix") return { kind: "fix", subject };
  if (prefix === "chore") return { kind: "chore", subject };
  // docs/refactor/perf/test/etc lo tratamos como "other" para no inflar el muro.
  return { kind: "other", subject };
}

function capitalize(s: string): string {
  if (!s) return s;
  return s.charAt(0).toUpperCase() + s.slice(1);
}

/**
 * Convierte una fecha en string relativa en español neutro.
 * Ej. "hace 5 minutos", "hace 2 horas", "hace 3 días", "hace 2 semanas",
 * "hace 1 mes", "hace 6 meses". Para >12 meses cae a "hace N años".
 */
function formatRelative(date: Date): string {
  const now = Date.now();
  const diffMs = now - date.getTime();
  if (diffMs < 0) return "ahora";

  const sec = Math.floor(diffMs / 1000);
  if (sec < 60) return "hace unos segundos";
  const min = Math.floor(sec / 60);
  if (min < 60) return min === 1 ? "hace 1 minuto" : `hace ${min} minutos`;
  const hr = Math.floor(min / 60);
  if (hr < 24) return hr === 1 ? "hace 1 hora" : `hace ${hr} horas`;
  const day = Math.floor(hr / 24);
  if (day < 7) return day === 1 ? "hace 1 día" : `hace ${day} días`;
  const week = Math.floor(day / 7);
  if (week < 4) return week === 1 ? "hace 1 semana" : `hace ${week} semanas`;
  const month = Math.floor(day / 30);
  if (month < 12) return month === 1 ? "hace 1 mes" : `hace ${month} meses`;
  const year = Math.floor(day / 365);
  return year === 1 ? "hace 1 año" : `hace ${year} años`;
}

// =============================================================================
// Narrativa Pax-themed (heurística por keywords, sin LLM)
// =============================================================================

/**
 * Devuelve una micro-narrativa "Pax-themed" para un commit. La forma es:
 *   "alguien {VERBO_DONO} {RECURSO} y {VERBO_EFECTO} {RESUMEN}"
 *
 * - El verbo de aporte (donó / sostuvo / cargó) y el recurso (atención, tiempo,
 *   cuidado) se eligen por hash determinístico para variar entre commits.
 * - El verbo de efecto se elige por kind (feat = "abrió/sumó", fix = "ajustó/curó",
 *   chore = "ordenó/limpió").
 * - El resumen es el subject del commit, simplificado para que la frase fluya.
 */
function buildNarrative(kind: CommitKind, subject: string): string {
  const resumen = simplifySubject(subject);

  // Pseudo-random determinista basado en el primer char del subject.
  // Así misma frase = misma narrativa entre renders.
  const seed = subject.charCodeAt(0) || 0;

  const aportes = [
    "donó atención",
    "sostuvo el ritmo",
    "cargó un cristal",
    "puso cuidado",
    "encendió una chispa",
  ];
  const aporte = aportes[seed % aportes.length];

  const efectoFeat = ["sumó al sistema", "abrió un nuevo gesto", "extendió la red"];
  const efectoFix = ["curó una grieta", "ajustó el flujo", "estabilizó la red"];
  const efectoChore = ["ordenó la cueva", "limpió un rincón", "afinó el sistema"];

  let efecto: string;
  if (kind === "feat") efecto = efectoFeat[seed % efectoFeat.length];
  else if (kind === "fix") efecto = efectoFix[seed % efectoFix.length];
  else efecto = efectoChore[seed % efectoChore.length];

  return `Alguien ${aporte} y ${efecto}: ${resumen}.`;
}

/**
 * Simplifica el subject para usar dentro de una frase narrativa.
 * - Quita comillas, paréntesis sobrantes, punto final.
 * - Lo deja en minúsculas (la primera letra de la oración la pone "Alguien").
 * - Recorta a ~80 chars con elipsis si pasa.
 */
function simplifySubject(subject: string): string {
  let s = subject.trim();
  s = s.replace(/[.!?]+$/g, "");
  s = s.toLowerCase();
  if (s.length > 80) s = s.slice(0, 77).replace(/\s+\S*$/, "") + "…";
  return s;
}
