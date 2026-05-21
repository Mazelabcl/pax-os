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
  // Excluir explícitamente todo lo binario y pesado del tracing serverless.
  // Las imágenes viven en public/ (CDN de Vercel) — NO van al lambda.
  outputFileTracingExcludes: {
    "*": [
      // Cualquier binario en content/ — al lambda solo van los .md
      "./content/**/*.png",
      "./content/**/*.jpg",
      "./content/**/*.jpeg",
      "./content/**/*.webp",
      "./content/**/*.mp4",
      "./content/**/*.webm",
      "./content/**/*.rar",
      "./content/**/*.zip",
      // Carpetas de descarte / histórico explícitamente
      "./content/storyboards/**/*.png",
      "./content/storyboards/**/*.jpg",
      "./content/exploratory-images/**",
      "./content/test-images/**",
      "./content/v2/**/*.png",
      "./content/video-bg-v1-archivo/**",
      "./content/video-bg-v2/**/*.png",
      "./content/canon-v2/**",
      "./content/pax-oraculo/visuals/**",
      "./content/videos/**",
      "./feedback/**",
      // Carpetas fuera de content/ que no son lambda runtime
      "./personajes finales/**",
      "./Personajes-Fix/**",
      "./pax/**",
      "./logs/**",
      "./landing-experiment/**",
      "./scripts/**",
      // Públicos — Vercel los sirve via CDN, no entran al lambda
      "./public/videos/**",
    ],
  },
};

export default nextConfig;
