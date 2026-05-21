"use client";

/**
 * /oraculo/resultado v5 — Reorden PAX PRIMERO + ampliacion maya/astral.
 *
 * Orden:
 *  1. Hero carta (cristal-eco + arquetipo)
 *  2. Tu arquetipo Pax — quien eres (Sanador Intenso, 4-6 parrafos profundos)
 *  3. Como tu cristal vibra con la tribu (5 maneras)
 *  4. Como se interlaza con Maya — lectura profunda Ix + Tono 7
 *  5. Como se interlaza con Astral — lectura profunda Escorpio/Piscis/Acuario
 *  6. Tu Gesto de la semana
 *  7. Cierre de los abuelos pax
 */

import Link from "next/link";
import Image from "next/image";
import { SistemasRow } from "@/components/oraculo/sistemas-row";

// Datos mock — en v2 real llegan via searchParams / session
const MOCK = {
  lugarNacimiento: "Santiago, Chile",
  fechaNacimiento: "1990-03-15",
  horaNacimiento: "14:30",
  // Maya
  nahual: "Ix",
  nahualdesc: "Jaguar / Tierra",
  tono: "7",
  tonodesc: "Reflexión",
  // Astral
  sol: "Escorpio",
  luna: "Piscis",
  ascendente: "Acuario",
  casa: "XII · Casa de lo oculto",
  // Pax
  arquetipo: "Sanador Intenso",
  intensidad: "Alta",
  cristalColor: "#B43FFF",
  cristalHex: "#B43FFF",
  cristalNombre: "Violeta Umbral",
  edicion: "PAX-2026-A1-0042",
  fecha: "21 mayo 2026",
};

