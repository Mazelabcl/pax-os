import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Aseguramos que `content/**/*.md` y la metadata de git viajen al bundle de Vercel.
  // Necesario porque las páginas lo leen vía `fs` en server components.
  outputFileTracingIncludes: {
    "/": ["./content/**/*"],
    "/lore": ["./content/**/*"],
    "/personajes": ["./content/**/*", "./public/images/personajes/**"],
    "/personajes/**": ["./content/**/*", "./public/images/personajes/**"],
    "/episodio-1/**": ["./content/**/*"],
    "/cambios": ["./content/**/*"],
  },
};

export default nextConfig;
