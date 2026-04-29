import { buildFullPrompt, getEpisodio1, tabContentPath } from "@/lib/episodio";
import { getLastUpdated } from "@/lib/git";
import { MarkdownRenderer } from "@/components/markdown-renderer";
import { CopyButton } from "@/components/copy-button";
import { EscenaCard } from "@/components/escena-card";
import { PromptCard } from "@/components/prompt-card";
import { Badge } from "@/components/ui/badge";
import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from "@/components/ui/tabs";

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

      {/* Tabs principales */}
      <Tabs defaultValue="escenas" className="w-full">
        <div className="-mx-4 mb-6 overflow-x-auto px-4">
          <TabsList className="h-9">
            <TabsTrigger value="escenas">Escenas</TabsTrigger>
            <TabsTrigger value="storyboard">Storyboard</TabsTrigger>
            <TabsTrigger value="seedance">Seedance</TabsTrigger>
            <TabsTrigger value="material">Material original</TabsTrigger>
          </TabsList>
        </div>

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

        {/* Tab 2: Storyboard / Nano Banana */}
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

        {/* Tab 4: Material original (sub-tabs) */}
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
      </Tabs>
    </div>
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
