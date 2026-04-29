---
title: Prompts Seedance — Episodio 1
description: Prompts video-gen escena por escena con references, audio cues y best practices Seedance 2026
tool: Seedance (clips de 15s)
---

## Cómo usar estos prompts

- **Orden recomendado de generación:** primero generá 3 seed-clips de identidad (Jiggy, Wiz, Mariela) en backdrop gris neutro, guardá el seed number de cada uno. Después arrancá los 16 prompts narrativos en orden cronológico (Escena 01 → 14) — esto te deja encadenar last-frame → first-frame sin tener que volver atrás. Las escenas con mayor riesgo (06, 09, 11) hacelas con el modelo ya "calibrado" después de las 3-4 primeras.
- **I2V vs T2V:** todo clip que tenga personaje recurrente va en modo **I2V (image-to-video)** con el char-sheet PNG cargado en slot 1 + el seed lock del seed-clip. T2V puro solo para clips sin personaje (Escena 01, parcialmente Escena 14). I2V con first-frame externo (Nano Banana / still pre-renderizado) es obligatorio en Escena 06 (texto handwritten legible), Escena 08A, Escena 11 (negociación de paletas) y Escena 14 (libreta brillando).
- **Encadenado clip-a-clip:** exportá el último frame del clip N como PNG y subílo como first-frame del clip N+1 cuando la transición es continuous (escenas 1-2, 5-6, 6-7, 8A-8B, 9-10, 11-12, 12-13). En hard cuts (3-4, 4-5, 7-8A, 13-14) NO uses el last-frame — la transición depende del salto de paleta y temperatura.
- **Parámetros sugeridos Seedance 2.0:** CFG 7.0 para personajes principales, 6.0 para escenas atmosféricas sin char (B1, B14). Steps 30 default, 40 para los clips de hinge (06, 08, 11). Seed: fijo por personaje (anotá los seed numbers de los 3 seed-clips abajo), aleatorio para escenas atmosféricas. Resolution: 1080p out, upscale a 4K post.
- **References según versión:** Seedance 2.0 acepta hasta 9 imágenes en multimodal slots. Asignación canónica para PAX: slots 1-2 character locks (face + outfit), slot 3 mood reference (portada o still previa), slots 4-5 lighting/palette references si aplica. NO subir foto real humana — el filtro la rechaza, todo lo humano va vía char-sheet AI-generated.

## Consistencia entre clips

- **Seeds fijos por personaje recurrente:** anotá el seed number del seed-clip de cada personaje. Reusalo TODA vez que ese personaje aparezca. Sin esto, drift garantizado al clip 4-5 (Hallazgo 2.2 del research).
- **Char-sheet textual literal repetido en cada prompt:** las primeras ~25 palabras de cada prompt son el char-sheet del personaje principal de ese clip, palabra por palabra, sin paráfrasis. El modelo anchorea a las primeras 20 palabras — si cambiás "turquoise iris" por "cyan iris" entre clips, la cara se mueve.
- **Last-frame chaining para transiciones continuous:** después de generar un clip, exportá frame final como PNG y subílo como Start Frame del siguiente clip cuando la escena es la misma o el match es continuo. Esto compensa la falta de memoria entre clips de Seedance.
- **Si Seedance dropea el lock visual** (cara que de repente se suaviza, color de ojo que cambia, prop que desaparece): regenerá el clip — NO lo arregles en post. Aplicá Single-Axis Iteration (cambiá UNA variable: primero el seed, después el CFG, después el char-sheet wording). Generá siempre 3 variaciones y elegí la mejor — la latent seed a veces saca un mal draw aunque los parámetros sean idénticos.

## Reference images globales

| Personaje / mood | Path |
|---|---|
| Jiggy (character lock) | `public/images/personajes/jiggy.png` |
| Wiz (character lock) | `public/images/personajes/wiz.png` |
| Byte (character lock) | `public/images/personajes/byte.png` |
| Luxa (character lock) | `public/images/personajes/luxa.png` |
| Zek (character lock) | `public/images/personajes/zek.png` |
| Mariela (character lock) | `public/images/personajes/mariela.png` |
| Mood — caverna acción/paleta universo | `public/images/portadas/portada.png` |
| Mood — poster heroico grupal Pax | `public/images/portadas/portada2.png` |

## Audio + sonido (general del episodio)

- **Score base:** sintetizador analógico cálido + cello bajo sostenido. Tono general menor en B1-B11, modula a mayor solo en B12 ("okay") y B13.
- **Pulso caverna (motivo recurrente):** subwoofer arrítmico bajo 40-55 Hz, como un latido lento. Aparece en B1, B2 (más suave), B4 (sub-audible bajo la libreta), B5, B6 (sincronizado con el latido de Mariela un instante), B13 (ya casi un latido normal), B14 (sincronizado con el pulso de la página, una vez, después silencio).
- **Foleys recurrentes:** caverna = goteo lejano, polvo cayendo en líneas verticales (whisper-level), reverb granular largo. Cocina Mariela = tic-tac de reloj de pared, rumor lejano de TV vecino, hum de pava cuando aplica, cerámica leve. Calle Av. Bilbao = hum mecánico de drones (no amenazante, utilitario), silencio de calle vacía, brisa nocturna mínima.
- **SFX clave únicos:** chime cyan agudo en B6 (un solo hit, descartable como olla del vecino). Cristal materializándose en B8B (panel de vidrio enfriándose con undertone cálido). Sub-tone shift cuando el dorado pulsa en B10 (frecuencia que sale del aire). Acorde mayor sostenido en B12 (primer momento mayor del piloto).
- **Diálogo total del episodio:** 33 palabras en líneas + 4 en end card = 37 palabras. Dialogue se inyecta en post; el prompt Seedance solo describe el gesto/expresión, no pide al modelo que sintetice voz. Lipsync se cubre con planos cuya boca queda fuera de cuadro o en sombra cuando es posible.

---

## Escena 01 — Un cristal a punto de apagarse

- **ID**: `escena-01`
- **Duración**: 15s → 1 clip Seedance
- **Plano(s)**: slow descending crane / dolly-down hacia el cristal, locked horizon
- **Personajes en frame**: ninguno (silueta Pax inmóvil muy al fondo, no identificable)
- **Reference images** (cargar en este orden):
  - `public/images/portadas/portada2.png` (mood reference — paleta caverna, atmósfera volumétrica)
- **First frame**: T2V directo (sin char). Si querés extra control, generar still en Nano Banana con el cristal magenta apenas latiendo en estalagmita baja, y usarlo como first-frame I2V.

**Prompt Seedance** (copiable):

```
A single magenta crystal the size of a fist embedded low on a dark stone stalagmite, faintly pulsing in the dark, surrounded by hundreds of empty unlit stalagmites in a vast subterranean cavern, one motionless cyclops silhouette barely visible far in the deep background.

Action: For the first 10 seconds: the camera slowly descends from above through dust-laden volumetric air toward the pulsing crystal, dust falling in slow vertical lines through a single sliver of bioluminescent ambient light. Then for the final 5 seconds: the camera holds at medium close-up on the crystal, which pulses once weak, almost stopping.

Camera: slow descending crane from high wide to medium close-up over 15 seconds, locked horizon, no shake, no rotation.

Setting: vast underground cavern Uray Pacha, hundreds of empty stone stalagmites of varying sizes scattered in deep background, rough porous igneous rock with fine mineral veining, dense atmospheric haze, scattered dust motes catching faint light, deep blue-violet shadows.

Lighting: single weak magenta emissive from the crystal as primary source, dim cyan ambient bioluminescent fill from above, deep blue-violet shadows (#0E0820), heavy volumetric god-rays through dust, high contrast bloom on emissive only.

Style: stylized 3D animation, semi-realistic PBR shading, painterly volumetric background, slight film grain, magenta-turquoise complementary color grading, premium mobile-game cinematic look, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no photorealistic style, no anime, no cel-shaded flat, no glowing portals, no fantasy battle clichés, no game HUD, no fast motion, no character close-ups, no facial detail.
```

**Negative prompt**:
```
photorealistic, hyperrealistic, anime, cel-shaded, 2D hand-drawn, cartoon outlines, glowing portal, magic circle, fireball, lightning, dragon, sword, HUD, gem counter, health bar, jittery motion, frame skip, character drift, eye glitch, watermark, text overlay, brand logos, fast motion, whip pan, dolly zoom, low resolution
```

**Audio**:
- **Diálogo**: ninguno
- **SFX clave**: pulso bajo arrítmico (40-55 Hz, como latido lento casi detenido), polvo cayendo whisper, reverb granular largo de caverna profunda
- **Ambient**: silencio cavernoso denso, sin música

**Transición a la siguiente escena**:
Continuous → Escena 02 mantiene la misma caverna, mismo cristal en frame, solo cambia el ángulo a plano reverso amplio. Encadená last-frame de B1 como first-frame de B2 si querés mantener exactamente la misma posición del cristal y la luz.

**Notas de dirección**:
El espectador entra a un mundo que se está apagando — la inacción es el mensaje. Riesgo Seedance: puede meter más cristales encendidos en el fondo "para llenar". Vigilá el negative prompt y regenerá si aparecen más de UN cristal emisivo en frame. La silueta del fondo es un detalle de diseño, no un personaje — si Seedance la dropea, no la regeneres por eso.

