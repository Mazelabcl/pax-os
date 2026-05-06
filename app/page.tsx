import Image from "next/image";
import Link from "next/link";
import { listPersonajeSummaries } from "@/lib/personajes";
import { listEpisodiosOutline } from "@/lib/episodios";
import { getRecentCommits, type RecentCommit } from "@/lib/git";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";

export const metadata = {
  title: "Pax — webserie animada",
  description:
    "Pax: una webserie animada sobre una tribu subterránea, sus cristales, y la energía colectiva que mueve al mundo. 12 episodios, 36 minutos.",
};

// =============================================================================
// Datos: cast core (orden canon Pipez Quest 2)
// =============================================================================

const CLAN_CORE_SLUGS = [
  "jiggy",
  "kz",
  "onyx",
  "agatha",
  "wiz",
  "byte",
  "luxa",
] as const;

// Tagline corto por personaje (1 línea, derivada de fichas).
const CLAN_TAGLINE: Record<(typeof CLAN_CORE_SLUGS)[number], string> = {
  jiggy: "El chasqui. Cruza túneles antes de que termine la frase.",
  kz: "El más joven. Torpe, intuitivo, corazón del clan.",
  onyx: "El motor físico. Empuja primero, piensa después.",
  agatha: "Ancla emocional. Recuerda para qué subimos.",
  wiz: "El viejo sabio. Custodia los cristales y guarda secretos.",
  byte: "Cerebro técnico. Encuentra el patrón antes de explicarlo.",
  luxa: "Comic relief con corazón. La que levanta cuando todo pesa.",
};

