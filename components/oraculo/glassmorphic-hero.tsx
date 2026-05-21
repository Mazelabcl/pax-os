"use client";

/**
 * GlassmorphicHero v2 — hero del Oráculo Pax rediseñado.
 *
 * Mejoras sobre v1:
 *  - Copy explícito que nombra los 3 sistemas (maya × astral × pax)
 *  - Capas CSS de cristales pulsando sobre el video bg
 *  - Capa de constelación dorada flotante
 *  - Footer de card con los 4 pilares: maya ✦ astral ✦ pax ✦ gesto
 *  - Componente SistemasRow integrado debajo del título
 *  - Mobile-first: card responde al viewport en mobile
 */

import { useRouter } from "next/navigation";

interface GlassmorphicHeroProps {
  onCtaClick?: () => void;
}

export function GlassmorphicHero({ onCtaClick }: GlassmorphicHeroProps) {
  const router = useRouter();

  const handleCta = () => {
    if (onCtaClick) {
      onCtaClick();
    } else {
      const formEl = document.getElementById("oraculo-form");
      if (formEl) {
        formEl.scrollIntoView({ behavior: "smooth" });
      }
    }
  };

  return (
    <>
      {/* Fonts + animations */}
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500&display=swap');
        @font-face {
          font-family: 'Didot';
          src: url('https://db.onlinewebfonts.com/c/251039e6849ad977a8bfc40b564dce89?family=Didot') format('woff2');
          font-weight: normal;
          font-style: normal;
        }

        .oraculo-serif { font-family: 'Didot', 'Didot LT STD', 'GFS Didot', Georgia, serif; }
        .oraculo-sans  { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }

        /* Botón glow naranja-coral exacto del brief */
        .oraculo-btn-glow {
          background: linear-gradient(to bottom, rgba(255,140,70,0.10), transparent);
          box-shadow: 0 4px 30px rgba(0,0,0,0.5),
                      inset 0 1px 0 rgba(255,140,70,0.5),
                      inset 0 0 0 1px rgba(255,255,255,0.1),
                      inset 0 -1px 2px rgba(0,0,0,0.8);
          transition: box-shadow 0.3s ease;
        }
        .oraculo-btn-glow:hover {
          box-shadow: 0 4px 30px rgba(0,0,0,0.5),
                      0 0 20px rgba(255,120,50,0.25),
                      inset 0 1px 0 rgba(255,140,70,0.7),
                      inset 0 0 0 1px rgba(255,255,255,0.15),
                      inset 0 -1px 2px rgba(0,0,0,0.8);
          background-image: radial-gradient(circle at center, rgba(255,120,50,0.1) 0%, transparent 70%),
                            linear-gradient(to bottom, rgba(255,140,70,0.10), transparent);
        }

        /* Film grain noise */
        .oraculo-noise {
          position: absolute;
          inset: 0;
          background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
          opacity: 0.04;
          pointer-events: none;
          z-index: 10;
        }

        /* Cristales pulsando — capa sobre el video */
        @keyframes cristal-pulse-1 {
          0%, 100% { opacity: 0.18; transform: scale(1); }
          50%       { opacity: 0.38; transform: scale(1.12); }
        }
        @keyframes cristal-pulse-2 {
          0%, 100% { opacity: 0.10; transform: scale(1); }
          50%       { opacity: 0.25; transform: scale(1.08); }
        }
        @keyframes cristal-pulse-3 {
          0%, 100% { opacity: 0.08; transform: scale(1); }
          60%       { opacity: 0.20; transform: scale(1.15); }
        }
        .cristal-layer-1 {
          animation: cristal-pulse-1 4s ease-in-out infinite;
        }
        .cristal-layer-2 {
          animation: cristal-pulse-2 6s ease-in-out infinite 1.5s;
        }
        .cristal-layer-3 {
          animation: cristal-pulse-3 5s ease-in-out infinite 3s;
        }

        /* Constelación flotando */
        @keyframes constelacion-float {
          0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0.12; }
          33%       { transform: translateY(-8px) rotate(1deg); opacity: 0.2; }
          66%       { transform: translateY(4px) rotate(-0.5deg); opacity: 0.15; }
        }
        .constelacion-layer {
          animation: constelacion-float 12s ease-in-out infinite;
        }

        /* Anchor cristal violeta header */
        @keyframes anchor-pulse {
          0%, 100% { opacity: 0.6; filter: drop-shadow(0 0 4px rgba(180,63,255,0.6)); }
          50%       { opacity: 1; filter: drop-shadow(0 0 8px rgba(180,63,255,1)); }
        }
        .anchor-cristal {
          animation: anchor-pulse 3s ease-in-out infinite;
        }

        /* Partículas doradas flotando */
        @keyframes particle-float-1 {
          0%,100% { transform: translate(0,0) scale(1); opacity: 0.5; }
          50%     { transform: translate(3px,-8px) scale(1.3); opacity: 0.8; }
        }
        @keyframes particle-float-2 {
          0%,100% { transform: translate(0,0) scale(1); opacity: 0.3; }
          50%     { transform: translate(-4px,-6px) scale(1.2); opacity: 0.6; }
        }
        @keyframes particle-float-3 {
          0%,100% { transform: translate(0,0) scale(0.8); opacity: 0.4; }
          50%     { transform: translate(5px,4px) scale(1.1); opacity: 0.7; }
        }
      `}</style>

      {/* Wrapper */}
      <div
        className="flex flex-col items-center justify-center w-full bg-black"
        style={{ backgroundColor: "#000000", minHeight: "calc(100vh - 56px)", gap: "16px" }}
      >
        {/* Breadcrumb tipográfico Pax — ambient */}
        <p
          className="oraculo-serif"
          style={{
            fontSize: "11px",
            letterSpacing: "0.35em",
            opacity: 0.3,
            color: "#B43FFF",
            fontStyle: "italic",
            userSelect: "none",
            textAlign: "center",
          }}
        >
          PAX · SISTEMA · GESTO
        </p>

        {/* Card — fijo 600×800 en desktop, responsive en mobile */}
        <div
          className="relative overflow-hidden"
          style={{
            width: "min(600px, 90vw)",
            height: "min(800px, calc(90vw * 4/3))",
            maxHeight: "90vh",
            background: "#000",
            boxShadow: "0 0 80px rgba(180,63,255,0.18), 0 25px 50px rgba(0,0,0,0.9)",
            borderRadius: "2px",
          }}
        >
          {/* ── Background video Pax-canon ── */}
          <div
            style={{
              position: "absolute",
              inset: 0,
              zIndex: 1,
              overflow: "hidden",
            }}
          >
            <video
              autoPlay
              loop
              muted
              playsInline
              preload="auto"
              style={{
                position: "absolute",
                inset: 0,
                width: "100%",
                height: "100%",
                objectFit: "cover",
                opacity: 0.7,
              }}
            >
              <source src="/videos/oraculo-hero-loop.webm" type="video/webm" />
              <source src="/videos/oraculo-hero-loop.mp4" type="video/mp4" />
            </video>
            {/* Partículas doradas suspendidas */}
            <div
              style={{
                position: "absolute",
                inset: 0,
                zIndex: 2,
                pointerEvents: "none",
                backgroundImage:
                  "radial-gradient(circle 1.5px at 12% 18%, rgba(251,191,36,0.9) 0%, transparent 100%), " +
                  "radial-gradient(circle 1px at 28% 40%, rgba(251,191,36,0.7) 0%, transparent 100%), " +
                  "radial-gradient(circle 2px at 58% 12%, rgba(251,191,36,0.8) 0%, transparent 100%), " +
                  "radial-gradient(circle 1px at 72% 28%, rgba(251,191,36,0.6) 0%, transparent 100%), " +
                  "radial-gradient(circle 1.5px at 45% 58%, rgba(251,191,36,0.7) 0%, transparent 100%), " +
                  "radial-gradient(circle 1px at 88% 45%, rgba(251,191,36,0.5) 0%, transparent 100%), " +
                  "radial-gradient(circle 1px at 18% 72%, rgba(251,191,36,0.6) 0%, transparent 100%), " +
                  "radial-gradient(circle 2px at 65% 75%, rgba(251,191,36,0.4) 0%, transparent 100%), " +
                  "radial-gradient(circle 1px at 35% 85%, rgba(251,191,36,0.5) 0%, transparent 100%), " +
                  "radial-gradient(circle 1.5px at 92% 80%, rgba(251,191,36,0.3) 0%, transparent 100%)",
                animation: "constelacion-float 12s ease-in-out infinite",
              }}
            />
          </div>

          {/* ── Capa cristales pulsando — violeta+magenta+dorado ── */}
          <div
            className="cristal-layer-1"
            style={{
              position: "absolute",
              inset: 0,
              zIndex: 3,
              pointerEvents: "none",
              background:
                "radial-gradient(ellipse 60% 40% at 30% 25%, rgba(180,63,255,0.28) 0%, transparent 70%), " +
                "radial-gradient(ellipse 40% 30% at 70% 65%, rgba(236,72,153,0.18) 0%, transparent 65%)",
            }}
          />
          <div
            className="cristal-layer-2"
            style={{
              position: "absolute",
              inset: 0,
              zIndex: 3,
              pointerEvents: "none",
              background:
                "radial-gradient(ellipse 35% 50% at 75% 20%, rgba(251,191,36,0.12) 0%, transparent 60%)",
            }}
          />
          <div
            className="cristal-layer-3"
            style={{
              position: "absolute",
              inset: 0,
              zIndex: 3,
              pointerEvents: "none",
              background:
                "radial-gradient(ellipse 50% 35% at 20% 80%, rgba(180,63,255,0.15) 0%, transparent 55%)",
            }}
          />

          {/* ── Capa constelación dorada flotante ── */}
          <div
            className="constelacion-layer"
            style={{
              position: "absolute",
              inset: 0,
              zIndex: 4,
              pointerEvents: "none",
              backgroundImage:
                "radial-gradient(circle 1px at 15% 20%, rgba(251,191,36,0.7) 0%, transparent 100%), " +
                "radial-gradient(circle 1px at 40% 35%, rgba(251,191,36,0.5) 0%, transparent 100%), " +
                "radial-gradient(circle 1.5px at 65% 18%, rgba(251,191,36,0.6) 0%, transparent 100%), " +
                "radial-gradient(circle 1px at 80% 30%, rgba(251,191,36,0.4) 0%, transparent 100%), " +
                "radial-gradient(circle 1px at 55% 55%, rgba(251,191,36,0.5) 0%, transparent 100%), " +
                "radial-gradient(circle 1.5px at 25% 65%, rgba(251,191,36,0.3) 0%, transparent 100%), " +
                "radial-gradient(circle 1px at 85% 70%, rgba(251,191,36,0.4) 0%, transparent 100%), " +
                "radial-gradient(circle 1px at 10% 82%, rgba(251,191,36,0.3) 0%, transparent 100%)",
            }}
          />

          {/* ── Film grain noise ── */}
          <div className="oraculo-noise" style={{ zIndex: 5 }} />

          {/* ── Gradient overlay superior/inferior ── */}
          <div
            style={{
              position: "absolute",
              inset: 0,
              background:
                "linear-gradient(to bottom, rgba(0,0,0,0.25) 0%, transparent 35%, rgba(0,0,0,0.60) 100%)",
              zIndex: 6,
              pointerEvents: "none",
            }}
          />

          {/* ── Contenido ── */}
          <div
            style={{
              position: "relative",
              zIndex: 20,
              height: "100%",
              display: "flex",
              flexDirection: "column",
              justifyContent: "space-between",
              padding: "clamp(24px, 5%, 42px) clamp(20px, 6%, 40px) clamp(20px, 4%, 36px)",
            }}
          >
            {/* Top — cristal anchor + eyebrow */}
            <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
              {/* Cristal violeta-magenta anchor (identidad visual) */}
              <div
                className="anchor-cristal"
                style={{
                  width: "10px",
                  height: "10px",
                  background: "linear-gradient(135deg, #B43FFF, #EC4899)",
                  clipPath: "polygon(50% 0%, 80% 20%, 100% 60%, 75% 100%, 25% 100%, 0% 60%, 20% 20%)",
                  flexShrink: 0,
                }}
              />
              <p
                className="oraculo-serif"
                style={{
                  fontSize: "clamp(16px, 3.5vw, 22px)",
                  fontWeight: 400,
                  color: "#f0f0f0",
                  filter: "drop-shadow(0 1px 2px rgba(0,0,0,0.8))",
                  margin: 0,
                  fontStyle: "italic",
                }}
              >
                Tu carta espera.
              </p>
            </div>

            {/* Centro — título + sistemas + botón */}
            <div style={{ display: "flex", flexDirection: "column", gap: "20px" }}>
              <h1
                className="oraculo-serif"
                style={{
                  fontSize: "clamp(28px, 6vw, 38px)",
                  lineHeight: "1.15",
                  fontWeight: 400,
                  color: "#ffffff",
                  margin: 0,
                  letterSpacing: "-0.5px",
                  fontStyle: "italic",
                }}
              >
                Una lectura ancestral
                <br />× tu chispa Pax.
              </h1>

              {/* Subtítulo — 3 sistemas explícitos */}
              <p
                className="oraculo-sans"
                style={{
                  fontSize: "clamp(12px, 2.5vw, 15px)",
                  fontWeight: 200,
                  color: "#a3a3a3",
                  margin: 0,
                  lineHeight: 1.5,
                  letterSpacing: "0.04em",
                }}
              >
                Maya × astral × arquetipo del servicio.
              </p>

              {/* CTA glassmorphic — style exacto del brief */}
              <button
                onClick={handleCta}
                className="oraculo-btn-glow oraculo-sans"
                style={{
                  display: "inline-flex",
                  alignItems: "center",
                  justifyContent: "center",
                  gap: "8px",
                  width: "fit-content",
                  padding: "12px 28px",
                  borderRadius: "100px",
                  border: "none",
                  cursor: "pointer",
                  fontSize: "14px",
                  fontWeight: 400,
                  color: "#ffffff",
                  letterSpacing: "0.02em",
                  position: "relative",
                  overflow: "hidden",
                }}
              >
                <span
                  style={{
                    width: "6px",
                    height: "6px",
                    borderRadius: "50%",
                    background: "rgba(255,140,70,0.9)",
                    display: "inline-block",
                    flexShrink: 0,
                  }}
                />
                Tirar la carta
              </button>
            </div>

            {/* Footer — 4 pilares del sistema */}
            <div
              className="oraculo-sans"
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
                fontSize: "11px",
                color: "#555",
                fontWeight: 300,
                flexWrap: "wrap",
              }}
            >
              <span>pax-os</span>
              <span style={{ color: "#444", opacity: 0.8 }}>|</span>
              {[
                { label: "maya", color: "#C084FC" },
                { label: "astral", color: "#67E8F9" },
                { label: "pax", color: "#B43FFF" },
                { label: "gesto", color: "#FCD34D" },
              ].map(({ label, color }, i) => (
                <span key={label} style={{ display: "flex", alignItems: "center", gap: "4px" }}>
                  {i > 0 && <span style={{ color: "#333", opacity: 0.6 }}>✦</span>}
                  <span style={{ color }}>{label}</span>
                </span>
              ))}
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
