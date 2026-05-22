---
title: Concept arts y first-frames — Nano Banana
description: Prompts para generar todos los assets que faltan antes de usar el storyboard y los prompts Seedance del episodio 1
tool: Nano Banana (Gemini Image)
---

## Cómo usar este archivo

- **Generá los HERO assets primero** con seed fijo (ver "Orden de generación" abajo). Anotá el seed que usaste — lo vas a reusar al regenerar variaciones del mismo HERO.
- **Después generá los DERIVADOS**, pasando el HERO correspondiente como `@image1` (image-to-image con denoise bajo, 0.25-0.35) para mantener la identidad visual del prop o la locación.
- **Después generá los first-frames de Seedance**, pasando como references el concept art de la locación + los character lock PNGs que ya existen en `public/images/personajes/`.
- **Cuando regeneres algo, usá el mismo seed.** Cambiar seed = cambiar identidad. Si necesitás iterar la composición, primero variá CFG/steps con seed fijo; recién después tocá el seed.
- **Inglés 100% en los prompts.** Cero jerga del worldbuilding (Uray Pacha, qhocha, wayra, chasqui, Pax, Kay-pacha) — todo descrito visualmente.
- **Aspect ratio canónico: 16:9** en todos los assets.
- **No subas foto real humana** a ningún slot. Mariela siempre va via su PNG character-lock generado por IA.

---

## Orden de generación recomendado

### Bloque A — HEROs reusables (generar primero, seed fijo, anotar seed)

1. `concept-cave-wide-dark` — base de todas las escenas de caverna
2. `concept-notebook-hero` — base de TODOS los derivados de libreta
3. `concept-mariela-kitchen-table-hero` — base de mesa de cocina (todos los planos overhead viven acá)
4. `concept-mariela-kitchen-dusk` — base de cocina al atardecer
5. `concept-mariela-kitchen-night` — base de cocina de noche
6. `concept-cave-stalagmites-reawakening` — variante de caverna (escena 13), comparte DNA con #1
7. `concept-office-cubicles-cool` — oficina Mariela
8. `concept-metro-line5-evening` — vagón metro
9. `concept-bilbao-grate-night` — calle Av. Bilbao

### Bloque B — Derivados (referencian un HERO como @image1)

10. `concept-notebook-on-table-dusk` ← deriva de #2 + #4
11. `concept-notebook-overhead-blank` ← deriva de #2 + #3
12. `concept-notebook-spine-crack-macro` ← deriva de #2
13. `concept-notebook-question-written` ← deriva de #11
14. `concept-cyclops-palm-macro` ← deriva de #1 + char-lock Wiz
15. `concept-kitchen-empty-glowing-notebook` ← deriva de #5 + #2
16. `concept-notebook-line-glowing-cyan` ← deriva de #13

### Bloque C — First-frames Seedance (referencian concepts + character locks)

17. `first-frame-escena-01` ← #1 + portada2.png
18. `last-frame-escena-01` (= `first-frame-escena-02`) ← #1 + char locks Wiz/Byte/Zek
19. `first-frame-escena-05` ← #4 + char lock Mariela
20. `first-frame-escena-06A` ← #11 + char lock Mariela
21. `last-frame-escena-06A` (= `first-frame-escena-06B`) ← #13 + char lock Mariela
22. `first-frame-escena-07` ← #1 + char locks Byte + Wiz
23. `first-frame-escena-08A` ← #13 + char lock Mariela
24. `first-frame-escena-08B` ← #14
25. `last-frame-escena-08B` (= `first-frame-escena-09`) ← #14 + char lock Wiz
26. `first-frame-escena-10` ← #9 + char locks Jiggy + Zek
27. `first-frame-escena-11` ← #5 + char locks Mariela + Jiggy
28. `last-frame-escena-11` (= `first-frame-escena-12`) ← #5 + char lock Mariela
29. `first-frame-escena-13` ← #6 + char lock Wiz
30. `first-frame-escena-14` ← #5 + #16

**Total: 30 assets a generar.**

---

## Style-lock (común a TODOS los prompts)

> Pegá este bloque al inicio de cada prompt Nano Banana. Si Nano Banana soporta system instructions persistentes, cargalo una sola vez ahí.

```
[Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cartoon proportions (small bipedal cyclops creatures around 3-3.5 heads tall, softened cinematic-3D human for the woman character), high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8 + warm tungsten #FFD08A as situational accents), saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes and god rays, slight film grain, color grading complementary magenta and turquoise, 16:9. Reads as premium mobile-game cinematic / animated key art. Negative: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, cel-shaded flat, generic family-feature look, fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, loading-screen blinking pulse.]
```

---

# Bloque A — HEROs reusables

## `concept-cave-wide-dark`

**Aliases que cubre**: `concept-cave-fading-crystals`, `concept-cave-wide-establishing`
**Aparece en (storyboard)**: escenas 01, 02, 07, 09
**Aparece en (Seedance)**: escena 01 (T2V/I2V), escena 02 (background)
**Tipo**: HERO reusable. Generá UNO. NO regenerar entre shots — la consistencia de la caverna depende de eso.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | Mood reference (paleta + atmósfera caverna ceremonial) | `public/images/portadas/portada2.png` ✓ |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Wide cinematic establishing shot of a vast subterranean cavern, almost completely dark. At dead center of the lower third, a single low stalagmite of porous igneous rock holds a fist-sized magenta crystal #FF49B4 with #E83FC8 rim — its emission almost spent, barely lighting itself, glowing at roughly 30 percent of full intensity. Dozens of empty hollow stalagmites of varying sizes recede into deep blue-violet shadow on all sides, dark and crystalless, telling a story of extinction without words. A single hairline shaft of pale-cyan #7FFFD4 ambient light slices vertically from a thin fissure in the rock ceiling at upper-left third, catching slow-falling dust motes in suspension at roughly 15 percent opacity. Dense volumetric haze fills the air. No characters in frame. Mood and atmosphere consistent with @image1 (mood reference). Composition: rule of thirds, dying crystal at lower-third intersection, ceiling shaft on upper-left third, leading lines of stalagmite tips converging on the central crystal. Palette: deep purple cavern #4B2E80, blue-violet shadow #0E0820, struggling magenta core #FF49B4 on the central crystal, hairline pale-cyan #7FFFD4 in ceiling shaft, no warm tones, no gold. Texture: rough porous igneous matte rock with thin mineral veining, glassy multifaceted crystal with hairline cooling cracks, dense volumetric haze with dust motes. Mood: silent agony, a world quietly going extinct. 16:9.

Negative: photorealistic, hyperrealistic, anime, moe, cel-shaded flat, 2D hand-drawn, harsh black outlines, oversaturated, multiple bright crystals, lava, fire, torches, treasure chest, dragon, sword, magic circle portal, glowing eyes, characters in frame, generic dungeon RPG look, generic family-feature animation, thriller vignette, low-contrast soft, fully lit cavern.
```

**Notas**:
- El cristal central debe estar al ~30% de brillo. Si Nano Banana lo pone full-bloom, regenerá — el arco con escena 13 depende de que este se vea moribundo.
- SOLO un cristal emisivo en frame. Si aparecen más de uno encendido, regenerá.
- Anotá el seed. Vas a reusarlo en `concept-cave-stalagmites-reawakening` (denoise bajo, mismo set).

---

## `concept-notebook-hero`

**Aliases que cubre**: `concept-notebook-leather-worn`, `concept-notebook-with-crack`
**Aparece en (storyboard)**: escenas 04, 05, 06, 08A, 11, 12, 14 (vía derivados)
**Aparece en (Seedance)**: escenas 04, 05, 06A, 06B, 08A, 14
**Tipo**: HERO reusable. Es el prop más visible del piloto — su identidad debe ser ABSOLUTA. Generá UNO y reusá vía derivados.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| ninguna — generación T2V pura | — | — |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Hero product-style three-quarter shot of a small A6 leather-bound notebook resting on a neutral dark surface. The cover is fingerprint-smoothed worn brown leather #6B4A2E with subtle tonal variations, slightly darkened at the corners from years of being held. A faded sun-bleached elastic band #A8927A wraps vertically around the cover, its color desaturated from sun exposure indicating the notebook has been carried in bags and pockets for years. Along the spine of the binding, a fine hairline crack runs the full length of the leather — a single thin fiber-deep fissure, no wider than a hair, slightly more visible at the lower third of the spine. The notebook is closed. Subtle leather grain visible under soft three-quarter key light. The page edges are slightly cream #F0E8D8, uneven from manual cutting, not machine-trim. Composition: notebook centered with slight three-quarter rotation showing both cover and spine, neutral dark cool background #2A2A30 to make leather pop, soft top-left key light with cool dusk-blue rim from upper-right, mild specular catching the elastic band edge. Palette: worn brown leather #6B4A2E, faded elastic #A8927A, paper cream #F0E8D8 on visible edges, dark neutral background #2A2A30, no fantasy colors, no glow, no emissive. Texture: matte worn leather with subtle skin-of-leather grain, faded woven elastic with visible thread weave, paper edge fibers visible. Mood: quietly cherished object, a tool held many times. 16:9.

Negative: photorealistic skin pores on leather, hyperrealistic stock photo, glamour product shot, glossy leather, brand new pristine notebook, large gaping crack on spine (must be hairline only), fantasy element, magic glow, cyan emission visible, magenta accent, watermark, text overlay, brand logos, anime, moe, 2D hand-drawn, cel-shaded flat, harsh black outlines, oversaturated.
```

**Notas**:
- Este HERO se usa como `@image1` en TODOS los derivados de libreta. Si Nano Banana drifta el lomo o la elastic band entre derivados, regenerá el derivado pasando este HERO con denoise más bajo (0.2).
- La grieta del lomo es **load-bearing**: es lo que se enciende cyan en escena 06B. Confirmá que sea visible-pero-fina antes de aprobar el HERO.
- Anotá el seed. Es el seed más importante del piloto después del de Mariela.

---

## `concept-mariela-kitchen-table-hero`

