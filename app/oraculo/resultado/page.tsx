"use client";

/**
 * /oraculo/resultado v6 — Lee el response real del API desde sessionStorage.
 *
 * Cambios v6:
 *  - Todo el contenido viene de sessionStorage['pax-oraculo-lectura'] (set por el form)
 *  - Si no hay data: mensaje + link de regreso a /oraculo
 *  - Bloque astral se oculta completo si data.astral es null
 *  - edition_serial en footer pequeno
 *  - Layout y styling identicos a v5 — solo cambia la fuente de datos
 */

import { useEffect, useState } from "react";
import Link from "next/link";
import Image from "next/image";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { SistemasRow } from "@/components/oraculo/sistemas-row";

// ---------- Tipos del contrato API ----------

interface NahualData {
  nombre: string;
  glyph: string;
  descripcion: string;
}

interface TonoData {
  numero: number;
  nombre: string;
  descripcion: string;
}

interface AstralPlanet {
  signo: string;
  grado: number;
  casa: number;
}

interface AstralAscendente {
  signo: string;
  grado: number;
}

interface AstralData {
  sol: AstralPlanet;
  luna: AstralPlanet;
  ascendente: AstralAscendente;
}

interface ArquetipoPax {
  nombre: string;
  descripcion: string;
  color_hex: string;
}

interface TribuItem {
  titulo: string;
  descripcion: string;
}

interface MayaBlock {
  nahual_text: string;
  tono_text: string;
  cruce_text: string;
}

interface AstralBlock {
  sol_text: string;
  luna_text: string;
  asc_text: string;
  cruce_text: string;
}

interface LecturaData {
  inputs: { fecha: string; hora: string | null; lugar: string | null };
  tzolkin: { kin: number; nahual: NahualData; tono: TonoData };
  astral: AstralData | null;
  arquetipo_pax: ArquetipoPax;
  lectura: {
    opening: string;
    pax_block: string;
    tribu_block: TribuItem[];
    maya_block: MayaBlock;
    astral_block: AstralBlock | null;
    gesto: string;
    cierre: string;
  };
  edition_serial: string;
}

// ---------- Utilidades ----------

function formatFecha(iso: string): string {
  try {
    const [year, month, day] = iso.split("-").map(Number);
    const date = new Date(year, month - 1, day);
    return date.toLocaleDateString("es-CL", { day: "numeric", month: "long", year: "numeric" });
  } catch {
    return iso;
  }
}

// ---------- Componente principal ----------

