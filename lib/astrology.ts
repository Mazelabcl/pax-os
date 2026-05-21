/**
 * lib/astrology.ts
 *
 * Wrapper para obtener la carta astral (sol / luna / ascendente) a partir de
 * fecha + hora + lugar. Usa dos servicios gratuitos:
 *
 *   1) OpenStreetMap Nominatim          -> geocodificar lugar -> lat/lon
 *      https://nominatim.openstreetmap.org/search
 *
 *   2) Free Astrology API (western)     -> planetas + casas (tropical)
 *      POST https://json.freeastrologyapi.com/western/planets
 *      POST https://json.freeastrologyapi.com/western/houses
 *      Header: x-api-key: <FREE_ASTROLOGY_API_KEY>
 *
 * Reglas:
 *  - Solo fetch nativo, sin librerias externas.
 *  - Timeout de 10s en cada llamada HTTP (AbortController).
 *  - Cero side effects: solo console.warn / console.error en fallos.
 *  - Nunca lanza: ante cualquier error o dato mal formado devuelve null.
 *  - El caller (API route) decide el fallback (p. ej. solo Tzolkin).
 */

// ---------------------------------------------------------------------------
// Tipos publicos
// ---------------------------------------------------------------------------

export interface AstralResult {
  sol: {
    signo: string;       // "Escorpio", "Piscis", etc (espanol)
    signo_en: string;    // "Scorpio", "Pisces" (input para LLM)
    grado: number;       // 0-30
    casa: number;        // 1-12
  };
  luna: {
    signo: string;
    signo_en: string;
    grado: number;
    casa: number;
  };
  ascendente: {
    signo: string;
    signo_en: string;
    grado: number;
  };
  // Casas dominantes (las 3 con mas planetas) - opcional
  casas_dominantes?: number[];
  // Aspecto mas tenso (oposicion / cuadratura) - opcional
  aspecto_principal?: string;
}

export interface GeocodingResult {
  lat: number;
  lon: number;
  displayName: string;
  timezone?: string;
}

// ---------------------------------------------------------------------------
// Constantes y helpers internos
// ---------------------------------------------------------------------------

const NOMINATIM_URL = "https://nominatim.openstreetmap.org/search";
const ASTRO_PLANETS_URL = "https://json.freeastrologyapi.com/western/planets";
const ASTRO_HOUSES_URL = "https://json.freeastrologyapi.com/western/houses";

const FETCH_TIMEOUT_MS = 6_000;

// Diccionario ingles -> espanol para signos zodiacales.
const SIGNO_ES: Record<string, string> = {
  Aries: "Aries",
  Taurus: "Tauro",
  Gemini: "Géminis",
  Cancer: "Cáncer",
  Leo: "Leo",
  Virgo: "Virgo",
  Libra: "Libra",
  Scorpio: "Escorpio",
  Sagittarius: "Sagitario",
  Capricorn: "Capricornio",
  Aquarius: "Acuario",
  Pisces: "Piscis",
};

/**
 * fetch con timeout via AbortController. Devuelve null si excede el timeout
 * o si la respuesta no es ok. Nunca lanza.
 */
async function fetchConTimeout(
  url: string,
  init: RequestInit = {},
  timeoutMs: number = FETCH_TIMEOUT_MS,
): Promise<Response | null> {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const res = await fetch(url, { ...init, signal: controller.signal });
    if (!res.ok) {
      console.warn(`[astrology] HTTP ${res.status} en ${url}`);
      return null;
    }
    return res;
  } catch (err) {
    console.warn(`[astrology] fetch fallo en ${url}:`, (err as Error).message);
    return null;
  } finally {
    clearTimeout(timer);
  }
}

/**
 * Estima un offset de zona horaria (en horas) a partir de la longitud.
 * Aproximacion suficiente para calculos astrales (la API toma el valor como
 * offset numerico). offset = lon / 15, redondeado a 0.5h mas cercano.
 */
function timezoneDesdeLongitud(lon: number): number {
  const raw = lon / 15;
  // redondeo a multiplos de 0.5 para acercar a zonas reales (India 5.5, etc).
  return Math.round(raw * 2) / 2;
}

/**
 * Parsea "YYYY-MM-DD" + "HH:MM" en componentes numericos.
 * Devuelve null si el formato es invalido.
 */
