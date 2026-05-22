# Carta del Oraculo Pax — Spec de diseno del producto

> Documento de especificacion del **producto-carta**. NO incluye codigo frontend. El frontend dev usa este doc para implementar.
>
> Fecha: 2026-05-20
> Estado: spec v1 — entrada principal para el MVP del Oraculo Pax.

---

## 0. Resumen ejecutivo

La **Carta del Oraculo Pax** es un objeto digital coleccionable que se siente premium, ritual y unico-por-persona. Funciona como el output principal del Oraculo: el visitante entrega fecha + hora + lugar de nacimiento, y recibe una **carta personalizada** que combina lectura ancestral (signo solar occidental, nahual maya, numero del nombre, aspecto dominante) con la sabiduria Pax (arquetipo de servicio, accion RUKLA sugerida, cristal personal).

Tiene que sentirse como un objeto de coleccion (tarot premium + TCG holo + edicion limitada), pero estar 100% nativo al universo Pax (paleta canon, cristales, tipografia, simbolismo).

---

## Parte 1 — Investigacion comparativa

### A. Pokemon TCG (clasico holo foil)

Componentes universales que aparecen en cada carta:

1. **Frame por tipo elemental** — el color del borde codifica el tipo (fuego rojo, agua azul, planta verde). Lectura instantanea de categoria.
2. **HP/stat numerico arriba a la derecha** — atributo numerico dominante visible al primer golpe.
3. **Ilustracion central enmarcada** — ocupa ~45% del area, siempre en proporcion fija para mantener la consistencia de coleccion.
4. **Type icon y attack list** — bloque tecnico con simbolos y costos. La carta es jugable, no solo decorativa.
5. **Foil holografico parcial** — solo en la ilustracion o en el frame, NO toda la carta. Genera escasez visual.
6. **Rarity symbol** (circulo, diamante, estrella) — abajo-derecha, micro-element que comunica valor.
7. **Set + numero de carta** (ej. "042/198") — abajo en el frame, refuerza coleccionabilidad.

**Insight Pokemon:** la jerarquia visual es **tipo → nombre → ilustracion → stats**. Todo respeta una grilla estricta que se mantiene en miles de cartas distintas. La consistencia ES el premium feel.

### B. Magic the Gathering (premium foil + masterpieces)

1. **Frame anatomy con header + art window + type line + text box + footer** — 5 zonas horizontales rigurosamente alineadas.
2. **Mana cost en esquina superior derecha** — el costo de jugar la carta, simbolo+numero, siempre en el mismo lugar.
3. **Type line debajo de la ilustracion** — "Creature — Human Wizard" o similar. Es el "que es esta cosa" en una sola linea.
4. **Text box con flavor text en italica** — separa mecanica (top) de narrativa (bottom italica). El flavor text es el alma poetica.
5. **Power/Toughness en esquina inferior derecha** (en criaturas) — stats finales, lugar fijo.
6. **Foil treatment full-card en premium / masterpiece** — la masterpiece es full-bleed foil, sin frame "tecnico" clasico, mas pictorica.
7. **Artist credit + copyright + set symbol** — footer pequeno, refuerza autoria y edicion.

**Insight Magic:** la separacion **mecanica vs flavor** es lo que crea capas de lectura. La carta "funciona" en juego, pero **emociona** en el flavor text. Pax debe tener esa dualidad: lectura tecnica (atributos) + frase poetica.

### C. Tarot Rider-Waite (tradicional)

1. **Borde ornamental simetrico** — marco grueso decorativo, contiene la ilustracion como reliquia.
2. **Ilustracion central full-frame** — figura simbolica que ocupa ~70% del area, dominio visual absoluto.
3. **Titulo en mayusculas en la parte inferior** — "THE HIGH PRIESTESS", siempre el mismo lugar.
4. **Numero romano en la parte superior** — "II", "VII", "XIII" — jerarquiza la carta dentro del mazo.
5. **Simbolismo embebido en la ilustracion** — cada elemento (columnas, luna, granadas) significa algo. Lectura por capas.
6. **Paleta restringida** — colores planos limitados (azul, amarillo, rojo, blanco) que codifican lecturas (azul=intuicion, amarillo=sol).
7. **Sin foil ni efectos modernos** — el premium feel viene del **rito** de la carta fisica, no del efecto visual.

