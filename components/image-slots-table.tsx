"use client";

import Image from "next/image";
import Link from "next/link";
import { Check, AlertTriangle } from "lucide-react";
import type { ImageSlot } from "@/lib/episodio";
import { cn } from "@/lib/utils";

interface ImageSlotsTableProps {
  slots: ImageSlot[];
  /** Si true, los conceptIds en estado TBD se linkean a `/episodio-1?tab=concept-arts#<id>`. */
  linkConcepts?: boolean;
  /** Título del bloque. Default: "Slots @imageN". */
  title?: string;
}

/**
 * Render visual de la tabla `@imageN` parseada del markdown.
 *
 * - Slots con PNG existente → thumbnail clickeable + check verde.
 * - Slots TBD con conceptId → badge amarillo + link a la tab Concept arts.
 * - Slots sin nada concreto → estado raw como texto plano.
 */
export function ImageSlotsTable({
  slots,
  linkConcepts = true,
  title = "Slots @imageN",
}: ImageSlotsTableProps) {
  if (slots.length === 0) return null;

  return (
    <div className="flex flex-col gap-2">
      <p className="text-xs font-medium uppercase tracking-wide text-muted-foreground">
        {title} ({slots.length})
      </p>
      <ul className="flex flex-col gap-2 rounded-lg border border-border bg-muted/20 p-2">
        {slots.map((s) => (
          <li
            key={s.slot}
            className="flex flex-col gap-2 rounded-md border border-border/60 bg-background/50 p-2 sm:flex-row sm:items-center"
          >
            <div className="flex items-center gap-2">
              <code className="font-mono text-xs text-primary">{s.slot}</code>
              <SlotEstadoBadge estado={s.estado} />
            </div>

            <div className="flex min-w-0 flex-1 items-center gap-2">
              {s.estado === "available" && s.refPath ? (
                <Link
                  href={`/${s.refPath}`}
                  target="_blank"
                  className="group/thumb relative inline-flex shrink-0 items-center gap-2 rounded-md border border-border bg-muted/30 p-1 transition-colors hover:border-primary/60 hover:bg-muted/60"
                  title={s.refPath}
                >
                  <span className="relative block size-10 overflow-hidden rounded bg-background">
                    <Image
                      src={`/${s.refPath}`}
                      alt={s.descripcion}
                      fill
                      sizes="40px"
                      className="object-cover"
                    />
                  </span>
                </Link>
              ) : null}

              <div className="flex min-w-0 flex-col gap-0.5">
                <span className="truncate text-xs leading-tight text-foreground/85">
                  {s.descripcion}
                </span>
                {s.estado === "available" && s.refPath && (
                  <span className="truncate text-[10px] leading-tight text-muted-foreground">
                    public/{s.refPath}
                  </span>
                )}
                {s.estado === "tbd" && s.conceptId && (
                  <span className="truncate text-[10px] leading-tight text-amber-300/80">
                    {linkConcepts ? (
                      <Link
                        href={`/episodio-1?tab=concept-arts#${s.conceptId}`}
                        className="font-mono underline-offset-2 hover:underline"
                      >
                        {s.conceptId}
                      </Link>
                    ) : (
                      <code className="font-mono">{s.conceptId}</code>
                    )}
                  </span>
                )}
                {s.estado === "unknown" && (
                  <span className="truncate text-[10px] leading-tight text-muted-foreground">
                    {s.estadoRaw}
                  </span>
                )}
              </div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

function SlotEstadoBadge({ estado }: { estado: ImageSlot["estado"] }) {
  if (estado === "available") {
    return (
      <span
        className={cn(
          "inline-flex items-center gap-1 rounded-md border px-1.5 py-0.5 text-[10px] font-medium uppercase tracking-wide",
          "border-emerald-500/40 bg-emerald-500/10 text-emerald-300",
        )}
      >
        <Check className="size-3" aria-hidden />
        Disponible
      </span>
    );
  }
  if (estado === "tbd") {
    return (
      <span
        className={cn(
          "inline-flex items-center gap-1 rounded-md border px-1.5 py-0.5 text-[10px] font-medium uppercase tracking-wide",
          "border-amber-500/40 bg-amber-500/10 text-amber-300",
        )}
      >
        <AlertTriangle className="size-3" aria-hidden />
        Generar primero
      </span>
    );
  }
  return (
    <span className="inline-flex items-center rounded-md border border-border px-1.5 py-0.5 text-[10px] font-medium uppercase tracking-wide text-muted-foreground">
      ?
    </span>
  );
}
