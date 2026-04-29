import { Suspense } from "react";
import {
  buildConceptArtFullPrompt,
  buildFullPrompt,
  getEpisodio1,
  tabContentPath,
} from "@/lib/episodio";
import type { ConceptArt } from "@/lib/episodio";
import { getLastUpdated } from "@/lib/git";
import { MarkdownRenderer } from "@/components/markdown-renderer";
import { CopyButton } from "@/components/copy-button";
import { EscenaCard } from "@/components/escena-card";
import { PromptCard } from "@/components/prompt-card";
import { ConceptArtCard } from "@/components/concept-art-card";
import { EpisodioTabs } from "@/components/episodio-tabs";
import { Badge } from "@/components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

export const metadata = {
  title: "Episodio 1 — Pax",
  description:
    "TLDR, pitch, división en escenas y prompts copiables (Nano Banana + Seedance) del piloto.",
};

export default async function Episodio1Page() {
  const episodio = await getEpisodio1();

  const heading = episodio.title
    ? `Episodio 1: ${episodio.title}`
    : "Episodio 1";

  const headerStats: string[] = [];
  if (episodio.duracionTotal) {
    headerStats.push(`${episodio.duracionTotal} min`);
  }
  if (episodio.cantidadEscenas > 0) {
    headerStats.push(`${episodio.cantidadEscenas} escenas`);
  }

  // Tabs históricos: pre-calc fecha por archivo.
  const updatedByTab = await Promise.all(
    episodio.tabs.map((tab) => getLastUpdated(tabContentPath(tab))),
  );

  return (
    <div className="mx-auto max-w-5xl px-4 py-8 sm:py-12">
      {/* Header destacado: TLDR + Pitch siempre visibles */}
      <header className="mb-10 flex flex-col gap-6">
        <div className="flex flex-col gap-3">
          <Badge variant="secondary" className="w-fit uppercase tracking-wider">
            Piloto
          </Badge>
          <h1 className="text-3xl font-bold tracking-tight sm:text-4xl md:text-5xl">
            {heading}
          </h1>
          {headerStats.length > 0 && (
            <div className="flex flex-wrap items-center gap-2">
              {headerStats.map((s) => (
                <Badge key={s} variant="outline" className="text-xs font-normal">
                  {s}
                </Badge>
              ))}
            </div>
          )}
        </div>

        {episodio.tldr && (
          <section
            aria-labelledby="tldr-heading"
            className="rounded-xl border border-zinc-800 bg-zinc-950/40 p-5 sm:p-6"
          >
            <h2
              id="tldr-heading"
              className="mb-3 text-xs font-semibold uppercase tracking-[0.18em] text-muted-foreground"
            >
              TLDR
            </h2>
            <p className="text-base leading-relaxed text-foreground/95 sm:text-lg">
              {episodio.tldr}
            </p>
          </section>
        )}

        {episodio.pitch && (
          <section
            aria-labelledby="pitch-heading"
            className="relative overflow-hidden rounded-xl border border-fuchsia-500/40 bg-gradient-to-br from-fuchsia-500/10 via-zinc-950/60 to-zinc-950 p-5 shadow-[0_0_0_1px_rgba(232,63,200,0.05)] sm:p-6"
          >
            <div className="mb-3 flex items-center justify-between gap-3">
              <h2
                id="pitch-heading"
                className="text-xs font-semibold uppercase tracking-[0.18em] text-fuchsia-300/80"
              >
                Pitch
              </h2>
              <CopyButton
                text={episodio.pitch}
                label="Copiar pitch"
                size="sm"
                variant="outline"
              />
            </div>
            <p className="text-base leading-relaxed text-foreground sm:text-[1.05rem]">
              {episodio.pitch}
            </p>
          </section>
        )}
      </header>

      {/* Tabs principales (sincronizadas con ?tab= en la URL).
          Suspense requerido por useSearchParams en el wrapper client. */}
      <Suspense fallback={<TabsFallback />}>
        <EpisodioTabs
          defaultValue="escenas"
          triggers={[
            { value: "escenas", label: "Escenas" },
            { value: "concept-arts", label: "Concept arts" },
            { value: "storyboard", label: "Storyboard" },
            { value: "seedance", label: "Seedance" },
            { value: "material", label: "Material original" },
          ]}
        >
        {/* Tab 1: Escenas */}
        <TabsContent value="escenas" className="mt-2">
          <div className="flex flex-col gap-4">
            {episodio.divisionResumen && (
              <p className="rounded-lg border border-border bg-muted/30 p-4 text-sm leading-relaxed text-muted-foreground sm:text-base">
                {episodio.divisionResumen}
              </p>
            )}
            {episodio.escenas.length === 0 ? (
              <p className="text-sm text-muted-foreground">
                No se pudieron parsear escenas. Revisar
                <code className="mx-1">content/episodio-1/escenas.md</code>.
              </p>
            ) : (
              <ul className="flex flex-col gap-3">
                {episodio.escenas.map((escena) => (
                  <li key={escena.id}>
                    <EscenaCard escena={escena} />
                  </li>
                ))}
              </ul>
            )}
          </div>
        </TabsContent>

        {/* Tab 2: Concept arts */}
        <TabsContent value="concept-arts" className="mt-2">
          <ConceptArtsView
            data={episodio.conceptArts}
            styleLock={episodio.styleLock}
          />
        </TabsContent>

        {/* Tab 3: Storyboard / Nano Banana */}
        <TabsContent value="storyboard" className="mt-2">
          <PromptList
            kind="nano"
            scenes={episodio.storyboard}
            styleLock={episodio.styleLock}
            emptyMessage="No se pudieron parsear los prompts de Nano Banana."
          />
        </TabsContent>

        {/* Tab 3: Seedance */}
        <TabsContent value="seedance" className="mt-2">
          <PromptList
            kind="seedance"
            scenes={episodio.seedance}
            styleLock={episodio.styleLock}
            emptyMessage="No se pudieron parsear los prompts de Seedance."
          />
        </TabsContent>

        {/* Tab 5: Material original (sub-tabs) */}
        <TabsContent value="material" className="mt-2">
          <Tabs defaultValue={episodio.tabs[0]?.id ?? "guion"} className="w-full">
            <div className="-mx-4 mb-4 overflow-x-auto px-4">
              <TabsList className="h-9">
                {episodio.tabs.map((tab) => (
                  <TabsTrigger key={tab.id} value={tab.id} className="px-3">
                    {tab.label}
                  </TabsTrigger>
                ))}
              </TabsList>
            </div>
            {episodio.tabs.map((tab, idx) => {
              const updated = updatedByTab[idx];
              return (
                <TabsContent key={tab.id} value={tab.id} className="mt-2">
                  {updated && (
                    <div className="mb-4">
                      <Badge variant="outline" className="text-xs font-normal">
                        Última actualización: {updated}
                      </Badge>
                    </div>
                  )}
                  <article className="min-w-0">
                    <MarkdownRenderer>{tab.content}</MarkdownRenderer>
                  </article>
                </TabsContent>
              );
            })}
          </Tabs>
        </TabsContent>
      </EpisodioTabs>
      </Suspense>
    </div>
  );
}