export default async function Home() {
  const [personajes, episodios, commits] = await Promise.all([
    listPersonajeSummaries(),
    listEpisodiosOutline(),
    getRecentCommits(15),
  ]);

  const clan = CLAN_CORE_SLUGS.map((slug) =>
    personajes.find((p) => p.slug === slug),
  ).filter((p): p is NonNullable<typeof p> => Boolean(p));

  // Capítulos con thumbnail disponible (1, 2). Resto = solo texto.
  const capThumbs: Record<number, string> = {
    1: "/images/storyboards/cap-1-hook-crystal-dimming.png",
    2: "/images/storyboards/cap-2-fresco-close-up.png",
  };

  return (
    <div className="flex flex-col">
      {/* ===================================================================
          1. HERO
          =================================================================== */}
      <section className="relative isolate overflow-hidden">
        <div className="absolute inset-0 -z-10">
          <Image
            src="/images/concepts/concept-cave-stalagmites-reawakening.png"
            alt="Caverna Pax con cristales magenta"
            fill
            priority
            className="object-cover opacity-50"
            sizes="100vw"
          />
          <div className="absolute inset-0 bg-gradient-to-b from-background/30 via-background/70 to-background" />
        </div>

        <div className="mx-auto flex min-h-[80vh] max-w-4xl flex-col items-center justify-center gap-6 px-4 py-24 text-center sm:py-32 md:py-40">
          <Badge
            variant="secondary"
            className="bg-fuchsia-500/15 uppercase tracking-wider text-fuchsia-200"
          >
            Webserie animada
          </Badge>
          <h1 className="text-balance text-3xl font-bold leading-tight tracking-tight sm:text-5xl md:text-6xl">
            No es magia.
            <br />
            Es el resultado de lo que hacemos.
          </h1>
          <p className="max-w-2xl text-balance text-base leading-relaxed text-muted-foreground sm:text-lg md:text-xl">
            Pax — una webserie animada sobre una tribu subterránea, sus
            cristales, y la energía colectiva que mueve al mundo.
          </p>
          <a
            href="#pitch"
            className="mt-6 inline-flex items-center gap-2 rounded-full border border-fuchsia-500/40 bg-fuchsia-500/10 px-5 py-2.5 text-sm font-medium text-fuchsia-100 transition-colors hover:bg-fuchsia-500/20 sm:text-base"
          >
            <span aria-hidden>↓</span>
            <span>Conoce el proyecto</span>
          </a>
        </div>
      </section>

      {/* ===================================================================
          2. ELEVATOR PITCH
          =================================================================== */}
      <section
        id="pitch"
        className="relative scroll-mt-16 bg-gradient-to-b from-background via-fuchsia-950/10 to-background"
      >
        <div className="mx-auto grid max-w-6xl gap-10 px-4 py-16 sm:py-24 md:grid-cols-[1.2fr_1fr] md:items-center md:gap-16">
          <div className="flex flex-col gap-5">
            <Badge variant="outline" className="w-fit text-xs">
              La idea
            </Badge>
            <h2 className="text-2xl font-semibold tracking-tight sm:text-3xl md:text-4xl">
              Bajo la tierra hay una tribu cuidando una red invisible.
            </h2>
            <div className="space-y-4 text-base leading-relaxed text-muted-foreground sm:text-lg">
              <p>
                Bajo la superficie del planeta vive una civilización entera: los{" "}
                <strong className="text-foreground">Pax</strong>. Cíclopes verdes
                curiosos, juguetones, alquimistas. Llevan ahí más tiempo del que
                cualquier humano recuerda.
              </p>
              <p>
                Custodian unos cristales subterráneos que se cargan con la
                energía que generan los actos de bondad humanos arriba — ayudar,
                compartir, enseñar, hacer un gesto sin que te lo pidan. Cuando un
                cristal se llena, los Pax lo activan, y arriba aparece algo
                concreto: una operación que se cubre, un árbol que crece, un
                perro que encuentra hogar.
              </p>
              <p className="text-foreground">
                Hoy la red está fallando. Por primera vez, los Pax tienen que
                subir.
              </p>
            </div>
          </div>

          <div className="relative mx-auto w-full max-w-sm">
            <div className="absolute -inset-8 -z-10 rounded-full bg-fuchsia-500/20 blur-3xl" />
            <div className="relative aspect-square w-full overflow-hidden rounded-2xl border border-fuchsia-500/30 bg-muted/30 shadow-2xl">
              <Image
                src="/images/personajes/jiggy.png"
                alt="Jiggy — el chasqui del clan Pax"
                fill
                sizes="(max-width: 768px) 80vw, 400px"
                className="object-cover"
              />
            </div>
            <p className="mt-3 text-center text-xs uppercase tracking-wider text-muted-foreground">
              Jiggy — el primero en subir
            </p>
          </div>
        </div>
      </section>

      {/* ===================================================================
          3. CÓMO FUNCIONA
          =================================================================== */}
      <section className="border-t border-border/50">
        <div className="mx-auto max-w-6xl px-4 py-16 sm:py-24">
          <div className="mb-12 max-w-2xl">
            <Badge variant="outline" className="mb-3 text-xs">
              El sistema
            </Badge>
            <h2 className="text-2xl font-semibold tracking-tight sm:text-3xl md:text-4xl">
              Cómo funciona Pax
            </h2>
            <p className="mt-4 text-base leading-relaxed text-muted-foreground sm:text-lg">
              Tres pasos simples. Una sola idea: lo que pasa arriba lo construyen
              las personas que arriba viven. Los Pax solo lo recogen, lo
              concentran y lo devuelven hecho cosa.
            </p>
          </div>

          <div className="grid gap-6 md:grid-cols-3">
            <ComoCard
              numero="01"
              titulo="Los humanos aportan"
              parrafo="Una clase compartida, un gesto en la calle, una donación pequeña. Cualquier mecánica que mueva valor humano hacia impacto real es una ruca — un punto de aporte. La red está hecha de muchas rucas funcionando a la vez."
            />
            <ComoCard
              numero="02"
              titulo="Los cristales cargan"
              parrafo="Cada gesto sincero arriba carga un cristal abajo. Los cristales siempre existieron — los Pax solo los custodian. Son la contabilidad viva de la bondad humana."
              ring
            />
            <ComoCard
              numero="03"
              titulo="El mundo se activa"
              parrafo="Cuando un cristal se llena, los Pax lo activan. La energía sale y arriba aparece algo concreto: una operación cubierta, un árbol que crece, un mensaje que llega justo a tiempo. No es magia. Es el resultado de lo que hacemos."
            />
          </div>

          <figure className="mt-12 overflow-hidden rounded-2xl border border-border/50 shadow-2xl">
            <Image
              src="/images/concepts/concept-cave-wide-dark.png"
              alt="Cámara central de cristales del clan Pax"
              width={1536}
              height={864}
              className="h-auto w-full"
              sizes="(max-width: 1280px) 100vw, 1280px"
            />
            <figcaption className="bg-muted/30 px-4 py-2 text-center text-xs italic text-muted-foreground sm:text-sm">
              Cámara central de cristales — donde el clan custodia la red.
            </figcaption>
          </figure>
        </div>
      </section>

      {/* ===================================================================
          4. EL CLAN
          =================================================================== */}
      <section className="border-t border-border/50 bg-gradient-to-b from-background to-fuchsia-950/10">
        <div className="mx-auto max-w-6xl px-4 py-16 sm:py-24">
          <div className="mb-12 max-w-2xl">
            <Badge variant="outline" className="mb-3 text-xs">
              El cast
            </Badge>
            <h2 className="text-2xl font-semibold tracking-tight sm:text-3xl md:text-4xl">
              Los siete que suben
            </h2>
            <p className="mt-4 text-base leading-relaxed text-muted-foreground sm:text-lg">
              Siete Pax con roles claros, voces distintas y una sola misión
              compartida: reactivar la red. Cámara los sigue a todos, pero cada
              episodio cede el peso a uno distinto.
            </p>
          </div>

          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {clan.map((p) => (
              <Link
                key={p.slug}
                href={`/personajes/${p.slug}`}
                className="group focus:outline-none"
              >
                <Card className="h-full overflow-hidden p-0 transition-all group-hover:scale-[1.02] group-hover:ring-1 group-hover:ring-fuchsia-500/40">
                  {p.image && (
                    <div className="relative aspect-square w-full overflow-hidden bg-muted">
                      <Image
                        src={p.image}
                        alt={p.name}
                        fill
                        sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"
                        className="object-cover transition-transform group-hover:scale-105"
                      />
                    </div>
                  )}
                  <CardContent className="flex flex-col gap-1.5 p-4">
                    <div className="flex items-baseline justify-between gap-2">
                      <h3 className="text-lg font-semibold tracking-tight">
                        {p.name}
                      </h3>
                      <span className="text-xs text-muted-foreground transition-colors group-hover:text-fuchsia-300">
                        Ver →
                      </span>
                    </div>
                    <p className="text-sm leading-snug text-muted-foreground">
                      {CLAN_TAGLINE[p.slug as keyof typeof CLAN_TAGLINE] ??
                        p.shortDescription}
                    </p>
                  </CardContent>
                </Card>
              </Link>
            ))}
          </div>

          <div className="mt-8 text-center">
            <Link
              href="/personajes"
              className="inline-flex items-center gap-2 text-sm font-medium text-fuchsia-200 transition-colors hover:text-fuchsia-100"
            >
              Ver cast completo (incluye humanos y secundarios) →
            </Link>
          </div>
        </div>
      </section>

      {/* ===================================================================
          4.5 ACTOS DE LA TRIBU
          =================================================================== */}
      {commits.length > 0 && (
        <section className="border-t border-border/50">
          <div className="mx-auto max-w-6xl px-4 py-16 sm:py-24">
            <div className="mb-10 max-w-2xl">
              <Badge variant="outline" className="mb-3 text-xs">
                Novedades
              </Badge>
              <h2 className="text-2xl font-semibold tracking-tight sm:text-3xl md:text-4xl">
                Actos de la tribu
              </h2>
              <p className="mt-4 text-base leading-relaxed text-muted-foreground sm:text-lg">
                Cada gesto humano que mejora el sistema queda registrado acá.
                Esto no es un changelog técnico — es energía cargando los
                cristales.
              </p>
            </div>

            <ul
              className="flex snap-x snap-mandatory gap-4 overflow-x-auto pb-3 sm:grid sm:snap-none sm:grid-cols-2 sm:gap-4 sm:overflow-visible sm:pb-0"
              aria-label="Últimos actos de la tribu"
            >
              {commits.map((c) => (
                <li
                  key={c.hash}
                  className="min-w-[85%] shrink-0 snap-start sm:min-w-0 sm:shrink"
                >
                  <ActoCard commit={c} />
                </li>
              ))}
            </ul>

            <div className="mt-8 flex flex-wrap items-center gap-x-6 gap-y-2 text-sm">
              <a
                href="https://github.com/Mazelabcl/pax-os"
                target="_blank"
                rel="noreferrer noopener"
                className="font-medium text-fuchsia-200 transition-colors hover:text-fuchsia-100"
              >
                Repo público en GitHub ↗
              </a>
              <Link
                href="/cambios"
                className="font-medium text-fuchsia-200 transition-colors hover:text-fuchsia-100"
              >
                Ver changelog completo →
              </Link>
            </div>
          </div>
        </section>
      )}

      {/* ===================================================================
          5. LA HISTORIA — 12 EPISODIOS
          =================================================================== */}
      <section className="border-t border-border/50">
        <div className="mx-auto max-w-5xl px-4 py-16 sm:py-24">
          <div className="mb-12 max-w-2xl">
            <Badge variant="outline" className="mb-3 text-xs">
              La temporada
            </Badge>
            <h2 className="text-2xl font-semibold tracking-tight sm:text-3xl md:text-4xl">
              12 episodios. 36 minutos. Una temporada.
            </h2>
            <p className="mt-4 text-base leading-relaxed text-muted-foreground sm:text-lg">
              Una sola historia partida en gestos. Cada capítulo es una misión:
              un Pax sube, encuentra a un humano, abre una ruca y vuelve. Los
              cristales abajo se cargan un poquito más.
            </p>
          </div>

          <ol className="flex flex-col gap-3">
            {episodios.map((ep) => {
              const thumb = capThumbs[ep.numero];
              const hasDetail = ep.numero === 1 || ep.numero === 2;
              const href = hasDetail ? `/episodios/${ep.numero}` : "/lore";
              return (
                <li key={ep.numero}>
                  <Link
                    href={href}
                    className="group flex gap-4 rounded-xl border border-border/60 bg-card/40 p-4 transition-colors hover:border-fuchsia-500/40 hover:bg-fuchsia-500/5 sm:gap-6 sm:p-5"
                  >
                    <div className="flex shrink-0 items-start gap-3 sm:gap-4">
                      <span className="font-mono text-xs text-muted-foreground sm:text-sm">
                        {String(ep.numero).padStart(2, "0")}
                      </span>
                      {thumb && (
                        <div className="relative hidden aspect-video w-32 shrink-0 overflow-hidden rounded-md border border-border/40 bg-muted sm:block sm:w-44">
                          <Image
                            src={thumb}
                            alt={`Storyboard episodio ${ep.numero}`}
                            fill
                            sizes="(max-width: 768px) 0px, 176px"
                            className="object-cover"
                          />
                        </div>
                      )}
                    </div>
                    <div className="flex min-w-0 flex-1 flex-col gap-1.5">
                      <div className="flex flex-wrap items-baseline gap-2">
                        <h3 className="text-base font-semibold tracking-tight sm:text-lg">
                          {ep.titulo}
                        </h3>
                        {hasDetail ? (
                          <Badge
                            variant="outline"
                            className="border-fuchsia-500/40 text-[10px] font-normal uppercase tracking-wider text-fuchsia-200"
                          >
                            Storyboard
                          </Badge>
                        ) : (
                          <Badge
                            variant="outline"
                            className="text-[10px] font-normal uppercase tracking-wider text-muted-foreground"
                          >
                            Outline
                          </Badge>
                        )}
                      </div>
                      <p className="text-sm leading-relaxed text-muted-foreground sm:text-[0.95rem]">
                        {ep.logline}
                      </p>
                      <span className="mt-1 text-xs text-fuchsia-300/80 transition-colors group-hover:text-fuchsia-200 sm:text-sm">
                        {hasDetail ? "Ver episodio →" : "Outline en el lore →"}
                      </span>
                    </div>
                  </Link>
                </li>
              );
            })}
          </ol>
        </div>
      </section>

      {/* ===================================================================
          6. FOOTER LINKS
          =================================================================== */}
      <section className="border-t border-border/50 bg-muted/10">
        <div className="mx-auto max-w-5xl px-4 py-12 sm:py-16">
          <h2 className="mb-6 text-lg font-semibold tracking-tight text-muted-foreground sm:text-xl">
            Más material
          </h2>
          <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            <FooterLink
              href="/lore"
              title="Lore canónico"
              desc="El mundo, la tribu, los cristales, las rucas, la crisis. Lectura larga, post-feedback Pipez."
            />
            <FooterLink
              href="/principles"
              title="Primeros principios"
              desc="Qué es Pax, cómo funciona, por qué importa. El núcleo del proyecto."
            />
            <FooterLink
              href="/personajes"
              title="Cast completo"
              desc="10 fichas: el clan core de 7 Pax + secundarios humanos (Mariela, Itzel) y Pax (Zek)."
            />
            <FooterLink
              href="/roadmap"
              title="Roadmap"
              desc="Por dónde va el proyecto. Quests cerradas y futuras."
            />
            <FooterLink
              href="https://publish.obsidian.md/pax"
              title="Vault público (Obsidian)"
              desc="El proceso vivo: notas, decisiones, lecciones."
              external
            />
            <FooterLink
              href="/legacy/v2"
              title="Archivo Quest 1"
              desc="La versión vieja de la web. Lore v4, Itzel, episodio 1 v2. Conservado para referencia."
              muted
            />
          </div>
        </div>
      </section>
    </div>
  );
}