export default function OraculoResultadoPage() {
  const [data, setData] = useState<LecturaData | null>(null);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    const raw = sessionStorage.getItem("pax-oraculo-lectura");
    if (raw) {
      try {
        setData(JSON.parse(raw));
      } catch {
        // JSON malformado — se trata como sin datos
      }
    }
    setReady(true);
  }, []);

  // Mientras hidrata
  if (!ready) return null;

  // Sin data: pantalla de regreso
  if (!data) {
    return (
      <div className="min-h-screen bg-black text-white flex flex-col items-center justify-center gap-6 px-6">
        <style>{`
          .r-serif { font-family: 'Cormorant Garamond', 'GFS Didot', Georgia, serif; }
          .r-sans  { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }
        `}</style>
        <p className="r-serif text-2xl font-light text-[#d4d4d4]" style={{ fontStyle: "italic" }}>
          Esta página requiere que tires una carta primero.
        </p>
        <Link
          href="/oraculo"
          className="r-sans text-sm text-[#B43FFF] hover:text-[#d07fff] transition-colors duration-200 font-light"
        >
          ← Ir al Oráculo
        </Link>
      </div>
    );
  }

  const { inputs, tzolkin, astral, arquetipo_pax, lectura, edition_serial } = data;
  const { nahual, tono } = tzolkin;
  const color = arquetipo_pax.color_hex || "#B43FFF";

  const fechaDisplay = formatFecha(inputs.fecha);

  return (
    <div className="min-h-screen bg-black text-white">

      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600&display=swap');
        .r-serif { font-family: 'Cormorant Garamond', 'GFS Didot', Georgia, serif; }
        .r-sans  { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }

        @keyframes cristal-glow {
          0%,100% { filter: drop-shadow(0 0 8px rgba(180,63,255,0.5)); opacity:0.7; }
          50%      { filter: drop-shadow(0 0 20px rgba(180,63,255,1)); opacity:1; }
        }
        .cristal-apagado {
          animation: cristal-glow 4s ease-in-out infinite;
          opacity: 0.35;
          filter: drop-shadow(0 0 4px rgba(180,63,255,0.2));
        }
        @keyframes fadeInUp {
          from { opacity:0; transform:translateY(20px); }
          to   { opacity:1; transform:translateY(0); }
        }
        .section-reveal {
          animation: fadeInUp 0.7s ease-out both;
        }
        .section-reveal:nth-child(1) { animation-delay:0.1s; }
        .section-reveal:nth-child(2) { animation-delay:0.2s; }
        .section-reveal:nth-child(3) { animation-delay:0.3s; }
        .section-reveal:nth-child(4) { animation-delay:0.4s; }
        .section-reveal:nth-child(5) { animation-delay:0.5s; }
        .section-reveal:nth-child(6) { animation-delay:0.6s; }
        .section-reveal:nth-child(7) { animation-delay:0.7s; }

        .tribu-card {
          transition: background 0.2s ease, border-color 0.2s ease;
        }
        .tribu-card:hover {
          background: rgba(180,63,255,0.08) !important;
          border-color: rgba(180,63,255,0.25) !important;
        }

        /* Tipografía body mejorada — lectura larga: mayor contraste y tamaño */
        .r-sans.text-sm,
        .r-sans.text-base {
          font-size: 1.0625rem !important;   /* 17px */
          line-height: 1.75 !important;
          font-weight: 400 !important;
          letter-spacing: 0.01em;
          color: #d4d4d4 !important;
        }
        .r-sans.text-xs {
          color: #c0c0c0 !important;
        }

        /* Markdown dentro del bloque pax */
        .pax-md h2 { font-family: 'Cormorant Garamond','GFS Didot',Georgia,serif; font-style:italic; font-size:1.35rem; font-weight:400; color:#e8d8ff; margin-bottom:0.5rem; margin-top:1rem; }
        .pax-md h3 { font-family: 'Inter',sans-serif; font-size:0.7rem; text-transform:uppercase; letter-spacing:0.15em; color:#a3a3a3; font-weight:300; margin-bottom:0.5rem; margin-top:1rem; }
        .pax-md p  { font-family: 'Inter',sans-serif; font-size:1.0625rem; color:#d4d4d4; font-weight:400; line-height:1.75; margin-bottom:0.5rem; letter-spacing:0.01em; }
        .pax-md strong { color:#e8d8ff; font-weight:400; }
        .pax-md em { font-style:italic; }
      `}</style>

      {/* ── Nav ── */}
      <nav className="px-6 py-5 flex items-center justify-between border-b" style={{ borderColor: "#111" }}>
        <Link
          href="/oraculo"
          className="text-xs text-[#aaa] hover:text-[#B43FFF] transition-colors duration-200 font-light flex items-center gap-2 r-sans"
        >
          ← Nueva lectura
        </Link>
        <div className="flex items-center gap-2">
          <div
            style={{
              width: "8px", height: "8px",
              background: "linear-gradient(135deg, #B43FFF, #EC4899)",
              clipPath: "polygon(50% 0%, 80% 20%, 100% 60%, 75% 100%, 25% 100%, 0% 60%, 20% 20%)",
              filter: "drop-shadow(0 0 3px rgba(180,63,255,0.7))",
            }}
          />
          <span className="text-xs text-[#bbb] font-light tracking-widest uppercase r-sans">
            Oráculo Pax
          </span>
        </div>
        <div className="w-24" />
      </nav>

      <main className="max-w-lg mx-auto px-6 py-12 flex flex-col gap-12">

        {/* ── 1. HERO CARTA ── */}
        <div className="section-reveal flex flex-col gap-6">
          <div
            className="relative rounded-lg overflow-hidden"
            style={{
              aspectRatio: "3/4",
              boxShadow: `0 0 100px ${color}26, 0 0 0 1px ${color}26`,
            }}
          >
            <Image
              src="/images/oraculo-v3/cristal-coleccionable-hero.png"
              alt="Carta coleccionable del Oráculo Pax — cristal-eco personal"
              fill
              style={{ objectFit: "cover", opacity: 0.6 }}
              sizes="(max-width: 768px) 100vw, 512px"
              priority
            />
            <div
              style={{
                position: "absolute", inset: 0,
                background: "linear-gradient(160deg, rgba(10,0,20,0.75) 0%, rgba(0,0,0,0.88) 100%)",
              }}
            />

            <div className="relative z-10 h-full flex flex-col justify-between p-7">
              <div className="flex items-start justify-between">
                <div>
                  <p className="r-sans text-xs tracking-[0.2em] uppercase text-[#B43FFF] font-light mb-1">
                    Lectura de los abuelos pax
                  </p>
                  <p className="r-sans text-[10px] text-[#aaa] font-light">{fechaDisplay}</p>
                </div>
                <p className="r-sans text-[10px] font-mono text-[#888] tracking-wider">{edition_serial}</p>
              </div>

              <div className="flex flex-col gap-3">
                <div className="flex justify-center mb-4">
                  <div
                    className="cristal-apagado"
                    style={{
                      width: "52px", height: "52px",
                      background: `linear-gradient(135deg, ${color}80 0%, rgba(236,72,153,0.3) 50%, ${color}b3 100%)`,
                      clipPath: "polygon(50% 0%, 80% 20%, 100% 60%, 75% 100%, 25% 100%, 0% 60%, 20% 20%)",
                    }}
                  />
                </div>

                <h1 className="r-serif text-3xl font-light text-white text-center leading-snug" style={{ fontStyle: "italic" }}>
                  {arquetipo_pax.nombre}
                </h1>

                <div className="flex justify-center">
                  <SistemasRow size="sm" />
                </div>

                <div className="flex flex-col gap-2 mt-2">
                  <MiniSistemaRow
                    color="#C084FC"
                    label="Maya"
                    value={`${nahual.nombre} (${nahual.descripcion}) · Tono ${tono.numero} — ${tono.nombre}`}
                  />
                  {astral && (
                    <MiniSistemaRow
                      color="#67E8F9"
                      label="Astral"
                      value={`Sol ${astral.sol.signo} · Luna ${astral.luna.signo} · Asc ${astral.ascendente.signo}`}
                    />
                  )}
                  <MiniSistemaRow color="#B43FFF" label="Pax" value={arquetipo_pax.nombre} />
                </div>
              </div>

              <div>
                <p className="r-sans text-xs text-[#aaa] font-light">
                  {inputs.lugar ?? ""}
                  {inputs.lugar && inputs.fecha ? " · " : ""}
                  {inputs.fecha}
                  {inputs.hora ? ` · ${inputs.hora}` : ""}
                </p>
              </div>
            </div>
          </div>

          {/* Cita de apertura */}
          <blockquote className="r-serif text-base font-light text-[#ccc] leading-relaxed italic text-center px-4">
            {lectura.opening}
          </blockquote>
        </div>

        <Divisor />

        {/* ── 2. TU ARQUETIPO PAX ── */}
        <div className="section-reveal">
          <SistemaSection
            color={color}
            bg={`${color}0d`}
            border={`${color}26`}
            label="Tu arquetipo Pax"
            icon={
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <polygon points="9,0.5 13,3 16,8 13,13 9,15.5 5,13 2,8 5,3" fill={color} opacity="0.8" />
              </svg>
            }
          >
            <div className="flex flex-col gap-4">
              {/* Cristales-eco — los 7 arquetipos */}
              <div
                className="relative w-full overflow-hidden rounded-md"
                style={{
                  border: `1px solid ${color}33`,
                  boxShadow: `0 0 20px ${color}14`,
                }}
              >
                <Image
                  src="/images/oraculo-v3/cristal-eco-7-variantes.png"
                  alt="Los 7 cristales-eco por arquetipo de servicio Pax"
                  width={600}
                  height={300}
                  style={{ width: "100%", height: "auto", display: "block", borderRadius: "4px" }}
                  sizes="(max-width: 768px) 100vw, 512px"
                />
              </div>

              <div className="flex items-baseline gap-3">
                <p className="r-serif text-2xl font-light" style={{ color, fontStyle: "italic" }}>
                  {arquetipo_pax.nombre}
                </p>
              </div>

              {/* Texto del arquetipo (markdown) */}
              <div className="pax-md">
                <ReactMarkdown remarkPlugins={[remarkGfm]}>
                  {lectura.pax_block}
                </ReactMarkdown>
              </div>

              {/* Cristal-eco */}
              <div
                className="rounded-md p-4 flex items-center gap-4 mt-2"
                style={{ background: `${color}0d`, border: `1px solid ${color}1f` }}
              >
                <div
                  className="cristal-apagado shrink-0"
                  style={{
                    width: "40px", height: "40px",
                    background: `linear-gradient(135deg, ${color}80, rgba(0,0,0,0.8))`,
                    clipPath: "polygon(50% 0%, 80% 20%, 100% 60%, 75% 100%, 25% 100%, 0% 60%, 20% 20%)",
                  }}
                />
                <div className="flex flex-col gap-1">
                  <p className="r-sans text-xs uppercase tracking-wider text-[#a3a3a3] font-light">Tu cristal personal</p>
                  <p className="r-sans text-sm text-white font-light">{arquetipo_pax.nombre}</p>
                  <div className="flex items-center gap-2">
                    <div style={{ width: "10px", height: "10px", borderRadius: "2px", background: color, opacity: 0.5 }} />
                    <span className="r-sans text-xs font-mono text-[#aaa]">{color}</span>
                  </div>
                </div>
              </div>

              {/* Puente Pax */}
              <div className="flex items-center gap-3 mt-1">
                <span style={{ color, opacity: 0.7, fontSize: "12px" }}>≈</span>
                <p className="r-sans text-[10px] tracking-[0.2em] uppercase font-light" style={{ color, opacity: 0.8 }}>
                  El puente Pax
                </p>
              </div>

              <div
                className="rounded-md p-4"
                style={{ background: `${color}0f`, border: `1px solid ${color}33` }}
              >
                <p className="r-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
                  {arquetipo_pax.descripcion}
                </p>
              </div>
            </div>
          </SistemaSection>
        </div>

        <Divisor />

        {/* ── 3. CÓMO TU CRISTAL VIBRA CON LA TRIBU ── */}
        <div className="section-reveal">
          <SistemaSection
            color="#EC4899"
            bg="rgba(236,72,153,0.04)"
            border="rgba(236,72,153,0.12)"
            label="Cómo tu cristal vibra con la tribu"
            icon={
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <circle cx="9" cy="9" r="7" stroke="#EC4899" strokeWidth="1.2" fill="none" opacity="0.6" />
                <circle cx="9" cy="9" r="3.5" stroke="#EC4899" strokeWidth="1" fill="none" opacity="0.4" />
                <circle cx="9" cy="9" r="1.2" fill="#EC4899" opacity="0.8" />
              </svg>
            }
          >
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-2">
              {lectura.tribu_block.map((item, i) => (
                <TribuCard
                  key={i}
                  title={item.titulo}
                  description={item.descripcion}
                  accentColor="#EC4899"
                />
              ))}
            </div>
          </SistemaSection>
        </div>

        <Divisor />

        {/* ── 4. COMO SE INTERLAZA CON MAYA ── */}
        <div className="section-reveal">
          <SistemaSection
            color="#C084FC"
            bg="rgba(192,132,252,0.04)"
            border="rgba(192,132,252,0.15)"
            label="Cómo se interlaza con Maya"
            icon={
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <rect x="9" y="1" width="8" height="8" rx="0.5" transform="rotate(45 9 1)" fill="#C084FC" opacity="0.7" />
              </svg>
            }
          >
            {/* Carta maya visual */}
            <div
              className="relative w-full overflow-hidden rounded-md"
              style={{
                border: "1px solid rgba(192,132,252,0.2)",
                boxShadow: "0 0 16px rgba(192,132,252,0.08)",
              }}
            >
              <Image
                src="/images/oraculo-v3/carta-maya-art.png"
                alt="Disco Tzolkin maya — calendario sagrado de 260 días"
                width={600}
                height={260}
                style={{ width: "100%", height: "auto", display: "block", borderRadius: "4px" }}
                sizes="(max-width: 768px) 100vw, 512px"
              />
            </div>

            <div className="grid grid-cols-2 gap-4">
              <DataBlock label="Nahual" value={nahual.nombre} sub={nahual.descripcion} color="#C084FC" />
              <DataBlock label="Tono" value={String(tono.numero)} sub={tono.nombre} color="#C084FC" />
            </div>

            <p className="r-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
              {lectura.maya_block.nahual_text}
            </p>
            <p className="r-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
              {lectura.maya_block.tono_text}
            </p>

            <div
              className="rounded-md p-4"
              style={{ background: "rgba(192,132,252,0.06)", border: "1px solid rgba(192,132,252,0.15)" }}
            >
              <p className="r-sans text-xs tracking-[0.15em] uppercase font-light mb-2" style={{ color: "#a3a3a3" }}>
                El cruce — Maya confirma a Pax
              </p>
              <p className="r-sans text-sm text-[#bbb] font-light leading-relaxed">
                {lectura.maya_block.cruce_text}
              </p>
            </div>
          </SistemaSection>
        </div>

        {/* ── 5. COMO SE INTERLAZA CON ASTRAL (solo si hay data astral) ── */}
        {astral && lectura.astral_block && (
          <>
            <Divisor />
            <div className="section-reveal">
              <SistemaSection
                color="#67E8F9"
                bg="rgba(103,232,249,0.04)"
                border="rgba(103,232,249,0.12)"
                label="Cómo se interlaza con Astral"
                icon={
                  <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                    <circle cx="9" cy="9" r="2.5" fill="#67E8F9" />
                    <circle cx="9" cy="2" r="1.3" fill="#67E8F9" opacity="0.6" />
                    <circle cx="9" cy="16" r="1.3" fill="#67E8F9" opacity="0.6" />
                    <circle cx="2" cy="9" r="1.3" fill="#67E8F9" opacity="0.6" />
                    <circle cx="16" cy="9" r="1.3" fill="#67E8F9" opacity="0.6" />
                  </svg>
                }
              >
                {/* Carta astral visual */}
                <div
                  className="relative w-full overflow-hidden rounded-md"
                  style={{
                    border: "1px solid rgba(103,232,249,0.2)",
                    boxShadow: "0 0 16px rgba(103,232,249,0.08)",
                  }}
                >
                  <Image
                    src="/images/oraculo-v3/carta-astral-art.png"
                    alt="Mapa estelar Pax-style — constelaciones y carta natal"
                    width={600}
                    height={260}
                    style={{ width: "100%", height: "auto", display: "block", borderRadius: "4px" }}
                    sizes="(max-width: 768px) 100vw, 512px"
                  />
                </div>

                <div className="grid grid-cols-2 gap-4">
                  <DataBlock label="Sol" value={astral.sol.signo} sub="Energía que expresas" color="#67E8F9" />
                  <DataBlock label="Luna" value={astral.luna.signo} sub="Energía que necesitas" color="#67E8F9" />
                  <DataBlock label="Ascendente" value={astral.ascendente.signo} sub="Lo que el mundo percibe" color="#67E8F9" />
                  <DataBlock label="Casa dominante" value={`${astral.luna.casa}`} sub="Casa dominante" color="#67E8F9" />
                </div>

                <p className="r-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
                  {lectura.astral_block.sol_text}
                </p>
                <p className="r-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
                  {lectura.astral_block.luna_text}
                </p>
                <p className="r-sans text-sm text-[#d4d4d4] font-light leading-relaxed">
                  {lectura.astral_block.asc_text}
                </p>

                <div
                  className="rounded-md p-4"
                  style={{ background: "rgba(103,232,249,0.05)", border: "1px solid rgba(103,232,249,0.12)" }}
                >
                  <p className="r-sans text-xs tracking-[0.15em] uppercase font-light mb-2" style={{ color: "#a3a3a3" }}>
                    El cruce — Astral confirma a Pax y a Maya
                  </p>
                  <p className="r-sans text-sm text-[#bbb] font-light leading-relaxed">
                    {lectura.astral_block.cruce_text}
                  </p>
                </div>
              </SistemaSection>
            </div>
          </>
        )}

        {/* Divisor visual — banda decorativa de cristales */}
        <div className="w-full overflow-hidden" style={{ borderRadius: "4px", border: "1px solid rgba(180,63,255,0.1)", minHeight: "80px" }}>
          <Image
            src="/images/oraculo-v3/divider-cristal-decorative.png"
            alt="Divisor decorativo con cristales Pax"
            width={1536}
            height={1024}
            style={{ width: "100%", height: "auto", display: "block", maxHeight: "120px", objectFit: "cover" }}
            sizes="(max-width: 768px) 100vw, 512px"
          />
        </div>

        {/* ── 6. GESTO DE LA SEMANA ── */}
        <div className="section-reveal">
          <SistemaSection
            color="#FCD34D"
            bg="rgba(252,211,77,0.04)"
            border="rgba(252,211,77,0.12)"
            label="Tu Gesto esta semana"
            icon={
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <circle cx="9" cy="9" r="7.5" stroke="#FCD34D" strokeWidth="1.5" fill="none" opacity="0.6" />
                <circle cx="9" cy="9" r="3.5" stroke="#FCD34D" strokeWidth="1" fill="none" opacity="0.4" />
                <circle cx="9" cy="9" r="1.2" fill="#FCD34D" opacity="0.8" />
              </svg>
            }
          >
            <div
              className="rounded-md p-4"
              style={{ background: "rgba(252,211,77,0.06)", border: "1px solid rgba(252,211,77,0.15)" }}
            >
              <p className="r-sans text-sm text-[#ddd] font-light leading-relaxed">
                {lectura.gesto}
              </p>
            </div>

            <p className="r-sans text-xs text-[#c0c0c0] font-light leading-relaxed">
              No tiene que ser perfecto. No tiene que resultar bien. Solo tiene que ser honesto.
              Un Gesto pequeño y real pesa más que cien gestos pensados y no hechos.
            </p>

            <label className="flex items-center gap-3 cursor-pointer mt-1" style={{ userSelect: "none" }}>
              <input type="checkbox" className="w-4 h-4 cursor-pointer" style={{ accentColor: "#FCD34D" }} />
              <span className="r-sans text-sm text-[#c0c0c0] font-light">
                Marcar cuando complete el Gesto de esta semana
              </span>
            </label>
          </SistemaSection>
        </div>

        <Divisor />

        {/* ── 7. CIERRE DE LOS ABUELOS PAX ── */}
        <div className="section-reveal">
          <div
            className="rounded-md overflow-hidden"
            style={{ background: "rgba(255,255,255,0.02)", border: "1px solid rgba(255,255,255,0.05)" }}
          >
            <div className="flex flex-col md:flex-row">
              {/* Retrato en mobile */}
              <div className="relative shrink-0" style={{ width: "100%", height: "180px" }}>
                <div className="md:hidden w-full h-full relative">
                  <Image
                    src="/images/oraculo-v3/agatha-portrait-mistica.png"
                    alt="Una de las abuelas pax leyendo cristales"
                    fill
                    style={{ objectFit: "cover", objectPosition: "top" }}
                    sizes="100vw"
                  />
                  <div style={{ position: "absolute", inset: 0, background: "linear-gradient(to bottom, transparent 40%, rgba(0,0,0,0.9) 100%)" }} />
                </div>
              </div>
              {/* Columna lateral md+ */}
              <div className="hidden md:block relative shrink-0" style={{ width: "180px", minHeight: "180px" }}>
                <Image
                  src="/images/oraculo-v3/agatha-portrait-mistica.png"
                  alt="Una de las abuelas pax leyendo cristales"
                  fill
                  style={{ objectFit: "cover", objectPosition: "top", borderRadius: "0" }}
                  sizes="180px"
                />
                <div style={{ position: "absolute", inset: 0, background: "linear-gradient(to right, transparent 60%, rgba(0,0,0,0.85) 100%)" }} />
              </div>

              {/* Texto cierre */}
              <div className="p-6 flex flex-col gap-4 -mt-12 md:mt-0 relative z-10">
                <div className="flex items-center gap-2">
                  <span style={{ color: "#FCD34D", opacity: 0.4, fontSize: "10px" }}>≈</span>
                  <p className="r-sans text-[10px] tracking-[0.2em] uppercase font-light" style={{ color: "#a3a3a3" }}>
                    Los abuelos pax cierran
                  </p>
                </div>
                <blockquote
                  className="r-serif text-sm font-light leading-relaxed italic"
                  style={{ color: "#d4d4d4", borderLeft: "2px solid rgba(252,211,77,0.2)", paddingLeft: "14px" }}
                >
                  {lectura.cierre.split("\n").map((line, i) => (
                    <span key={i}>
                      {line}
                      {i < lectura.cierre.split("\n").length - 1 && <br />}
                    </span>
                  ))}
                </blockquote>
              </div>
            </div>
          </div>
        </div>

        {/* ── CTA Pago ── */}
        <div className="section-reveal flex flex-col gap-5 pb-8">
          <style>{`
            @keyframes cta-glow-pulse {
              0%, 100% {
                box-shadow:
                  0 0 0 0 rgba(180,63,255,0),
                  0 0 30px rgba(180,63,255,0.3),
                  0 4px 40px rgba(0,0,0,0.6),
                  inset 0 1px 0 rgba(212,168,87,0.5),
                  inset 0 0 0 1px rgba(255,255,255,0.1),
                  inset 0 -1px 2px rgba(0,0,0,0.8);
              }
              50% {
                box-shadow:
                  0 0 0 8px rgba(180,63,255,0.07),
                  0 0 60px rgba(236,72,153,0.5),
                  0 4px 40px rgba(0,0,0,0.7),
                  inset 0 1px 0 rgba(212,168,87,0.7),
                  inset 0 0 0 1px rgba(255,255,255,0.15),
                  inset 0 -1px 2px rgba(0,0,0,0.8);
              }
            }
            .cta-encender {
              animation: cta-glow-pulse 2.8s ease-in-out infinite;
              background: linear-gradient(135deg, rgba(180,63,255,0.18) 0%, rgba(236,72,153,0.12) 50%, rgba(212,168,87,0.12) 100%);
              transition: all 0.3s ease;
            }
            .cta-encender:hover {
              background: linear-gradient(135deg, rgba(180,63,255,0.30) 0%, rgba(236,72,153,0.22) 50%, rgba(212,168,87,0.20) 100%);
              transform: translateY(-1px);
            }
          `}</style>

          <div className="text-center flex flex-col gap-2">
            <p className="r-serif text-base font-light text-[#d4d4d4]" style={{ fontStyle: "italic" }}>
              Tu cristal personal está apagado.
            </p>
            <p className="r-sans text-xs text-[#aaa] font-light leading-relaxed">
              Completar el ciclo enciende tu cristal en el universo Pax.
              El dinero llega al 100% a una fundación real — sin monto mínimo.
            </p>
          </div>

          <button
            className="cta-encender w-full px-12 py-5 rounded-full text-white tracking-wide transition-all duration-300 flex items-center justify-center gap-3"
          >
            <svg width="18" height="18" viewBox="0 0 18 18" fill="none" style={{ flexShrink: 0 }}>
              <polygon
                points="9,0.5 13.5,3.5 16.5,9 13.5,14.5 9,17.5 4.5,14.5 1.5,9 4.5,3.5"
                fill="none"
                stroke="rgba(212,168,87,0.9)"
                strokeWidth="1.2"
              />
              <polygon
                points="9,3.5 12,5.5 14,9 12,12.5 9,14.5 6,12.5 4,9 6,5.5"
                fill="rgba(180,63,255,0.5)"
                stroke="rgba(236,72,153,0.6)"
                strokeWidth="0.8"
              />
              <circle cx="9" cy="9" r="2" fill="rgba(212,168,87,0.8)" />
            </svg>
            <span className="flex flex-col items-center gap-0.5">
              <span className="r-serif text-lg" style={{ fontStyle: "italic", fontWeight: 300, letterSpacing: "0.04em" }}>
                Encender el cristal
              </span>
              <span className="r-sans text-[10px] font-light tracking-[0.2em] uppercase" style={{ color: "rgba(212,168,87,0.8)" }}>
                pay what you can · 100% va a fundaciones
              </span>
            </span>
          </button>

          <p className="r-sans text-center text-[10px] text-[#888] font-light">
            Sin monto mínimo · el cristal enciende igual · impacto real
          </p>
        </div>

        <div className="text-center pb-4">
          <Link
            href="/oraculo/como-funciona"
            className="r-sans text-xs text-[#aaa] hover:text-[#B43FFF] transition-colors duration-200 font-light"
          >
            Cómo se construyó esta lectura →
          </Link>
        </div>

        {/* Edition serial en footer */}
        <div className="text-center pb-8">
          <p className="r-sans text-[10px] font-mono text-[#666] tracking-widest">
            {edition_serial}
          </p>
        </div>

      </main>
    </div>
  );
}

/* ------------------------------------------------------------------ */
/* Sub-componentes                                                       */
/* ------------------------------------------------------------------ */

function Divisor({ glyph = "◈", color = "rgba(180,63,255,0.5)" }: { glyph?: string; color?: string }) {
  return (
    <div className="flex items-center gap-4">
      <div className="flex-1 h-px" style={{ background: "rgba(255,255,255,0.04)" }} />
      <span style={{ color, fontSize: "12px", opacity: 0.7, lineHeight: 1 }}>{glyph}</span>
      <div className="flex-1 h-px" style={{ background: "rgba(255,255,255,0.04)" }} />
    </div>
  );
}

interface SistemaSectionProps {
  color: string;
  bg: string;
  border: string;
  label: string;
  icon: React.ReactNode;
  children: React.ReactNode;
}

function SistemaSection({ color, bg, border, label, icon, children }: SistemaSectionProps) {
  return (
    <div className="rounded-lg overflow-hidden" style={{ background: bg, border: `1px solid ${border}` }}>
      <div className="px-5 py-4 flex items-center gap-3 border-b" style={{ borderColor: border }}>
        {icon}
        <p className="r-sans text-xs tracking-[0.18em] uppercase font-light" style={{ color }}>
          {label}
        </p>
      </div>
      <div className="px-5 py-5 flex flex-col gap-3">
        {children}
      </div>
    </div>
  );
}

interface DataBlockProps { label: string; value: string; sub: string; color: string; }

function DataBlock({ label, value, sub, color }: DataBlockProps) {
  return (
    <div
      className="rounded-md p-3 flex flex-col gap-1"
      style={{ background: "rgba(255,255,255,0.02)", border: "1px solid rgba(255,255,255,0.04)" }}
    >
      <p className="r-sans text-[10px] uppercase tracking-wider font-light" style={{ color: "#a3a3a3" }}>{label}</p>
      <p className="r-serif text-lg font-light" style={{ color }}>{value}</p>
      <p className="r-sans text-[10px] font-light" style={{ color: "#a3a3a3" }}>{sub}</p>
    </div>
  );
}

function MiniSistemaRow({ color, label, value }: { color: string; label: string; value: string }) {
  return (
    <div className="flex items-center gap-2 text-xs" style={{ fontFamily: "Inter, sans-serif" }}>
      <span
        className="shrink-0 px-2 py-0.5 rounded-sm font-light uppercase tracking-wider"
        style={{
          color, fontSize: "9px", letterSpacing: "0.1em",
          background: `${color}18`, border: `1px solid ${color}30`,
        }}
      >
        {label}
      </span>
      <span style={{ color: "#d4d4d4", fontWeight: 300 }}>{value}</span>
    </div>
  );
}

interface TribuCardProps {
  title: string;
  description: string;
  accentColor: string;
}

function TribuCard({ title, description, accentColor }: TribuCardProps) {
  return (
    <div
      className="tribu-card rounded-md p-4 flex flex-col gap-2"
      style={{
        background: "rgba(236,72,153,0.03)",
        border: "1px solid rgba(236,72,153,0.1)",
      }}
    >
      <p className="r-sans text-xs font-light" style={{ color: accentColor, letterSpacing: "0.04em" }}>
        {title}
      </p>
      <p className="r-sans text-xs text-[#c0c0c0] font-light leading-relaxed">
        {description}
      </p>
    </div>
  );
}
