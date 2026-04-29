"use client";

import Image from "next/image";
import Link from "next/link";
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

interface PromptCardProps {
  numero: string;
  titulo: string;
  beat: string | null;
  /** Paths relativos a `public/`. */
  refs: string[];
  prompt: string;
  negative: string | null;
  /** Texto completo (style-lock + refs + prompt + negative) ya armado server-side. */
  fullCopy: string;
  notas: string | null;
  audio: string | null;
  /** Etiqueta del badge inicial: "Nano" / "Seedance" / etc. */
  badge?: string;
}

export function PromptCard({
  numero,
  titulo,
  beat,
  refs,
  prompt,
  negative,
  fullCopy,
  notas,
  audio,
  badge,
}: PromptCardProps) {
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
    <Card className="overflow-visible">
      <CardHeader className="gap-2">
        <div className="flex flex-wrap items-center gap-2">
          <Badge variant="secondary" className="font-mono text-xs">
            {numero}
          </Badge>
          {badge && (
            <Badge variant="outline" className="text-xs font-normal">
              {badge}
            </Badge>
          )}
          <CardTitle className="text-base sm:text-lg">{titulo}</CardTitle>
        </div>
        {beat && (
          <p className="text-xs text-muted-foreground sm:text-sm">{beat}</p>
        )}
      </CardHeader>
      <CardContent className="flex flex-col gap-3">
        {refs.length > 0 && (
          <div className="flex flex-col gap-2">
            <p className="text-xs font-medium uppercase tracking-wide text-muted-foreground">
              Reference images ({refs.length})
            </p>
            <div className="flex flex-wrap gap-2">
              {refs.map((ref) => (
                <Link
                  key={ref}
                  href={`/${ref}`}
                  target="_blank"
                  className="group/thumb relative inline-flex items-center gap-2 rounded-md border border-border bg-muted/30 p-1.5 pr-3 transition-colors hover:border-primary/60 hover:bg-muted/60"
                  title={ref}
                >
                  <span className="relative block size-12 overflow-hidden rounded bg-background sm:size-14">
                    <Image
                      src={`/${ref}`}
                      alt={ref}
                      fill
                      sizes="56px"
                      className="object-cover"
                    />
                  </span>
                  <span className="hidden text-[11px] leading-tight text-muted-foreground group-hover/thumb:text-foreground sm:inline">
                    {ref.split("/").pop()}
                  </span>
                </Link>
              ))}
            </div>
          </div>
        )}

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
        </div>

        {open && (
          <div className="flex flex-col gap-3 border-t border-border pt-3">
            <details className="rounded-md border border-border bg-muted/20" open>
              <summary className="cursor-pointer px-3 py-2 text-xs font-medium uppercase tracking-wide text-muted-foreground">
                Prompt principal
              </summary>
              <pre className="overflow-x-auto whitespace-pre-wrap break-words border-t border-border bg-muted/10 px-3 py-3 text-xs leading-relaxed">
                {prompt}
              </pre>
            </details>
            {negative && (
              <details className="rounded-md border border-border bg-muted/20">
                <summary className="cursor-pointer px-3 py-2 text-xs font-medium uppercase tracking-wide text-muted-foreground">
                  Negative prompt
                </summary>
                <pre className="overflow-x-auto whitespace-pre-wrap break-words border-t border-border bg-muted/10 px-3 py-3 text-xs leading-relaxed">
                  {negative}
                </pre>
              </details>
            )}
            {audio && (
              <details className="rounded-md border border-border bg-muted/20">
                <summary className="cursor-pointer px-3 py-2 text-xs font-medium uppercase tracking-wide text-muted-foreground">
                  Audio
                </summary>
                <div className="border-t border-border bg-muted/10 px-3 py-3 text-xs leading-relaxed whitespace-pre-wrap">
                  {audio}
                </div>
              </details>
            )}
            {notas && (
              <details className="rounded-md border border-border bg-muted/20">
                <summary className="cursor-pointer px-3 py-2 text-xs font-medium uppercase tracking-wide text-muted-foreground">
                  Notas de dirección
                </summary>
                <div className="border-t border-border bg-muted/10 px-3 py-3 text-xs leading-relaxed whitespace-pre-wrap">
                  {notas}
                </div>
              </details>
            )}
          </div>
        )}
      </CardContent>
    </Card>
  );
}