**Aparece en (storyboard)**: escenas 05, 06, 08A, 11, 12, 14 (vía derivados)
**Aparece en (Seedance)**: escenas 05, 06, 08A, 11, 12, 14 (vía derivados)
**Tipo**: HERO reusable. La superficie de mesa es la base del 30% de los planos overhead del piloto.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| ninguna — generación T2V pura | — | — |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Overhead three-quarter shot of a small wooden kitchen table for two, photographed from a 35-degree angle showing both the surface and one chair. The tabletop is solid pine #C9A877 with visible long-grain wood grain running parallel to the long edge, two faint concentric mug-ring stains near the center where someone has set hot drinks for years, a few hairline scratches catching light at oblique angle, one small chip on the front-right corner. The table is approximately 80cm long. One simple wooden chair #A88860 with a slightly worn seat cushion in muted ochre cotton sits angled against it. The surrounding floor visible at frame edges is ceramic tile #D8CFC2 with darker grout lines, slightly worn at corners. Background out of focus, suggesting a domestic kitchen interior. Composition: rule of thirds, table fills lower two-thirds of frame, chair on right third, soft falloff to dark interior at upper-left and upper-right corners. Palette: warm pine #C9A877 with darker grain #8E6A3F, ochre cushion #B8924E, ceramic tile floor #D8CFC2, neutral cool background falloff #3D3D45, no fantasy palette, no emissive. Texture: matte unvarnished wood with visible grain and aging marks, soft cotton cushion fabric, ceramic tile with slight specular at edges, no glossy surfaces. Mood: lived-in modest domestic, a real table where someone has eaten alone many times. 16:9.

Negative: photorealistic interior magazine shot, glamour kitchen porn, marble countertops, designer furniture, brand new pristine table, glossy varnish, fantasy element, magic glow, cyan emission, magenta accent, watermark, brand logos, anime, moe, 2D, cel-shaded flat, oversaturated, kitchen straight from a TV cooking show.
```

**Notas**:
- Mug-ring stains en el centro — son el ancla de continuidad para los planos overhead. Si los derivados los pierden, se nota.
- El cushion ochre evita confusión con el dorado de Luxa: es muted, no saturado.

---

## `concept-mariela-kitchen-dusk`

**Aparece en (storyboard)**: escena 05
**Aparece en (Seedance)**: escena 05 (concept de locación)
**Tipo**: HERO reusable. Es la cocina al atardecer — humo rosa en ventana, sin lámpara prendida todavía o recién encendida.
**Deriva de**: `concept-mariela-kitchen-table-hero` — pasar como `@image1` con denoise medio (0.4-0.5)

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-mariela-kitchen-table-hero | (generar primero) |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Medium-wide interior shot of a small Ñuñoa Santiago apartment kitchen at dusk, around 7:30 PM in winter, framing as established by the table set in @image1. The kitchen is approximately 3 meters wide. A gas stovetop with an old aluminum kettle sits on the right side of frame, the kettle's brushed-steel surface catching faint cool light. A single Edison-style tungsten pendant bulb #FFD08A hangs above the small wooden kitchen table from @image1, just turned on, its filament glowing amber-warm and beginning to pool a small warm circle on the tabletop. Through a window on the left side of frame: Santiago city skyline at dusk, smog-pink sky #E8A0A0 fading upward to cool dusk-blue #5A6E8A, the distant Andes mountain range barely visible as silhouette. A faint reflection of the room is held in the window glass. A small ceramic cup holding three sharpened wooden pencils sits on the corner of the counter. A small fridge #E8E0D2 visible in deep background on the left, modest and worn. Tile floor #D8CFC2 with grout lines visible. Composition: rule of thirds, window with city view in left third, kitchen table with bulb pool in lower-right third, stovetop with kettle on right, fridge as soft anchor in upper-left depth. Palette: warm tungsten #FFD08A pool around the bulb (small, just-on intensity), dusk-blue #5A6E8A from window, smog-pink #E8A0A0 in upper window, ochre tile #D8CFC2, neutral wood and ceramic, no fantasy palette glow anywhere. Texture: matte wood and ceramic, brushed steel kettle, painted refrigerator, soft tile floor, glass window with subtle reflections. Mood: contemplative cool-warm crossover, the second before someone comes home. 16:9.

Negative: photorealistic interior shot, glamour kitchen, magazine cover composition, marble surfaces, designer fixtures, fantasy element, magenta crystal, turquoise glow, cyclops creature, anime, moe, 2D hand-drawn, cel-shaded flat, oversaturated, thriller vignette, telenovela melodrama lighting, kitchen straight from a TV cooking show, brand logos.
```

**Notas**:
- La ventana es el corazón del HERO — el reflejo y el atardecer son parte del beat de escena 05. Si Nano Banana entrega ventana sin reflejo o sin atardecer, regenerá.
- Bulbo recién encendido (small warm pool, NO full saturation). En `concept-mariela-kitchen-night` el pool va más amplio.

---

## `concept-mariela-kitchen-night`

**Aliases que cubre**: `concept-mariela-house-kitchen` (cuando se usa para vista nocturna)
**Aparece en (storyboard)**: escenas 11, 12, 14
**Aparece en (Seedance)**: escenas 11, 12, 14 (concept de locación)
**Tipo**: HERO reusable. Misma cocina, ventana ya oscura, bulbo full-pool.
**Deriva de**: `concept-mariela-kitchen-dusk` — pasar como `@image1` con denoise medio (0.4)

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-mariela-kitchen-dusk | (generar primero) |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Medium-wide interior shot of the same small Ñuñoa Santiago apartment kitchen depicted in @image1, now at night around 10:30 PM. The window on the left side now shows full night: deep night-blue #1A2330 sky with scattered city lights as small warm pinpoints in the distance, no atmospheric glow remaining, the Andes silhouette no longer visible. The single Edison-style tungsten pendant bulb #FFD08A above the small wooden kitchen table is now fully lit, casting a wider warm pool that covers most of the tabletop and softens onto the closest tile floor. A modest white refrigerator #E8E0D2 stands on the left side of frame between the window and the table, its surface catching faint warm rim from the bulb on its right edge and faint cool dusk-blue rim from the window on its left. The aluminum kettle on the gas stovetop sits cool, no steam. Tile floor #D8CFC2 with grout lines visible, slightly more shadow at edges than the dusk version. Composition: rule of thirds, refrigerator as soft anchor on left third, table with bulb pool in center-right, window with night sky in upper-left third, stovetop on right. Palette: warm tungsten #FFD08A pool dominant (wider than dusk version), dusk-blue #2A3A5A in shadow corners and from window, ochre tile #D8CFC2, neutral wood and ceramic, no fantasy palette glow anywhere. Texture: same matte wood and ceramic and steel, painted refrigerator surface with subtle texture, glass window now showing only night reflections of the room. Mood: late, intimate, settled, a kitchen at the end of the day. 16:9.

Negative: photorealistic interior shot, glamour kitchen porn, magazine composition, fantasy element, magenta crystal in frame, turquoise glow, cyclops creature visible (Jiggy enters in a different prompt), anime, moe, 2D, cel-shaded flat, oversaturated, thriller vignette, telenovela lighting, brand logos, watermark, fully bright kitchen (must keep warm pool with shadow corners), full daylight visible through window.
```

**Notas**:
- La heladera a la izquierda del frame es **load-bearing** — Jiggy emerge desde detrás de ella en escena 11. Si Nano Banana la pone en otro lado, regenerá.
- Window: night sky con city lights pinpoints (NO atardecer, NO total black). Si entrega ventana plana negra, regenerá.

---

## `concept-cave-stalagmites-reawakening`

**Aparece en (storyboard)**: escena 13
**Aparece en (Seedance)**: escena 13 (concept de locación)
**Tipo**: HERO reusable, derivado de la caverna pero con reactivación visible.
**Deriva de**: `concept-cave-wide-dark` — pasar como `@image1` con denoise medio (0.4-0.5)

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-cave-wide-dark | (generar primero) |
| `@image2` | Mood reference | `public/images/portadas/portada2.png` ✓ |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Wide cinematic shot of the same vast subterranean cavern as @image1, but visibly less dead now. The central low stalagmite still holds the original magenta crystal, now glowing slightly stronger than before — roughly 45 percent intensity instead of 30. Two of the previously empty stalagmites nearest to the central one now hold faint magenta emission #FF49B4 at low intensity, small new crystals reawakening in their cores at roughly 30 percent intensity each — only TWO stalagmites lit, not more, the rest remain empty and dark. The pale-cyan #7FFFD4 shaft from the ceiling fissure has slightly intensified, now at roughly 25 percent opacity instead of 15 percent, and a slow upward spiral of fine dust motes is visibly rising through the shaft — the air is moving for the first time. Dense volumetric haze fills the lower air. No characters in frame. Atmosphere matches @image2 (mood reference). Composition: rule of thirds, the central crystal at lower-third intersection, the two reawakening stalagmites flanking it in lower third, ceiling shaft on upper-left third with rising dust spiral as vertical anchor. Palette: magenta #FF49B4 / #E83FC8 in the three glowing crystals (slightly warmer overall than scene 1 but still cool-dominant), deep purple cavern #4B2E80, blue-violet shadow #0E0820 (slightly less pronounced), pale-cyan #7FFFD4 in ceiling shaft, no warm tones, no gold. Texture: rough porous igneous rock with mineral veining, glassy newly-forming crystals with hairline cooling cracks at edges, dense volumetric haze with rising dust motes. Mood: sustained relief, the place no longer dying, a fragile recovery. 16:9.

Negative: photorealistic, hyperrealistic, anime, moe, every stalagmite glowing brightly (must be only 2 reawakening plus the original central one), full-bright cavern, fantasy battle scene, sword, dragon, magic circle, sparkle burst, lightning, oversaturated, generic dungeon RPG look, characters in frame, cel-shaded flat, harsh black outlines, gold tone, warm light source, lava, fire.
```

**Notas**:
- SOLO dos estalagmitas se reactivan, además de la central. Si Nano Banana ilumina más de eso, mata el arco con el episodio 2 — regenerá.
- El dust spiral ascendente es la lectura visual del air-current entre mundos. Si la imagen lo pierde, regenerá.

---

## `concept-office-cubicles-cool`

**Aliases que cubre**: `concept-office-mariela-cubicles`, `concept-office-cubicle-mariela`
**Aparece en (storyboard)**: escena 03
**Aparece en (Seedance)**: escena 03 (concept de locación)
**Tipo**: HERO. Una sola escena, pero con paleta tan específica que merece HERO seed.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| ninguna — generación T2V pura | — | — |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Wide cinematic interior shot of a small open-plan office in Providencia Santiago at end of workday, around 6:45 PM on a weekday. Approximately nine identical grey cubicle workstations #B8BEC4 arranged in three rows of three, dividers at chest height, each with a generic monitor showing spreadsheet windows. One cubicle in the foreground (slightly emphasized via composition) has a small framed photo of an 8-year-old child on the desk, a ceramic mug, and a closed leather notebook beside the keyboard. Cool fluorescent ceiling tubes #DDE3E8 glow even and flat across the room with the slight greenish tint typical of office tube lights. Beige low-pile carpet #C2B59C visible at floor level. A wall clock reading 6:47 PM is mounted on the far wall. Through a small distant window in deep background, dusk-blue #5A6E8A from outside is barely visible. A photocopier sits along the right wall in deep depth. The space is mundane, lived-in, slightly tired — not glamorous, not designer. No people in frame. Composition: rule of thirds, foreground cubicle in lower-right third, wall clock in upper-left third, depth of cubicle field receding into pale gray on the left, fluorescent tube as horizontal anchor on upper third. Palette: cool fluorescent white #DDE3E8 dominant with slight green tint, dusk-blue #5A6E8A from distant window, beige carpet #C2B59C, muted desk neutrals, generic gray cubicle dividers, strictly no magenta, no turquoise, no fantasy palette accents, no warm pockets. Texture: matte fabric cubicle dividers with subtle weave, brushed plastic keyboards, slight specular on monitor screens, low-pile carpet, generic office furniture surfaces. Mood: clinical competent emptiness, the absence of color as a design statement. 16:9.

