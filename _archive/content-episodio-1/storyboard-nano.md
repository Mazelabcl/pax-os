---
title: Storyboard — Prompts Nano Banana
description: Prompts image-to-image por escena para generar el storyboard visual del episodio 1
tool: Nano Banana (Gemini Image)
---

## Como usar estos prompts

- Cada escena declara una tabla **Reference images requeridas** con slots `@image1`, `@image2`, `@image3`, etc. Subi las imagenes a Nano Banana **en ese orden exacto** — el slot 1 es siempre el character lock principal de la escena.
- En el prompt copiable referenciamos los slots literalmente como `@image1`, `@image2`, etc., para que el modelo sepa que cada referencia aporta (character vs mood vs concept de locacion).
- **Orden de slots**: `@image1` = character lock principal. `@image2` = segundo character lock si hay 2 personajes (si no, mood reference). Despues mood references (portadas). Despues concept arts de locacion.
- **Concept arts faltantes (TBD)**: si una escena necesita un asset que NO existe en `public/images/personajes/` o `public/images/portadas/`, se declara con un ID estable (ej. `concept-room-jiggy-dawn`) y el prompt lo referencia igual con `@imageN` — aldot debe generar primero ese concept con Nano Banana usando el archivo `concept-arts.md` y subirlo en el slot correspondiente al correr el prompt de la escena.
- **Iteracion en dos pasos**: primer pass con denoise alto (~0.7) para fijar composicion y encuadre; segundo pass con denoise bajo (~0.25-0.35) usando el resultado anterior + la reference de personaje para clavar el character lock sin que mute el shading del style-guide.
- **Aspect ratio canonico: 16:9** en todos los prompts. No cambiar — el piloto entero es 16:9.
- El bloque **Style-lock** (seccion siguiente) ya viene incluido al inicio de cada "Prompt visual" copiable. Si Nano Banana soporta system instructions persistentes, pegalo una sola vez ahi; si no, copialo antes del prompt de cada escena.
- **Ingles 100%** en todos los prompts. La narrativa y notas de direccion estan en castellano, pero el bloque copiable que entra al modelo es solo ingles. Cero jerga inventada del worldbuilding dentro del prompt — todo se describe visualmente.

## Reference images disponibles

| Personaje / Asset | Ruta (relativa a `public/`) | Uso |
| --- | --- | --- |
| Jiggy | `images/personajes/jiggy.png` | character lock |
| Wiz | `images/personajes/wiz.png` | character lock |
| Byte | `images/personajes/byte.png` | character lock |
| Luxa | `images/personajes/luxa.png` | character lock |
| Zek | `images/personajes/zek.png` | character lock |
| Mariela | `images/personajes/mariela.png` | character lock |
| Portada 1 (accion frenetica + paleta universo) | `images/portadas/portada.png` | mood/style reference (caverna activa) |
| Portada 2 (poster heroico grupal) | `images/portadas/portada2.png` | mood/style reference (caverna ceremonial) |

> Las portadas se usan como **style reference** unicamente para shots ambientados en la caverna subterranea. NO se usan como mood reference para shots de Mariela (cocina/oficina/metro/calle): esos son tonal-opuestos por diseno.

## Style-lock (comun a todas las escenas)

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]
```

---

## Escena 01 — Un cristal a punto de apagarse

**Beat narrativo**: el mundo se presenta por su sintoma — algo central aca se esta muriendo y nadie llega a salvarlo.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | Mood reference (caverna ceremonial, atmosfera volumetrica densa) | `public/images/portadas/portada2.png` ✓ |
| `@image2` | Concept art: establishing wide de la caverna subterranea, vasta y casi a oscuras, con una estalagmita central que sostiene un unico cristal magenta apenas pulsando | **TBD — generar primero con Nano Banana** (ID `concept-cave-wide-establishing`) |

**Prompt visual** (copiable, ingles puro):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Wide cinematic shot, slow descending crane move (24-28mm equivalent), of a vast nearly-dark subterranean cavern as established in @image2 (the cavern concept art). A single low stalagmite at center holds an embedded magenta crystal the size of a fist, faintly pulsing — its emission almost spent, barely lighting itself. Dozens of empty hollow stalagmites surround it, dark and silent, telling a story of extinction without words. Rule of thirds: the dying crystal sits at lower-third intersection, leading lines of stalagmite tips converging on it. A single hairline shaft of pale-cyan ambient bioluminescence slices vertically from a fissure in the rock ceiling, catching slow-falling dust particles in suspension. In the deep background, a tiny still silhouette of a small bipedal creature stands motionless — unreachable, not approaching. Mood and atmosphere consistent with @image1 (mood reference). Palette: deep purple cavern #4B2E80 and blue-violet shadows #0E0820, struggling magenta core #FF49B4 on the central crystal, hairline pale-cyan #7FFFD4 in the ceiling shaft, no warm tones. Texture: rough porous igneous matte rock with thin mineral veining, glassy multifaceted crystal with hairline cooling cracks, dense volumetric haze with dust motes catching cyan light. Mood: silent agony, curiosity at the edge of grief. Rendered as stylized 3D animation cinematic, high-contrast neon-magic lighting, marked bloom on the dying magenta emissive, painterly background, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, 3D render look, generic family-feature animation look, anime, moe, harsh black outlines, oversaturated, flat cel-shading, dungeon RPG cliche, treasure chest, torch on wall, sword, dragon, magic circle portal, glowing eyes on background silhouette, game HUD, gem counter, mini-map, loading bar, low-contrast soft lighting, thriller vignetting, beauty-shot DOF
```

**Notas de direccion**: el espectador tiene que sentir que llego a un velorio sin saberlo. La silueta del fondo no es amenaza ni misterio — es duelo. Si el cristal magenta brilla mas de lo "casi-apagado", se rompe el arco emocional con escena-13. Mantener el shaft cyan finisimo: es semilla subliminal de la activacion que viene en B14.

---

## Escena 02 — Los que esperan

