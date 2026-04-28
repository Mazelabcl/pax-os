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
