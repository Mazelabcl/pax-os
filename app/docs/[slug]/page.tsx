import { notFound } from "next/navigation";
import Link from "next/link";
import { getDocBySlug, listAllDocs } from "@/lib/docs";
import { MarkdownRenderer } from "@/components/markdown-renderer";
import type { Metadata } from "next";

interface PageProps {
  params: Promise<{ slug: string }>;
}

/** Pre-genera los 8 slugs estáticos al build. */
export function generateStaticParams() {
  return listAllDocs().map((doc) => ({ slug: doc.slug }));
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { slug } = await params;
  const docs = listAllDocs();
  const meta = docs.find((d) => d.slug === slug);
  if (!meta) return { title: "Docs — Pax" };

  return {
    title: `${meta.title} — Pax`,
    description: meta.description,
  };
}

export default async function DocPage({ params }: PageProps) {
  const { slug } = await params;

  let doc;
  try {
    doc = await getDocBySlug(slug);
  } catch {
    notFound();
  }

  return (
    <div className="mx-auto max-w-4xl px-4 py-10 sm:py-14">
      {/* Breadcrumb */}
      <nav className="mb-8 flex items-center gap-1.5 text-xs text-muted-foreground">
        <Link href="/docs" className="hover:text-foreground transition-colors">
          Docs
        </Link>
        <span>/</span>
        <span className="text-foreground/70">{doc.meta.title}</span>
      </nav>

      {/* Contenido markdown */}
      <MarkdownRenderer
        className={[
          // Sobrescribir colores de acento para alinear con paleta Pax
          "prose-a:text-[#3DCCA3] hover:prose-a:text-[#3DCCA3]/80",
          "prose-headings:text-foreground",
          // Tablas con borde visible
          "prose-table:border-collapse",
          "prose-th:border prose-th:border-border prose-th:bg-muted prose-th:px-3 prose-th:py-2",
          "prose-td:border prose-td:border-border prose-td:px-3 prose-td:py-2",
          // Blockquotes con acento magenta
          "prose-blockquote:border-l-[#EC4899] prose-blockquote:text-muted-foreground",
          // Hr sutil
          "prose-hr:border-border",
        ].join(" ")}
      >
        {doc.content}
      </MarkdownRenderer>

      {/* Footer */}
      <footer className="mt-16 flex flex-col gap-3 border-t border-border pt-6 sm:flex-row sm:items-center sm:justify-between">
        <code className="text-[11px] text-muted-foreground/60 font-mono">
          {doc.meta.displayPath}
        </code>
        <Link
          href="/docs"
          className="text-xs text-[#3DCCA3] hover:text-[#3DCCA3]/80 transition-colors"
        >
          ← Volver a Docs
        </Link>
      </footer>
    </div>
  );
}