---

## Escena 02 — Los que esperan

- **ID**: `escena-02`
- **Duración**: 15s → 1 clip Seedance
- **Plano(s)**: static wide reverse, locked tripod
- **Personajes en frame**: Wiz (silueta, frente, apoyado en bastón), Byte (silueta atrás, LED audífonos lima tenue), Zek (silueta atrás, brim de gorra atrapando luz)
- **Reference images** (cargar en este orden):
  - `public/images/personajes/wiz.png` (character lock — incluso en silueta para que la proporción sea correcta)
  - `public/images/personajes/byte.png` (lock — los LEDs lima son su silhouette identifier)
  - `public/images/personajes/zek.png` (lock — el brim de gorra es su silhouette identifier)
  - `public/images/portadas/portada2.png` (mood / paleta)
- **First frame**: I2V con last-frame de B1 (mismo cristal, misma luz) — Seedance compone las 3 siluetas detrás.

**Prompt Seedance** (copiable):

```
@Wiz an elder cyclops in deep purple hooded robe leaning on a dark wooden staff topped with a magenta-violet crystal, white voluminous beard, in silhouette in foreground; behind him @Byte a young cyclops in dark purple hoodie with large over-ear headphones glowing faint lime-green LEDs in silhouette mid-ground; further back @Zek a cyclops with a sideways purple cap whose brim catches a tiny edge of light, in silhouette. The dying magenta crystal embedded in the stalagmite is visible deep in the background, faintly pulsing.

Action: For the first 10 seconds: all three silhouettes stand motionless, only the lime LEDs and the magenta crystal pulse faintly. Wiz looks at the distant crystal, then slowly tilts his head upward toward a hairline crack in the cavern ceiling where a thin sliver of surface light filters down. Then for the final 5 seconds: Wiz lowers his head one inch, holds. The other two do not move. The inaction is the decision.

Camera: static wide reverse shot, locked tripod, no camera movement, full cavern depth visible.

Setting: same vast underground cavern as before, hundreds of empty stalagmites, hairline ceiling crack with thin sliver of pale surface light filtering down, dense atmospheric haze, dust motes.

Lighting: distant magenta crystal as weak background emissive, faint lime-green LED glow on Byte's headphones (#A7F432), pale cyan sliver from ceiling crack, deep blue-violet ambient shadows (#0E0820), high silhouette contrast — characters mostly black against background light.

Style: stylized 3D animation, semi-realistic PBR shading, painterly volumetric background, slight film grain, magenta-turquoise complementary color grading, premium mobile-game cinematic look, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no photorealistic, no anime, no cel-shaded flat, no facial detail visible (silhouettes only), no character drift, no extra figures, no fast motion, no glowing eyes through silhouette.
```

**Negative prompt**:
```
photorealistic, hyperrealistic, anime, cel-shaded, 2D, faces visible in detail, more than three figures, glowing eyes through silhouette, jittery motion, character morph, frame skip, watermark, text overlay, brand logos, fast motion, whip pan, dolly zoom
```

**Audio**:
- **Diálogo**: ninguno
- **SFX clave**: mismo pulso pero más suave, una nota baja de cello sostenida que entra a los 4 segundos
- **Ambient**: respiración apenas audible de Wiz, reverb cavernoso

**Transición a la siguiente escena**:
Hard cut → Escena 03 (oficina Mariela, fluorescent blanco frío). El salto de paleta es el mensaje: caverna mágica → mundo humano clínico. NO encadenar last-frame.

**Notas de dirección**:
3 siluetas, no 4 (Luxa NO está acá — debuta en B9). Si Seedance mete una cuarta silueta, regenerá. Riesgo Seedance: puede iluminar las caras "para que se vean" — vigilar negative prompt y exigir que las caras queden en sombra total. Los identificadores de silueta son: bastón con cristal magenta (Wiz), LEDs lima (Byte), brim de gorra (Zek). Sin esos 3 elementos no hay reading.

---

## Escena 03 — Mariela en la oficina

- **ID**: `escena-03`
- **Duración**: 15s → 1 clip Seedance
- **Plano(s)**: slow gentle pan right de cubículos a Mariela, después static medium en ella
- **Personajes en frame**: Mariela (foreground, frente a la planilla), un compañero (background, pasando, tira carpeta sin parar)
- **Reference images** (cargar en este orden):
  - `public/images/personajes/mariela.png` (character lock)
- **First frame**: T2V directo — escena nueva, paleta nueva, no sirve last-frame de B2.

**Prompt Seedance** (copiable):

```
@Mariela a 36-year-old Latin-American woman, brown hair pulled back in low ponytail, sober light office blouse, thin metal-framed glasses with hairline scratch on right lens, no makeup, calm tired competent vacant expression, naturalistic stylized human skin tones with softened cinematic 3D features, sitting at a desk in a small Santiago office with nine cubicles around her, a spreadsheet with pivot tables and yellow-and-red highlighted cells on her monitor, a mug of cold coffee, a small framed photo of an 8-year-old niece on the desk quietly off to the side.

Action: For the first 8 seconds: the camera slowly pans right across the cubicles approaching @Mariela's workstation, ending on her face in medium shot. Then for the final 7 seconds: a coworker walks past behind her and drops a manila folder on her desk without stopping; @Mariela closes one spreadsheet tab and opens another with a single small mouse-click, expression unchanged. The wall clock behind her reads 6:47 PM.

Camera: slow gentle pan right at constant speed for 8 seconds, then static medium shot for 7 seconds, locked horizon, no shake.

Setting: small open-plan office in Providencia Santiago at end of workday, nine grey cubicles, fluorescent ceiling tubes overhead, a distant photocopier visible, beige carpet, neutral office furniture, mundane and lived-in, not glamorous.

Lighting: cool-white fluorescent overhead 4500K dominant, slight green tint typical of office tube lights, no warm pockets, even flat fill across the room, mild specular on glasses, dusk-blue from window in deep background.

Style: stylized 3D animation, semi-realistic PBR shading, softened human proportions, slight film grain, neutral cool office color grading, painterly background depth, premium animated cinematic look, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no photorealistic facial details, no anime, no cel-shaded flat, no thriller vignette, no glamour beauty shot, no magenta or turquoise emissives, no Pax palette in this scene, no fast motion, no extra figures crowding the frame, no character drift on Mariela's face.
```

**Negative prompt**:
```
photorealistic facial pores, hyperrealistic skin, anime big-eyes, cel-shaded, glamour beauty lighting, thriller vignette, magenta crystal, turquoise glow, fantasy elements, more than 2 figures in foreground, character drift, jittery motion, watermark, text overlay, brand logos on monitors, readable spreadsheet text, fast motion
```

**Audio**:
- **Diálogo**:
  - COWORKER (apenas mirando arriba): "Thanks, Mari." (~0:08-0:09 del clip)
  - MARIELA (sin mirar atrás): "Sure." (~0:10 del clip)
- **SFX clave**: fotocopiadora distante, hum de aire acondicionado, click de mouse, golpe seco de carpeta sobre escritorio
- **Ambient**: oficina rumorosa baja, fluorescent ballast hum 50Hz

**Transición a la siguiente escena**:
Hard cut → Escena 04 (metro). El cello de B2 ya se desvaneció en B3 — B4 vuelve a introducir piano y el pulso sub-audible.

**Notas de dirección**:
Mariela presentada en 15 segundos sin un solo descriptor de cámara. La cultura latina filmada como cotidiana, no como escenografía. Riesgo Seedance: puede glamorizarla con shallow DOF y backlight bonito — el negative prompt rechaza eso. Riesgo lipsync: el diálogo es muy corto (3 palabras totales), si Seedance no lo logra limpio, planificar plano alternativo donde la boca de Mariela quede fuera de cuadro durante "Sure" y meter el dialogue en post.

---

## Escena 04 — La libreta en el metro

- **ID**: `escena-04`
- **Duración**: 15s → 1 clip Seedance
- **Plano(s)**: static medium con subtle handheld sway (movimiento del vagón), después tighter sobre la libreta
- **Personajes en frame**: Mariela (foreground, parada agarrada al pasamanos), pasajeros (out-of-focus background, sin caras detalladas)
- **Reference images** (cargar en este orden):
  - `public/images/personajes/mariela.png` (character lock — misma identidad que B3)
- **First frame**: T2V directo. Opcional: still pre-renderizado de Mariela parada en el vagón con la libreta cerrada en la mano para anclar pose inicial.

**Prompt Seedance** (copiable):

