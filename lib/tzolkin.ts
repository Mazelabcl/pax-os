/**
 * Tzolkin — calculo determinista del calendario sagrado maya (kin/nahual/tono).
 *
 * El Tzolkin combina 20 nahuales (sellos) x 13 tonos (numeros) = 260 dias.
 * Cada fecha gregoriana mapea a un kin unico entre 1 y 260.
 *
 * Formula:
 *   1. Fecha gregoriana -> Julian Day Number (JDN) via Fliegel-Van Flandern.
 *   2. kin = ((JDN - 584283) mod 260) + 1.
 *   3. nahual_idx = (kin - 1) mod 20.
 *   4. tono_idx = (kin - 1) mod 13.
 *
 * Correlacion GMT 584283 (Goodman-Martinez-Thompson, Thompson 1935) — estandar
 * usado por la mayoria de academicos mesoamericanistas.
 *
 * Mapeo nahual -> arquetipo Pax: tabla determinista (7 arquetipos del Oraculo).
 */

// ============================================================================
// TIPOS PUBLICOS
// ============================================================================

export type ArquetipoPaxNombre =
  | "Sanador Intenso"
  | "Companero Sereno"
  | "Mistico Vidente"
  | "Mentor del Clan"
  | "Cuidador del Hogar"
  | "Guerrero Altruista"
  | "Sabio del Tiempo";

export interface NahualInfo {
  idx: number; // 0-19
  nombre: string;
  glyph: string;
  descripcion: string;
}

export interface TonoInfo {
  idx: number; // 0-12
  numero: number; // 1-13
  nombre: string;
  descripcion: string;
}

export interface ArquetipoPax {
  nombre: ArquetipoPaxNombre;
  descripcion: string;
  color_hex: string;
}

export interface TzolkinResult {
  kin: number; // 1-260
  nahual: NahualInfo;
  tono: TonoInfo;
  arquetipo_pax: ArquetipoPax;
}

// ============================================================================
// LOOKUP: 20 NAHUALES
// ============================================================================

