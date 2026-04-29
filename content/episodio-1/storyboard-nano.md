---
title: Storyboard — Prompts Nano Banana
description: Prompts image-to-image por escena para generar el storyboard visual del episodio 1
tool: Nano Banana (Gemini Image)
---

## Cómo usar estos prompts

- Cargá las **reference images en el orden indicado** por escena. La primera reference fija el character lock; las siguientes (portadas) actúan como mood/style reference. Si Nano Banana solo acepta una reference principal, usá el character lock como ancla y mencioná la portada como "tonal reference" en el campo de notas del UI.
- **Iteración en dos pasos:** primer pass con denoise alto (~0.7) para fijar composición y encuadre; segundo pass con denoise bajo (~0.25-0.35) usando el resultado anterior + la reference de personaje para clavar el character lock sin que mute el shading del style-guide.
- **Aspect ratio canónico: 16:9** en todos los prompts. No cambiar — el piloto entero es 16:9.
- El bloque **Style-lock** (sección siguiente) ya viene incluido al inicio de cada "Prompt visual" copiable. Si Nano Banana soporta system instructions persistentes, pegalo una sola vez ahí; si no, copialo antes del prompt de cada escena.

## Reference images disponibles

| Personaje / Asset | Ruta (relativa a `public/`) | Uso |
| --- | --- | --- |
| Jiggy | `images/personajes/jiggy.png` | character lock |
| Wiz | `images/personajes/wiz.png` | character lock |
| Byte | `images/personajes/byte.png` | character lock |
| Luxa | `images/personajes/luxa.png` | character lock |
| Zek | `images/personajes/zek.png` | character lock |
| Mariela | `images/personajes/mariela.png` | character lock |
| Portada 1 (acción frenética + paleta universo) | `images/portadas/portada.png` | mood/style reference (caverna activa) |
| Portada 2 (poster heroico grupal) | `images/portadas/portada2.png` | mood/style reference (caverna ceremonial) |

> Las portadas se usan como **style reference** únicamente para shots ambientados en Uray Pacha. NO se usan como mood reference para shots de Mariela (cocina/oficina/metro/calle): esos son tonal-opuestos por diseño.

## Style-lock (común a todas las escenas)

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (Pax cyclops 3-3.5 heads, Mariela softened cinematic-3D human), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]
```

---

## Escena 01 — Un cristal a punto de apagarse

**Beat narrativo**: el mundo se presenta por su síntoma — algo central acá se está muriendo y nadie llega a salvarlo.

**Reference images** (cargar en este orden):
1. `public/images/portadas/portada2.png` — mood/style reference (caverna ceremonial, atmósfera volumétrica densa)

**Prompt visual** (copiable):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (Pax cyclops 3-3.5 heads, Mariela softened cinematic-3D human), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Wide cinematic shot, slow descending crane move (24-28mm equivalent), of a vast nearly-dark subterranean cavern called Uray Pacha. A single low stalagmite at center holds an embedded magenta crystal the size of a fist, faintly pulsing — its emission almost spent, barely lighting itself. Dozens of empty hollow stalagmites surround it, dark and silent, telling a story of extinction without words. Rule of thirds: the dying crystal sits at lower-third intersection, leading lines of stalagmite tips converging on it. A single hairline shaft of pale-cyan ambient bioluminescence slices vertically from a fissure in the rock ceiling, catching slow-falling dust particles in suspension. In the deep background, a tiny still silhouette stands motionless — unreachable, not approaching. Palette: deep purple cavern #4B2E80 and blue-violet shadows #0E0820, struggling magenta core #FF49B4 on the central crystal, hairline pale-cyan #7FFFD4 in the ceiling shaft, no warm tones. Texture: rough porous igneous matte rock with thin mineral veining, glassy multifaceted crystal with hairline cooling cracks, dense volumetric haze with dust motes catching cyan light. Mood: silent agony, curiosity at the edge of grief. Rendered as stylized 3D animation cinematic, high-contrast neon-magic lighting, marked bloom on the dying magenta emissive, painterly background, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, 3D render look, generic family-feature animation look, anime, moe, harsh black outlines, oversaturated, flat cel-shading, dungeon RPG cliche, treasure chest, torch on wall, sword, dragon, magic circle portal, glowing eyes on background silhouette, game HUD, gem counter, mini-map, loading bar, low-contrast soft lighting, thriller vignetting, beauty-shot DOF
```

**Notas de dirección**: el espectador tiene que sentir que llegó a un velorio sin saberlo. La silueta del fondo no es amenaza ni misterio — es duelo. Si el cristal magenta brilla más de lo "casi-apagado", se rompe el arco emocional con escena-13. Mantener el shaft cyan finísimo: es semilla subliminal de la activación que viene en B14.

---

## Escena 02 — Los que esperan

**Beat narrativo**: la inacción es la decisión — saben que no pueden bajar a buscar la chispa, tienen que esperar que llegue desde arriba.

**Reference images** (cargar en este orden):
1. `public/images/personajes/wiz.png` — character lock para Wiz
2. `public/images/personajes/byte.png` — character lock para Byte
3. `public/images/personajes/zek.png` — character lock para Zek
4. `public/images/portadas/portada2.png` — mood/style reference