// =============================================================================
// Subcomponentes
// =============================================================================

function ActoCard({ commit }: { commit: RecentCommit }) {
  // Glyph + color por tipo de commit. Usamos caracteres unicode finos en lugar
  // de SVGs/emojis para mantener el tono Pax (basalt + jade + amber).
  const glyph =
    commit.kind === "feat" ? "⊕" : commit.kind === "fix" ? "⌬" : "·";
  const glyphCls =
    commit.kind === "feat"
      ? "text-emerald-300"
      : commit.kind === "fix"
        ? "text-amber-300"
        : "text-muted-foreground";
  const labelCls =
    commit.kind === "feat"
      ? "border-emerald-500/40 text-emerald-200"
      : commit.kind === "fix"
        ? "border-amber-500/40 text-amber-200"
        : "border-border/60 text-muted-foreground";
  const label =
    commit.kind === "feat"
      ? "Aporte"
      : commit.kind === "fix"
        ? "Reparación"
        : "Mantención";

  return (
    <article className="flex h-full flex-col gap-3 rounded-xl border border-border/60 bg-card/50 p-5 transition-colors hover:border-fuchsia-500/40 hover:bg-fuchsia-500/5">
      <header className="flex items-center justify-between gap-3">
        <span
          className={
            "inline-flex items-center gap-2 font-mono text-xs " + glyphCls
          }
          aria-hidden
        >
          <span className="text-base leading-none">{glyph}</span>
          <span>{commit.hash}</span>
        </span>
        <Badge
          variant="outline"
          className={
            "text-[10px] font-normal uppercase tracking-wider " + labelCls
          }
        >
          {label}
        </Badge>
      </header>

      <h3 className="text-base font-semibold tracking-tight text-foreground sm:text-lg">
        {commit.title}
      </h3>

      <p className="text-sm leading-relaxed text-muted-foreground">
        {commit.narrative}
      </p>

      <footer className="mt-auto pt-2 text-xs text-muted-foreground/80">
        {commit.relative}
      </footer>
    </article>
  );
}

