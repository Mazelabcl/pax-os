import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { cn } from "@/lib/utils";

interface VersionToggleProps {
  /** Versión actual que el usuario está viendo. */
  current: "v1" | "v2";
  /** Etiqueta corta que describe qué se está viendo. Ej. "Lore v4 (post-feedback Pipez)". */
  label: string;
  /** Path al que va el toggle (la otra versión). Ej. "/lore" o "/v2/lore". */
  toHref: string;
  /** Texto del botón. Ej. "Volver a V1" o "Ver V2". */
  toLabel: string;
  className?: string;
}

/**
 * Banner sticky-friendly que muestra "Estás viendo: VX — <label>" + botón a la otra versión.
 * Se usa arriba de cada página de /v2/* y, si fuese útil, arriba de las páginas v1.
 */
export function VersionToggle({
  current,
  label,
  toHref,
  toLabel,
  className,
}: VersionToggleProps) {
  const isV2 = current === "v2";
  return (
    <div
      className={cn(
        "mb-6 flex flex-col gap-3 rounded-lg border bg-card p-3 sm:flex-row sm:items-center sm:justify-between",
        isV2 ? "border-fuchsia-500/40" : "border-border",
        className,
      )}
    >
      <div className="flex flex-wrap items-center gap-2 text-sm">
        <Badge
          variant={isV2 ? "secondary" : "outline"}
          className={cn(
            "uppercase tracking-wider",
            isV2 && "bg-fuchsia-500/15 text-fuchsia-200",
          )}
        >
          {isV2 ? "V2" : "V1"}
        </Badge>
        <span className="text-muted-foreground">{label}</span>
      </div>
      <Button asChild variant="outline" size="sm">
        <Link href={toHref}>{toLabel}</Link>
      </Button>
    </div>
  );
}