**Insight Tarot:** la **simetria + el numero romano + el titulo + la ilustracion central simbolica** son lo que hace que la carta se sienta "destino", no "estadistica". Pax debe heredar este sentimiento de fatum.

### D. Otros sistemas modernos (Dixit, Mystic Vale, KeyForge, Sorcery Contested Realm)

1. **Dixit:** ilustraciones full-bleed sin texto. La ilustracion es la carta. Lo evocador es el producto.
2. **Mystic Vale:** cartas con bandas transparentes apilables. Innovacion fisica que solo aplica a fisico.
3. **KeyForge:** cada carta tiene un **identificador unico de mazo** ("House Brobnar / Set Age of Ascension / Card 042/350"). Coleccionabilidad por unicidad del set entero.
4. **Sorcery Contested Realm:** frame con **fondo translucido degradado** en lugar de bloque opaco — moderno, etereo.
5. **Lorcana:** ilustraciones tipo cinema still (no concept art). La carta se siente como un frame de pelicula.
6. **Marvel Champions:** atributos en circulos contadores grandes y legibles a 1m. UX a distancia.
7. **Tendencia moderna comun:** menos frame "tecnico", mas full-bleed; tipografia mas elegante (serif fina o sans grotesca contemporanea); menor saturacion, mas atmosfera; **edition number visible y unico**.

**Insight modernos:** la frontera entre "carta jugable" y "objeto-arte" se borro. Las cartas mas premium 2020-2026 parecen carteles de cine miniatura.

---

## Parte 2 — Anatomia de la Carta Oraculo Pax

### 2.1 — Identidad de la carta

- **Producto:** Carta del Oraculo Pax, unica por persona, generada al momento.
- **Ratio canon:** vertical 2.5 : 3.5 (estilo tarot). Equivalente a 750 × 1050 px en mobile, 900 × 1260 px en desktop.
- **Estilo dominante Pax:** 3D PBR neon-magico (segun pax-core). Paleta canon obligatoria.
- **Paleta de la carta (todas las variantes):**
  - Violeta dominante `#B43FFF`
  - Jade acento `#3DCCA3`
  - Amber luz `#F59E0B`
  - Basalt fondo `#1E1E2E`
  - Magenta destello `#EC4899`
  - Dorado borde premium `#D4A857`
  - Blanco texto `#F7F4EE`

### 2.2 — Componentes de la carta (anatomia maestra)

> Esta es la anatomia base. Cada layout (Parte 3) reordena estos componentes pero **todos deben estar presentes**.

#### Componente 1 — Frame ornamental (borde decorativo)

- **Info que lleva:** marco visual que contiene toda la carta. Patron de simbolos Pax (cristales miniatura, ondas de energia, espirales mayas estilizadas).
- **Tamano:** 5-8% del area total (borde de ~30-50 px en 750 de ancho).
- **Tipografia:** N/A (es ilustracion).
- **Color:** dorado `#D4A857` sobre violeta `#B43FFF` con halo jade `#3DCCA3` interior.
- **Interactivo:** estatico, pero con micro-shimmer al hover (animacion CSS sutil).

#### Componente 2 — Title (nombre de la lectura)

- **Info que lleva:** titulo poetico del arquetipo. Ej. *"EL CAMINO DEL SANADOR INTENSO"* o *"LA CRISTAL DE LA OBSERVADORA"*. Generado a partir de la combinacion arquetipo + aspecto dominante.
- **Tamano:** 8-10% del area total. Headline.
- **Tipografia:** serif display elegante, peso semibold, tracking +50, mayusculas. Sugerencia: **Cinzel**, **Cormorant Garamond Display**, **Spectral**. Fallback: Georgia.
- **Color:** dorado `#D4A857` con sombra violeta `#B43FFF` 20% opacity.
- **Interactivo:** estatico.

#### Componente 3 — Foil/holo digital

- **Info que lleva:** efecto visual de profundidad. NO es informacion textual, es **textura premium**.
- **Tamano:** afecta el 100% del area, pero solo es visible en interaccion.
- **Tipografia:** N/A.
- **Color:** gradient animado violeta `#B43FFF` → magenta `#EC4899` → jade `#3DCCA3` → amber `#F59E0B`, con angulo que sigue el cursor (efecto CSS `conic-gradient` + `transform: rotateX/Y` al `mousemove`).
- **Interactivo:** SI — al hover/touchmove la carta se inclina suavemente (8-12 grados max) y el gradient se desplaza. En mobile, responde al giroscopio si esta disponible. **Es el alma de "premium-coleccionable".**

