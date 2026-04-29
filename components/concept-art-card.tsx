"use client";

import { useState } from "react";
import { Check, Copy, ChevronDown } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { cn } from "@/lib/utils";
import { ImageSlotsTable } from "@/components/image-slots-table";
import type { ConceptArt } from "@/lib/episodio";

interface ConceptArtCardProps {
  art: ConceptArt;
  /** Posición numerada en el orden de generación global (1-30). null si no aplica. */
  ordenNum: number | null;
  /** Texto completo (style-lock + slots + prompt) ya armado server-side. */
  fullCopy: string;
}

const TIPO_COLORS: Record<ConceptArt["tipo"], string> = {
  HERO: "border-fuchsia-500/40 bg-fuchsia-500/10 text-fuchsia-200",
  DERIVADO: "border-cyan-500/40 bg-cyan-500/10 text-cyan-200",
  "FIRST-FRAME": "border-amber-500/40 bg-amber-500/10 text-amber-200",
};

export function ConceptArtCard({ art, ordenNum, fullCopy }: ConceptArtCardProps) {
  const [copied, setCopied] = useState(false);
  const [open, setOpen] = useState(false);

  async function handleCopy() {
    try {
      await navigator.clipboard.writeText(fullCopy);
      setCopied(true);
      setTimeout(() => setCopied(false), 1800);
    } catch {
      setCopied(false);
    }
  }

  return (
    <Card id={art.id} className="scroll-mt-28 overflow-visible">
      <CardHeader className="gap-2">
        <div className="flex flex-wrap items-center gap-2">
          {ordenNum !== null && (
            <Badge variant="secondary" className="font-mono text-xs">
              #{String(ordenNum).padStart(2, "0")}
            </Badge>
          )}
          <span
            className={cn(
              "inline-flex items-center rounded-md border px-1.5 py-0.5 text-[10px] font-medium uppercase tracking-wide",
              TIPO_COLORS[art.tipo],
            )}
          >
            {art.tipo}
          </span>
          <Badge variant="outline" className="text-[10px] font-normal uppercase tracking-wide">
            Bloque {art.bloque}
          </Badge>
          <CardTitle className="font-mono text-sm sm:text-base">
            {art.id}
          </CardTitle>
        </div>
        {art.aliases.length > 0 && (
          <p className="text-xs text-muted-foreground">
            <span className="font-medium">Aliases:</span>{" "}
            {art.aliases.map((a, i) => (
              <span key={a}>
                <code className="font-mono">{a}</code>
                {i < art.aliases.length - 1 ? ", " : ""}
              </span>
            ))}
          </p>
        )}
        {art.derivaDe && (
          <p className="text-xs text-muted-foreground">
            <span className="font-medium">Deriva de:</span>{" "}
            <code className="font-mono text-cyan-300/80">{art.derivaDe}</code>
          </p>
        )}
      </CardHeader>
      <CardContent className="flex flex-col gap-3">
        {(art.apareceStoryboard || art.apareceSeedance || art.paraClip) && (
          <div className="flex flex-col gap-1 text-xs text-foreground/80 sm:text-sm">
            {art.apareceStoryboard && (
              <p>
                <span className="font-medium text-muted-foreground">
                  Aparece en (storyboard):
                </span>{" "}
                {art.apareceStoryboard}
              </p>
            )}
            {art.apareceSeedance && (
              <p>
                <span className="font-medium text-muted-foreground">
                  Aparece en (Seedance):
                </span>{" "}
                {art.apareceSeedance}
              </p>
            )}
            {art.paraClip && (
              <p>
                <span className="font-medium text-muted-foreground">Para:</span>{" "}
                {art.paraClip}
              </p>
            )}
          </div>
        )}

        <ImageSlotsTable
          slots={art.slots}
          title="Reference images requeridas"
          linkConcepts
        />

        <div className="flex flex-wrap items-center gap-2">
          <Button
            type="button"
            size="sm"
            onClick={handleCopy}
            className="gap-2"
            aria-label={copied ? "Copiado" : "Copiar prompt completo"}
          >
            {copied ? (
              <>
                <Check className="size-4" aria-hidden />
                Copiado
              </>
            ) : (
              <>
                <Copy className="size-4" aria-hidden />
                Copiar prompt completo
              </>
            )}
          </Button>
          <Button
            type="button"
            variant="ghost"
            size="sm"
            onClick={() => setOpen((v) => !v)}
            className="gap-1"
          >
            <ChevronDown
              className={cn(
                "size-4 transition-transform",
                open && "rotate-180",
              )}
              aria-hidden
            />
            {open ? "Ocultar detalle" : "Ver detalle"}
          </Button>
          <span className="text-[10px] uppercase tracking-wide text-muted-foreground">
            Estado: pendiente generar
          </span>
        </div>

        {open && (
          <div className="flex flex-col gap-3 border-t border-border pt-3">
            <details className="rounded-md border border-border bg-muted/20" open>
              <summary className="cursor-pointer px-3 py-2 text-xs font-medium uppercase tracking-wide text-muted-foreground">
                Prompt Nano Banana
              </summary>
              <pre className="overflow-x-auto whitespace-pre-wrap break-words border-t border-border bg-muted/10 px-3 py-3 text-xs leading-relaxed">
                {art.prompt}
              </pre>
            </details>
            {art.notas && (
              <details className="rounded-md border border-border bg-muted/20">
                <summary className="cursor-pointer px-3 py-2 text-xs font-medium uppercase tracking-wide text-muted-foreground">
                  Notas de generación
                </summary>
                <div className="border-t border-border bg-muted/10 px-3 py-3 text-xs leading-relaxed whitespace-pre-wrap">
                  {art.notas}
                </div>
              </details>
            )}
          </div>
        )}
      </CardContent>
    </Card>
  );
}

// TODO(tracking): persistir estado "generado" via localStorage cuando aldot
// pida iteración futura. Por ahora todos los concept-arts arrancan como
// "pendiente generar". Endpoint sugerido: `useLocalStorage("pax-concept-${id}")`
// dentro de este componente para toggle ✓ / pendiente.