**Prompt visual** (copiable):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (Pax cyclops 3-3.5 heads, Mariela softened cinematic-3D human), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Wide reverse shot of the same dim Uray Pacha cavern, locked-off camera (28mm equivalent). In the deep middle ground, three small cyclops Pax silhouettes stand still on a worn stone ledge, viewed from behind and slightly to the side: Wiz (see ref) in front, leaning on his wooden staff with the violet-magenta crystal tip catching faint magenta rim light, his white beard and deep-purple hooded robe forming a clear vertical silhouette; behind and to the left Byte (see ref), his over-ear headphones glowing dim lime green #A7F432 in two soft halos against the dark; behind and to the right Zek (see ref), the visor of his purple cap catching one single edge of magenta light, his shoulders relaxed but his head tilted up. Wiz looks toward a hairline fissure in the cavern ceiling where a thin shaft of pale-cyan #7FFFD4 light leaks through. The dying magenta crystal from scene 1 still sits in the lower foreground, unfocused but present. Composition: rule of thirds, three Pax silhouettes clustered on the right third, ceiling fissure on upper-left third, dying crystal as out-of-focus foreground anchor. Palette: deep purple #4B2E80 and blue-violet shadow #0E0820 dominate, faint magenta #E83FC8 rim on Wiz's staff, lime #A7F432 only on Byte's headphone LEDs, sodium-free, gold-free. Mood: collective contemplation, weight, the stillness of waiting. Dense volumetric haze, slow dust falling through the cyan shaft. Stylized 3D animation, semi-realistic PBR with subsurface scattering on green-turquoise skin, high-contrast neon-magic lighting, painterly volumetric background, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature animation, harsh black outlines, four-eyed characters, two eyes per Pax (Pax are cyclops with one central eye), oversaturated, action pose, combat stance, fantasy battle cliche, sword, dragon, glowing magic circle, game HUD, mini-map, gem counter, thriller vignette, glamour DOF
```

**Notas de dirección**: la quietud es la actuación. Si cualquiera de los tres parece "en pose" o "en formación heroica" se contamina con la portada-1 (acción frenética) — acá es lo opuesto. Wiz mira la grieta del techo, no el cristal: ya sabe que la salvación no está abajo. Confirmar UN solo ojo central en cada Pax — image-gen tiende a meter dos.

---

## Escena 03 — Mariela en la oficina

**Beat narrativo**: presentamos a la protagonista por su funcionamiento — eficiente, invisible, automática.

**Reference images** (cargar en este orden):
1. `public/images/personajes/mariela.png` — character lock para Mariela

**Prompt visual** (copiable):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (Pax cyclops 3-3.5 heads, Mariela softened cinematic-3D human), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Medium shot, locked-off (35mm equivalent), of Mariela (see ref) — the woman from reference image, mid-thirties, dark brown hair pulled back in a low ponytail, sober blouse, thin metal-framed glasses with a single hairline scratch on the right lens — sitting at her cubicle desk in a small Providencia, Santiago office at 18:47 on a weeknight. She is half-turned toward her monitor, her face competent and vacant, eyes flat on a spreadsheet showing pivot tables with yellow and red highlighted cells reflected faintly in her lenses. A cold mug of coffee sits beside the keyboard. A small picture frame holds a photo of an 8-year-old niece, placed without prominence. A male coworker passes behind her dropping a manila folder on the corner of her desk — captured mid-stride, slightly out of focus. Eight other identical cubicle dividers recede in shallow depth behind her under cool fluorescent 4500K ceiling lighting. A wall clock reading 18:47 is visible in the background. Composition: rule of thirds, Mariela on the left third, fluorescent ceiling line on upper third, depth receding into pale gray cubicle field. Palette: cool fluorescent white #DDE3E8, dusk-blue shadow #2A3A5A, muted desk neutrals — strictly no magenta, no turquoise, no Pax-palette accents anywhere in frame. Mood: clinical, competent emptiness, automation as armor. Texture: matte fabric blouse, brushed steel keyboard, slight specular on coffee mug rim, fluorescent lighting flat and even. Stylized 3D animation, semi-realistic PBR softened cinematic human, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, DSLR portrait, glamour beauty lighting, anime, moe, big anime eyes, exaggerated cartoon proportions, harsh black outlines, magenta crystal, turquoise glow, neon, fantasy elements, Pax cyclops in frame, mystical glow, thriller vignette, dramatic chiaroscuro, telenovela lighting, oversaturated
```

**Notas de dirección**: la oficina debe leerse como cualquiera, no como "oficina de personaje". Si aparece UN solo elemento mágico (cristal, glow magenta, partícula cyan) se rompe el contraste fundacional con la caverna — la regla es CERO Pax-palette en este beat. Mariela no es triste; es operativa. Esa diferencia es todo.

---

## Escena 04 — La libreta en el metro

**Beat narrativo**: aparece el objeto-símbolo — la libreta — y se establece en un solo gesto que hace medio año que no la usa.

**Reference images** (cargar en este orden):
1. `public/images/personajes/mariela.png` — character lock para Mariela