function parsearFechaHora(
  fecha: string,
  hora: string,
): {
  year: number;
  month: number;
  date: number;
  hours: number;
  minutes: number;
} | null {
  const mFecha = /^(\d{4})-(\d{2})-(\d{2})$/.exec(fecha);
  const mHora = /^(\d{1,2}):(\d{2})$/.exec(hora);
  if (!mFecha || !mHora) return null;
  const year = parseInt(mFecha[1], 10);
  const month = parseInt(mFecha[2], 10);
  const date = parseInt(mFecha[3], 10);
  const hours = parseInt(mHora[1], 10);
  const minutes = parseInt(mHora[2], 10);
  if (
    !Number.isFinite(year) ||
    !Number.isFinite(month) ||
    !Number.isFinite(date) ||
    !Number.isFinite(hours) ||
    !Number.isFinite(minutes) ||
    month < 1 || month > 12 ||
    date < 1 || date > 31 ||
    hours < 0 || hours > 23 ||
    minutes < 0 || minutes > 59
  ) {
    return null;
  }
  return { year, month, date, hours, minutes };
}

/**
 * Determina en que casa esta un grado absoluto del zodiaco (0-360), dadas
 * las cuspides de las 12 casas (en grados absolutos, en orden).
 */
function casaParaGrado(
  gradoAbs: number,
  cuspides: number[],
): number {
  // Normalizamos grados a [0, 360)
  const g = ((gradoAbs % 360) + 360) % 360;
  for (let i = 0; i < 12; i++) {
    const inicio = ((cuspides[i] % 360) + 360) % 360;
    const fin = ((cuspides[(i + 1) % 12] % 360) + 360) % 360;
    // El sector puede cruzar 0 grados.
    if (inicio <= fin) {
      if (g >= inicio && g < fin) return i + 1;
    } else {
      if (g >= inicio || g < fin) return i + 1;
    }
  }
  return 1;
}

// ---------------------------------------------------------------------------
// 1) Geocoding: lugar -> lat/lon via Nominatim
// ---------------------------------------------------------------------------

/**
 * Convierte un nombre de lugar (ej. "Santiago, Chile") en lat/lon usando
 * OpenStreetMap Nominatim. Nominatim exige User-Agent identificable.
 * Rate limit free: ~1 req/seg.
 */
export async function geocodificarLugar(
  lugar: string,
): Promise<GeocodingResult | null> {
  if (!lugar || !lugar.trim()) return null;
  const url = `${NOMINATIM_URL}?q=${encodeURIComponent(lugar)}&format=json&limit=1`;
  const res = await fetchConTimeout(url, {
    headers: {
      "User-Agent": "Pax-Oraculo/1.0 (pax-os.vercel.app)",
      Accept: "application/json",
    },
    cache: "no-store",
  });
  if (!res) return null;
  try {
    const data = await res.json();
    if (!Array.isArray(data) || data.length === 0) return null;
    const first = data[0];
    const lat = parseFloat(first.lat);
    const lon = parseFloat(first.lon);
    if (!Number.isFinite(lat) || !Number.isFinite(lon)) return null;
    return {
      lat,
      lon,
      displayName: String(first.display_name ?? lugar),
      // Nominatim no entrega timezone directamente; el caller puede derivarlo
      // o lo hace internamente calcularCartaAstral.
      timezone: undefined,
    };
  } catch (err) {
    console.warn("[astrology] parse Nominatim fallo:", (err as Error).message);
    return null;
  }
}

// ---------------------------------------------------------------------------
// 2) Carta astral: free-astrology-api (western, tropical)
// ---------------------------------------------------------------------------

interface AstroPlanetOut {
  planet?: { en?: string };
  fullDegree?: number;
  normDegree?: number;
  isRetro?: string | boolean;
  zodiac_sign?: { number?: number; name?: { en?: string } };
}

interface AstroHouseOut {
  House?: number;
  degree?: number;
  normDegree?: number;
  zodiac_sign?: { number?: number; name?: { en?: string } };
}

/**
 * Llama al endpoint western/planets de free-astrology-api.
 * Devuelve el array de planetas crudo o null si falla.
 */
async function fetchPlanetas(
  body: Record<string, unknown>,
  apiKey: string,
): Promise<AstroPlanetOut[] | null> {
  const res = await fetchConTimeout(ASTRO_PLANETS_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": apiKey,
    },
    body: JSON.stringify(body),
    cache: "no-store",
  });
  if (!res) return null;
  try {
    const json = await res.json();
    const output = json?.output;
    if (!Array.isArray(output)) return null;
    return output as AstroPlanetOut[];
  } catch (err) {
    console.warn("[astrology] parse planetas fallo:", (err as Error).message);
    return null;
  }
}

