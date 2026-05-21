# Crítica honesta del MVP /oraculo — v1

> Análisis previo al rediseño v2. Identifica 7 issues concretos donde el MVP actual no cumple la promesa de "knowledge humano+paxian visible".

---

## Issue 1 — Hero card: el copy no dice de qué se trata

**Qué está mal:** "Mira hacia abajo." + "El oráculo te está esperando." + "Tu carta ancestral, leída desde el corazón de la tribu." es genérico. Podría ser cualquier oráculo. No menciona los 3 sistemas (maya, astral, pax) de manera explícita. El visitante no sabe en qué se diferencia esto de un horóscopo común.

**Qué espera el usuario:** que al ver el hero ya sepa que hay una fusión de sistemas. "Maya × astral × arquetipo del servicio" visible desde el primer segundo.

**Cómo se mejora:** Cambiar el copy del hero a algo que nombre los sistemas. Footer de la card debe listar los 4 pilares visualmente: "maya ✦ astral ✦ pax ✦ rukla".

---

## Issue 2 — Formulario: border-bottom básico vs. experiencia glassmorphic

**Qué está mal:** Los inputs tienen `border-b border-[#333]` y fondo transparente. Es el estilo más básico posible. Contrasta fuertemente con la estética glassmorphic del hero card — hay un quiebre visual total entre la sección 1 (el hero) y la sección 2 (el form).

**Qué espera el usuario:** que el form tenga el mismo lenguaje visual que el hero: glass, blur, bordes luminosos violeta-coral, sensación de estar dentro del mismo universo.

**Cómo se mejora:** Envolver el form en un glassmorphic container (backdrop-blur, fondo rgba oscuro, borde violeta sutil). Los inputs con `rounded-lg`, fondo rgba, focus ring violeta.

---

## Issue 3 — MockOracleCard: no muestra los 3 sistemas (maya / astral / pax)

**Qué está mal:** La carta de resultado tiene: arquetipo genérico + mensaje Agatha + gesto de la semana. No hay mención de nahual maya, ni tono, ni signo astral (sol/luna/ascendente), ni ningún símbolo visual. Es una tarjeta de texto con un cristal decorativo.

**Qué espera el usuario:** ver explícitamente la fusión — un row "Maya: Nahual X · Tono Y", un row "Astral: Sol en Z · Luna en W · Asc en V", un row "Arquetipo Pax: Portador de Umbral · intensidad alta". Iconografía minimalista por sistema, no solo texto.

**Cómo se mejora:** Agregar 3 sub-secciones con iconos/símbolos CSS simples, paleta diferenciada por sistema (violeta para maya, azul-jade para astral, dorado para pax), código de edición tipo "PAX-2026-A1-0042", swatch del cristal-eco con hex code visible.

---

## Issue 4 — /como-funciona: texto plano sin experiencia visual

**Qué está mal:** Es una lista de secciones numeradas con texto sobre fondo negro liso. No hay imágenes, no hay motion, no hay contexto visual que haga sentir al visitante dentro del universo Pax. El lore de Agatha, la Cámara, Iris, Baba — todo es texto corrido sin ancla visual.

**Qué espera el usuario:** una experiencia scroll-cinematica donde cada sección tiene su propio card visual sobre un fondo en movimiento. Las 8 imágenes generadas (C/D hero, texture, decorative) deben estar integradas aquí como ilustraciones, no solo como decoración.

**Cómo se mejora:** Cada sub-sección (maya, astral, pax, rukla, quién-te-lee) es una card glassmorphic con imagen de fondo propia, fade-in al scroll, misma estética que el hero.

---

## Issue 5 — /resultado: no tiene layered storytelling por sistema

**Qué está mal:** La página resultado muestra el arquetipo + un bloque de texto + grid de datos astrológicos 3x2 + gesto de la semana. Los datos están en un grid genérico sin identidad visual. No hay distinción entre "esto es tu parte maya" vs "esto es tu parte astral" vs "esto es tu arquetipo Pax".

**Qué espera el usuario:** 3 o 4 secciones diferenciadas visualmente, cada una con paleta, icono y tono propio. El visitante debe poder decir "aquí me explican lo maya, aquí lo astral, aquí lo Pax".

**Cómo se mejora:** Reemplazar el grid genérico por 4 secciones glassmorphic con paletas distintas (violeta-rosado para maya, azul-jade para astral, violeta-dorado para pax, verde-cristal para la acción). Cristal-eco encima de todo, como anchor visual central.

---

## Issue 6 — Cristal-eco: placeholder vacío sin identidad

**Qué está mal:** El cristal-eco en la carta mock y en resultado es un div con clip-path y color fijo violeta. No tiene forma determinada, no tiene hex code visible, no tiene nombre. Tampoco hay diferencia entre cristal apagado y encendido a nivel de diseño — solo hay opacity.

**Qué espera el usuario:** un swatch visual claro con hex code (ej. "#B43FFF"), forma específica por arquetipo sugerida, animación de pulso diferente entre apagado (lento, tenue) y encendido (brillante, fulgurante).

**Cómo se mejora:** Mostrar el cristal-eco como un elemento primario de la carta — nombre del color, hex code, descripción de 1 línea ("violeta-umbral: el color del que entra primero"), animación CSS diferenciada.

---

## Issue 7 — Identidad de los 4 sistemas no es escaneable en 5 segundos

**Qué está mal:** En ninguna de las 3 páginas hay un elemento visual único que le diga al visitante "esto fusiona 4 sistemas". El footer del hero menciona "pax-os ✦ oráculo ✦ rukla ✦ tribu" — eso no dice nada sobre los sistemas de lectura.

**Qué espera el usuario:** un badge o row siempre visible (en el header de la carta, en la top bar de /como-funciona, en el nav de /resultado) que diga los 4 sistemas con símbolos: "🔶 Maya · ⭐ Astral · 💎 Pax · 🌀 Rukla" (o equivalentes CSS, sin emoji reales si se prefiere).

**Cómo se mejora:** Crear un componente `<SistemasRow />` reutilizable con los 4 badges (iconos minimalistas SVG inline + label + color de acento por sistema) que aparezca en el header de la carta y en el hero de /como-funciona.