```
@Mariela a 36-year-old Latin-American woman, brown hair pulled back in low ponytail, sober light office blouse, thin metal-framed glasses, no makeup, calm tired expression, softened stylized human proportions, standing in a packed Santiago Line 5 metro car at evening rush hour holding a chrome handrail, blurred passengers around her without detailed faces, the camera frames her alone among the crowd.

Action: For the first 7 seconds: @Mariela pulls her phone from her bag, glances at a Slack notification, ignores it, puts it away. Then for the final 8 seconds: she automatically reaches into her bag and pulls out a small A6 brown leather-bound notebook with a sun-faded elastic band and a thin hairline crack running along the spine; she opens it but pauses on the previous entry from 6 months ago — three lines of her own handwriting in pencil; she stares one second too long, then closes it and puts it back without writing.

Camera: static medium shot with very subtle handheld sway from the moving train, slow tighter framing on the notebook in the second half, locked horizon overall, no zoom, no aggressive shake.

Setting: interior of a Santiago Line 5 metro car at evening rush hour around 7 PM, scuffed metal interior, blurred crowd of commuters around her, red emergency hammer in deep background, scratched windows showing dark tunnel walls passing.

Lighting: cool-blue interior fluorescents from overhead metro tubes, intermittent flicker as train passes lights in tunnel, mild specular on chrome rail and glasses, no warm tones, neutral urban evening palette.

Style: stylized 3D animation, semi-realistic PBR shading, softened human proportions, slight film grain, neutral cool urban color grading, painterly out-of-focus crowd, premium animated cinematic look, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no aggressive shake, no text overlay, no readable handwriting in close-up, no watermark, no brand logos, no readable phone notification text, no photorealistic facial details, no anime, no cel-shaded flat, no Pax palette, no fast motion, no character drift on Mariela's face, no extra figures with detailed faces.
```

**Negative prompt**:
```
photorealistic skin pores, hyperrealistic, anime, cel-shaded, glamour beauty shot, thriller vignette, magenta crystal, turquoise glow, readable handwriting on notebook page, readable phone screen text, brand logos visible, more than one face in detail, character drift, jittery motion beyond train sway, watermark, text overlay, fast motion
```

**Audio**:
- **Diálogo**: ninguno
- **SFX clave**: rumor del metro, brake squeal lejano, slack notification ping (corto, ignorado), single low piano note cuando aparece la libreta, pulso de la caverna sub-audible (40 Hz) solo cuando la cámara está sobre la libreta
- **Ambient**: vagón lleno respirando, anuncios apagados de estación, ruedas sobre rieles

**Transición a la siguiente escena**:
Soft cut / dissolve corto → Escena 05 (cocina Ñuñoa, atardecer). El piano sostiene a través del corte.

**Notas de dirección**:
La libreta como objeto-símbolo entra en 15s sin que nadie la nombre. Riesgo Seedance: la entrada de la libreta de 3 líneas con texto legible — vamos a ignorar la legibilidad real (Seedance no es confiable con texto handwritten); el viewer no necesita leer "groceries / call mom / fix printer", solo necesita LEER que hay 3 líneas de letra humana fechada. Si Seedance saca squiggles, está bien. NO regenerar por eso.

---

## Escena 05 — La cocina, antes de escribir

- **ID**: `escena-05`
- **Duración**: 15s → 1 clip Seedance
- **Plano(s)**: slow dolly-in de medium-wide a medium close, locked horizon
- **Personajes en frame**: Mariela
- **Reference images** (cargar en este orden):
  - `public/images/personajes/mariela.png` (character lock)
- **First frame**: T2V directo. Opcional: still pre-renderizado en Nano Banana de Mariela parada frente a la pava con el reflejo en la ventana, para fijar el primer beat.

**Prompt Seedance** (copiable):

```
@Mariela a 36-year-old Latin-American woman, brown hair pulled back in low ponytail, sober light office blouse, thin metal-framed glasses, calm tired expression, softened stylized human proportions, standing in a small kitchen of a Ñuñoa Santiago apartment at dusk, a single warm tungsten Edison-style hanging bulb above a small wooden kitchen table, a steel kettle on a gas stove, a window showing Santiago at dusk with the Andes barely visible behind a smog-pink sky, ceramic tile floor.

Action: For the first 6 seconds: @Mariela places the kettle on the stove and turns the gas on, then stands still beside it, catches her own reflection in the window glass and holds her own gaze for a long beat. Then for the final 9 seconds: she reaches into her bag on the chair, pulls out the same small brown leather notebook from the metro scene, sets it gently on the table, picks a pencil from a small ceramic jar, sits down on a wooden chair, places hands flat on the table next to the closed notebook, and pauses — long pause — not opening it yet.

Camera: slow dolly-in from medium-wide framing of the whole kitchen to medium close-up of @Mariela seated at the table over 15 seconds, locked horizon, no shake.

Setting: small Ñuñoa apartment kitchen, ceramic tile floor in muted ochre, single hanging Edison bulb above table, dusk-blue cool window light from the right, warm tungsten pool from the bulb, modest fridge in deep background, gas stove with steel kettle, small wooden table with two chairs, ceramic pencil jar, no clutter.

Lighting: warm tungsten 3000K key light from overhead Edison bulb pooling on the table and on @Mariela's face from above, cool dusk-blue 5500K fill from the window on her left side, soft contrast, mild volumetric warm haze around the bulb, deep dusk-blue shadows in corners, no Pax palette emissives.

Style: stylized 3D animation, semi-realistic PBR shading, softened human proportions, slight film grain, warm tungsten + cool dusk complementary color grading, painterly volumetric background, premium animated cinematic look, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no photorealistic, no anime, no cel-shaded flat, no thriller vignette, no glamour beauty shot, no magenta crystal visible yet, no turquoise emissive, no fantasy elements, no fast motion, no character drift on Mariela's face, no other figures.
```

**Negative prompt**:
```
photorealistic skin pores, hyperrealistic, anime, cel-shaded, glamour beauty shot, thriller vignette, shallow DOF cinematic blur, magenta crystal visible, turquoise emissive, Pax characters in frame, fantasy elements, brand logos, watermark, text overlay, character drift, jittery motion, fast motion, multiple figures
```

**Audio**:
- **Diálogo**: ninguno
- **SFX clave**: pava empezando a zumbar suave (stove ignition click, water hum), pulso de la caverna muy suave bajo el piano (sub-audible), piano sostenido nota baja
- **Ambient**: cocina silenciosa, tic-tac muy lejano de reloj de pared, brisa apenas en ventana

**Transición a la siguiente escena**:
Continuous → Escena 06 misma cocina, mismo encuadre, just zoom-in temporal (lo cubre el editor con un cut tighter o lo deja como un solo dolly seguido). Encadená last-frame de B5 como first-frame de B6.

**Notas de dirección**:
Beat contemplativo, score haciendo 70% del trabajo. Riesgo Seedance: puede acelerar el dolly — sin la duración explícita "over 15 seconds" llegaría a close-up muy rápido. Vigilá. Riesgo continuidad: la libreta tiene que ser EXACTA a la de B4 (mismo crack en lomo, misma faded elastic). Si difiere, regenerá B5 o ajustá B4.

---

## Escena 06 — La pregunta

- **ID**: `escena-06`
- **Duración**: 30s → **2 clips Seedance encadenados (escena-06-A + escena-06-B)**
- **Plano(s)**: tight close-up sobre la mano y la página, después push-in muy lento al lomo
- **Personajes en frame**: Mariela (mano y antebrazo, cara fuera de foco a veces)
- **Reference images** (cargar en este orden):
  - `public/images/personajes/mariela.png` (character lock — el antebrazo y mano)
- **First frame**: I2V con first-frame externo OBLIGATORIO. Generá en Nano Banana el still del primer frame de B6-A (mano de Mariela apoyada sobre página en blanco después de la entrada vieja, lápiz en la otra mano) — esto fija la composición. Para B6-B, last-frame de B6-A es first-frame.

### Sub-clip escena-06-A (15s) — escribir la pregunta

**Prompt Seedance** (copiable):

```
@Mariela's left hand and forearm in tight close-up, brown hair faintly visible at top of frame, the hand resting on an open page of a small brown A6 leather-bound notebook on a small wooden kitchen table, a wooden pencil held in her right hand entering frame from the right; the page is blank except for a previous entry visible at the top of the page in older fading pencil handwriting (three short lines, intentionally illegible squiggles), the rest of the page empty.

Action: For the first 5 seconds: her hand rests on the page, she lifts the pencil, hesitates, the pencil tip hovers above the empty space below the old entry. Then for the final 10 seconds: she writes slowly with the unsteady hand of someone out of practice — the pencil moves left to right across the page producing handwritten cursive English text reading "Why did I stop writing here?" but the actual letterforms can be approximate placeholder squiggles, the legible final text will be composited in post-production. After writing she lifts the pencil, holds it suspended a centimeter above the page, stares at the line.

Camera: static tight close-up framed on hand-and-page, very subtle natural micro-movement, no zoom, no shake, locked horizon.

Setting: same small Ñuñoa kitchen as before, wooden table surface with subtle grain, warm tungsten lamp pool falling on the page from above, kettle visible blurred in deep background.

Lighting: warm tungsten 3000K key light from above pooling on the page, soft warm fill on her hand, cool dusk-blue rim from the window in deep background, mild volumetric haze, soft contrast, the page itself slightly glowing under the warm light.

Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on hand, slight film grain, warm tungsten + cool dusk color grading, painterly out-of-focus background, premium animated cinematic look, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay (handwritten letters are placeholder, real text added in post), no watermark, no brand logos, no photorealistic skin pores, no anime, no cel-shaded flat, no thriller vignette, no glamour beauty shot, no magenta crystal visible, no turquoise emissive yet, no fast motion, no character drift, no other figures.
```

