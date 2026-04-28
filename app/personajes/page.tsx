import Image from "next/image";
import Link from "next/link";
import { listPersonajeSummaries } from "@/lib/personajes";
import { getLastUpdatedAny } from "@/lib/git";
import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export const metadata = {
  title: "Personajes — Pax",
  description:
    "Galería de personajes del universo Pax: Jiggy, Wiz, Byte, Luxa, Zek y Mariela.",
};

export default async function PersonajesPage() {
  const personajes = await listPersonajeSummaries();
  const updated = await getLastUpdatedAny([
    "content/personajes",
    "public/images/personajes",
  ]);

  return (
    <div className="mx-auto max-w-6xl px-4 py-8 sm:py-12">
      <div className="mb-6 flex flex-wrap items-center gap-3">
        <h1 className="text-3xl font-bold tracking-tight sm:text-4xl">
          Personajes
        </h1>
        {updated && (
          <Badge variant="outline" className="text-xs font-normal">
            Última actualización: {updated}
          </Badge>
        )}
      </div>

      <p className="mb-8 max-w-2xl text-sm leading-relaxed text-muted-foreground sm:text-base">
        Los Pax son cíclopes verde turquesa que custodian las chispas humanas
        bajo tierra. Acá vas a encontrar a cada uno con su prompt visual
        copiable y su rol en la historia. Mariela es la única humana del grupo
        — protagonista del episodio 1.
      </p>

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {personajes.map((p) => (
          <Link
            key={p.slug}
            href={`/personajes/${p.slug}`}
            className="group focus:outline-none"
          >
            <Card className="h-full overflow-hidden p-0 transition-all group-hover:scale-[1.02] group-hover:ring-1 group-hover:ring-zinc-700">
              {p.image ? (
                <div className="relative aspect-square w-full overflow-hidden bg-muted">
                  <Image
                    src={p.image}
                    alt={p.name}
                    fill
                    sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"
                    className="object-cover"
                  />
                </div>
              ) : (
                <div className="flex aspect-square w-full items-center justify-center bg-muted text-xs text-muted-foreground">
                  sin imagen
                </div>
              )}
              <CardHeader className="px-4 pt-4">
                <CardTitle className="text-lg">{p.name}</CardTitle>
              </CardHeader>
              <CardContent className="px-4 pb-4 pt-2">
                <p className="line-clamp-2 text-sm text-muted-foreground">
                  {p.shortDescription || "Sin descripción todavía."}
                </p>
              </CardContent>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
}
