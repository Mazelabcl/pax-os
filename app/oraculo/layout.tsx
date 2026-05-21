/**
 * Layout específico para /oraculo y sub-rutas.
 *
 * Reemplaza el layout global para las rutas del oráculo:
 *   - Sin SiteNav del sitio principal (el hero glassmorphic necesita full-screen limpio)
 *   - Sin footer global
 *   - bg negro puro
 *
 * Cada página del oráculo maneja su propio nav/footer interno si lo necesita.
 */

import type { Metadata } from "next";

export const metadata: Metadata = {
  title: {
    template: "%s | Oráculo Pax",
    default: "Oráculo Pax — Tu carta ancestral",
  },
  description:
    "El Oráculo Pax lee tu momento de nacimiento y te devuelve tu arquetipo de servicio. Pay what you can. 100% se dona.",
};

export default function OraculoLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen bg-black text-white">
      {children}
    </div>
  );
}
