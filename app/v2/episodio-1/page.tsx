import { readMarkdown, extractToc } from "@/lib/markdown";
import { getLastUpdated } from "@/lib/git";
import { MarkdownRenderer } from "@/components/markdown-renderer";
import { VersionToggle } from "@/components/version-toggle";
import { Badge } from "@/components/ui/badge";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";

export const metadata = {
  title: "Episodio 1 V2 — Pax",
  description:
    "Guion v2 R2 del piloto Pax. Cold open Apu, match-cut a Yucatán, Itzel y el primer pulso de empatía de la generación.",
};

export default async function Episodio1V2Page() {
  const result = await readMarkdown("v2/episodio-1/escenas.md").catch(
    () => null,
  );

  if (!result) {
    return (
      <div className="mx-auto max-w-3xl px-4 py-8 sm:py-12">
        <VersionToggle
          current="v2"
          label="Episodio 1 V2"
          toHref="/episodio-1"
          toLabel="Ver Episodio 1 V1"
        />
        <h1 className="mb-4 text-3xl font-bold">Episodio 1 v2</h1>
        <p className="text-muted-foreground">
          Próximamente. El archivo{" "}
          <code>content/v2/episodio-1/escenas.md</code> aún no está disponible.
        </p>
      </div>
    );
  }

  const toc = extractToc(result.content, 3);
  const updated = await getLastUpdated("content/v2/episodio-1/escenas.md");

  return (
    <div className="mx-auto max-w-6xl px-4 py-8 sm:py-12">
      <VersionToggle
        current="v2"
        label="Episodio 1 V2 — guion R2 post-feedback Pipez."
        toHref="/episodio-1"
        toLabel="Ver Episodio 1 V1"
      />

      <div className="mb-6 flex flex-wrap items-center gap-3">
        <h1 className="text-3xl font-bold tracking-tight sm:text-4xl">
          Episodio 1 v2
        </h1>
        <Badge
          variant="outline"
          className="border-fuchsia-500/40 text-xs font-normal text-fuchsia-200"
        >
          score 88.25/100 · GO al storyboard
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