/**
 * Llama al endpoint western/houses de free-astrology-api.
 * Devuelve el array de casas crudo o null si falla.
 */
async function fetchCasas(
  body: Record<string, unknown>,
  apiKey: string,
): Promise<AstroHouseOut[] | null> {
  const res = await fetchConTimeout(ASTRO_HOUSES_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": apiKey,
    },
    body: JSON.stringify(body),
    cache: "no-store",
  });
  if (!res) return null;
  try {
    const json = await res.json();
    const houses = json?.output?.Houses;
    if (!Array.isArray(houses)) return null;
    return houses as AstroHouseOut[];
  } catch (err) {
    console.warn("[astrology] parse casas fallo:", (err as Error).message);
    return null;
  }
}

/**
 * Encuentra un planeta por nombre (case-insensitive) en el array crudo.
 */
function buscarPlaneta(
  planetas: AstroPlanetOut[],
  nombre: string,
): AstroPlanetOut | null {
  const n = nombre.toLowerCase();
  for (const p of planetas) {
    const en = (p.planet?.en ?? "").toLowerCase();
    if (en === n) return p;
  }
  return null;
}

/**
 * Calcula casas dominantes: las 3 casas con mas planetas (Sol..Pluto).
 * Si no hay datos suficientes devuelve undefined.
 */
function calcularCasasDominantes(
  planetas: AstroPlanetOut[],
  cuspides: number[],
): number[] | undefined {
  const planetasContados = [
    "Sun", "Moon", "Mercury", "Venus", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto",
  ];
  const conteo: Record<number, number> = {};
  for (const nombre of planetasContados) {
    const p = buscarPlaneta(planetas, nombre);
    if (!p || typeof p.fullDegree !== "number") continue;
    const casa = casaParaGrado(p.fullDegree, cuspides);
    conteo[casa] = (conteo[casa] ?? 0) + 1;
  }
  const entradas = Object.entries(conteo)
    .map(([k, v]) => ({ casa: Number(k), n: v }))
    .sort((a, b) => b.n - a.n);
  if (entradas.length === 0) return undefined;
  return entradas.slice(0, 3).map((e) => e.casa);
}

/**
 * Detecta el aspecto mas tenso (oposicion ~180 o cuadratura ~90) entre los
 * planetas personales y los transpersonales. Devuelve descripcion en espanol.
 */
function detectarAspectoPrincipal(
  planetas: AstroPlanetOut[],
): string | undefined {
  const nombres = [
    "Sun", "Moon", "Mercury", "Venus", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto",
  ];
  const nombresEs: Record<string, string> = {
    Sun: "Sol", Moon: "Luna", Mercury: "Mercurio", Venus: "Venus",
    Mars: "Marte", Jupiter: "Júpiter", Saturn: "Saturno",
    Uranus: "Urano", Neptune: "Neptuno", Pluto: "Plutón",
  };
  const posiciones: Array<{ nombre: string; grado: number }> = [];
  for (const n of nombres) {
    const p = buscarPlaneta(planetas, n);
    if (p && typeof p.fullDegree === "number") {
      posiciones.push({ nombre: n, grado: p.fullDegree });
    }
  }
  let mejor: { tipo: string; a: string; b: string; delta: number } | null = null;
  const ORB = 6; // orbe permitido en grados
  for (let i = 0; i < posiciones.length; i++) {
    for (let j = i + 1; j < posiciones.length; j++) {
      let diff = Math.abs(posiciones[i].grado - posiciones[j].grado);
      diff = diff > 180 ? 360 - diff : diff;
      // oposicion 180, cuadratura 90
      const dOpos = Math.abs(diff - 180);
      const dCuad = Math.abs(diff - 90);
      const candidato = dOpos < dCuad
        ? { tipo: "oposición", delta: dOpos }
        : { tipo: "cuadratura", delta: dCuad };
      if (candidato.delta > ORB) continue;
      if (!mejor || candidato.delta < mejor.delta) {
        mejor = {
          tipo: candidato.tipo,
          a: posiciones[i].nombre,
          b: posiciones[j].nombre,
          delta: candidato.delta,
        };
      }
    }
  }
  if (!mejor) return undefined;
  return `${nombresEs[mejor.a] ?? mejor.a} en ${mejor.tipo} con ${nombresEs[mejor.b] ?? mejor.b}`;
}

