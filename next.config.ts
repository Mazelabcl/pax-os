import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Aseguramos que `content/**/*.md` y la metadata de git viajen al bundle de Vercel.
  // Necesario porque las páginas lo leen vía `fs` en server components.
  outputFileTracingIncludes: {
    "/lore": ["./content/**/*"],
    "/personajes/**": ["./content/**/*"],
    "/episodio-1/**": ["./content/**/*"],
  },
};

export default nextConfig;