// Orden tradicional del Tzolkin (idx 0..19).
// Fuentes: Tedlock "Time and the Highland Maya", Jenkins "Maya Cosmogenesis",
// Aveni "Skywatchers". Glyphs: simbolos representativos (no son los glifos
// epigraficos exactos sino emojis Unicode que evocan al sello).
const NAHUALES: readonly NahualInfo[] = [
  {
    idx: 0,
    nombre: "Imix",
    glyph: "\u{1F40A}", // cocodrilo
    descripcion:
      "Cocodrilo primigenio. Representa el origen, el mundo primordial y el alimento que sostiene la vida. Energia de hogar, proteccion y arranque de los ciclos.",
  },
  {
    idx: 1,
    nombre: "Ik'",
    glyph: "\u{1F343}", // hoja al viento
    descripcion:
      "Viento y espiritu. Es el aliento que da vida y la palabra que comunica. Energia de inspiracion, mensajes y movimiento sutil entre mundos.",
  },
  {
    idx: 2,
    nombre: "Ak'bal",
    glyph: "\u{1F319}", // luna creciente / noche
    descripcion:
      "Noche y oscuridad fertil. Guarda los suenos, la intuicion y la sabiduria oculta. Energia de introspeccion y misterio interior.",
  },
  {
    idx: 3,
    nombre: "K'an",
    glyph: "\u{1F33D}", // mazorca de maiz
    descripcion:
      "Semilla y maiz. Es el potencial latente y la fertilidad del germen. Energia de maduracion, abundancia futura y promesa de crecimiento.",
  },
  {
    idx: 4,
    nombre: "Chikchan",
    glyph: "\u{1F40D}", // serpiente
    descripcion:
      "Serpiente y fuerza vital. Encarna la energia kundalini, lo sexual y lo instintivo. Energia de transformacion intensa y poder corporal.",
  },
  {
    idx: 5,
    nombre: "Kimi",
    glyph: "\u{1F480}", // calavera
    descripcion:
      "Muerte y transmutacion. No es final sino umbral: cierra ciclos para abrir otros. Energia de renacimiento y transicion respetuosa.",
  },
  {
    idx: 6,
    nombre: "Manik'",
    glyph: "\u{270B}", // mano abierta
    descripcion:
      "Mano sanadora. Es la que toma, da y restaura. Energia de servicio, de oficio paciente y de gestion del cuidado hacia otros.",
  },
  {
    idx: 7,
    nombre: "Lamat",
    glyph: "\u{2B50}", // estrella
    descripcion:
      "Estrella y conejo. Trae armonia, fertilidad y abundancia ludica. Energia de arte, belleza y alegria que multiplica.",
  },
  {
    idx: 8,
    nombre: "Muluk",
    glyph: "\u{1F4A7}", // gota de agua
    descripcion:
      "Agua y luna. Es la ofrenda y la purificacion emocional. Energia de sensibilidad, devocion y limpieza de lo acumulado.",
  },
  {
    idx: 9,
    nombre: "Ok",
    glyph: "\u{1F415}", // perro
    descripcion:
      "Perro guia. Encarna la lealtad y el amor incondicional. Energia de companero fiel, de guia en el camino y de afecto que sostiene.",
  },
  {
    idx: 10,
    nombre: "Chuwen",
    glyph: "\u{1F412}", // mono
    descripcion:
      "Mono artista. Es el juego, la creatividad y la imitacion sagrada. Energia de arte, humor y combinatoria libre de formas.",
  },
  {
    idx: 11,
    nombre: "Eb",
    glyph: "\u{1F6B6}", // persona caminando
    descripcion:
      "Camino y humano. Es la escalera del destino y el libre albedrio que lo recorre. Energia de eleccion consciente y vocacion de servicio.",
  },
  {
    idx: 12,
    nombre: "Ben",
    glyph: "\u{1F33E}", // cana / mazorca verde
    descripcion:
      "Cana y maiz tierno. Es el pilar del hogar, la autoridad amorosa y el cuidado de los ninos. Energia de estructura que protege a los suyos.",
  },
  {
    idx: 13,
    nombre: "Ix",
    glyph: "\u{1F406}", // jaguar
    descripcion:
      "Jaguar magico. Camina entre el mundo visible y el invisible. Energia de chamanismo, sensibilidad sagrada y poder sigiloso.",
  },
  {
    idx: 14,
    nombre: "Men",
    glyph: "\u{1F985}", // aguila
    descripcion:
      "Aguila visionaria. Mira desde lo alto y abarca el conjunto. Energia de claridad mental, ambicion noble y vision global.",
  },
  {
    idx: 15,
    nombre: "Kib",
    glyph: "\u{1F56F}", // vela
    descripcion:
      "Guerrero sabio. Porta la conciencia ancestral y el perdon. Energia de introspeccion guerrera y de luz que disuelve cargas heredadas.",
  },
  {
    idx: 16,
    nombre: "Kaban",
    glyph: "\u{1F30D}", // tierra
    descripcion:
      "Tierra en movimiento. Es la sincronizacion con los ciclos del planeta. Energia de evolucion consciente y fuerza terrestre que organiza.",
  },
  {
    idx: 17,
    nombre: "Etznab",
    glyph: "\u{1FA9E}", // espejo
    descripcion:
      "Espejo de obsidiana. Refleja la verdad sin adornos. Energia de claridad, integridad y discernimiento que corta lo falso.",
  },
  {
    idx: 18,
    nombre: "Kawak",
    glyph: "\u{26C8}", // tormenta
    descripcion:
      "Tormenta y truenos. Es el llamado catalizador al cambio. Energia de purificacion intensa, ruptura necesaria y renovacion electrica.",
  },
  {
    idx: 19,
    nombre: "Ahau",
    glyph: "\u{2600}", // sol
    descripcion:
      "Sol y florescencia. Es la iluminacion del proposito cumplido. Energia de maestria, plenitud y entrega luminosa al mundo.",
  },
];

// ============================================================================
// LOOKUP: 13 TONOS
// ============================================================================

