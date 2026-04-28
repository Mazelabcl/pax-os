"use client";

import { useState } from "react";
import { Check, Copy } from "lucide-react";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

interface CopyButtonProps {
  /** Texto a copiar al clipboard. */
  text: string;
  /** Etiqueta visible junto al icono. Default: "Copiar". */
  label?: string;
  className?: string;
  variant?: React.ComponentProps<typeof Button>["variant"];
  size?: React.ComponentProps<typeof Button>["size"];
}

/**
 * Botón cliente que copia `text` al clipboard. Feedback: icono Copy → Check 1.5s.
 */
export function CopyButton({
  text,
  label = "Copiar",
  className,
  variant = "outline",
  size = "sm",
}: CopyButtonProps) {
  const [copied, setCopied] = useState(false);

  async function handleCopy() {
    try {
      await navigator.clipboard.writeText(text);
      setCopied(true);
      setTimeout(() => setCopied(false), 1500);
    } catch {
      // Fallback silencioso. Si el browser no soporta clipboard API no rompemos UI.
      setCopied(false);
    }
  }

  return (
    <Button
      type="button"
      variant={variant}
      size={size}
      onClick={handleCopy}
      className={cn("gap-2", className)}
      aria-label={copied ? "Copiado" : label}
    >
      {copied ? (
        <>
          <Check className="size-4" aria-hidden />
          <span>Copiado</span>
        </>
      ) : (
        <>
          <Copy className="size-4" aria-hidden />
          <span>{label}</span>
        </>
      )}
    </Button>
  );
}
