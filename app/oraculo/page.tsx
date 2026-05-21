"use client";

/**
 * /oraculo v4 — Entrada principal del Oráculo Pax.
 *
 * Cambios v4:
 *  - Form hace POST real a /api/oraculo/lectura
 *  - Loading state real mientras el backend procesa (no timeout fijo)
 *  - Mensajes rotativos cada 1.5s durante el POST
 *  - Si response.ok: guarda data en sessionStorage + redirect a /oraculo/resultado
 *  - Si falla: muestra error inline con botón retry
 *  - Si tarda >20s: avisa pero no aborta
 */

import { useState, useEffect, useRef } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import Image from "next/image";
import { GlassmorphicHero } from "@/components/oraculo/glassmorphic-hero";
import { SistemasRow } from "@/components/oraculo/sistemas-row";

interface FormData {
  fechaNacimiento: string;
  horaNacimiento: string;
  lugarNacimiento: string;
}

const LOADING_STEPS = [
  "Calculando tu nahual maya...",
  "Trazando tu carta astral...",
  "Conectando con el arquetipo...",
  "Tejiendo tu lectura...",
  "Los abuelos pax están escuchando...",
];

export default function OraculoPage() {
  const router = useRouter();
  const loadingRef = useRef<HTMLDivElement>(null);

  const [form, setForm] = useState<FormData>({
    fechaNacimiento: "",
    horaNacimiento: "",
    lugarNacimiento: "",
  });
  const [loading, setLoading] = useState(false);
  const [loadingStep, setLoadingStep] = useState(0);
  const [formVisible, setFormVisible] = useState(true);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);
  const [slowWarning, setSlowWarning] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const isFormValid =
    form.fechaNacimiento.trim() !== "" && form.lugarNacimiento.trim() !== "";

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!isFormValid || loading) return;

    setErrorMsg(null);
    setSlowWarning(false);

    // 1. Fade out el form
    setFormVisible(false);

    // 2. Pequeña pausa de transicion, luego mostrar loading
    await new Promise<void>((resolve) => setTimeout(resolve, 300));
    setLoading(true);

    // Scroll al loading state
    setTimeout(() => {
      loadingRef.current?.scrollIntoView({ behavior: "smooth", block: "center" });
    }, 100);

    // Aviso de demora si el backend tarda mas de 20s (no abortar)
    const slowTimer = setTimeout(() => setSlowWarning(true), 20000);

    try {
      const res = await fetch("/api/oraculo/lectura", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          fecha: form.fechaNacimiento,
          hora: form.horaNacimiento || undefined,
          lugar: form.lugarNacimiento,
        }),
      });

      clearTimeout(slowTimer);

      const json = await res.json();

      if (!res.ok || !json.ok) {
        throw new Error(json.error ?? "Error desconocido del servidor.");
      }

      // Guardar en sessionStorage y redirigir
      sessionStorage.setItem("pax-oraculo-lectura", JSON.stringify(json.data));
      router.push("/oraculo/resultado");
    } catch (err: unknown) {
      clearTimeout(slowTimer);
      setLoading(false);
      setFormVisible(true);
      setSlowWarning(false);
      const message =
        err instanceof Error ? err.message : "Hubo un problema leyendo tu carta. Inténtalo de nuevo.";
      setErrorMsg(message);
    }
  };

  // Rotar los mensajes de loading cada 1.5s
  useEffect(() => {
    if (!loading) return;
    const interval = setInterval(() => {
      setLoadingStep((prev) => (prev + 1) % LOADING_STEPS.length);
    }, 1500);
    return () => clearInterval(interval);
  }, [loading]);

  return (
    <div className="bg-black min-h-screen text-white">

      {/* ── Sección 0 — Ritual de los místicos (pre-hero full-viewport) ── */}
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600&display=swap');

        @keyframes ken-burns-ritual {
          0%   { transform: scale(1) translate(0%, 0%); }
          100% { transform: scale(1.08) translate(-2%, -1%); }
        }
        .ritual-bg {
          animation: ken-burns-ritual 12s ease-in-out infinite alternate;
        }
        @keyframes ritual-fade-in {
          from { opacity: 0; transform: translateY(16px); }
          to   { opacity: 1; transform: translateY(0); }
        }
        .ritual-eyebrow { animation: ritual-fade-in 0.8s ease-out 0.2s both; }
        .ritual-h1      { animation: ritual-fade-in 0.9s ease-out 0.4s both; }
        .ritual-sub     { animation: ritual-fade-in 0.9s ease-out 0.6s both; }
        .ritual-cta     { animation: ritual-fade-in 0.9s ease-out 0.8s both; }

        /* Tipografía body — mejor contraste en sección form */
        #oraculo-form p.oraculo-form-body {
          font-size: 17px;
          line-height: 1.75;
          font-weight: 400;
          color: #c0c0c0;
          letter-spacing: 0.01em;
        }

        @keyframes ritual-cta-glow {
          0%,100% {
            box-shadow:
              0 0 0 0 rgba(255,140,70,0),
              0 4px 30px rgba(0,0,0,0.6),
              inset 0 1px 0 rgba(255,140,70,0.5),
              inset 0 0 0 1px rgba(255,255,255,0.1);
          }
          50% {
            box-shadow:
              0 0 0 6px rgba(255,140,70,0.06),
              0 4px 30px rgba(0,0,0,0.7),
              inset 0 1px 0 rgba(255,140,70,0.7),
              inset 0 0 0 1px rgba(255,255,255,0.15);
          }
        }
        .ritual-btn {
          animation: ritual-cta-glow 2.5s ease-in-out infinite;
          background: linear-gradient(to bottom, rgba(255,140,70,0.12), transparent);
          transition: background 0.3s ease, transform 0.2s ease;
        }
        .ritual-btn:hover {
          background: linear-gradient(to bottom, rgba(255,140,70,0.22), rgba(180,63,255,0.08));
          transform: translateY(-1px);
        }
      `}</style>

      <section
        className="relative w-full overflow-hidden flex items-center justify-center"
        style={{ minHeight: "100dvh" }}
      >
        {/* Fondo — imagen ritual con ken-burns */}
        <div className="absolute inset-0 overflow-hidden" style={{ zIndex: 1 }}>
          <div className="absolute inset-0 ritual-bg" style={{ transformOrigin: "center center" }}>
            <Image
              src="/images/oraculo-v3/ritual-misticos-pax.png"
              alt="Ritual de los místicos Pax — consejo ancestral leyendo cristales"
              fill
              style={{ objectFit: "cover", objectPosition: "center" }}
              sizes="100vw"
              priority
            />
          </div>
        </div>

        {/* Overlay gradiente top-down para legibilidad */}
        <div
          className="absolute inset-0"
          style={{
            background:
              "linear-gradient(to bottom, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.3) 40%, rgba(0,0,0,0.65) 75%, rgba(0,0,0,0.92) 100%)",
            zIndex: 2,
          }}
        />

        {/* Contenido centrado */}
        <div
          className="relative flex flex-col items-center text-center gap-5 px-6 py-20"
          style={{ maxWidth: "640px", zIndex: 10 }}
        >
          {/* Eyebrow */}
          <p
            className="ritual-eyebrow text-xs tracking-[0.25em] uppercase font-light"
            style={{ fontFamily: "Inter, sans-serif", color: "#B43FFF", letterSpacing: "0.25em" }}
          >
            Lectura ancestral × Pax
          </p>

          {/* H1 */}
          <h1
            className="ritual-h1 font-light text-white leading-tight"
            style={{
              fontFamily: "'Cormorant Garamond', 'GFS Didot', Georgia, serif",
              fontStyle: "italic",
              fontSize: "clamp(2.8rem, 8vw, 5rem)",
              lineHeight: 1.1,
            }}
          >
            Tu cristal te espera.
          </h1>

          {/* Subtítulo */}
          <p
            className="ritual-sub font-extralight leading-relaxed"
            style={{
              fontFamily: "Inter, sans-serif",
              fontSize: "clamp(0.95rem, 2.5vw, 1.15rem)",
              color: "rgba(244,239,230,0.75)",
              maxWidth: "480px",
            }}
          >
            Hay un ritual de místicos preparado para leer la vibración que dejaste cuando naciste.
          </p>

          {/* CTA */}
          <button
            className="ritual-cta ritual-btn mt-2 px-10 py-4 rounded-full text-sm font-light text-white tracking-wide flex items-center gap-2"
            style={{ fontFamily: "Inter, sans-serif" }}
            onClick={() => {
              document.getElementById("oraculo-hero")?.scrollIntoView({ behavior: "smooth", block: "start" });
            }}
          >
            <span
              style={{
                width: "6px", height: "6px", borderRadius: "50%",
                background: "rgba(255,140,70,0.9)", display: "inline-block", flexShrink: 0,
              }}
            />
            Conocer mi cristal
          </button>

          {/* Scroll hint */}
          <div
            className="ritual-cta mt-4 flex flex-col items-center gap-1"
            style={{ opacity: 0.4 }}
          >
            <div
              style={{
                width: "1px", height: "32px",
                background: "linear-gradient(to bottom, rgba(255,255,255,0), rgba(255,255,255,0.5))",
              }}
            />
            <p className="text-[9px] tracking-[0.2em] uppercase" style={{ fontFamily: "Inter, sans-serif", color: "#aaa" }}>
              bajar
            </p>
          </div>
        </div>
      </section>

      {/* ── Sección 1 — Hero glassmorphic v2 (con el video) ── */}
      <div id="oraculo-hero">
        <GlassmorphicHero />
      </div>

      {/* Sección 2 — Formulario glassmorphic */}
      <section
        id="oraculo-form"
        className="mx-auto max-w-xl px-6 py-20 flex flex-col gap-10"
      >
        {/* Ilustración — carta coleccionable (mockup de lo que recibe el usuario) */}
        <div className="flex justify-center">
          <div
            style={{
              maxWidth: "240px",
              width: "100%",
              borderRadius: "8px",
              border: "1px solid rgba(180,63,255,0.2)",
              boxShadow: "0 0 40px rgba(180,63,255,0.12), 0 8px 32px rgba(0,0,0,0.5)",
              overflow: "hidden",
            }}
          >
            <Image
              src="/images/oraculo-v3/cristal-coleccionable-hero.png"
              alt="Carta coleccionable con cristal-eco — lo que recibes al tirar la carta"
              width={480}
              height={640}
              style={{ width: "100%", height: "auto", display: "block" }}
              sizes="240px"
              priority
            />
          </div>
        </div>

        {/* Header del form */}
        <div
          className="flex flex-col gap-3 transition-opacity duration-300"
          style={{ opacity: formVisible ? 1 : 0 }}
        >
          {/* Sub-label discreto */}
          <div className="flex items-center gap-2 mb-1">
            <CristalAnchorSmall />
            <p
              className="text-xs tracking-[0.18em] uppercase text-[#a3a3a3]"
              style={{ fontFamily: "Inter, sans-serif", fontWeight: 300 }}
            >
              El punto de partida
            </p>
          </div>
          <h2
            className="text-2xl font-light text-white leading-snug"
            style={{ fontFamily: "'Cormorant Garamond', 'GFS Didot', Georgia, serif", fontStyle: "italic" }}
          >
            Cuéntame cuándo llegaste.
          </h2>
          <p className="oraculo-form-body" style={{ fontFamily: "Inter, sans-serif" }}>
            Tu fecha, hora y lugar de nacimiento le dicen a los tres sistemas (maya, astral y Pax)
            de qué tipo de energía estás hecho. Cuanto más exactos, más profunda la lectura.
          </p>
          <SistemasRow className="mt-1" />
        </div>

        {/* Form glassmorphic */}
        <form
          onSubmit={handleSubmit}
          className="flex flex-col gap-5 rounded-lg p-6 transition-opacity duration-300"
          style={{
            background: "rgba(255,255,255,0.03)",
            border: "1px solid rgba(180,63,255,0.15)",
            backdropFilter: "blur(12px)",
            boxShadow: "0 8px 40px rgba(0,0,0,0.4), inset 0 1px 0 rgba(180,63,255,0.12)",
            opacity: formVisible ? 1 : 0,
            pointerEvents: formVisible ? "auto" : "none",
          }}
        >
          {/* Fecha de nacimiento */}
          <div className="flex flex-col gap-2">
            <label
              htmlFor="fechaNacimiento"
              className="text-xs tracking-wide uppercase font-light flex items-center gap-2"
              style={{ fontFamily: "Inter, sans-serif", color: "#C084FC" }}
            >
              <span style={{ color: "#C084FC", opacity: 0.7, fontSize: "9px" }}>◆</span>
              Fecha de nacimiento
            </label>
            <input
              type="date"
              id="fechaNacimiento"
              name="fechaNacimiento"
              value={form.fechaNacimiento}
              onChange={handleChange}
              required
              className="rounded-md px-4 py-3 text-white text-sm font-light outline-none transition-all duration-200 [color-scheme:dark]"
              style={{
                background: "rgba(255,255,255,0.04)",
                border: "1px solid rgba(180,63,255,0.2)",
                fontFamily: "Inter, sans-serif",
              }}
              onFocus={(e) => {
                e.currentTarget.style.border = "1px solid rgba(180,63,255,0.6)";
                e.currentTarget.style.boxShadow = "0 0 0 3px rgba(180,63,255,0.08)";
              }}
              onBlur={(e) => {
                e.currentTarget.style.border = "1px solid rgba(180,63,255,0.2)";
                e.currentTarget.style.boxShadow = "none";
              }}
            />
          </div>

          {/* Hora de nacimiento */}
          <div className="flex flex-col gap-2">
            <label
              htmlFor="horaNacimiento"
              className="text-xs tracking-wide uppercase font-light flex items-center gap-2"
              style={{ fontFamily: "Inter, sans-serif", color: "#67E8F9" }}
            >
              <span style={{ color: "#67E8F9", opacity: 0.7, fontSize: "9px" }}>●</span>
              Hora de nacimiento{" "}
              <span className="text-[#aaa] normal-case not-italic font-light" style={{ fontSize: "10px" }}>
                (opcional — mejora la lectura astral)
              </span>
            </label>
            <input
              type="time"
              id="horaNacimiento"
              name="horaNacimiento"
              value={form.horaNacimiento}
              onChange={handleChange}
              className="rounded-md px-4 py-3 text-white text-sm font-light outline-none transition-all duration-200 [color-scheme:dark]"
              style={{
                background: "rgba(255,255,255,0.04)",
                border: "1px solid rgba(103,232,249,0.15)",
                fontFamily: "Inter, sans-serif",
              }}
              onFocus={(e) => {
                e.currentTarget.style.border = "1px solid rgba(103,232,249,0.5)";
                e.currentTarget.style.boxShadow = "0 0 0 3px rgba(103,232,249,0.06)";
              }}
              onBlur={(e) => {
                e.currentTarget.style.border = "1px solid rgba(103,232,249,0.15)";
                e.currentTarget.style.boxShadow = "none";
              }}
            />
          </div>

          {/* Lugar de nacimiento */}
          <div className="flex flex-col gap-2">
            <label
              htmlFor="lugarNacimiento"
              className="text-xs tracking-wide uppercase font-light flex items-center gap-2"
              style={{ fontFamily: "Inter, sans-serif", color: "#B43FFF" }}
            >
              <span style={{ color: "#B43FFF", opacity: 0.7, fontSize: "9px" }}>⬟</span>
              Ciudad de nacimiento
            </label>
            <input
              type="text"
              id="lugarNacimiento"
              name="lugarNacimiento"
              value={form.lugarNacimiento}
              onChange={handleChange}
              placeholder="ej. Santiago, Chile"
              required
              className="rounded-md px-4 py-3 text-white text-sm font-light outline-none transition-all duration-200 placeholder:text-[#333]"
              style={{
                background: "rgba(255,255,255,0.04)",
                border: "1px solid rgba(180,63,255,0.2)",
                fontFamily: "Inter, sans-serif",
              }}
              onFocus={(e) => {
                e.currentTarget.style.border = "1px solid rgba(180,63,255,0.6)";
                e.currentTarget.style.boxShadow = "0 0 0 3px rgba(180,63,255,0.08)";
              }}
              onBlur={(e) => {
                e.currentTarget.style.border = "1px solid rgba(180,63,255,0.2)";
                e.currentTarget.style.boxShadow = "none";
              }}
            />
            <p className="text-xs text-[#aaa] font-light" style={{ fontFamily: "Inter, sans-serif" }}>
              Ciudad + país. Necesario para calcular tu ascendente con precisión.
            </p>
          </div>

          {/* Divisor */}
          <div className="h-px" style={{ background: "rgba(180,63,255,0.1)" }} />

          {/* Error inline */}
          {errorMsg && (
            <div
              className="rounded-md px-4 py-3 flex flex-col gap-2"
              style={{
                background: "rgba(239,68,68,0.06)",
                border: "1px solid rgba(239,68,68,0.25)",
              }}
            >
              <p className="text-xs text-[#f87171] font-light" style={{ fontFamily: "Inter, sans-serif" }}>
                {errorMsg}
              </p>
              <button
                type="button"
                onClick={() => setErrorMsg(null)}
                className="text-xs text-[#aaa] hover:text-[#ddd] font-light transition-colors duration-200 text-left"
                style={{ fontFamily: "Inter, sans-serif" }}
              >
                Cerrar aviso e intentar de nuevo →
              </button>
            </div>
          )}

          {/* CTA */}
          <button
            type="submit"
            disabled={!isFormValid || loading}
            className="py-3.5 px-8 rounded-full text-sm font-light tracking-wide text-white transition-all duration-300 disabled:opacity-40 disabled:cursor-not-allowed"
            style={{
              fontFamily: "Inter, sans-serif",
              background: isFormValid
                ? "linear-gradient(to bottom, rgba(255,140,70,0.10), transparent)"
                : "rgba(255,255,255,0.02)",
              boxShadow: isFormValid
                ? "0 4px 30px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,140,70,0.5), inset 0 0 0 1px rgba(255,255,255,0.1), inset 0 -1px 2px rgba(0,0,0,0.8)"
                : "inset 0 0 0 1px rgba(255,255,255,0.06)",
            }}
          >
            {loading ? "Interpretando..." : "Tirar la carta"}
          </button>
        </form>

        {/* Loading state premium */}
        {loading && (
          <div
            ref={loadingRef}
            className="flex flex-col items-center gap-6 py-12 animate-in fade-in duration-500"
          >
            {/* Cristal violeta-magenta pulsando */}
            <PremiumLoadingCristal />

            {/* Texto principal */}
            <div className="flex flex-col items-center gap-2 text-center">
              <p
                className="text-xl font-light text-white"
                style={{ fontFamily: "'Cormorant Garamond', 'GFS Didot', Georgia, serif", fontStyle: "italic" }}
              >
                Los abuelos pax están leyendo tu carta...
              </p>
              {/* Mensaje rotativo */}
              <p
                key={loadingStep}
                className="text-xs text-[#aaa] font-light animate-in fade-in duration-300"
                style={{ fontFamily: "Inter, sans-serif", letterSpacing: "0.08em" }}
              >
                {LOADING_STEPS[loadingStep]}
              </p>
              {/* Aviso de demora (>20s) */}
              {slowWarning && (
                <p
                  className="text-xs font-light animate-in fade-in duration-500 mt-2"
                  style={{ fontFamily: "Inter, sans-serif", color: "#aaa", maxWidth: "260px", textAlign: "center" }}
                >
                  Esto se está tardando más de lo esperado. Por favor espera...
                </p>
              )}
            </div>

            {/* Barra de progreso sutil — loop infinito mientras espera al backend */}
            <div
              className="w-32 h-px overflow-hidden"
              style={{ background: "rgba(180,63,255,0.1)" }}
            >
              <div
                className="h-full"
                style={{
                  background: "linear-gradient(to right, transparent, #B43FFF, transparent)",
                  animation: "loading-bar-loop 2s ease-in-out infinite",
                }}
              />
            </div>

            <style>{`
              @keyframes loading-bar-loop {
                0%   { transform: translateX(-100%); width: 60%; }
                100% { transform: translateX(200%); width: 60%; }
              }
            `}</style>
          </div>
        )}
      </section>

      {/* Footer */}
      <footer className="border-t py-10 px-6 text-center flex flex-col gap-3" style={{ borderColor: "#111" }}>
        <p className="text-xs text-[#aaa] font-light tracking-wide" style={{ fontFamily: "Inter, sans-serif" }}>
          Aquí abajo escuchamos cuándo naciste arriba. Ahora vamos a escuchar para qué.
        </p>
        <div className="flex items-center justify-center gap-4 text-xs text-[#bbb]" style={{ fontFamily: "Inter, sans-serif" }}>
          <Link
            href="/oraculo/como-funciona"
            className="hover:text-[#B43FFF] transition-colors duration-200"
          >
            Cómo funciona el oráculo
          </Link>
          <span className="text-[#666]">✦</span>
          <span>pay what you can — 100% se dona</span>
        </div>
      </footer>
    </div>
  );
}

/* ------------------------------------------------------------------ */
/* CristalAnchorSmall                                                   */
/* ------------------------------------------------------------------ */
function CristalAnchorSmall() {
  return (
    <div
      style={{
        width: "8px",
        height: "8px",
        background: "linear-gradient(135deg, #B43FFF, #EC4899)",
        clipPath: "polygon(50% 0%, 80% 20%, 100% 60%, 75% 100%, 25% 100%, 0% 60%, 20% 20%)",
        flexShrink: 0,
        filter: "drop-shadow(0 0 4px rgba(180,63,255,0.8))",
      }}
    />
  );
}

/* ------------------------------------------------------------------ */
/* PremiumLoadingCristal — cristal SVG pulsando para el loading state   */
/* ------------------------------------------------------------------ */
function PremiumLoadingCristal() {
  return (
    <>
      <style>{`
        @keyframes cristal-loading-pulse {
          0%, 100% {
            filter: drop-shadow(0 0 8px rgba(180,63,255,0.4)) drop-shadow(0 0 24px rgba(236,72,153,0.2));
            opacity: 0.7;
            transform: scale(1);
          }
          50% {
            filter: drop-shadow(0 0 20px rgba(180,63,255,1)) drop-shadow(0 0 40px rgba(236,72,153,0.5));
            opacity: 1;
            transform: scale(1.08);
          }
        }
        @keyframes cristal-ring-pulse {
          0%, 100% { opacity: 0.15; transform: scale(1); }
          50%       { opacity: 0.35; transform: scale(1.2); }
        }
        .cristal-loading { animation: cristal-loading-pulse 1.6s ease-in-out infinite; }
        .cristal-ring-1  { animation: cristal-ring-pulse 1.6s ease-in-out infinite 0.4s; }
        .cristal-ring-2  { animation: cristal-ring-pulse 1.6s ease-in-out infinite 0.8s; }
      `}</style>

      <div className="relative flex items-center justify-center" style={{ width: "80px", height: "80px" }}>
        {/* Aros concéntricos de fondo */}
        <div
          className="cristal-ring-2 absolute rounded-full"
          style={{
            width: "76px", height: "76px",
            border: "1px solid rgba(180,63,255,0.3)",
          }}
        />
        <div
          className="cristal-ring-1 absolute rounded-full"
          style={{
            width: "56px", height: "56px",
            border: "1px solid rgba(236,72,153,0.4)",
          }}
        />
        {/* Cristal central */}
        <div
          className="cristal-loading"
          style={{
            width: "44px",
            height: "44px",
            background: "linear-gradient(135deg, rgba(180,63,255,0.9) 0%, rgba(236,72,153,0.7) 50%, rgba(180,63,255,1) 100%)",
            clipPath: "polygon(50% 0%, 80% 20%, 100% 60%, 75% 100%, 25% 100%, 0% 60%, 20% 20%)",
          }}
        />
      </div>
    </>
  );
}
