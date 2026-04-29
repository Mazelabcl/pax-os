"use client";

import { useState } from "react";
import { ChevronDown } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { cn } from "@/lib/utils";
import type { Escena } from "@/lib/episodio";

interface EscenaCardProps {
  escena: Escena;
  /** Si true, arranca abierta. Default: false (mobile-friendly). */
  defaultOpen?: boolean;
}

export function EscenaCard({ escena, defaultOpen = false }: EscenaCardProps) {
  const [open, setOpen] = useState(defaultOpen);

  return (
    <Card>
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        className="text-left"
        aria-expanded={open}
      >
        <CardHeader className="gap-2">
          <div className="flex items-center justify-between gap-3">
            <div className="flex flex-wrap items-center gap-2">
              <Badge variant="secondary" className="font-mono text-xs">
                {escena.numero}
              </Badge>
              {escena.duracion && (
                <Badge variant="outline" className="text-xs font-normal">
                  {escena.duracion}
                </Badge>
              )}
              <CardTitle className="text-base leading-snug sm:text-lg">
                {escena.titulo}
              </CardTitle>
            </div>
            <ChevronDown
              className={cn(
                "size-4 shrink-0 text-muted-foreground transition-transform",
                open && "rotate-180",
              )}
              aria-hidden
            />
          </div>
          {escena.beat && (
            <p className="text-xs text-muted-foreground sm:text-sm">
              {escena.beat}
            </p>
          )}
        </CardHeader>
      </button>
      {open && (
        <CardContent className="flex flex-col gap-3 border-t border-border pt-4 text-sm">
          {escena.ubicacion && (
            <Field label="Ubicación" value={escena.ubicacion} />
          )}
          {escena.personajes && (
            <Field label="Personajes" value={escena.personajes} />
          )}
          {escena.mood && <Field label="Mood" value={escena.mood} />}
          {escena.descripcion && (
            <Field label="Descripción" value={escena.descripcion} multiline />
          )}
          {escena.dialogo && (
            <Field label="Diálogo / sonido" value={escena.dialogo} multiline />
          )}
        </CardContent>
      )}
    </Card>
  );
}

function Field({
  label,
  value,
  multiline,
}: {
  label: string;
  value: string;
  multiline?: boolean;
}) {
  return (
    <div className="flex flex-col gap-1">
      <span className="text-xs font-medium uppercase tracking-wide text-muted-foreground">
        {label}
      </span>
      <p
        className={cn(
          "leading-relaxed text-foreground/90",
          multiline ? "whitespace-pre-wrap" : "",
        )}
      >
        {value}
      </p>
    </div>
  );
}
