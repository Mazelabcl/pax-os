import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import remarkToc from "remark-toc";
import rehypeSlug from "rehype-slug";
import type { ComponentProps } from "react";
import { cn } from "@/lib/utils";

interface MarkdownRendererProps {
  children: string;
  className?: string;
}

/**
 * Imagen markdown renderizada como `<figure>` + `<figcaption>` cuando tiene alt.
 * El alt text del markdown (`![alt](src)`) se usa como caption visible debajo de
 * la imagen. Sirve para ilustrar pitch/lore con captions narrativos.
 *
 * Nota: usamos `<img>` nativo (no `next/image`) porque (a) las imágenes vienen
 * dinámicas desde markdown sin width/height conocidos en build time, (b) el
 * overhead de optimización es marginal para 5 PNG bien dimensionadas, (c)
 * mantiene el renderer agnóstico y server-side-only.
 */
function MarkdownImage({ src, alt, title }: ComponentProps<"img">) {
  if (typeof src !== "string") return null;
  const caption = title || alt;
  return (
    <figure className="my-8">
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img
        src={src}
        alt={alt ?? ""}
        loading="lazy"
        className="w-full rounded-lg border border-border shadow-2xl"
      />
      {caption && (
        <figcaption className="mt-2 text-center text-xs italic text-muted-foreground sm:text-sm">
          {caption}
        </figcaption>
      )}
    </figure>
  );
}

/**
 * Server-friendly wrapper de react-markdown con tipografía Tailwind `prose`.
 * - GFM (tablas, task lists, strikethrough)
 * - TOC automático en cualquier heading que diga "Tabla de contenidos" o `## Contents`
 * - Slugs estables (rehype-slug) para anchors y TOC
 * - Imágenes con caption visible (alt → figcaption)
 *
 * Nota: rehype-pretty-code se omite a propósito en este pase para mantener el
 * componente RSC-friendly sin overhead de Shiki en cada render. Se puede sumar
 * después si aldot pide highlight de código real.
 */
export function MarkdownRenderer({ children, className }: MarkdownRendererProps) {
  return (
    <div
      className={cn(
        "prose prose-invert max-w-none",
        "prose-headings:scroll-mt-24 prose-headings:font-semibold",
        "prose-a:text-primary hover:prose-a:opacity-80",
        "prose-pre:border prose-pre:border-border prose-pre:bg-muted",
        "prose-code:before:content-none prose-code:after:content-none",
        "prose-img:rounded-lg prose-img:border prose-img:border-border",
        className,
      )}
    >
      <ReactMarkdown
        remarkPlugins={[remarkGfm, remarkToc]}
        rehypePlugins={[rehypeSlug]}
        components={{
          img: MarkdownImage,
        }}
      >
        {children}
      </ReactMarkdown>
    </div>
  );
}