#### Componente 4 — Ilustracion central (cristal personal)

- **Info que lleva:** render generado del cristal personal del visitante. Forma + color codifica el arquetipo. Ej. cristal hexagonal violeta intenso para Healer-Intenso, cristal octaedrico jade para Observador-Sereno.
- **Tamano:** 35-50% del area total segun layout (el "heart" visual).
- **Tipografia:** N/A.
- **Color:** color cristal dominante (ver componente 9) sobre fondo basalt `#1E1E2E` con halo magenta-violeta.
- **Interactivo:** rota lentamente en idle (3D suave, 1 vuelta cada 12s) y acelera ligeramente al hover.
- **Fuente del render:** en MVP usar 1 de N (8-12) cristales pre-generados via GPT Image 2, asignados por arquetipo. En v2, render procedural en tiempo real.

#### Componente 5 — Arquetipo principal (etiqueta de servicio)

- **Info que lleva:** una de las ~8-12 categorias de arquetipo de servicio Pax. Ej. *"HEALER · Intensidad orientada al cuidado"*, *"WEAVER · Tejedora de comunidad"*, *"WATCHER · Observador que sostiene"*.
- **Tamano:** 4-6% del area.
- **Tipografia:** sans grotesca moderna, peso bold, tracking +100, mayusculas en la primera palabra. Sugerencia: **Inter**, **Geist**, **Manrope**.
- **Color:** jade `#3DCCA3` para la primera palabra, blanco `#F7F4EE` para el subtitulo.
- **Interactivo:** estatico.

#### Componente 6 — Sub-atributos (lectura ancestral)

- **Info que lleva:** 4 micro-bloques con la lectura tecnica:
  - **Signo solar occidental** (ej. "Escorpio")
  - **Nahual maya** (ej. "Kawak / Tormenta")
  - **Numero del nombre** (1-9, suma reducida)
  - **Aspecto dominante** (ej. "Agua / profundidad")
- **Tamano:** 8-10% del area, grid 2×2 o linea horizontal.
- **Tipografia:** sans grotesca, peso regular, micro-size (12-14 px), tracking +30.
- **Color:** blanco `#F7F4EE` 70% opacity, etiqueta en amber `#F59E0B`.
- **Interactivo:** estatico. Tooltip opcional al hover de cada atributo con explicacion breve.

#### Componente 7 — Mensaje principal (mensaje poetico)

- **Info que lleva:** 2-3 lineas profundas, el "corazon" de la lectura. Generado combinando arquetipo + sub-atributos. Ej. *"Naciste para sostener lo que otros no pueden ver. Tu fuerza no se mide por lo que cargas, sino por la quietud con la que lo haces."*
- **Tamano:** 10-12% del area.
- **Tipografia:** serif elegante, italica, peso regular, tracking +10, leading 1.5. Sugerencia: **Cormorant Garamond**, **EB Garamond italic**, **Spectral italic**.
- **Color:** blanco `#F7F4EE` 95% opacity sobre fondo basalt.
- **Interactivo:** estatico. Selectable text (el visitante quiere copiar).

#### Componente 8 — Accion RUKLA sugerida

- **Info que lleva:** 1 linea con accion concreta de servicio. Ej. *"RUKLA: Esta semana, escucha a alguien sin intentar arreglar lo que dice."* Conecta con la mecanica Pax (el acto pequeno que enciende un cristal).
- **Tamano:** 5-7% del area.
- **Tipografia:** sans grotesca, peso medium, leading 1.4. La palabra "RUKLA" en bold + tracking +80.
- **Color:** amber `#F59E0B` para "RUKLA:", blanco `#F7F4EE` para la accion.
- **Interactivo:** estatico. Selectable.

#### Componente 9 — Color cristal (swatch + hex)

- **Info que lleva:** swatch de color (15-25 px circulo o cuadrado) + codigo hex. Es **el cristal que se enciende cuando esta persona hace su RUKLA**. Es ID visual unico de esa lectura.
- **Tamano:** 3-4% del area.
- **Tipografia:** monospace para el hex. Sugerencia: **JetBrains Mono**, **IBM Plex Mono**.
- **Color:** el color del cristal + texto hex en blanco 60% opacity.
- **Interactivo:** click copia el hex al clipboard (UX detail premium).

