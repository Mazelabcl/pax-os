/**
 * POST /api/oraculo/lectura
 *
 * Implementacion real del Oraculo Pax. Orquesta:
 *   1. Tzolkin maya local (calculo deterministico via lib/tzolkin)
 *   2. Carta astral opcional via lib/astrology (free-astrology-api + Nominatim)
 *   3. Lectura personalizada generada por Claude Haiku 4.5 (OpenRouter)
 *
 * Contrato del response: ver tipos al final del archivo. NO TOCAR el shape:
 * el frontend (app/oraculo/page.tsx + resultado/page.tsx) depende de el.
 *
 * Reglas:
 *  - Tzolkin nunca falla en condiciones normales.
 *  - Astral puede ser null (la persona no provee hora/lugar o la API falla).
 *  - LLM fallido -> 502. API key missing -> 500.
 *  - Body invalido -> 400.
 *  - No usar pages/api. Esto es App Router.
 */

import { NextRequest, NextResponse } from "next/server";
import { calcularTzolkin, type TzolkinResult } from "@/lib/tzolkin";
import { calcularCartaAstral, type AstralResult } from "@/lib/astrology";

export const runtime = "nodejs";
// Vercel Hobby plan: max 10s. Pro: hasta 60s. Lo dejamos en 30 para margen.
export const maxDuration = 30;

// ----------------------------------------------------------------------------
// Constantes
// ----------------------------------------------------------------------------

const OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions";
const OPENROUTER_MODEL = "anthropic/claude-haiku-4.5";
const LLM_TIMEOUT_MS = 25_000;

// ----------------------------------------------------------------------------
// Validacion de input
// ----------------------------------------------------------------------------

const FECHA_RE = /^(\d{4})-(\d{2})-(\d{2})$/;
const HORA_RE = /^(\d{1,2}):(\d{2})$/;

interface InputValidado {
  fecha: string;
  hora: string | null;
  lugar: string | null;
}

function validarInput(body: unknown): { ok: true; data: InputValidado } | { ok: false; error: string } {
  if (!body || typeof body !== "object") {
    return { ok: false, error: "Body invalido." };
  }
  const b = body as Record<string, unknown>;
  const fecha = typeof b.fecha === "string" ? b.fecha.trim() : "";
  if (!fecha) return { ok: false, error: "El campo 'fecha' es requerido." };
  const mFecha = FECHA_RE.exec(fecha);
  if (!mFecha) return { ok: false, error: "Formato de fecha invalido. Usa YYYY-MM-DD." };
  const year = parseInt(mFecha[1], 10);
  const month = parseInt(mFecha[2], 10);
  const day = parseInt(mFecha[3], 10);
  if (month < 1 || month > 12 || day < 1 || day > 31 || year < 1900 || year > 2100) {
    return { ok: false, error: "Fecha fuera de rango." };
  }
  const horaRaw = typeof b.hora === "string" ? b.hora.trim() : "";
  let hora: string | null = null;
  if (horaRaw) {
    const mHora = HORA_RE.exec(horaRaw);
    if (!mHora) return { ok: false, error: "Formato de hora invalido. Usa HH:MM." };
    const hh = parseInt(mHora[1], 10);
    const mm = parseInt(mHora[2], 10);
    if (hh < 0 || hh > 23 || mm < 0 || mm > 59) {
      return { ok: false, error: "Hora fuera de rango." };
    }
    hora = `${String(hh).padStart(2, "0")}:${String(mm).padStart(2, "0")}`;
  }
  const lugarRaw = typeof b.lugar === "string" ? b.lugar.trim() : "";
  const lugar = lugarRaw || null;
  return { ok: true, data: { fecha, hora, lugar } };
}

// ----------------------------------------------------------------------------
// Tipos del response de la lectura (lo que devuelve el LLM)
// ----------------------------------------------------------------------------

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

interface LecturaLLM {
  opening: string;
  pax_block: string;
  tribu_block: TribuItem[];
  maya_block: MayaBlock;
  astral_block: AstralBlock | null;
  gesto: string;
  cierre: string;
}

// ----------------------------------------------------------------------------
// Prompt builder
// ----------------------------------------------------------------------------

