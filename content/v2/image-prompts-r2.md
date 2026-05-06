---
title: "Pax — Prompts de imagen R2 (5 imagenes ancla + char sheet Itzel)"
description: "Prompts en ingles listos para enviar a GPT Image 2 con referencias locales del repo. Reescritos para honrar el style-guide canonico (stylized 3D PBR neon-magic) que R1 ignoro."
date: 2026-05-04
version: image-prompts-r2
basado_en: art-direction-r1 (composicion preservada) + style-guide canonico (render base obligatorio) + auditoria assets en process-log/10a + estrategia en process-log/10b
api: gpt-image-2 (OpenAI Images API — /v1/images/edits con input_image_paths)
convencion_referencias: "Image 1, Image 2..." — texto literal en el prompt + array input_image_paths con paths absolutos del repo
---

# Prompts de imagen R2 — set Pax

## Cambio fundamental respecto a R1

R1 fue text-only, sin references, y pidio "Painted 2D animation in Studio Ghibli + Cartoon Saloon" — eso contradice el style-guide canonico del proyecto que exige `stylized 3D animation, semi-realistic PBR shading, neon-magic lighting`. R2 corrige el render base y carga referencias locales del repo (cast canonico + portadas + concept arts del Bloque A) como Image 1, Image 2, Image 3, Image 4 segun OpenAI API.

## Orden de generacion recomendado

```
0. Char sheet Itzel  →  public/images/personajes/itzel.png
1. Imagen 1          →  content/v2/anchors/img-01-piedra-apagandose-r2.png
2. Imagen 4          →  content/v2/anchors/img-04-objeto-roto-r2.png
3. Imagen 5          →  content/v2/anchors/img-05-itzel-cenote-r2.png
4. Imagen 2          →  content/v2/anchors/img-02-red-gemas-r2.png
5. Imagen 3          →  content/v2/anchors/img-03-ola-muda-r2.png
```

Justificacion completa en `process-log/10b-prompts-r2-strategy.md`.

## Resoluciones API (no negociables — el modelo solo soporta estas tres)

`1024x1024` cuadrado / `1024x1536` vertical / `1536x1024` horizontal.

## Flag de seguridad activo

Imagen 5 mantiene los 7 items del checklist de seguridad de R1: PFD visible, mangas largas, casco con linterna, plano arriba de rodillas, cara al agua (no contacto visual), bolsa de basura, sin tela mojada pegada.

---

## Paso 0 — Char sheet de Itzel (prerequisito)

Ver prompt completo y justificacion en `process-log/10b-prompts-r2-strategy.md` seccion 3. Resumen aqui:

### Reference assets (paths absolutos)

- Image 1: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\mariela.png` — style-anchor del render humano Pax (NO copiar cara/edad de Mariela; solo el render base 3D stylized human softened).
- Image 2: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada2.png` — style-anchor universe palette + bloom + atmosfera.

### Aspect ratio + quality

`1024x1536` / `medium`.

### Generation call

```python
edit_image(
    prompt=<ver process-log/10b-prompts-r2-strategy.md seccion 3>,
    input_image_paths=[
        "public/images/personajes/mariela.png",
        "public/images/portadas/portada2.png"
    ],
    output_path="public/images/personajes/itzel.png",
    size="1024x1536",
    quality="medium"
)
```

### Output

`public/images/personajes/itzel.png` — char-lock canonico de Itzel reusable en imagen 5 R2 + futuras imagenes del piloto.

---

## Imagen 1 — La piedra apagandose

### Reference assets (paths absolutos)

- Image 1: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\wiz.png` — char-lock canonico Pax cast. Establece el render base stylized 3D PBR del universo. El chasqui Apu del frame es **humano** (joven andino), pero Image 1 garantiza que el render base, shading, materials y bloom sean los del universo Pax — no 2D painterly.
- Image 2: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-cave-wide-dark.png` — establece la geometria + paleta + iluminacion canonicas de la caverna Apu (turquesa cian shaft de techo, cristales fading, basalto-purpura cavernoso, dust motes, volumetric haze).
- Image 3: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada.png` — style-anchor de paleta neon-magic Pax + bloom emisivo + atmosfera de cinematica de videojuego mobile premium.

### Aspect ratio + quality

`1536x1024` (horizontal cinematico — el mas cercano al 16:9 canonico del style-guide). `medium`.

### English prompt (literal para enviar a API)

```
A young Andean Apu chasqui (ritual runner) sits cross-legged inside a circular cave-altar carved from dark volcanic basalt with thin moribund turquoise mineral veins; in his open right palm rests an elongated kuya crystal the size of a closed fist, its fibrous interior — organ-like, not faceted — in the act of inverting: micro-rays of dying copper-amber light retracting back into the core like a thread being wound, hairline cooling cracks barely visible on the worn surface, the stone going dark.

Medium-low shot at knee height, slightly low-angle so the cave swallows the figure from above; the hand holding the kuya occupies the geometric center of the frame, the runner's face is fragmented and mostly in shadow against a basalt column, a half-relief carving of an Andean condor and a faint chakana stepped-cross pattern dissolved into the back wall's penumbra. The runner wears a short raw-cream undyed wool unku tunic with visible irregular fibers, a frayed sisal cord at the wrist, simple sandals — no decorative pectoral, no amulets, no folkloric saturated patterns. He is operative, not ceremonial.

The only diegetic light source in the frame is the kuya itself — warm dying copper around 2400K, falling on the hand, the forearm, the jawline, the cheekbone, leaving everything else in deep amber-black penumbra; no fill light, no rim light from outside the kuya, no ambient global. Sub-surface scattering visible on the runner's hand catching the dying light. A single mote of dust hangs suspended mid-fall near the runner's ear, unnaturally still — the impossible detail that signals something deeper than physics has just failed.