Negative: photorealistic interior photo, glamour office shot, designer co-working space, modern startup-loft aesthetic, magenta neon, turquoise glow, fantasy elements, anime, moe, big anime eyes, cyclops creatures, harsh black outlines, oversaturated, thriller vignette, telenovela lighting, watermark, brand logos, employees in frame, characters visible, dramatic chiaroscuro.
```

**Notas**:
- CERO paleta fantástica. Si Nano Banana mete UN solo glow magenta o cyan "para llenar", regenerá. La regla del style-guide es absoluta acá.
- Si entrega oficina demasiado moderna/diseñada, regenerá pidiendo "1990s-2000s standard corporate office, not startup".

---

## `concept-metro-line5-evening`

**Aliases que cubre**: `concept-metro-car-rush-hour`
**Aparece en (storyboard)**: escena 04
**Aparece en (Seedance)**: escena 04 (concept de locación)
**Tipo**: HERO. Una sola escena.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| ninguna — generación T2V pura | — | — |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Interior medium-wide shot of a packed Santiago Line 5 metro car at evening rush hour, around 7:15 PM. The car interior is scuffed brushed-metal #9CA3AB with worn plastic seats #5C6470, vertical chrome handrails running floor to ceiling at intervals, horizontal handrails at standing height with hanging straps. The car is densely packed with adult commuters in winter coats #2A2D33 and #3D4148 in muted blacks and grays, viewed from a slightly low angle as if the camera were standing among them. None of the commuter faces are detailed — they are softly out of focus, reading phones or staring blankly forward. Through the car windows on both sides, dark tunnel walls flash past with intermittent flicker as the train passes tunnel lights, brief streaks of cool blue-white. A red emergency hammer in a small bracket is visible mid-wall in deeper background. The cool-blue interior fluorescent tubes #C4D8DE overhead flatten the lighting with slight greenish tint typical of metro lighting. Composition: rule of thirds, vertical handrail in left third as foreground graphic, blurred crowd filling middle and right two thirds, ceiling tube as horizontal anchor on upper third. Palette: cool fluorescent green-white #C4D8DE, dusk-blue #2A3A5A through windows, muted winter coat blacks #2A2D33 and grays #5C6470, brushed metal #9CA3AB, scuffed plastic, no warm tones except a single faint tungsten pocket from one overhead bulb in deep background, no fantasy palette accents. Texture: scuffed brushed metal walls, worn plastic seats, brushed steel handrails with soft specular, matte heavy winter coat fabric, glass windows. Mood: invasive cotidian, the loneliness of being surrounded. 16:9.

Negative: photorealistic crowded photo, hyperrealistic interior shot, glamour subway scene, empty pristine metro car (must read as packed), modern designer transit, fantasy elements, magenta crystal, turquoise glow, cyclops creatures, anime, moe, big anime eyes, harsh black outlines, oversaturated, thriller vignette, action chase, watermark, brand logos visible on coats, characters with detailed expressive faces in foreground.
```

**Notas**:
- Faces blurred / no detalladas — si Nano Banana enfoca a un commuter random, regenerá. Mariela entra en el first-frame, no acá.
- LLENO, no vacío. "Packed" es load-bearing.

---

## `concept-bilbao-grate-night`

**Aliases que cubre**: `concept-street-grate-low-angle-night`
**Aparece en (storyboard)**: escena 10
**Aparece en (Seedance)**: escena 10 (concept de locación)
**Tipo**: HERO. Sodium-orange-only beat.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| ninguna — generación T2V pura | — | — |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Wide low-angle exterior shot looking up from beneath a rectangular cast-iron sewer grate set into the asphalt of a wide avenue in Ñuñoa Santiago, around 10:00 PM on a quiet weekday. The grate's vertical iron bars #2C2622 with rust patches stripe the upper two-thirds of the frame, viewed from below. Through the grate slats, the empty avenue above is visible: aged asphalt #3D3835 with hairline cracks, a single old sodium-vapor streetlamp #FF8A30 (~2000K) hanging on a tall metal post on the left side casting an orange cone of light across the asphalt and through the grate slats, partially illuminating the bars in warm orange. The street is empty — no cars, no people. Three storeys above the street in the night sky, two small spherical black surveillance drones #1A1A1F with single magenta #E83FC8 LED indicator lights patrol in slow lateral sweep, visible through the grate slats and against the deep night-blue #1A2330 sky. Just below the grate, the tunnel interior is dark and damp, faint mineral residue on tunnel walls. Composition: rule of thirds, grate vertical bars as foreground graphic stripe, sodium streetlamp in upper-left third, two drones silhouetted in upper-right third against night sky, asphalt and street ground in middle. Palette: sodium orange #FF8A30 (exclusive to this beat in the entire pilot), night-blue #1A2330 sky, drone magenta #E83FC8 LED accents (small dots), cast-iron rust #2C2622, asphalt gray-black #3D3835, deep tunnel shadow below, no other colors, no warm tungsten, no cyan. Texture: cast-iron grate with rust patches and chipped paint, aged asphalt with crack texture, glassy magenta LED on drone shells, brushed plastic on drone bodies, slight haze in the streetlamp cone. Mood: sparse stealth, the city as patient ambient surveillance, neither hostile nor welcoming. 16:9.

Negative: photorealistic night street photo, hyperrealistic urban shot, fully-lit street (must be sparse sodium pool only), brand logos, anime, moe, harsh black outlines, oversaturated, thriller vignette, drones firing or attacking or in aggressive pose, drone red LEDs (must be magenta), warm tungsten visible, fantasy elements, magic circles, lightning, watermark, characters in frame, busy night street with cars, modern futuristic drones (must read as utilitarian patrol).
```

**Notas**:
- Sodium #FF8A30 es ÚNICO de este asset en todo el piloto. Usar sin miedo, NO mezclar con tungsten warm.
- Drones con LED magenta SMALL (puntos), no glow burst. Si Nano Banana hace drones con glow grande, regenerá — drift hacia "menacing villain".

---

# Bloque B — Derivados

## `concept-notebook-on-table-dusk`

**Aparece en (storyboard)**: escena 05
**Tipo**: derivado.
**Deriva de**: `concept-notebook-hero` + `concept-mariela-kitchen-table-hero` — pasar ambos como references con denoise bajo (0.3)

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-notebook-hero | (generar primero) |
| `@image2` | concept-mariela-kitchen-table-hero | (generar primero) |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Three-quarter medium close-up of the brown leather A6 notebook from @image1 placed flat on the wooden kitchen table from @image2, photographed from a 30-degree angle looking down. The notebook is closed with its faded elastic band wrapped vertically, its identity matching @image1 exactly (same worn leather grain, same hairline crack along the spine, same faded elastic). Beside the notebook on the table, a single sharpened wooden pencil #C9A877 with a sharp graphite tip rests parallel to the notebook's long edge. Behind them, a small plain ceramic cup #E8E0D2 holds two more sharpened pencils standing upright as a holder. The wooden tabletop matches @image2 exactly (same pine grain, same mug-ring stains visible at the edges of frame, same hairline scratches). A single warm tungsten Edison-style bulb #FFD08A is just turned on above-left, casting a soft warm pool that lights the notebook cover and table surface from above-left at slight angle. The far edge of the table fades into cool dusk-blue shadow #5A6E8A from a window off-frame. Composition: rule of thirds, notebook on left two-thirds, pencil cup on right third, leading lines of wood grain converging into shallow depth. Palette: worn brown leather #6B4A2E, faded elastic #A8927A, warm pine table #C9A877, ceramic cream #E8E0D2, warm tungsten pool #FFD08A, dusk-blue shadow falloff #5A6E8A, no fantasy palette glow, no emissive. Texture: matte worn leather, faded woven elastic, matte unvarnished wood with grain visible, matte ceramic, sharpened cedar pencil. Mood: a tool placed deliberately, the second before someone sits down. 16:9.

Negative: photorealistic product photo, glamour stock shot, magazine composition, multiple notebooks, brand new pristine leather, fantasy element, magenta crystal, cyan glow, magical aura around the notebook, anime, moe, 2D, cel-shaded flat, oversaturated, thriller vignette, watermark, brand logos, hand visible in frame.
```

**Notas**:
- Si la libreta se ve diferente al HERO (color, grieta), regenerá con denoise más bajo (0.2).

---

## `concept-notebook-overhead-blank`

**Aparece en (storyboard)**: escena 06
**Tipo**: derivado.
**Deriva de**: `concept-notebook-hero` + `concept-mariela-kitchen-table-hero` — pasar ambos como references con denoise bajo (0.3)

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-notebook-hero | (generar primero) |
| `@image2` | concept-mariela-kitchen-table-hero | (generar primero) |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Tight overhead top-down shot, camera directly above the table, framed on the open A6 brown leather notebook from @image1 lying flat on the wooden kitchen table from @image2. The notebook is open showing both pages: the left page has a previous handwritten entry of three short pencil lines in fading graphite — intentionally illegible squiggles, just the indication of three lines of human cursive — while the right page is freshly blank cream paper #F0E8D8. A single sharpened wooden pencil rests diagonally on the right edge of the open notebook, tip pointing toward the blank page. The leather spine of the notebook runs vertically through the center of the frame; along it, the same hairline crack from @image1 is visible as a thin fiber-deep fissure. The tabletop wood grain visible at frame edges matches @image2 exactly. A warm tungsten Edison bulb #FFD08A from above-left casts a soft warm pool centered on the open pages, with subtle shadow of the pencil falling across the right page from upper-right. Composition: dead-center overhead with pages dominating frame, spine as vertical center line, blank right page in right half, written left page in left half. Palette: paper cream #F0E8D8, graphite gray on the left page squiggles, worn brown leather spine #6B4A2E, warm pine table at frame edges #C9A877, warm tungsten pool #FFD08A, dusk-blue shadow corners #2A3A5A, no fantasy palette glow. Texture: matte uncoated paper with subtle fiber texture, worn leather spine with visible hairline crack, matte wood grain at edges, sharpened cedar pencil. Mood: invitation, threshold, the second before something is written. 16:9.