**Beat narrativo**: la inaccion es la decision — saben que no pueden bajar a buscar la chispa, tienen que esperar que llegue desde arriba.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | Character sheet de Wiz (cyclops anciano, barba blanca, tunica con capucha morada, baston con cristal violeta-magenta en la punta) | `public/images/personajes/wiz.png` ✓ |
| `@image2` | Character sheet de Byte (cyclops joven con auriculares over-ear con LEDs verdes lima, orejas elasticas puntiagudas) | `public/images/personajes/byte.png` ✓ |
| `@image3` | Character sheet de Zek (cyclops adolescente con gorra morada de visera, postura relajada) | `public/images/personajes/zek.png` ✓ |
| `@image4` | Mood reference (caverna ceremonial) | `public/images/portadas/portada2.png` ✓ |
| `@image5` | Concept art: establishing wide de la caverna subterranea (mismo set que escena 01) | **TBD — generar primero con Nano Banana** (ID `concept-cave-wide-establishing`) |

**Prompt visual** (copiable, ingles puro):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Wide reverse shot of the same dim subterranean cavern from @image5 (cavern concept art), locked-off camera (28mm equivalent). In the deep middle ground, three small cyclops creatures stand still on a worn stone ledge, viewed from behind and slightly to the side: @image1 (the elder cyclops with white beard, deep-purple hooded robe, holding a wooden staff topped with a violet-magenta crystal) in front, leaning on his staff with the crystal tip catching faint magenta rim light, white beard and hooded robe forming a clear vertical silhouette; behind and to the left @image2 (the cyclops with over-ear headphones), his over-ear headphones glowing dim lime green #A7F432 in two soft halos against the dark, pointed elastic ears alert; behind and to the right @image3 (the teenage cyclops with purple visor cap), the visor of his purple cap catching one single edge of magenta light, shoulders relaxed but head tilted up. The elder cyclops looks toward a hairline fissure in the cavern ceiling where a thin shaft of pale-cyan #7FFFD4 light leaks through. A faintly pulsing magenta crystal embedded in a small central stalagmite still sits in the lower foreground, unfocused but present. Mood and palette consistent with @image4 (mood reference). Composition: rule of thirds, three creatures clustered on the right third, ceiling fissure on upper-left third, dying crystal as out-of-focus foreground anchor. Palette: deep purple #4B2E80 and blue-violet shadow #0E0820 dominate, faint magenta #E83FC8 rim on the elder's staff, lime #A7F432 only on the headphone LEDs, no sodium tones, no gold. Mood: collective contemplation, weight, the stillness of waiting. Dense volumetric haze, slow dust falling through the cyan shaft. Stylized 3D animation, semi-realistic PBR with subsurface scattering on green-turquoise skin, high-contrast neon-magic lighting, painterly volumetric background, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature animation, harsh black outlines, four-eyed characters, two eyes per cyclops creature (each must have ONE central eye only), oversaturated, action pose, combat stance, fantasy battle cliche, sword, dragon, glowing magic circle, game HUD, mini-map, gem counter, thriller vignette, glamour DOF
```

**Notas de direccion**: la quietud es la actuacion. Si cualquiera de los tres parece "en pose" o "en formacion heroica" se contamina con la portada-1 (accion frenetica) — aca es lo opuesto. Wiz mira la grieta del techo, no el cristal: ya sabe que la salvacion no esta abajo. Confirmar UN solo ojo central en cada criatura — image-gen tiende a meter dos.

---

## Escena 03 — Mariela en la oficina

**Beat narrativo**: presentamos a la protagonista por su funcionamiento — eficiente, invisible, automatica.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | Character sheet de Mariela (mujer de mediados de treinta, pelo castano oscuro recogido en cola baja, lentes con marco metalico fino, blusa sobria) | `public/images/personajes/mariela.png` ✓ |
| `@image2` | Concept art: cubiculo de oficina corporativa estandar en Santiago, iluminacion fluorescente fria, paneles divisorios grises, monitor encendido con planilla | **TBD — generar primero con Nano Banana** (ID `concept-office-cubicle-mariela`) |

**Prompt visual** (copiable, ingles puro):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Medium shot, locked-off (35mm equivalent), of @image1 (the woman from the character reference: mid-thirties, dark brown hair pulled back in a low ponytail, sober blouse, thin metal-framed glasses with a single hairline scratch on the right lens) sitting at her desk in @image2 (the office cubicle concept) at 18:47 on a weeknight. She is half-turned toward her monitor, her face competent and vacant, eyes flat on a spreadsheet showing pivot tables with yellow and red highlighted cells reflected faintly in her lenses. A cold mug of coffee sits beside the keyboard. A small picture frame holds a photo of an 8-year-old niece, placed without prominence. A male coworker passes behind her dropping a manila folder on the corner of her desk — captured mid-stride, slightly out of focus. Eight other identical cubicle dividers recede in shallow depth behind her under cool fluorescent 4500K ceiling lighting. A wall clock reading 18:47 is visible in the background. Composition: rule of thirds, the woman on the left third, fluorescent ceiling line on upper third, depth receding into pale gray cubicle field. Palette: cool fluorescent white #DDE3E8, dusk-blue shadow #2A3A5A, muted desk neutrals — strictly no magenta, no turquoise, no fantasy palette accents anywhere in frame. Mood: clinical, competent emptiness, automation as armor. Texture: matte fabric blouse, brushed steel keyboard, slight specular on coffee mug rim, fluorescent lighting flat and even. Stylized 3D animation, semi-realistic PBR softened cinematic human, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, DSLR portrait, glamour beauty lighting, anime, moe, big anime eyes, exaggerated cartoon proportions, harsh black outlines, magenta crystal, turquoise glow, neon, fantasy elements, cyclops creatures in frame, mystical glow, thriller vignette, dramatic chiaroscuro, telenovela lighting, oversaturated
```

**Notas de direccion**: la oficina debe leerse como cualquiera, no como "oficina de personaje". Si aparece UN solo elemento magico (cristal, glow magenta, particula cyan) se rompe el contraste fundacional con la caverna — la regla es CERO paleta fantastica en este beat. Mariela no es triste; es operativa. Esa diferencia es todo.

---

## Escena 04 — La libreta en el metro

**Beat narrativo**: aparece el objeto-simbolo — la libreta — y se establece en un solo gesto que hace medio ano que no la usa.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | Character sheet de Mariela | `public/images/personajes/mariela.png` ✓ |
| `@image2` | Concept art: interior de vagon de metro de Santiago en hora punta, lleno de pasajeros con abrigos de invierno, iluminacion fluorescente fria, ventanas con luz azul del tunel | **TBD — generar primero con Nano Banana** (ID `concept-metro-car-rush-hour`) |
| `@image3` | Concept art: primer plano de libreta A6 de cuero marron gastada, banda elastica decolorada por el sol, fina grieta a lo largo del lomo | **TBD — generar primero con Nano Banana** (ID `concept-notebook-leather-worn`) |