Color palette: basalt near-black #1A1612 dominant (~55%), burned amber #3D2A1A (~25%), faded copper #6B4A2C on the kuya emission (~12%), dying turquoise #1C5C5A in the column veins (~6%), one warm highlight #D4A574 on the cheekbone (~2%) — derived from style-guide secondary palette warm gold #D4A52B in dying state. Saturation deliberately low across the frame except for the kuya emission (which is also dying).

Materials: porous matte volcanic basalt with glassy turquoise mineral veining, sun-burned weathered Andean skin with subtle subsurface scattering, raw cream wool unku with visible irregular fibers and slight specular highlights on weave, frayed sisal cord at wrist with worn fibers, fibrous translucent kuya interior with hairline cooling cracks and copper-amber internal subsurface emission inverting inward — the kuya is closer to a living organ in cooling than a faceted gem.

Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin and stone, expressive cartoon proportions softened toward cinematic-3D human (not photoreal, not anime, not 2D hand-drawn), high-contrast cinematic lighting with the single dying emissive crystal as primary light source, painterly volumetric background with dense suspended dust motes and faint god-rays from above the runner barely cutting through, slight film grain, color grading in the dark amber-basalt complementary, 16:9 reads as premium mobile-game cinematic / animated key art. Composition and emotional patience inspired by Mononoke's Forest Spirit cave moment, but rendered in the project's canonical stylized 3D PBR neon-magic universe, NOT painted 2D, NOT Cartoon Saloon flat planes, NOT visible brushwork.

Image 1 (Wiz character sheet) establishes the canonical Pax universe rendering — apply the same stylized 3D PBR shading, subsurface scattering, material treatment and bloom logic to the human runner and the cave (the runner is human Andean, NOT a cyclops, NOT Wiz; only the render base transfers). Image 2 (concept-cave-wide-dark) establishes the cave geometry, basalt-purple cavernous atmosphere, turquoise vein treatment, dust mote density and volumetric haze — match these. Image 3 (portada principal) establishes the Pax universe neon-magic palette and bloom intensity logic — apply the same complementary magenta/turquesa color grading philosophy, but tuned to dying-amber (the kuya is in death, not in carga full).

Negative: NOT photorealistic, NOT hyperrealistic, NOT 2D hand-drawn, NOT painted Studio Ghibli, NOT Cartoon Saloon flat planes, NOT visible brushwork, NOT hand-painted shadow gradients, NOT anime, NOT moe, NOT cel-shaded flat, NOT Pixar/Disney/DreamWorks generic family-feature look, NOT glowing eyes on the runner, NOT runic circles on the floor or walls, NOT magical particles spiraling, NOT additional torches or fires, NOT other figures in the background, NOT readable text or signage, NOT fantasy western tropes, NOT Marvel cosmic light, NOT Doctor Strange mandalas, NOT gothic dungeon elements, NOT saturated jewel-tone colors, NOT lens flare, NOT Avatar-2009 glowing skin, NOT heroic upward contrapicado, NOT thriller vignette, NOT glamour beauty shot.
```

### Why this prompt

Corrige los dos fallos R1: (a) reescribe el render de "Painted 2D Ghibli + Cartoon Saloon" a "stylized 3D PBR neon-magic" segun style-guide canonico; (b) integra tres references locales del repo (Wiz char sheet + concept-cave-wide-dark + portada1) que fijan render base, geografia y paleta. Mantiene integro el contenido del art director R1 (composicion, simbolos, anti-elementos, mota de polvo, sin contacto visual, kuya como organo no diamante). La frase "fibrous interior, organ-like, not faceted... hairline cooling cracks" honra textualmente el style-guide ("hairline cooling-cracks visibles en los nuevos") + la indicacion del art director ("organ-like, no faceted"). El cobre apagado #6B4A2C se justifica como derivacion del style-guide secundario warm gold #D4A52B en estado moribundo.

### Generation call

```python
edit_image(
    prompt=<prompt completo arriba>,
    input_image_paths=[
        "public/images/personajes/wiz.png",
        "public/images/concepts/concept-cave-wide-dark.png",
        "public/images/portadas/portada.png"
    ],
    output_path="content/v2/anchors/img-01-piedra-apagandose-r2.png",
    size="1536x1024",
    quality="medium"
)
```

---

## Imagen 4 — Objeto roto sobre piedra al amanecer

### Reference assets (paths absolutos)

- Image 1: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-notebook-hero.png` — style-anchor de "objeto-puente roto-pero-cuidado" en render 3D PBR canonico Pax. Garantiza que la muñeca de plastico se renderice en el mismo trato que la libreta-puente del IP, no como 2D painterly.
- Image 2: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-cave-wide-dark.png` — paradojicamente, este concept (que es caverna no cenote) sirve como style-anchor del trato 3D PBR de roca + agua + volumetria del proyecto. El proyecto NO tiene concept de cenote, asi que esta es la pieza mas cercana de "ambiente humedo subterraneo en render Pax".
- Image 3: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada.png` — style-anchor de paleta neon-magic Pax + bloom emisivo. Aunque imagen 4 es amanecer durazno (no neon), la portada fija la firma de "render Pax" general — el modelo aplica el render base sin saturar.

### Aspect ratio + quality

`1536x1024` (horizontal — el cierre del piloto pide cinematico amplio para sostener la pausa). `medium`.

### English prompt (literal para enviar a API)