**Prompt visual** (copiable):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (Pax cyclops 3-3.5 heads, Mariela softened cinematic-3D human), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Medium shot (35-50mm equivalent), locked-off, framed slightly low to feel like a fellow passenger's eyeline, of Mariela (see ref) standing inside a packed Santiago Metro Línea 5 car at evening rush hour. She holds the stainless overhead handrail with her right hand, the strap of a worn shoulder bag on her left arm, surrounded by the soft blur of other commuters in winter coats reading phones. Her left hand has just opened a small A6 brown leather notebook with a sun-faded elastic band and a fine crack along the spine — held at chest height, the page she is looking at is the last entry: three handwritten lines in her own pencil reading "groceries / call mom / fix printer", dated six months ago. Her face is held one beat too long over the page, faint micro-expression of recognition without softness. Practical fluorescent metro lighting overhead, cool greenish-white #C4D8DE, with intermittent dusk-blue #2A3A5A light bleeding through the windows from the tunnel. Composition: rule of thirds, Mariela in the left third with the notebook held at lower-third intersection, leading lines of the metro car ceiling and handrails converging into shallow depth on the right third. Palette: cool fluorescent green-white, dusk blue, muted winter coat blacks and grays, faint warm tungsten of a single overhead bulb pocket — no Pax-palette accents. Texture: worn leather notebook with fingerprint-smoothed cover and elastic band, brushed steel handrail with soft specular, matte coats. Mood: dead habit, small private weight. Stylized 3D animation, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, DSLR portrait, glamour beauty DOF, magenta neon, turquoise crystal glow, Pax cyclops, fantasy elements, anime, moe, big anime eyes, harsh black outlines, oversaturated, thriller vignetting, dramatic chiaroscuro, empty deserted metro car (must read as packed), action pose
```

**Notas de dirección**: el plano tiene que sentir invasión cotidiana, no "soledad poética". El vagón está LLENO y eso amplifica su aislamiento. La libreta es protagonista pero no se ilumina ni brilla — todavía no. Si aparece glow cyan en la grieta del lomo acá, se quema el reveal de B6.

---

## Escena 05 — La cocina, antes de escribir

**Beat narrativo**: ella decide sentarse — no escribe todavía, pero ya se está dando permiso.

**Reference images** (cargar en este orden):
1. `public/images/personajes/mariela.png` — character lock para Mariela

**Prompt visual** (copiable):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (Pax cyclops 3-3.5 heads, Mariela softened cinematic-3D human), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Medium-wide shot (35mm equivalent), locked-off, of a small kitchen in a Ñuñoa apartment, Santiago, at sunset. Mariela (see ref) stands at the kitchen counter beside a stovetop where an old aluminum kettle has just begun to hiss, her body angled three-quarters toward the window. Through the window: Santiago skyline at dusk, smog-pink sky #E8A0A0 fading to cool dusk-blue #5A6E8A, the Andes barely visible as silhouette. Her own reflection is faintly held in the window glass, ghosted over the city. A single warm Edison-style tungsten bulb #FFD08A hangs as a pendant lamp over a small wooden table, pooling warm light on the surface. On the table: the brown leather A6 notebook from scene 4 placed flat, a sharpened wooden pencil pulled from a small ceramic cup. Mariela's posture is quiet, hands resting at her sides, just looking at her own reflection one beat too long. Tile floor #D8CFC2 with grout lines. Composition: rule of thirds, Mariela in the right third, window with reflection in the upper-left third, table with notebook in lower-left third — the two anchors of the scene. Palette: warm tungsten #FFD08A pool on table, dusk-blue #5A6E8A from window, muted ceramic neutrals, no Pax-palette glow. Texture: worn ceramic kettle with brushed-steel handle, matte wood table, soft cotton blouse fabric. Mood: contemplative, suspended, the second before a decision. Stylized 3D animation, soft warm haze in the bulb pool, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, DSLR, glamour beauty lighting, anime, moe, big anime eyes, harsh black outlines, magenta neon, turquoise crystal glow, Pax cyclops in frame, fantasy elements, mystical aura around Mariela, thriller vignette, telenovela melodrama lighting, oversaturated, kitchen straight from a TV cooking show
```

**Notas de dirección**: el reflejo en la ventana es el corazón del plano. Si la imagen lo pierde o lo pone solo decorativo, el beat no funciona — ella está viéndose a sí misma decidir. La cocina es chica, modesta, real; nada de "kitchen porn" de revista. Tungsten warm es la ÚNICA fuente cálida del kay-pacha humano hasta acá.

---

## Escena 06 — La pregunta

**Beat narrativo**: la regla mágica del universo se activa — alguien arriba escribe una pregunta sincera por primera vez en mucho tiempo.

**Reference images** (cargar en este orden):
1. `public/images/personajes/mariela.png` — character lock para Mariela (mano y antebrazo)

