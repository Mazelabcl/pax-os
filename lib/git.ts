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