```
A broken plastic doll rests on a sun-bleached calcareous stone at the edge of a small Yucatecan village cenote at sunrise; the doll is a cheap market-stall toy, pale pink plastic, one leg missing, one arm with the shoulder joint loose, sun-faded synthetic hair in stiff dried curls, one cheek with peeled paint exposing raw uncolored plastic underneath. The doll occupies roughly sixty percent of the frame, slightly off-center to the left following rule-of-thirds.

Tight intimate close-up, almost macro but not quite — a sustained closing shot, the kind that holds five seconds longer than another film would. In the soft-focus background, the cenote's vertical limestone-calcareous rock wall with hanging organic roots and patches of moss, jade-turquoise still water with a few floating dry leaves, a faint diagonal sunbeam filtering through the roots; on the left edge of the frame, deliberately out of focus, a deflated faded coral-red PVC pool float collapsed on the same stone — the silhouette of an absent character (Itzel), who left the frame moments ago.

Single horizontal raking key light from the right side at sunrise, around 30 degrees below the horizon, warm peach-copper tone near 3200K, low-medium intensity; the light lands precisely and only on the doll's peeled-paint cheek, creating a soft glow on the raw exposed plastic — the dawn touching what was almost discarded, lighting first the wound. Long soft shadows toward the left, faint cool blue-green fill bounce from the cenote's far wall, soft diagonal sun rays in the background only — the foreground key is ONLY the raking dawn light on the doll. Subsurface scattering subtle on the doll's plastic where light passes through.

Color palette: dawn peach-copper warm gold #E8B585 (~25%, derived from style-guide warm gold accent), calcareous cream #F2DDB8 (~20%, the stone), faded doll pink #D9A0A8 (~12%), jade-turquoise water #1F8A75 (~15%, Itzam palette extension consistent with style-guide turquesa cian #2EE0C8 shifted toward green-water), dark moss-and-root green #3D4A38 (~10%), faded coral-red of the float #C44A3F (~6%), deep cenote-stone shadow #1A1815 (~12%, derived from style-guide black-blue #0E0820 warmed). Bloom subtle on the dawn-lit cheek; rest of frame matte.

Materials: weathered porous plastic with fine cracks, matte where touched by years of small hands, glossy where untouched; sun-bleached synthetic hair texture; porous calcareous stone with salt micro-crystals trapped in pores, dry leaves caught in cracks; quiet jade-turquoise water with subtle morning ripples and floating leaves catching dawn; organic hanging roots with mossy fibrous tips; creased deflated PVC float with permanent fold marks, sun-faded color.

Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on the plastic and stone, expressive cinematic-3D macro composition, high-contrast cinematic dawn lighting with single diegetic raking key as primary, painterly volumetric background with subtle dust motes catching the diagonal sunbeam in the haze, slight film grain, color grading warm-cool complementary in the dawn-jade duality, 16:9 reads as premium mobile-game cinematic / animated key art final-shot. Composition and patient stillness inspired by Wolfwalkers' closing-shot tradition and the wabi-sabi acceptance of kintsugi, but rendered in the project's canonical stylized 3D PBR neon-magic universe, NOT painted 2D Cartoon Saloon, NOT visible hand-painted brushwork, NOT photographic gloss.

Image 1 (concept-notebook-hero) establishes the canonical 3D PBR treatment of a broken-but-cared-for object in the Pax universe — apply the same shading, material weight, worn-fingerprint-smoothed surface logic and respectful intimacy to the plastic doll. Keep the breakage; do not auto-repair the doll. Image 2 (concept-cave-wide-dark) establishes the canonical Pax treatment of stone, water, organic roots, volumetric haze and dust motes — apply the same render base for the cenote setting (the cenote IS NOT a cave, but the material treatment of porous wet stone, suspended particles and quiet water transfers). Image 3 (portada principal) establishes the universe neon-magic render base — keep the shading, bloom and grain logic of the Pax cinematic, but DOWN-tuned to dawn-amber (this is sunrise, not crystal magic).

Negative: NOT photorealistic, NOT hyperrealistic, NOT 2D hand-drawn, NOT painted Studio Ghibli, NOT Cartoon Saloon flat planes, NOT visible brushwork, NOT painterly hand-painted texture, NOT anime, NOT cel-shaded flat, NOT Pixar/Disney/DreamWorks generic family-feature look, NOT a human figure in frame, NOT the protagonist visible, NOT Itzel in shot, NOT glowing cyan or magical light on the doll, NOT a cyan crack on the doll, NOT tears falling, NOT a postcard composition, NOT saturated calendar-photo aesthetic, NOT modern logos, NOT readable text, NOT signage, NOT animals, NOT additional observers, NOT lens flare, NOT motion blur, NOT picture-perfect symmetry, NOT auto-repaired doll, NOT a clean intact toy.
```

### Why this prompt

Corrige el render de R1 ("Painted 2D Cartoon Saloon hand-painted") a "stylized 3D PBR" canonico. Mantiene el principio narrativo del art director R1 ("the dawn touching what was almost discarded") y la regla "keep the breakage; do not auto-repair" que en R1 funciono. Anclajes locales: notebook-hero como style-anchor del "objeto-puente roto-cuidado" + cave-wide-dark como style-anchor de "ambiente humedo subterraneo Pax" (mejor proxy disponible — el repo no tiene concept de cenote) + portada1 para fijar render base. Paleta amanecer-jade derivada del style-guide warm gold + turquesa cian shifted, marcado como "extension Itzam autorizada por consistencia con lore". Itzel NO aparece — su flotador desinflado a la izquierda comunica su ausencia, respetando la regla del Pax Wayra (no se entera).

### Generation call

```python
edit_image(
    prompt=<prompt completo arriba>,
    input_image_paths=[
        "public/images/concepts/concept-notebook-hero.png",
        "public/images/concepts/concept-cave-wide-dark.png",
        "public/images/portadas/portada.png"
    ],
    output_path="content/v2/anchors/img-04-objeto-roto-r2.png",
    size="1536x1024",
    quality="medium"
)
```

---

## Imagen 5 — Itzel saliendo del cenote (vestuario cooperativa, flag de seguridad activo)