**Prompt visual** (copiable, ingles puro):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Medium shot (35-50mm equivalent), locked-off, framed slightly low to feel like a fellow passenger's eyeline, of @image1 (the woman from the character reference) standing inside @image2 (the packed metro car concept) at evening rush hour. She holds the stainless overhead handrail with her right hand, the strap of a worn shoulder bag on her left arm, surrounded by the soft blur of other commuters in winter coats reading phones. Her left hand has just opened @image3 (the small A6 brown leather notebook) — held at chest height, the page she is looking at is the last entry: three handwritten lines in her own pencil reading "groceries / call mom / fix printer", dated six months ago. Her face is held one beat too long over the page, faint micro-expression of recognition without softness. Practical fluorescent metro lighting overhead, cool greenish-white #C4D8DE, with intermittent dusk-blue #2A3A5A light bleeding through the windows from the tunnel. Composition: rule of thirds, the woman in the left third with the notebook held at lower-third intersection, leading lines of the metro car ceiling and handrails converging into shallow depth on the right third. Palette: cool fluorescent green-white, dusk blue, muted winter coat blacks and grays, faint warm tungsten of a single overhead bulb pocket — no fantasy palette accents. Texture: worn leather notebook with fingerprint-smoothed cover and elastic band, brushed steel handrail with soft specular, matte coats. Mood: dead habit, small private weight. Stylized 3D animation, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, DSLR portrait, glamour beauty DOF, magenta neon, turquoise crystal glow, cyclops creatures, fantasy elements, anime, moe, big anime eyes, harsh black outlines, oversaturated, thriller vignetting, dramatic chiaroscuro, empty deserted metro car (must read as packed), action pose
```

**Notas de direccion**: el plano tiene que sentir invasion cotidiana, no "soledad poetica". El vagon esta LLENO y eso amplifica su aislamiento. La libreta es protagonista pero no se ilumina ni brilla — todavia no. Si aparece glow cyan en la grieta del lomo aca, se quema el reveal de B6.

---

## Escena 05 — La cocina, antes de escribir

**Beat narrativo**: ella decide sentarse — no escribe todavia, pero ya se esta dando permiso.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | Character sheet de Mariela | `public/images/personajes/mariela.png` ✓ |
| `@image2` | Concept art: cocina pequena de departamento en Santiago al atardecer, con mesa de madera, hervidor de aluminio en estufa, lampara colgante Edison sobre la mesa, ventana con vista a la ciudad y la cordillera | **TBD — generar primero con Nano Banana** (ID `concept-mariela-kitchen-dusk`) |
| `@image3` | Concept art: libreta A6 de cuero marron sobre mesa de madera junto a lapiz de madera afilado, taza de ceramica como portalapices | **TBD — generar primero con Nano Banana** (ID `concept-notebook-on-table`) |

**Prompt visual** (copiable, ingles puro):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Medium-wide shot (35mm equivalent), locked-off, of @image2 (the small apartment kitchen at sunset) with @image1 (the woman from the character reference) standing at the kitchen counter beside a stovetop where an old aluminum kettle has just begun to hiss, her body angled three-quarters toward the window. Through the window: city skyline at dusk, smog-pink sky #E8A0A0 fading to cool dusk-blue #5A6E8A, distant mountain range barely visible as silhouette. Her own reflection is faintly held in the window glass, ghosted over the city. A single warm Edison-style tungsten bulb #FFD08A hangs as a pendant lamp over a small wooden table, pooling warm light on the surface. On the table from @image3: the brown leather A6 notebook placed flat, a sharpened wooden pencil pulled from a small ceramic cup. Her posture is quiet, hands resting at her sides, just looking at her own reflection one beat too long. Tile floor #D8CFC2 with grout lines. Composition: rule of thirds, the woman in the right third, window with reflection in the upper-left third, table with notebook in lower-left third — the two anchors of the scene. Palette: warm tungsten #FFD08A pool on table, dusk-blue #5A6E8A from window, muted ceramic neutrals, no fantasy palette glow. Texture: worn ceramic kettle with brushed-steel handle, matte wood table, soft cotton blouse fabric. Mood: contemplative, suspended, the second before a decision. Stylized 3D animation, soft warm haze in the bulb pool, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, DSLR, glamour beauty lighting, anime, moe, big anime eyes, harsh black outlines, magenta neon, turquoise crystal glow, cyclops creatures in frame, fantasy elements, mystical aura around the woman, thriller vignette, telenovela melodrama lighting, oversaturated, kitchen straight from a TV cooking show
```

**Notas de direccion**: el reflejo en la ventana es el corazon del plano. Si la imagen lo pierde o lo pone solo decorativo, el beat no funciona — ella esta viendose a si misma decidir. La cocina es chica, modesta, real; nada de "kitchen porn" de revista. Tungsten warm es la UNICA fuente calida del mundo humano hasta aca.

---

## Escena 06 — La pregunta

**Beat narrativo**: la regla magica del universo se activa — alguien arriba escribe una pregunta sincera por primera vez en mucho tiempo.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | Character sheet de Mariela (referencia para mano y antebrazo) | `public/images/personajes/mariela.png` ✓ |
| `@image2` | Concept art: primer plano cenital de libreta A6 de cuero marron abierta sobre mesa de madera, pagina en blanco, lapiz de madera afilado | **TBD — generar primero con Nano Banana** (ID `concept-notebook-overhead-blank`) |
| `@image3` | Concept art: detalle de lomo de libreta de cuero gastado con grieta capilar muy fina recorriendo el lomo | **TBD — generar primero con Nano Banana** (ID `concept-notebook-spine-crack`) |