function TabsFallback() {
  return (
    <div className="h-9 animate-pulse rounded-md border border-border bg-muted/40" />
  );
}

interface PromptListProps {
  kind: "nano" | "seedance";
  scenes: Awaited<ReturnType<typeof getEpisodio1>>["storyboard"];
  styleLock: string;
  emptyMessage: string;
}

function PromptList({ kind, scenes, styleLock, emptyMessage }: PromptListProps) {
  const intro =
    kind === "nano"
      ? "15 prompts image-to-image para generar el storyboard. Cada bloque arma style-lock + references + prompt + negative en una sola copia."
      : "16 prompts video-gen optimizados con best practices Seedance 2026. Cada bloque arma style-lock + references + prompt + negative en una sola copia. El audio se inyecta en post.";

  const badge = kind === "nano" ? "Nano Banana" : "Seedance";

  return (
    <div className="flex flex-col gap-4">
      <p className="text-sm leading-relaxed text-muted-foreground sm:text-base">
        {intro}
      </p>
      {styleLock && (
        <div className="flex flex-wrap items-center gap-2 rounded-lg border border-dashed border-border bg-muted/20 px-3 py-2 text-xs text-muted-foreground">
          <span className="font-medium uppercase tracking-wide">Style-lock global</span>
          <span className="hidden sm:inline">— se incluye automáticamente al copiar</span>
          <CopyButton text={styleLock} label="Copiar style-lock" size="sm" />
        </div>
      )}
      {scenes.length === 0 ? (
        <p className="text-sm text-muted-foreground">{emptyMessage}</p>
      ) : (
        <ul className="flex flex-col gap-4">
          {scenes.map((scene) => (
            <li key={`${kind}-${scene.id}`}>
              <PromptCard
                numero={scene.numero}
                titulo={scene.titulo}
                beat={scene.beat}
                refs={scene.refs}
                slots={scene.slots}
                prompt={scene.prompt}
                negative={scene.negative}
                fullCopy={buildFullPrompt(scene, styleLock)}
                notas={scene.notas}
                audio={scene.audio}
                badge={badge}
              />
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

// =============================================================================
// Concept arts view (server component)
// =============================================================================

interface ConceptArtsViewProps {
  data: Awaited<ReturnType<typeof getEpisodio1>>["conceptArts"];
  styleLock: string;
}

function ConceptArtsView({ data, styleLock }: ConceptArtsViewProps) {
  // Mapa de id → posición global en el orden recomendado (1..N).
  const ordenGlobal = new Map<string, number>();
  let n = 1;
  for (const b of data.bloques) {
    for (const id of b.orden) {
      if (!ordenGlobal.has(id)) ordenGlobal.set(id, n++);
    }
  }

  // Items agrupados por bloque, en el orden declarado (con fallback al orden de aparición).
  const itemsPorBloque = new Map<"A" | "B" | "C", ConceptArt[]>([
    ["A", []],
    ["B", []],
    ["C", []],
  ]);
  const byId = new Map(data.items.map((it) => [it.id, it]));
  for (const b of data.bloques) {
    const arr = itemsPorBloque.get(b.letra) ?? [];
    for (const id of b.orden) {
      const it = byId.get(id);
      if (it) arr.push(it);
    }
    // Items del archivo que no están en el orden del bloque pero comparten letra:
    for (const it of data.items) {
      if (it.bloque === b.letra && !b.orden.includes(it.id) && !arr.includes(it)) {
        arr.push(it);
      }
    }
    itemsPorBloque.set(b.letra, arr);
  }

  return (
    <div className="flex flex-col gap-6">
      {/* Header */}
      <div className="flex flex-col gap-3 rounded-xl border border-border bg-muted/20 p-5">
        <div className="flex flex-wrap items-center gap-2">
          <Badge variant="secondary" className="uppercase tracking-wider">
            Concept arts
          </Badge>
          <Badge variant="outline" className="text-xs font-normal">
            {data.total} assets a generar
          </Badge>
        </div>
        <h2 className="text-lg font-semibold sm:text-xl">
          Pipeline de generación con Nano Banana
        </h2>
        {data.comoUsar.length > 0 && (
          <ul className="flex flex-col gap-1.5 text-sm leading-relaxed text-muted-foreground sm:text-[0.95rem]">
            {data.comoUsar.slice(0, 4).map((bullet, i) => (
              <li
                key={i}
                className="relative pl-4 before:absolute before:left-0 before:top-2.5 before:size-1 before:rounded-full before:bg-fuchsia-400/70"
              >
                {bullet}
              </li>
            ))}
          </ul>
        )}
      </div>

      {/* Banner: orden de generación con dependencia */}
      <OrdenGeneracion bloques={data.bloques} ordenGlobal={ordenGlobal} />

      {/* Lista por bloque */}
      {(["A", "B", "C"] as const).map((letra) => {
        const items = itemsPorBloque.get(letra) ?? [];
        if (items.length === 0) return null;
        const meta = data.bloques.find((b) => b.letra === letra);
        return (
          <section key={letra} className="flex flex-col gap-3">
            <header className="flex flex-col gap-1">
              <div className="flex flex-wrap items-baseline gap-2">
                <h3 className="text-base font-semibold sm:text-lg">
                  Bloque {letra}{meta ? ` — ${meta.titulo}` : ""}
                </h3>
                <Badge variant="outline" className="text-[10px] font-normal uppercase tracking-wide">
                  {items.length} {items.length === 1 ? "asset" : "assets"}
                </Badge>
              </div>
              {meta?.descripcion && (
                <p className="text-xs text-muted-foreground sm:text-sm">
                  {meta.descripcion}
                </p>
              )}
            </header>
            <ul className="flex flex-col gap-3">
              {items.map((art) => (
                <li key={art.id}>
                  <ConceptArtCard
                    art={art}
                    ordenNum={ordenGlobal.get(art.id) ?? null}
                    fullCopy={buildConceptArtFullPrompt(art, styleLock)}
                  />
                </li>
              ))}
            </ul>
          </section>
        );
      })}
    </div>
  );
}

interface OrdenGeneracionProps {
  bloques: Awaited<ReturnType<typeof getEpisodio1>>["conceptArts"]["bloques"];
  ordenGlobal: Map<string, number>;
}

function OrdenGeneracion({ bloques, ordenGlobal }: OrdenGeneracionProps) {
  const arrows = ["→", "→"]; // entre bloques
  return (
    <section
      aria-labelledby="orden-heading"
      className="flex flex-col gap-3 rounded-xl border border-fuchsia-500/30 bg-gradient-to-br from-fuchsia-500/5 via-zinc-950/40 to-zinc-950 p-4 sm:p-5"
    >
      <div className="flex items-center gap-2">
        <h3
          id="orden-heading"
          className="text-xs font-semibold uppercase tracking-[0.18em] text-fuchsia-300/90"
        >
          Orden de generación recomendado
        </h3>
      </div>
      <p className="text-xs leading-relaxed text-muted-foreground sm:text-sm">
        Los HEROs primero (anclan identidad). Después los derivados (referencian HEROs como{" "}
        <code className="font-mono">@image1</code>). Finalmente los first-frames Seedance
        (combinan concepts + character locks). Respetá el orden — los seeds dependen de él.
      </p>
      <div className="grid gap-3 sm:grid-cols-3">
        {bloques.map((b, i) => (
          <div
            key={b.letra}
            className="flex flex-col gap-2 rounded-lg border border-border bg-background/40 p-3"
          >
            <div className="flex items-center gap-2">
              <span className="inline-flex size-6 items-center justify-center rounded-md bg-fuchsia-500/20 font-mono text-xs font-bold text-fuchsia-200">
                {b.letra}
              </span>
              <span className="text-xs font-semibold uppercase tracking-wide text-foreground">
                Bloque {b.letra}
              </span>
              {i < bloques.length - 1 && (
                <span className="ml-auto hidden text-fuchsia-300/60 sm:inline">
                  {arrows[i] ?? "→"}
                </span>
              )}
            </div>
            <p className="text-xs leading-snug text-muted-foreground">{b.titulo}</p>
            <ol className="flex flex-col gap-1 text-[11px] leading-tight text-foreground/85">
              {b.orden.slice(0, 12).map((id) => {
                const num = ordenGlobal.get(id);
                return (
                  <li key={id} className="flex items-baseline gap-1.5">
                    <span className="font-mono text-muted-foreground">
                      {num !== undefined ? String(num).padStart(2, "0") : "??"}
                    </span>
                    <a
                      href={`#${id}`}
                      className="truncate font-mono text-fuchsia-200/90 underline-offset-2 hover:underline"
                    >
                      {id}
                    </a>
                  </li>
                );
              })}
              {b.orden.length > 12 && (
                <li className="text-muted-foreground">
                  +{b.orden.length - 12} más…
                </li>
              )}
            </ol>
          </div>
        ))}
      </div>
    </section>
  );
}