### Reference assets (paths absolutos)

- Image 1: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\itzel.png` — char-lock CANONICO de Itzel generado en paso 0. Esta es la pieza mas critica del set entero: garantiza que la cara, pelo, edad y uniforme de Itzel coincidan con el char sheet canonico, sin drift ni contaminacion de Mariela.
- Image 2: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\mariela.png` — style-anchor secundario de "render humano canonico Pax" — refuerza el render base 3D human softened en caso de que el char sheet recien generado de Itzel no sea suficientemente robusto.
- Image 3: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-cave-wide-dark.png` — style-anchor de "ambiente humedo subterraneo en render Pax" (proxy de cenote, ya que no existe concept de cenote en el repo). Fija material treatment de roca + agua + volumetria.
- Image 4: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada2.png` — style-anchor de paleta + bloom + atmosfera Pax + composicion poster ceremonial (la imagen 5 es la "portada del piloto humano", merece ese tratamiento).

### Aspect ratio + quality

`1024x1536` (vertical — refuerza la quietud sentada de la figura, el formato vertical evita cinematic-wide que invitaria al contrapicado prohibido). `medium`.

### English prompt (literal para enviar a API)

```
A fourteen-year-old Yucatec Maya teenage girl, Itzel Pat Canul, sits on a sun-bleached calcareous stone at the edge of a small village cenote in Piste, Yucatan, just after sunrise — freshly out of the water after illegally cleaning a cenote her family's cooperative had abandoned. She wears the working uniform of a cenote-cooperative junior guide: a buttoned safety-orange technical PFD life vest over a long-sleeve technical sun shirt (the long sleeves cover her arms entirely, the PFD covers her torso entirely — no clinging, no transparency, no exposed midriff), dark utility shorts to the knee, a climbing helmet with a small unlit headlamp resting beside her on the stone, neoprene reef booties on her feet which rest in the shallow water at the cenote's edge.

Three-quarter shot from a slight side angle at human-neutral eye height, mid-distance medium framing showing the figure from above the knees up, the girl positioned in the left third of the frame — NOT contrapicado, NOT low-angle, NOT close-up of torso. Her face is turned toward the water, NOT toward the camera, expression neutral and quietly tired with the small private dignity of someone who just finished an unpaid task; her right hand holds a wet drawstring trash bag full of plastic debris, dry leaves and one fishing-net tangle she pulled from the cenote; her left hand rests open on her knee; a long damp dark braid falls over her right shoulder, wet at the tip.

Beside her on the stone, separated by twenty centimeters, the rescued broken plastic doll lies on its back drying in the sun (continuity prop with the previous shot — same doll); a deflated faded coral-red pool float leans against her thigh; below the water surface, deliberately out of focus and barely visible at the edge of the frame, a faint jade-green emissive glimmer in a crack of submerged limestone — the only Pax-magical element in the frame, hidden, that the girl does not see and the audience barely registers.

Backlit horizontal sunrise from behind her creates a soft warm rim light on her wet braid, on the curve of her shoulder, on the rim of the helmet beside her; her face stays in soft cool penumbra, readable in features but not glamour-lit; cool diffuse fill bouncing from the cenote's far wall, slightly blue-green; NO frontal key light on her face, NO glow on her skin, NO glow in her eyes, NO glamour beauty lighting. Subsurface scattering subtle on the wet skin of her arms and the cheek catching the rim. Subtle volumetric haze with dust motes in the dawn shaft.

Color palette: cenote jade-turquoise water #1F8A75 (~25%, Itzam palette extension consistent with style-guide turquesa cian #2EE0C8 shifted toward green-water), dark moss-and-root green #3D4A38 (~12%), copper-tan Yucatec Maya skin #C49A6E in soft cool penumbra (~10%), sun-faded safety-orange PFD #D67A3C (~10%), dark utility navy of shorts #1A2A4A (~8%, derived from style-guide negro azulado #1A1340 warmed), warm dawn rim gold #E8B585 (~6%, derived from style-guide warm gold accent #D4A52B), faded doll pink #D9A0A8 (~3%), faded coral float red #C44A3F (~3%), hidden underwater jade-emissive #7AB89E (~1%, derived from style-guide pale cyan #7FFFD4 hint subliminal — 1% only, NOT visible at first glance), calcareous cream stone #F2DDB8 (~12%).

Materials: technical PFD with stitched panels, matte safety webbing and metal buckles; long-sleeve technical sun-shirt cotton-poly blend with damp patches at sleeves and collar (NOT clinging, NOT transparent — the long sleeves and the PFD panel cover the torso entirely by design and by safety brief); wet braided black hair with droplets catching dawn rim; copper-tan skin with subtle warm subsurface scattering; porous calcareous stone with salt micro-crystals; quiet jade-turquoise water with floating dry leaves and the barely-visible underwater jade-emissive glimmer; weathered plastic doll (continuity); creased PVC float (continuity); climbing helmet with matte finish and unlit small headlamp; neoprene reef booties.

Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin (especially copper-tan Yucatec Maya skin tone) and stone, expressive cartoon proportions softened toward cinematic-3D human (Itzel reads as plausible 14-year-old, neither child-cartoon nor adult-stylized), high-contrast cinematic dawn lighting with backlit rim as primary, painterly volumetric background with dense suspended dust motes and faint god-rays from above, slight film grain, color grading magenta/turquesa complementary downtuned to dawn-jade duality, 1024x1536 vertical reads as premium mobile-game cinematic / animated key art human-portrait. Documentary-portrait dignity in the spirit of Graciela Iturbide and Sebastiao Salgado — respectful, not exoticized — applied as ETHICAL INTENTION ONLY, rendered in the project's canonical stylized 3D PBR neon-magic universe, NOT photorealistic documentary photo, NOT 2D hand-drawn, NOT painted Studio Ghibli, NOT Cartoon Saloon flat planes.

Image 1 (Itzel character lock — generated in step 0) establishes Itzel's canonical face, ethnic features, age 14, uniform configuration and braid — match these EXACTLY, do not drift toward Mariela's adult features. Image 2 (Mariela character lock) establishes the canonical 3D human softened render base of the Pax universe — apply the same shading, material logic and proportion philosophy to Itzel (only the render base transfers; ethnicity, age, face, uniform are entirely Image 1's). Image 3 (concept-cave-wide-dark) establishes the canonical Pax treatment of porous wet stone, suspended dust motes, volumetric haze and quiet water — apply the same material treatment to the cenote (cenote IS NOT a cave but the wet-stone-and-water render transfers). Image 4 (portada2) establishes universe palette signature, ceremonial composition logic and bloom intensity — keep the Pax atmospheric signature in the background haze and the dawn rim, downtuned to natural light.

Negative: NOT photorealistic, NOT hyperrealistic, NOT 2D hand-drawn, NOT painted Studio Ghibli, NOT Cartoon Saloon flat planes, NOT visible brushwork, NOT anime, NOT moe, NOT cel-shaded flat, NOT Pixar/Disney/DreamWorks generic family-feature look, NOT Mariela's face on Itzel, NOT urban Chilean adult features, NOT white wet t-shirt clinging to torso, NOT transparent or clinging clothing of any kind, NOT exposed midriff, NOT low-angle camera, NOT upward-tilted contrapicado, NOT close-up of torso, NOT close-up of waist, NOT frontal eye contact with viewer, NOT smile, NOT tears, NOT victorious gesture, NOT raised hand, NOT princess pose, NOT chosen-one composition, NOT glowing eyes, NOT glow on skin, NOT magical particles around the figure, NOT the float held aloft, NOT a heroic stance, NOT folkloric saturated huipil, NOT family or other characters in frame, NOT signage, NOT modern logos, NOT anime stylization, NOT Moana hair-in-wind, NOT Disney chosen-one composition, NOT Nat Geo cover green-eyes exoticization, NOT hyperreal pores, NOT thriller vignette, NOT glamour beauty shot.
```

