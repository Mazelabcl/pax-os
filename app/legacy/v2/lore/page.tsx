import { readMarkdown, extractToc } from "@/lib/markdown";
import { getLastUpdated } from "@/lib/git";
import { MarkdownRenderer } from "@/components/markdown-renderer";
import { VersionToggle } from "@/components/version-toggle";
import { Badge } from "@/components/ui/badge";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";

export const metadata = {
  title: "Lore V2 — Pax",
  description:
    "Lore v4 R2 (post-feedback de Pipez). Cosmos Pax cerrado: regla única, runners, ushnus y la red de seis naciones subterráneas.",
};

export default async function LoreV2Page() {
  const result = await readMarkdown("v2/lore.md").catch(() => null);

  if (!result) {
    return (
      <div className="mx-auto max-w-3xl px-4 py-8 sm:py-12">
        <VersionToggle
          current="v2"
          label="Lore V4 (post-feedback Pipez)"
          toHref="/lore"
          toLabel="Volver a Lore V1"
        />
        <h1 className="mb-4 text-3xl font-bold">Lore v4</h1>
        <p className="text-muted-foreground">
          Próximamente. El archivo <code>content/v2/lore.md</code> aún no está
          disponible.
        </p>
      </div>
    );
  }

  const toc = extractToc(result.content, 3);
  const updated = await getLastUpdated("content/v2/lore.md");

  return (
    <div className="mx-auto max-w-6xl px-4 py-8 sm:py-12">
      <VersionToggle
        current="v2"
        label="Lore V4 (post-feedback Pipez) — V3 disponible en /lore."
        toHref="/lore"
        toLabel="Ver Lore V1"
      />

      <div className="mb-6 flex flex-wrap items-center gap-3">
        <h1 className="text-3xl font-bold tracking-tight sm:text-4xl">
          Lore v4
        </h1>
        <Badge
          variant="outline"
          className="border-fuchsia-500/40 text-xs font-normal text-fuchsia-200"
        >
          score 87.2/100
        </Badge>
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
          <MarkdownRenderer>{result.content}</MarkdownRenderer>
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