#### Componente 10 — Frase de cierre (sello poetico)

- **Info que lleva:** 1 linea de cierre etereo. Ej. *"Y asi, el cristal se enciende."* o *"Pax te recibe."* Repetible entre cartas (es la "marca" de cierre del oraculo).
- **Tamano:** 3-5% del area.
- **Tipografia:** serif italica, peso light, tracking +120, mayusculas.
- **Color:** dorado `#D4A857` 80% opacity.
- **Interactivo:** estatico.

#### Componente 11 — Edition / Serial (coleccionabilidad)

- **Info que lleva:** numero unico de carta. Formato: `PAX-2026-A1-0042` donde:
  - `PAX` = brand
  - `2026` = ano de emision
  - `A1` = serie/wave (A1 es la primera tirada del Oraculo MVP)
  - `0042` = numero secuencial unico
- **Tamano:** 2-3% del area.
- **Tipografia:** monospace, micro-size (10-11 px), tracking +60.
- **Color:** blanco `#F7F4EE` 40% opacity.
- **Interactivo:** estatico. Genera sensacion de "esta es la carta numero 42 emitida en la historia".

#### Componente 12 — Footer (firma del proyecto)

- **Info que lleva:** texto discreto `pax-os.vercel.app` + simbolo cristal mini.
- **Tamano:** 2-3% del area.
- **Tipografia:** sans grotesca, peso regular, micro-size.
- **Color:** blanco `#F7F4EE` 30% opacity.
- **Interactivo:** click va a la home del sitio.

### 2.3 — Resumen visual de la anatomia

| # | Componente | % area | Tipografia | Color principal | Interactivo |
|---|---|---|---|---|---|
| 1 | Frame ornamental | 5-8% | — | Dorado #D4A857 | Hover shimmer |
| 2 | Title | 8-10% | Serif display | Dorado #D4A857 | No |
| 3 | Foil/holo | 100% (overlay) | — | Gradient anim. | **SI hover/tilt** |
| 4 | Ilustracion cristal | 35-50% | — | Color cristal | Rotacion idle |
| 5 | Arquetipo | 4-6% | Sans bold | Jade #3DCCA3 | No |
| 6 | Sub-atributos | 8-10% | Sans regular | Blanco/Amber | Tooltip hover |
| 7 | Mensaje | 10-12% | Serif italic | Blanco #F7F4EE | Selectable |
| 8 | RUKLA action | 5-7% | Sans medium | Amber #F59E0B | Selectable |
| 9 | Color cristal swatch | 3-4% | Monospace | Cristal + hex | Click copy |
| 10 | Frase cierre | 3-5% | Serif italic | Dorado 80% | No |
| 11 | Edition serial | 2-3% | Monospace | Blanco 40% | No |
| 12 | Footer | 2-3% | Sans | Blanco 30% | Click link |

---

## Parte 3 — 4 layouts visuales

### Layout 1 — "Tarot clasico" (RECOMENDADO COMO DEFAULT)

- **Tamano carta:** 2.5 : 3.5 ratio vertical (750 × 1050 px mobile).
- **Estilo dominante:** ornamentado, simetrico, ritual. Heredero directo de Rider-Waite + Pax canon.
- **Mockup ASCII:**

```
┌──────────────────────────────────┐
│ ╔══════════════════════════════╗ │ <- frame ornamental dorado
│ ║ ·····  PAX-2026-A1-0042  ··· ║ │ <- edition serial top-right
│ ║                              ║ │
│ ║      EL CAMINO DEL           ║ │ <- title (2 lineas, centrado)
│ ║      SANADOR INTENSO         ║ │
│ ║                              ║ │
│ ║      ╔══════════════╗        ║ │
│ ║      ║              ║        ║ │
│ ║      ║      ◆       ║        ║ │ <- ilustracion cristal central
│ ║      ║   (cristal   ║        ║ │     (45% del area)
│ ║      ║   personal)  ║        ║ │
│ ║      ║              ║        ║ │
│ ║      ╚══════════════╝        ║ │
│ ║                              ║ │
│ ║    HEALER · Intensidad       ║ │ <- arquetipo
│ ║    orientada al cuidado      ║ │
│ ║                              ║ │
│ ║  ─────────────────────────   ║ │
│ ║  Escorpio · Kawak · 7 · Agua ║ │ <- sub-atributos en linea
│ ║  ─────────────────────────   ║ │
│ ║                              ║ │
│ ║   "Naciste para sostener     ║ │
│ ║    lo que otros no pueden    ║ │ <- mensaje (italica)
│ ║    ver. Tu fuerza es la      ║ │
│ ║    quietud."                 ║ │
│ ║                              ║ │
│ ║  RUKLA: Esta semana,         ║ │ <- accion sugerida
│ ║  escucha sin arreglar.       ║ │
│ ║                              ║ │
│ ║      ◉ #B43FFF               ║ │ <- swatch cristal + hex
│ ║                              ║ │
│ ║   "Y asi, el cristal         ║ │ <- frase cierre
│ ║    se enciende."             ║ │
│ ║                              ║ │
│ ║      pax-os.vercel.app       ║ │ <- footer
│ ╚══════════════════════════════╝ │
└──────────────────────────────────┘
```

