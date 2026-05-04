import Link from "next/link";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { VersionToggle } from "@/components/version-toggle";

export const metadata = {
  title: "Pax V2 — Pax",
  description:
    "La versión post-feedback Pipez. Lore v4, Itzel finalista, episodio 1 v2 y la narrativa del proceso.",
};

interface V2Card {
  href: string;
  title: string;
  description: string;
  score?: string;
}

const cards: V2Card[] = [
  {
    href: "/v2/lore",
    title: "Lore v4",
    description:
      "Cosmos Pax cerrado: regla única, ushnus, runners y la red de seis naciones subterráneas. Versión post-crítica, score 87.2/100.",
    score: "87.2",
  },
  {
    href: "/v2/personajes",
    title: "Personajes — Itzel",
    description:
      "Itzel Pat Canul, adolescente maya yucateca, finalista como protagonista del piloto. Más 3 candidatos secundarios para próximos episodios.",
    score: "87.25",
  },
  {
    href: "/v2/episodio-1",
    title: "Episodio 1 v2",
    description:
      "Guion R2 con cold open Apu, match-cut a Yucatán y el primer pulso de empatía de la generación. GO al storyboard.",
    score: "88.25",
  },
  {
    href: "/v2/proceso",
    title: "Cómo llegamos aquí",
    description:
      "La narrativa del proceso: del feedback de Pipez a la v2. Diez capítulos sobre cómo se reescribió el universo.",
  },
];

export default function V2Home() {
  return (
    <div className="mx-auto max-w-5xl px-4 py-8 sm:py-12">
      <VersionToggle
        current="v2"
        label="Estás viendo la versión V2 — post-feedback de Pipez."
        toHref="/"
        toLabel="Volver a V1"
      />

      <header className="mb-10 flex flex-col gap-5">
        <Badge variant="secondary" className="w-fit uppercase tracking-wider">
          Pax V2
        </Badge>
        <h1 className="text-3xl font-bold tracking-tight sm:text-5xl">
          Pax v2 — la versión que vio Pipez (y lo que cambió)
        </h1>
        <blockquote className="border-l-2 border-fuchsia-500/50 pl-4 text-base italic leading-relaxed text-muted-foreground sm:text-lg">
          &ldquo;Esta luna, por primera vez en una generación, un cristal Apu se
          quebró.&rdquo;
        </blockquote>

        <div className="flex flex-wrap items-center gap-2">
          <Badge
            variant="outline"
            className="border-fuchsia-500/40 text-xs font-normal text-fuchsia-200"
          >
            Lore 87.2
          </Badge>
          <Badge
            variant="outline"
            className="border-fuchsia-500/40 text-xs font-normal text-fuchsia-200"
          >
            Itzel 87.25
          </Badge>
          <Badge
            variant="outline"
            className="border-fuchsia-500/40 text-xs font-normal text-fuchsia-200"
          >
            Episodio 88.25
          </Badge>
        </div>
      </header>

      <section>
        <h2 className="mb-6 text-2xl font-semibold tracking-tight sm:text-3xl">
          Explorar V2
        </h2>
        <div className="grid gap-4 sm:grid-cols-2">
          {cards.map((card) => (
            <Link
              key={card.href}
              href={card.href}
              className="group focus:outline-none"
            >
              <Card className="h-full transition-colors group-hover:border-fuchsia-500/60">
                <CardHeader>
                  <div className="flex items-center justify-between gap-2">
                    <CardTitle className="text-xl">{card.title}</CardTitle>
                    {card.score && (
                      <Badge
                        variant="outline"
                        className="border-fuchsia-500/40 text-xs font-normal text-fuchsia-200"
                      >
                        {card.score}
                      </Badge>
                    )}
                  </div>
                  <CardDescription className="text-sm leading-relaxed">
                    {card.description}
                  </CardDescription>
                </CardHeader>
                <CardContent className="pt-0 text-sm text-muted-foreground">
                  Abrir →
                </CardContent>
              </Card>
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}
