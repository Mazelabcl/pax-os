import { readMarkdown } from "@/lib/markdown";
import { getLastUpdated } from "@/lib/git";
import { MarkdownRenderer } from "@/components/markdown-renderer";
import { VersionToggle } from "@/components/version-toggle";
import { Badge } from "@/components/ui/badge";

export const metadata = {
  title: "Personajes V2 — Pax",
  description:
    "Itzel Pat Canul es la finalista como protagonista del piloto. Más 3 candidatos secundarios para próximos episodios.",
};

export default async function PersonajesV2Page() {
  const result = await readMarkdown(
    "v2/personajes/elegido-candidatos.md",
  ).catch(() => null);

  if (!result) {
    return (
      <div className="mx-auto max-w-3xl px-4 py-8 sm:py-12">
        <VersionToggle
          current="v2"
          label="Personajes V2"
          toHref="/personajes"
          toLabel="Ver cast V1"
        />
        <h1 className="mb-4 text-3xl font-bold">Personajes v2</h1>
        <p className="text-muted-foreground">
          Próximamente. El archivo{" "}
          <code>content/v2/personajes/elegido-candidatos.md</code> aún no está
          disponible.
        </p>
      </div>
    );
  }

  const updated = await getLastUpdated(
    "content/v2/personajes/elegido-candidatos.md",
  );

  return (
    <div className="mx-auto max-w-4xl px-4 py-8 sm:py-12">
      <VersionToggle
        current="v2"
        label="Personajes V2 — candidatos al rol del elegido."
        toHref="/personajes"
        toLabel="Ver cast V1"
      />

      <div className="mb-6 flex flex-wrap items-center gap-3">
        <h1 className="text-3xl font-bold tracking-tight sm:text-4xl">
          Personajes v2
        </h1>
        <Badge
          variant="outline"
          className="border-fuchsia-500/40 text-xs font-normal text-fuchsia-200"
        >
          Itzel 87.25/100
        </Badge>
        {updated && (
          <Badge variant="outline" className="text-xs font-normal">
            Última actualización: {updated}
          </Badge>
        )}
      </div>

      {/* Banner de protagonista finalista */}
      <section
        aria-labelledby="finalista-heading"
        className="mb-8 rounded-xl border border-fuchsia-500/40 bg-gradient-to-br from-fuchsia-500/10 via-zinc-950/60 to-zinc-950 p-5 sm:p-6"
      >
        <h2
          id="finalista-heading"
          className="mb-2 text-xs font-semibold uppercase tracking-[0.18em] text-fuchsia-300/90"
        >
          Protagonista finalista
        </h2>
        <p className="text-base leading-relaxed text-foreground sm:text-[1.05rem]">
          <strong>Itzel Pat Canul</strong> es la protagonista finalista del
          piloto. Los otros 3 candidatos quedan como personajes secundarios
          para próximos episodios.
        </p>
      </section>

      <article className="min-w-0">
        <MarkdownRenderer>{result.content}</MarkdownRenderer>
      </article>
    </div>
  );
}