### Sub-clip escena-06-B (15s) — el chime cyan y el lomo

**Prompt Seedance** (copiable):

```
@Mariela's left hand resting on the page of the small brown A6 leather-bound notebook, the recently written line in handwritten cursive across the page (placeholder squiggles, real text added in post), her hand still and motionless, the pencil set down beside the notebook, the kettle on the stove behind her in deep blurred background.

Action: For the first 8 seconds: her hand stays motionless on the page, only her thumb moves a quarter-millimeter; behind her in deep blurred background the kettle clicks off automatically and a small wisp of steam dissipates; she does not react to it. Then for the final 7 seconds: the camera pushes in very slowly from the page toward the spine of the notebook on the right edge of frame, ending on extreme close-up of the leather spine where a hairline crack runs along the binding; for one barely-perceptible instant the crack emits a thin soft pale-cyan glow then it is gone; she does not see it because the camera is on the spine.

Camera: very slow push-in from tight close-up on hand-and-page to extreme close-up on the notebook spine over 15 seconds, locked horizon, no shake.

Setting: same kitchen, same lighting as previous shot, table grain visible.

Lighting: warm tungsten 3000K key from above as before, but in the final 3 seconds the leather spine itself emits a thin pale-cyan glow (#7FFFD4) along the hairline crack — soft, low intensity, no bloom, almost subliminal; mild volumetric haze unchanged.

Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on leather and hand, slight film grain, warm tungsten + subliminal pale-cyan accent, painterly background, premium animated cinematic look, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay (text added in post), no watermark, no brand logos, no photorealistic, no anime, no cel-shaded flat, no thriller vignette, no fantasy clichés, no large magenta emissive, no fast motion, no character drift, no other figures, no overly bright cyan glow (must be subtle and brief).
```

**Negative prompt** (común a 06-A y 06-B):
```
readable handwriting (placeholder OK, real text composited in post), photorealistic skin, hyperrealistic, anime, cel-shaded, glamour beauty shot, thriller vignette, large magenta crystal in frame, fantasy spell effects, glowing portal, watermark, brand logos, character drift, jittery motion, fast motion, overly intense cyan bloom in spine
```

**Audio** (cubre los 30s entre 06-A y 06-B):
- **Diálogo**: ninguno
- **SFX clave**:
  - 0:00-0:15 (06-A): leve scratch del lápiz sobre papel, respiración contenida de Mariela, pulso de caverna que se sincroniza por un instante con su latido humano y se desvanece
  - 0:15-0:30 (06-B): kettle click off (apagado automático), wisp de vapor, single high cyan-toned chime agudo (un solo hit, descartable como olla del vecino cayendo) sobre el último segundo cuando aparece el glow del lomo
- **Ambient**: cocina silenciosa, tic-tac de reloj lejano, hum residual del bulbo

**Transición a la siguiente escena**:
Hard cut → Escena 07 (caverna, Byte detecta). El salto de cocina silenciosa a caverna con audífono pingeando es el "segundo respiro" del cuento. NO encadenar last-frame.

**Notas de dirección**:
Hinge narrativo del piloto. Riesgo Seedance crítico: texto handwritten legible es 60% confiable — generamos con squiggles placeholder y compositamos la frase exacta "Why did I stop writing here?" en post (After Effects / DaVinci) sobre AMBOS sub-clips. Mismo asset de overlay reutilizado en B14 — tipografía idéntica, posición idéntica, así el viewer reconoce inmediatamente la frase en el cliffhanger. El glow cyan del lomo en B6-B también es post (mask emisivo sobre el crack) si Seedance no lo logra subtle — más confiable así que pedirle al modelo "subtle cyan glow for 1.5 frames".

---

## Escena 07 — Byte detecta la pregunta

- **ID**: `escena-07`
- **Duración**: 15s → 1 clip Seedance
- **Plano(s)**: static medium con Byte foreground / Wiz background, después leve push-in cuando Byte se gira
- **Personajes en frame**: Byte (foreground), Wiz (background)
- **Reference images** (cargar en este orden):
  - `public/images/personajes/byte.png` (character lock principal)
  - `public/images/personajes/wiz.png` (character lock secundario, en plano más lejano)
  - `public/images/portadas/portada2.png` (mood caverna)
- **First frame**: I2V — generá still en Nano Banana o re-usá last-frame de B2 con Byte y Wiz ya iluminados (no más siluetas, ahora vemos sus caras turquesa).

**Prompt Seedance** (copiable):

```
@Byte a young cyclops underground-tribe character with single large central turquoise eye and double specular highlight, smooth turquoise-green skin (#21D8B6), elastic pointed ears, dark purple hoodie with lime-green neon trim, large over-ear neural headphones with bright lime-green LED rings (#A7F432), four-fingered hands, 3.5 head proportions, focused concentrated expression; behind him @Wiz an elder cyclops in deep purple hooded robe with white voluminous beard, leaning on a dark wooden staff topped with magenta-violet crystal, partially in shadow.

Action: For the first 5 seconds: hard cut from previous scene to @Byte's face in medium shot, his elastic ears twitch sharply, his lime-green LED headphones emit a single ping pulse, his single turquoise eye widens. Then for the next 5 seconds: he raises two fingers and presses them against the side of one earcup, listening intently. Then for the final 5 seconds: he turns his head toward @Wiz behind him; @Wiz closes his single eye for one second, opens it, lifts his staff and points it slowly toward an unseen dark passage to his right, but does not move.

Camera: static medium two-shot framed on Byte foreground and Wiz mid-ground, very slight push-in over the final 5 seconds when Byte turns, locked horizon, no shake.

Setting: same Uray Pacha cavern qhocha, the dying magenta crystal still faintly visible in deep background, hundreds of empty stalagmites around, dense atmospheric haze, dust motes catching light.

Lighting: faint magenta crystal emissive from background, lime-green LED glow on Byte's headphones (#A7F432) bouncing onto his cheek and the side of his hoodie, cool turquoise fill from above, deep blue-violet shadows (#0E0820), high contrast bloom on LEDs only, mild volumetric haze.

Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on turquoise skin, slight film grain, magenta-turquoise complementary color grading with lime accent, painterly volumetric background, premium animated cinematic look, 16:9, 15 seconds.

Negative: no cuts (within the 15s, scene starts on hard cut from previous), no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no photorealistic, no anime big-eyes, no cel-shaded flat, no fantasy battle clichés, no extra Pax characters in frame, no character drift, no fast motion, no Wiz speaking yet, no glowing eyes overload.
```

**Negative prompt**:
```
photorealistic, anime big-glossy-eyes, cel-shaded flat, cartoon outlines, fantasy spell effects, lightning, fireball, glowing portal, more than two Pax in frame, character drift, jittery motion, watermark, text overlay, brand logos, fast motion, overly intense LED bloom, Wiz facial movement (he is still and silent except for staff lift)
```

**Audio**:
- **Diálogo**:
  - BYTE (bajo, urgente, factual): "She's pressing the pencil. The question arrived." (~0:06-0:10 del clip, mientras tiene los dedos en el earcup)
- **SFX clave**: ping del audífono lima (un solo hit corto), staff de Wiz golpea piedra una vez (nota clara baja, ~0:13)
- **Ambient**: el sound design vuelve a respirar por primera vez desde B1 — el silencio cavernoso ya no es total

**Transición a la siguiente escena**:
Hard cut a Escena 08-A (extreme close-up de la mano de Mariela apretando el lápiz). Es el primer match-cut del piloto y la regla del universo. NO encadenar last-frame — el corte es el efecto.

**Notas de dirección**:
Primer diálogo Pax del piloto. Línea de Byte obedece la regla Pirahã: cada palabra nombra algo observable (lápiz, presionar, llegó). Riesgo Seedance: lipsync corto de 7 palabras; puede salir limpio o desincronizado. Si sale mal, planificar fallback con Byte parcialmente girado (boca menos visible) y meter dialogue en post. Riesgo Wiz: en background, no se mueve excepto la pupila y el staff — si Seedance le da micromovimientos faciales innecesarios, regenerá.

---

## Escena 08 — Match-cut: el lápiz y la palma

- **ID**: `escena-08`
- **Duración**: 15s totales → **2 sub-clips Seedance: escena-08A (3s) + escena-08B (12s)**
- **Plano(s)**: extreme close-up macro estático en ambos. Sin movimiento de cámara.
- **Personajes en frame**: 08A = Mariela (solo mano izquierda + página). 08B = Wiz (solo palma derecha + ojo en foco suave atrás).
- **Reference images**:
  - 08A: `public/images/personajes/mariela.png`
  - 08B: `public/images/personajes/wiz.png` + `public/images/portadas/portada2.png`
- **First frame**: I2V para ambos. Para 08A, last-frame de B7 NO sirve (estamos en cocina) — generar still de mano apretando lápiz. Para 08B, generar still de palma de Wiz vacía.

### Sub-clip escena-08A (3s) — mano apretando el lápiz

