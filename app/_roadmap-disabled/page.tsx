import { readMarkdown, extractToc } from "@/lib/markdown";
import { getLastUpdated } from "@/lib/git";
import { MarkdownRenderer } from "@/components/markdown-renderer";
import { Badge } from "@/components/ui/badge";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";

export const metadata = {
  title: "Roadmap — Pax",
  description: "Por dónde va el proyecto Pax: completado, actual, futuro.",
};

export default async function RoadmapPage() {
  const doc = await readMarkdown("roadmap.md");
  const toc = extractToc(doc.content, 3);
  const updated = await getLastUpdated("content/roadmap.md");

  return (
    <div className="mx-auto max-w-6xl px-4 py-8 sm:py-12">
      <div className="mb-6 flex flex-wrap items-center gap-3">
        <h1 className="text-3xl font-bold tracking-tight sm:text-4xl">
          Roadmap
        </h1>
        {updated && (
          <Badge variant="outline" className="text-xs font-normal">
            Última actualización: {updated}
          </Badge>
        )}
      </div>

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