// ---------------------------------------------------------------------------
// 3) API publica: calcularCartaAstral
// ---------------------------------------------------------------------------

export async function calcularCartaAstral(input: {
  fecha: string; // "YYYY-MM-DD"
  hora: string;  // "HH:MM" (24h)
  lugar: string; // input del usuario, lo geocodificamos internamente
}): Promise<AstralResult | null> {
  const apiKey = process.env.FREE_ASTROLOGY_API_KEY;
  if (!apiKey) {
    console.warn(
      "[astrology] FREE_ASTROLOGY_API_KEY no esta seteada; devolviendo null",
    );
    return null;
  }

  const dt = parsearFechaHora(input.fecha, input.hora);
  if (!dt) {
    console.warn("[astrology] fecha/hora invalidas:", input.fecha, input.hora);
    return null;
  }

  const geo = await geocodificarLugar(input.lugar);
  if (!geo) return null;

  const timezone = geo.timezone !== undefined
    ? Number(geo.timezone)
    : timezoneDesdeLongitud(geo.lon);

  const body: Record<string, unknown> = {
    year: dt.year,
    month: dt.month,
    date: dt.date,
    hours: dt.hours,
    minutes: dt.minutes,
    seconds: 0,
    latitude: geo.lat,
    longitude: geo.lon,
    timezone,
    config: {
      observation_point: "topocentric",
      ayanamsha: "tropical",
      language: "en",
    },
  };

  const bodyCasas: Record<string, unknown> = {
    ...body,
    config: {
      observation_point: "topocentric",
      ayanamsha: "tropical",
      house_system: "Placidus",
      language: "en",
    },
  };

  // Ejecutamos planetas + casas en paralelo
  const [planetas, casas] = await Promise.all([
    fetchPlanetas(body, apiKey),
    fetchCasas(bodyCasas, apiKey),
  ]);

  if (!planetas || !casas || casas.length < 12) return null;

  const sol = buscarPlaneta(planetas, "Sun");
  const luna = buscarPlaneta(planetas, "Moon");
  // El ascendente viene como "planet" en el endpoint planets o como casa 1.
  const ascendentePlanet = buscarPlaneta(planetas, "Ascendant");

  if (!sol || !luna) return null;

  // Cuspides absolutas en orden de casa 1..12
  const cuspidesOrdenadas = [...casas]
    .sort((a, b) => (a.House ?? 0) - (b.House ?? 0));
  const cuspidesGrados = cuspidesOrdenadas.map((h) => h.degree ?? 0);
  if (cuspidesGrados.length !== 12) return null;

  // Helper para mapear un planeta crudo al shape publico
  const planetaPublico = (p: AstroPlanetOut) => {
    const signoEn = p.zodiac_sign?.name?.en ?? "";
    const signo = SIGNO_ES[signoEn] ?? signoEn;
    const grado = typeof p.normDegree === "number" ? p.normDegree : 0;
    const fullDeg = typeof p.fullDegree === "number" ? p.fullDegree : 0;
    const casa = casaParaGrado(fullDeg, cuspidesGrados);
    return { signo, signo_en: signoEn, grado, casa };
  };

  const solPub = planetaPublico(sol);
  const lunaPub = planetaPublico(luna);

  // Ascendente: preferimos el "planet" Ascendant; si no, la casa 1.
  let ascSignoEn = "";
  let ascGrado = 0;
  if (ascendentePlanet) {
    ascSignoEn = ascendentePlanet.zodiac_sign?.name?.en ?? "";
    ascGrado = typeof ascendentePlanet.normDegree === "number"
      ? ascendentePlanet.normDegree
      : 0;
  } else {
    const casa1 = cuspidesOrdenadas[0];
    ascSignoEn = casa1?.zodiac_sign?.name?.en ?? "";
    ascGrado = typeof casa1?.normDegree === "number" ? casa1.normDegree : 0;
  }
  const ascSigno = SIGNO_ES[ascSignoEn] ?? ascSignoEn;

  const result: AstralResult = {
    sol: solPub,
    luna: lunaPub,
    ascendente: {
      signo: ascSigno,
      signo_en: ascSignoEn,
      grado: ascGrado,
    },
    casas_dominantes: calcularCasasDominantes(planetas, cuspidesGrados),
    aspecto_principal: detectarAspectoPrincipal(planetas),
  };

  // Validacion final: signos no vacios
  if (!result.sol.signo_en || !result.luna.signo_en || !result.ascendente.signo_en) {
    return null;
  }

  return result;
}