- **Justificacion:** simetria absoluta = sensacion de destino. El cristal central es protagonista. El mensaje en italica abajo del cristal es el momento poetico. El frame ornamental dorado le da el "rito" de tarot premium. Funciona en mobile sin reflow porque todo apila vertical.
- **Implementacion frontend hint:** contenedor `aspect-[5/7]` con `border` ornamental SVG o `border-image`. Flex column vertical centrado. Cristal como `<Image>` SVG/PNG animado con `transform: rotateY` en idle loop. Mensaje en `<blockquote>` italica.

---

### Layout 2 — "TCG tactico"

- **Tamano carta:** 2.5 : 3.5 ratio vertical (750 × 1050 px), pero con grilla mas tecnica.
- **Estilo dominante:** coleccionable gamer. Atributos en grid arriba/abajo, ilustracion media-superior, bloque tecnico inferior. Heredero de Pokemon TCG + KeyForge.
- **Mockup ASCII:**

```
┌──────────────────────────────────┐
│┌────────────────────────────────┐│
││ EL SANADOR INTENSO     [◉ V7] ││ <- title + nivel/HP-like a la derecha
│├────────────────────────────────┤│
││  ┌──────────────────────────┐  ││
││  │                          │  ││
││  │           ◆              │  ││ <- ilustracion cristal
││  │      (cristal violeta    │  ││     (35% del area, mas chica)
││  │       hexagonal)         │  ││
││  │                          │  ││
││  └──────────────────────────┘  ││
│├────────────────────────────────┤│
││ HEALER · Cuidado intenso       ││ <- arquetipo
│├────────────────────────────────┤│
││ ⊙ Solar     Escorpio           ││
││ ⊙ Nahual    Kawak / Tormenta   ││ <- sub-atributos grid 2 cols
││ ⊙ Numero    7                  ││
││ ⊙ Aspecto   Agua / profundidad ││
│├────────────────────────────────┤│
││ MENSAJE                        ││
││ Naciste para sostener lo que   ││ <- mensaje (no italica, tecnico)
││ otros no pueden ver.           ││
│├────────────────────────────────┤│
││ RUKLA                          ││
││ Escucha sin intentar arreglar. ││ <- accion en bloque etiquetado
│├────────────────────────────────┤│
││ CRISTAL  ◉  #B43FFF            ││ <- swatch + hex inline
│├────────────────────────────────┤│
││ "Y asi el cristal se enciende."││ <- cierre (italica chica)
││                                ││
││ PAX-2026-A1-0042   pax-os.app  ││ <- footer con edition
│└────────────────────────────────┘│
└──────────────────────────────────┘
```

- **Justificacion:** la grilla tecnica con bloques etiquetados (MENSAJE, RUKLA, CRISTAL) lo hace legible como "ficha de personaje". Apela al coleccionista TCG. El nivel/HP-like al lado del title (`V7` = numero del nombre) agrega gamification. Menos ritual, mas "datasheet del alma".
- **Implementacion frontend hint:** grid CSS 12-column con secciones bien delimitadas por `border-t` jade. Cada bloque (`MENSAJE`, `RUKLA`, `CRISTAL`) tiene su label en uppercase amber + contenido debajo. Funciona muy bien para shareability porque es legible incluso en thumbnail.

---

### Layout 3 — "Cinematic masterpiece"

