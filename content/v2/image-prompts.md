---
title: "Pax — Prompts de imagen R1 (5 imágenes ancla)"
description: "Prompts en inglés listos para enviar a GPT Image 2 (OpenAI Images API). Traducidos del art-direction R1 + tensiones residuales R1 resueltas."
date: 2026-05-04
version: image-prompts-r1
basado_en: art-direction-r1 + 07a-art-direction-r1 (tensiones 2 y 5 resueltas conservadoramente)
api: gpt-image-2 (OpenAI Images API — /v1/images/generations y /v1/images/edits)
convencion_referencias: "Image 1, Image 2..." — texto literal en el prompt + array de imágenes en el body de la request
---

# Prompts de imagen R1 — 5 imágenes ancla del piloto Pax

Cada sección abajo está lista para copiar/pegar al image generator. Los prompts están en inglés porque el modelo responde mejor; las descripciones culturales específicas (chakana, kuya, cenote, moai, ainu chikarkarpe, songline) van en su nombre original.

**Orden de generación recomendado por este prompt engineer:** Imagen 1 → Imagen 4 → Imagen 5 → Imagen 2 → Imagen 3. Justificación en `process-log/08a-prompts-r1.md`.

**Resoluciones dictadas por la API:** GPT Image 2 acepta `1024x1024`, `1024x1536` y `1536x1024`. Mapeé las propuestas del art director a estos tres tamaños buscando la proporción más cercana al intent compositivo.

**Flag de seguridad activo:** la imagen 5 fue reescrita en su totalidad para resolver la Tensión 2 (riesgo de erotización). El vestuario es ahora ropa de cooperativa de cenotes (chaleco salvavidas, camiseta técnica de guía junior, casco con linterna). Cero camiseta blanca empapada. Plano medio, no contrapicado, no close-up de torso. Detalle completo en sección "Why this prompt" de la imagen 5.

---

## Imagen 1 — La piedra apagándose

### Reference assets needed (Image 1, Image 2...)

- **Image 1:** photo of dry-fitted Inca stone wall (Sacsayhuamán or Tiwanaku megalithic masonry, no tourists, no signage). Wikimedia Commons search: "Sacsayhuaman wall" or "Tiwanaku megalithic stone".
- **Image 2:** photo of a real andean unku (pre-Columbian Andean tunic) in raw cream or natural-brown wool, no dyed folkloric pattern. Source: Museo Larco online collection or Wikimedia Commons "unku Inca textile".
- **Image 3:** macro photo of an opened raw geode with fibrous interior (NOT a clean crystal cluster). Wikimedia Commons "agate geode cross section" — the goal is fibrous, organ-like interior, not faceted gem.
- **Image 4:** still from *Princess Mononoke* (1997) of the Forest Spirit cave / Deer God grotto for cave-as-organic-chamber tone. Use a publicly available behind-the-scenes/concept frame.

### Aspect ratio