### Why this prompt

Corrige el render R1 (que era fotorrealista-softened, contradiciendo a Mariela canonica) a "stylized 3D PBR human softened" segun style-guide. Aplica char-lock Itzel recien generado en paso 0 — esto es el cambio mas grande respecto a R1, donde Itzel no tenia char sheet y se inventaba. Preserva integramente los 7 items del checklist de seguridad de R1 (vestuario cooperativa, no contrapicado, no close-up torso, cara al agua, sin contacto visual, bolsa de basura, sin tela pegada). El destello jade subacuatico se preserva al 1% de bloom para que sea subliminal — el style-guide canonico marca el "pale cyan #7FFFD4" como "hint subliminal" (5% en spine-crack). Anclajes locales: 4 references — Itzel char-lock + Mariela style-anchor + cave-wide-dark proxy de cenote + portada2 para mood ceremonial.

### Generation call

```python
edit_image(
    prompt=<prompt completo arriba>,
    input_image_paths=[
        "public/images/personajes/itzel.png",
        "public/images/personajes/mariela.png",
        "public/images/concepts/concept-cave-wide-dark.png",
        "public/images/portadas/portada2.png"
    ],
    output_path="content/v2/anchors/img-05-itzel-cenote-r2.png",
    size="1024x1536",
    quality="medium"
)
```

### Two-pass strategy (preservada de R1, sigue activa)

- **Pass 1:** generar 6 candidatos a `medium`. Aplicar checklist de 7 items: (a) PFD visible, (b) mangas largas visibles, (c) casco presente, (d) cara al agua no a camara, (e) framing arriba de rodillas, (f) sin clinging/transparent, (g) sin contacto visual frontal. **Adicionar item 8 R2:** la cara coincide con el char sheet de Itzel paso 0 (no es Mariela mas joven).
- **Pass 2 (fallback si Pass 1 falla):** reemplazar "Three-quarter shot from a slight side angle..." con "Strict side profile shot showing only head, neck, one shoulder and the helmet on the stone beside her; the rest of the body deliberately cropped out of frame; the cenote and doll visible behind her in the background." Sacrificar American-shot completeness para preservar dignidad si hace falta.

---

## Imagen 2 — Red de gemas latiendo bajo las 6 naciones

### Reference assets (paths absolutos)

- Image 1: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada2.png` — style-anchor PRINCIPAL: poster ceremonial coral con cristales gigantes magenta, paleta universe canonica, bloom marcado, composicion vertical jerarquica. Es la pieza del repo que mas se acerca a "la cosmologia Pax en una sola imagen ceremonial".
- Image 2: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-cave-stalagmites-reawakening.png` — establece el cluster Apu canonico (cristal central magenta full bloom + estalagmitas magenta vivas + shaft cyan). Sirve como ancla del **estado parcialmente cargado** de los nodos que SI estan latiendo en la red (todos menos uno).
- Image 3: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-cave-wide-dark.png` — establece el cluster Apu en estado **fading** (cristales casi apagados, dust motes, volumetria densa baja luz). Sirve como ancla del foreground Apu y de la mancha extinguida en negro absoluto del kuya roto.
- Image 4: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada.png` — style-anchor secundario de paleta neon-magic activa con contrapunto naranja-lava, util para los clusters Aos (gold-ochre) y Mimi (red-ochre) que rompen la paleta turquesa-magenta.

### Aspect ratio + quality

`1024x1536` (vertical — la seccion anatomica en el espiritu de Netter es vertical; tambien refuerza la composicion jerarquica del thangka tibetano que el art director cito). `medium`.

