import Image from "next/image";
import Link from "next/link";
import { getStyleGuide } from "@/lib/episodio";
import { MarkdownRenderer } from "@/components/markdown-renderer";
import { CopyButton } from "@/components/copy-button";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export const metadata = {
  title: "Estilo — Pax",
  description:
    "DNA visual canónico de Pax: paleta, lighting, encuadres y bloque de estilo reutilizable.",
};

interface PaletteColor {
  name: string;
  hex: string;
  role?: string;
}

interface PaletteGroup {
  title: string;
  blurb?: string;
  colors: PaletteColor[];
}

// Hardcoded de style-guide.md — fuente: content/style-guide.md ## Paleta.
// Si cambia el guide, actualizar acá. (No parseamos para mantener color labels en español
// y poder agrupar sin regex frágil.)
const PALETTE: PaletteGroup[] = [
  {
    title: "Primarios",
    colors: [
      { name: "Magenta neón rim", hex: "#E83FC8", role: "Cristales / rim-lights" },
      { name: "Magenta neón core", hex: "#FF49B4", role: "Cristales (centro)" },
      { name: "Turquesa cian piel", hex: "#21D8B6", role: "Piel cíclope base" },
      { name: "Turquesa highlight", hex: "#2EE0C8", role: "Piel highlights" },
      { name: "Iris Pax", hex: "#3FE0C8", role: "Ojo cíclope" },
      { name: "Púrpura ambiente", hex: "#4B2E80", role: "Caverna" },
      { name: "Púrpura Wiz cloak", hex: "#3D2A66", role: "Túnica Wiz" },
      { name: "Púrpura Zek/Luxa", hex: "#7A3FB2", role: "Ropa secundaria" },
      { name: "Negro azulado", hex: "#0E0820", role: "Sombras profundas" },
      { name: "Negro azulado claro", hex: "#1A1340", role: "Sombras medias" },
    ],
  },
  {
    title: "Secundarios",
    colors: [
      { name: "Warm gold core", hex: "#FFE34D", role: "Cristal Luxa" },
      { name: "Warm gold deep", hex: "#D4A52B", role: "Tribal / cálido caverna" },
      { name: "Warm gold edge", hex: "#F1E3AA", role: "Edge gold" },
      { name: "Tungsten cocina", hex: "#FFD08A", role: "Cocina Mariela 3000K" },
      { name: "Dusk blue día", hex: "#5A6E8A", role: "Ventana Santiago día" },
      { name: "Dusk blue noche", hex: "#2A3A5A", role: "Ventana Santiago noche" },
    ],
  },
  {
    title: "Acentos",
    colors: [
      { name: "Lime Byte", hex: "#A7F432", role: "EXCLUSIVO LEDs Byte" },
      { name: "Pale cyan activación", hex: "#7FFFD4", role: "Pulso mágico subliminal" },
      { name: "Pale-dusty gold ancla", hex: "#D9C28A", role: "EXCLUSIVO B13B insert" },
      { name: "Sodium streetlamp", hex: "#FF8A30", role: "EXCLUSIVO Av. Bilbao B10" },
    ],
  },
];

interface ReferenceImage {
  src: string;
  name: string;
  role: string;
}

const CHARACTER_REFS: ReferenceImage[] = [
  { src: "/images/personajes/jiggy.png", name: "Jiggy", role: "Character lock" },
  { src: "/images/personajes/wiz.png", name: "Wiz", role: "Character lock" },
  { src: "/images/personajes/byte.png", name: "Byte", role: "Character lock" },
  { src: "/images/personajes/luxa.png", name: "Luxa", role: "Character lock" },
  { src: "/images/personajes/zek.png", name: "Zek", role: "Character lock" },
  {
    src: "/images/personajes/mariela.png",
    name: "Mariela",
    role: "Character lock (humano)",
  },
];

const MOOD_REFS: ReferenceImage[] = [
  {
    src: "/images/portadas/portada.png",
    name: "Portada — acción frenética",
    role: "Mood / paleta universo",
  },
  {
    src: "/images/portadas/portada2.png",
    name: "Portada — poster heroico",
    role: "Mood / caverna ceremonial",
  },
];

// Frase DNA tomada del style-guide ## DNA en una frase
const DNA = `Animación 3D estilizada con shading semi-realista, subsurface scattering en pieles cíclope verde turquesa, materiales PBR y emisivos saturados (cristales magenta-cian sobre púrpura cavernoso) iluminados con neón mágico de alto contraste cinematográfico, atravesados por volumetría densa y polvo en suspensión; lectura tipo cinemática de videojuego mobile premium / key art animado, NUNCA fotorrealismo ni Pixar genérico ni anime.`;