**Prompt visual** (copiable, ingles puro):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Tight overhead shot (50-85mm equivalent), slow inferred push-in, framing as in @image2 (the overhead notebook concept). The left hand of @image1 (the woman from character reference) holds a sharpened wooden pencil over the open A6 brown leather notebook on the small wooden kitchen table. The page is freshly blank, just past a previous entry of three pencil lines. She has just finished writing in tentative, hesitant cursive — the kind of handwriting from someone out of practice — the words "Why did I stop writing here?" in soft graphite. The pencil tip rests at the end of the question mark, lifted a millimeter. Along the spine of the notebook (the same hairline crack visible in @image3), an almost imperceptible thread of pale-cyan #7FFFD4 light glows for one breath at no more than 5% opacity — barely visible, easy to miss on first watch. Behind the hand, the kettle on the stove has just clicked off on its own, slightly out of focus. Warm tungsten #FFD08A pool from a single Edison pendant lights the page from above-left, casting soft shadow of the pencil across the paper. Composition: centered on the page with hand entering from lower-right, rule of thirds anchors the written line on upper-third, notebook spine on left-third where the cyan hint lives. Palette: warm tungsten #FFD08A dominant, dusk-blue #2A3A5A in deep shadow, paper cream #F0E8D8, graphite gray on the line, hairline pale-cyan #7FFFD4 at 5% on the spine. Texture: matte uncoated paper, worn fingerprint-smoothed leather spine with visible fiber crack, sharpened pencil with subtle graphite specular. Mood: intimate, contained seismic event. Stylized 3D animation, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic skin pores, hyperrealistic, DSLR macro, glamour DOF, magenta crystal, turquoise glow on hand, anime, moe, harsh black outlines, fantasy magic circle, glowing portal, sparkles, fairy dust, full visible cyan spine glow above 5% (must remain near-subliminal), oversaturated, thriller vignette, loading-screen UI pulse, square-wave blink on cyan hint
```

**Notas de direccion**: el cyan en la grieta del lomo es la regla del universo asomando — tiene que ser CASI invisible. Si el espectador lo nota la primera vez, esta mal. La letra es protagonista: titubeante, lenta, humana. El kettle apagandose solo en segundo plano es subtextual, no lo enfoques. Este es el shot mas importante del episodio — es el "encendido" silencioso.

---

## Escena 07 — Byte detecta la pregunta

**Beat narrativo**: abajo se enteran — y por primera vez algo se mueve.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | Character sheet de Byte | `public/images/personajes/byte.png` ✓ |
| `@image2` | Character sheet de Wiz | `public/images/personajes/wiz.png` ✓ |
| `@image3` | Mood reference (caverna ceremonial) | `public/images/portadas/portada2.png` ✓ |
| `@image4` | Concept art: interior de la caverna subterranea, el mismo set que escena 01-02 | **TBD — generar primero con Nano Banana** (ID `concept-cave-wide-establishing`) |

**Prompt visual** (copiable, ingles puro):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Medium two-shot (50mm equivalent), locked-off with a 5-degree slight Dutch tilt, of @image1 (the cyclops with over-ear headphones and pointed elastic ears) and @image2 (the elder cyclops with white beard and purple staff) inside @image4 (the dim cavern set). @image1 stands in the foreground three-quarters facing camera, his pointed elastic ears just having flicked alert, his over-ear headphones glowing brighter lime-green #A7F432 than before, his single turquoise eye widened with pupil enlarged. His right hand is pressed two-fingered against the right earcup. He is mid-turn toward @image2. @image2 stands behind him to the right, his single eye closed for one beat with white beard catching faint magenta rim light from his staff's violet-magenta crystal tip — staff held vertical, just beginning to lift to point toward an off-screen passage to the right. Around them, dense volumetric haze, slow-falling dust catching faint magenta and cyan ambient light. A faintly pulsing magenta crystal sits as out-of-focus background anchor in the lower-left. Mood and palette consistent with @image3 (mood reference). Composition: rule of thirds, @image1 in the left third, @image2 in the right third, slight Dutch tilt creates contained alarm without melodrama. Palette: deep purple #4B2E80 cavern base, blue-violet #0E0820 shadow, magenta #E83FC8 rim from the elder's staff, lime green #A7F432 emissive on the headphones (slightly intensified vs scene 2), turquoise #2EE0C8 on both single eyes. Texture: green-turquoise cyclops skin with subsurface scattering, matte purple velvet on the elder's robe with thread weave, glossy plastic on the headphones with bright LED. Mood: alert, the cavern's first inhalation in hours. Stylized 3D animation, marked bloom on lime headphone LEDs, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, anime, moe, two eyes per cyclops creature (must be cyclops, ONE central eye only), big anime eyes, harsh black outlines, generic family-feature look, fantasy battle stance, sword, magic circle, gem counter HUD, loading bar, oversaturated, thriller vignette, action movie pose, lightning bolts
```

**Notas de direccion**: la direccion de luz de Wiz tiene que coincidir con escena-02 (rim magenta desde su propio baston) — son el mismo lugar y el mismo momento del dia subterraneo. La escena se "lee" como un latido: el lime de Byte sube de intensidad por primera vez. Si la imagen mete teatralidad (gestos amplios, gritos), se rompe el codigo del universo: la magia es susurrada.

---

## Escena 08A — El lapiz apretado (cocina)

**Beat narrativo**: la regla magica del universo se demuestra. Aca. Sin que nadie la diga. (Plano A del match-cut, ~3 segundos.)

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | Character sheet de Mariela (referencia para mano) | `public/images/personajes/mariela.png` ✓ |
| `@image2` | Concept art: primer plano cenital de libreta A6 de cuero marron abierta con linea escrita "Why did I stop writing here?" sobre mesa de madera | **TBD — generar primero con Nano Banana** (ID `concept-notebook-question-written`) |