Negative: photorealistic macro shot, glamour stationery photography, multiple notebooks, fully blank both pages (must show 3 lines on left page), readable text on left page (must be illegible squiggles), fantasy element, cyan glow on spine yet, magenta crystal, magical aura, anime, moe, 2D, cel-shaded flat, oversaturated, watermark, brand logos, hand or finger visible.
```

**Notas**:
- 3 líneas en página izquierda, blank en derecha. Si Nano Banana llena ambas o vacía la izquierda, regenerá.
- NO debe haber glow cyan en lomo en este derivado — eso es load-bearing del beat 06B, debe quedar invisible acá.

---

## `concept-notebook-spine-crack-macro`

**Aparece en (storyboard)**: escena 06
**Tipo**: derivado.
**Deriva de**: `concept-notebook-hero` — pasar como `@image1` con denoise muy bajo (0.2)

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-notebook-hero | (generar primero) |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Extreme macro close-up of the leather spine of the brown A6 notebook from @image1, photographed from the side at very close range showing only a 4cm horizontal section of the spine binding. The hairline crack from @image1 is now clearly visible running along the leather as a thin fiber-deep fissure roughly 2cm long, slightly widening at its center, the leather fibers exposed at the crack edges. The leather grain is highly visible: small worn smooth patches from years of being held, slight darkening at the binding fold, faint specular at the very edge where leather meets the page block. Behind the spine slightly out of focus, the cream page edges #F0E8D8 of the notebook are visible as a pale band. A warm tungsten light #FFD08A from above-left catches the leather and produces a faint specular highlight along the binding edge. Composition: extreme centered macro, the crack itself running horizontally across the lower-third anchor, leather grain dominating the frame, page edges as soft background band on upper third. Palette: worn brown leather #6B4A2E with darker fissure interior #4A2F1C, warm tungsten highlight #FFD08A on edge, paper cream #F0E8D8 in soft background, deep dusk-blue shadow corners #2A3A5A, no fantasy palette, no glow yet. Texture: ultra-detailed leather grain with visible fibers, smoothed worn patches, fissure interior showing exposed leather core, matte finish with edge specular. Mood: detail of an object hiding more than it shows, the moment before something happens. 16:9.

Negative: photorealistic leather product photo, hyperrealistic stock macro, glamour shot, brand new pristine leather, gaping wide crack (must be hairline only), cyan glow visible (must be unlit in this concept), magenta accent, fantasy element, watermark, brand logos, anime, moe, cel-shaded flat, oversaturated.
```

**Notas**:
- Sin glow cyan en este concept. El glow se compone en post sobre este still como mask emisivo.

---

## `concept-notebook-question-written`

**Aparece en (storyboard)**: escena 08A
**Tipo**: derivado.
**Deriva de**: `concept-notebook-overhead-blank` — pasar como `@image1` con denoise bajo (0.25)

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-notebook-overhead-blank | (generar primero) |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Tight overhead top-down shot of the same open A6 brown leather notebook on the wooden kitchen table as in @image1, identical composition and framing. The right page that was blank in @image1 now has a single line of handwritten cursive English text written in soft pencil graphite reading exactly "Why did I stop writing here?" — the handwriting is tentative, hesitant, slightly unsteady, the letters lean inconsistently as someone out of practice would write, the pencil pressure varying. The line sits roughly one-third down from the top of the right page. The pencil from @image1 is still resting diagonally to the right, tip near the end of the question mark. The hairline crack on the spine remains identical to @image1. Composition matches @image1 exactly. Palette: paper cream #F0E8D8, graphite gray on the line, worn brown leather spine #6B4A2E, warm pine table at edges #C9A877, warm tungsten pool #FFD08A, dusk-blue shadow corners #2A3A5A, no fantasy palette glow. Texture: matte paper, soft pencil graphite with subtle compression marks where pressed harder, leather spine, wood grain. Mood: contained seismic moment, a question written for no one. 16:9.

Negative: photorealistic macro photo, perfectly neat handwriting (must be tentative and unsteady), typed text, printed text, calligraphy, multiple lines (must be one line only), readable previous entry on left page (must remain illegible squiggles), fantasy element, cyan glow on spine (not yet visible), magenta crystal, anime, moe, watermark, brand logos.
```

**Notas**:
- La frase EXACTA: "Why did I stop writing here?" — si Nano Banana entrega texto distinto o squiggles, regenerá. Esta frase es load-bearing del piloto entero.
- Letra titubeante, NO caligráfica. Si sale prolija, regenerá.
- Asset alternativo recomendado: si Nano Banana es poco confiable con texto handwritten en inglés, usá `concept-notebook-overhead-blank` y compositá la frase en post (After Effects / DaVinci) usando una tipografía cursive handwritten consistente. Esa misma overlay se reutiliza en escena 14.

---

## `concept-cyclops-palm-macro`

**Aparece en (storyboard)**: escena 08B
**Tipo**: derivado.
**Deriva de**: `concept-cave-wide-dark` (atmósfera) + char lock Wiz (anatomía mano) — pasar ambos como references con denoise medio (0.4)

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | char lock Wiz | `public/images/personajes/wiz.png` ✓ |
| `@image2` | concept-cave-wide-dark (para atmósfera) | (generar primero) |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Extreme macro close-up of the right palm of the elder cyclops creature from @image1, an open hand with four-fingered anatomy (NOT five fingers), green-turquoise skin #21D8B6 with subsurface scattering visible, slightly knotted with age, palm fully open and empty facing upward in deep cavern darkness. The palm fills the lower-center of the frame. Behind the palm in soft focus, his single droopy-lidded turquoise eye #3FE0C8 is partially visible above his white voluminous beard, watching the empty palm intently with an expression of recognition (not surprise). The eye is in soft background focus, the palm in sharp foreground. Cavern atmosphere matches @image2 — dense particulate haze, almost total darkness around the palm, faint blue-violet ambient #0E0820 only on the cavern walls deep behind. Composition: extreme centered macro, palm fills lower two-thirds, eye in soft focus upper third, beard catching faint cool ambient at the bottom of frame. Palette: green-turquoise skin #21D8B6 with marked subsurface scattering, deep blue-violet ambient #0E0820 and #4B2E80, soft turquoise eye #3FE0C8 in background, faint cool ambient on white beard fibers, no warm tones, no magenta yet (the palm is empty in this concept), no gold. Texture: soft cyclops skin with marked subsurface scattering and faint subsurface emission, age lines on palm visible as shallow creases, white beard fiber detail in soft focus. Mood: stillness before revelation, the second before the universe quietly proves its rule. 16:9.

Negative: photorealistic skin pores, hyperrealistic, DSLR macro, two eyes (must be cyclops, one central eye), five fingers (must be four-fingered), six fingers, anime big-glossy-eyes, moe, harsh black outlines, magenta crystal already in palm (must be empty in this concept), turquoise glow on palm itself, sparkle, fantasy magic effect, lightning, watermark, brand logos, cel-shaded flat, oversaturated.
```

**Notas**:
- 4 dedos. Si Nano Banana entrega 5, regenerá hasta clavarlo. Anatomía cíclope es load-bearing.
- Palma vacía. El cristal aparece en Seedance, no en este concept.

---

## `concept-kitchen-empty-glowing-notebook`

**Aparece en (storyboard)**: escena 14
**Tipo**: derivado.
**Deriva de**: `concept-mariela-kitchen-night` + `concept-notebook-on-table-dusk` (composición mesa+libreta) — pasar ambos como references con denoise medio (0.4)

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-mariela-kitchen-night | (generar primero) |
| `@image2` | concept-notebook-hero | (generar primero) |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Medium-wide interior shot of the same Ñuñoa kitchen as @image1, now empty and quiet at late night around 11:30 PM, no people in frame. On the small wooden kitchen table at the center of the room, the brown leather A6 notebook from @image2 lies open page-up showing the recently written cursive English line "Why did I stop writing here?" on the right page (handwritten in soft pencil graphite, tentative cursive). A single sharpened wooden pencil rests beside it. A second drained ceramic mug of tea #E8E0D2 sits next to the kettle on the gas stovetop in soft mid-focus, indicating she had a second cup before going to sleep. The Edison-style tungsten pendant bulb #FFD08A is still on above the table, casting its full warm pool. Through an internal doorway visible at the right edge of frame, a closed bedroom door is barely seen; a thin warm strip of soft yellow light #F4D8A4 spills from beneath it across a small section of ceramic tile floor — indicating the inhabitant is sleeping behind the door. The window on the left shows full night-blue #1A2330 sky with scattered city light pinpoints. Composition: rule of thirds, table with open notebook in center-right at lower-third intersection, kettle and second mug in upper-left third, bedroom door light strip in lower-right third, hanging bulb pool framing top. Palette: warm tungsten #FFD08A pool dominant, dusk-blue #2A3A5A in shadow, paper cream #F0E8D8, worn brown leather, ceramic cream, soft yellow #F4D8A4 strip under bedroom door, no magenta crystal in frame, no turquoise emissive, no characters. Texture: matte wood, ceramic, leather, paper, painted door surface. Mood: cliffhanger, an empty room holding a question that is still alive. 16:9.

Negative: photorealistic, hyperrealistic, anime, moe, characters in frame (must be empty kitchen), cyclops creature visible, magenta crystal, turquoise crystal glow, fully bright cyan glow on notebook line (this concept holds no glow on the line yet — that is escena 14 Seedance/post layer), thriller vignette, glamour shot, watermark, brand logos, fully dark room (warm tungsten must be on), open bedroom door, person visible in bedroom.
```

**Notas**:
- En este concept la frase está escrita pero NO brilla cyan. El glow se compone en post como overlay emisivo.
- La franja de luz bajo la puerta es load-bearing emocional. Si Nano Banana la dropea, regenerá.

---

## `concept-notebook-line-glowing-cyan`

**Aparece en (storyboard)**: escena 14
**Tipo**: derivado.
**Deriva de**: `concept-notebook-question-written` — pasar como `@image1` con denoise muy bajo (0.2)

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-notebook-question-written | (generar primero) |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Tight overhead close-up of the open notebook page from @image1, identical composition and framing, focused on the right page where the handwritten cursive English line "Why did I stop writing here?" sits. The line itself now emits a soft pulsing pale-cyan glow #7FFFD4 at approximately 70 percent opacity — only the letterforms glow, not the rest of the page. The glow appears to come from within the graphite of the letters themselves, as if the pencil mark were back-lit, with a soft halo extending roughly 2-3mm around each letter. The rest of the page remains lit only by the warm tungsten pool from above. The handwriting itself remains identical to @image1 (same letterforms, same hesitant cursive, same position). The hairline crack on the spine glows very faintly pale-cyan as well at roughly 5 percent opacity, near-subliminal. No square-wave UI blink — the glow reads as smooth heartbeat-rate breathing, as if the page were alive. Composition matches @image1 exactly. Palette: pale-cyan #7FFFD4 dominant on the line (the activation made visible), warm tungsten #FFD08A pool on the rest of the page, paper cream #F0E8D8, worn brown leather spine #6B4A2E with hairline cyan glow at 5%, warm pine table edges #C9A877, dusk-blue shadow corners #2A3A5A. Texture: matte paper with cyan glow appearing to emanate from inside the graphite rather than the surface, worn leather spine, wood grain. Mood: cliffhanger, a question alive in an empty room, mirror-inverted opening of the episode. 16:9.

Negative: photorealistic, hyperrealistic, full-page glow (only the written line must glow), square-wave UI blink (must be heartbeat smooth sine), loading-screen pulse, magenta crystal visible, turquoise full-saturation glow, magic circle, sparkle burst, fairy trail, fantasy magic effect, anime, moe, harsh black outlines, oversaturated thriller, glamour macro shot, watermark, brand logos, characters in frame, hand visible.
```

