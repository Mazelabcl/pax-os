import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import remarkToc from "remark-toc";
import rehypeSlug from "rehype-slug";
import { cn } from "@/lib/utils";

interface MarkdownRendererProps {
  children: string;
  className?: string;
}

/**
 * Server-friendly wrapper de react-markdown con tipografía Tailwind `prose`.
 * - GFM (tablas, task lists, strikethrough)
 * - TOC automático en cualquier heading que diga "Tabla de contenidos" o `## Contents`
 * - Slugs estables (rehype-slug) para anchors y TOC
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
      >
        {children}
      </ReactMarkdown>
    </div>
  );
}