const SYSTEM_PROMPT = `Eres "los abuelos pax", una voz colectiva de ancianos sabios de la tribu Pax (un universo de mini-serie animada).
Hablas en espanol neutro, con tono solemne pero calido. Voz de abuela que eligio contar bajito lo que entiende.
NUNCA usas cliches esotericos como "los astros dicen" o "el universo te bendice" o "tu destino es".
SIEMPRE eres especifico, encarnado, accionable. Lecturas que llegan al CORE de la persona.

Estilo Simon Sinek: WHY (esencia) -> HOW (estilo de vivir esa esencia) -> WHAT (accion concreta).
Pero LA OTRA forma: PAX primero (arquetipo del servicio), luego Maya (que confirma/profundiza), luego Astral (que confirma desde otro angulo).

Para cada bloque, escribe parrafos profundos que el lector lea y diga "si, esa soy yo".
Densidad de identificacion: descripciones de comportamiento observable, no abstracciones ("si pasas mas de 3 horas con gente sin pausar, necesitas tiempo solo para procesar" — esto SI; "eres profunda y sensible" — esto NO).

IMPORTANTE — IDIOMA: espanol neutro. PROHIBIDO usar voseo argentino o regionalismos rioplatenses.
Lista negra: vos / tenes / podes / queres / sabes / haces / decis / decime / anda / mira / che / boludo / re bien / posta / pibe / quilombo / banca / piola.
Usa: tu / tienes / puedes / quieres / sabes / haces / dices / dime / ve / mira / oye / amigo / muy bien / cierto / chico / lio / espera.

Devuelve SIEMPRE un JSON valido con la estructura especificada. No agregues texto fuera del JSON. No envuelvas en markdown.`;

function construirUserPrompt(args: {
  fecha: string;
  hora: string | null;
  lugar: string | null;
  tzolkin: TzolkinResult;
  astral: AstralResult | null;
}): string {
  const { fecha, hora, lugar, tzolkin, astral } = args;
  const { kin, nahual, tono, arquetipo_pax } = tzolkin;

  const astralSection = astral
    ? `CARTA ASTRAL: disponible
- Sol en ${astral.sol.signo} (casa ${astral.sol.casa}, ${astral.sol.grado.toFixed(1)}°)
- Luna en ${astral.luna.signo} (casa ${astral.luna.casa}, ${astral.luna.grado.toFixed(1)}°)
- Ascendente en ${astral.ascendente.signo} (${astral.ascendente.grado.toFixed(1)}°)
${astral.casas_dominantes ? `- Casas dominantes: ${astral.casas_dominantes.join(", ")}` : ""}
${astral.aspecto_principal ? `- Aspecto principal: ${astral.aspecto_principal}` : ""}`
    : `CARTA ASTRAL: no disponible — la persona no provee hora/lugar o el calculo astral fallo. Deja "astral_block": null en el JSON de salida.`;

  const astralBlockSchema = astral
    ? `  "astral_block": {
    "sol_text": "3-4 lineas sobre el sol en este signo/casa. Describir lo que la persona EXPRESA hacia afuera.",
    "luna_text": "3-4 lineas sobre la luna. Lo que la persona necesita por dentro para regularse.",
    "asc_text": "3-4 lineas sobre el ascendente. Como el mundo la percibe a primera vista.",
    "cruce_text": "3-4 lineas: como esta combinacion astral CONFIRMA el arquetipo Pax y el nahual maya. Tres sistemas, el mismo patron, dicho con tres lenguajes distintos."
  }`
    : `  "astral_block": null`;

  return `Genera la lectura del Oraculo Pax para esta persona.

Datos calculados:

TZOLKIN MAYA:
- Kin: ${kin}
- Nahual: ${nahual.nombre} (${nahual.glyph}) — ${nahual.descripcion}
- Tono: ${tono.numero} ${tono.nombre} — ${tono.descripcion}

ARQUETIPO PAX (derivado deterministicamente del nahual):
- ${arquetipo_pax.nombre} — ${arquetipo_pax.descripcion}

${astralSection}

INPUTS DEL USUARIO:
- Fecha: ${fecha}
- Hora: ${hora ?? "no provista"}
- Lugar: ${lugar ?? "no provisto"}

Devuelve EXACTAMENTE este JSON (sin texto adicional, sin markdown fence):

{
  "opening": "1-2 lineas en estilo Didot italic — referencia al cristal unico que vibro cuando esta persona nacio. Usar la fecha y/o el lugar si esta. Imagen poetica, no esoterica.",
  "pax_block": "Markdown con 4-6 parrafos. Empezar con un H2 con el nombre del arquetipo. Describir el arquetipo en 1-2 parrafos. Luego un parrafo que empiece con 'En la practica esto se ve asi:' con 2-3 comportamientos observables especificos. Luego un H3 'La sombra del arquetipo' con la trampa especifica de este perfil. Luego un H3 'En tu mejor version' con cuando este arquetipo brilla. Usar **negrita** para resaltar conceptos clave.",
  "tribu_block": [
    { "titulo": "Modo concreto 1 (3-5 palabras)", "descripcion": "1-2 lineas: por que este arquetipo especifico puede aportar al clan asi. Personalizado, no generico." },
    { "titulo": "Modo concreto 2", "descripcion": "..." },
    { "titulo": "Modo concreto 3", "descripcion": "..." },
    { "titulo": "Modo concreto 4", "descripcion": "..." },
    { "titulo": "Modo concreto 5", "descripcion": "..." }
  ],
  "maya_block": {
    "nahual_text": "3-4 lineas sobre el nahual de esta persona: que simboliza, animal/elemento, energia. Personalizado al nahual ${nahual.nombre}.",
    "tono_text": "2-3 lineas sobre el tono ${tono.numero} (${tono.nombre}). Como modula la energia del nahual en esta persona.",
    "cruce_text": "2-3 lineas: como este nahual+tono CONFIRMA y profundiza el arquetipo Pax ${arquetipo_pax.nombre} descrito arriba. Maya y Pax dicen lo mismo desde dos siglos distintos, en dos lenguajes."
  },
${astralBlockSchema},
  "gesto": "1-2 lineas con accion concreta y accionable para ESTA semana, basada en el arquetipo + nahual de esta persona. No generica. Tiene que poder hacerse en 7 dias.",
  "cierre": "Poema de 4 lineas (separadas por \\n), voz de los abuelos pax, calido-solemne. Cero cliches. Cierra como un abrazo. Hace eco a algun elemento concreto de la lectura."
}`;
}