> **Nota:** Seedance genera nativo en 15s, no en 3s. Generamos un clip de 15s donde los primeros 3s son el contenido y los últimos 12s son hold cuasi-estático del mismo frame; el editor corta a 3s. Alternativa más simple: generar el clip de 15s, en post recortar los primeros 3s, descartar el resto.

**Prompt Seedance** (copiable):

```
Extreme macro close-up of @Mariela's left hand, a 36-year-old Latin-American woman's hand with naturalistic stylized softened skin tones, fingers gripping a wooden pencil firmly enough that the lead leaves a visible pressure-mark dent in the paper below; the pencil is pressed against the page of a small brown A6 leather-bound notebook open on a wooden kitchen table, the page showing the recently written cursive line "Why did I stop writing here?" (placeholder squiggles, real text in post) immediately above the pencil tip; a single grain of graphite catches the warm tungsten light at the pencil tip.

Action: For the first 3 seconds: the hand holds the pencil pressed against the page, the lead-mark dent visible, the hand trembles a quarter-millimeter once, the graphite grain glints. Then for the final 12 seconds: the hand holds nearly motionless, only the warm tungsten light slowly shifting on the wooden surface, the editor will use only the first 3 seconds of this generation.

Camera: static extreme macro close-up, locked tripod, no zoom, no movement, no shake.

Setting: same small Ñuñoa kitchen as before, wooden table surface with subtle grain, page of the notebook visible in frame.

Lighting: warm tungsten 3000K key light from above pooling on the page and hand, soft warm fill, deep dusk-blue shadows in negative space, mild volumetric haze, the graphite grain catches a tiny specular highlight.

Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on hand, slight film grain, warm tungsten color grading, painterly background, premium animated cinematic look, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay (placeholder squiggles, real text composited in post), no watermark, no brand logos, no photorealistic skin pores, no anime, no cel-shaded flat, no fast motion, no character drift, no magenta or turquoise emissive, no fantasy elements.
```

### Sub-clip escena-08B (12s) — palma de Wiz, formación del cristal

> **Nota:** misma lógica — generar 15s, recortar a 12s en post, o generar full 15s y mantener un 3s pad de "palma con cristal asentado" al final.

**Prompt Seedance** (copiable):

```
Extreme macro close-up of @Wiz's right palm, an elder cyclops's open hand with weathered four-fingered turquoise-green skin (#21D8B6), faint subsurface scattering, the palm fully open and empty in the dark of the Uray Pacha cavern, his single droopy-lidded turquoise eye visible in soft focus behind the palm watching the empty hand intently.

Action: For the first 2 seconds: the palm is empty, only the soft cavern ambient light visible on it, total silence. Then for the next 4 seconds: above the palm, out of nothing, a small dense magenta crystal materializes — appearing in formation, the air shimmers and the crystal solidifies in real time, freshly formed, glowing magenta from within (#E83FC8 rim, #FF49B4 core). Then for the next 4 seconds: the new crystal pulses bright once, settles, then floats two centimeters above his skin, slowly rotating; the camera holds; @Wiz's eye in soft focus behind watches it. Then for the final 5 seconds: the crystal continues to float and pulse softly, the palm and eye unchanged, the editor will use only up to the 12th second.

Camera: static extreme macro close-up, locked tripod, no zoom, no movement, no shake.

Setting: deep Uray Pacha cavern background, completely dark except for the new crystal's emissive light, hairline cavern texture barely visible behind in deep blur.

Lighting: the new magenta crystal as the only emissive (rim #E83FC8, core #FF49B4) lighting the palm and Wiz's eye from below, deep blue-violet shadows (#0E0820) everywhere else, high contrast, bloom on emissive crystal only, mild volumetric haze.

Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on turquoise skin and on the crystal, slight film grain, magenta-turquoise complementary color grading, painterly background, premium animated cinematic look, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no photorealistic, no anime, no cel-shaded flat, no fantasy battle clichés, no glowing portal, no magic circle, no lightning, no extra crystals, no character drift, no fast motion, no other figures in frame, no fingers closing on crystal yet (closes only in scene 9).
```

**Negative prompt** (común 08A + 08B):
```
photorealistic, hyperrealistic, anime, cel-shaded, fantasy magic circle, glowing portal, lightning, fireball, brand logos, watermark, text overlay (real text composited in post), more than one crystal, character drift, jittery motion, fast motion, abrupt formation flash, overly intense bloom
```

**Audio** (cubre 0-15s del beat):
- **Diálogo**: ninguno
- **SFX clave**:
  - 08A (0-3s): silencio de cocina, presión del lápiz contra el papel apenas audible, paper crackle muy leve
  - HARD CUT: 1 frame de silencio total (≈42ms a 24fps)
  - 08B (3-15s del beat): sonido de formación del cristal — panel de vidrio enfriándose con tono cálido por debajo, pulse magenta cuando estalla brillante, después drone bajo sostenido mientras flota
- **Ambient**: nada de música. Es sonido puro.

**Transición a la siguiente escena**:
Continuous → Escena 09 (mismo plano pero más abierto). Last-frame de 08B (palma con cristal flotando) es first-frame de B9.

**Notas de dirección**:
**Bisagra del piloto.** El match-cut es el efecto entero — no hay nada entre los dos planos. NUNCA prompt a Seedance "Mariela's hand and Wiz's hand in one clip" — los promediaría. Son DOS prompts, DOS generaciones, UN cut en editor. Riesgo Seedance principal: la formación del cristal "out of nothing" puede salir como flash espontáneo poco creíble; pedir explícitamente "shimmer/solidify in real time" y tener listo regenerar 3-4 veces hasta que se sienta orgánico. Cyril el editor: el frame de silencio absoluto entre 08A y 08B es **load-bearing** — no lo cubras con un sting musical.

---

## Escena 09 — Wiz reconoce, Jiggy y Luxa cargan

- **ID**: `escena-09`
- **Duración**: 15s → 1 clip Seedance (con fallback a 2 micro-shots si falla)
- **Plano(s)**: static medium en Wiz, Jiggy entra de izquierda, Luxa entra de derecha, Jiggy sale
- **Personajes en frame**: Wiz, Jiggy, Luxa (3 figuras Pax — riesgo medio)
- **Reference images** (cargar en este orden):
  - `public/images/personajes/wiz.png` (lock principal, en frame todo el clip)
  - `public/images/personajes/jiggy.png` (lock — entra a los 5s)
  - `public/images/personajes/luxa.png` (lock — entra a los 9s, debut visual)
  - `public/images/portadas/portada2.png` (mood caverna)
- **First frame**: I2V con last-frame de B8B (palma de Wiz con cristal flotando). Crítico: este es Luxa's debut, el char-sheet textual de ella debe estar 100% literal.

**Prompt Seedance** (copiable):

```
@Wiz an elder cyclops in deep purple hooded robe with white voluminous beard, leaning on a dark wooden staff with magenta-violet crystal, his right palm open with a freshly-formed small dense magenta crystal floating two centimeters above the skin pulsing softly; tight on his face and palm in the dark of the Uray Pacha cavern; one slow tear rolls from the corner of his single eye, catches in his white beard, falls.

Action: For the first 5 seconds: @Wiz's eye holds the crystal, a single tear rolls down through his beard, he whispers almost as an exhale, then closes his fingers around the new magenta crystal and presses it briefly to his chest. Then for the next 5 seconds: @Jiggy a small cyclops chasqui-runner with smooth turquoise-green skin (#21D8B6), single large central eye, brown-red leather chest harness with metal buckle, leather satchel at hip, no headwear, 3.5 head proportions, enters frame from the left already in motion ready to run, raises his open right hand, @Wiz without breaking eye contact places the new magenta crystal into @Jiggy's right palm. Then for the final 5 seconds: @Luxa a slender cyclops with single large cyan-turquoise eye, faint luminous turquoise-green skin, purple headband with hanging ends, multicolor tribal-patterned poncho with purple-gold-turquoise-magenta geometry, enters silently from the right holding up a golden-yellow warm crystal (#FFE34D core, #D4A52B deep), without slowing she presses the gold crystal into @Jiggy's left palm and vanishes back into the dark; @Jiggy is already turning toward an unseen tunnel — magenta in his right hand, gold in his left — and exits frame.

Camera: static medium shot framed wide enough to fit three figures in sequence, very slight handheld settle, locked horizon, no zoom, no shake.

Setting: same Uray Pacha qhocha as scene 8B, deep cavern background, faint hairline cavern texture, dense atmospheric haze.

Lighting: the new magenta crystal as primary emissive (#E83FC8 rim, #FF49B4 core) lighting Wiz's face and palm and Jiggy's hands, faint cyan ambient fill from above, when Luxa enters her golden crystal adds a warm gold pocket (#FFE34D) for 3 seconds blending magenta-cool with warm-gold contrast on Jiggy, deep blue-violet shadows.

Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on all turquoise skin and on the crystals, slight film grain, magenta-turquoise complementary color grading with brief warm-gold visitor accent, painterly volumetric background, premium animated cinematic look, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no photorealistic, no anime, no cel-shaded flat, no fantasy battle clichés, no glowing portal, no extra Pax characters beyond Wiz Jiggy Luxa, no character drift on three faces, no fast motion, no Luxa speaking, no melodramatic poses.
```

