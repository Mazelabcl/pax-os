import Image from "next/image";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft, ArrowRight } from "lucide-react";
import {
  getEpisodioDetalle,
  listEpisodiosOutline,
  type StoryboardShot,
} from "@/lib/episodios";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";

interface PageProps {
  params: Promise<{ id: string }>;
}

// Caps con storyboard completo (PNG + companion .md). Fallback a outline si falta.
const CAPS_CON_DETALLE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] as const;
// Total caps generados como rutas estaticas (todos los del outline).
const CAPS_SSG = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] as const;

export async function generateStaticParams() {
  return CAPS_SSG.map((n) => ({ id: String(n) }));
}

export async function generateMetadata({ params }: PageProps) {
  const { id } = await params;
  const numero = parseInt(id, 10);
  const ep = numero
    ? await getEpisodioDetalle(numero).catch(() => null)
    : null;
  if (!ep) {
    return { title: "Episodio no encontrado — Pax" };
  }
  return {
    title: `Episodio ${ep.numero} — ${ep.titulo} — Pax`,
    description: ep.logline,
  };
}

export default async function EpisodioDetallePage({ params }: PageProps) {
  const { id } = await params;
  const numero = parseInt(id, 10);
  if (!Number.isFinite(numero)) notFound();

  const detalle = await getEpisodioDetalle(numero);
  if (!detalle) notFound();

  // Solo cap 1 y 2 tienen detalle visual completo.
  const tieneDetalle = (CAPS_CON_DETALLE as readonly number[]).includes(numero);

  const outline = await listEpisodiosOutline();
  const previo = outline.find((e) => e.numero === numero - 1);
  const siguiente = outline.find((e) => e.numero === numero + 1);

  // Hero: si hay companion sin shotNumber lo usamos; si no, primer shot numerado.
  const heroShot =
    detalle.shots.find((s) => s.shotNumber === null) ?? detalle.shots[0];

  // Storyboard secuencial: SOLO shots numerados, en orden estricto 01, 02, 03...
  const shotsOrdenados = detalle.shots
    .filter((s) => s.shotNumber !== null)
    .sort((a, b) => (a.shotNumber ?? 0) - (b.shotNumber ?? 0));

  return (
    <div className="flex flex-col">
      {/* Top nav */}
      <div className="mx-auto w-full max-w-5xl px-4 pt-6">
        <Button asChild variant="ghost" size="sm" className="-ml-2">
          <Link href="/">
            <ArrowLeft className="size-4" aria-hidden />
            Volver al inicio
          </Link>
        </Button>
      </div>

      {/* =====================================================================
          HERO
          ===================================================================== */}
      <section className="relative isolate mt-4 overflow-hidden">
        {heroShot && (
          <div className="absolute inset-0 -z-10">
            <Image
              src={heroShot.image}
              alt={heroShot.titulo || `Storyboard episodio ${numero}`}
              fill
              priority
              sizes="100vw"
              className="object-cover opacity-50"
            />
            <div className="absolute inset-0 bg-gradient-to-b from-background/40 via-background/70 to-background" />
          </div>
        )}

        <div className="mx-auto flex max-w-4xl flex-col gap-5 px-4 py-20 sm:py-28">
          <div className="flex flex-wrap items-center gap-2">
            <Badge
              variant="secondary"
              className="bg-fuchsia-500/15 uppercase tracking-wider text-fuchsia-200"
            >
              Episodio {numero}
            </Badge>
            {detalle.tono && (
              <Badge variant="outline" className="text-xs font-normal">
                {detalle.tono}
              </Badge>
            )}
          </div>
          <h1 className="text-balance text-3xl font-bold tracking-tight sm:text-4xl md:text-5xl">
            {detalle.titulo}
          </h1>
          <p className="max-w-2xl text-balance text-base leading-relaxed text-muted-foreground sm:text-lg">
            {detalle.logline}
          </p>
        </div>
      </section>

      {/* =====================================================================
          HOOK
          ===================================================================== */}
      {detalle.hook && (
        <section className="mx-auto w-full max-w-3xl px-4 pt-4 sm:pt-8">
          <div className="rounded-xl border border-fuchsia-500/30 bg-fuchsia-500/5 p-5 sm:p-6">
            <div className="mb-2 text-[11px] font-semibold uppercase tracking-[0.18em] text-fuchsia-300/80">
              Hook · 0:00–0:08
            </div>
            <p className="text-sm leading-relaxed text-foreground/95 sm:text-base">
              {detalle.hook}
            </p>
          </div>
        </section>
      )}

      {/* =====================================================================
          STORYBOARD SECUENCIAL — orden estricto por número de shot.
          Una imagen por fila. Caption con plano/composición.
          ===================================================================== */}
      {tieneDetalle && shotsOrdenados.length > 0 && (
        <section className="mx-auto w-full max-w-3xl px-4 py-12 sm:py-16">
          <div className="mb-6 flex items-baseline justify-between gap-4">
            <h2 className="text-xl font-semibold tracking-tight sm:text-2xl">
              Storyboard
            </h2>
            <span className="text-xs uppercase tracking-wider text-muted-foreground">
              {shotsOrdenados.length} shots · orden secuencial
            </span>
          </div>
          <div className="flex flex-col gap-10">
            {shotsOrdenados.map((shot) => (
              <ShotFigure key={shot.slug} shot={shot} />
            ))}
          </div>
        </section>
      )}

      {/* =====================================================================
          BEATS NARRATIVOS — texto limpio, sin imágenes intercaladas.
          ===================================================================== */}
      {tieneDetalle && detalle.beats.length > 0 && (
        <section className="mx-auto w-full max-w-3xl px-4 pb-12 sm:pb-16">
          <h2 className="mb-6 text-xl font-semibold tracking-tight sm:text-2xl">
            Beats narrativos
          </h2>
          <ul className="flex flex-col gap-4">
            {detalle.beats.map((b, i) => (
              <li
                key={i}
                className="text-base leading-relaxed text-foreground/90 sm:text-lg"
              >
                {b}
              </li>
            ))}
          </ul>
        </section>
      )}

      {/* Caps sin storyboard: solo outline. */}
      {!tieneDetalle && detalle.beats.length > 0 && (
        <section className="mx-auto w-full max-w-3xl px-4 py-12 sm:py-16">
          <div className="mb-4 rounded-lg border border-border/50 bg-muted/30 p-4 text-sm text-muted-foreground">
            Este episodio todavía no tiene storyboards generados. Lo que sigue
            es el outline narrativo.
          </div>
          <h2 className="mb-6 text-xl font-semibold tracking-tight sm:text-2xl">
            Beats
          </h2>
          <ul className="flex flex-col gap-4">
            {detalle.beats.map((b, i) => (
              <li
                key={i}
                className="text-base leading-relaxed text-foreground/90 sm:text-lg"
              >
                {b}
              </li>
            ))}
          </ul>
        </section>
      )}

      {/* =====================================================================
          TABLA TÉCNICA
          ===================================================================== */}
      {tieneDetalle && shotsOrdenados.length > 0 && (
        <section className="mx-auto w-full max-w-5xl px-4 py-12 sm:py-16">
          <h2 className="mb-6 text-xl font-semibold tracking-tight sm:text-2xl">
            Tabla técnica
          </h2>
          <div className="overflow-x-auto rounded-xl border border-border/60">
            <table className="w-full min-w-[640px] divide-y divide-border/60 text-left text-sm">
              <thead className="bg-muted/40 text-xs uppercase tracking-wider text-muted-foreground">
                <tr>
                  <th scope="col" className="px-3 py-3 font-medium">
                    Shot
                  </th>
                  <th scope="col" className="px-3 py-3 font-medium">
                    Plano / composición
                  </th>
                  <th scope="col" className="px-3 py-3 font-medium">
                    Personajes
                  </th>
                  <th scope="col" className="px-3 py-3 font-medium">
                    Mood / paleta
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-border/60">
                {shotsOrdenados.map((s) => (
                  <tr key={s.slug} className="align-top">
                    <td className="px-3 py-3 font-mono text-xs">
                      {s.shotNumber !== null
                        ? String(s.shotNumber).padStart(2, "0")
                        : "—"}
                    </td>
                    <td className="px-3 py-3 text-muted-foreground">
                      {s.plano || "—"}
                    </td>
                    <td className="px-3 py-3 text-muted-foreground">
                      {s.personajes || "—"}
                    </td>
                    <td className="px-3 py-3 text-muted-foreground">
                      {s.mood || "—"}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      )}

      {/* =====================================================================
          CLIFFHANGER
          ===================================================================== */}
      {detalle.cliffhanger && (
        <section className="mx-auto w-full max-w-3xl px-4 py-8">
          <div className="rounded-xl border border-border/60 bg-card/50 p-5 sm:p-6">
            <div className="mb-2 text-[11px] font-semibold uppercase tracking-[0.18em] text-muted-foreground">
              Cliffhanger / gancho próximo cap
            </div>
            <p className="text-sm leading-relaxed text-foreground/95 sm:text-base">
              {detalle.cliffhanger}
            </p>
          </div>
        </section>
      )}

      {/* =====================================================================
          PÁGINA CÓMIC — cierre full-width si está disponible.
          ===================================================================== */}
      {tieneDetalle && detalle.comicPage && (
        <section className="mx-auto w-full max-w-4xl px-4 py-12 sm:py-16">
          <div className="mb-4 flex items-baseline justify-between gap-4">
            <h2 className="text-xl font-semibold tracking-tight sm:text-2xl">
              Página cómic
            </h2>
            <span className="text-xs uppercase tracking-wider text-muted-foreground">
              Compilado del cap
            </span>
          </div>
          <div className="overflow-hidden rounded-xl border border-border/60 bg-muted/30 shadow-2xl">
            <Image
              src={detalle.comicPage}
              alt={`Página cómic episodio ${numero}`}
              width={2048}
              height={2730}
              sizes="(max-width: 768px) 100vw, 1024px"
              className="h-auto w-full"
            />
          </div>
        </section>
      )}

      {/* Caps sin comic page: placeholder discreto. */}
      {tieneDetalle && !detalle.comicPage && (
        <section className="mx-auto w-full max-w-3xl px-4 py-12">
          <div className="rounded-xl border border-dashed border-border/60 bg-muted/20 p-6 text-center">
            <div className="mb-2 text-xs uppercase tracking-wider text-muted-foreground">
              Página cómic
            </div>
            <p className="text-sm text-muted-foreground">
              En compilación. Cuando esté lista, vivirá acá.
            </p>
          </div>
        </section>
      )}

      <Separator className="mx-auto my-8 max-w-5xl" />

      {/* =====================================================================
          FOOTER NAV
          ===================================================================== */}
      <section className="mx-auto w-full max-w-5xl px-4 pb-16">
        <div className="grid gap-3 sm:grid-cols-3">
          <NavLinkCard
            href={previo ? `/episodios/${previo.numero}` : null}
            label={
              previo ? `Ep ${previo.numero} — ${previo.titulo}` : "Sin previo"
            }
            direction="prev"
          />
          <NavLinkCard
            href="/lore"
            label="Lore — el mundo entero"
            direction="middle"
          />
          <NavLinkCard
            href={
              siguiente ? `/episodios/${siguiente.numero}` : null
            }
            label={
              siguiente
                ? `Ep ${siguiente.numero} — ${siguiente.titulo}`
                : "Sin siguiente"
            }
            direction="next"
          />
        </div>
      </section>
    </div>
  );
}

// =============================================================================
// Subcomponentes
// =============================================================================

function ShotFigure({ shot }: { shot: StoryboardShot }) {
  const shotLabel =
    shot.shotNumber !== null
      ? `Shot ${String(shot.shotNumber).padStart(2, "0")}`
      : null;
  // Caption técnica: shotLabel · plano · personajes (si los hay)
  const techParts = [shotLabel, shot.plano].filter(Boolean) as string[];
  const personajesLine = shot.personajes && shot.personajes.length > 0
    ? shot.personajes
    : null;

  return (
    <figure className="flex flex-col gap-3">
      <div className="overflow-hidden rounded-xl border border-border/60 bg-muted/30 shadow-2xl">
        <Image
          src={shot.image}
          alt={shot.titulo}
          width={1536}
          height={1024}
          sizes="(max-width: 768px) 100vw, 768px"
          className="h-auto w-full"
        />
      </div>
      <figcaption className="flex flex-col gap-1.5">
        {techParts.length > 0 && (
          <span className="text-[11px] font-mono uppercase tracking-wider text-muted-foreground">
            {techParts.join(" · ")}
          </span>
        )}
        {shot.caption && (
          <span className="text-sm leading-relaxed text-foreground/85 sm:text-base">
            {shot.caption}
          </span>
        )}
        {personajesLine && (
          <span className="text-xs italic text-muted-foreground">
            {personajesLine}
          </span>
        )}
        {shot.mood && (
          <span className="text-xs text-muted-foreground/80">{shot.mood}</span>
        )}
      </figcaption>
    </figure>
  );
}

function NavLinkCard({
  href,
  label,
  direction,
}: {
  href: string | null;
  label: string;
  direction: "prev" | "middle" | "next";
}) {
  const arrow =
    direction === "prev" ? (
      <ArrowLeft className="size-4" aria-hidden />
    ) : direction === "next" ? (
      <ArrowRight className="size-4" aria-hidden />
    ) : null;

  const content = (
    <div className="flex flex-col gap-1.5">
      <span className="flex items-center gap-1 text-[11px] uppercase tracking-wider text-muted-foreground">
        {direction === "prev" && arrow}
        {direction === "prev"
          ? "Anterior"
          : direction === "next"
            ? "Siguiente"
            : "Contexto"}
        {direction === "next" && arrow}
      </span>
      <span className="text-sm font-medium tracking-tight">{label}</span>
    </div>
  );

  if (!href) {
    return (
      <div className="rounded-lg border border-dashed border-border/40 bg-muted/10 p-4 opacity-60">
        {content}
      </div>
    );
  }
  return (
    <Link
      href={href}
      className="group rounded-lg border border-border/60 bg-card/40 p-4 transition-colors hover:border-fuchsia-500/40 hover:bg-fuchsia-500/5"
    >
      {content}
    </Link>
  );
}
