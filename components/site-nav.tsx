import Link from "next/link";
import { cn } from "@/lib/utils";

interface NavLink {
  href: string;
  label: string;
  /** Si true, mostramos un dot rojo discreto a la derecha del label. */
  dot?: boolean;
  /** Si true, lo destacamos con tono atenuado (por ejemplo, archivo legacy). */
  muted?: boolean;
  /** Si true, abre en pestaña nueva (links externos). */
  external?: boolean;
}

const links: NavLink[] = [
  { href: "/", label: "Inicio" },
  { href: "/personajes", label: "El clan" },
  { href: "/episodios/1", label: "Episodios" },
  { href: "/lore", label: "Lore" },
  { href: "/cambios", label: "Cambios", dot: true },
  { href: "/legacy/v2", label: "Archivo", muted: true },
];

interface SiteNavProps {
  className?: string;
}

/**
 * Navegación top fija. Server component. Sin estado activo por ahora.
 * Estructura Quest 2: Inicio / El clan / Episodios / Lore / Cambios / Archivo.
 */
export function SiteNav({ className }: SiteNavProps) {
  return (
    <header
      className={cn(
        "sticky top-0 z-40 w-full border-b border-border bg-background/80 backdrop-blur",
        className,
      )}
    >
      <div className="mx-auto flex h-14 max-w-6xl items-center justify-between gap-4 px-4">
        <Link href="/" className="text-base font-semibold tracking-tight">
          Pax
        </Link>
        <nav className="flex items-center gap-0.5 overflow-x-auto sm:gap-2 text-sm">
          {links.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              target={link.external ? "_blank" : undefined}
              rel={link.external ? "noreferrer" : undefined}
              className={cn(
                "relative inline-flex items-center gap-1.5 whitespace-nowrap rounded-md px-2 py-1 transition-colors",
                link.muted
                  ? "text-muted-foreground/70 hover:bg-accent hover:text-foreground"
                  : "text-muted-foreground hover:bg-accent hover:text-foreground",
              )}
            >
              {link.label}
              {link.dot && (
                <span
                  aria-label="hay novedades"
                  className="size-1.5 rounded-full bg-red-500"
                />
              )}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