**Prompt visual** (copiable):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (Pax cyclops 3-3.5 heads, Mariela softened cinematic-3D human), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Tight overhead shot (50-85mm equivalent), slow inferred push-in, of Mariela's left hand from reference image, holding a sharpened wooden pencil over an open A6 brown leather notebook on a small wooden kitchen table. The page is freshly blank, just past a previous entry of three pencil lines. She has just finished writing in tentative, hesitant cursive — the kind of handwriting from someone out of practice — the words "Why did I stop writing here?" in soft graphite. The pencil tip rests at the end of the question mark, lifted a millimeter. On the spine of the notebook, where a hairline crack runs along the worn leather, an almost imperceptible thread of pale-cyan #7FFFD4 light glows for one breath at no more than 5% opacity — barely visible, easy to miss on first watch. Behind the hand, the kettle on the stove has just clicked off on its own, slightly out of focus. Warm tungsten #FFD08A pool from a single Edison pendant lights the page from above-left, casting soft shadow of the pencil across the paper. Composition: centered on the page with hand entering from lower-right, rule of thirds anchors the written line on upper-third, notebook spine on left-third where the cyan hint lives. Palette: warm tungsten #FFD08A dominant, dusk-blue #2A3A5A in deep shadow, paper cream #F0E8D8, graphite gray on the line, hairline pale-cyan #7FFFD4 at 5% on the spine. Texture: matte uncoated paper, worn fingerprint-smoothed leather spine with visible fiber crack, sharpened pencil with subtle graphite specular. Mood: intimate, contained seismic event. Stylized 3D animation, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic skin pores, hyperrealistic, DSLR macro, glamour DOF, magenta crystal, turquoise glow on hand, anime, moe, harsh black outlines, fantasy magic circle, glowing portal, sparkles, fairy dust, full visible cyan spine glow above 5% (must remain near-subliminal), oversaturated, thriller vignette, loading-screen UI pulse, square-wave blink on cyan hint
```

**Notas de dirección**: el cyan en la grieta del lomo es la regla del universo asomando — tiene que ser CASI invisible. Si el espectador lo nota la primera vez, está mal. La letra es protagonista: titubeante, lenta, humana. El kettle apagándose solo en segundo plano es subtextual, no lo enfoques. Este es el shot más importante del episodio — es el "encendido" silencioso.

---

## Escena 07 — Byte detecta la pregunta

**Beat narrativo**: abajo se enteran — y por primera vez algo se mueve.

**Reference images** (cargar en este orden):
1. `public/images/personajes/byte.png` — character lock para Byte
2. `public/images/personajes/wiz.png` — character lock para Wiz
3. `public/images/portadas/portada2.png` — mood/style reference

**Prompt visual** (copiable):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (Pax cyclops 3-3.5 heads, Mariela softened cinematic-3D human), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Medium two-shot (50mm equivalent), locked-off with a 5-degree slight Dutch tilt, of Byte (see ref) and Wiz (see ref) in the dim Uray Pacha cavern. Byte stands in the foreground three-quarters facing camera, his pointed elastic ears just having flicked alert, his over-ear headphones glowing brighter lime-green #A7F432 than before, his single turquoise eye widened with pupil enlarged. His right hand is pressed two-fingered against the right earcup. He is mid-turn toward Wiz. Wiz stands behind him to the right, his single eye closed for one beat with his white beard catching faint magenta rim light from his staff's violet-magenta crystal tip — staff held vertical, just beginning to lift to point toward an off-screen passage to the right. Around them, dense volumetric haze, slow-falling dust catching faint magenta and cyan ambient light. The dying magenta crystal from scenes 1-2 sits as out-of-focus background anchor in the lower-left. Composition: rule of thirds, Byte in the left third, Wiz in the right third, slight Dutch tilt creates contained alarm without melodrama. Palette: deep purple #4B2E80 cavern base, blue-violet #0E0820 shadow, magenta #E83FC8 rim from Wiz's staff, lime green #A7F432 emissive on Byte's headphones (slightly intensified vs scene 2), turquoise #2EE0C8 on both single eyes. Texture: green-turquoise cyclops skin with subsurface scattering, matte purple velvet on Wiz's robe with thread weave, glossy plastic on Byte's headphones with bright LED. Mood: alert, the cavern's first inhalation in hours. Stylized 3D animation, marked bloom on lime headphone LEDs, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, anime, moe, two eyes per Pax (Pax must be cyclops, ONE central eye only), big anime eyes, harsh black outlines, generic family-feature look, fantasy battle stance, sword, magic circle, gem counter HUD, loading bar, oversaturated, thriller vignette, action movie pose, lightning bolts
```

**Notas de dirección**: la dirección de luz de Wiz tiene que coincidir con escena-02 (rim magenta desde su propio staff) — son el mismo lugar y el mismo momento del día subterráneo. La escena se "lee" como un latido: el lime de Byte sube de intensidad por primera vez. Si la imagen mete teatralidad (gestos amplios, gritos), se rompe el código del universo: la magia es susurrada.

---

## Escena 08A — El lápiz apretado (cocina)

**Beat narrativo**: la regla mágica del universo se demuestra. Acá. Sin que nadie la diga. (Plano A del match-cut, ~3 segundos.)

**Reference images** (cargar en este orden):
1. `public/images/personajes/mariela.png` — character lock para Mariela (mano)

