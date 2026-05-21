import Link from "next/link";
import { listAllDocs } from "@/lib/docs";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Docs — Pax",
  description: "Documentos vivos del proyecto Pax. Lore, naming, research, beats y diseños.",
};

export default function DocsIndexPage() {
  const docs = listAllDocs();

  return (
    <div className="mx-auto max-w-5xl px-4 py-12 sm:py-16">
      {/* Header */}
      <div className="mb-10 space-y-2">
        <p className="text-xs font-semibold uppercase tracking-widest text-[#3DCCA3]">
          Documentos vivos
        </p>
        <h1 className="text-3xl font-semibold tracking-tight sm:text-4xl">
          Pax Docs
        </h1>
        <p className="max-w-xl text-sm text-muted-foreground sm:text-base">
          Lore, naming, research, beats y diseños. Todo lo que define el universo Pax
          en un solo lugar.
        </p>
      </div>

      {/* Grid */}
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
        {docs.map((doc) => (
          <Link
            key={doc.slug}
            href={`/docs/${doc.slug}`}
            className="group relative flex flex-col gap-2 rounded-xl border border-border bg-card p-5 transition-colors hover:border-[#B43FFF]/60 hover:bg-accent"
          >
            {/* Title */}
            <h2 className="text-sm font-semibold leading-tight text-foreground group-hover:text-[#B43FFF] transition-colors sm:text-base">
              {doc.title}
            </h2>

            {/* Description */}
            <p className="text-xs text-muted-foreground leading-relaxed sm:text-sm">
              {doc.description}
            </p>

            {/* Footer: path + arrow */}
            <div className="mt-auto flex items-center justify-between pt-3">
              <code className="text-[10px] text-muted-foreground/60 font-mono truncate max-w-[80%]">
                {doc.displayPath}
              </code>
              <span className="text-[#EC4899] text-xs opacity-0 transition-opacity group-hover:opacity-100">
                →
              </span>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