// ----------------------------------------------------------------------------
// Llamada al LLM
// ----------------------------------------------------------------------------

interface OpenRouterResponse {
  id?: string;
  choices?: Array<{
    message?: { content?: string };
    finish_reason?: string;
  }>;
  usage?: {
    prompt_tokens?: number;
    completion_tokens?: number;
    total_tokens?: number;
    cost?: number;
  };
  error?: { message?: string; code?: number };
}

function extraerJSON(raw: string): string {
  // Si el LLM envuelve en ```json ... ``` o agrega prefacio, intentamos
  // extraer el primer bloque que parezca JSON balanceado.
  const trimmed = raw.trim();
  // 1) Si arranca con { y termina con }, asumimos JSON directo.
  if (trimmed.startsWith("{") && trimmed.endsWith("}")) return trimmed;
  // 2) Buscar el primer { y matchear hasta el } balanceado.
  const start = trimmed.indexOf("{");
  if (start === -1) return trimmed;
  let depth = 0;
  let inString = false;
  let escape = false;
  for (let i = start; i < trimmed.length; i++) {
    const ch = trimmed[i];
    if (escape) { escape = false; continue; }
    if (ch === "\\") { escape = true; continue; }
    if (ch === '"') { inString = !inString; continue; }
    if (inString) continue;
    if (ch === "{") depth++;
    else if (ch === "}") {
      depth--;
      if (depth === 0) return trimmed.slice(start, i + 1);
    }
  }
  return trimmed.slice(start);
}