**Negative prompt**:
```
photorealistic, anime big-glossy-eyes, cel-shaded flat, fantasy magic circles, lightning, glowing portals, more than three Pax in frame, character drift on Wiz / Jiggy / Luxa faces, jittery motion, watermark, text overlay, brand logos, fast motion, overly bright crystal bloom, characters touching or overlapping in a way that triggers amalgamation glitch, melodramatic tears
```

**Audio**:
- **Diálogo**:
  - WIZ (bajo, casi para sí, almost an exhale): "Still warm. Should burn me — and it doesn't." (~0:02-0:05 del clip)
- **SFX clave**: respiración audible de Wiz, pasos de Luxa apenas un roce de tela (silenciosos, no impacto), primera zancada de Jiggy hace sonar un latido del pulso de la caverna ligeramente más fuerte
- **Ambient**: caverna respirando, score sustains una nota baja warm

**Transición a la siguiente escena**:
Hard cut → Escena 10 (Av. Bilbao, calle nocturna, paleta urbana). El salto de caverna mágica a calle urbana mundana es deliberado.

**Notas de dirección**:
3 figuras Pax en mismo plate = riesgo amalgamation glitch (se tocan o superponen → caras se promedian). **Fallback documentado:** si Seedance falla 3 generaciones seguidas con drift en cara, partir en 2 micro-shots: (a) Wiz tear + línea + cierra dedos sobre cristal (~6s); (b) Jiggy entra, recibe magenta, Luxa intercepta gold, Jiggy sale (~9s). Editor cose. Coreografía clave: Jiggy entra por izquierda, Luxa por derecha, NO se tocan entre ellas, solo tocan a Jiggy en momentos distintos. Si Seedance hace que Wiz y Luxa se toquen, regenerá. Lipsync Wiz: línea de 8 palabras, casi un susurro — boca apenas se abre, low-risk lipsync. Si falla, fallback con boca semi-tapada por la barba.

---

## Escena 10 — El cruce a la superficie

- **ID**: `escena-10`
- **Duración**: 15s → 1 clip Seedance
- **Plano(s)**: low-angle wide bajo la rejilla, después static medium en Jiggy, drones drift visible en upper third
- **Personajes en frame**: Jiggy (foreground bajo rejilla), Zek (background dentro del túnel), 2 drones (upper third, sobre la calle)
- **Reference images** (cargar en este orden):
  - `public/images/personajes/jiggy.png` (lock)
  - `public/images/personajes/zek.png` (lock — background del túnel)
- **First frame**: I2V con still pre-renderizado de Jiggy bajo la rejilla mirando arriba con cristales en cada mano. NO usar last-frame de B9 (cambio de escena).

**Prompt Seedance** (copiable):

```
@Jiggy a small cyclops chasqui-runner with smooth turquoise-green skin (#21D8B6), single large central turquoise eye, brown-red leather chest harness with metal buckle, leather satchel at hip, four-fingered hands, the new magenta crystal closed in his right fist glowing magenta through the gaps between fingers, the warm golden-yellow crystal (#FFE34D) cupped in his open left palm; he stands in a sliver of darkness just below a rectangular storm-drain grate at street level on a Santiago Ñuñoa avenue at night around 10 PM; behind him deeper in the tunnel @Zek a cyclops in tilted purple cap with retro analog boombox at his hip stands quietly. Three stories above through the grate, two small black spherical antibody-drones with magenta LED indicators drift on a slow patrol pattern across an empty sodium-lit street.

Action: For the first 5 seconds: @Jiggy looks up through the grate at the drones, the nearest drone's magenta LED begins to swing toward the grate. Then for the next 5 seconds: without taking his eyes off the drones, @Jiggy brushes the surface of the golden crystal once with his left thumb; the gold pulses almost imperceptibly. Then for the final 5 seconds: the two nearest drones drift exactly 30 degrees off-axis — not fleeing, not reacting in fear, simply re-pathing their patrol as if their scan-target had shifted; they continue oblivious; behind @Jiggy in the tunnel, @Zek taps his boombox once and a single low pulse vibrates through the tunnel air; @Jiggy syncs his breathing to it, climbs up through the grate, and disappears.

Camera: low-angle wide static framed from below the grate looking up, then very slight push-in on @Jiggy in the second half, locked horizon, no shake.

Setting: storm-drain grate beneath a streetlamp on Av. Bilbao Ñuñoa Santiago around 10 PM, empty avenue above visible through the grate bars, sodium streetlamp pool of orange light (#FF8A30) on the asphalt above, tunnel interior dark and damp below, faint mineral residue on the tunnel walls.

Lighting: sodium streetlamp orange (#FF8A30) on the street level above, deep blue night-sky negative space, two drone magenta LEDs (#E83FC8) sweeping slowly, magenta crystal glow leaking through Jiggy's right fist, warm gold glow (#FFE34D) from his left palm, deep blue-violet tunnel shadows below, mild atmospheric haze and slight humidity, sodium light hazing through the grate bars.

Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on turquoise skin, slight film grain, urban night sodium-orange + magenta-cool drone palette + warm gold accent on Jiggy's left hand, painterly background, premium animated cinematic look, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no photorealistic, no anime, no cel-shaded flat, no fantasy battle clichés, no menacing thriller drone sound or visual treatment, no drones fleeing in fear, no drones exploding, no aggressive drone reaction, no fast motion, no character drift, no Zek leaving the tunnel, no extra figures.
```

**Negative prompt**:
```
photorealistic, anime, cel-shaded flat, thriller vignette, menacing villain drones, drones in fear, drones exploding, drones attacking, lightning, fireball, glowing portal, magic circle, more than two drones, character drift on Jiggy or Zek, jittery motion, watermark, text overlay, brand logos on drones, fast motion, Zek exiting tunnel, glamour beauty shot, drone aggressive turn
```

**Audio**:
- **Diálogo**: ninguno
- **SFX clave**: drone hum mecánico (utilitario, NO amenazante), sub-tone shift cuando el dorado pulsa (frecuencia que sale del aire, casi subliminal), boombox tap (subwoofer al otro lado de una pared, felt-not-heard)
- **Ambient**: brisa mínima de calle nocturna vacía, sodium streetlamp ballast hum bajo

**Transición a la siguiente escena**:
Hard cut → Escena 11 (cocina Mariela, Jiggy ya dentro). El salto cubre el "cruce" implícito.

**Notas de dirección**:
**Riesgo prompt-engineering CRÍTICO:** la palabra "drones" es semánticamente cargada con threat/villain. Hay que insistir en negative ("not menacing, not fleeing, simply re-pathing") y en positive ("oblivious", "system re-pathing"). Si Seedance hace que los drones giren agresivamente o cambien color de LED, regenerá — el tono se rompe. La regla mágica del dorado se demuestra en 2 segundos sin línea de diálogo. El thumb-brush del cristal es el gesto crítico — si Seedance lo dropea, regenerá. Riesgo Zek: solo el brim de gorra y el tap del boombox son su lectura — si está más visible que eso, OK; si está menos, OK.

---

## Escena 11 — La entrega invisible

- **ID**: `escena-11`
- **Duración**: 15s → 1 clip Seedance
- **Plano(s)**: slow dolly-in de medium-wide (cocina con Mariela y refri en frame) a medium close (mano de Mariela y mano de Jiggy)
- **Personajes en frame**: Mariela (sentada, sin verlo), Jiggy (aparece desde detrás del refri, real para la cámara, invisible para ella)
- **Reference images** (cargar en este orden):
  - `public/images/personajes/mariela.png` (lock)
  - `public/images/personajes/jiggy.png` (lock)
  - `public/images/portadas/portada2.png` (mood — opcional, paleta de Jiggy)
- **First frame**: I2V con first-frame externo OBLIGATORIO. Generá en Nano Banana el frame inicial con Mariela sentada en la cocina + Jiggy emergiendo apenas detrás del refri, con el dual rim-light correcto (magenta izq / tungsten der). Esto es el clip más delicado del piloto en términos de paleta.

**Prompt Seedance** (copiable):

