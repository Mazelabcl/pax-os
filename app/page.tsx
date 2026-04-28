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

interface SectionCard {
  href: string;
  title: string;
  description: string;
  status?: "disponible" | "proximamente";
}

const sections: SectionCard[] = [
  {
    href: "/lore",
    title: "Lore",
    description:
      "El universo Pax: cíclopes subterráneos, chispas, ushnus y la regla de la pregunta sincera.",
    status: "disponible",
  },
  {
    href: "/personajes",
    title: "Personajes",
    description:
      "Jiggy, Wiz, Byte, Luxa, Zek y Mariela. Galería con descripción, prompt visual y ficha.",
    status: "proximamente",
  },
  {
    href: "/episodio-1",
    title: "Episodio 1",
    description:
      "Script, beat sheet, storyboard y guion técnico del piloto.",
    status: "proximamente",
  },
];

export default function Home() {
  return (
    <div className="flex flex-col">
      <section className="relative isolate overflow-hidden">
        <div className="absolute inset-0 -z-10">
          <Image
            src="/images/portadas/portada2.png"
            alt="Portada del universo Pax"
            fill
            priority
            className="object-cover opacity-40"
            sizes="100vw"
          />
          <div className="absolute inset-0 bg-gradient-to-b from-background/20 via-background/70 to-background" />
        </div>

        <div className="mx-auto flex max-w-4xl flex-col items-start gap-6 px-4 py-20 sm:py-28 md:py-36">
          <Badge variant="secondary" className="uppercase tracking-wider">
            Mini-serie animada
          </Badge>
          <h1 className="text-4xl font-bold tracking-tight sm:text-6xl md:text-7xl">
            Pax
          </h1>
          <p className="max-w-2xl text-base text-muted-foreground sm:text-lg">
            Cíclopes subterráneos custodiando chispas humanas. Una pregunta
            sincera arriba enciende un cristal abajo. Acá vas a encontrar el
            lore, los personajes y el material del episodio 1.
          </p>
        </div>
      </section>

      <section className="mx-auto w-full max-w-5xl px-4 py-12 sm:py-16">
        <h2 className="mb-6 text-2xl font-semibold tracking-tight sm:text-3xl">
          Explorar
        </h2>
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {sections.map((section) => {
            const isAvailable = section.status === "disponible";
            return (
              <Link
                key={section.href}
                href={section.href}
                className="group focus:outline-none"
              >
                <Card className="h-full transition-colors group-hover:border-primary/60">
                  <CardHeader>
                    <div className="flex items-center justify-between gap-2">
                      <CardTitle className="text-xl">{section.title}</CardTitle>
                      {!isAvailable && (
                        <Badge
                          variant="outline"
                          className="text-xs font-normal"
                        >
                          próximamente
                        </Badge>
                      )}
                    </div>
                    <CardDescription className="text-sm leading-relaxed">
                      {section.description}
                    </CardDescription>
                  </CardHeader>
                  <CardContent className="pt-0 text-sm text-muted-foreground">
                    {isAvailable ? "Abrir →" : "Disponible pronto"}
                  </CardContent>
                </Card>
              </Link>
            );
          })}
        </div>
      </section>
    </div>
  );
}