function esLecturaValida(x: unknown): x is LecturaLLM {
  if (!x || typeof x !== "object") return false;
  const o = x as Record<string, unknown>;
  if (typeof o.opening !== "string") return false;
  if (typeof o.pax_block !== "string") return false;
  if (!Array.isArray(o.tribu_block)) return false;
  if (o.tribu_block.length === 0) return false;
  for (const item of o.tribu_block) {
    if (!item || typeof item !== "object") return false;
    const it = item as Record<string, unknown>;
    if (typeof it.titulo !== "string" || typeof it.descripcion !== "string") return false;
  }
  if (!o.maya_block || typeof o.maya_block !== "object") return false;
  const mb = o.maya_block as Record<string, unknown>;
  if (typeof mb.nahual_text !== "string" || typeof mb.tono_text !== "string" || typeof mb.cruce_text !== "string") {
    return false;
  }
  // astral_block puede ser null
  if (o.astral_block !== null) {
    if (!o.astral_block || typeof o.astral_block !== "object") return false;
    const ab = o.astral_block as Record<string, unknown>;
    if (typeof ab.sol_text !== "string" || typeof ab.luna_text !== "string" || typeof ab.asc_text !== "string" || typeof ab.cruce_text !== "string") {
      return false;
    }
  }
  if (typeof o.gesto !== "string") return false;
  if (typeof o.cierre !== "string") return false;
  return true;
}