**Prompt visual** (copiable, ingles puro):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Extreme close-up macro shot (100-150mm equivalent), locked-off, of the left hand of @image1 (the woman from character reference) on the page from @image2 (the notebook with the written question). Fingers grip a sharpened wooden pencil so tightly that knuckles whiten faintly under softened cinematic-3D skin shading and the paper below shows visible compression marks under the lead. The frame holds tight on the pencil tip pressed against the page just below the handwritten line "Why did I stop writing here?", a single grain of graphite on the page surface catching the warm tungsten #FFD08A pool from above. Her hand trembles a fraction of a millimeter — captured as micro-blur on the pencil shaft's tip only. Background out of focus: the cream of the page, the shadow of the spine, the table edge. Composition: centered macro hero, rule of thirds places the written line at upper-third, pencil tip at center anchor, graphite grain catching highlight at lower-third. Palette: warm tungsten #FFD08A dominant, paper cream #F0E8D8, graphite gray, deep dusk-blue #2A3A5A in shadow corners — no fantasy palette glow at all in this plate. Texture: matte uncoated paper, sharpened cedar pencil with grain visible, soft skin with subtle subsurface scattering on knuckle, faint specular on polished pencil shaft. Mood: contained seismic moment, the millisecond before a cosmos rearranges. Stylized 3D animation, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic skin pores, hyperrealistic macro, DSLR product shot, glamour beauty DOF, magenta neon, turquoise crystal glow, cyclops creatures, sparkles, fantasy magic, anime, moe, harsh black outlines, oversaturated, thriller vignette, dramatic chiaroscuro, hand model glamour
```

**Notas de direccion**: cero magia visible en este plato — la magia esta en el match-cut con 8B, no en el frame. Si aparece cualquier glow de paleta fantastica aca, se rompe la sorpresa. La compresion del papel debajo del lapiz es el detalle hero: muestra cuanto esta apretando sin mostrar emocion en cara.

---

## Escena 08B — La palma de Wiz (caverna)

**Beat narrativo**: la regla magica del universo se demuestra. Aca. Sin que nadie la diga. (Plano B del match-cut, ~12 segundos, hard cut desde 8A.)

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | Character sheet de Wiz (referencia para palma + ojo en foco suave detras) | `public/images/personajes/wiz.png` ✓ |
| `@image2` | Mood reference (caverna ceremonial) | `public/images/portadas/portada2.png` ✓ |
| `@image3` | Concept art: macro de palma de cyclops con cuatro dedos abierta hacia arriba en oscuridad densa, fondo de bruma volumetrica de caverna | **TBD — generar primero con Nano Banana** (ID `concept-cyclops-palm-macro`) |

**Prompt visual** (copiable, ingles puro):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Extreme close-up macro shot (100-150mm equivalent), locked-off, framed as in @image3 (the cyclops palm macro concept). The right palm of @image1 (the elder cyclops from character reference) — a small four-fingered hand with green-turquoise #21D8B6 skin, slightly knotted with age, opened upward in deep cavern darkness. Above the palm, hovering exactly two centimeters above the skin, a small newly-formed magenta crystal #FF49B4 with #E83FC8 rim has just materialized — dense, faceted, with hairline cooling cracks visible at its edges, glassy multifaceted body holding internal subsurface emission, pulsing strongly once mid-frame. The crystal casts warm magenta rim light onto the skin of the palm and faint magenta bloom into the surrounding volumetric haze. In soft focus directly behind the palm, his single turquoise #3FE0C8 eye watches the crystal — not with surprise, with recognition; the eye partly visible above the white beard which catches faint magenta edge light. Dense particulate cavern haze surrounds the moment, dust motes spiraling slowly inward toward the new crystal as if drawn to it. Mood and palette consistent with @image2 (mood reference). Composition: extreme centered hero on the floating crystal, palm forming the foreground curve, eye in upper-third soft-focus background, rule of thirds places the crystal exactly at the optical center. Palette: magenta #FF49B4 core and #E83FC8 rim dominant, deep purple #4B2E80 ambient, blue-violet #0E0820 shadow, turquoise #21D8B6 on palm skin and #3FE0C8 in the soft-focus eye, no warm tones, no cyan, no gold. Texture: glassy multifaceted crystal with internal emission and hairline cooling cracks, soft green-turquoise cyclops skin with marked subsurface scattering, matte white beard with fine fiber detail. Mood: silent revelation, the universe quietly proving its rule. Stylized 3D animation, marked bloom on the new crystal, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic skin pores, hyperrealistic, DSLR macro, two eyes (must be cyclops, single eye only), five fingers (must be 4-fingered cyclops hand), anime, moe, big anime eyes, harsh black outlines, generic family-feature look, sword, dragon, magic circle portal, sparkle burst, fairy dust, lightning, gem counter HUD, oversaturated, loading-screen blink pulse, square-wave flash, glamour beauty DOF
```

**Notas de direccion**: este es el otro hero shot del episodio junto con B6. El cristal aparece — no se ensambla, no se construye en pantalla, no tiene FX trail. Esta / no esta. Una sola pulsacion fuerte. Si la imagen agrega "magic forming animation" se contamina con fantasy cliche. La cara de Wiz no muestra sorpresa: muestra reconocimiento. Coordinar con el editor: hard cut desde 8A con un frame de silencio total, sin transicion FX.

---

## Escena 09 — Wiz reconoce, Jiggy y Luxa cargan

**Beat narrativo**: la chispa nueva pasa de manos — abajo se confirma que esta si es real, y arranca el relevo hacia arriba.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | Character sheet de Jiggy (cyclops adolescente con piel turquesa, arnes de cuero, ojo turquesa unico) | `public/images/personajes/jiggy.png` ✓ |
| `@image2` | Character sheet de Wiz | `public/images/personajes/wiz.png` ✓ |
| `@image3` | Character sheet de Luxa (cyclops femenina con vincha morada y poncho tribal multicolor) | `public/images/personajes/luxa.png` ✓ |
| `@image4` | Mood reference (caverna ceremonial) | `public/images/portadas/portada2.png` ✓ |
| `@image5` | Concept art: interior de la caverna subterranea con bruma densa | **TBD — generar primero con Nano Banana** (ID `concept-cave-wide-establishing`) |