function ComoCard({
  numero,
  titulo,
  parrafo,
  ring,
}: {
  numero: string;
  titulo: string;
  parrafo: string;
  ring?: boolean;
}) {
  return (
    <div
      className={
        "flex flex-col gap-3 rounded-xl border bg-card/60 p-5 sm:p-6 " +
        (ring
          ? "border-fuchsia-500/40 shadow-[0_0_0_1px_rgba(232,63,200,0.05)]"
          : "border-border/60")
      }
    >
      <span className="font-mono text-xs uppercase tracking-widest text-fuchsia-300/80">
        {numero}
      </span>
      <h3 className="text-lg font-semibold tracking-tight sm:text-xl">
        {titulo}
      </h3>
      <p className="text-sm leading-relaxed text-muted-foreground sm:text-[0.95rem]">
        {parrafo}
      </p>
    </div>
  );
}

function FooterLink({
  href,
  title,
  desc,
  external,
  muted,
}: {
  href: string;
  title: string;
  desc: string;
  external?: boolean;
  muted?: boolean;
}) {
  const cls =
    "group block rounded-lg border bg-card/40 p-4 transition-colors hover:border-fuchsia-500/40 hover:bg-fuchsia-500/5 " +
    (muted ? "border-border/40 opacity-80" : "border-border/60");
  const titleCls =
    "text-sm font-semibold tracking-tight " +
    (muted ? "text-muted-foreground" : "text-foreground");
  const content = (
    <>
      <div className="mb-1 flex items-baseline justify-between gap-2">
        <span className={titleCls}>{title}</span>
        <span className="text-xs text-muted-foreground transition-colors group-hover:text-fuchsia-300">
          {external ? "↗" : "→"}
        </span>
      </div>
      <p className="text-xs leading-relaxed text-muted-foreground sm:text-[0.85rem]">
        {desc}
      </p>
    </>
  );
  if (external) {
    return (
      <a
        href={href}
        target="_blank"
        rel="noreferrer noopener"
        className={cls}
      >
        {content}
      </a>
    );
  }
  return (
    <Link href={href} className={cls}>
      {content}
    </Link>
  );
}
