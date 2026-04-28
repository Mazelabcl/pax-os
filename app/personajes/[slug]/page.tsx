import Image from "next/image";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft } from "lucide-react";
import {
  getPersonajeDetail,
  listPersonajeSlugs,
  personajeFilePath,
} from "@/lib/personajes";
import { getLastUpdated } from "@/lib/git";
import { CopyButton } from "@/components/copy-button";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";

interface PageProps {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  const slugs = await listPersonajeSlugs();
  return slugs.map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: PageProps) {
  const { slug } = await params;
  const personaje = await getPersonajeDetail(slug);
  if (!personaje) {
    return { title: "Personaje no encontrado — Pax" };
  }
  return {
    title: `${personaje.name} — Pax`,
    description: personaje.shortDescription || `Ficha de ${personaje.name}.`,
  };
}

export default async function PersonajeDetailPage({ params }: PageProps) {
  const { slug } = await params;
  const personaje = await getPersonajeDetail(slug);

  if (!personaje) {
    notFound();
  }

  const updated = await getLastUpdated(personajeFilePath(slug));

  return (
    <div className="mx-auto max-w-4xl px-4 py-8 sm:py-12">
      <div className="mb-6">
        <Button asChild variant="ghost" size="sm" className="-ml-2">
          <Link href="/personajes">
            <ArrowLeft className="size-4" aria-hidden />
            Volver a personajes
          </Link>
        </Button>
      </div>

      {personaje.image && (
        <div className="mb-6 overflow-hidden rounded-xl border border-border">
          <div className="relative aspect-square w-full max-w-md bg-muted">
            <Image
              src={personaje.image}
              alt={personaje.name}
              fill
              sizes="(max-width: 768px) 100vw, 28rem"
              priority
              className="object-cover"
            />
          </div>
        </div>
      )}

      <div className="mb-6 flex flex-wrap items-center gap-3">
        <h1 className="text-3xl font-bold tracking-tight sm:text-4xl">
          {personaje.name}
        </h1>
        {updated && (
          <Badge variant="outline" className="text-xs font-normal">
            Última actualización: {updated}
          </Badge>
        )}
      </div>

      {personaje.descripcion && (
        <section className="mb-8">
          <h2 className="mb-2 text-lg font-semibold tracking-tight">
            Descripción
          </h2>
          <p className="whitespace-pre-line text-sm leading-relaxed text-muted-foreground sm:text-base">
            {personaje.descripcion}
          </p>
        </section>
      )}

      {personaje.rol && (
        <section className="mb-8">
          <h2 className="mb-2 text-lg font-semibold tracking-tight">
            Rol en la historia
          </h2>
          <p className="whitespace-pre-line text-sm leading-relaxed text-muted-foreground sm:text-base">
            {personaje.rol}
          </p>
        </section>
      )}

      {personaje.marca && (
        <section className="mb-8">
          <h2 className="mb-2 text-lg font-semibold tracking-tight">
            Marca distintiva visual
          </h2>
          <p className="whitespace-pre-line text-sm leading-relaxed text-muted-foreground sm:text-base">
            {personaje.marca}
          </p>
        </section>
      )}

      <Separator className="my-8" />

      {personaje.prompt && (
        <section className="mb-8">
          <div className="mb-3 flex flex-wrap items-center justify-between gap-3">
            <h2 className="text-lg font-semibold tracking-tight">
              Prompt visual
            </h2>
            <CopyButton text={personaje.prompt} label="Copiar prompt" />
          </div>
          <div className="rounded-lg border border-border bg-card p-4">
            <pre className="whitespace-pre-wrap break-words font-mono text-xs leading-relaxed text-foreground/90">
              {personaje.prompt}
            </pre>
          </div>
        </section>
      )}

      {personaje.seed && (
        <section className="mb-8">
          <h2 className="mb-2 text-lg font-semibold tracking-tight">Seed</h2>
          <code className="inline-block rounded-md border border-border bg-muted px-2 py-1 font-mono text-xs">
            {personaje.seed}
          </code>
        </section>
      )}
    </div>
  );
}