// Idx 0..12, numero 1..13. Nombres y atributos segun la tradicion del
// "Encantamiento del Sueno" (Jose Arguelles) — convencion mas difundida hoy.
const TONOS: readonly TonoInfo[] = [
  {
    idx: 0,
    numero: 1,
    nombre: "Magnetico",
    descripcion: "Atrae y unifica el proposito. Inicia el ciclo concentrando intencion.",
  },
  {
    idx: 1,
    numero: 2,
    nombre: "Lunar",
    descripcion: "Polariza y estabiliza desafiando. Saca a la luz el reto a integrar.",
  },
  {
    idx: 2,
    numero: 3,
    nombre: "Electrico",
    descripcion: "Activa el servicio y enciende la accion. Energiza el movimiento hacia afuera.",
  },
  {
    idx: 3,
    numero: 4,
    nombre: "Auto-existente",
    descripcion: "Define la forma. Da estructura concreta a lo que aun era idea.",
  },
  {
    idx: 4,
    numero: 5,
    nombre: "Entonado",
    descripcion: "Comanda con empoderamiento. Centra la voz interna y la afina al proposito.",
  },
  {
    idx: 5,
    numero: 6,
    nombre: "Ritmico",
    descripcion: "Organiza el equilibrio. Coordina lo cotidiano con el ritmo del ciclo.",
  },
  {
    idx: 6,
    numero: 7,
    nombre: "Resonante",
    descripcion: "Sintoniza con el conjunto. Inspira y se deja inspirar por lo que vibra alrededor.",
  },
  {
    idx: 7,
    numero: 8,
    nombre: "Galactico",
    descripcion: "Armoniza con la integridad. Pone en coherencia el actuar con la verdad propia.",
  },
  {
    idx: 8,
    numero: 9,
    nombre: "Solar",
    descripcion: "Pulsa la intencion realizada. Es el latido firme que ya muestra resultados.",
  },
  {
    idx: 9,
    numero: 10,
    nombre: "Planetario",
    descripcion: "Manifiesta la perfeccion del ciclo. Concreta en el mundo lo que se gesto.",
  },
  {
    idx: 10,
    numero: 11,
    nombre: "Espectral",
    descripcion: "Disuelve y libera. Suelta lo que ya cumplio su funcion para dejar espacio.",
  },
  {
    idx: 11,
    numero: 12,
    nombre: "Cristal",
    descripcion: "Coopera con dedicacion. Comparte y se entrega al trabajo colectivo.",
  },
  {
    idx: 12,
    numero: 13,
    nombre: "Cosmico",
    descripcion: "Trasciende con presencia. Cierra el ciclo elevando la experiencia a lo universal.",
  },
];

// ============================================================================
// LOOKUP: NAHUAL -> ARQUETIPO PAX
// ============================================================================

// Mapeo determinista de los 20 nahuales hacia los 7 arquetipos del Oraculo Pax.
// Tabla validada por el orquestador.
const ARQUETIPOS_PAX: Record<ArquetipoPaxNombre, ArquetipoPax> = {
  "Sanador Intenso": {
    nombre: "Sanador Intenso",
    descripcion:
      "Camina entre lo visible y lo invisible para devolver el equilibrio. En Pax es quien sostiene al herido y atraviesa la sombra sin perderse, dejando como rastro un cristal-eco violeta.",
    color_hex: "#B43FFF",
  },
  "Companero Sereno": {
    nombre: "Companero Sereno",
    descripcion:
      "Trae armonia, juego y ternura al clan. En Pax es la presencia que recuerda que la vida tambien se celebra, suavizando con su luz rosada los dias mas duros.",
    color_hex: "#FFB3C7",
  },
  "Cuidador del Hogar": {
    nombre: "Cuidador del Hogar",
    descripcion:
      "Sostiene la casa, la cocina, los ninos y el ciclo cotidiano. En Pax es pilar del clan que asegura que haya semilla, fuego y techo, irradiando un verde jade firme.",
    color_hex: "#3DCCA3",
  },
  "Mistico Vidente": {
    nombre: "Mistico Vidente",
    descripcion:
      "Ve mas alla del horizonte inmediato y trae visiones al consejo. En Pax es voz que orienta cuando el clan duda, brillando con un dorado solar de claridad.",
    color_hex: "#FFD27A",
  },
  "Mentor del Clan": {
    nombre: "Mentor del Clan",
    descripcion:
      "Ensena, guia y transmite el oficio ancestral. En Pax es quien toma de la mano a la nueva generacion y le pasa la memoria del pueblo en un eco turquesa.",
    color_hex: "#5FE8E3",
  },
  "Guerrero Altruista": {
    nombre: "Guerrero Altruista",
    descripcion:
      "Toma la fuerza vital y la pone al servicio del clan en los momentos de crisis. En Pax es el cuerpo que se interpone por los suyos, ardiendo en un rojo magmatico.",
    color_hex: "#D43A1F",
  },
  "Sabio del Tiempo": {
    nombre: "Sabio del Tiempo",
    descripcion:
      "Sabe leer los ciclos, las muertes y los renaceres. En Pax es voz que recuerda que todo pasa y todo retorna, dejando un resplandor purpura profundo.",
    color_hex: "#9B30E8",
  },
};

