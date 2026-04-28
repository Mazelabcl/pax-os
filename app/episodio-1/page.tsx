import { getEpisodio1, tabContentPath } from "@/lib/episodio";
import { getLastUpdated } from "@/lib/git";
import { MarkdownRenderer } from "@/components/markdown-renderer";
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
    "Guion, beat sheet, storyboard y guion técnico del piloto de Pax.",
};

export default async function Episodio1Page() {
  const episodio = await getEpisodio1();

  // Pre-calculamos la fecha de última actualización por tab para que cada panel
  // pueda mostrarla sin necesidad de un client component extra.
  const updatedByTab = await Promise.all(
    episodio.tabs.map((tab) => getLastUpdated(tabContentPath(tab))),
  );

  const heading = episodio.title
    ? `Episodio 1: ${episodio.title}`
    : "Episodio 1";

  return (
    <div className="mx-auto max-w-5xl px-4 py-8 sm:py-12">
      <div className="mb-2">
        <h1 className="text-3xl font-bold tracking-tight sm:text-4xl">
          {heading}
        </h1>
      </div>
      {episodio.synopsis && (
        <p className="mb-6 max-w-3xl text-sm leading-relaxed text-muted-foreground sm:text-base">
          {episodio.synopsis}
        </p>
      )}

      <Tabs defaultValue={episodio.tabs[0]?.id ?? "guion"} className="w-full">
        {/* Mobile: scroll horizontal si no caben */}
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
    </div>
  );
}
