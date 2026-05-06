import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Solo incluir markdown y metadata git en el bundle serverless.
  // Las imágenes viven en public/ y Vercel las sirve via CDN — NO van al lambda.
  // Antes incluíamos content/**/* completo (141MB) y excedía el bundle limit.
  outputFileTracingIncludes: {
    "/": ["./content/**/*.md"],
    "/lore": ["./content/**/*.md"],
    "/personajes": ["./content/**/*.md"],
    "/personajes/**": ["./content/**/*.md"],
    "/episodio-1/**": ["./content/**/*.md"],
    "/episodios/**": ["./content/**/*.md"],
    "/cambios": ["./content/CHANGELOG.md"],
    "/principles": ["./content/principles.md"],
    "/roadmap": ["./content/roadmap.md"],
  },
  // Excluir explícitamente carpetas de imágenes en content/ del tracing.
  outputFileTracingExcludes: {
    "*": [
      "./content/storyboards/**/*.png",
      "./content/storyboards/**/*.jpg",
      "./content/exploratory-images/**",
      "./content/test-images/**",
      "./content/v2/**/*.png",
      "./feedback/**",
    ],
  },
};

export default nextConfig;