**Prompt visual** (copiable):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (Pax cyclops 3-3.5 heads, Mariela softened cinematic-3D human), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Extreme close-up macro shot (100-150mm equivalent), locked-off, of Mariela's left hand from reference image, fingers gripping a sharpened wooden pencil so tightly that knuckles whiten faintly under softened cinematic-3D skin shading and the paper below shows visible compression marks under the lead. The frame holds tight on the pencil tip pressed against the page just below the handwritten line "Why did I stop writing here?", a single grain of graphite on the page surface catching the warm tungsten #FFD08A pool from above. Her hand trembles a fraction of a millimeter — captured as micro-blur on the pencil shaft's tip only. Background out of focus: the cream of the page, the shadow of the spine, the table edge. Composition: centered macro hero, rule of thirds places the written line at upper-third, pencil tip at center anchor, graphite grain catching highlight at lower-third. Palette: warm tungsten #FFD08A dominant, paper cream #F0E8D8, graphite gray, deep dusk-blue #2A3A5A in shadow corners — no Pax-palette glow at all in this plate. Texture: matte uncoated paper, sharpened cedar pencil with grain visible, soft skin with subtle subsurface scattering on knuckle, faint specular on polished pencil shaft. Mood: contained seismic moment, the millisecond before a cosmos rearranges. Stylized 3D animation, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic skin pores, hyperrealistic macro, DSLR product shot, glamour beauty DOF, magenta neon, turquoise crystal glow, Pax cyclops, sparkles, fantasy magic, anime, moe, harsh black outlines, oversaturated, thriller vignette, dramatic chiaroscuro, hand model glamour
```

**Notas de dirección**: cero magia visible en este plato — la magia está en el match-cut con 8B, no en el frame. Si aparece cualquier glow Pax-palette acá, se rompe la sorpresa. La compresión del papel debajo del lápiz es el detalle hero: muestra cuánto está apretando sin mostrar emoción en cara.

---

## Escena 08B — La palma de Wiz (caverna)

**Beat narrativo**: la regla mágica del universo se demuestra. Acá. Sin que nadie la diga. (Plano B del match-cut, ~12 segundos, hard cut desde 8A.)

**Reference images** (cargar en este orden):
1. `public/images/personajes/wiz.png` — character lock para Wiz (palma + ojo en foco suave atrás)
2. `public/images/portadas/portada2.png` — mood/style reference

**Prompt visual** (copiable):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (Pax cyclops 3-3.5 heads, Mariela softened cinematic-3D human), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Extreme close-up macro shot (100-150mm equivalent), locked-off, of Wiz's right palm from reference image — a small four-fingered cyclops hand with green-turquoise #21D8B6 skin, slightly knotted with age, opened upward in deep cavern darkness. Above the palm, hovering exactly two centimeters above the skin, a small newly-formed magenta crystal #FF49B4 with #E83FC8 rim has just materialized — dense, faceted, with hairline cooling cracks visible at its edges, glassy multifaceted body holding internal subsurface emission, pulsing strongly once mid-frame. The crystal casts warm magenta rim light onto the skin of the palm and faint magenta bloom into the surrounding volumetric haze. In soft focus directly behind the palm, Wiz's single turquoise #3FE0C8 eye watches the crystal — not with surprise, with recognition; the eye partly visible above the white beard which catches faint magenta edge light. Dense particulate cavern haze surrounds the moment, dust motes spiraling slowly inward toward the new crystal as if drawn to it. Composition: extreme centered hero on the floating crystal, palm forming the foreground curve, eye in upper-third soft-focus background, rule of thirds places the crystal exactly at the optical center. Palette: magenta #FF49B4 core and #E83FC8 rim dominant, deep purple #4B2E80 ambient, blue-violet #0E0820 shadow, turquoise #21D8B6 on palm skin and #3FE0C8 in the soft-focus eye, no warm tones, no cyan, no gold. Texture: glassy multifaceted crystal with internal emission and hairline cooling cracks, soft green-turquoise cyclops skin with marked subsurface scattering, matte white beard with fine fiber detail. Mood: silent revelation, the universe quietly proving its rule. Stylized 3D animation, marked bloom on the new crystal, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic skin pores, hyperrealistic, DSLR macro, two eyes (must be cyclops, single eye only), five fingers (must be 4-fingered cyclops hand), anime, moe, big anime eyes, harsh black outlines, generic family-feature look, sword, dragon, magic circle portal, sparkle burst, fairy dust, lightning, gem counter HUD, oversaturated, loading-screen blink pulse, square-wave flash, glamour beauty DOF
```

**Notas de dirección**: este es el otro hero shot del episodio junto con B6. El cristal aparece — no se ensambla, no se construye en pantalla, no tiene FX trail. Está / no está. Una sola pulsación fuerte. Si la imagen agrega "magic forming animation" se contamina con fantasy cliche. La cara de Wiz no muestra sorpresa: muestra reconocimiento. Coordinar con el editor: hard cut desde 8A con un frame de silencio total, sin transición FX.

---

## Escena 09 — Wiz reconoce, Jiggy y Luxa cargan

**Beat narrativo**: la chispa nueva pasa de manos — abajo se confirma que esta sí es real, y arranca el relevo hacia arriba.

**Reference images** (cargar en este orden):
1. `public/images/personajes/wiz.png` — character lock para Wiz
2. `public/images/personajes/jiggy.png` — character lock para Jiggy
3. `public/images/personajes/luxa.png` — character lock para Luxa
4. `public/images/portadas/portada2.png` — mood/style reference

