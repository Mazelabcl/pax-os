import Link from "next/link";
import { readMarkdown, extractToc } from "@/lib/markdown";
import { getLastUpdated } from "@/lib/git";
import { MarkdownRenderer } from "@/components/markdown-renderer";
import { VersionToggle } from "@/components/version-toggle";
import { Badge } from "@/components/ui/badge";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";

export const metadata = {
  title: "Pitch — Pax V2",
  description:
    "Pax en 2 minutos: la versión accesible del universo. Si nunca leíste nada de Pax, empezá acá.",
};

const PLACEHOLDER = `# Pax — la mini-serie en 2 minutos

> Próximamente: el pitch accesible para entrar al universo Pax sin contexto previo.
`;

export default async function PitchPage() {
  const result = await readMarkdown("v2/pitch.md").catch(() => null);
  const content = result?.content ?? PLACEHOLDER;
  const isPlaceholder = !result;

  const toc = extractToc(content, 3);
  const updated = result
    ? await getLastUpdated("content/v2/pitch.md")
    : null;

  return (
    <div className="mx-auto max-w-6xl px-4 py-8 sm:py-12">
      <VersionToggle
        current="v2"
        label="Pitch V2 — la versión accesible (archivo Quest 1)."
        toHref="/legacy/v2"
        toLabel="Volver a /legacy/v2"
      />

      <div className="mb-4 rounded-lg border border-fuchsia-500/40 bg-fuchsia-500/10 p-3 text-sm text-fuchsia-100 sm:text-base">
        Estás viendo la versión accesible. Si querés el lore técnico completo:{" "}
        <Link
          href="/legacy/v2/lore"
          className="font-medium underline underline-offset-2 hover:opacity-80"
        >
          /legacy/v2/lore
        </Link>
        .
      </div>

      <div className="mb-6 flex flex-wrap items-center gap-3">
        <h1 className="text-3xl font-bold tracking-tight sm:text-4xl">
          Pax en 2 minutos
        </h1>
        {isPlaceholder ? (
          <Badge
            variant="outline"
            className="border-amber-500/40 text-xs font-normal text-amber-200"
          >
            En escritura
          </Badge>
        ) : (
          updated && (
            <Badge variant="outline" className="text-xs font-normal">
              Última actualización: {updated}
            </Badge>
          )
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
          <MarkdownRenderer>{content}</MarkdownRenderer>
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