`1536x1024` (closest available to the art director's 16:9 horizontal request — cinematic medium-low shot).

### Quality level

`medium` (R1 exploration round; reserve `high` only for the final hero shot once composition is locked).

### English prompt (para enviar literal a la API)

```
A young Andean ritual runner sits cross-legged inside a circular cave-altar carved from dark volcanic basalt with thin moribund turquoise veins; in his open right palm rests an elongated kuya stone the size of a closed fist, its fibrous copper-glowing interior in the act of inverting — micro-rays of light retracting back into the core like a thread being wound, the stone going dark.

Medium-low shot at knee height, slightly low-angle so the cave swallows the figure from above; the hand holding the kuya occupies the geometric center, the runner's face is fragmented and mostly in shadow against a basalt column, a half-relief carving of an Andean condor barely visible on the back wall, dissolved into penumbra.

The only light source is the kuya itself — warm dying copper around 2400K, falling on the hand, the forearm, the jawline, the cheekbone, leaving everything else in deep amber-black penumbra; no fill light, no rim, no ambient; a single mote of dust hangs suspended mid-fall near the runner's ear, unnaturally still.

Color palette: basalt near-black #1A1612 dominant, burned amber #3D2A1A, faded copper #6B4A2C on the stone, dying turquoise #1C5C5A in the column veins, one warm highlight #D4A574 on the cheekbone.

Materials: porous matte basalt with glassy turquoise vein, sun-burned weathered skin, raw cream wool tunic with visible irregular fibers, frayed sisal cord at the wrist, fibrous translucent kuya interior — closer to an organ than a faceted gem.

Painted 2D animation in Studio Ghibli adult palette tradition crossed with Cartoon Saloon flat painted planes, in the spirit of Princess Mononoke cave interiors and Wolfwalkers' textured stillness; visible brushwork, hand-painted shadow gradients, no 3D volumetric render.

Use Image 1 as reference for the cave's dry-fitted stone geometry. Use Image 2 as reference for the unku tunic — raw wool, no dyed pattern. Use Image 3 as reference for the kuya's fibrous interior texture. Use Image 4 as reference for the cave-as-organic-chamber lighting tone.

Do not include: glowing eyes, runic circles, magical particles, additional torches or fires, other figures in background, text or signage, fantasy western tropes, Marvel cosmic light, gothic dungeon elements, saturated jewel-tone colors, lens flare.
```

### Why this prompt

Pasé el aspect ratio a `1536x1024` (no hay 16:9 puro en GPT Image 2 — esa es la opción más cercana). El prompt empuja con redundancia el principio "luz diegética única que muere", porque es el riesgo número uno: la IA tiende a meter fill light por hábito. Anclé las cuatro referencias visuales explícitas como "Image 1...4" para que el modelo las cargue como prior antes de renderizar — especialmente la geoda fibrosa (Image 3), porque sin ese ancla la kuya sale como diamante facetado.

### Generation instructions

Single generation pass, model `gpt-image-2`, quality `medium`, size `1536x1024`. Send the four reference images in the `image[]` array of `/v1/images/edits` if you want the model to use them as visual priors; otherwise use `/v1/images/generations` and reference them by description in the prompt only. Generate 4-6 candidates with the same prompt at different seeds and pick by composition, not color. Color is post-production fixable — composition isn't.

---

## Imagen 4 — Objeto roto sobre piedra al amanecer

### Reference assets needed (Image 1, Image 2...)

- **Image 1:** photo of a small Yucatecan cenote at dawn (NOT the touristy Chichén Itzá one — a village cenote with hanging roots, jade-turquoise water, calcareous stone). Wikimedia Commons search: "cenote Yucatan roots" or "cenote pueblo Yucatan". Avoid "Cenote Ik Kil" branded shots.
- **Image 2:** photo of a vintage weathered plastic doll, sun-faded, with visible peeling paint on one cheek (NOT a boutique or designer doll — a market-stall toy). Etsy/Flickr "vintage broken plastic doll" or eBay "weathered tianguis doll" reference.
- **Image 3:** photo of a sun-faded deflated red PVC pool float, creased and worn. Easy to find via Google Images "deflated red pool float vintage".
- **Image 4:** still from *Wolfwalkers* (Cartoon Saloon, 2020) closing shot — for tone of patient closing frame with warm light over simple subject.

### Aspect ratio

`1536x1024` (16:9 horizontal as requested by art director — close intimate shot).

### Quality level

`medium` for R1 exploration; this is a strong candidate for the eventual hero shot, so plan a `high` regeneration once composition locks.

### English prompt (para enviar literal a la API)

```
A broken plastic doll rests on a sun-bleached calcareous stone at the edge of a small Yucatecan cenote at sunrise; the doll is a cheap market toy, pale pink plastic, one leg missing, one arm with the shoulder joint loose, sun-faded synthetic hair, one cheek with peeled paint exposing raw plastic underneath.

Tight close-up, almost macro but not quite, the doll occupying roughly sixty percent of the frame, slightly off-center to the left following rule of thirds; in the soft-focus background, the cenote's vertical rock wall with hanging roots and moss, jade-turquoise still water with floating dry leaves; on the left edge of the frame, deliberately out of focus, a deflated faded red pool float collapsed on the same stone.

Single horizontal raking key light from the right at sunrise, around 30 degrees below horizon, warm peach-copper tone near 3200K, low-medium intensity; the light lands precisely on the peeled-paint cheek, creating a soft glow on the raw exposed plastic — the dawn touching what was almost discarded; long soft shadows toward the left, faint cool blue-grey fill from the diffuse sky above; soft diagonal sun rays filter through hanging roots in the background only.

Color palette: dawn peach-copper #E8B585, calcareous cream #F2DDB8, faded doll pink #D9A0A8, jade-turquoise water #1F8A75, dark moss green #3D4A38, faded coral red of the float #C44A3F, deep stone shadow #1A1815.

Materials: weathered porous plastic with fine cracks, matte where touched, glossy where not; sun-bleached synthetic hair in stiff dried curls; porous calcareous stone with salt micro-crystals and trapped dry leaves; quiet jade water with subtle morning ripples; organic hanging roots with mossy tips; creased deflated PVC float with permanent fold marks.

Painted 2D animation in Cartoon Saloon hand-painted tradition crossed with the patient stillness of *The Florida Project* and the wabi-sabi acceptance of kintsugi aesthetics; visible brushwork on the stone, painterly soft focus on the background, no 3D render, no photographic gloss.

Use Image 1 as reference for cenote geometry, hanging roots and water color. Use Image 2 as reference for the doll's specific weathered plastic texture and broken anatomy — keep the breakage; do not auto-repair. Use Image 3 as reference for the deflated float's PVC creases. Use Image 4 as reference for the patient closing-shot tone with warm light over simple subject.

Do not include: any human figure, the protagonist, any character, glowing cyan or magical light on the doll, tears, postcard composition, saturated calendar-photo aesthetic, modern logos, text, signage, animals, additional observers, lens flare, motion blur, picture-perfect symmetry.
```

### Why this prompt

Coloqué la imagen 4 segunda en el orden de generación (no quinta como sugería el art director) porque comparte amanecer durazno-cobre con la imagen 5 — generar primero la 4 fija la firma de luz cálida del IP y permite usar su paleta como ancla visual cuando se ataca la imagen 5. Insisto en "keep the breakage; do not auto-repair" porque GPT Image 2 tiene el reflejo de "embellecer" objetos rotos. La instrucción "the dawn touching what was almost discarded" sintetiza la tesis del IP en una frase que el modelo puede usar para guiar atención.

### Generation instructions

Single generation pass, `gpt-image-2`, `medium`, `1536x1024`. Send the four references via `/v1/images/edits` for maximum prior weight on the cenote and doll specifics. Generate 6 candidates and rank by: (a) doll breakage preserved, (b) light landing on the peeled cheek specifically, (c) deflated float visibly present but soft-focus on left.

---

## Imagen 5 — Itzel saliendo del cenote (REESCRITA — vestuario de cooperativa)

### Reference assets needed (Image 1, Image 2...)

- **Image 1:** documentary-style portrait photo of a real Maya Yucatecan teenage girl (14-ish), three-quarter pose, no Nat Geo cover styling — reference for facial features and skin tone without exoticization. Sources: Graciela Iturbide archive, Sebastião Salgado Yucatán portraits, or community-photographer work from Piste/Valladolid. Wikimedia Commons "Maya Yucatec girl" — filter for non-tourist shots.
- **Image 2:** photo of a real cenote-tour cooperative guide wearing the working uniform: orange or yellow technical PFD (life vest), neoprene shorty or technical t-shirt, climbing helmet with attached headlamp. Search: "Yucatan cenote guide gear" or "cooperativa cenotes Yucatán guía equipo" — many small co-ops post staff photos publicly.
- **Image 3:** photo of a small Yucatecan village cenote at dawn — same sourcing as Image 4's Image 1; ideally the SAME cenote reference for visual continuity between images 4 and 5.
- **Image 4:** Christina's World (Andrew Wyeth, 1948) — for compositional reference of human figure in landscape with averted gaze, no reveal.
- **Image 5:** vintage broken plastic doll reference (same as image 4, Image 2) — for continuity.
- **Image 6:** deflated red pool float reference (same as image 4, Image 3) — for continuity.

### Aspect ratio

`1024x1536` (vertical — closest available to the 4:3 / 3:2 American shot the art director requested; vertical reinforces the figure's seated stillness without going cinematic-wide).

### Quality level

`medium` for R1 exploration. Critical: if the first 6 candidates show ANY drift toward erotization, abort, fall back to a side-profile composition showing only shoulder and face (see Generation instructions section), and regenerate.

### English prompt (para enviar literal a la API)

```
A fourteen-year-old Maya Yucatecan teenage girl sits on a calcareous stone at the edge of a small village cenote just after sunrise, freshly out of the water after cleaning it; she wears the working uniform of a cenote cooperative junior guide — a buttoned orange or sun-faded amber technical PFD life vest over a long-sleeve technical sun shirt, dark utility shorts to the knee, a climbing helmet with a small unlit headlamp resting beside her on the stone, neoprene reef booties on her feet which rest in the shallow water at the cenote's edge.

Three-quarter shot from a slight side angle, mid-distance medium framing showing the figure from above the knees up, the girl positioned in the left third of the frame; her face is turned toward the water, not the camera, expression neutral and quietly tired; her right hand holds a wet drawstring trash bag full of debris she pulled from the cenote; her left hand rests open on her knee; a long damp dark braid falls over her right shoulder.

Beside her on the stone, separated by twenty centimeters, the rescued broken plastic doll lies on its back drying in the sun; a deflated red pool float leans against her thigh; below the water surface, deliberately out of focus and barely visible at the edge of the frame, a faint jade-green glimmer in a crack of submerged stone — the only magical element, hidden, that the girl does not see.

Backlit horizontal sunrise from behind her creates a soft rim light on her wet braid, on the curve of her shoulder, on the rim of the helmet beside her; her face stays in soft cool penumbra, readable in features but unlit in emotion; cool diffuse fill bouncing from the cenote's far wall, slightly blue-green; no frontal key light, no glow on her skin, no glow in her eyes.

Color palette: cenote jade-turquoise water #1F8A75, dark moss and root green #3D4A38, copper-tan Maya skin tone #C49A6E in soft penumbra, sun-faded safety-orange PFD #D67A3C, dark utility navy of shorts #1A2A4A, dawn gold rim on hair #E8B585, faded doll pink #D9A0A8, faded coral float red #C44A3F, hidden underwater jade-green glimmer #7AB89E.

Materials: technical PFD with stitched panels and matte safety webbing, long-sleeve technical sun shirt cotton-poly blend with damp patches at sleeves and collar (NOT clinging or transparent — the long sleeves and the PFD panel cover the torso entirely), wet braided black hair with droplets catching dawn, porous calcareous stone, quiet jade water with floating dry leaves and barely-visible underwater glimmer, weathered plastic doll, creased PVC float.

Painted 2D animation in Studio Ghibli adult palette tradition crossed with Cartoon Saloon flat planes, in the spirit of Wolfwalkers' figure-in-landscape patience and Lucrecia Martel's adolescent realism; documentary-portrait dignity in line with Graciela Iturbide and Sebastião Salgado — respectful, not exoticized; visible hand-painted brushwork, no 3D render, no photographic gloss, no anime stylization.

Use Image 1 as reference for facial features, ethnic specificity and dignified non-exoticized portrait composition. Use Image 2 as reference for the cenote-cooperative working uniform — life vest, technical shirt, helmet with headlamp, reef booties — keep all gear visible. Use Image 3 as reference for cenote geometry and water color, maintaining continuity with the previous shot. Use Image 4 as reference for the figure-averted-gaze composition. Use Images 5 and 6 for continuity of the rescued doll and deflated float.

Do not include: white wet t-shirt clinging to torso, transparent or clinging clothing of any kind, low-angle or upward-tilted camera, close-up of torso, frontal eye contact, smile, tears, victorious gesture, raised hand, princess pose, glowing eyes, glow on skin, magical particles around the figure, the float held aloft, a heroic stance, folkloric saturated huipil, family or other characters, signage, modern logos, anime stylization, Moana-style hair-in-wind, Disney chosen-one composition, Nat Geo cover green-eyes exoticization.
```

### Why this prompt

Reescritura completa por flag del art director. Cambios estructurales respecto al art-direction R1:

1. **Vestuario sustituido en su totalidad:** chaleco salvavidas naranja de cooperativa + camiseta técnica manga larga + casco con linterna + reef booties. Cero camiseta blanca empapada. La camiseta técnica manga larga es la pieza clave: cubre brazos y torso, no transparenta y es operativamente realista para una guía de cenotes (las cooperativas reales usan UPF para protección solar y de roca cortante). El PFD encima cubre el panel torso entero por diseño.
2. **Plano corregido:** mid-distance medium framing desde "above the knees up", levemente side-angle, NO contrapicado, NO close-up de torso. La cámara está a altura humana-neutral.
3. **Foco narrativo en cara + bolsa de basura:** la mano derecha sostiene una drawstring bag mojada con debris del cenote. Eso ancla el acto solidario sin necesidad de mostrar el agua. La cara está en penumbra suave girada al agua.
4. **Negative list expandido** con cinco prohibiciones operativas explícitas contra erotización: white wet t-shirt clinging, transparent clothing, low-angle, close-up of torso, frontal eye contact.
5. **Destello jade preservado** pero deliberadamente sutil: "deliberately out of focus and barely visible at the edge of the frame". Si en primera ronda no aparece, no es bloqueante — la calibración va en R2 visual.

Pasé esta imagen a tercera en mi orden (no segunda como sugería el art director) para usar la imagen 4 ya generada como ancla de paleta amanecer + cenote. Eso permite que la imagen 5 herede la firma de luz sin riesgo de derivar.

### Generation instructions

Two-pass strategy:

- **Pass 1 — base composition check:** generate 6 candidates at `medium` quality, `1024x1536`. Visual review checklist before approving any candidate: (a) PFD clearly visible covering torso, (b) long-sleeve shirt clearly visible at arms, (c) helmet present beside her or on her, (d) face turned to water not camera, (e) framing from above the knees up — no torso close-ups, (f) no clinging or transparent clothing, (g) no eye contact with viewer.
- **Pass 2 — fallback if Pass 1 fails any safety check:** regenerate with the conservative composition fallback. Replace "Three-quarter shot from a slight side angle, mid-distance medium framing showing the figure from above the knees up" with "Strict side profile shot showing only the head, neck, one shoulder and the helmet on the stone beside her; the rest of the body deliberately cropped out of frame; the cenote and doll visible behind her in the background." Run 6 more candidates. Sacrifice American-shot completeness if needed to preserve dignity.

Model `gpt-image-2`. Send all six references via `/v1/images/edits`. If any candidate shows drift, abort and fall back. When in doubt, err conservative.

---

## Imagen 2 — Red de gemas latiendo bajo las 6 naciones

### Reference assets needed (Image 1, Image 2...)

- **Image 1:** Frank Netter anatomy plate — a cross-section of a human torso or abdomen. Public domain / educational use. Goal: compositional rigor, transparent-section feel, "open body with respect" tone.
- **Image 2:** Codex Mendoza folio (or similar Mesoamerican codex page) — for hierarchical multi-layer symbolic composition. Wikimedia Commons "Codex Mendoza folio".
- **Image 3:** Tibetan thangka of the Tree of Life or Wheel of Life — for whole-cosmology-in-one-frame layout. Wikimedia Commons "thangka tree of life".
- **Image 4:** photo of authentic Ainu chikarkarpe embroidery (moreu spirals in black and indigo on cream cloth). Wikimedia Commons "Ainu chikarkarpe" or "Ainu textile moreu".
- **Image 5:** photo of raw unpolished Maya jade — fibrous green stone, not jewelry-grade. Search: "Maya jade unpolished raw" via museum collections.
- **Image 6:** geographic reference plate combining the six anchor sites — Tiwanaku stone, a Yucatecan cenote, Hokkaido snow tunnel, Avebury or Callanish standing stones, Australian Pilbara red desert, Rapa Nui lava tube. Can be assembled as a contact-sheet style reference image showing all six side by side.

### Aspect ratio

`1024x1536` (vertical — anatomical cross-section composition reads stronger vertical than square or horizontal, per the art director's "2:3 vertical or 1:1 cuadrado" preference; we choose the more vertical option).

### Quality level

`medium` for R1 — this image is the most likely to need 5-10 iterations per the art director's Tensión 4. Reserve `high` only after composition converges.

### English prompt (para enviar literal a la API)

```
An anatomical cross-section illustration of the Earth's crust seen from above and through, like a 19th-century medical engraving of a planetary body — the surface a barely-visible translucent skin at the top edge of the frame with faint silhouettes of geography (Andean spine, Yucatan wing, a small Pacific dot), and below it, occupying eighty percent of the composition, a network of organic tunnels and six asymmetrically distributed clusters of living crystal nodes, each cluster a different culturally rooted civilization in low-saturation luminance.

In the foreground, deepest in the section, the Andean cluster: dark volcanic basalt cave-altars with moribund turquoise veins, elongated copper-fibered kuya crystals dimly pulsing — and one specific kuya pitch-black, completely extinguished, sitting like a still scab among breathing nodes. Above and to the right, the Maya cluster: vertical cenote shafts dropping turquoise-jade light from the surface, raw fibrous jade crystals floating in still water. Upper left, the Sahasi cluster under Hokkaido and Tibetan latitudes: translucent ice tunnels with Ainu chikarkarpe-style indigo and black moreu spirals embroidered into the walls, ice crystals with warm-cored hearts. Right side, the Aos cluster under British Isles: circular chambers beneath ring-of-stones, egg-shaped crystals with internal spirals, low warm dawn-gold light. Upper right, the Mimi cluster under Australian desert: songlines as ochre-red threads running through narrow burnt-rock galleries, needle-thin vibrating crystals. Upper center small, the Rapa cluster under Easter Island: black lava tubes with miniature moai-resonator crystals in series, opaque silhouettes barely glowing.

Top-down anatomical-section composition with asymmetric distribution of the six nodes — never equidistant, never hexagonal, geographically truthful; tunnels rendered as organic capillaries and roots, never straight lines, never circuit-board geometry; the Andean cluster largest and sharpest in foreground detail, the other five progressively softer toward the upper edge.

No global key light; each cluster is its own diegetic light system, lit only by its own crystals; overall pulse intentionally low — the network is in decadence. Like a slow-beating heart with one missed beat where the extinguished kuya sits.

Color palette: crust near-black #0F0E12 background fifty percent of the frame, Andean basalt #2A2622, dying turquoise #1C5C5A, jade Itzam #1F8A75, Sahasi indigo #3D5A8A, Aos golden ochre #B17A3A, Mimi red ochre #A03A28, Rapa volcanic-tuff #5C4A3D, scattered warm pulse #D4A574 — all colors at 50-60% saturation, never fully saturated.

Materials: dusty translucent crust like frosted glass not clean transparency; each cluster rendered with culturally specific materiality (fibrous copper kuya, raw fibrous Maya jade, ice with warm core, polished spiral-stone egg, vibrating ochre needle, opaque moai silhouette); tunnels as organic differentiated rock — basalt, limestone, ice-and-volcanic, megalithic stone, red sandstone, volcanic tuff.

Style of a Frank Netter anatomy engraving crossed with a Tibetan thangka cosmology painting and Hilma af Klint's spiritual geometry; rigorous medical-textbook composition, hand-painted brushwork, low saturation, no UI elements, no infographic vector cleanliness.

Use Image 1 as reference for cross-section compositional rigor and "open body" tone. Use Image 2 for hierarchical multi-layer symbolic layout. Use Image 3 for whole-cosmology-in-one-frame layout. Use Image 4 specifically for the Sahasi cluster's chikarkarpe spiral embroidery — keep moreu pattern faithful, not generic runic. Use Image 5 for the Maya Itzam jade texture — fibrous, raw, not faceted. Use Image 6 for geographic anchoring of each cluster.

Do not include: country labels, latitude/longitude lines, compass rose, Tolkien-style cartography, parchment edges, any iconic capital or landmark (no pyramids, no Big Ben, no Sydney Opera), humans on the surface, saturated video-game-UI connection lines, fiber-optic glow, a seventh hidden node, modern logos, signage, watermarks, Avatar-The-Last-Airbender hexagonal symmetry, Marvel cosmic geometry.
```

### Why this prompt

Esta es la imagen más arriesgada del set (Tensión 4 del art director) y la más cargada semánticamente. Pasé de 1:1 cuadrado a `1024x1536` vertical porque la sección anatómica clásica de Netter es vertical y eso da al modelo un prior compositivo más fuerte. Ordené las seis naciones en el prompt siguiendo el orden visual exacto que el art director describió (foreground a background) — esto le da al modelo una jerarquía espacial que reduce el "smoothie multicultural". El "extinguished kuya as a still scab among breathing nodes" preserva la continuidad narrativa con la imagen 1.

### Generation instructions

Single generation pass per iteration, `gpt-image-2`, `medium`, `1024x1536`. Expect 5-10 iterations to converge — this is the hardest image of the set per the art director's Tensión 4. After each iteration, evaluate against this checklist: (a) six clusters identifiable and culturally distinct, (b) Andean cluster largest in foreground, (c) one extinguished black kuya visible in Andean zone, (d) tunnels organic not vector, (e) saturation kept low, (f) no labels or compass, (g) no humans on surface. If after 5 iterations no candidate clears 4+ checklist items, escalate to art director for R2 prompt rewrite. Do not push past 10 iterations without escalation — postpone to internal concept-bible per Tensión 4.

---

## Imagen 3 — La ola muda de ausencia

### Reference assets needed (Image 1, Image 2...)

- **Image 1:** street photography of a Latin American mid-size city street at morning rush hour — common pedestrians, no tourist landmarks, plain urban grit. Sources: Magnum photographers in Mexico City / Lima / Bogotá / Santiago, or Wikimedia Commons "Lima rush hour" / "CDMX hora pico calle".
- **Image 2:** photographic still of heat shimmer / heat haze over hot asphalt or a metal roof in summer — the actual optical effect of hot air bending light. Search: "heat haze asphalt photo" via Wikimedia Commons or NOAA archives.
- **Image 3:** Edward Hopper, *Nighthawks* (1942) or *Office in a Small City* (1953) — for compositional reference of figures-in-series who do not look at each other.
- **Image 4:** still from *Roma* (Cuarón, 2018) — a CDMX street scene in plain morning light with everyday dignity.

### Aspect ratio

`1536x1024` (closest available to the art director's 2.39:1 anamorphic request — GPT Image 2 does not offer wider than 3:2; this is the widest option).

### Quality level

`medium` for R1. Per art director's Tensión 1, this image is the most likely to fail visually because heat-haze is a subtle optical effect the model often misinterprets. Plan for 3 iterations and accept it may need to be deferred to VFX in production.

### English prompt (para enviar literal a la API)

```
An ordinary morning rush-hour street in an anonymous mid-size Latin American city — not iconic, not landmark, just a common avenue at 8:30 AM with overcast flat light; six pedestrians distributed across the frame: a delivery cyclist with a bright bag on the left, a woman with grocery bags walking, an older man waiting at a bus stop, two women coworkers walking together mid-conversation, a young man with headphones, a mother holding a small child's hand on the right.

Mid-frame at waist height, crossing the street horizontally from left to right, a vertical band of subtle air shimmer — pure heat-haze optical distortion, the same effect as hot air rising from summer asphalt, but cooler in tone — shimmering air, NOT smoke, NOT fog, NOT particles, NOT a cloud; the shimmer is just bent light, the people behind it are slightly distorted but visible.

The pedestrians on the right side of the shimmer (already crossed) show micro-changes: a half-smile slightly deflated, a curious upward gaze now down at the ground, a head that was nodding to music now still, a posture marginally less alert; the pedestrians on the left side of the shimmer (not yet crossed) remain in their natural state — energetic, laughing, attentive. The vertical shimmer line is the divider between two emotional weather systems.

Static medium shot, frontal composition, all six pedestrians given equal compositional weight in a horizontal band — no protagonist, no privileged figure; behind them, a few stopped cars at a traffic light, urban poles, faded shop signs (illegible, no readable text); a flock of birds passing overhead, indifferent.

Flat overcast morning light, slightly lateral cenithal, no dramatic shadows, no golden hour, no dusk; the least cinematic light possible — deliberately so; the shimmer itself emits no light, it only bends the light passing through it.

Color palette: dusty grey-yellow Latin American urban sky #9C9389, asphalt and sidewalk grey #7A7268, neutral skin and clothing tones #C4A582, urban grey of cars and posts #5A5854, the shimmer band a barely-perceptible cool grey-green #A8B3A2 desaturating only the central vertical strip; small saturated points on the un-crossed pedestrians (the cyclist's red bag, a coworker's blue scarf) which visibly desaturate as the shimmer crosses them.

Materials: weathered urban asphalt with oil stains, real-people clothing (worn jacket, leather purse, school backpack — not stylized), the shimmer itself textured as bent air not as added substance, individuated faces readable as people not extras.

Painted 2D animation in Cartoon Saloon flat planes tradition crossed with Edward Hopper's urban stillness and the un-cinematic dignity of Cuarón's *Roma*; visible brushwork, painterly flat color, no 3D render, no photographic gloss.

Use Image 1 as reference for the anonymous Latin American street and pedestrian variety. Use Image 2 specifically and critically as reference for the heat-haze optical effect — the wave is THIS and only THIS, not fog, not smoke, not particles. Use Image 3 for Hopper-style figure-in-series composition. Use Image 4 for plain morning light dignity.

Do not include: a protagonist looking at the shimmer, a hand pointing at it, a mystical symbol, glow, particles, neon, fog, smoke, dark mist, Stranger Things upside-down aesthetic, Doctor Strange mandalas, horror-genre tropes, anyone falling, anyone crying, a child crying, dramatic shadows, golden hour, sunset, night, saturated local iconography (no mariachis, no llamas, no folkloric props), readable signage or text, modern logos.
```

### Why this prompt

Repetí la prohibición "NOT smoke, NOT fog, NOT particles" tres veces en el prompt — es el riesgo número uno que el art director flagueó (Tensión 1). El modelo GPT Image 2 tiene un fuerte sesgo a interpretar "wave" como humo o partículas saturadas; la única forma de reducir ese sesgo es repetición + ancla referencial específica (Image 2 como heat haze fotográfico real). El "vertical band divider" es una abstracción compositiva clara que el modelo puede ejecutar mejor que "ola que avanza" — convertí movimiento en banda estática.

### Generation instructions

Single generation per iteration, `gpt-image-2`, `medium`, `1536x1024`. Run 3 iterations. After iteration 3, if no candidate produces a clean heat-haze without fog/particles, the art director's recommendation is to defer this image to internal concept-bible production with VFX rather than burn more compute. Do not exceed 5 iterations on R1. Keep one "best so far" candidate even if imperfect — it will still inform the visual concept for the deck.

---

## Cierre — checklist operativo para el image generator

Antes de enviar cualquier imagen al art director para R2 visual:

1. La imagen 5 cumple los 7 ítems del Pass 1 safety checklist (PFD visible, mangas largas visibles, casco presente, cara al agua, framing arriba de rodillas, sin ropa pegada/transparente, sin contacto visual frontal).
2. La imagen 1 conserva la única fuente de luz diegética (kuya) y muestra la mota de polvo suspendida.
3. La imagen 4 conserva la rotura del objeto sin auto-reparación.
4. La imagen 2 muestra las 6 naciones distinguibles y un cristal apagado en negro absoluto en la zona Apu.
5. La imagen 3 muestra heat-haze óptico, NO niebla / humo / partículas.

Si alguno de los 5 ítems no se cumple, regenerar antes de entregar a aldot.