**Prompt visual** (copiable):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (Pax cyclops 3-3.5 heads, Mariela softened cinematic-3D human), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Medium-tight three-shot (50mm equivalent), locked-off slightly low, in the dim Uray Pacha cavern. Wiz (see ref) stands center-left holding the newly-formed magenta crystal #FF49B4 floating two centimeters above his right palm, his single turquoise eye fixed on it, a single slow tear caught mid-fall trapped in his white beard catching faint magenta rim light. Jiggy (see ref) enters from frame-left already mid-motion, his right hand opened upward, his single turquoise eye wide and ready, leather harness across his chest, lower body angled into a runner's pre-stride — captured at the exact frame where Wiz is placing the magenta crystal #FF49B4 onto Jiggy's right palm. Simultaneously, Luxa (see ref) enters from frame-right barely slowing, her purple headband catching faint warm light, her tribal multicolor poncho flowing, pressing a smaller golden-warm crystal #FFE34D into Jiggy's left palm without making eye contact — already pivoting back into the dark. Jiggy's two crystals now read clearly: magenta on the right hand, warm gold on the left. Around them dense volumetric haze, magenta and faint gold pools of light overlapping for the only time in the episode. Composition: rule of thirds, Wiz on the left third with the magenta exchange at center anchor, Luxa exiting on the right third with gold trail, Jiggy as the connective figure spanning the middle. Palette: magenta #E83FC8 core / #FF49B4 from Wiz's new crystal, warm gold #FFE34D / #F1E3AA from Luxa's crystal (visiting warmth, the only gold in any cavern shot), turquoise #21D8B6 cyclops skin, deep purple #4B2E80 ambient, blue-violet #0E0820 shadow. Texture: glassy faceted crystals with internal emission, worn leather harness on Jiggy with brass buckle, woven multicolor tribal cloth on Luxa with visible thread weave, matte purple velvet on Wiz with deep folds. Mood: reverence, urgent handoff, three-second window of converging warmth. Stylized 3D animation, marked bloom on both crystals, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, anime, moe, two eyes per Pax (must be cyclops single eye), five-fingered hands (must be four-fingered), big anime eyes, harsh black outlines, generic family-feature look, group-pose hero formation (must read as motion not pose), magic circle, sparkle burst, lightning, sword, gem counter HUD, oversaturated thriller, glamour DOF, melodramatic pose
```

**Notas de dirección**: este es el ÚNICO momento del piloto donde gold y magenta coexisten en cuadro — es la negociación de paletas que el style-guide protege. Si Luxa se queda demasiado en el plano se vuelve grupo-pose; tiene que sentirse "pase de testigo en relevo". La lágrima de Wiz es chica, contenida, atrapada en la barba — no una lágrima de close-up emocional barato. Confirmar 4 dedos por mano y 1 ojo central por personaje.

---

## Escena 10 — El cruce a la superficie

**Beat narrativo**: el cristal dorado de Luxa demuestra su función — Jiggy puede cruzar sin que los drones lo registren.

**Reference images** (cargar en este orden):
1. `public/images/personajes/jiggy.png` — character lock para Jiggy
2. `public/images/personajes/zek.png` — character lock para Zek (en túnel detrás)

**Prompt visual** (copiable):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (Pax cyclops 3-3.5 heads, Mariela softened cinematic-3D human), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Wide low-angle shot (24mm equivalent), looking up from beneath a rectangular cast-iron sewer grate set into the asphalt of Avenida Bilbao, Ñuñoa, Santiago, around 10pm. The grate's vertical bars stripe the frame against the night sky; an old sodium streetlamp #FF8A30 hangs above-left casting orange cone light across the asphalt and through the grate slats. The street is empty. Three storeys above in the night sky, two small spherical black anti-body drones with single magenta #E83FC8 LEDs patrol in slow lateral sweep — visible through the grate slats. Just below the grate in a strip of darkness, Jiggy (see ref) stands looking up: the magenta crystal #FF49B4 closed in his right fist (faint glow leaking between his fingers), the warm gold crystal #FFE34D resting open on his left palm. His single turquoise eye reflects the sodium orange in a faint warm rim — the first time Pax skin meets warm tungsten/sodium light in the episode. He has just brushed the gold crystal once with his left thumb; the gold pulses subtly, and the nearest drone's LED is mid-drift, rotating exactly 30 degrees off-axis as if its scan target slipped. Behind Jiggy in the deeper dark of the access tunnel, Zek (see ref) stands with his purple cap tilted, boombox at his hip, having just struck it once — a faint sub-tonal pressure visible as soft displacement of dust haze in the tunnel air. Composition: rule of thirds, grate vertical lines as foreground graphic, Jiggy in lower-right third, sodium streetlamp in upper-left third, drones in upper-right third silhouetted, Zek as soft out-of-focus depth anchor in the back. Palette: sodium orange #FF8A30 (exclusive to this beat), night-blue #2A3A5A sky, drone magenta #E83FC8 LED accents, magenta #FF49B4 leaking from Jiggy's right fist, warm gold #FFE34D on his left palm, turquoise #21D8B6 cyclops skin. Texture: cast-iron grate with rust and chipped paint, asphalt with grain, glassy crystals with internal emission, brushed plastic on drone shells. Mood: stealth, the magic rule made visible in geometry — drones drift, do not flee. Stylized 3D animation, slight haze in the streetlamp cone, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, DSLR night photo, anime, moe, big anime eyes, harsh black outlines, generic family-feature look, action chase pose, drones firing or attacking, magic circle portal, lightning bolt from crystal, glowing fairy trail, gem counter HUD, mini-map, two eyes per Pax (must be cyclops), five-fingered hands, oversaturated thriller vignette, glamour DOF, fully-lit street (must be sparse sodium pool only)
```

**Notas de dirección**: los drones no son enemigos en pantalla — son rutina ambiental que se desvía. Si la imagen los muestra "reaccionando" o "alertados", se rompe la regla del cristal dorado (no los huye, los re-rutea). El sodio naranja es ÚNICO de este beat en todo el piloto — usar sin miedo. Jiggy con rim sodium en piel turquoise es el preview tonal del crossover de B11.

---

## Escena 11 — La entrega invisible

**Beat narrativo**: el manifiesto del proyecto pasa físicamente — el calorcito en el pecho deja de ser metáfora y se vuelve plano de cine.

**Reference images** (cargar en este orden):
1. `public/images/personajes/mariela.png` — character lock para Mariela
2. `public/images/personajes/jiggy.png` — character lock para Jiggy

