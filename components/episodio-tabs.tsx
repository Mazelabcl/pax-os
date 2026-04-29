"use client";

import { useEffect, useState } from "react";
import { useSearchParams, useRouter, usePathname } from "next/navigation";
import {
  Tabs,
  TabsList,
  TabsTrigger,
  TabsContent,
} from "@/components/ui/tabs";

interface EpisodioTabsProps {
  /** IDs y labels de las tabs principales. */
  triggers: { value: string; label: string }[];
  /** Tab por default si no hay query param. */
  defaultValue: string;
  /** Nombre del query param. Default: "tab". */
  paramName?: string;
  children: React.ReactNode;
}

/**
 * Tabs principales del episodio que sincroniza el tab activo con el query
 * param `?tab=` y permite que un anchor (`#concept-…`) haga scroll al item
 * dentro de la tab seleccionada.
 *
 * Cuando se cambia de tab manualmente, hace `replace` del URL (sin scroll
 * para no perder el contexto en mobile).
 */
export function EpisodioTabs({
  triggers,
  defaultValue,
  paramName = "tab",
  children,
}: EpisodioTabsProps) {
  const searchParams = useSearchParams();
  const router = useRouter();
  const pathname = usePathname();

  // Derivamos el value directamente del searchParams (sin setState en effect).
  // Si hay override local (usuario clickeó una tab), respetamos ese.
  const validValues = new Set(triggers.map((t) => t.value));
  const fromUrl = searchParams.get(paramName);
  const urlValue =
    fromUrl && validValues.has(fromUrl) ? fromUrl : defaultValue;

  // Override local (usuario clickeó una tab). Cuando coincide con la URL,
  // back/forward del browser gobiernan de nuevo. No hace falta setState extra:
  // el `replace` del router en `handleChange` actualiza el searchParams.
  const [localOverride, setLocalOverride] = useState<string | null>(null);
  const value = localOverride ?? urlValue;

  // Después de montar / cambiar de tab, si hay anchor en URL, scroll al elemento.
  useEffect(() => {
    if (typeof window === "undefined") return;
    if (window.location.hash) {
      const id = decodeURIComponent(window.location.hash.slice(1));
      // Esperá un tick a que la tab activa renderee el contenido.
      requestAnimationFrame(() => {
        const el = document.getElementById(id);
        if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    }
  }, [value]);

  function handleChange(next: string) {
    setLocalOverride(next);
    // Persistir en URL sin scroll.
    const params = new URLSearchParams(searchParams.toString());
    if (next === defaultValue) {
      params.delete(paramName);
    } else {
      params.set(paramName, next);
    }
    const qs = params.toString();
    router.replace(`${pathname}${qs ? `?${qs}` : ""}`, { scroll: false });
  }

  return (
    <Tabs value={value} onValueChange={handleChange} className="w-full">
      <div className="-mx-4 mb-6 overflow-x-auto px-4">
        <TabsList className="h-9">
          {triggers.map((t) => (
            <TabsTrigger key={t.value} value={t.value}>
              {t.label}
            </TabsTrigger>
          ))}
        </TabsList>
      </div>
      {children}
    </Tabs>
  );
}

export { TabsContent };