export default async function EstiloPage() {
  const { content, styleLock } = await getStyleGuide();

  return (
    <div className="mx-auto max-w-5xl px-4 py-8 sm:py-12">
      <header className="mb-10 flex flex-col gap-4">
        <Badge variant="secondary" className="w-fit uppercase tracking-wider">
          Style guide
        </Badge>
        <h1 className="text-3xl font-bold tracking-tight sm:text-4xl md:text-5xl">
          Estilo visual de Pax
        </h1>
        <p className="text-base leading-relaxed text-muted-foreground sm:text-lg">
          DNA visual canónico para todo prompt de generación.
        </p>
      </header>

      {/* DNA card */}
      <section
        aria-labelledby="dna-heading"
        className="mb-10 rounded-xl border border-fuchsia-500/30 bg-gradient-to-br from-fuchsia-500/10 via-zinc-950/60 to-zinc-950 p-5 sm:p-6"
      >
        <h2
          id="dna-heading"
          className="mb-3 text-xs font-semibold uppercase tracking-[0.18em] text-fuchsia-300/80"
        >
          DNA en una frase
        </h2>
        <p className="text-base leading-relaxed text-foreground sm:text-lg">
          {DNA}
        </p>
      </section>

      {/* Paleta */}
      <section className="mb-10">
        <h2 className="mb-4 text-2xl font-semibold tracking-tight sm:text-3xl">
          Paleta
        </h2>
        <div className="flex flex-col gap-6">
          {PALETTE.map((group) => (
            <div key={group.title}>
              <h3 className="mb-3 text-sm font-semibold uppercase tracking-wide text-muted-foreground">
                {group.title}
              </h3>
              <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5">
                {group.colors.map((c) => (
                  <ColorSwatch key={c.hex + c.name} color={c} />
                ))}
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Reference images */}
      <section className="mb-10">
        <h2 className="mb-4 text-2xl font-semibold tracking-tight sm:text-3xl">
          Reference images
        </h2>
        <p className="mb-5 text-sm text-muted-foreground">
          Cargar como reference en cualquier prompt donde aparezca el personaje.
          Las portadas se usan solo como mood-reference de caverna (no en shots
          de Mariela).
        </p>

        <h3 className="mb-3 text-sm font-semibold uppercase tracking-wide text-muted-foreground">
          Character locks
        </h3>
        <div className="mb-6 grid grid-cols-2 gap-3 sm:grid-cols-3 md:grid-cols-3 lg:grid-cols-6">
          {CHARACTER_REFS.map((r) => (
            <ReferenceTile key={r.src} item={r} />
          ))}
        </div>

        <h3 className="mb-3 text-sm font-semibold uppercase tracking-wide text-muted-foreground">
          Mood / style references
        </h3>
        <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
          {MOOD_REFS.map((r) => (
            <ReferenceTile key={r.src} item={r} wide />
          ))}
        </div>
      </section>

      {/* Resto del style-guide en markdown */}
      <section className="mb-10">
        <h2 className="mb-4 text-2xl font-semibold tracking-tight sm:text-3xl">
          Detalle completo
        </h2>
        <article className="min-w-0">
          <MarkdownRenderer>{content}</MarkdownRenderer>
        </article>
      </section>

      {/* Sticky bottom: copiar style-lock */}
      {styleLock && (
        <div className="pointer-events-none fixed inset-x-0 bottom-4 z-30 flex justify-center px-4">
          <div className="pointer-events-auto flex max-w-md items-center gap-3 rounded-full border border-fuchsia-500/40 bg-zinc-950/95 px-4 py-2 shadow-lg backdrop-blur">
            <span className="hidden text-xs text-muted-foreground sm:inline">
              Style-lock listo para pegar
            </span>
            <CopyButton
              text={styleLock}
              label="Copiar style-lock"
              size="sm"
              variant="default"
            />
          </div>
        </div>
      )}
    </div>
  );
}

function ColorSwatch({ color }: { color: PaletteColor }) {
  return (
    <Card size="sm" className="overflow-hidden">
      <div
        className="h-16 w-full"
        style={{ backgroundColor: color.hex }}
        aria-label={`Swatch ${color.name}`}
      />
      <CardContent className="flex flex-col gap-0.5 pb-3 pt-2">
        <span className="text-xs font-medium leading-tight">{color.name}</span>
        <span className="font-mono text-[11px] uppercase text-muted-foreground">
          {color.hex}
        </span>
        {color.role && (
          <span className="text-[11px] leading-tight text-muted-foreground">
            {color.role}
          </span>
        )}
      </CardContent>
    </Card>
  );
}

function ReferenceTile({ item, wide }: { item: ReferenceImage; wide?: boolean }) {
  return (
    <Link
      href={item.src}
      target="_blank"
      className="group block overflow-hidden rounded-xl border border-border bg-muted/20 transition-colors hover:border-primary/60"
    >
      <div className={wide ? "relative aspect-[16/9]" : "relative aspect-square"}>
        <Image
          src={item.src}
          alt={item.name}
          fill
          sizes="(max-width: 768px) 50vw, 240px"
          className="object-cover"
        />
      </div>
      <div className="flex flex-col gap-0.5 p-3">
        <span className="text-sm font-medium leading-tight">{item.name}</span>
        <span className="text-[11px] uppercase tracking-wide text-muted-foreground">
          {item.role}
        </span>
      </div>
    </Link>
  );
}
