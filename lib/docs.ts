import { readMarkdown } from "@/lib/markdown";

export interface DocMeta {
  slug: string;
  /** Path relativo a content/ — se pasa directo a readMarkdown */
  contentPath: string;
  /** Path "legible" para mostrar al usuario en la UI */
  displayPath: string;
  title: string;
  description: string;
}

export const DOCS_MANIFEST: DocMeta[] = [
  {
    slug: "pax-core",
    contentPath: "pax-core.md",
    displayPath: "content/pax-core.md",
    title: "Pax Core — Documento Madre",
    description:
      "Source-of-truth maestro del proyecto. La esencia, el lore y los pilares narrativos en un solo lugar.",
  },
  {
    slug: "naming-rukla",
    contentPath: "pax-core/naming-rukla.md",
    displayPath: "content/pax-core/naming-rukla.md",
    title: "Naming — Alternativas a RUKLA",
    description:
      "12 propuestas para reemplazar el nombre temporal RUKLA, organizadas en 4 categorías con top 3 recomendado.",
  },
  {
    slug: "oraculo-lore",
    contentPath: "pax-oraculo/_lore.md",
    displayPath: "content/pax-oraculo/_lore.md",
    title: "Oráculo Pax — Lore",
    description:
      "Lore diegético del Oráculo Pax: cómo existe en la mitología y cómo el visitante lo experimenta.",
  },
  {
    slug: "oraculo-research",
    contentPath: "pax-oraculo/_research.md",
    displayPath: "content/pax-oraculo/_research.md",
    title: "Oráculo Pax — Research místico",
    description:
      "Research sobre sistemas ancestrales (astrología, Tzolkin, arquetipos) + APIs para el MVP del Oráculo.",
  },
  {
    slug: "oraculo-variantes",
    contentPath: "pax-oraculo/_variantes-visuales.md",
    displayPath: "content/pax-oraculo/_variantes-visuales.md",
    title: "Oráculo Pax — Variantes visuales",
    description:
      "5 propuestas estéticas para el MVP del Oráculo + 20 prompts GPT Image 2 listos para generar.",
  },
  {
    slug: "oraculo-card",
    contentPath: "pax-oraculo/_card-design.md",
    displayPath: "content/pax-oraculo/_card-design.md",
    title: "Oráculo Pax — Card Design",
    description:
      "Especificación del producto-carta del Oráculo Pax. Guía para el frontend developer del MVP.",
  },
  {
    slug: "video-bg-final",
    contentPath: "video-bg-v2/_FINAL.md",
    displayPath: "content/video-bg-v2/_FINAL.md",
    title: "Video BG — Entregables finales",
    description:
      "2 videos de fondo para el sitio: imagen inicial, imagen final, prompt Seedance y descripción por video.",
  },
  {
    slug: "video-bg-beats",
    contentPath: "video-bg-v2/_beat-sheet-pax-pixar.md",
    displayPath: "content/video-bg-v2/_beat-sheet-pax-pixar.md",
    title: "Video BG — Beat sheet Pax-Pixar",
    description:
      "Beat sheet v2 de los 2 videos de fondo. Reemplaza el archivo v1 descartado por ser visualmente genérico.",
  },
];

/** Slugs válidos — usados para validar en getDocBySlug */
const VALID_SLUGS = new Set(DOCS_MANIFEST.map((d) => d.slug));

export interface DocContent {
  meta: DocMeta;
  content: string;
}

/**
 * Devuelve metadatos + contenido del .md para un slug dado.
 * Valida que el slug exista en el manifest (sin traversal).
 * Lanza si el slug es inválido o el archivo no se puede leer.
 */
export async function getDocBySlug(slug: string): Promise<DocContent> {
  if (!VALID_SLUGS.has(slug)) {
    throw new Error(`Slug desconocido: "${slug}"`);
  }

  const meta = DOCS_MANIFEST.find((d) => d.slug === slug)!;
  const doc = await readMarkdown(meta.contentPath);

  return {
    meta,
    content: doc.content,
  };
}

/** Devuelve el manifest completo. */
export function listAllDocs(): DocMeta[] {
  return DOCS_MANIFEST;
}