**Notas**:
- Heartbeat smooth, NO blink. Si Nano Banana entrega un still y querés validar el "smooth" en post, generá 2-3 stills con distintas intensidades del glow (50%, 70%, 85%) y elegí — el video de escena 14 va a interpolar entre ellos en el push-in.
- Fallback recomendado: si Nano Banana no logra el glow cyan limpio en las letras, generá este still SIN glow y compositá el glow en post (mask emisivo sobre el path de las letras). Es el método más confiable según la nota del seedance-director.

---

# Bloque C — First-frames Seedance

## `first-frame-escena-01`

**Para**: clip Seedance escena 01 (15s, T2V/I2V).
**Tipo**: first-frame externo, opcional pero recomendado para mayor control.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-cave-wide-dark | (generar primero) |
| `@image2` | Mood reference | `public/images/portadas/portada2.png` ✓ |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Wide cinematic establishing first frame of a vast subterranean cavern, framing matching @image1 exactly but with the camera positioned slightly higher than the @image1 establishing — this is the start of a slow descending crane move, so the angle should be roughly 5 degrees more downward looking. The single low stalagmite at center holds the fist-sized magenta crystal #FF49B4 with #E83FC8 rim, faintly pulsing at approximately 30 percent intensity. Dozens of empty hollow stalagmites recede into deep blue-violet shadow. Hairline pale-cyan #7FFFD4 shaft from ceiling fissure at upper-left third, dust motes catching light. In the deep background at the far edge of visibility, a single tiny still silhouette of a small bipedal cyclops creature stands motionless, unidentifiable, just a shape, not a character. Mood and atmosphere consistent with @image2. Composition: rule of thirds, dying crystal at lower-third intersection, ceiling shaft on upper-left third, leading lines of stalagmite tips converging on the crystal, distant silhouette tiny in the deep background as a textural detail. Palette: deep purple #4B2E80, blue-violet shadow #0E0820, magenta core #FF49B4, hairline pale-cyan #7FFFD4, no warm tones. Texture: rough porous rock, glassy crystal with hairline cracks, dense volumetric haze. Mood: silent agony, a velorio without ceremony. 16:9.

Negative: photorealistic, anime, moe, multiple bright crystals, fully lit cavern, fantasy battle scene, dragon, treasure chest, recognizable character in background (must be unidentifiable silhouette), characters in foreground, magic circle, lightning, watermark, brand logos, cel-shaded flat, oversaturated, harsh black outlines, low contrast.
```

**Notas**:
- Este first-frame le da a Seedance el punto de partida exacto del crane move. Si lo omitís, Seedance hace T2V puro y el clip queda OK pero menos predecible.

---

## `last-frame-escena-01` (= `first-frame-escena-02`)

**Para**: cierre de escena 01 + apertura de escena 02. Encadenado continuous.
**Tipo**: last-frame de un clip + first-frame del siguiente.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-cave-wide-dark | (generar primero) |
| `@image2` | char lock Wiz | `public/images/personajes/wiz.png` ✓ |
| `@image3` | char lock Byte | `public/images/personajes/byte.png` ✓ |
| `@image4` | char lock Zek | `public/images/personajes/zek.png` ✓ |
| `@image5` | Mood reference | `public/images/portadas/portada2.png` ✓ |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Wide reverse cinematic shot of the same cavern as @image1, camera now lower and slightly angled to the side as if the slow descending crane of escena 01 has finished. The dying magenta crystal on the central stalagmite is visible mid-frame at lower-third anchor, faintly pulsing at 30 percent. In the deep mid-ground on a worn stone ledge in three-quarter back view, three small cyclops creatures stand motionless as pure silhouettes against the cavern's dim ambient: in the front the elder from @image2 (deep-purple hooded robe, white voluminous beard, leaning on a dark wooden staff with a violet-magenta crystal tip, the staff's crystal catching faint magenta rim light); behind him to the left @image3 (over-ear headphones with two soft lime-green LED halos #A7F432 the only bright accent on his silhouette, pointed elastic ears alert); behind him to the right @image4 (purple visor cap whose brim catches one single edge of magenta light, shoulders relaxed, head tilted up). All three are mostly black silhouettes — no facial detail visible — readable only by these three diagnostic features (staff-crystal, lime LEDs, cap brim). The elder is facing toward the hairline ceiling fissure on upper-left third where the pale-cyan #7FFFD4 shaft filters down. Atmosphere matches @image5. Composition: rule of thirds, three silhouettes clustered on the right third on the ledge, ceiling fissure on upper-left third, dying central crystal as out-of-focus foreground anchor on lower-left. Palette: deep purple #4B2E80, blue-violet shadow #0E0820, magenta rim from staff #E83FC8, lime LED accent #A7F432 on Byte's headphones (only bright spot besides crystals), pale-cyan #7FFFD4 in shaft, no warm tones, no gold. Texture: rock, glassy crystal, dense volumetric haze, silhouettes mostly featureless. Mood: collective contemplation, the stillness of waiting. 16:9.

Negative: photorealistic, anime, moe, faces visible in detail on silhouettes, more than three figures, four cyclops in frame (Luxa NOT here), glowing eyes through silhouette, fantasy battle, magic circle, sword, dragon, action pose, two eyes per cyclops creature (must be cyclops, single eye), watermark, brand logos, oversaturated, fully-lit characters, cel-shaded flat, harsh black outlines.
```

**Notas**:
- 3 silhouettes, NO 4. Luxa debuta en escena 09. Si Nano Banana mete una cuarta, regenerá.
- Diagnostic features no negociables: staff con cristal magenta (Wiz), lime LEDs (Byte), cap brim (Zek). Sin esos tres, no se lee.

---

## `first-frame-escena-05`

**Para**: clip Seedance escena 05 (15s, slow dolly-in en cocina al atardecer).
**Tipo**: first-frame externo recomendado.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-mariela-kitchen-dusk | (generar primero) |
| `@image2` | char lock Mariela | `public/images/personajes/mariela.png` ✓ |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Medium-wide cinematic interior of the small Ñuñoa apartment kitchen from @image1 at dusk around 7:30 PM. @image2 (a 36-year-old Latin-American woman, brown hair pulled back in a low ponytail, sober light office blouse, thin metal-framed glasses with hairline scratch on right lens, calm tired competent expression, softened cinematic-3D human proportions, naturalistic stylized skin tones) stands at the kitchen counter beside the gas stovetop where the old aluminum kettle has just been placed, her body angled three-quarters toward the window on the left. Through the window: city skyline at dusk, smog-pink #E8A0A0 sky fading upward to dusk-blue #5A6E8A, the Andes mountain range barely silhouetted. Her own reflection is faintly held in the window glass, ghosted over the city — both her and the city visible. The Edison-style tungsten pendant bulb #FFD08A above the small wooden table is just turned on, beginning to pool warm light on the surface. On the table, the closed brown leather A6 notebook with faded elastic from the existing concept and a sharpened wooden pencil resting beside it. Her posture is quiet, hands resting at her sides, just looking at her own reflection. Composition: rule of thirds, woman in right third in three-quarter pose, window with reflection in upper-left third, table with notebook in lower-left third. Palette: warm tungsten #FFD08A pool around bulb (small, just-on), dusk-blue #5A6E8A from window, smog-pink #E8A0A0 on upper window, ochre tile #D8CFC2, muted ceramic neutrals, neutral wood, no fantasy palette glow. Texture: worn ceramic kettle with brushed-steel handle, soft cotton blouse, matte wood table, glass window with subtle reflections, fine specular on glasses lens. Mood: contemplative, suspended, the second before a decision. 16:9.

Negative: photorealistic skin pores, hyperrealistic DSLR shot, glamour beauty lighting, anime big eyes, moe, magenta crystal, turquoise glow, cyclops creature in frame, fantasy element, mystical aura, thriller vignette, telenovela melodrama, kitchen straight from a TV cooking show, watermark, brand logos, harsh black outlines, oversaturated, full-bright kitchen, woman with exaggerated expression.
```

**Notas**:
- El reflejo en ventana es load-bearing del beat. Si Nano Banana lo dropea, regenerá.

---

## `first-frame-escena-06A`

**Para**: clip Seedance escena 06A (15s, tight close-up sobre mano y página).
**Tipo**: first-frame externo OBLIGATORIO según seedance-prompts.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-notebook-overhead-blank | (generar primero) |
| `@image2` | char lock Mariela | `public/images/personajes/mariela.png` ✓ |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Tight close-up overhead shot of the open A6 brown leather notebook on the wooden kitchen table from @image1, exact same framing and composition. The left hand and forearm of @image2 (the woman from the character reference, naturalistic stylized softened skin tones, no rings, no nail polish, slightly cool lighting on skin from above) enters the frame from the lower-right and rests on the right page of the notebook, palm down, fingers slightly relaxed. Her right hand also enters from the right edge holding a sharpened wooden pencil between thumb and index finger, the pencil tip hovering roughly 2cm above the right page, not yet touching, indicating she is about to write. The previous entry of three illegible squiggles is visible on the left page from @image1. The hairline crack on the leather spine is identical to @image1, no glow yet. A warm tungsten Edison bulb #FFD08A pool from above-left lights the page and her hand from above, casting soft shadow of the pencil and her fingers across the right page. Composition matches @image1. Palette: warm tungsten #FFD08A dominant, paper cream #F0E8D8, graphite gray on left page squiggles, worn brown leather spine #6B4A2E, warm pine table at edges #C9A877, soft warm-olive softened skin tone with subtle subsurface scattering on hand, dusk-blue #2A3A5A in shadow corners, no fantasy palette glow. Texture: matte paper, soft skin with subtle subsurface scattering on knuckles, sharpened cedar pencil, worn leather, wood grain. Mood: hesitation, the moment before, breath held. 16:9.

Negative: photorealistic skin pores, hyperrealistic DSLR macro, glamour beauty DOF, hand model glamour shot, anime, moe, big anime eyes (face is out of frame), readable previous entry on left page (must be illegible squiggles), text already written on right page (must be blank), cyan glow on spine (not yet), magenta crystal, fantasy element, watermark, brand logos, hand with rings, polished nails, multiple hands besides hers, oversaturated, harsh black outlines.
```

