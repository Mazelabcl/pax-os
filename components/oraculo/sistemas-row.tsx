/**
 * SistemasRow — badge row que muestra los 4 sistemas del Oráculo Pax.
 * Aparece en el header de la carta, en /como-funciona y en /resultado.
 * Iconos SVG inline minimalistas por sistema.
 */

interface SistemasRowProps {
  size?: "sm" | "md";
  className?: string;
}

const sistemas = [
  {
    key: "maya",
    label: "Maya",
    color: "#C084FC",
    icon: (
      // Rombo — glifo maya estilizado
      <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
        <rect x="6" y="1" width="5" height="5" rx="0.5" transform="rotate(45 6 1)" fill="currentColor" opacity="0.8" />
      </svg>
    ),
  },
  {
    key: "astral",
    label: "Astral",
    color: "#67E8F9",
    icon: (
      // Estrella de 6 puntas estilizada
      <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
        <circle cx="6" cy="6" r="1.5" fill="currentColor" />
        <circle cx="6" cy="1" r="1" fill="currentColor" opacity="0.7" />
        <circle cx="6" cy="11" r="1" fill="currentColor" opacity="0.7" />
        <circle cx="1" cy="6" r="1" fill="currentColor" opacity="0.7" />
        <circle cx="11" cy="6" r="1" fill="currentColor" opacity="0.7" />
      </svg>
    ),
  },
  {
    key: "pax",
    label: "Pax",
    color: "#B43FFF",
    icon: (
      // Cristal heptagonal — símbolo Pax
      <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
        <polygon
          points="6,0.5 9.5,2.5 11,6 9.5,9.5 6,11.5 2.5,9.5 1,6 2.5,2.5"
          fill="currentColor"
          opacity="0.8"
        />
      </svg>
    ),
  },
  {
    key: "gesto",
    label: "Gesto",
    color: "#FCD34D",
    icon: (
      // Espiral — ciclo de reciprocidad
      <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
        <circle cx="6" cy="6" r="4.5" stroke="currentColor" strokeWidth="1.2" fill="none" opacity="0.7" />
        <circle cx="6" cy="6" r="2" stroke="currentColor" strokeWidth="1" fill="none" opacity="0.5" />
        <circle cx="6" cy="6" r="0.8" fill="currentColor" opacity="0.8" />
      </svg>
    ),
  },
];

export function SistemasRow({ size = "sm", className = "" }: SistemasRowProps) {
  const textSize = size === "md" ? "11px" : "10px";
  const gap = size === "md" ? "10px" : "8px";

  return (
    <div
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap,
        flexWrap: "wrap",
      }}
      className={className}
    >
      {sistemas.map(({ key, label, color, icon }, i) => (
        <span
          key={key}
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: "4px",
            color,
            fontSize: textSize,
            fontFamily: "Inter, sans-serif",
            fontWeight: 300,
            letterSpacing: "0.06em",
          }}
        >
          {i > 0 && (
            <span style={{ color: "#333", fontSize: "9px", margin: "0 2px" }}>✦</span>
          )}
          <span style={{ color }}>{icon}</span>
          <span style={{ textTransform: "uppercase", color, opacity: 0.9 }}>{label}</span>
        </span>
      ))}
    </div>
  );
}