```
@Mariela a 36-year-old Latin-American woman seated at a small wooden kitchen table with the open brown leather A6 notebook in front of her, her left hand resting on the table beside the notebook, a mug of cold tea beside her, brown hair in low ponytail, thin metal-framed glasses, soft tired expression; @Jiggy a small cyclops chasqui-runner with smooth turquoise-green skin (#21D8B6), single large central eye, brown-red leather chest harness, four-fingered hands, the small new magenta crystal in his right palm, emerges from behind the refrigerator behind her — invisible to her but fully real to the camera. Jiggy receives a dual rim light: thin magenta rim (#E83FC8) on his left side from his own crystal aura, and warm tungsten rim (#FFD08A 3000K) on his right side catching the kitchen's hanging-bulb fall-off — the two rim-lights blend along his shoulder so he reads as belonging in this room, not as a CG paste-in.

Action: For the first 5 seconds: @Mariela starts to reach forward to close the notebook; @Jiggy moves with the calm of someone delivering something heavy and small, approaching her left hand from behind. Then for the next 5 seconds: @Jiggy opens his right palm carrying the magenta crystal and gently presses it against the back of @Mariela's left hand resting on the table; her hand twitches once. Then for the final 5 seconds: @Mariela slowly lifts her left hand, looks at it, sees nothing visible there but her face shifts — a tiny surprised softening; she brings her palm closer to her chest, holds it; @Jiggy is already gone — having stepped back behind the refrigerator out of frame.

Camera: very slow dolly-in from medium-wide framing of the whole kitchen with Mariela seated and refrigerator visible to medium close-up on her hand and chest area over 15 seconds, locked horizon, no shake.

Setting: same small Ñuñoa kitchen as scenes 5 and 6, wooden table, open notebook with the recently written line, cold mug of tea, single warm tungsten Edison hanging bulb, refrigerator on the left side of frame, dusk-blue light from the window, ceramic tile floor.

Lighting: warm tungsten 3000K (#FFD08A) primary key from the hanging bulb pooling on the table and on Mariela's face, cool dusk-blue 5500K fill from the window on her left, on @Jiggy specifically a dual rim light setup — magenta rim (#E83FC8) on his left side from his crystal's emissive, warm tungsten rim (#FFD08A) on his right side from the room — the two rim-lights blend into a single warm-cool integrated outline along his shoulder and arm; mild volumetric haze, warm pool around the bulb.

Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on both Mariela's softened human skin and Jiggy's turquoise skin, slight film grain, warm-tungsten + cool-dusk + magenta-rim integrated palette negotiation, painterly background, premium animated cinematic look, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no photorealistic, no anime, no cel-shaded flat, no Mariela seeing Jiggy, no Mariela reacting visibly to Jiggy's presence, no Jiggy looking like a CG paste-in, no flat key light on Jiggy with no warm wrap, no saturated turquoise skin against warm walls without rim integration, no fast motion, no character drift, no other Pax characters in frame, no glowing portal, no fantasy effects.
```

**Negative prompt**:
```
photorealistic, anime, cel-shaded flat, glamour beauty shot, thriller vignette, Mariela seeing Jiggy, Mariela reacting visibly, Jiggy paste-in look, flat key light on Jiggy, character ghosting, more than 2 figures, character drift, jittery motion, watermark, text overlay, brand logos, fast motion, glowing portals, magic circles, fantasy effects
```

**Audio**:
- **Diálogo**: ninguno
- **SFX clave**: tic-tac de reloj de pared, TV del vecino al otro lado del muro (apenas audible, voces ininteligibles), sonido del cristal de B8B apenas presente como recuerdo (whisper-level)
- **Ambient**: cocina silenciosa, ningún score (silencio total con sólo foleys ambientales)

**Transición a la siguiente escena**:
Continuous → Escena 12 (mismo encuadre, Jiggy ya se fue, Mariela cierra los dedos sobre el calorcito). Encadenar last-frame.

**Notas de dirección**:
**Beat más delicado del piloto en paleta — única escena donde Pax-palette y Kay-palette comparten plate.** Image contract: Jiggy debe verse iluminado por la cocina, NO pegado encima. Si el primer pase sale "paste-in" (turquesa saturada plana contra paredes cálidas), regenerá con énfasis en "magenta rim left + tungsten rim right blended". Riesgo Seedance específico: puede hacer que Mariela mire a Jiggy — eso ROMPE el beat. Si lo hace, regenerá inmediato. La cara de Mariela debe pasar de neutral a "tiny softening" sin que ella mire para abajo a su mano hasta el segundo 8. Lipsync: cero diálogo, low-risk.

---

## Escena 12 — "Okay"

- **ID**: `escena-12`
- **Duración**: 15s → 1 clip Seedance
- **Plano(s)**: static medium en Mariela, después leve push-in cuando dice "okay"
- **Personajes en frame**: Mariela
- **Reference images** (cargar en este orden):
  - `public/images/personajes/mariela.png` (lock)
- **First frame**: I2V con last-frame de B11 (Mariela con la mano sobre el pecho).

**Prompt Seedance** (copiable):

```
@Mariela a 36-year-old Latin-American woman, brown hair in low ponytail, thin metal-framed glasses, sober blouse, softened stylized human proportions, seated at the small wooden kitchen table, her left hand closed gently over her chest holding an invisible warmth, the open notebook visible on the table with the recently written line on the page, a mug of cold tea beside her, the kettle on the stove behind her in soft focus.

Action: For the first 5 seconds: @Mariela closes her fingers over the warmth on her chest, looks at the notebook page at her own handwriting; her face does not break — something smaller and more real than crying happens — the corners of her mouth move half a centimeter upward then settle. Then for the next 5 seconds: she stands, picks up the mug of cold tea, walks to the sink and pours it out, then refills the kettle from the tap and places it back on the stove turning the gas on. Then for the final 5 seconds: she walks back to the chair and sits down again, does not open the notebook again, just sits, exhales softly, says one word almost inaudible.

Camera: static medium shot framed on Mariela seated at the table, very slight push-in over the final 5 seconds when she returns to sit, locked horizon, no shake.

Setting: same Ñuñoa kitchen, wooden table, ceramic tile floor, single warm tungsten Edison bulb, sink visible on the right side of frame, dusk-blue light from the window now darker (later in the night).

Lighting: warm tungsten 3000K key light from the hanging bulb, cool dusk-blue fill from the window now slightly darker (later evening), mild volumetric haze, warm pool around the bulb, slightly warmer overall grade than scenes 5-6 — this is the first major-key emotional moment of the episode.

Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on softened human skin, slight film grain, warm-tungsten dominant color grading with subtle warmer push (first major key moment of the episode), painterly background, premium animated cinematic look, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no photorealistic skin pores, no anime, no cel-shaded flat, no thriller vignette, no glamour beauty shot with shallow DOF, no Pax characters in frame, no magenta crystal visible, no turquoise emissive, no fantasy elements, no fast motion, no character drift, no melodramatic crying, no big smile (only half-centimeter mouth corner movement).
```

**Negative prompt**:
```
photorealistic, hyperrealistic, anime, cel-shaded, thriller vignette, glamour beauty shot, shallow DOF cinematic blur, Pax characters in frame, magenta crystal, turquoise emissive, fantasy elements, character drift on Mariela, jittery motion, watermark, text overlay, brand logos, fast motion, melodramatic crying, big smile, exaggerated facial expression
```

**Audio**:
- **Diálogo**:
  - MARIELA (a nadie, casi inaudible): "...okay." (~0:13-0:14 del clip, justo cuando se sienta)
- **SFX clave**: agua llenando la pava, click del gas, hum de la pava empezando a calentar, **un único acorde cálido sostenido** (primer momento en tono mayor del episodio — entra a los 0:08 y sostiene hasta el final)
- **Ambient**: cocina silenciosa, tic-tac de reloj

**Transición a la siguiente escena**:
Hard cut → Escena 13 (caverna Uray Pacha, qhocha más viva). El acorde mayor sostiene a través del corte y se transforma en el score warm de B13.

**Notas de dirección**:
La transformación de Mariela en una sílaba. Riesgo Seedance: puede sobre-actuar la sonrisa o hacerla llorar. Énfasis en negative: "no melodramatic crying, no big smile, only half-centimeter mouth corner movement". Lipsync: 1 palabra ("okay"), low-risk pero crítico — si falla, fallback con cara semi-girada.

---

## Escena 13 — Wiz y Jiggy abajo: "esta se queda"

- **ID**: `escena-13`
- **Duración**: 15s → 1 clip Seedance (B13A) + insert post-prod ≈80ms (B13B, NO Seedance)
- **Plano(s)**: slow descending crane / dolly-down a lo largo de la silueta de Wiz desde atrás, después static cuando Jiggy entra
- **Personajes en frame**: Wiz (de espaldas parcial al inicio, después se gira), Jiggy (entra corriendo a los ~7s)
- **Reference images** (cargar en este orden):
  - `public/images/personajes/wiz.png` (lock)
  - `public/images/personajes/jiggy.png` (lock)
  - `public/images/portadas/portada2.png` (mood)
- **First frame**: I2V con still pre-renderizado de Wiz de espaldas observando la wayra-current.

**Prompt Seedance** (copiable):