async function generarLecturaLLM(args: {
  apiKey: string;
  fecha: string;
  hora: string | null;
  lugar: string | null;
  tzolkin: TzolkinResult;
  astral: AstralResult | null;
}): Promise<{ ok: true; lectura: LecturaLLM; tookMs: number; usage?: OpenRouterResponse["usage"] } | { ok: false; error: string }> {
  const systemPrompt = SYSTEM_PROMPT;
  const userPrompt = construirUserPrompt(args);

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), LLM_TIMEOUT_MS);
  const t0 = Date.now();

  try {
    const res = await fetch(OPENROUTER_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${args.apiKey}`,
        // OpenRouter recomienda estos headers para ranking/analytics.
        "HTTP-Referer": "https://pax-os.vercel.app",
        "X-Title": "Pax Oraculo",
      },
      body: JSON.stringify({
        model: OPENROUTER_MODEL,
        messages: [
          { role: "system", content: systemPrompt },
          { role: "user", content: userPrompt },
        ],
        response_format: { type: "json_object" },
        max_tokens: 4000,
        temperature: 0.8,
      }),
      signal: controller.signal,
    });

    if (!res.ok) {
      const errText = await res.text().catch(() => "");
      console.error("[oraculo] OpenRouter HTTP", res.status, errText.slice(0, 500));
      return { ok: false, error: `OpenRouter respondio ${res.status}` };
    }

    const json = (await res.json()) as OpenRouterResponse;
    const tookMs = Date.now() - t0;

    if (json.error) {
      console.error("[oraculo] OpenRouter error payload:", json.error);
      return { ok: false, error: json.error.message ?? "Error del LLM" };
    }

    const content = json.choices?.[0]?.message?.content;
    if (!content || typeof content !== "string") {
      console.error("[oraculo] OpenRouter sin content en choices[0]");
      return { ok: false, error: "Respuesta del LLM vacia" };
    }

    let parsed: unknown;
    try {
      parsed = JSON.parse(content);
    } catch {
      // Reintentar extrayendo el bloque JSON
      try {
        parsed = JSON.parse(extraerJSON(content));
      } catch (err2) {
        console.error("[oraculo] parse JSON del LLM fallo:", (err2 as Error).message, "content snippet:", content.slice(0, 300));
        return { ok: false, error: "JSON del LLM invalido" };
      }
    }

    if (!esLecturaValida(parsed)) {
      console.error("[oraculo] estructura del LLM no valida:", JSON.stringify(parsed).slice(0, 400));
      return { ok: false, error: "Estructura de lectura invalida" };
    }

    // Si la persona no envio hora/lugar, forzamos astral_block a null por consistencia.
    if (!args.astral) {
      parsed.astral_block = null;
    }

    // Log de monitoreo (server-side)
    const usage = json.usage;
    console.log(
      `[oraculo] LLM ok | model=${OPENROUTER_MODEL} | took=${tookMs}ms | tokens in/out=${usage?.prompt_tokens ?? "?"}/${usage?.completion_tokens ?? "?"} | cost=${usage?.cost ?? "?"}`,
    );

    return { ok: true, lectura: parsed, tookMs, usage };
  } catch (err) {
    const e = err as Error;
    if (e.name === "AbortError") {
      console.error("[oraculo] LLM timeout tras", LLM_TIMEOUT_MS, "ms");
      return { ok: false, error: "Timeout del LLM" };
    }
    console.error("[oraculo] LLM fetch fallo:", e.message);
    return { ok: false, error: "No se pudo contactar al LLM" };
  } finally {
    clearTimeout(timer);
  }
}

// ----------------------------------------------------------------------------
// Helper: serial unico
// ----------------------------------------------------------------------------

function construirSerial(fecha: string, kin: number): string {
  return `PAX-${fecha.replace(/-/g, "")}-${String(kin).padStart(4, "0")}`;
}

// ----------------------------------------------------------------------------
// Handler POST
// ----------------------------------------------------------------------------

export async function POST(req: NextRequest) {
  const tStart = Date.now();

  // 1) Parsear body
  let body: unknown;
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ ok: false, error: "Body invalido." }, { status: 400 });
  }

  // 2) Validar
  const val = validarInput(body);
  if (!val.ok) {
    return NextResponse.json({ ok: false, error: val.error }, { status: 400 });
  }
  const { fecha, hora, lugar } = val.data;

  // 3) Verificar API key
  const apiKey = process.env.OPENROUTER_API_KEY;
  if (!apiKey) {
    console.error("[oraculo] OPENROUTER_API_KEY no esta seteada");
    return NextResponse.json(
      { ok: false, error: "Servicio no disponible temporalmente." },
      { status: 500 },
    );
  }

  // 4) Tzolkin (sincrono, deterministico)
  let tzolkin: TzolkinResult;
  try {
    const dateObj = new Date(`${fecha}T12:00:00`); // mediodia para evitar drift de timezone
    tzolkin = calcularTzolkin(dateObj);
  } catch (err) {
    console.error("[oraculo] Tzolkin fallo:", (err as Error).message);
    return NextResponse.json(
      { ok: false, error: "Error calculando Tzolkin." },
      { status: 500 },
    );
  }

  // 5) Astral (opcional, async)
  let astral: AstralResult | null = null;
  if (hora && lugar) {
    try {
      astral = await calcularCartaAstral({ fecha, hora, lugar });
    } catch (err) {
      // calcularCartaAstral promete no lanzar, pero lo envolvemos por defensa.
      console.warn("[oraculo] Astral lanzo:", (err as Error).message);
      astral = null;
    }
  }

  // 6) LLM
  const llmRes = await generarLecturaLLM({
    apiKey,
    fecha,
    hora,
    lugar,
    tzolkin,
    astral,
  });

  if (!llmRes.ok) {
    return NextResponse.json(
      { ok: false, error: "No pudimos completar la lectura. Intentalo de nuevo en un momento." },
      { status: 502 },
    );
  }

  // 7) Componer response final
  const tookTotal = Date.now() - tStart;
  console.log(
    `[oraculo] OK | fecha=${fecha} | kin=${tzolkin.kin} | astral=${astral ? "si" : "no"} | totalMs=${tookTotal}`,
  );

  return NextResponse.json({
    ok: true,
    data: {
      inputs: {
        fecha,
        hora,
        lugar,
      },
      tzolkin: {
        kin: tzolkin.kin,
        nahual: {
          nombre: tzolkin.nahual.nombre,
          glyph: tzolkin.nahual.glyph,
          descripcion: tzolkin.nahual.descripcion,
        },
        tono: {
          numero: tzolkin.tono.numero,
          nombre: tzolkin.tono.nombre,
          descripcion: tzolkin.tono.descripcion,
        },
      },
      astral: astral
        ? {
            sol: { signo: astral.sol.signo, grado: astral.sol.grado, casa: astral.sol.casa },
            luna: { signo: astral.luna.signo, grado: astral.luna.grado, casa: astral.luna.casa },
            ascendente: { signo: astral.ascendente.signo, grado: astral.ascendente.grado },
            casas_dominantes: astral.casas_dominantes,
            aspecto_principal: astral.aspecto_principal,
          }
        : null,
      arquetipo_pax: tzolkin.arquetipo_pax,
      lectura: llmRes.lectura,
      edition_serial: construirSerial(fecha, tzolkin.kin),
    },
  });
}