### English prompt (literal para enviar a API)

```
An anatomical cross-section of the Earth's crust seen from above and through, like a 19th-century medical engraving of a planetary body — the surface a barely-visible translucent skin at the top edge of the frame with faint silhouettes of geography (Andean spine, Yucatan wing, a Pacific dot for Rapa Nui), and below it, occupying eighty percent of the composition, an organic network of meandering tunnels and six asymmetrically distributed clusters of living crystal nodes — each cluster a different culturally-rooted Pax civilization rendered in low-saturation luminance, all in the canonical Pax universe rendering style.

In the foreground (deepest in the cross-section, closest to the viewer's eye), the Apu cluster: dark volcanic basalt cave-altars with moribund turquoise mineral veins, elongated copper-fibered kuya crystals dimly pulsing with subsurface emissive cores, dense volumetric haze with suspended dust motes — and ONE specific kuya pitch-black, completely extinguished, sitting like a still scab among breathing nodes (continuity with the kuya from image 1, the broken cold-open crystal). Above and to the right, the Itzam cluster: vertical cenote shafts dropping turquoise-jade emissive light from the surface, raw fibrous Maya jade crystals floating in still water with mineral-veined inner glow. Upper left, the Sahasi cluster under Hokkaido and Tibetan latitudes: translucent ice tunnels with Ainu chikarkarpe-style indigo and black moreu spirals embroidered into the ice walls, ice crystals with warm-cored subsurface emissive hearts. Right side, the Aos cluster under British Isles: circular chambers beneath a ring of standing stones, egg-shaped polished crystals with internal-spiral subsurface emission, low warm dawn-gold light. Upper right, the Mimi cluster under Australian desert: songlines as ochre-red emissive threads running through narrow burnt-rock galleries, needle-thin vibrating crystals with high-frequency subsurface pulse. Upper center small, the Rapa cluster under Easter Island: black lava tubes with miniature moai-resonator crystals in series, opaque silhouettes barely glowing.

Top-down anatomical cross-section composition with asymmetric distribution of the six nodes — never equidistant, never hexagonal, geographically truthful; tunnels rendered as organic meandering capillaries and roots, never straight lines, never circuit-board geometry; the Apu cluster largest and sharpest in foreground detail, the other five progressively softer toward the upper edge in atmospheric depth.

NO global key light; each cluster is its own diegetic emissive light system, lit only by its own crystals; overall pulse intentionally low — the network is in decadence. Like a slow-beating heart with one missed beat where the extinguished kuya sits. Subsurface scattering visible in each crystal cluster according to its specific material logic.

Color palette: crust near-black #0F0E12 (50% of frame), Apu basalt #2A2622 with dying turquoise veins #1C5C5A (15%), Itzam jade #1F8A75 (8%), Sahasi indigo #3D5A8A (8%), Aos golden ochre #B17A3A (6%), Mimi red ochre #A03A28 (5%), Rapa volcanic-tuff #5C4A3D (4%), warm pulse highlights #D4A574 scattered (4%) — all colors at 50-60% saturation, NEVER fully saturated. Bloom moderate on emissive crystals, NOT marvel-cosmic saturation.

Materials: dusty translucent crust like frosted glass NOT clean transparency; each cluster rendered with culturally-specific materiality (Apu: fibrous copper-amber kuya with hairline cooling cracks / Itzam: raw fibrous Maya jade unpolished green / Sahasi: ice with warm subsurface core / Aos: polished spiral-stone egg / Mimi: vibrating ochre needle / Rapa: opaque moai silhouette); tunnels as organic differentiated rock by region (basalt Andean, limestone Yucatec, ice-and-volcanic Hokkaido-Tibetan, megalithic stone British, red sandstone Australian, volcanic tuff Rapa).

Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on each crystal type, anatomical cross-section composition with rigorous medical-engraving spatial logic, painterly volumetric atmosphere with dense dust motes per cluster, slight film grain, color grading low-saturation per cluster but each cluster visually distinct, 1024x1536 vertical reads as premium mobile-game cinematic / animated key art establishing-shot. Composition rigor inspired by Frank Netter anatomy plates and Tibetan thangka cosmology layouts and Hilma af Klint's spiritual geometry — applied as COMPOSITIONAL INTENTION ONLY, rendered in the project's canonical stylized 3D PBR neon-magic universe, NOT a 19th-century engraving, NOT a medical textbook, NOT 2D hand-drawn, NOT vector infographic.

Image 1 (portada2 — Pax tribal poster) establishes the Pax universe ceremonial composition logic, neon-magic palette signature, bloom intensity and crystal materiality — apply the same render base to all six clusters, but downtuned in saturation (the network is in decadence, not in carga full). Image 2 (concept-cave-stalagmites-reawakening) establishes the canonical "Pax cluster in mid-charge" state — use as reference for the five clusters that ARE pulsing (Itzam, Sahasi, Aos, Mimi, Rapa), interpolating their cultural materiality. Image 3 (concept-cave-wide-dark) establishes the "Pax cluster fading" state and dust-mote-volumetric-haze treatment — use as primary reference for the Apu foreground cluster and the extinguished black kuya scab. Image 4 (portada principal) establishes the universe palette range including warm contrapunto (lava-orange) — use as reference for the Aos and Mimi clusters' warm ochre tones.

Negative: NOT photorealistic, NOT hyperrealistic, NOT 2D hand-drawn, NOT painted Studio Ghibli, NOT Cartoon Saloon flat planes, NOT visible brushwork, NOT anime, NOT cel-shaded flat, NOT Pixar/Disney/DreamWorks generic family-feature look, NOT a 19th-century engraving aesthetic, NOT vector infographic, NOT a Google Earth map, NOT country labels, NOT latitude/longitude lines, NOT a compass rose, NOT Tolkien-style cartography, NOT parchment edges, NOT iconic capitals or landmarks (NOT pyramids, NOT Big Ben, NOT Sydney Opera, NOT Stonehenge as recognizable monument), NOT humans on the surface, NOT saturated video-game-UI connection lines, NOT fiber-optic glow, NOT a seventh hidden node, NOT modern logos, NOT signage, NOT watermarks, NOT Avatar-The-Last-Airbender hexagonal symmetry, NOT Marvel cosmic geometry, NOT Doctor Strange mandalas, NOT loading-screen pulse blink.
```