**Notas**:
- Mano izquierda apoyada, mano derecha con lápiz suspendido. Si Nano Banana invierte (lápiz en izquierda), regenerá — el storyboard tiene la cocina coreografiada con izquierda apoyada.
- Página derecha BLANCA en este first-frame. La frase aparece durante el clip.

---

## `last-frame-escena-06A` (= `first-frame-escena-06B`)

**Para**: cierre de 06A + apertura de 06B. Encadenado continuous, mismo set, casi mismo frame.
**Tipo**: last-frame de un clip + first-frame del siguiente.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-notebook-question-written | (generar primero) |
| `@image2` | char lock Mariela | `public/images/personajes/mariela.png` ✓ |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Tight close-up overhead shot of the open notebook on the wooden kitchen table, framing identical to @image1, focused on the page where the cursive English line "Why did I stop writing here?" has just been written in tentative pencil graphite. The left hand of @image2 (same hand from the character reference, naturalistic stylized softened skin) rests motionless palm-down on the right page beside the written line, no longer holding anything tense. The sharpened wooden pencil has been set down beside the notebook on the table, parallel to the long edge, no longer in her hand. Behind the page in deep blurred background, the gas stovetop with the aluminum kettle is barely visible. The hairline crack on the leather spine remains identical to @image1, no glow yet. Warm tungsten Edison bulb pool #FFD08A from above-left as before. Composition matches @image1. Palette: warm tungsten #FFD08A dominant, paper cream #F0E8D8, graphite gray on the line, worn brown leather, warm pine table edges, softened warm-olive skin on hand, dusk-blue shadow corners, no fantasy palette glow yet. Texture: matte paper, soft skin, leather, wood grain. Mood: stillness after the seismic moment, breath returning. 16:9.

