import { readMarkdown } from "@/lib/markdown";
import { getLastUpdated } from "@/lib/git";
import { MarkdownRenderer } from "@/components/markdown-renderer";
import { Badge } from "@/components/ui/badge";

export const metadata = {
  title: "Cambios recientes — Pax",
  description:
    "Lista de cambios recientes en el proyecto Pax. Revisá esta página primero si volvés después de unos días.",
};

export default async function CambiosPage() {
  const doc = await readMarkdown("CHANGELOG.md");
  const updated = await getLastUpdated("content/CHANGELOG.md");

  return (
    <div className="mx-auto max-w-3xl px-4 py-8 sm:py-12">
      <div className="mb-3 flex flex-wrap items-center gap-3">
        <h1 className="text-3xl font-bold tracking-tight sm:text-4xl">
          Cambios recientes
        </h1>
        {updated && (
          <Badge variant="outline" className="text-xs font-normal">
            Última actualización: {updated}
          </Badge>
        )}
      </div>
      <p className="mb-8 max-w-2xl text-sm leading-relaxed text-muted-foreground sm:text-base">
        Cada vez que actualizamos algo en Pax, lo anotamos acá. Si entrás
        después de unos días, mirá esta página primero.
      </p>

      <article className="min-w-0">
        <MarkdownRenderer>{doc.content}</MarkdownRenderer>
      </article>
    </div>
  );
}