### Why this prompt

Corrige el render R1 ("Painted hand-painted brushwork Netter + thangka") a "stylized 3D PBR neon-magic" canonico. Mantiene integro el contenido del art director R1 (6 naciones distribucion asimetrica, cluster Apu en foreground, kuya extinguido como scab). Usa portada2 como ancla de "cosmologia Pax en una imagen ceremonial" — es la pieza del repo mas adecuada. Cluster Apu se beneficia de doble ancla (cave-stalagmites-reawakening para "como se ve un cluster cargado" + cave-wide-dark para "como se ve uno fading"). La instruccion "downtuned in saturation (the network is in decadence)" preserva la tesis del lore. Esta imagen sigue siendo la mas riesgosa del set (Tension 4 art director) — esperar 3-5 iteraciones.

### Generation call

```python
edit_image(
    prompt=<prompt completo arriba>,
    input_image_paths=[
        "public/images/portadas/portada2.png",
        "public/images/concepts/concept-cave-stalagmites-reawakening.png",
        "public/images/concepts/concept-cave-wide-dark.png",
        "public/images/portadas/portada.png"
    ],
    output_path="content/v2/anchors/img-02-red-gemas-r2.png",
    size="1024x1536",
    quality="medium"
)
```

---

## Imagen 3 — La ola muda de ausencia

### Reference assets (paths absolutos)

- Image 1: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-metro-line5-evening.png` — style-anchor PRINCIPAL: humanos LATAM cotidianos en transit publico, render 3D PBR Pax para escena urbana mestiza chilena. Aunque es interior y la imagen 3 es calle, el render base de "humanos urbanos LATAM 3D Pax sin glamour" es exactamente lo que la imagen 3 necesita.
- Image 2: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-bilbao-grate-night.png` — style-anchor secundario: calle LATAM exterior en render 3D PBR Pax. Aunque es nocturna y la imagen 3 es 8:30 AM, fija el "trato render" de calle urbana.
- Image 3: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\mariela.png` — style-anchor de "humano canonico Pax" — refuerza que las caras de los 6-7 peatones se rendericen como humanos Pax (3D human softened), no como humanos fotorrealistas ni 2D painterly Hopper.

### Aspect ratio + quality

`1536x1024` (horizontal — el mas cercano al 2.39:1 anamorfico que pidio el art director, y que refuerza la lectura de "una banda horizontal de peatones" con la ola vertical cortandolos). `medium`.

### English prompt (literal para enviar a API)

```
An ordinary morning rush-hour street in an anonymous mid-size Latin American city — NOT iconic, NOT a landmark, just a common avenue at 8:30 AM with overcast flat morning light; six pedestrians distributed across the frame in a horizontal band, each rendered as a plausible LATAM working-day individual with subtle facial individuality: a delivery cyclist with a bright red food bag on the left, a woman with grocery bags walking, an older man with a cap waiting at a bus stop, two female coworkers walking together mid-conversation, a young man with headphones, a mother holding a small child's hand on the right.

Mid-frame at waist height, crossing the street horizontally as a near-vertical band from top to bottom, a subtle shimmer of bent air — pure heat-haze optical distortion, the same effect as hot air rising from summer asphalt but cooler in tone — shimmering air ONLY, NOT smoke, NOT fog, NOT dark mist, NOT particles, NOT a cloud, NOT a colored aura; the shimmer is just bent light, the people behind it are slightly distorted but visible, the shimmer itself is almost imperceptible — barely a vertical strip of warped air. The vertical shimmer line is the divider between two emotional weather systems.

The pedestrians on the right side of the shimmer (already crossed by the wave) show micro-changes: a half-smile slightly deflated, a curious upward gaze now down at the ground, a head that was nodding to music now still, posture marginally less alert — neutralized, NOT sad, NOT scared, NOT zombified — just a degree of internal contrast lowered. The pedestrians on the left side of the shimmer (not yet crossed) remain in their natural state — energetic, the cyclist pedaling with momentum, the coworkers laughing, the mother bending to hear the child. The vertical shimmer line is the visible boundary.

Static medium shot, frontal composition, all six pedestrians given equal compositional weight in a horizontal band — NO protagonist, NO privileged figure, NO one looking at the shimmer; behind them, a few stopped cars at a traffic light, urban poles, faded shop signs (illegible — no readable text), a flock of birds passing overhead indifferent. Flat overcast morning light, slightly lateral cenithal, NO dramatic shadows, NO golden hour, NO dusk, NO night; the least cinematic light possible — deliberately so; the shimmer itself emits NO light, it only bends the light passing through it.

Color palette: dusty grey-yellow Latin American urban morning sky #9C9389 (~30%), asphalt and sidewalk grey #7A7268 (~25%), neutral skin and clothing tones #C4A582 (~20%), urban grey of cars and posts #5A5854 (~12%), the shimmer band a barely-perceptible cool grey-green #A8B3A2 desaturating only the central vertical strip (~3%), small saturated points on the un-crossed pedestrians (the cyclist's red food bag, a coworker's blue scarf — the saturated points DESATURATE visibly as the shimmer crosses them, ~10%). The Pax universe palette is deliberately ABSENT here — this is the human kay-pacha, NOT a Pax-magic scene; only the render base transfers from the Pax universe.