- **Tamano carta:** 2.5 : 3.5 ratio vertical, **pero con ilustracion full-bleed**.
- **Estilo dominante:** cinematografico, full-bleed art, textos translucidos superpuestos. Heredero de Magic Masterpieces + Sorcery + Lorcana.
- **Mockup ASCII:**

```
┌──────────────────────────────────┐
│::::::::::::::::::::::::::::::::::│ <- ilustracion FULL-BLEED
│::::::::::::::::::::::::::::::::::│   (cristal + escenario Pax
│::::::::::::::::::::::::::::::::::│    abstracto, neon-magico)
│::::::: PAX-2026-A1-0042 :::::::::│ <- edition flotante translucido
│::::::::::::::::::::::::::::::::::│
│:::::::::::::: ◆ :::::::::::::::::│
│:::::::::::::::::::::::::::::::::::│ <- cristal centrado, irradia
│::::::::::::::::::::::::::::::::::│
│::::::::::::::::::::::::::::::::::│
│  ╭────────────────────────────╮  │
│  │  EL SANADOR INTENSO        │  │ <- title sobre overlay
│  │  HEALER · Cuidado intenso  │  │     translucido violeta
│  ╰────────────────────────────╯  │
│::::::::::::::::::::::::::::::::::│
│::::::::::::::::::::::::::::::::::│
│  ╭────────────────────────────╮  │
│  │ Escorpio  Kawak  7  Agua   │  │ <- sub-atributos en bar
│  ╰────────────────────────────╯  │     translucido inferior
│::::::::::::::::::::::::::::::::::│
│  ╭────────────────────────────╮  │
│  │ "Naciste para sostener lo  │  │
│  │  que otros no pueden ver." │  │ <- mensaje sobre overlay basalt
│  │                            │  │     85% opacity
│  │ RUKLA: Escucha sin arreg.  │  │
│  │                            │  │
│  │ ◉ #B43FFF                  │  │
│  ╰────────────────────────────╯  │
│::::::::::::::::::::::::::::::::::│
│ "Y asi el cristal se enciende."  │ <- frase cierre flotante
│ pax-os.vercel.app                │     sin overlay
└──────────────────────────────────┘
```

- **Justificacion:** el efecto cinema. La ilustracion ocupa todo el rectangulo, los textos viven en cards translucidas (`backdrop-blur` + alpha) flotando sobre el arte. Maximo premium feel, maximo Instagram-shareable. El cristal y la atmosfera Pax respiran. Riesgo: la legibilidad depende fuerte del contrast del background.
- **Implementacion frontend hint:** `<div>` con `bg-image` full-bleed cover. Encima, multiples `<div>` con `backdrop-filter: blur(12px)` + `bg-basalt/40` + `rounded-2xl` para los overlays. Texto blanco con sombra negra suave para legibilidad garantizada.

---

### Layout 4 — "Minimal monolithic"

- **Tamano carta:** 2.5 : 3.5 ratio vertical, fondo basalt liso, tipografia gigante.
- **Estilo dominante:** minimal monolithic, premium Apple/A24. Cero frame ornamental, cero gradient ruido. Cristal central como unica imagen. Tipografia es la heroe.
- **Mockup ASCII:**

```
┌──────────────────────────────────┐
│                                  │
│  PAX-2026-A1-0042                │ <- edition top-left micro
│                                  │
│                                  │
│                                  │
│                                  │
│              ◆                   │ <- cristal solo, centrado
│           (grande,               │     30% del area
│            irradia               │     irradia luz violeta
│            suave)                │
│                                  │
│                                  │
│                                  │
│                                  │
│  EL                              │
│  SANADOR                         │ <- title MUY grande
│  INTENSO                         │     serif display, mayusculas
│                                  │     left-aligned
│                                  │
│  Healer · Intensidad orientada   │ <- arquetipo sub-line
│  al cuidado                      │
│                                  │
│  Escorpio   Kawak   7   Agua     │ <- sub-atributos sutiles
│                                  │
│  ────                            │ <- divider micro jade
│                                  │
│  Naciste para sostener lo que    │
│  otros no pueden ver. Tu fuerza  │ <- mensaje en serif italica
│  es la quietud.                  │     leading generoso
│                                  │
│  ── RUKLA ──                     │
│  Escucha sin intentar arreglar.  │ <- RUKLA con label entre rayas
│                                  │
│  ◉  #B43FFF                      │ <- swatch minimal
│                                  │
│  Y asi el cristal se enciende.   │ <- cierre, sin comillas
│                                  │
│                            pax-os│ <- footer micro bottom-right
└──────────────────────────────────┘
```

