import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Solo incluir markdown y metadata git en el bundle serverless.
  // Las imágenes viven en public/ y Vercel las sirve via CDN — NO van al lambda.
  // Desde la Fase 2 de reorg los .md viven repartidos en _lore/, gestos/, _meta/
  // y content/CHANGELOG.md. _archive/ también va por compatibilidad con rutas
  // legacy (episodio-1).
  outputFileTracingIncludes: {
    "/": [
      "./content/**/*.md",
      "./_lore/**/*.md",
      "./gestos/**/*.md",
      "./_meta/**/*.md",
      "./_archive/content-episodio-1/**/*.md",
    ],
  },
  // Excluir explícitamente todo lo binario y pesado del tracing serverless.
  // Las imágenes viven en public/ (CDN de Vercel) — NO van al lambda.
  outputFileTracingExcludes: {
    "*": [
      // Cualquier binario donde sea — al lambda solo van los .md
      "./content/**/*.png",
      "./content/**/*.jpg",
      "./content/**/*.jpeg",
      "./content/**/*.webp",
      "./content/**/*.mp4",
      "./content/**/*.webm",
      "./content/**/*.rar",
      "./content/**/*.zip",
      "./_lore/**/*.png",
      "./_lore/**/*.jpg",
      "./_lore/**/*.jpeg",
      "./_lore/**/*.webp",
      "./gestos/**/*.png",
      "./gestos/**/*.jpg",
      "./gestos/**/*.jpeg",
      "./gestos/**/*.webp",
      "./gestos/**/*.mp4",
      "./gestos/**/*.webm",
      "./_archive/**/*.png",
      "./_archive/**/*.jpg",
      "./_archive/**/*.jpeg",
      "./_archive/**/*.webp",
      "./_archive/**/*.mp4",
      "./_archive/**/*.webm",
      // Carpetas de descarte / histórico explícitamente
      "./gestos/01-miniserie/storyboards/**/*.png",
      "./gestos/01-miniserie/storyboards/**/*.jpg",
      "./gestos/02-oraculo/visuals/**",
      "./gestos/04-video-bg/_descarte/**",
      "./gestos/04-video-bg/video1-deep-dive/**/*.png",
      "./gestos/04-video-bg/video2-gem-chase/**/*.png",
      "./_archive/canon-v2/**",
      "./_archive/content-test-images/**",
      "./_archive/content-exploratory-images/**",
      "./_archive/video-bg-v1/**",
      "./content/videos/**",
      "./feedback/**",
      // Carpetas fuera del runtime serverless
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