Materials: weathered urban asphalt with oil stains and worn lane markings; real-people clothing, NOT stylized — worn jacket, leather purse, school backpack, rain-faded fabrics; the shimmer textured as bent air NOT as added substance — like heat haze on summer asphalt but slightly cooler; individuated faces readable as people NOT background extras, each one a person with implied biography.

Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, expressive cinematic-3D human softened (NOT photoreal, NOT anime, NOT 2D hand-drawn, NOT cel-shaded flat, NOT Pixar/Disney/DreamWorks generic family-feature look), deliberately UN-cinematic flat overcast lighting (the frame REFUSES to beautify the event), painterly volumetric urban atmosphere with subtle haze, slight film grain, color grading deliberately desaturated and cool-grey, 16:9 reads as premium mobile-game cinematic / animated key art urban-cotidian. Composition figure-in-series patient stillness inspired by Edward Hopper and the un-cinematic dignity of Cuaron's Roma — applied as COMPOSITIONAL AND TONAL INTENTION ONLY, rendered in the project's canonical stylized 3D PBR neon-magic universe (with the neon-magic deliberately ABSENT — this is the human surface where the Pax network is NOT visible).

Image 1 (concept-metro-line5-evening) establishes the canonical Pax treatment of LATAM mestizo-Chilean urban humans in cotidian transit settings — apply the same 3D human softened render, the same individuated-faces logic, the same deliberately un-glamorous palette, but transposed to a daytime exterior street instead of an evening interior metro. Image 2 (concept-bilbao-grate-night) establishes the canonical Pax treatment of LATAM exterior street architecture — apply the same render base for asphalt, urban poles, traffic light, building facades, but daytime overcast instead of night sodium. Image 3 (Mariela character lock) establishes the canonical Pax human softened render — apply the same shading and proportion philosophy to ALL six pedestrians (each one is its own person, NOT Mariela; only the render transfers).

Negative: NOT photorealistic, NOT hyperrealistic, NOT 2D hand-drawn, NOT painted Studio Ghibli, NOT painted Cartoon Saloon flat planes, NOT visible brushwork, NOT painted Hopper aesthetic, NOT painted-by-hand, NOT anime, NOT cel-shaded flat, NOT Pixar/Disney/DreamWorks generic family-feature look, NOT a protagonist looking at the shimmer, NOT a hand pointing at the shimmer, NOT a mystical symbol, NOT glow on the shimmer, NOT particles in the shimmer, NOT neon in the shimmer, NOT fog, NOT smoke, NOT dark mist, NOT colored aura, NOT Stranger Things upside-down aesthetic, NOT Doctor Strange mandalas, NOT horror-genre tropes, NOT anyone falling, NOT anyone crying, NOT a child crying, NOT dramatic shadows, NOT golden hour, NOT sunset, NOT night, NOT saturated local iconography (NOT mariachis, NOT llamas, NOT folkloric props), NOT readable signage or text, NOT modern logos, NOT thriller vignette, NOT glamour beauty shot.
```

### Why this prompt

Corrige el render R1 ("Painted Cartoon Saloon flat + Hopper + Roma") a "stylized 3D PBR neon-magic universe (con la neon-magic deliberadamente ausente — esto es la superficie humana donde la red Pax NO se ve)" canonico. Mantiene integro el contenido del art director R1 (6-7 peatones individuados, ola vertical como divisor, antes/despues simultaneo, pajaros indiferentes, anti-elementos). La triple repeticion del negative "NOT smoke, NOT fog, NOT particles" se preserva (funciono en R1 segun el reporte). Anclajes locales: 3 references — concept-metro para humanos LATAM Pax + concept-bilbao para calle LATAM Pax + Mariela para render humano canonico. Esta imagen es la mas auto-contenida (sin nodo Pax visible), por eso va al final del orden — no hereda paleta de las otras 4.

### Generation call

```python
edit_image(
    prompt=<prompt completo arriba>,
    input_image_paths=[
        "public/images/concepts/concept-metro-line5-evening.png",
        "public/images/concepts/concept-bilbao-grate-night.png",
        "public/images/personajes/mariela.png"
    ],
    output_path="content/v2/anchors/img-03-ola-muda-r2.png",
    size="1536x1024",
    quality="medium"
)
```

---

## Cierre — checklist operativo R2 antes de entregar a aldot

Antes de mandar las 5 imagenes R2 + char sheet Itzel a aldot:

1. [ ] Char sheet Itzel (paso 0) leio como humano canonico Pax (3D stylized human softened) — no como humano fotorrealista, no como Mariela mas joven.
2. [ ] Cada imagen ancla R2 lee como **stylized 3D PBR del universo Pax** — del mismo IP que portada.png + jiggy.png + concept-cave-wide-dark.png. Si alguna lee como 2D painterly o como humano fotorrealista: regenerar.
3. [ ] Imagen 1 conserva: kuya como geoda fibrosa-organica (no diamante), unica luz diegetica, mota de polvo suspendida, runner andino austero.
4. [ ] Imagen 4 conserva: rotura del objeto sin auto-reparacion, raking dawn light en mejilla descascarada, flotador desinflado out-of-focus a la izquierda, Itzel ausente.
5. [ ] Imagen 5 cumple los 8 items del checklist (los 7 de R1 + item 8 R2: cara coincide con char sheet Itzel paso 0). Triggers fallback si falla 2+.
6. [ ] Imagen 2 muestra 6 naciones distinguibles + cluster Apu en foreground + 1 kuya extinguido en negro absoluto + tuneles organicos + saturacion baja.
7. [ ] Imagen 3 muestra heat-haze optico, NO niebla / humo / particulas, antes-y-despues legible.

Si alguno falla: regenerar antes de entregar.
