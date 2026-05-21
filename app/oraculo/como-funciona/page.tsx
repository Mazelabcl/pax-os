"use client";

/**
 * /oraculo/como-funciona v2 — Experiencia cinematica de 5 secciones.
 *
 * Cada seccion es un glass card con imagen propia sobre fondo oscuro con
 * video bg continuo. Animaciones CSS scroll-triggered por seccion.
 * Las 8 visuales (C/D) integradas como ilustraciones, no decoracion.
 */

import Link from "next/link";
import Image from "next/image";
import { SistemasRow } from "@/components/oraculo/sistemas-row";

export default function ComoFuncionaPage() {
  return (
    <div className="min-h-screen bg-black text-white overflow-x-hidden">

      {/* ── STYLES ── */}
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600&display=swap');
        .cf-serif { font-family: 'Cormorant Garamond', 'GFS Didot', Georgia, serif; }
        .cf-sans  { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }

        /* Body text mejorado — contraste y tamaño para lectura larga */
        .cf-sans.text-sm { font-size: 1.0625rem !important; line-height: 1.75 !important; font-weight: 400 !important; color: #d4d4d4 !important; letter-spacing: 0.01em; }

        /* Noise overlay */
        .cf-noise {
          position: absolute;
          inset: 0;
          background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
          opacity: 0.04;
          pointer-events: none;
          z-index: 10;
        }

        /* Scroll fade-in sin framer-motion */
        @keyframes fadeInUp {
          from { opacity: 0; transform: translateY(24px); }
          to   { opacity: 1; transform: translateY(0); }
        }
        .fade-section {
          animation: fadeInUp 0.8s ease-out both;
        }
        .fade-section:nth-child(1) { animation-delay: 0.1s; }
        .fade-section:nth-child(2) { animation-delay: 0.2s; }
        .fade-section:nth-child(3) { animation-delay: 0.3s; }
        .fade-section:nth-child(4) { animation-delay: 0.4s; }
        .fade-section:nth-child(5) { animation-delay: 0.5s; }

        /* Cristal anchor pulso */
        @keyframes anchor-pulse {
          0%,100% { opacity:0.6; filter:drop-shadow(0 0 4px rgba(180,63,255,0.6)); }
          50%      { opacity:1;   filter:drop-shadow(0 0 8px rgba(180,63,255,1)); }
        }
        .anchor-pulse { animation: anchor-pulse 3s ease-in-out infinite; }
      `}</style>

      {/* ── HERO con video Pax-canon ── */}
      <section className="relative w-full overflow-hidden flex items-center justify-center" style={{ minHeight: "60vh" }}>
        {/* Video bg */}
        <div className="absolute inset-0 overflow-hidden" style={{ zIndex: 1 }}>
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
              opacity: 0.5,
            }}
          >
            <source src="/videos/oraculo-hero-loop.webm" type="video/webm" />
            <source src="/videos/oraculo-hero-loop.mp4" type="video/mp4" />
          </video>
        </div>
        {/* Gradient sobre la imagen */}
        <div
          className="absolute inset-0"
          style={{
            background: "linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.6) 60%, #000 100%)",
            zIndex: 2,
          }}
        />
        {/* Noise */}
        <div className="cf-noise" style={{ zIndex: 3 }} />

        {/* Contenido hero */}
        <div className="relative z-10 flex flex-col items-center text-center gap-5 px-6 py-20" style={{ maxWidth: "600px" }}>
          {/* Cristal anchor */}
          <div
            className="anchor-pulse"
            style={{
              width: "12px", height: "12px",
              background: "linear-gradient(135deg, #B43FFF, #EC4899)",
              clipPath: "polygon(50% 0%, 80% 20%, 100% 60%, 75% 100%, 25% 100%, 0% 60%, 20% 20%)",
            }}
          />
          <p className="cf-sans text-xs tracking-[0.2em] uppercase text-[#B43FFF] font-light">
            Meta-explicación
          </p>
          <h1
            className="cf-serif text-3xl font-light text-white leading-snug"
            style={{ fontStyle: "italic" }}
          >
            Cómo leo tu carta.
          </h1>
          <p className="cf-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
            Cada lectura fusiona tres sistemas de conocimiento humano con el arquetipo Pax.
            <br />Aquí te muestro cada capa.
          </p>
          <SistemasRow size="md" />
        </div>
      </section>

      {/* ── SECCIONES — carousel narrativo de 5 cards ── */}
      <div className="max-w-3xl mx-auto px-6 py-16 flex flex-col gap-16">

        {/* ── Sección 1 — Maya ── */}
        <NarrativeCard
          index="01"
          accentColor="#C084FC"
          borderColor="rgba(192,132,252,0.2)"
          bgGradient="rgba(192,132,252,0.04)"
          imageSrc="/images/oraculo-v3/carta-maya-art.png"
          eyebrow="Lo que te leo de Maya"
          title="El Tzolkin — tu nahual y tu tono"
          icon={
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <rect x="10" y="1" width="9" height="9" rx="0.5" transform="rotate(45 10 1)" fill="#C084FC" opacity="0.7" />
            </svg>
          }
        >
          <p className="cf-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
            El <strong className="text-[#C084FC] font-normal">Tzolkin</strong> es el calendario sagrado maya de 260 días.
            Cada día tiene un <em>nahual</em> (arquetipo energético, como Ix el Jaguar o Imix la Cocodrila) y un <em>tono</em> (número del 1 al 13 que define la intensidad y propósito).
          </p>
          <p className="cf-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
            La combinación nahual + tono del día en que naciste define tu energía de base. No es predicción —
            es un lenguaje de patrones que los mayas destilaron en siglos de observación. Yo lo uso para
            identificar <strong className="text-white font-normal">de qué tipo de energía está hecho tu gesto de servicio</strong>.
          </p>
          <div
            className="rounded-md p-3 mt-1"
            style={{ background: "rgba(192,132,252,0.06)", border: "1px solid rgba(192,132,252,0.12)" }}
          >
            <p className="cf-sans text-xs text-[#C084FC] font-light">
              Ejemplo: Nahual Ix (Jaguar / Tierra) · Tono 7 (Reflexión) → una persona que conecta lo invisible con lo visible, cuyo servicio ocurre en momentos de quietud y observación profunda.
            </p>
          </div>
        </NarrativeCard>

        {/* ── Sección 2 — Astral ── */}
        <NarrativeCard
          index="02"
          accentColor="#67E8F9"
          borderColor="rgba(103,232,249,0.2)"
          bgGradient="rgba(103,232,249,0.03)"
          imageSrc="/images/oraculo-v3/carta-astral-art.png"
          eyebrow="Lo que te leo de Astral"
          title="Sol, luna y ascendente — el cielo del momento exacto"
          icon={
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <circle cx="10" cy="10" r="3" fill="#67E8F9" />
              <circle cx="10" cy="2" r="1.5" fill="#67E8F9" opacity="0.6" />
              <circle cx="10" cy="18" r="1.5" fill="#67E8F9" opacity="0.6" />
              <circle cx="2" cy="10" r="1.5" fill="#67E8F9" opacity="0.6" />
              <circle cx="18" cy="10" r="1.5" fill="#67E8F9" opacity="0.6" />
            </svg>
          }
        >
          <p className="cf-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
            Tu <strong className="text-[#67E8F9] font-normal">sol</strong> es la energía que expresas.
            Tu <strong className="text-[#67E8F9] font-normal">luna</strong> es la energía que necesitas.
            Tu <strong className="text-[#67E8F9] font-normal">ascendente</strong> es la energía que el mundo percibe en ti.
          </p>
          <p className="cf-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
            Para calcular el ascendente real necesito fecha + hora + lugar exactos — de ahí la importancia de los tres campos.
            Uso efemérides astronómicas reales, no estimaciones. La carta natal completa tiene 10 planetas y 12 casas;
            yo extraigo los <strong className="text-white font-normal">3 datos que más impactan tu arquetipo de servicio</strong>.
          </p>
          <div
            className="rounded-md p-3 mt-1"
            style={{ background: "rgba(103,232,249,0.04)", border: "1px solid rgba(103,232,249,0.1)" }}
          >
            <p className="cf-sans text-xs text-[#67E8F9] font-light">
              Ejemplo: Sol Escorpio · Luna Piscis · Asc Cáncer → agua triple. El servicio ocurre a través del cuidado profundo, la intuición y la capacidad de sostener lo emocional que otros no pueden sostener.
            </p>
          </div>
        </NarrativeCard>

        {/* ── Sección 3 — Pax ── */}
        <NarrativeCard
          index="03"
          accentColor="#B43FFF"
          borderColor="rgba(180,63,255,0.2)"
          bgGradient="rgba(180,63,255,0.04)"
          imageSrc="/images/oraculo-v3/cristal-eco-7-variantes.png"
          eyebrow="Lo que te agrego de Pax"
          title="El arquetipo del servicio — tu cristal-eco personal"
          icon={
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <polygon points="10,0.5 14.5,3.5 17.5,8.5 14.5,13.5 10,16.5 5.5,13.5 2.5,8.5 5.5,3.5" fill="#B43FFF" opacity="0.8" />
            </svg>
          }
        >
          <p className="cf-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
            Aquí viene la capa Pax. Tomo el nahual + los signos astrales y los paso por el filtro del universo Pax:
            <em> ¿qué tipo de gesto de servicio describe esta combinación?</em>
          </p>
          <p className="cf-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
            El resultado es tu <strong className="text-[#B43FFF] font-normal">arquetipo de servicio</strong> —
            la forma específica en que tu energía natural encaja con una necesidad del mundo.
            No es identidad. Es <strong className="text-white font-normal">vocación de ofrenda</strong>.
          </p>
          <p className="cf-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
            Tu <strong className="text-[#B43FFF] font-normal">cristal-eco</strong> tiene el color que
            mezcla el tono maya con el elemento astral dominante. Ese cristal nace apagado en la Cámara
            que Escucha Arriba — y se enciende cuando completas el ciclo.
          </p>
        </NarrativeCard>

        {/* ── Sección 4 — El Gesto ── */}
        <NarrativeCard
          index="04"
          accentColor="#FCD34D"
          borderColor="rgba(252,211,77,0.18)"
          bgGradient="rgba(252,211,77,0.03)"
          imageSrc="/images/oraculo-v3/constelacion-pax-bg.png"
          eyebrow="El Gesto"
          title="Tu acto invisible enciende un cristal real"
          icon={
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <circle cx="10" cy="10" r="8" stroke="#FCD34D" strokeWidth="1.5" fill="none" opacity="0.6" />
              <circle cx="10" cy="10" r="4" stroke="#FCD34D" strokeWidth="1" fill="none" opacity="0.4" />
              <circle cx="10" cy="10" r="1.5" fill="#FCD34D" opacity="0.8" />
            </svg>
          }
        >
          <p className="cf-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
            Un <strong className="text-[#FCD34D] font-normal">Gesto</strong> es cualquier acto creativo
            que genera impacto o dinero, donde el dinero se dona 100%.
            El Oráculo Pax es un Gesto.
          </p>

          {/* Diagrama del loop */}
          <div
            className="rounded-md p-4 font-mono text-xs leading-loose"
            style={{ background: "rgba(255,255,255,0.02)", border: "1px solid rgba(252,211,77,0.1)" }}
          >
            {[
              { text: "Tu lectura completa", indent: 0, color: "#FCD34D" },
              { text: "↓", indent: 1, color: "#888" },
              { text: "Pay what you can (acto libre)", indent: 1, color: "#d4d4d4" },
              { text: "↓", indent: 2, color: "#888" },
              { text: "Cristal-eco se enciende en la Cámara", indent: 2, color: "#B43FFF" },
              { text: "↓", indent: 3, color: "#888" },
              { text: "Cristal-anchor del Uray Pacha recibe carga", indent: 3, color: "#d4d4d4" },
              { text: "↓", indent: 4, color: "#888" },
              { text: "100% del dinero llega a fundación real", indent: 4, color: "#ffffff" },
              { text: "↓", indent: 5, color: "#888" },
              { text: "Impacto real en superficie", indent: 5, color: "#d4d4d4" },
              { text: "↓", indent: 6, color: "#888" },
              { text: "Nuevos gestos de bondad → nuevas agujas vibran", indent: 6, color: "#34D399" },
            ].map(({ text, indent, color }, i) => (
              <div key={i} style={{ paddingLeft: `${indent * 16}px`, color }}>
                {text}
              </div>
            ))}
          </div>

          <p className="cf-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
            La mitología y la economía son la misma cosa. El visitante no está donando <em>además de</em> recibir
            una lectura — el acto de pagar <strong className="text-white font-normal">es</strong> lo que completa
            la lectura en la diegesis.
          </p>
        </NarrativeCard>

        {/* ── Sección 5 — Los abuelos pax ── */}
        <NarrativeCard
          index="05"
          accentColor="#EC4899"
          borderColor="rgba(236,72,153,0.2)"
          bgGradient="rgba(236,72,153,0.03)"
          imageSrc="/images/oraculo-v3/agatha-portrait-mistica.png"
          imageAlt="Una de las abuelas pax leyendo cristales"
          eyebrow="Quienes te leen"
          title="Los abuelos pax — los que llevan siglos escuchando"
          icon={
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <circle cx="10" cy="7" r="4" stroke="#EC4899" strokeWidth="1.5" fill="none" opacity="0.7" />
              <path d="M3 18c0-3.866 3.134-7 7-7s7 3.134 7 7" stroke="#EC4899" strokeWidth="1.5" fill="none" opacity="0.5" />
            </svg>
          }
        >
          <p className="cf-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
            Los <strong className="text-[#EC4899] font-normal">abuelos pax</strong> son los ancianos del clan,
            los que llevan siglos escuchando los cristales y traduciendo lo que vibran en lecturas.
            No guardan la memoria del clan (eso es Wiz) — guardan la memoria del cielo:
            la vocación de cada humano, el patrón que traen desde que nacieron.
          </p>
          <p className="cf-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
            A los abuelos los asisten <strong className="text-white font-normal">Iris</strong> (joven cartógrafa de
            constelaciones — traduce las agujas vibrantes a un mapa legible) y{" "}
            <strong className="text-white font-normal">Baba</strong> (Pax ancestral que sostiene la conexión
            entre la cámara y el Uray Pacha — cuando Baba canta, el oráculo está activo).
          </p>
          <blockquote
            className="cf-serif text-sm text-[#ccc] font-light leading-relaxed italic border-l-2 pl-4"
            style={{ borderColor: "rgba(236,72,153,0.4)" }}
          >
            "Aquí abajo escuchamos cuándo naciste arriba. Ahora vamos a escuchar para qué."
          </blockquote>
        </NarrativeCard>

      </div>

      {/* ── CTA FINAL ── */}
      <div className="max-w-3xl mx-auto px-6 pb-20 flex flex-col items-center gap-6 text-center">
        <div className="h-px w-full" style={{ background: "rgba(180,63,255,0.1)" }} />
        <p className="cf-serif text-lg text-[#d4d4d4] font-light" style={{ fontStyle: "italic" }}>
          ¿Lista tu pregunta?
        </p>
        <Link
          href="/oraculo"
          className="inline-flex items-center gap-2 py-3 px-8 rounded-full text-sm font-light text-white tracking-wide transition-all duration-300"
          style={{
            fontFamily: "Inter, sans-serif",
            background: "linear-gradient(to bottom, rgba(255,140,70,0.10), transparent)",
            boxShadow:
              "0 4px 30px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,140,70,0.5), inset 0 0 0 1px rgba(255,255,255,0.1), inset 0 -1px 2px rgba(0,0,0,0.8)",
          }}
        >
          <span
            style={{
              width: "6px", height: "6px", borderRadius: "50%",
              background: "rgba(255,140,70,0.9)", display: "inline-block", flexShrink: 0,
            }}
          />
          Ir al oráculo
        </Link>
        <p className="cf-sans text-xs text-[#aaa] font-light" style={{ fontFamily: "Inter, sans-serif" }}>
          pay what you can — 100% se dona
        </p>
      </div>

    </div>
  );
}

/* ------------------------------------------------------------------ */
/* NarrativeCard — card cinematica de una seccion narrativa             */
/* ------------------------------------------------------------------ */
interface NarrativeCardProps {
  index: string;
  accentColor: string;
  borderColor: string;
  bgGradient: string;
  imageSrc: string;
  imageAlt?: string;
  eyebrow: string;
  title: string;
  icon: React.ReactNode;
  children: React.ReactNode;
}

function NarrativeCard({
  index,
  accentColor,
  borderColor,
  bgGradient,
  imageSrc,
  imageAlt,
  eyebrow,
  title,
  icon,
  children,
}: NarrativeCardProps) {
  const altText = imageAlt ?? title;
  return (
    <div
      className="fade-section rounded-lg overflow-hidden"
      style={{
        background: bgGradient,
        border: `1px solid ${borderColor}`,
        backdropFilter: "blur(8px)",
      }}
    >
      {/* Imagen — full-width visible arriba en mobile y md+ */}
      <div
        className="relative w-full overflow-hidden"
        style={{ height: "260px" }}
      >
        <Image
          src={imageSrc}
          alt={altText}
          fill
          style={{ objectFit: "cover", opacity: 0.85 }}
          sizes="(max-width: 768px) 100vw, 768px"
        />
        {/* Overlay: fade bottom para legibilidad del texto */}
        <div
          style={{
            position: "absolute", inset: 0,
            background: "linear-gradient(to bottom, transparent 30%, rgba(0,0,0,0.75) 100%)",
          }}
        />
        {/* Número de sección — encima de la imagen */}
        <div
          className="absolute top-4 right-4 font-mono text-2xl"
          style={{ color: accentColor, opacity: 0.5, fontWeight: 300 }}
        >
          {index}
        </div>
      </div>

      {/* Contenido — debajo de la imagen */}
      <div className="flex flex-col gap-4 p-6">
        {/* Eyebrow + icon */}
        <div className="flex items-center gap-2">
          {icon}
          <p
            className="text-xs tracking-[0.18em] uppercase font-light"
            style={{ fontFamily: "Inter, sans-serif", color: accentColor }}
          >
            {eyebrow}
          </p>
        </div>

        {/* Título */}
        <h2
          className="text-lg font-light text-white leading-snug"
          style={{ fontFamily: "'Cormorant Garamond', 'GFS Didot', Georgia, serif", fontStyle: "italic" }}
        >
          {title}
        </h2>

        {/* Divisor */}
        <div className="h-px" style={{ background: borderColor }} />

        {/* Contenido */}
        <div className="flex flex-col gap-3">
          {children}
        </div>
      </div>
    </div>
  );
}