Negative: photorealistic, hyperrealistic, anime, moe, hand still holding pencil (must be set down), pencil mid-air, woman face in frame (must be hand only with face out), cyan glow on spine yet (the chime hasn't happened — must remain unlit), magenta crystal, fantasy element, watermark, brand logos, multiple hands, harsh black outlines, oversaturated, dramatic chiaroscuro.
```

**Notas**:
- El lápiz está APOYADO en la mesa, no en la mano. Si Nano Banana lo deja en la mano, regenerá — el clip 06B muestra la mano quieta sin pencil.
- Sin glow cyan. El glow aparece en los últimos 1-3 frames de 06B.

---

## `first-frame-escena-07`

**Para**: clip Seedance escena 07 (15s, Byte foreground / Wiz background, primer plano detallado de Pax).
**Tipo**: first-frame externo recomendado para fijar el debut visual de los personajes "iluminados" (no más siluetas).

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | char lock Byte | `public/images/personajes/byte.png` ✓ |
| `@image2` | char lock Wiz | `public/images/personajes/wiz.png` ✓ |
| `@image3` | concept-cave-wide-dark (atmósfera) | (generar primero) |
| `@image4` | Mood reference | `public/images/portadas/portada2.png` ✓ |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Medium two-shot interior of the same cavern as @image3, camera at chest height with a slight 5-degree Dutch tilt for contained alarm. @image1 (a young cyclops creature with single large central turquoise eye #3FE0C8 and double specular highlight, smooth turquoise-green skin #21D8B6 with subsurface scattering, elastic pointed ears, dark purple hoodie with lime-green neon trim, large over-ear neural headphones with bright lime-green LED rings #A7F432 currently glowing slightly stronger than usual, four-fingered hands, 3-3.5 head proportions) stands in the foreground three-quarters facing camera, his pointed elastic ears just having flicked alert, his single turquoise eye widened with pupil enlarged, his right hand pressed two-fingered against the right earcup as if listening intently. Behind him to the right and slightly back, @image2 (an elder cyclops creature in deep purple hooded robe with white voluminous beard, leaning on a dark wooden staff topped with a violet-magenta crystal — single turquoise eye #3FE0C8 visible, four-fingered hands) stands partially in shadow, his single eye closed for one beat, his white beard catching faint magenta rim light from his staff's crystal, the staff held vertical not yet pointing. Around them, dense volumetric cavern haze, slow-falling dust catching faint magenta and cyan ambient. A faintly pulsing magenta crystal sits as out-of-focus background anchor in lower-left. Atmosphere matches @image4. Composition: rule of thirds, @image1 in left third, @image2 in right third, slight Dutch tilt creates contained alarm without melodrama. Palette: deep purple #4B2E80 cavern base, blue-violet #0E0820 shadow, magenta #E83FC8 rim from elder's staff, lime green #A7F432 emissive on Byte's headphones (slightly intensified), turquoise #21D8B6 cyclops skin and #3FE0C8 in both single eyes. Texture: green-turquoise cyclops skin with subsurface scattering, matte purple velvet on elder's robe with thread weave, glossy plastic on headphones with bright LED, white beard fiber detail. Mood: alert, the cavern's first inhalation in hours. 16:9.

Negative: photorealistic, hyperrealistic, anime big-glossy-eyes, moe, two eyes per cyclops creature (must be cyclops, ONE central eye each), big anime eyes, harsh black outlines, generic family-feature look, fantasy battle stance, sword, magic circle, lightning, gem counter HUD, loading bar, oversaturated, thriller vignette, action pose, melodramatic gesture, watermark, brand logos, four cyclops in frame (only Byte and Wiz here).
```

**Notas**:
- 1 ojo central por cyclops. Verificar antes de aprobar.
- LEDs lime de Byte ligeramente más brillantes que en escena 02. Eso es el "primer respiro" del audio diseñado.

---

## `first-frame-escena-08A`

**Para**: clip Seedance escena 08A (3s usables, hand gripping pencil).
**Tipo**: first-frame externo OBLIGATORIO.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-notebook-question-written | (generar primero) |
| `@image2` | char lock Mariela | `public/images/personajes/mariela.png` ✓ |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Extreme macro close-up of the left hand of @image2 (a 36-year-old Latin-American woman's hand with naturalistic stylized softened skin tones, slight warm-olive subsurface scattering, no rings, no polish), fingers gripping a sharpened wooden pencil firmly enough that knuckles whiten faintly under softened cinematic-3D skin shading. The pencil is pressed against the page of the open A6 notebook from @image1 — the page showing the recently written cursive English line "Why did I stop writing here?" immediately above the pencil tip. The paper below the lead shows visible compression marks where the tip is pressed hard. A single grain of graphite catches the warm tungsten light at the very tip of the pencil, a small specular highlight. The hairline crack on the leather spine remains visible at left edge of frame, no glow yet. Composition: centered macro, the written line at upper-third anchor, pencil tip at center, graphite grain at lower-third with highlight, fingers framing the right side. Palette: warm tungsten #FFD08A dominant pool, paper cream #F0E8D8, graphite gray, deep dusk-blue shadow corners #2A3A5A, soft warm-olive softened skin on knuckles with subtle subsurface scattering, no fantasy palette accents at all in this frame. Texture: matte uncoated paper with subtle compression marks under lead, sharpened cedar pencil with grain visible, soft skin with subtle subsurface scattering on knuckles, faint specular on polished pencil shaft. Mood: contained seismic moment, the millisecond before a cosmos rearranges. 16:9.

Negative: photorealistic skin pores, hyperrealistic DSLR macro, glamour hand model shot, beauty DOF, anime, moe, big anime eyes (face is out of frame), magenta crystal visible, turquoise glow, cyan emission anywhere, cyclops creatures, fantasy element, sparkle, magic, watermark, brand logos, multiple hands, hand with rings, polished nails, oversaturated, harsh black outlines, dramatic chiaroscuro.
```

**Notas**:
- CERO magia visible. La sorpresa es el match-cut con 08B.
- Compression marks bajo el lápiz = el detalle hero. Si Nano Banana no los muestra, regenerá.

---

## `first-frame-escena-08B`

**Para**: clip Seedance escena 08B (12s usables, palma de Wiz, materialización del cristal).
**Tipo**: first-frame externo OBLIGATORIO.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-cyclops-palm-macro | (generar primero) |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Extreme macro close-up of the right palm of the elder cyclops creature, framing identical to @image1. The palm is fully open and empty in the dark of the cavern, no crystal yet in this first frame — the materialization happens during the Seedance clip. His single droopy-lidded turquoise eye #3FE0C8 visible in soft focus behind the palm watching the empty hand intently. Composition matches @image1 exactly. Palette matches @image1: green-turquoise skin #21D8B6 with marked subsurface scattering, deep blue-violet ambient #0E0820 and #4B2E80, soft turquoise eye in soft focus, faint cool ambient on white beard fibers at bottom of frame, no warm tones, no magenta yet (palm empty), no gold. Texture matches @image1. Mood: stillness before the rule of the universe demonstrates itself, the second before. 16:9.

Negative: photorealistic skin pores, hyperrealistic, two eyes (must be cyclops one eye), five fingers (must be four), six fingers, anime, moe, magenta crystal already in palm (must be empty), turquoise glow on palm itself, sparkle, magic effect, lightning, fantasy magic circle, watermark, brand logos, cel-shaded flat, oversaturated.
```

**Notas**:
- Este first-frame es esencialmente igual al concept `concept-cyclops-palm-macro`. Podés reutilizar ese mismo PNG como first-frame y saltarte una generación. Si lo regenerás, asegurate de matchear pixel-perfect.

---

## `last-frame-escena-08B` (= `first-frame-escena-09`)

**Para**: cierre de 08B + apertura de 09. Encadenado continuous.
**Tipo**: last-frame de un clip + first-frame del siguiente.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-cyclops-palm-macro | (generar primero) |
| `@image2` | char lock Wiz | `public/images/personajes/wiz.png` ✓ |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Extreme macro close-up of the right palm of the elder cyclops creature from @image2, framing matching @image1 but with the palm now holding a freshly-materialized small dense magenta crystal #FF49B4 with #E83FC8 rim floating exactly two centimeters above the skin. The crystal is glassy multifaceted with hairline cooling cracks visible at its edges, pulsing strongly mid-frame, glowing magenta from within. The crystal casts warm magenta rim light onto the skin of the palm and faint magenta bloom into the surrounding volumetric haze. His single droopy-lidded turquoise eye #3FE0C8 visible in soft focus behind the palm now watches the crystal with an expression of recognition (not surprise). Dense particulate cavern haze surrounds the moment, dust motes spiraling slowly inward toward the new crystal. Composition: extreme centered hero on the floating crystal, palm forming foreground curve, eye in upper-third soft-focus background, crystal exactly at the optical center. Palette: magenta #FF49B4 core and #E83FC8 rim dominant, deep purple #4B2E80 ambient, blue-violet #0E0820 shadow, turquoise #21D8B6 on palm with magenta rim wrap, #3FE0C8 in soft-focus eye, no warm tones, no cyan, no gold. Texture: glassy multifaceted crystal with internal emission and hairline cooling cracks, soft green-turquoise cyclops skin with marked subsurface scattering and magenta rim wrap, matte white beard with fine fiber detail. Mood: silent revelation, the universe quietly proving its rule. 16:9.

Negative: photorealistic skin pores, hyperrealistic, two eyes (must be cyclops one eye), five fingers (must be four), six fingers, anime, moe, harsh black outlines, multiple crystals (must be one), crystal touching the palm (must float 2cm above), abrupt formation flash, sparkle burst, fairy dust, lightning, magic circle, fantasy battle scene, watermark, brand logos, oversaturated thriller, glamour DOF.
```

**Notas**:
- Cristal flotando 2cm arriba de la palma, NO tocándola. Load-bearing.
- Una sola pulsación fuerte mid-frame — si el still se ve "establecido y tranquilo", elegí el momento de máxima emisión.

---

## `first-frame-escena-10`

**Para**: clip Seedance escena 10 (15s, low-angle bajo rejilla).
**Tipo**: first-frame externo recomendado.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-bilbao-grate-night | (generar primero) |
| `@image2` | char lock Jiggy | `public/images/personajes/jiggy.png` ✓ |
| `@image3` | char lock Zek | `public/images/personajes/zek.png` ✓ |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Wide low-angle exterior shot framing identical to @image1, looking up from beneath the cast-iron sewer grate with the empty Av. Bilbao avenue and night sky visible above. Just below the grate in a sliver of darkness, @image2 (a small bipedal cyclops runner-creature with smooth turquoise-green skin #21D8B6 with subsurface scattering, single large central turquoise eye #3FE0C8, brown-red leather chest harness with metal buckle, leather satchel at hip, four-fingered hands, 3-3.5 head proportions) stands looking up through the grate at the night sky. In his right fist, closed, he holds the new magenta crystal #FF49B4 — its glow leaking faintly between his fingers as small slivers of magenta light. In his open left palm, resting upward, the warm golden-yellow crystal #FFE34D from Luxa rests visible, its warm gold core glowing softly. His single turquoise eye reflects the sodium orange #FF8A30 from the streetlamp above in a faint warm rim — the first time green-turquoise cyclops skin meets warm tungsten/sodium light in the episode. Behind him in the deeper dark of the access tunnel approximately 2 meters back, @image3 (the teenage cyclops with sideways purple visor cap, retro analog boombox at his hip, four-fingered hands) stands quietly with one hand resting on the boombox. The two patrol drones from @image1 are visible in the upper sky through the grate slats, magenta LED indicators small. Composition matches @image1. Palette: sodium orange #FF8A30 from streetlamp, night-blue #1A2330 sky, drone magenta #E83FC8 small LEDs, magenta #FF49B4 leaking from Jiggy's right fist, warm gold #FFE34D from his left palm (visiting warmth, exclusive), turquoise #21D8B6 cyclops skin with subtle subsurface scattering, deep tunnel shadow #0E0820 around them. Texture: cast-iron grate with rust, asphalt, glassy crystals with internal emission, brushed plastic on drone shells and boombox casing, worn leather harness and satchel, soft cyclops skin. Mood: stealth ready, the magic rule about to make itself visible in geometry. 16:9.

Negative: photorealistic, hyperrealistic night photo, anime, moe, big anime eyes, two eyes per cyclops (must be cyclops single eye), five-fingered cyclops hand (must be four), thriller vignette, drones firing, drones with red LEDs (must be magenta), drones aggressive, magic circle, lightning, fairy trail, gem counter HUD, watermark, brand logos, fully-lit street, more than two drones in frame, characters in foreground street, anime body proportions on cyclops.
```

**Notas**:
- Magenta en derecha, gold en izquierda. Si Nano Banana invierte, regenerá.
- Drones con LED magenta SMALL, no glow burst.

---

## `first-frame-escena-11`

**Para**: clip Seedance escena 11 (15s, slow dolly-in en cocina con entrega invisible).
**Tipo**: first-frame externo OBLIGATORIO según seedance-prompts. **El clip más delicado del piloto en términos de paleta — este first-frame tiene que clavarlo.**

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-mariela-kitchen-night | (generar primero) |
| `@image2` | char lock Mariela | `public/images/personajes/mariela.png` ✓ |
| `@image3` | char lock Jiggy | `public/images/personajes/jiggy.png` ✓ |
| `@image4` | Mood reference (paleta caverna para piel de Jiggy) | `public/images/portadas/portada2.png` ✓ |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Medium-wide cinematic interior of the same Ñuñoa kitchen as @image1 at night around 10:30 PM. @image2 (the woman from the character reference, brown hair pulled back in low ponytail, sober blouse, thin metal-framed glasses with hairline scratch on right lens, soft tired expression, softened cinematic-3D human proportions) is seated at the small wooden kitchen table with the open brown leather A6 notebook in front of her, her left hand resting flat on the table beside the page that holds the cursive English line "Why did I stop writing here?", her right hand starting to lift toward the cover as if about to close the notebook. A mug of cold tea sits beside her, condensation dried. From behind the white refrigerator on the LEFT side of frame, @image3 (a small bipedal cyclops creature with smooth turquoise-green skin #21D8B6 with subsurface scattering, single large central turquoise eye #3FE0C8, brown-red leather chest harness with metal buckle, leather satchel at hip, four-fingered hands, 3-3.5 head proportions) emerges low and quiet, walking with the careful gait of someone delivering something heavy and small — invisible to her, fully present to the camera. He approaches her left hand, his own right palm open holding the small magenta crystal #FF49B4. Critical lighting on @image3: he receives a DUAL RIM LIGHT — thin magenta rim #E83FC8 on his LEFT side from his own crystal's emissive aura, and warm tungsten rim #FFD08A 3000K on his RIGHT side from the kitchen's hanging Edison bulb fall-off. The two rim-lights blend into a single warm-cool integrated outline along his shoulder and arm so he reads as belonging in this room, not as a CG paste-in. @image2 is unaware, eyes still on the notebook. Composition: rule of thirds, @image2 in right two-thirds at the table, @image3 entering on left third low behind the refrigerator, the future contact point of palms in lower-center. Palette: warm tungsten #FFD08A pool dominant from Edison bulb, dusk-blue #2A3A5A in shadow corners and from window, magenta #FF49B4 / #E83FC8 contained to @image3 and his crystal only, turquoise #21D8B6 on @image3's skin with magenta-on-left + tungsten-on-right rim wrap. The cyclops's color palette from @image4 is preserved on his body. Texture: matte wooden table with cup-ring marks, soft cotton blouse, worn leather harness on @image3, glassy magenta crystal with internal emission, painted refrigerator surface. Mood: warm domestic miracle about to happen, the project's manifesto in a single physical gesture. 16:9.

Negative: photorealistic, hyperrealistic DSLR portrait, glamour beauty DOF, anime, moe, big anime eyes, two eyes on cyclops (must be cyclops single eye), five-fingered cyclops hand (must be four), the woman seeing the cyclops (must remain unaware, eyes on notebook), the woman looking down at her hand prematurely, magic circle, sparkle, fairy trail, gem counter HUD, oversaturated thriller, dramatic chiaroscuro, telenovela melodrama, flat key light on cyclops (must have dual rim), cyclops looking like a CG paste-in (must integrate into kitchen lighting), watermark, brand logos, more than two figures.
```

**Notas**:
- Mariela NO mira a Jiggy. Si Nano Banana le acomoda los ojos hacia Jiggy, regenerá inmediato — rompe el beat más importante del piloto.
- Dual rim light en Jiggy es load-bearing. Magenta-izquierda + tungsten-derecha. Si sale plano o monocromático, regenerá.
- Heladera en el LADO IZQUIERDO del frame. Si la pone a la derecha, regenerá.

---

## `last-frame-escena-11` (= `first-frame-escena-12`)

**Para**: cierre de escena 11 + apertura de escena 12. Encadenado continuous.
**Tipo**: last-frame de un clip + first-frame del siguiente.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-mariela-kitchen-night | (generar primero) |
| `@image2` | char lock Mariela | `public/images/personajes/mariela.png` ✓ |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Tight medium shot of @image2 (the woman from the character reference, soft tired expression, softened cinematic-3D human proportions) seated at the small wooden kitchen table inside the same Ñuñoa kitchen as @image1. Her left hand is now closed gently against her own sternum, fingers cupped around an invisible warmth, palm pressing flat to her chest. Her gaze rests on the open notebook page where the cursive line "Why did I stop writing here?" is visible. Her face shows a tiny micro-shift — the smallest softening of a small hardness, no visible smile yet, no tears, just an internal change registered in the corners of the mouth and the eyes. The cyclops is GONE — no longer in frame, having stepped back behind the refrigerator out of view. The kitchen looks exactly as in @image1 but with no second figure visible. The Edison bulb pool is the same. The mug of cold tea remains beside her. A barely-perceptible 8% opacity warm tungsten residue glow sits on her left palm where the crystal was pressed — near-subliminal, easy to miss. Composition: rule of thirds, @image2 in the right third in seated three-quarter pose with hand to chest, notebook in lower-left third, kettle and tea cup as soft anchors. Palette: warm tungsten #FFD08A dominant, dusk-blue #2A3A5A in shadow corners, paper cream and pencil graphite on visible page, soft warm-olive softened skin tone on her hand and face, faint warm-tungsten residue at 8% on her left palm only — no fantasy palette glow visible. Texture: matte wooden table, soft cotton blouse, paper, faint warm subsurface on her skin where the crystal was pressed. Mood: minimal reconciliation, a small private warmth. 16:9.

Negative: photorealistic skin pores, hyperrealistic, DSLR portrait, glamour beauty lighting, anime, moe, big anime eyes, harsh black outlines, big smile (must be sub-centimeter mouth corner shift, no visible teeth), tears streaming, melodramatic crying, magenta crystal visible, turquoise glow visible (the residue is warm not cool), cyclops creature in frame (he is gone), sparkle, magic aura around the woman, thriller vignette, telenovela close-up, oversaturated, full-bright key light, watermark, brand logos.
```

**Notas**:
- Sub-centimeter mouth corner shift. Si Nano Banana entrega sonrisa visible, regenerá.
- Residue WARM (8%) en palma, NO cyan. Esto es importante — el cyan está en la libreta, no en ella.

---

## `first-frame-escena-13`

**Para**: clip Seedance escena 13 (15s, slow descending crane sobre Wiz de espaldas).
**Tipo**: first-frame externo recomendado.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-cave-stalagmites-reawakening | (generar primero) |
| `@image2` | char lock Wiz | `public/images/personajes/wiz.png` ✓ |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Wide cinematic shot of the cavern from @image1, with @image2 (the elder cyclops creature in deep purple hooded robe, white voluminous beard, holding the dark wooden staff with the violet-magenta crystal at its tip, four-fingered hands) standing in three-quarter back view in the center-left of frame. His back is partly to camera, his white-bearded head visible from the side, his single eye observing a thin upward air current — fine motes of dust spiraling slowly upward through the hairline crack in the cavern ceiling on upper-left third, where the pale-cyan #7FFFD4 shaft now glows at 25 percent opacity (warmer/stronger than scene 1's 15%). Around him, the two reawakening stalagmites from @image1 hold faint magenta glow #FF49B4 at low intensity. The original central stalagmite still glows magenta slightly stronger than before. The camera is positioned slightly above and behind him, ready to descend. Composition: rule of thirds, elder on left third in three-quarter back view, ceiling fissure with rising dust spiral on upper-left third as vertical anchor, two reawakening stalagmites in lower-third base flanking, central original crystal at lower-third anchor. Palette: matches @image1 exactly — magenta #FF49B4 / #E83FC8 on the three glowing crystals, deep purple #4B2E80 ambient, blue-violet #0E0820 shadow, pale-cyan #7FFFD4 in ceiling shaft, deep-purple velvet on Wiz's robe, turquoise on his exposed skin, no warm tones, no gold (the gold pocket-spark insert happens in post). Texture: matte porous rock, glassy newly-forming crystals, dense volumetric haze with rising dust, matte purple velvet on robe with deep folds, white beard fiber detail. Mood: contemplative observer, the place no longer dying, an open question, breath returning to the world. 16:9.

Negative: photorealistic, anime, moe, every stalagmite glowing brightly (must be only 2 reawakening plus the original), Wiz facing camera (must be three-quarter back view), Jiggy in frame (he enters during the clip), gold crystal visible in Wiz's hand or pocket (the pocket-spark is a post-production insert, NOT in this still), more than one cyclops in frame, fantasy battle, sword, dragon, magic circle, lightning, sparkle burst, watermark, brand logos, oversaturated, harsh black outlines, two eyes (must be cyclops single eye).
```

**Notas**:
- Wiz de tres-cuartos espalda. Cara semi-visible solo de costado. Si Nano Banana lo gira de frente, regenerá — el clip empieza con él de espaldas y se gira durante el clip.
- SIN gold-spark en bolsillo. Eso es insert post-prod manual.

---

## `first-frame-escena-14`

**Para**: clip Seedance escena 14 (15s, slow push-in cocina vacía).
**Tipo**: first-frame externo OBLIGATORIO. Es el cliffhanger del piloto.

**Reference images requeridas**:

| Slot | Imagen | Path / Estado |
|------|--------|---------------|
| `@image1` | concept-kitchen-empty-glowing-notebook | (generar primero) |
| `@image2` | concept-notebook-line-glowing-cyan (para reference del glow target) | (generar primero) |

**Prompt Nano Banana**:

```
[Style-lock pegado arriba]

Medium-wide cinematic interior shot framing identical to @image1, the same empty Ñuñoa kitchen at late night around 11:30 PM. The small wooden kitchen table at center holds the open brown leather A6 notebook lying flat page-up. The right page shows the cursive English line "Why did I stop writing here?" — but in this first frame, the line is NOT YET glowing cyan; it is rendered as the same handwritten graphite line as in earlier scenes, lit only by the warm tungsten Edison bulb. (The cyan glow visible in @image2 builds DURING the Seedance clip, not in this first frame.) The hairline crack on the leather spine is visible, faintly pale-cyan #7FFFD4 at 5% opacity (continuity from escena 06B). A second drained ceramic mug of tea sits beside the kettle on the gas stovetop, indicating she had a second cup. Through the internal doorway visible at right edge of frame, the closed bedroom door has a thin warm strip of soft yellow light #F4D8A4 spilling from beneath it. The window on the left shows full night-blue #1A2330 sky with scattered city light pinpoints. No people in frame. Composition matches @image1. Palette: warm tungsten #FFD08A pool dominant from Edison bulb, dusk-blue #2A3A5A in shadow, paper cream #F0E8D8, worn brown leather, ceramic cream, soft yellow #F4D8A4 strip under bedroom door, hairline pale-cyan #7FFFD4 at 5% on spine crack only (subliminal), no other fantasy palette glow yet. Texture: matte wood, ceramic, leather, paper, painted door surface. Mood: cliffhanger first frame, an empty room before its quiet activation, the second before the page wakes up. 16:9.

Negative: photorealistic, hyperrealistic, anime, moe, characters in frame (must be empty), cyclops creature visible, magenta crystal visible, full-page glow on notebook (must be unlit on the line in this first frame — the cyan glow on letters is what builds DURING the clip, not in the first frame), full-saturation cyan on letters, square-wave UI blink, loading-screen pulse, magic circle, sparkle, fairy trail, fantasy effect, thriller vignette, glamour shot, watermark, brand logos, fully dark room (warm tungsten must be on), open bedroom door, person visible.
```

**Notas**:
- Frase escrita en graphite, sin glow cyan. El glow se construye durante los 12s del push-in en Seedance + post-prod.
- 5% glow en lomo (continuidad B6). Casi invisible. Si Nano Banana lo hace visible, regenerá.

---

# Apéndice — Riesgos y contradicciones detectadas

Durante la consolidación de IDs entre `storyboard-nano.md` y `seedance-prompts.md` detecté las siguientes tensiones. **Vos decidís cuál prevalece**:

1. **`concept-cave-fading-crystals` (Seedance E01) vs `concept-cave-wide-establishing` (Storyboard E01-E02-E07-E09)**: ambos describen la caverna con cristal central moribundo. Los unifiqué en `concept-cave-wide-dark` con un solo prompt. Sin contradicción real, solo nombres distintos.

2. **`concept-notebook-with-crack` (Seedance) vs `concept-notebook-leather-worn` (Storyboard E04) vs el spine-crack-macro (Storyboard E06)**: el seedance-director usa el mismo ID `concept-notebook-with-crack` en E04, E05, E06, E08 y E14, lo cual implica que la grieta del lomo es visible en TODOS los planos de libreta desde el inicio. El storyboard tiene un asset separado `concept-notebook-leather-worn` (sin grieta visible) para E04 y un macro de spine para E06. **Decidí**: unifico en `concept-notebook-hero` con grieta hairline siempre visible (porque es continuidad), y el macro `concept-notebook-spine-crack-macro` se mantiene como asset separado para el plano cerrado de B6. Si querés que la grieta NO sea visible en E04 y aparezca recién en E06, hay que generar dos versiones del HERO. Te flageo por si querés decidir distinto.

3. **`concept-mariela-kitchen-dusk` (Storyboard E05) vs `concept-mariela-house-kitchen` (Seedance, usado en E05 con descripción dusk + en E11/E14 con descripción night)**: el seedance-director usa el MISMO ID para versión dusk (E05) y night (E11/E14), lo cual es inconsistente. **Decidí**: separo en `concept-mariela-kitchen-dusk` y `concept-mariela-kitchen-night` (con night derivando del dusk para mantener identidad). El seedance-prompts.md tiene un naming bug que vale corregir.

4. **`concept-notebook-on-table` (Storyboard E05) vs sin equivalente en Seedance**: el storyboard pide un derivado específico para E05 con libreta cerrada + lápiz en jarra cerámica. Lo incluí como `concept-notebook-on-table-dusk`. Si no lo querés, podés saltearlo y usar `concept-notebook-hero` directo en E05.

5. **`concept-cyclops-palm-macro` y `first-frame-escena-08B`**: son esencialmente la misma imagen (palma vacía de Wiz en oscuridad). El storyboard lo declara como concept para B8B; el seedance-director lo declara como first-frame. Recomendé reutilizar el mismo PNG para ambos (ahorra una generación). Si preferís dos generaciones distintas para tener variantes de iluminación, generá ambos.

6. **`first-frame-escena-08B` y `last-frame-escena-08B`**: son el inicio (palma vacía) y el final (palma con cristal flotando) del mismo clip. Generé prompts separados. El last-frame también es first-frame de E09 según el seedance-director.

7. **Storyboard escena 14 usa `mariela.png` como `@image3` (mood reference humano)**: esto es un truco curioso del storyboard — usar el char lock como tonal reference de paleta neutra warm. Funciona, pero es no-estándar. Lo respeté en el first-frame de E14 indirectamente vía el concept de cocina nocturna.

8. **Asset que NO está en mi lista pero podrías querer**: `first-frame-escena-03`, `first-frame-escena-04`, `first-frame-escena-12` adicional. El seedance-director los marca como T2V directos o opcionales — los omití. Si vas a querer control fino sobre el inicio de E03 (oficina) o E04 (metro), pedímelos y los agrego.

9. **Texto handwritten en stills**: Nano Banana tiene confiabilidad ~60% para texto cursive en inglés. Para los assets que requieren la frase exacta "Why did I stop writing here?" (`concept-notebook-question-written`, `concept-notebook-line-glowing-cyan`, `first-frame-escena-08A`, `first-frame-escena-14`), recomendé fallback de generar SIN texto y compositar la frase en post como overlay tipográfico consistente. Esto también soluciona la consistencia entre B6 y B14 (mismo overlay reutilizado). Si querés que Nano Banana renderee el texto directo, vas a tener que iterar 3-5 veces por asset.

10. **Char lock Luxa NO se usa en ningún first-frame**: Luxa debuta en E09 pero el seedance-director NO declaró un first-frame externo para E09 — usa el last-frame de E08B como first-frame. Eso significa que Luxa entra "en vivo" durante el clip Seedance. Riesgo: el debut visual de Luxa depende 100% de la generación de Seedance. Si querés más control, podríamos agregar `first-frame-escena-09-luxa-entry` (Wiz palm con cristal + Jiggy ya en frame + Luxa apareciendo a la derecha). Te lo flageo por si lo querés.