```
@Wiz an elder cyclops in deep purple hooded robe, white voluminous beard, dark wooden staff with magenta-violet crystal, standing with his back partly to camera observing a wayra-current — fine motes of dust spiraling slowly upward through a hairline crack in the cavern ceiling, a near-invisible pressure shift in the air; the qhocha is the same Uray Pacha cavern as before but visibly less dead now: two of the empty stalagmites nearest Wiz have begun to glow faintly magenta, just two, tiny, but clearly more alive than before.

Action: For the first 7 seconds: the camera slowly descends along @Wiz's silhouette from behind — the deep purple robe, the staff, the back of the white-bearded head — observing the upward-spiraling wayra dust; he stands silent, watching the air. Then for the next 4 seconds: @Jiggy a small cyclops chasqui-runner with turquoise-green skin and brown-red leather harness runs into the qhocha breathing hard, no crystal in hand (he delivered it), no gold crystal visible (consumed or pocketed off-screen); he stops in front of @Wiz panting; @Wiz turns slowly to face @Jiggy. Then for the final 4 seconds: @Wiz looks at @Jiggy and replies; around them the two faintly-glowing stalagmites pulse softly magenta — the cavern is starting to breathe again.

Camera: slow descending crane along Wiz's back silhouette for first 7 seconds, then static medium two-shot for the remaining 8 seconds, locked horizon, no shake.

Setting: Uray Pacha qhocha, cavern visibly slightly more alive than scene 2 — two stalagmites near Wiz emit faint magenta glow, hairline ceiling crack with thin upward dust spiral (wayra-current), dense atmospheric haze, mineral cavern walls.

Lighting: warm magenta from the two newly-glowing stalagmites near Wiz, soft cyan ambient from above, deep blue-violet shadows (#0E0820), thin pale-cyan shaft from ceiling crack catching the spiral dust, mild volumetric haze, the cavern noticeably brighter than the cold open even though still dim, no other emissives.

Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on turquoise skin and on Wiz's beard, slight film grain, magenta-turquoise complementary color grading slightly warmer than scenes 1-2, painterly volumetric background, premium animated cinematic look, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no photorealistic, no anime, no cel-shaded flat, no fantasy battle clichés, no glowing portal, no extra crystals visible, no pocket close-up, no second crystal in Wiz's hand or robe, no extra Pax characters beyond Wiz and Jiggy, no character drift, no fast motion, no aggressive cavern light bloom, no melodramatic poses.
```

**Negative prompt**:
```
photorealistic, anime, cel-shaded, fantasy magic circles, glowing portal, lightning, second crystal in Wiz's pocket or hand (post-production insert handles this), pocket close-up, more than 2 Pax in frame, character drift, jittery motion, watermark, text overlay, brand logos, fast motion, overly bright stalagmite bloom, melodramatic poses
```

**Audio**:
- **Diálogo**:
  - JIGGY (recuperando aire): "Do I pass it to the next runner?" (~0:11-0:13 del clip, después de frenar frente a Wiz)
  - WIZ (girando lento, mirándolo): "Wait. This one stays a while." (~0:13-0:15 del clip)
- **SFX clave**: brisa wayra apenas audible (whisper-level), pulso de caverna ahora suena casi como un latido normal (no más arrítmico), score crece suave warm — no triunfal
- **Ambient**: caverna respirando, dust motes spiral

**Transición a la siguiente escena**:
Hard cut → Escena 14 (cocina vacía, libreta brillando). El cello vuelve y se sincroniza con el pulso de la página.

**Notas de dirección**:
**INSERTO TÉCNICO POST-PROD (B13B):** a los 7.0s del clip B13A (entre "Wait." y "This one stays a while.") se inserta en post 2 frames a 24fps (≈83ms) de un extreme close-up del INTERIOR del bolsillo izquierdo de la túnica de Wiz, mostrando un segundo cristal pale-dusty-gold (#D9C28A, low saturation) ~60% del tamaño del magenta nuevo, con el meñique de Wiz rozando su superficie. **NO se genera con Seedance** — es ilustración manual o still pre-renderizado, compositado en Premiere/DaVinci/AE matcheando el LUT de B13A. Source asset lo provee `pax-visual-designer`. Riesgo Seedance B13A: que el modelo "sume" un cristal en el bolsillo o en la mano de Wiz sin pedirlo (Seedance tiende a "rellenar"). Negative prompt es explícito; si igual lo mete, regenerá. Lipsync Wiz+Jiggy: dos líneas cortas, low-risk; si falla, planificar fallback con planos donde la boca de Wiz quede semi-tapada por la barba.

---

## Escena 14 — La libreta brilla sola

- **ID**: `escena-14`
- **Duración**: 15s → 1 clip Seedance
- **Plano(s)**: very slow dolly-in / push-in sobre la libreta abierta, después static hold sobre la página, fade a negro
- **Personajes en frame**: ninguno (cocina vacía, Mariela duerme fuera de plano)
- **Reference images** (cargar en este orden):
  - `public/images/portadas/portada2.png` (mood — opcional, paleta general)
- **First frame**: I2V con first-frame externo OBLIGATORIO. Generá en Nano Banana el still de la cocina vacía con la libreta abierta, segunda taza vacía al lado de la pava, luz de la mesa encendida, franja de luz bajo puerta del dormitorio. Esto fija el cliffhanger.

**Prompt Seedance** (copiable):

```
A small empty Ñuñoa kitchen at night, the small wooden kitchen table in the center of frame, the open brown leather A6 notebook lying flat on the table page-up showing the recently written cursive line (placeholder squiggles, real text composited in post matching scene 6), a second drained ceramic mug of tea beside the kettle on the stove indicating she had a second cup, the warm tungsten Edison hanging bulb still on above the table, a thin band of soft yellow light spilling under a closed bedroom door at the edge of frame indicating Mariela is asleep beyond the door, ceramic tile floor, no figures in frame.

Action: For the first 12 seconds: the camera slowly pushes in from medium-wide of the whole kitchen to extreme close-up on the page of the notebook over 12 seconds, the handwritten line on the page slowly becoming the full frame; as the camera approaches, the handwritten line starts to glow softly pale-cyan (#7FFFD4) — only the line, not the rest of the page — pulsing slowly, alive, like a heartbeat, the glow building gradually. Then for the final 3 seconds: hold on the close-up of the glowing handwritten line pulsing once more, then fade to black.

Camera: very slow dolly-in / push-in from medium-wide of the kitchen to extreme close-up on the notebook page over 12 seconds, then 3-second static hold and fade to black, locked horizon, no shake.

Setting: same Ñuñoa kitchen as scenes 5-6-11-12, now empty and quiet at late night, slight increase in ambient cool shadows, warm tungsten still on, second mug visible by the kettle, closed bedroom door at edge of frame with thin yellow band of light underneath.

Lighting: warm tungsten 3000K from hanging bulb pooling on the table, cool dusk-blue ambient in the corners, in the final 8 seconds the handwritten line begins emitting a pale-cyan glow (#7FFFD4) from within the page itself, soft and pulsing, no harsh bloom, no aggressive emissive, just a gentle living-cyan glow on the letterforms; mild volumetric haze, the rest of the page remains lit only by tungsten.

Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on leather and paper, slight film grain, warm tungsten + subliminal pale-cyan accent on text, painterly background, premium animated cinematic look, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay (handwritten letterforms are placeholder, real text composited in post matching scene 6 exactly), no watermark, no brand logos, no photorealistic, no anime, no cel-shaded flat, no thriller vignette, no glamour beauty shot, no glowing portal, no magenta crystal visible, no other emissives beyond the cyan line, no characters in frame, no fast motion, no aggressive cyan bloom, no UI-style square-wave blink (the pulse is smooth heartbeat sine, not square).
```

**Negative prompt**:
```
photorealistic, hyperrealistic, anime, cel-shaded flat, thriller vignette, glamour beauty shot, glowing portal, magic circle, magenta crystal, characters in frame, jittery motion, watermark, text overlay (real text in post), brand logos, fast motion, square-wave UI blink, overly bright cyan bloom, loading-screen pulse, frame skip
```

**Audio**:
- **Diálogo**: ninguno
- **SFX clave**: una nota baja de cello — la misma del cold open B1 — entra a los 0:02 y sostiene; el pulso de la caverna y el pulso de la página son el mismo ritmo ahora y se sincronizan UNA vez (~0:10) de manera audible, después silencio total los últimos 2-3 segundos antes del fade
- **Ambient**: cocina silenciosa, tic-tac de reloj cada vez más distante, brisa apenas en ventana

**Transición a la siguiente escena**:
Fade to black → end card (PAX logo + "the wind starts somewhere"). End card va en post, no en Seedance.

**Notas de dirección**:
Cliffhanger. **El glow cyan de la frase es el simbolo del episodio entero en un solo plano** — la legibilidad del texto handwritten es load-bearing, el viewer DEBE leer "Why did I stop writing here?" y reconocerlo de B6. Asset post-prod: el MISMO overlay handwritten usado en B6 (same typography, same handwriting, same position) compuesto sobre este plate. El glow cyan también va en post como mask emisivo sobre las letras del overlay — más confiable que pedir a Seedance "glowing handwritten cyan English text". Riesgo Seedance: que renderice la frase con squiggles distintos a B6 — no importa, los reemplaza el overlay. Riesgo grave: que Seedance haga un "loading screen blinking pulse" en vez de heartbeat sine smooth — negative prompt es explícito.

---

## Resumen final

- **Total clips Seedance:** 16 generaciones narrativas (14 escenas + 1 sub-prompt extra escena-06 + 1 sub-prompt extra escena-08).
- **Generaciones adicionales:** 3 seed-clips de identidad (Jiggy, Wiz, Mariela) — recomendado generar antes de los 16 narrativos.
- **Inserto post-prod (NO Seedance):** B13B, 2 frames ≈83ms, asset ilustrado a mano por `pax-visual-designer`.
- **Compositados post-prod:** handwritten overlay "Why did I stop writing here?" reutilizado en B6 + B14, glow cyan emisivo sobre letras en B6-B + B14, y el insert B13B.
- **Total duración generada:** 14 escenas × 15s = 3:30 + Escena 06 segundo sub-clip 15s = 3:45.