**Prompt visual** (copiable, ingles puro):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Medium-tight three-shot (50mm equivalent), locked-off slightly low, inside @image5 (the dim cavern set). @image1 (the teenage cyclops with leather harness from character reference) is the connective figure spanning the middle. @image2 (the elder cyclops from character reference) stands center-left holding a newly-formed magenta crystal #FF49B4 floating two centimeters above his right palm, his single turquoise eye fixed on it, a single slow tear caught mid-fall trapped in his white beard catching faint magenta rim light. @image1 enters from frame-left already mid-motion, his right hand opened upward, his single turquoise eye wide and ready, leather harness across his chest, lower body angled into a runner's pre-stride — captured at the exact frame where @image2 is placing the magenta crystal #FF49B4 onto @image1's right palm. Simultaneously, @image3 (the female cyclops with purple headband and tribal multicolor poncho from character reference) enters from frame-right barely slowing, her purple headband catching faint warm light, her tribal multicolor poncho flowing, pressing a smaller golden-warm crystal #FFE34D into @image1's left palm without making eye contact — already pivoting back into the dark. @image1's two crystals now read clearly: magenta on the right hand, warm gold on the left. Around them dense volumetric haze, magenta and faint gold pools of light overlapping for the only time in the episode. Mood and palette consistent with @image4 (mood reference). Composition: rule of thirds, @image2 on the left third with the magenta exchange at center anchor, @image3 exiting on the right third with gold trail, @image1 as the connective figure spanning the middle. Palette: magenta #E83FC8 core / #FF49B4 from the elder's new crystal, warm gold #FFE34D / #F1E3AA from the female cyclops's crystal (visiting warmth, the only gold in any cavern shot), turquoise #21D8B6 cyclops skin, deep purple #4B2E80 ambient, blue-violet #0E0820 shadow. Texture: glassy faceted crystals with internal emission, worn leather harness on @image1 with brass buckle, woven multicolor tribal cloth on @image3 with visible thread weave, matte purple velvet on @image2 with deep folds. Mood: reverence, urgent handoff, three-second window of converging warmth. Stylized 3D animation, marked bloom on both crystals, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, anime, moe, two eyes per cyclops creature (must be cyclops single eye), five-fingered hands (must be four-fingered), big anime eyes, harsh black outlines, generic family-feature look, group-pose hero formation (must read as motion not pose), magic circle, sparkle burst, lightning, sword, gem counter HUD, oversaturated thriller, glamour DOF, melodramatic pose
```

**Notas de direccion**: este es el UNICO momento del piloto donde gold y magenta coexisten en cuadro — es la negociacion de paletas que el style-guide protege. Si Luxa se queda demasiado en el plano se vuelve grupo-pose; tiene que sentirse "pase de testigo en relevo". La lagrima de Wiz es chica, contenida, atrapada en la barba — no una lagrima de close-up emocional barato. Confirmar 4 dedos por mano y 1 ojo central por personaje.

---

## Escena 10 — El cruce a la superficie

**Beat narrativo**: el cristal dorado de Luxa demuestra su funcion — Jiggy puede cruzar sin que los drones lo registren.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | Character sheet de Jiggy | `public/images/personajes/jiggy.png` ✓ |
| `@image2` | Character sheet de Zek | `public/images/personajes/zek.png` ✓ |
| `@image3` | Concept art: vista contrapicado desde debajo de una rejilla rectangular de hierro fundido en el asfalto de una calle nocturna en Santiago, con farola de luz sodio naranja arriba y dos pequenos drones esfericos negros patrullando el cielo nocturno | **TBD — generar primero con Nano Banana** (ID `concept-street-grate-low-angle-night`) |

**Prompt visual** (copiable, ingles puro):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Wide low-angle shot (24mm equivalent), framing as in @image3 (the street-grate concept). Looking up from beneath a rectangular cast-iron sewer grate set into the asphalt of an avenue in Santiago, around 10pm. The grate's vertical bars stripe the frame against the night sky; an old sodium streetlamp #FF8A30 hangs above-left casting orange cone light across the asphalt and through the grate slats. The street is empty. Three storeys above in the night sky, two small spherical black surveillance drones with single magenta #E83FC8 LEDs patrol in slow lateral sweep — visible through the grate slats. Just below the grate in a strip of darkness, @image1 (the teenage cyclops with leather harness from character reference) stands looking up: a magenta crystal #FF49B4 closed in his right fist (faint glow leaking between his fingers), a warm gold crystal #FFE34D resting open on his left palm. His single turquoise eye reflects the sodium orange in a faint warm rim — the first time green-turquoise cyclops skin meets warm tungsten/sodium light in the episode. He has just brushed the gold crystal once with his left thumb; the gold pulses subtly, and the nearest drone's LED is mid-drift, rotating exactly 30 degrees off-axis as if its scan target slipped. Behind @image1 in the deeper dark of the access tunnel, @image2 (the teenage cyclops with purple visor cap from character reference) stands with his cap tilted, a portable boombox at his hip, having just struck it once — a faint sub-tonal pressure visible as soft displacement of dust haze in the tunnel air. Composition: rule of thirds, grate vertical lines as foreground graphic, @image1 in lower-right third, sodium streetlamp in upper-left third, drones in upper-right third silhouetted, @image2 as soft out-of-focus depth anchor in the back. Palette: sodium orange #FF8A30 (exclusive to this beat), night-blue #2A3A5A sky, drone magenta #E83FC8 LED accents, magenta #FF49B4 leaking from @image1's right fist, warm gold #FFE34D on his left palm, turquoise #21D8B6 cyclops skin. Texture: cast-iron grate with rust and chipped paint, asphalt with grain, glassy crystals with internal emission, brushed plastic on drone shells. Mood: stealth, the magic rule made visible in geometry — drones drift, do not flee. Stylized 3D animation, slight haze in the streetlamp cone, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, DSLR night photo, anime, moe, big anime eyes, harsh black outlines, generic family-feature look, action chase pose, drones firing or attacking, magic circle portal, lightning bolt from crystal, glowing fairy trail, gem counter HUD, mini-map, two eyes per cyclops creature (must be cyclops), five-fingered hands, oversaturated thriller vignette, glamour DOF, fully-lit street (must be sparse sodium pool only)
```

**Notas de direccion**: los drones no son enemigos en pantalla — son rutina ambiental que se desvia. Si la imagen los muestra "reaccionando" o "alertados", se rompe la regla del cristal dorado (no los huye, los re-rutea). El sodio naranja es UNICO de este beat en todo el piloto — usar sin miedo. Jiggy con rim sodium en piel turquoise es el preview tonal del crossover de B11.

---

## Escena 11 — La entrega invisible

**Beat narrativo**: el manifiesto del proyecto pasa fisicamente — el calorcito en el pecho deja de ser metafora y se vuelve plano de cine.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | Character sheet de Mariela | `public/images/personajes/mariela.png` ✓ |
| `@image2` | Character sheet de Jiggy | `public/images/personajes/jiggy.png` ✓ |
| `@image3` | Concept art: cocina pequena de departamento de noche, mismo set que escena 05, con lampara colgante Edison encendida y heladera al lado izquierdo del encuadre | **TBD — generar primero con Nano Banana** (ID `concept-mariela-kitchen-night`) |