// Tabla deterministica idx_nahual -> ArquetipoPaxNombre.
// Indices se corresponden con NAHUALES[i].nombre:
//   0 Imix, 1 Ik', 2 Ak'bal, 3 K'an, 4 Chikchan, 5 Kimi, 6 Manik', 7 Lamat,
//   8 Muluk, 9 Ok, 10 Chuwen, 11 Eb, 12 Ben, 13 Ix, 14 Men, 15 Kib, 16 Kaban,
//   17 Etznab, 18 Kawak, 19 Ahau
const NAHUAL_A_ARQUETIPO: readonly ArquetipoPaxNombre[] = [
  "Cuidador del Hogar", // 0 Imix
  "Sabio del Tiempo", // 1 Ik'
  "Sanador Intenso", // 2 Ak'bal
  "Cuidador del Hogar", // 3 K'an
  "Guerrero Altruista", // 4 Chikchan
  "Sabio del Tiempo", // 5 Kimi
  "Mentor del Clan", // 6 Manik'
  "Companero Sereno", // 7 Lamat
  "Companero Sereno", // 8 Muluk
  "Sanador Intenso", // 9 Ok
  "Companero Sereno", // 10 Chuwen
  "Mentor del Clan", // 11 Eb
  "Cuidador del Hogar", // 12 Ben
  "Sanador Intenso", // 13 Ix
  "Mistico Vidente", // 14 Men
  "Mentor del Clan", // 15 Kib
  "Guerrero Altruista", // 16 Kaban
  "Mistico Vidente", // 17 Etznab
  "Guerrero Altruista", // 18 Kawak
  "Mistico Vidente", // 19 Ahau
];

// ============================================================================
// CALCULO
// ============================================================================

/**
 * Convierte una fecha gregoriana (year/month/day) a Julian Day Number.
 * Algoritmo de Fliegel-Van Flandern (1968), valido para todo el rango
 * gregoriano usable en la web (>= 1583 sobra).
 */
function gregorianToJDN(year: number, month: number, day: number): number {
  const a = Math.floor((14 - month) / 12);
  const y = year + 4800 - a;
  const m = month + 12 * a - 3;
  return (
    day +
    Math.floor((153 * m + 2) / 5) +
    365 * y +
    Math.floor(y / 4) -
    Math.floor(y / 100) +
    Math.floor(y / 400) -
    32045
  );
}

// Correlacion GMT (Goodman-Martinez-Thompson). JDN del kin 1 de la Cuenta Larga.
const CORRELACION_GMT = 584283;

/**
 * Calcula el resultado Tzolkin para una fecha gregoriana dada.
 * Pure function. Sin dependencias externas, sin side effects.
 *
 * Usa la fecha en hora local (getFullYear/getMonth/getDate) para evitar
 * desfases por UTC cuando el consumidor pasa un Date construido con
 * `new Date(2026, 4, 21)`.
 */
export function calcularTzolkin(fecha: Date): TzolkinResult {
  const year = fecha.getFullYear();
  const month = fecha.getMonth() + 1; // getMonth() es 0-indexado
  const day = fecha.getDate();

  const jdn = gregorianToJDN(year, month, day);

  // ((x mod n) + n) mod n para garantizar resultado no negativo aunque
  // el operador % de JS pueda devolver negativos con dividendos negativos.
  const kin = (((jdn - CORRELACION_GMT) % 260) + 260) % 260 + 1; // 1..260

  const nahualIdx = (kin - 1) % 20;
  const tonoIdx = (kin - 1) % 13;

  const nahual = NAHUALES[nahualIdx];
  const tono = TONOS[tonoIdx];
  const arquetipoNombre = NAHUAL_A_ARQUETIPO[nahualIdx];
  const arquetipo_pax = ARQUETIPOS_PAX[arquetipoNombre];

  return {
    kin,
    nahual,
    tono,
    arquetipo_pax,
  };
}

// ============================================================================
// TESTS INLINE (opcionales, ejecutables con `npx tsx lib/tzolkin.ts`)
// ============================================================================

// Solo correr cuando este archivo se invoca directamente como script.
// `require` no esta tipado en modo ESM estricto pero existe en runtime tsx.
declare const require: { main?: unknown } | undefined;
declare const module: { exports?: unknown } | undefined;

if (
  typeof require !== "undefined" &&
  typeof module !== "undefined" &&
  (require as { main?: unknown }).main === module
) {
  const fechas: Array<[string, Date]> = [
    ["2026-05-21 (hoy)", new Date(2026, 4, 21)],
    ["1990-07-15", new Date(1990, 6, 15)],
    ["2000-01-01", new Date(2000, 0, 1)],
  ];

  for (const [label, fecha] of fechas) {
    const r = calcularTzolkin(fecha);
    // eslint-disable-next-line no-console
    console.log(
      `${label} -> kin ${r.kin} | ${r.nahual.glyph} ${r.nahual.nombre} (${r.nahual.idx}) | tono ${r.tono.numero} ${r.tono.nombre} | arquetipo: ${r.arquetipo_pax.nombre} (${r.arquetipo_pax.color_hex})`,
    );
  }
}