**Prompt visual** (copiable):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (Pax cyclops 3-3.5 heads, Mariela softened cinematic-3D human), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Medium shot (50mm equivalent), locked-off, same kitchen and same framing as scene 5/6 but later in the night — the tea cup beside Mariela now visibly cold, condensation dried. Mariela (see ref) sits at the small wooden table with the open notebook in front of her, her left hand resting flat on the table beside the page with the question, her right hand about to close the cover. From behind the refrigerator on the left side of frame, Jiggy (see ref) emerges low and quiet, walking with the careful gait of someone delivering something heavy and small — invisible to her, fully present to the camera. He approaches her left hand, his own right palm open holding the magenta crystal #FF49B4 from scene 8B, and gently presses it against her palm. On Jiggy's body in this single frame, the lighting integrates a warm tungsten #FFD08A rim from the kitchen pendant on his right shoulder side and a soft magenta #E83FC8 rim from his own crystal on his left side — a complementary warm-cool gradient over his green-turquoise skin. This is the only shot in the episode where Pax-palette and human-kitchen-palette negotiate on the same body. Mariela's face holds a micro-shift: a small hardness softens; her hand twitches once, lifts an inch, presses to her own chest. Jiggy is already turning to leave. Composition: rule of thirds, Mariela on the right two-thirds with notebook, Jiggy on the left third entering low, the contact point of palms anchored at center horizon. Palette: warm tungsten #FFD08A pool dominant, dusk-blue #2A3A5A in shadow, magenta #FF49B4 / #E83FC8 contained to Jiggy and his crystal only, turquoise #21D8B6 on Jiggy's skin. Texture: matte wooden table with cup-ring marks, soft cotton on Mariela's blouse, worn leather harness on Jiggy, glassy magenta crystal with internal emission. Mood: warm domestic miracle, the project's manifesto in a single physical gesture. Stylized 3D animation, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, DSLR portrait, glamour beauty DOF, anime, moe, big anime eyes, harsh black outlines, generic family-feature look, two eyes on Jiggy (must be cyclops single eye), five-fingered Pax hand, Mariela seeing Jiggy / looking at Jiggy (must remain unaware), magic circle, sparkle burst, fairy trail, gem counter HUD, oversaturated thriller, dramatic chiaroscuro, telenovela melodrama lighting
```

**Notas de dirección**: la regla central del plano: Mariela NO ve a Jiggy. La cámara sí. Si el image-gen acomoda los ojos de Mariela hacia Jiggy, está mal. La "mezcla de paletas" sobre el cuerpo de Jiggy es la única excepción del piloto al separation strict warm/cool entre mundos — usar el rim doble como demostración técnica del crossover, no como magia generalizada en el cuarto.

---

## Escena 12 — "Okay"

**Beat narrativo**: la transformación de Mariela cabe en una sola sílaba — y eso es suficiente.

**Reference images** (cargar en este orden):
1. `public/images/personajes/mariela.png` — character lock para Mariela

**Prompt visual** (copiable):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (Pax cyclops 3-3.5 heads, Mariela softened cinematic-3D human), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Tight medium shot (85mm equivalent), locked-off, of Mariela (see ref) seated at the small kitchen table — her right hand closed gently against her own sternum, fingers cupped around an invisible warmth, her gaze on the open notebook page with her own handwritten line "Why did I stop writing here?" still on it. Her face does not break into emotion: instead, the corners of her mouth lift half a centimeter, hold for one beat, then settle. Behind her, the cold tea cup is visible beside the kettle, and she is mid-rise with body language that reads "going to refill". A single Edison-style tungsten #FFD08A pendant pours warm light from above-left, its pool slightly shifted from earlier scenes — the first warm key in the kitchen has imperceptibly intensified by 5%, a residue of the crystal exchange. Faint warm-tungsten residue glow at 8% opacity on Mariela's left palm where she received the crystal — barely visible, easy to miss. Composition: rule of thirds, Mariela in the right third in seated three-quarter pose, notebook in lower-left third, kettle and tea cup as soft background anchors. Palette: warm tungsten #FFD08A dominant (slightly intensified), dusk-blue #2A3A5A in shadow corners, paper cream and pencil graphite on the visible page, no Pax-palette glow visible in frame except the subliminal palm residue. Texture: matte wooden table, soft cotton blouse, ceramic kettle with brushed-steel handle, paper, faint warm subsurface on her skin where the crystal was pressed. Mood: minimal reconciliation, the first warm tone the kitchen has truly held, the second before she stands up. Stylized 3D animation, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic skin pores, hyperrealistic, DSLR portrait, glamour beauty lighting, anime, moe, big anime eyes, harsh black outlines, big smile (must be sub-centimeter mouth corner shift), tears streaming, melodrama, magenta crystal visible, turquoise glow, Pax cyclops in frame, fantasy element, sparkle, magic aura around Mariela, thriller vignette, telenovela close-up, oversaturated, full-bright key light
```

**Notas de dirección**: este es el "tono mayor" del episodio — pero es chiquito. Si la sonrisa pasa de medio centímetro, mata el plano. El residue cyan/warm en su palma debe ser casi invisible (8% máx) — es el espejo del cyan en el lomo de B6, pero ahora warm. La intensificación del tungsten es subliminal: nadie tiene que notar que la luz cambió, solo sentir que la cocina dejó de estar fría.

---

## Escena 13 — Wiz y Jiggy abajo: "esta se queda"

**Beat narrativo**: por primera vez en el episodio, las estalagmitas vacías empiezan a brillar — el lugar deja de morir.

**Reference images** (cargar en este orden):
1. `public/images/personajes/wiz.png` — character lock para Wiz
2. `public/images/personajes/jiggy.png` — character lock para Jiggy
3. `public/images/portadas/portada2.png` — mood/style reference

