import Image from "next/image";
import Link from "next/link";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
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
    href: "/legacy/v2/lore",
    title: "Lore v4",
    description:
      "Cosmos Pax cerrado: regla única, ushnus, runners y la red de seis naciones subterráneas. Versión post-crítica, score 87.2/100.",
    score: "87.2",
  },
  {
    href: "/legacy/v2/personajes",
    title: "Personajes — Itzel",
    description:
      "Itzel Pat Canul, adolescente maya yucateca, finalista como protagonista del piloto. Más 3 candidatos secundarios para próximos episodios.",
    score: "87.25",
  },
  {
    href: "/legacy/v2/episodio-1",
    title: "Episodio 1 v2",
    description:
      "Guion R2 con cold open Apu, match-cut a Yucatán y el primer pulso de empatía de la generación. GO al storyboard.",
    score: "88.25",
  },
  {
    href: "/legacy/v2/proceso",
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

      {/* Hero — portada heroica del clan original (legacy quest 1) */}
      <figure className="mb-10 overflow-hidden rounded-xl border border-fuchsia-500/30 shadow-2xl">
        <Image
          src="/images/portadas/portada2.png"
          alt="Tribu Pax — poster heroico (archivo Quest 1)"
          width={1536}
          height={1024}
          priority
          className="h-auto w-full"
        />
        <figcaption className="bg-fuchsia-500/5 px-4 py-2 text-xs italic text-muted-foreground sm:text-sm">
          Tribu Pax — poster heroico (archivo Quest 1).
        </figcaption>
      </figure>

      {/* Onboarding: resumen del pitch — actualizar si pitch.md cambia */}
      <section className="mb-12 rounded-xl border border-fuchsia-500/40 bg-fuchsia-500/5 p-5 sm:p-7">
        <div className="mb-4 flex flex-wrap items-center gap-2">
          <Badge
            variant="secondary"
            className="bg-fuchsia-500/15 text-fuchsia-200"
          >
            Empezá acá
          </Badge>
          <span className="text-xs uppercase tracking-wider text-muted-foreground">
            ¿Nunca leíste nada de Pax?
          </span>
        </div>

        <h2 className="mb-4 text-2xl font-semibold tracking-tight sm:text-3xl">
          Pax en 30 segundos
        </h2>
        <p className="mb-6 text-base leading-relaxed text-foreground/90 sm:text-lg">
          Qué pasaría si bajo la corteza del planeta viviera una civilización
          antigua que lleva siglos cuidando un sistema invisible que sostiene
          el equilibrio del mundo, y que ese sistema solo se enciende cuando
          los humanos arriba son solidarios entre sí. Hace generaciones que la
          solidaridad cae. El sistema se está apagando. Y hay una adolescente
          maya, en un cenote olvidado de Yucatán, que sin saberlo acaba de
          hacer el primer gesto en una generación que reactiva el ciclo.
        </p>

        <h3 className="mb-3 text-xl font-semibold tracking-tight sm:text-2xl">
          El mundo
        </h3>
        <p className="mb-4 text-base leading-relaxed text-foreground/90">
          Bajo la superficie del planeta hay una civilización antigua: los Pax.
          No son una tribu chica — están repartidos por todo el mundo, en una
          red de túneles que recorre el planeta entero. Cada nación Pax hereda
          la estética y los rituales de la cultura ancestral más cercana al
          territorio que tiene encima.
        </p>
        <p className="mb-6 text-base leading-relaxed text-foreground/90">
          Los Pax bajo Yucatán visten y rezan como mayas. Los que viven bajo
          los Andes son herederos de los rituales andinos. Los de Rapa Nui se
          mueven entre tubos de lava y resuenan con los moai. Son seis en
          total. El piloto se enfoca en dos.
        </p>

        <Button
          asChild
          size="lg"
          className="bg-fuchsia-500 text-white hover:bg-fuchsia-400"
        >
          <Link href="/legacy/v2/pitch">Leer pitch completo (2 min) →</Link>
        </Button>
      </section>

      <section>
        <h2 className="mb-6 text-2xl font-semibold tracking-tight sm:text-3xl">
          Explorar V2
        </h2>
        <div className="grid gap-4 sm:grid-cols-2">
          <Link
            href="/legacy/v2/pitch"
            className="group focus:outline-none sm:col-span-2"
          >
            <Card className="h-full border-fuchsia-500/50 bg-fuchsia-500/5 transition-colors group-hover:border-fuchsia-500/80">
              <CardHeader>
                <div className="flex items-center justify-between gap-2">
                  <CardTitle className="text-xl text-fuchsia-100">
                    Empezá acá: Pax en 2 minutos
                  </CardTitle>
                  <Badge
                    variant="outline"
                    className="border-fuchsia-500/60 text-xs font-normal text-fuchsia-200"
                  >
                    Onboarding
                  </Badge>
                </div>
                <CardDescription className="text-sm leading-relaxed">
                  El pitch accesible: premisa, mundo, regla central, riesgo,
                  protagonista y tesis. Si nunca leíste nada de Pax, este es el
                  punto de entrada.
                </CardDescription>
              </CardHeader>
              <CardContent className="pt-0 text-sm text-fuchsia-200">
                Abrir →
              </CardContent>
            </Card>
          </Link>

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