- **Justificacion:** silencio visual = lujo. La ausencia de frame ornamental hace que el cristal pese mas. Funciona para audiencias que ven el tarot clasico como "kitsch". Es la version "no estoy gritando, soy premium". Riesgo: pierde el feel coleccionable de TCG/tarot — se parece mas a poster A24 que a carta.
- **Implementacion frontend hint:** `bg-basalt-950` con padding generoso (`px-12 py-16`). Title en `text-7xl` serif display. Todo left-aligned excepto el cristal centrado. Generous whitespace. Animaciones minimas: solo el cristal respira. Sin overlays, sin foil agresivo. Holo solo se activa en hover muy sutil.

---

## Parte 4 — Recomendacion

### Layout recomendado como default del MVP: **Layout 1 "Tarot clasico"**

**Por que:**

1. **Coherencia con el producto.** El Oraculo Pax ES una lectura ancestral. El usuario espera el lenguaje visual del tarot. Layout 1 entrega la expectativa sin reinventar la rueda.
2. **Premium feel sin riesgo.** El frame ornamental dorado + simetria + cristal central + mensaje en italica son un combo probado durante 150 anos. Imposible que se sienta cheap.
3. **Mejor balance entre informacion y emocion.** Todos los 12 componentes encajan sin amontonarse. El usuario lee top-down naturalmente (title → cristal → arquetipo → mensaje → RUKLA → cierre).
4. **Shareability.** El formato vertical con frame ornamental se ve bien en thumbnail (WhatsApp, Instagram story) y en full screen.
5. **Mobile-first natural.** El stack vertical respeta mobile sin gymnastics de CSS.

### Fallback / variantes opcionales

- **Si el feedback de Pipez es "se siente kitsch / muy tarot tradicional":** mover a **Layout 4 "Minimal monolithic"**. Mismo contenido, lenguaje visual A24/Apple. Premium sin ornamental.
- **Si el equipo quiere maximo "wow" para campana de lanzamiento:** **Layout 3 "Cinematic masterpiece"** como version premium edition. Es la version "edicion especial" del Oraculo (ej. solsticios, lunas nuevas).
- **Si en algun momento el Oraculo se vuelve gamificado** (ej. mazo coleccionable, intercambio entre usuarios): pivot a **Layout 2 "TCG tactico"** porque es el que mejor codifica "ficha de personaje".

### Roadmap visual sugerido

| Fase | Layout | Razon |
|---|---|---|
| MVP launch | Layout 1 (Tarot clasico) | Default seguro, premium probado |
| Iteracion 2 | Permitir toggle a Layout 4 (Minimal) | Cobertura audiencia A24/Apple |
| Edicion especial (solsticios) | Layout 3 (Cinematic) | "Limited drop" feel |
| Gamificacion futura | Layout 2 (TCG) | Solo si se vuelve coleccion intercambiable |

---

## Apendice — Reglas duras del diseno (para el frontend dev)

1. **Ratio 2.5:3.5 obligatorio.** No deformar. En mobile, `width: 100%; aspect-ratio: 5/7;`.
2. **Paleta canon obligatoria.** Cero colores fuera de la paleta de la seccion 2.1.
3. **Tipografias maximo 3 familias por carta.** Sugerencia: 1 serif display (titles) + 1 sans grotesca (atributos) + 1 monospace (codigos).
4. **Foil/holo efecto debe ser sutil.** Inclinacion maxima 12 grados. Si marea, esta mal calibrado.
5. **El cristal central NUNCA debe ser placeholder.** Si no hay cristal generado, mostrar uno default del set canon (no un emoji, no un SVG generico).
6. **Edition serial UNICO por carta.** Backend genera incrementalmente.
7. **Selectable text en mensaje + RUKLA + frase cierre.** El visitante quiere copiar.
8. **Click en swatch copia hex.** UX detail premium obligatorio.
9. **Animacion idle del cristal SIEMPRE on.** Es lo que diferencia "screenshot" de "objeto vivo".
10. **Footer `pax-os.vercel.app` SIEMPRE presente.** Es la marca de la edicion.

---

> Fin del spec. Frontend dev usa este doc + el documento de variantes visuales A-E del visual designer para implementar.