export default function OraculoResultadoPage() {
  return (
    <div className="min-h-screen bg-black text-white">

      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500&display=swap');
        @font-face {
          font-family: 'Didot';
          src: url('https://db.onlinewebfonts.com/c/251039e6849ad977a8bfc40b564dce89?family=Didot') format('woff2');
          font-weight: normal; font-style: normal;
        }
        .r-serif { font-family: 'Didot', 'GFS Didot', Georgia, serif; }
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

        /* Tribu cards hover */
        .tribu-card {
          transition: background 0.2s ease, border-color 0.2s ease;
        }
        .tribu-card:hover {
          background: rgba(180,63,255,0.08) !important;
          border-color: rgba(180,63,255,0.25) !important;
        }

      `}</style>

      {/* ── Nav ── */}
      <nav className="px-6 py-5 flex items-center justify-between border-b" style={{ borderColor: "#111" }}>
        <Link
          href="/oraculo"
          className="text-xs text-[#555] hover:text-[#B43FFF] transition-colors duration-200 font-light flex items-center gap-2 r-sans"
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
          <span className="text-xs text-[#444] font-light tracking-widest uppercase r-sans">
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
              boxShadow: "0 0 100px rgba(180,63,255,0.15), 0 0 0 1px rgba(180,63,255,0.15)",
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
                  <p className="r-sans text-[10px] text-[#444] font-light">{MOCK.fecha}</p>
                </div>
                <p className="r-sans text-[10px] font-mono text-[#333] tracking-wider">{MOCK.edicion}</p>
              </div>

              <div className="flex flex-col gap-3">
                <div className="flex justify-center mb-4">
                  <div
                    className="cristal-apagado"
                    style={{
                      width: "52px", height: "52px",
                      background: "linear-gradient(135deg, rgba(180,63,255,0.5) 0%, rgba(236,72,153,0.3) 50%, rgba(180,63,255,0.7) 100%)",
                      clipPath: "polygon(50% 0%, 80% 20%, 100% 60%, 75% 100%, 25% 100%, 0% 60%, 20% 20%)",
                    }}
                  />
                </div>

                <h1 className="r-serif text-3xl font-light text-white text-center leading-snug" style={{ fontStyle: "italic" }}>
                  {MOCK.arquetipo}
                </h1>

                <div className="flex justify-center">
                  <SistemasRow size="sm" />
                </div>

                <div className="flex flex-col gap-2 mt-2">
                  <MiniSistemaRow color="#C084FC" label="Maya" value={`${MOCK.nahual} (${MOCK.nahualdesc}) · Tono ${MOCK.tono} — ${MOCK.tonodesc}`} />
                  <MiniSistemaRow color="#67E8F9" label="Astral" value={`Sol ${MOCK.sol} · Luna ${MOCK.luna} · Asc ${MOCK.ascendente}`} />
                  <MiniSistemaRow color="#B43FFF" label="Pax" value={`${MOCK.arquetipo} · Intensidad ${MOCK.intensidad}`} />
                </div>
              </div>

              <div>
                <p className="r-sans text-xs text-[#555] font-light">
                  {MOCK.lugarNacimiento} · {MOCK.fechaNacimiento} · {MOCK.horaNacimiento}
                </p>
              </div>
            </div>
          </div>

          {/* Cita de apertura */}
          <blockquote className="r-serif text-base font-light text-[#ccc] leading-relaxed italic text-center px-4">
            "Cuando naciste, un cristal vibró. No fue cualquier cristal — fue uno con tu forma exacta.
            Esta lectura es la primera vez que escuchas su murmullo."
          </blockquote>
        </div>

        <Divisor />

        {/* ── 2. TU ARQUETIPO PAX ── */}
        <div className="section-reveal">
          <SistemaSection
            color="#B43FFF"
            bg="rgba(180,63,255,0.05)"
            border="rgba(180,63,255,0.15)"
            label="Tu arquetipo Pax"
            icon={
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <polygon points="9,0.5 13,3 16,8 13,13 9,15.5 5,13 2,8 5,3" fill="#B43FFF" opacity="0.8" />
              </svg>
            }
          >
            <div className="flex flex-col gap-4">
              {/* Cristales-eco — los 7 arquetipos, visible */}
              <div
                className="relative w-full overflow-hidden rounded-md"
                style={{
                  border: "1px solid rgba(180,63,255,0.2)",
                  boxShadow: "0 0 20px rgba(180,63,255,0.08)",
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
                <p className="r-serif text-2xl font-light" style={{ color: "#B43FFF", fontStyle: "italic" }}>
                  {MOCK.arquetipo}
                </p>
                <span
                  className="r-sans text-[10px] font-light px-2 py-0.5 rounded-full"
                  style={{
                    color: "#B43FFF", border: "1px solid rgba(180,63,255,0.3)",
                    background: "rgba(180,63,255,0.06)",
                  }}
                >
                  Intensidad {MOCK.intensidad}
                </span>
              </div>

              {/* Parrafo 1 — el arquetipo en si */}
              <p className="r-sans text-sm text-[#aaa] font-light leading-relaxed">
                Un Sanador Intenso no trabaja en la superficie. No ofrece consuelo fácil ni respuestas rápidas.
                Trabaja en el fondo del problema, donde todavía no hay palabras para lo que está pasando.
                Si alguna vez sentiste que entras a una conversación y ya sabes lo que la otra persona no pudo
                todavía decir en voz alta — eso es lo que eres. No es intuición mística.
                Es un procesamiento profundo que ocurre antes de que intervenga el pensamiento consciente.
              </p>

              {/* Parrafo 2 — como lo vives en el dia a dia */}
              <p className="r-sans text-sm text-[#aaa] font-light leading-relaxed">
                En la práctica, esto se ve así: cuando alguien en tu círculo está mal, tú lo sabes antes de que
                te lo digan. Cuando una situación está a punto de escalar, tú ya lo sentiste 10 minutos atrás
                y no sabes bien cómo explicarlo. Si pasas más de 3 horas con mucha gente sin pausar,
                necesitas tiempo solo para procesar — no porque seas introvertido, sino porque tu sistema
                está procesando lo que pasa <em>entre</em> las personas, no solo lo que pasa contigo.
                Eso agota. Y también es un don.
              </p>

              {/* Parrafo 3 — sombra/desafio */}
              <div
                className="rounded-md p-4"
                style={{ background: "rgba(180,63,255,0.04)", border: "1px solid rgba(180,63,255,0.12)" }}
              >
                <p className="r-sans text-xs tracking-[0.15em] uppercase font-light mb-2" style={{ color: "#555" }}>
                  La sombra del arquetipo
                </p>
                <p className="r-sans text-sm text-[#999] font-light leading-relaxed">
                  El Sanador Intenso tiene un desafío específico: carga los problemas de otros como si fueran suyos.
                  No por elección — por constitución. Si alguien a tu alrededor está sufriendo y no lo resuelve,
                  a veces sientes que es tu responsabilidad hacerlo. No lo es. El Sanador que no aprende a soltar
                  termina agotado antes de que sea su turno de recibir ayuda.
                  La intensidad es el don. El límite es la práctica que queda por hacer.
                </p>
              </div>

              {/* Parrafo 4 — cuando estas en tu mejor version */}
              <p className="r-sans text-sm text-[#aaa] font-light leading-relaxed">
                Estás en tu mejor versión cuando alguien necesita que alguien entre primero al cuarto difícil.
                La conversación que todos evitaron. El momento donde la persona no sabe cómo pedir ayuda
                y tú simplemente te sientas al lado sin agenda, sin plan, sin necesitar que resulte de cierta manera.
                Cuando eso pasa — cuando entras sin esperar nada a cambio — algo en el universo Pax
                lo llama un <strong className="text-[#B43FFF] font-normal">Gesto</strong>.
                Y ese Gesto enciende algo que no se apaga solo.
              </p>

              {/* Parrafo 5 — como te puede confundir el mundo */}
              <p className="r-sans text-sm text-[#aaa] font-light leading-relaxed">
                El mundo a veces no sabe qué hacer contigo. Te llaman "demasiado serio", "demasiado intenso",
                "por qué siempre vas al fondo de todo". Lo que ellos ven como exceso es exactamente
                tu herramienta de trabajo. Cuando alguien dice "no te tomes las cosas tan a pecho",
                lo que no está viendo es que tú no elegiste tomártelas — simplemente las recibes así.
                Eso no es debilidad. Es el precio de entrada de un arquetipo que opera donde otros no entran.
              </p>

              {/* Cristal-eco */}
              <div
                className="rounded-md p-4 flex items-center gap-4 mt-2"
                style={{ background: "rgba(180,63,255,0.05)", border: "1px solid rgba(180,63,255,0.12)" }}
              >
                <div
                  className="cristal-apagado shrink-0"
                  style={{
                    width: "40px", height: "40px",
                    background: "linear-gradient(135deg, rgba(180,63,255,0.5), rgba(0,0,0,0.8))",
                    clipPath: "polygon(50% 0%, 80% 20%, 100% 60%, 75% 100%, 25% 100%, 0% 60%, 20% 20%)",
                  }}
                />
                <div className="flex flex-col gap-1">
                  <p className="r-sans text-xs uppercase tracking-wider text-[#555] font-light">Tu cristal personal</p>
                  <p className="r-sans text-sm text-white font-light">{MOCK.cristalNombre}</p>
                  <div className="flex items-center gap-2">
                    <div style={{ width: "10px", height: "10px", borderRadius: "2px", background: MOCK.cristalColor, opacity: 0.5 }} />
                    <span className="r-sans text-xs font-mono text-[#555]">{MOCK.cristalHex}</span>
                  </div>
                </div>
              </div>

              {/* Puente Pax */}
              <div className="flex items-center gap-3 mt-1">
                <span style={{ color: "#B43FFF", opacity: 0.7, fontSize: "12px" }}>≈</span>
                <p className="r-sans text-[10px] tracking-[0.2em] uppercase font-light" style={{ color: "#B43FFF", opacity: 0.8 }}>
                  El puente Pax
                </p>
              </div>

              <div
                className="rounded-md p-4"
                style={{ background: "rgba(180,63,255,0.06)", border: "1px solid rgba(180,63,255,0.2)" }}
              >
                <p className="r-serif text-sm font-light leading-relaxed" style={{ color: "#d4aaff", fontStyle: "italic" }}>
                  "Cuando entras primero donde hay oscuridad y sostienes el espacio
                  para que otra persona pueda respirar —
                  eso enciende algo en el universo Pax.
                  Nosotros lo llamamos un <em>Gesto</em>.
                  Ese Gesto no lo puede hacer nadie más.
                  Solo el que entró."
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
            <p className="r-sans text-sm text-[#888] font-light leading-relaxed">
              Con tu perfil — Sanador Intenso, agua triple, umbral — hay maneras concretas en que tu energía
              puede aportar a que Pax llegue más lejos. No todas requieren tiempo ni dinero.
            </p>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-2">
              <TribuCard
                icon={
                  <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                    <path d="M9 2C9 2 4 5 4 10C4 12.8 6.2 15 9 15C11.8 15 14 12.8 14 10C14 5 9 2 9 2Z" stroke="#EC4899" strokeWidth="1.2" fill="none" opacity="0.7" />
                    <circle cx="9" cy="10" r="1.5" fill="#EC4899" opacity="0.8" />
                  </svg>
                }
                title="Acompañar en silencio"
                description="No resolver — solo estar presente. Tu agua triple te da una capacidad de presencia que pocas personas tienen. Sentarse con alguien que está pasando algo difícil, sin agenda, ya es un Gesto."
                accentColor="#EC4899"
              />
              <TribuCard
                icon={
                  <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                    <path d="M3 9 Q6 4 9 9 Q12 14 15 9" stroke="#EC4899" strokeWidth="1.5" fill="none" strokeLinecap="round" opacity="0.7" />
                    <circle cx="3" cy="9" r="1.5" fill="#EC4899" opacity="0.5" />
                    <circle cx="15" cy="9" r="1.5" fill="#EC4899" opacity="0.5" />
                  </svg>
                }
                title="Compartir lo que percibes"
                description="El Sanador Intenso ve cosas que otros no ven todavía. Escribirlo, contarlo, publicarlo — transmitir esa perspectiva ya activa algo. Si algo de esta lectura resuena, compartirla es un Gesto concreto."
                accentColor="#EC4899"
              />
              <TribuCard
                icon={
                  <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                    <rect x="3" y="8" width="5" height="7" rx="1" stroke="#EC4899" strokeWidth="1.2" fill="none" opacity="0.6" />
                    <rect x="10" y="5" width="5" height="10" rx="1" stroke="#EC4899" strokeWidth="1.2" fill="none" opacity="0.6" />
                    <path d="M5.5 8V5M12.5 5V2" stroke="#EC4899" strokeWidth="1" strokeLinecap="round" opacity="0.4" />
                  </svg>
                }
                title="Donar lo que puedas"
                description="Cada peso del Oráculo se dona al 100% a fundaciones reales. No hay monto mínimo. Tu intensidad Escorpio-Piscis sabe que las cosas que importan merecen que les demos algo real."
                accentColor="#EC4899"
              />
              <TribuCard
                icon={
                  <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                    <circle cx="9" cy="6" r="3" stroke="#EC4899" strokeWidth="1.2" fill="none" opacity="0.7" />
                    <path d="M3 16C3 12.7 5.7 10 9 10S15 12.7 15 16" stroke="#EC4899" strokeWidth="1.2" fill="none" opacity="0.5" strokeLinecap="round" />
                    <path d="M12 7C13 5.5 15 5 16 6" stroke="#EC4899" strokeWidth="1" fill="none" opacity="0.4" strokeLinecap="round" />
                  </svg>
                }
                title="Crear un espacio de cuidado"
                description="Un grupo, un canal, un encuentro mensual. Personas que también sienten demasiado. Tu perfil Acuario-ascendente hace que esos espacios se vuelvan comunidad cuando tú los convocas."
                accentColor="#EC4899"
              />
              <TribuCard
                icon={
                  <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                    <path d="M9 3L10.5 7H15L11.5 9.5L13 13.5L9 11L5 13.5L6.5 9.5L3 7H7.5L9 3Z" stroke="#EC4899" strokeWidth="1.2" fill="none" opacity="0.7" strokeLinejoin="round" />
                  </svg>
                }
                title="Dar ideas de mejora"
                description="¿Ves algo que podría estar mejor en Pax? Dilo. El Sanador Intenso tiene diagnóstico rápido — percibe dónde algo no funciona antes de que los demás lo noten. Esa mirada crítica y constructiva es un regalo."
                accentColor="#EC4899"
              />
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
              <DataBlock label="Nahual" value={MOCK.nahual} sub={MOCK.nahualdesc} color="#C084FC" />
              <DataBlock label="Tono" value={MOCK.tono} sub={MOCK.tonodesc} color="#C084FC" />
            </div>

            {/* Parrafo 1 — el nahual Ix */}
            <p className="r-sans text-sm text-[#999] font-light leading-relaxed">
              Ix es el jaguar maya: animal de noche, cazador silencioso, custodio de espacios sagrados.
              No es el jaguar agresivo de la iconografía occidental — es el guardián que se mueve sin ser visto,
              que entra primero a la oscuridad y la conoce antes de que llegue el resto.
              Si naciste bajo Ix, ya sabes lo que es entrar a un lugar y sentir cosas que nadie más siente.
              Sabes lo que es percibir el malestar de alguien sin que esa persona lo haya dicho en voz alta.
              Esto no es magia — es una sensibilidad fina que la tradición maya nombra y honra como un don específico.
            </p>

            {/* Parrafo 2 — el tono 7 */}
            <p className="r-sans text-sm text-[#999] font-light leading-relaxed">
              Tu tono 7 es el tono del equilibrio: el centro exacto del Tzolkin,
              el punto entre el comienzo (1) y el cierre (13).
              Vivir bajo el tono 7 significa que tu energía natural busca armonizar antes que dominar.
              Cuando estás en balance, eres puente entre extremos — el que puede estar con la persona enojada
              y con la persona herida al mismo tiempo, sin tomar partido, sin perder el centro.
              Cuando no estás en balance, intentas equilibrar todo a costa tuya, hasta que no queda nada.
            </p>

            {/* Parrafo 3 — el cruce con Pax */}
            <div
              className="rounded-md p-4"
              style={{ background: "rgba(192,132,252,0.06)", border: "1px solid rgba(192,132,252,0.15)" }}
            >
              <p className="r-sans text-xs tracking-[0.15em] uppercase font-light mb-2" style={{ color: "#555" }}>
                El cruce — Maya confirma a Pax
              </p>
              <p className="r-sans text-sm text-[#bbb] font-light leading-relaxed">
                El cruce Ix + Tono 7 es exactamente el arquetipo del Sanador Intenso que Pax ya describió,
                pero contado desde hace dos mil años. Una sensibilidad de jaguar para percibir lo que no se dice,
                y un don de equilibrio para sostener sin imponer. Maya y Pax están diciendo lo mismo
                desde dos siglos distintos, en dos idiomas distintos. Eso no es coincidencia.
                Es el patrón que llevas desde que naciste.
              </p>
            </div>

            {/* Parrafo 4 — anecdota concreta */}
            <p className="r-sans text-sm text-[#999] font-light leading-relaxed">
              Piensa en la última vez que alguien llegó a ti "sin nada en particular" — sin saber muy bien
              por qué te escribió o te llamó — y terminó contándote algo que no le había contado a nadie.
              Eso es Ix + 7 en acción. El jaguar crea el espacio de confianza sin hacer nada visible.
              El tono 7 lo mantiene estable mientras la persona llega sola a lo que necesita decir.
              No necesitaste forzar nada. Solo estar.
            </p>

            {/* Parrafo 5 — sombra del nahual+tono */}
            <p className="r-serif text-sm font-light leading-relaxed" style={{ color: "#d4b8f0", fontStyle: "italic" }}>
              "La sombra de Ix es el aislamiento: el jaguar que se aleja demasiado y olvida volver.
              La sombra del tono 7 es el agotamiento del puente — sostener tanta tensión sin que nadie
              sostenga a quien sostiene. Si reconoces ese patrón, la tradición maya te diría:
              encuentra tu cueva. No para esconderte. Para recargar."
            </p>
          </SistemaSection>
        </div>

        <Divisor />

        {/* ── 5. COMO SE INTERLAZA CON ASTRAL ── */}
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
              <DataBlock label="Sol" value={MOCK.sol} sub="Energía que expresas" color="#67E8F9" />
              <DataBlock label="Luna" value={MOCK.luna} sub="Energía que necesitas" color="#67E8F9" />
              <DataBlock label="Ascendente" value={MOCK.ascendente} sub="Lo que el mundo percibe" color="#67E8F9" />
              <DataBlock label="Casa dominante" value="XII" sub={MOCK.casa} color="#67E8F9" />
            </div>

            {/* Parrafo 1 — sol Escorpio */}
            <p className="r-sans text-sm text-[#999] font-light leading-relaxed">
              Sol en Escorpio: lo que te mueve por dentro no es fácil de explicar a alguien que no lo siente.
              Escorpio no busca lo superficial — busca el fondo. Si miras tus relaciones más importantes,
              vas a ver que ninguna fue casual ni liviana. Cuando algo no te importa hasta los huesos, no te interesa.
              Eso es agotador para ti y a veces incomprensible para los demás,
              pero es la forma exacta en que tu sol arde. No hay versión tuya que funcione a media intensidad.
            </p>

            {/* Parrafo 2 — luna Piscis */}
            <p className="r-sans text-sm text-[#999] font-light leading-relaxed">
              Luna en Piscis: tu mundo interior es agua. Sientes lo que va a pasar antes de que pase.
              Lloras con películas que otros no entienden por qué te afectan.
              Te disuelves en la energía de los lugares — entras a un cuarto y ya sabes si ahí hubo pelea
              hace dos horas, aunque nadie te lo diga. Esto puede ser una bendición enorme
              (empatía sin límite, conexión real con los demás) o un agujero (te confundes con el otro,
              absorbes lo que no es tuyo, pierdes el borde de dónde terminas tú).
              Saber que esa luna es tu luna te da algo concreto: la posibilidad de honrarla en vez de pelearla.
            </p>

            {/* Parrafo 3 — ascendente Acuario */}
            <p className="r-sans text-sm text-[#999] font-light leading-relaxed">
              Ascendente Acuario: el mundo te ve más distante de lo que eres.
              Acuario es la máscara del visionario — la persona que piensa en sistemas, que ve el problema
              desde arriba antes de bajarse al detalle, que se desconecta cuando se siente sobre-estimulada.
              Eres un Escorpio-Piscis intenso por dentro, pero llegas a la gente con la frescura de Acuario.
              Esa aparente contradicción no es bug — es exactamente la combinación que hace que las personas
              confíen en ti antes de conocerte bien. Te ven como alguien que no va a juzgar. Y tienen razón.
            </p>

            {/* Parrafo 4 — el cruce con Pax y Maya */}
            <div
              className="rounded-md p-4"
              style={{ background: "rgba(103,232,249,0.05)", border: "1px solid rgba(103,232,249,0.12)" }}
            >
              <p className="r-sans text-xs tracking-[0.15em] uppercase font-light mb-2" style={{ color: "#555" }}>
                El cruce — Astral confirma a Pax y a Maya
              </p>
              <p className="r-sans text-sm text-[#bbb] font-light leading-relaxed">
                Escorpio va al fondo, Piscis disuelve los bordes, Acuario sostiene sin juzgar.
                Es el mismo perfil que Ix el Jaguar + Tono 7 describió desde Maya, y el mismo perfil
                que el arquetipo Sanador Intenso nombró desde Pax.
                Tres sistemas, tres siglos distintos, el mismo patrón.
                Lo que cambia es el lenguaje. Lo que no cambia eres tú.
              </p>
            </div>

            {/* Parrafo 5 — casa XII + aspecto especifico */}
            <p className="r-sans text-sm text-[#999] font-light leading-relaxed">
              La Casa XII es la casa de lo que no se ve: el inconsciente, los procesos que ocurren
              por debajo de la superficie antes de llegar al mundo visible.
              Tener influencia en la Casa XII con tu combinación agua significa que tu trabajo real
              suele ocurrir en espacios que otros no pueden ver ni medir — las conversaciones que nadie sabe
              que tuviste, el sostén emocional que diste sin que quedara registro, el cambio que facilitaste
              sin que nadie supiera que fuiste tú. Ese trabajo existe. Vale lo mismo que cualquier trabajo visible.
              Más, incluso.
            </p>
          </SistemaSection>
        </div>

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
                Esta semana busca una conversación que estás evitando —
                solo una — e iníciala tú primero.
                No tienes que resolverla. Solo abrirla.
                Eso enciende el cristal del <strong className="text-[#FCD34D] font-normal">Sanador</strong>.
              </p>
            </div>

            <p className="r-sans text-xs text-[#555] font-light leading-relaxed">
              No tiene que ser perfecto. No tiene que resultar bien. Solo tiene que ser honesto.
              Un Gesto pequeño y real pesa más que cien gestos pensados y no hechos.
            </p>

            <label className="flex items-center gap-3 cursor-pointer mt-1" style={{ userSelect: "none" }}>
              <input type="checkbox" className="w-4 h-4 cursor-pointer" style={{ accentColor: "#FCD34D" }} />
              <span className="r-sans text-sm text-[#666] font-light">
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
            {/* Layout: imagen arriba en mobile, lateral en md+ */}
            <div className="flex flex-col md:flex-row">
              {/* Retrato de la abuela — imagen visible */}
              <div
                className="relative shrink-0"
                style={{ width: "100%", height: "180px" }}
              >
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
              <div
                className="hidden md:block relative shrink-0"
                style={{ width: "180px", minHeight: "180px" }}
              >
                <Image
                  src="/images/oraculo-v3/agatha-portrait-mistica.png"
                  alt="Una de las abuelas pax leyendo cristales"
                  fill
                  style={{ objectFit: "cover", objectPosition: "top", borderRadius: "0" }}
                  sizes="180px"
                />
                <div style={{ position: "absolute", inset: 0, background: "linear-gradient(to right, transparent 60%, rgba(0,0,0,0.85) 100%)" }} />
              </div>

              {/* Texto */}
              <div className="p-6 flex flex-col gap-4 -mt-12 md:mt-0 relative z-10">
                <div className="flex items-center gap-2">
                  <span style={{ color: "#FCD34D", opacity: 0.4, fontSize: "10px" }}>≈</span>
                  <p className="r-sans text-[10px] tracking-[0.2em] uppercase font-light" style={{ color: "#555" }}>
                    Los abuelos pax cierran
                  </p>
                </div>
                <blockquote
                  className="r-serif text-sm font-light leading-relaxed italic"
                  style={{ color: "#aaa", borderLeft: "2px solid rgba(252,211,77,0.2)", paddingLeft: "14px" }}
                >
                  "No sé cuándo vas a hacer ese Gesto.
                  Pero el cristal ya vibró cuando te escuché llegar.
                  Lo que enciendes arriba,
                  lo recibimos abajo."
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
            <p className="r-serif text-base font-light text-[#888]" style={{ fontStyle: "italic" }}>
              Tu cristal personal está apagado.
            </p>
            <p className="r-sans text-xs text-[#555] font-light leading-relaxed">
              Completar el ciclo enciende tu cristal en el universo Pax.
              El dinero llega al 100% a una fundación real — sin monto mínimo.
            </p>
          </div>

          <button
            className="cta-encender w-full px-12 py-5 rounded-full text-white tracking-wide transition-all duration-300 flex items-center justify-center gap-3"
          >
            {/* Cristal icon SVG */}
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

            {/* Label */}
            <span className="flex flex-col items-center gap-0.5">
              <span
                className="r-serif text-lg"
                style={{ fontStyle: "italic", fontWeight: 300, letterSpacing: "0.04em" }}
              >
                Encender el cristal
              </span>
              <span
                className="r-sans text-[10px] font-light tracking-[0.2em] uppercase"
                style={{ color: "rgba(212,168,87,0.8)" }}
              >
                pay what you can · 100% va a fundaciones
              </span>
            </span>
          </button>

          <p className="r-sans text-center text-[10px] text-[#333] font-light">
            Sin monto mínimo · el cristal enciende igual · impacto real
          </p>
        </div>

        <div className="text-center pb-4">
          <Link
            href="/oraculo/como-funciona"
            className="r-sans text-xs text-[#444] hover:text-[#B43FFF] transition-colors duration-200 font-light"
          >
            Cómo se construyó esta lectura →
          </Link>
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
  videoBg?: string;
}

function SistemaSection({ color, bg, border, label, icon, children, videoBg }: SistemaSectionProps) {
  return (
    <div className="rounded-lg overflow-hidden relative" style={{ background: bg, border: `1px solid ${border}` }}>
      {videoBg && (
        <video
          src={videoBg}
          autoPlay
          loop
          muted
          playsInline
          className="tribu-video-bg"
        />
      )}
      <div className="px-5 py-4 flex items-center gap-3 border-b relative z-10" style={{ borderColor: border }}>
        {icon}
        <p className="r-sans text-xs tracking-[0.18em] uppercase font-light" style={{ color }}>
          {label}
        </p>
      </div>
      <div className="px-5 py-5 flex flex-col gap-3 relative z-10">
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
      <p className="r-sans text-[10px] uppercase tracking-wider font-light" style={{ color: "#555" }}>{label}</p>
      <p className="r-serif text-lg font-light" style={{ color }}>{value}</p>
      <p className="r-sans text-[10px] font-light" style={{ color: "#555" }}>{sub}</p>
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
      <span style={{ color: "#888", fontWeight: 300 }}>{value}</span>
    </div>
  );
}

/* ------------------------------------------------------------------ */
/* TribuCard — card de la sección "Cómo tu cristal vibra con la tribu" */
/* ------------------------------------------------------------------ */
interface TribuCardProps {
  icon: React.ReactNode;
  title: string;
  description: string;
  accentColor: string;
}

function TribuCard({ icon, title, description, accentColor }: TribuCardProps) {
  return (
    <div
      className="tribu-card rounded-md p-4 flex flex-col gap-2"
      style={{
        background: "rgba(236,72,153,0.03)",
        border: "1px solid rgba(236,72,153,0.1)",
      }}
    >
      <div className="flex items-center gap-2">
        {icon}
        <p
          className="r-sans text-xs font-light"
          style={{ color: accentColor, letterSpacing: "0.04em" }}
        >
          {title}
        </p>
      </div>
      <p className="r-sans text-xs text-[#666] font-light leading-relaxed">
        {description}
      </p>
    </div>
  );
}