**Prompt visual** (copiable, ingles puro):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Medium shot (50mm equivalent), locked-off, framing as in @image3 (the kitchen at night concept) — the tea cup beside the table now visibly cold, condensation dried. @image1 (the woman from character reference) sits at the small wooden table with the open notebook in front of her, her left hand resting flat on the table beside the page with the question, her right hand about to close the cover. From behind the refrigerator on the left side of frame, @image2 (the teenage cyclops with leather harness from character reference) emerges low and quiet, walking with the careful gait of someone delivering something heavy and small — invisible to her, fully present to the camera. He approaches her left hand, his own right palm open holding a magenta crystal #FF49B4, and gently presses it against her palm. On @image2's body in this single frame, the lighting integrates a warm tungsten #FFD08A rim from the kitchen pendant on his right shoulder side and a soft magenta #E83FC8 rim from his own crystal on his left side — a complementary warm-cool gradient over his green-turquoise skin. This is the only shot in the episode where fantasy cool palette and human-kitchen-warm palette negotiate on the same body. @image1's face holds a micro-shift: a small hardness softens; her hand twitches once, lifts an inch, presses to her own chest. @image2 is already turning to leave. Composition: rule of thirds, @image1 on the right two-thirds with notebook, @image2 on the left third entering low, the contact point of palms anchored at center horizon. Palette: warm tungsten #FFD08A pool dominant, dusk-blue #2A3A5A in shadow, magenta #FF49B4 / #E83FC8 contained to @image2 and his crystal only, turquoise #21D8B6 on @image2's skin. Texture: matte wooden table with cup-ring marks, soft cotton on @image1's blouse, worn leather harness on @image2, glassy magenta crystal with internal emission. Mood: warm domestic miracle, the project's manifesto in a single physical gesture. Stylized 3D animation, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, DSLR portrait, glamour beauty DOF, anime, moe, big anime eyes, harsh black outlines, generic family-feature look, two eyes on the cyclops (must be cyclops single eye), five-fingered cyclops hand, the woman seeing the cyclops / looking at the cyclops (must remain unaware), magic circle, sparkle burst, fairy trail, gem counter HUD, oversaturated thriller, dramatic chiaroscuro, telenovela melodrama lighting
```

**Notas de direccion**: la regla central del plano: Mariela NO ve a Jiggy. La camara si. Si el image-gen acomoda los ojos de Mariela hacia Jiggy, esta mal. La "mezcla de paletas" sobre el cuerpo de Jiggy es la unica excepcion del piloto al separation strict warm/cool entre mundos — usar el rim doble como demostracion tecnica del crossover, no como magia generalizada en el cuarto.

---

## Escena 12 — "Okay"

**Beat narrativo**: la transformacion de Mariela cabe en una sola silaba — y eso es suficiente.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | Character sheet de Mariela | `public/images/personajes/mariela.png` ✓ |
| `@image2` | Concept art: cocina pequena de departamento de noche, mismo set que escena 11, con mesa de madera, hervidor en estufa, taza de te fria | **TBD — generar primero con Nano Banana** (ID `concept-mariela-kitchen-night`) |

**Prompt visual** (copiable, ingles puro):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Tight medium shot (85mm equivalent), locked-off, of @image1 (the woman from character reference) seated at the small wooden table inside @image2 (the night kitchen concept) — her right hand closed gently against her own sternum, fingers cupped around an invisible warmth, her gaze on the open notebook page with her own handwritten line "Why did I stop writing here?" still on it. Her face does not break into emotion: instead, the corners of her mouth lift half a centimeter, hold for one beat, then settle. Behind her, the cold tea cup is visible beside the kettle, and she is mid-rise with body language that reads "going to refill". A single Edison-style tungsten #FFD08A pendant pours warm light from above-left, its pool slightly shifted from earlier scenes — the first warm key in the kitchen has imperceptibly intensified by 5%, a residue of the crystal exchange. Faint warm-tungsten residue glow at 8% opacity on her left palm where she received the crystal — barely visible, easy to miss. Composition: rule of thirds, the woman in the right third in seated three-quarter pose, notebook in lower-left third, kettle and tea cup as soft background anchors. Palette: warm tungsten #FFD08A dominant (slightly intensified), dusk-blue #2A3A5A in shadow corners, paper cream and pencil graphite on the visible page, no fantasy palette glow visible in frame except the subliminal palm residue. Texture: matte wooden table, soft cotton blouse, ceramic kettle with brushed-steel handle, paper, faint warm subsurface on her skin where the crystal was pressed. Mood: minimal reconciliation, the first warm tone the kitchen has truly held, the second before she stands up. Stylized 3D animation, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic skin pores, hyperrealistic, DSLR portrait, glamour beauty lighting, anime, moe, big anime eyes, harsh black outlines, big smile (must be sub-centimeter mouth corner shift), tears streaming, melodrama, magenta crystal visible, turquoise glow, cyclops creatures in frame, fantasy element, sparkle, magic aura around the woman, thriller vignette, telenovela close-up, oversaturated, full-bright key light
```

**Notas de direccion**: este es el "tono mayor" del episodio — pero es chiquito. Si la sonrisa pasa de medio centimetro, mata el plano. El residue cyan/warm en su palma debe ser casi invisible (8% max) — es el espejo del cyan en el lomo de B6, pero ahora warm. La intensificacion del tungsten es subliminal: nadie tiene que notar que la luz cambio, solo sentir que la cocina dejo de estar fria.

---

## Escena 13 — Wiz y Jiggy abajo: "esta se queda"

**Beat narrativo**: por primera vez en el episodio, las estalagmitas vacias empiezan a brillar — el lugar deja de morir.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | Character sheet de Wiz | `public/images/personajes/wiz.png` ✓ |
| `@image2` | Character sheet de Jiggy | `public/images/personajes/jiggy.png` ✓ |
| `@image3` | Mood reference (caverna ceremonial) | `public/images/portadas/portada2.png` ✓ |
| `@image4` | Concept art: caverna subterranea con dos estalagmitas reactivandose con suave emision magenta, fisura cenital con haz de luz cyan palido, bruma volumetrica densa con motas ascendiendo | **TBD — generar primero con Nano Banana** (ID `concept-cave-stalagmites-reawakening`) |