**Prompt visual** (copiable):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (Pax cyclops 3-3.5 heads, Mariela softened cinematic-3D human), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Wide shot (28mm equivalent), slow descending camera, of the Uray Pacha qhocha cavern. Wiz (see ref) stands center-left in three-quarter back view, his deep-purple hooded robe and white beard reading clearly, his staff held lightly, his single eye watching a wayra current — a slow upward spiral of dust motes rising through the ceiling fissure, lit by a slightly warmer-than-before pale-cyan #7FFFD4 shaft (now at 25% opacity vs 15% in scene 1). Jiggy (see ref) has just run back into frame from the right, breath heavy, hands empty — no magenta crystal, no gold crystal — his harness slightly askew, posture still in arrival decel. Around the two figures, two of the previously-empty hollow stalagmites closest to Wiz now hold faint magenta #FF49B4 emission at low intensity — small new crystals reawakening in their cores. The dying central crystal from scene 1 now reads slightly stronger as well. Just two stalagmites lit, not more — but a clear contrast to scene 2 where none glowed. Composition: rule of thirds, Wiz on the left third, Jiggy on the right third arriving in frame, the ceiling fissure shaft on upper-third as vertical compositional anchor, the two reawakening stalagmites in lower-third base. Palette: magenta #FF49B4 / #E83FC8 in the new stalagmite glows and central crystal, deep purple #4B2E80 ambient, blue-violet #0E0820 shadow, pale-cyan #7FFFD4 in the ceiling shaft (subtly intensified), turquoise #21D8B6 cyclops skin, no warm tones, no gold. Texture: matte porous igneous rock with mineral veining, glassy newly-forming crystals with hairline cooling cracks, dense volumetric haze with rising dust, matte purple velvet on Wiz, worn leather on Jiggy. Mood: sustained relief, an open question, the place no longer dying. Stylized 3D animation, marked bloom on the new emissive stalagmites, slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, anime, moe, big anime eyes, harsh black outlines, generic family-feature look, every stalagmite glowing brightly (must be only 2 reawakening), action stance, magic circle, sparkle burst, lightning, sword, dragon, two eyes per Pax (must be cyclops), five-fingered hands, oversaturated, thriller vignette, glamour DOF
```

**Notas de dirección**: SOLO dos estalagmitas se reactivan — el cuento es la fragilidad de la recuperación, no la fiesta. Si la imagen llena la caverna de glow, mata el arco con el episodio 2. AVISO PARA EDITOR: en post-producción se inserta aquí, durante ~80ms, una chispa-ancla pale-dusty-gold #D9C28A (anchor-spark, B13B exclusivo del style-guide) — NO la incluir en este prompt; es un insert manual fuera del scope de Nano Banana. Reservá ese frame en montaje.

---

## Escena 14 — La libreta brilla sola

**Beat narrativo**: el episodio cierra abriendo — la pregunta queda viva mientras ella ya se fue a dormir.

**Reference images** (cargar en este orden):
1. (sin character lock — ningún personaje en cuadro)
2. `public/images/personajes/mariela.png` — opcional, solo como tonal reference para los neutros del cuarto

**Prompt visual** (copiable):

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (Pax cyclops 3-3.5 heads, Mariela softened cinematic-3D human), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]

Tight overhead push-in shot (50-85mm equivalent), slow inferred dolly forward, of the small wooden kitchen table at night — the kitchen empty of people. The open A6 brown leather notebook lies on the table, page facing up showing the handwritten pencil line "Why did I stop writing here?". The line itself emits a soft pulsing pale-cyan #7FFFD4 glow at approximately 70% opacity, breathing in slow heartbeat-rate sine wave — only the line glows, not the rest of the page. The kitchen pendant Edison bulb #FFD08A is still on, casting its warm pool over the table from above-left, holding a second tea cup beside the kettle (the one she just drank). In the background through an internal doorway visible at frame-edge, the bedroom door is closed and a thin warm strip of light spills from beneath it across the tile floor — Mariela is sleeping there, off-screen. Composition: rule of thirds, the glowing handwritten line at center anchor for the push-in, kettle and second cup in upper-left third, bedroom door light strip in lower-right third, the warm pendant pool framing top-left. Palette: pale-cyan #7FFFD4 (now dominant on the line, the activation made visible), warm tungsten #FFD08A pool, dusk-blue #2A3A5A in shadow, paper cream, leather brown on notebook spine, faint pale-cyan still on the spine crack at 5% as continuity from scene 6. Texture: matte uncoated paper with the cyan glow appearing to come from the graphite itself rather than the page surface, worn leather notebook, ceramic kettle, painted wood door. Mood: cliffhanger, mirror-inverted opening, a question alive in an empty room. Stylized 3D animation, smooth slow heartbeat-pulse on the cyan glow (NOT square-wave UI blink — must read as breathing, not as loading-screen), slight film grain, 16:9 aspect ratio.
```

**Negative prompt**:

```
photorealistic, hyperrealistic, DSLR macro, anime, moe, harsh black outlines, generic family-feature look, full-page glow (only the written line must glow), magenta crystal visible, turquoise/teal full-saturation glow, Pax cyclops in frame, Mariela in frame (must be empty), sparkle, fairy trail, magic circle portal, gem counter HUD, loading-screen blink, square-wave pulse, fast strobe, oversaturated thriller vignette, melodramatic backlight
```

**Notas de dirección**: el glow es heartbeat smooth, NO UI blink. Si la imagen muestra blink-on / blink-off, falla la regla del style-guide (anti-loading-screen pulse). Es el espejo invertido del cold open: el cristal magenta se moría en silencio, ahora la pregunta se enciende en silencio. Sostener el frame mental cinco segundos antes del fade a negro. La luz bajo la puerta es el ancla emocional — Mariela no sabe lo que dejó vivo en su cocina.
