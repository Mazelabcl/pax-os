import Link from "next/link";
import { readMarkdown, extractToc } from "@/lib/markdown";
import { getLastUpdated } from "@/lib/git";
import { MarkdownRenderer } from "@/components/markdown-renderer";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";

export const metadata = {
  title: "Lore — Pax",
  description:
    "Lore del universo Pax. Versión amigable por default, versión técnica completa disponible.",
};

type LoreVariant = "amigable" | "tecnica";

interface PageProps {
  searchParams: Promise<{ v?: string }>;
}

const SOURCES: Record<LoreVariant, { file: string; relPath: string }> = {
  amigable: { file: "lore-amigable.md", relPath: "content/lore-amigable.md" },
  tecnica: { file: "lore.md", relPath: "content/lore.md" },
};

export default async function LorePage({ searchParams }: PageProps) {
  const sp = await searchParams;
  const variant: LoreVariant = sp?.v === "tecnica" ? "tecnica" : "amigable";
  const source = SOURCES[variant];

  const doc = await readMarkdown(source.file);
  const toc = extractToc(doc.content, 3);
  const updated = await getLastUpdated(source.relPath);

  const otherVariant: LoreVariant =
    variant === "amigable" ? "tecnica" : "amigable";
  const toggleHref = otherVariant === "tecnica" ? "/lore?v=tecnica" : "/lore";

  return (
    <div className="mx-auto max-w-6xl px-4 py-8 sm:py-12">
      <div className="mb-6 flex flex-wrap items-center gap-3">
        <h1 className="text-3xl font-bold tracking-tight sm:text-4xl">Lore</h1>
        {updated && (
          <Badge variant="outline" className="text-xs font-normal">
            Última actualización: {updated}
          </Badge>
        )}
      </div>

      {/* Toggle amigable / técnico */}
      <div className="mb-6 flex flex-col gap-3 rounded-lg border border-border bg-card p-3 sm:flex-row sm:items-center sm:justify-between">
        <div className="text-sm">
          <span className="font-medium">
            {variant === "amigable"
              ? "Lore amigable (recomendado)"
              : "Lore técnico (canon completo)"}
          </span>
          <span className="ml-2 text-muted-foreground">
            {variant === "amigable"
              ? "Versión corta para colaboradores."
              : "Versión exhaustiva con todas las reglas internas."}
          </span>
        </div>
        <Button asChild variant="outline" size="sm">
          <Link href={toggleHref}>
            {otherVariant === "tecnica"
              ? "Ver versión técnica completa"
              : "Volver a la versión amigable"}
          </Link>
        </Button>
      </div>

      {/* Mobile: TOC colapsable arriba */}
      {toc.length > 0 && (
        <details className="mb-6 rounded-lg border border-border bg-card p-3 lg:hidden">
          <summary className="cursor-pointer text-sm font-medium">
            Tabla de contenidos ({toc.length})
          </summary>
          <ul className="mt-3 space-y-1 text-sm">
            {toc.map((item) => (
              <li
                key={item.slug}
                style={{ paddingLeft: `${(item.level - 1) * 12}px` }}
              >
                <a
                  href={`#${item.slug}`}
                  className="text-muted-foreground hover:text-foreground"
                >
                  {item.text}
                </a>
              </li>
            ))}
          </ul>
        </details>
      )}

      <Separator className="mb-8 hidden lg:block" />

      <div className="grid gap-10 lg:grid-cols-[1fr_220px]">
        <article className="min-w-0">
          <MarkdownRenderer>{doc.content}</MarkdownRenderer>
        </article>

        {/* Desktop: TOC sticky a la derecha */}
        {toc.length > 0 && (
          <aside className="hidden lg:block">
            <div className="sticky top-20">
              <p className="mb-3 text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                En esta página
              </p>
              <ScrollArea className="h-[calc(100vh-8rem)] pr-2">
                <ul className="space-y-1.5 text-sm">
                  {toc.map((item) => (
                    <li
                      key={item.slug}
                      style={{
                        paddingLeft: `${(item.level - 1) * 10}px`,
                      }}
                    >
                      <a
                        href={`#${item.slug}`}
                        className="block text-muted-foreground transition-colors hover:text-foreground"
                      >
                        {item.text}
                      </a>
                    </li>
                  ))}
                </ul>
              </ScrollArea>
            </div>
          </aside>
        )}
      </div>
    </div>
  );
}