**Prompt visual** (copiable, ingles puro):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Wide shot (28mm equivalent), slow descending camera, of the subterranean cavern as established in @image4 (the reawakening cavern concept). @image1 (the elder cyclops with white beard and purple staff from character reference) stands center-left in three-quarter back view, his deep-purple hooded robe and white beard reading clearly, his staff held lightly, his single eye watching a slow upward spiral of dust motes rising through the ceiling fissure, lit by a slightly warmer-than-before pale-cyan #7FFFD4 shaft (now at 25% opacity vs 15% in scene 1). @image2 (the teenage cyclops with leather harness from character reference) has just run back into frame from the right, breath heavy, hands empty — no magenta crystal, no gold crystal — his harness slightly askew, posture still in arrival decel. Around the two figures, two of the previously-empty hollow stalagmites closest to @image1 now hold faint magenta #FF49B4 emission at low intensity — small new crystals reawakening in their cores. The dying central crystal from scene 1 now reads slightly stronger as well. Just two stalagmites lit, not more — but a clear contrast to scene 2 where none glowed. Mood and palette consistent with @image3 (mood reference). Composition: rule of thirds, @image1 on the left third, @image2 on the right third arriving in frame, the ceiling fissure shaft on upper-third as vertical compositional anchor, the two reawakening stalagmites in lower-third base. Palette: magenta #FF49B4 / #E83FC8 in the new stalagmite glows and central crystal, deep purple #4B2E80 ambient, blue-violet #0E0820 shadow, pale-cyan #7FFFD4 in the ceiling shaft (subtly intensified), turquoise #21D8B6 cyclops skin, no warm tones, no gold. Texture: matte porous igneous rock with mineral veining, glassy newly-forming crystals with hairline cooling cracks, dense volumetric haze with rising dust, matte purple velvet on @image1, worn leather on @image2. Mood: sustained relief, an open question, the place no longer dying. Stylized 3D animation, marked bloom on the new emissive stalagmites, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, anime, moe, big anime eyes, harsh black outlines, generic family-feature look, every stalagmite glowing brightly (must be only 2 reawakening), action stance, magic circle, sparkle burst, lightning, sword, dragon, two eyes per cyclops creature (must be cyclops), five-fingered hands, oversaturated, thriller vignette, glamour DOF
```

**Notas de direccion**: SOLO dos estalagmitas se reactivan — el cuento es la fragilidad de la recuperacion, no la fiesta. Si la imagen llena la caverna de glow, mata el arco con el episodio 2. AVISO PARA EDITOR: en post-produccion se inserta aqui, durante ~80ms, una chispa-ancla pale-dusty-gold #D9C28A (anchor-spark, B13B exclusivo del style-guide) — NO la incluir en este prompt; es un insert manual fuera del scope de Nano Banana. Reservar ese frame en montaje.

---

## Escena 14 — La libreta brilla sola

**Beat narrativo**: el episodio cierra abriendo — la pregunta queda viva mientras ella ya se fue a dormir.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | Concept art: cocina pequena de noche con la mesa de madera vacia, libreta abierta sobre la mesa con la linea escrita brillando en cyan palido, lampara colgante Edison aun encendida | **TBD — generar primero con Nano Banana** (ID `concept-kitchen-empty-glowing-notebook`) |
| `@image2` | Concept art: detalle de pagina de libreta con la frase "Why did I stop writing here?" escrita a lapiz, con un sutil glow cyan emanando de las letras | **TBD — generar primero con Nano Banana** (ID `concept-notebook-line-glowing-cyan`) |
| `@image3` | Mood reference (tonal: neutros calidos del cuarto humano, sin paleta fantastica) | `public/images/personajes/mariela.png` ✓ |

**Prompt visual** (copiable, ingles puro):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Tight overhead push-in shot (50-85mm equivalent), slow inferred dolly forward, framing as in @image1 (the empty kitchen with glowing notebook concept) — the small wooden kitchen table at night, the kitchen empty of people. The open A6 brown leather notebook lies on the table, page facing up showing the handwritten pencil line "Why did I stop writing here?" exactly as detailed in @image2 (the glowing line concept). The line itself emits a soft pulsing pale-cyan #7FFFD4 glow at approximately 70% opacity, breathing in slow heartbeat-rate sine wave — only the line glows, not the rest of the page. The kitchen pendant Edison bulb #FFD08A is still on, casting its warm pool over the table from above-left, holding a second tea cup beside the kettle (the one she just drank). In the background through an internal doorway visible at frame-edge, the bedroom door is closed and a thin warm strip of light spills from beneath it across the tile floor — the woman is sleeping there, off-screen. Tonal palette consistent with @image3 (mood reference for the human room neutrals). Composition: rule of thirds, the glowing handwritten line at center anchor for the push-in, kettle and second cup in upper-left third, bedroom door light strip in lower-right third, the warm pendant pool framing top-left. Palette: pale-cyan #7FFFD4 (now dominant on the line, the activation made visible), warm tungsten #FFD08A pool, dusk-blue #2A3A5A in shadow, paper cream, leather brown on notebook spine, faint pale-cyan still on the spine crack at 5% as continuity from scene 6. Texture: matte uncoated paper with the cyan glow appearing to come from the graphite itself rather than the page surface, worn leather notebook, ceramic kettle, painted wood door. Mood: cliffhanger, mirror-inverted opening, a question alive in an empty room. Stylized 3D animation, smooth slow heartbeat-pulse on the cyan glow (NOT square-wave UI blink — must read as breathing, not as loading-screen), slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, DSLR macro, anime, moe, harsh black outlines, generic family-feature look, full-page glow (only the written line must glow), magenta crystal visible, turquoise/teal full-saturation glow, cyclops creatures in frame, the woman in frame (must be empty), sparkle, fairy trail, magic circle portal, gem counter HUD, loading-screen blink, square-wave pulse, fast strobe, oversaturated thriller vignette, melodramatic backlight
```

**Notas de direccion**: el glow es heartbeat smooth, NO UI blink. Si la imagen muestra blink-on / blink-off, falla la regla del style-guide (anti-loading-screen pulse). Es el espejo invertido del cold open: el cristal magenta se moria en silencio, ahora la pregunta se enciende en silencio. Sostener el frame mental cinco segundos antes del fade a negro. La luz bajo la puerta es el ancla emocional — Mariela no sabe lo que dejo vivo en su cocina.
