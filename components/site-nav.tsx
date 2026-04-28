import Link from "next/link";
import { cn } from "@/lib/utils";

interface NavLink {
  href: string;
  label: string;
  /** Si true, mostramos un dot rojo discreto a la derecha del label. */
  dot?: boolean;
}

const links: NavLink[] = [
  { href: "/", label: "Inicio" },
  { href: "/lore", label: "Lore" },
  { href: "/personajes", label: "Personajes" },
  { href: "/episodio-1", label: "Episodio 1" },
  { href: "/cambios", label: "Cambios", dot: true },
];

interface SiteNavProps {
  className?: string;
}

/**
 * Navegación top fija. Server component. Sin estado activo por ahora —
 * se puede sumar `usePathname` en una v2 si aldot lo pide.
 */
export function SiteNav({ className }: SiteNavProps) {
  return (
    <header
      className={cn(
        "sticky top-0 z-40 w-full border-b border-border bg-background/80 backdrop-blur",
        className,
      )}
    >
      <div className="mx-auto flex h-14 max-w-5xl items-center justify-between gap-4 px-4">
        <Link
          href="/"
          className="text-base font-semibold tracking-tight"
        >
          Pax
        </Link>
        <nav className="flex items-center gap-1 sm:gap-3 text-sm">
          {links.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className="relative inline-flex items-center gap-1.5 rounded-md px-2 py-1 text-muted-foreground transition-colors hover:bg-accent hover:text-foreground"
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
