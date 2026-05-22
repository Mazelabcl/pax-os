"""Storyboard Cap 2 — Detalle de los frescos. Close-up de uno de los frescos mostrando un humano antiguo y un Pax conectados por un cristal entre ellos. Descubrimiento histórico: NO son los primeros."""

from openai_images import edit_image

PROMPT = """
[IDENTITY LOCK]
This image shows a CARVED STONE BAS-RELIEF FRESCO, not living characters. The fresco depicts TWO figures rendered as ancient stylized stone carving: ONE human and ONE Pax. They must be carved in stone, not photographic.

The CARVED Pax figure has the visual vocabulary of the Pax species: cyclops-type single-eyed humanoid with ONE central eye visible (carved as a single round shape with an inset cyclops pupil), elongated pointed elastic ears, four-fingered hand, 3-3.5-head proportions. Stylized into pre-Columbian-inflected stone bas-relief lines (Mayan-glyph-like geometric chevrons, Quechua-like step patterns, Rapa Nui-like simplified face) — a Pax-universe interpretation, NOT a literal copy of any real-world artifact.

The CARVED human figure is a non-specific ancient indigenous human silhouette with two eyes, two arms, five fingers — also rendered in the same stylized stone bas-relief idiom. Robe, simple geometric headdress hint. The human and Pax are roughly the same visual scale, EQUAL in the composition (the canon: 'el que carga no carga solo' — the one who carries does not carry alone).

Between the human and the Pax, both figures hold their hands joined around a central CRYSTAL — carved in stone, faceted geometric — emerging from the meeting of their hands. A faint pale-cyan #7FFFD4 subliminal subsurface emission inside the crystal hints that the crystal is still alive even in the stone — only 8-15% intensity.

[SUBJECT]
Macro close-up of the carved stone fresco from Episode 2's ancestral ushnu temple. The shot reveals the moment Byte's holographic device throws a faint cyan readout across the carving — the device is NOT in frame, only its cool subtle light wash. Very fine cracks, weathering, mineral veining in the stone. Dust motes settled in the recessed grooves of the carving. Faint pale-dusty gold #D9C28A pollen-like glow across the high points of the carving from above. The fresco occupies almost the entire frame — this is the discovery shot, the close-up that says 'this happened before'.

[COMPOSITION]
Square 1024x1024 macro close-up. The two carved figures + central crystal centered slightly off-thirds. The carving fills 80% of the frame. A small slice of cavern darkness at the top-right corner gives depth context. Macro lens equivalent (100-150mm). Shallow but not extreme depth of field — the carving is sharp across the figures, the deeper grooves and corners fall slightly soft. NO living Pax in frame.

[LIGHT + PALETTE]
Stylized 3D PBR semi-realistic shading with rough porous igneous matte stone material. Primary key light: warm pale-dusty gold #D9C28A from upper-left (the ancestral memory tone), grazing across the high points of the carving. Secondary rim: faint magenta from a residual healthy crystal off-frame, casting a soft magenta rim on the stone's right edge. Subtle cool cyan #7FFFD4 subsurface emission inside the carved crystal at the center of the figures' joined hands — only 8-15% intensity, pale and quiet, NOT loud. Dense volumetric haze with thick golden-pale dust motes. Bloom subtle on the cyan crystal. Palette: warm pale-dusty gold + basalt + magenta rim, with the subliminal cyan accent. NO modern tungsten, NO surface daylight.

[STYLE / RENDER]
Stylized 3D animation render, premium mobile-game cinematic / animated key art quality, semi-realistic PBR stone materials, slight film grain, 1024x1024 storyboard frame. NOT 2D, NOT painterly, NOT illustration, NOT anime, NOT photorealistic, NOT cel-shaded flat. The carving must read as carved stone, not as a 2D illustration projected on stone.

[REFERENCE INTEGRATION]
Image 1 (concept-cave-stalagmites-reawakening.png) anchors cavern atmosphere, crystal language, and pale-dusty gold accent. Image 2 (jiggy.png) is the LIVING Pax reference — the carving's Pax figure must read as the same species (cyclops single eye, four fingers, pointed ears, 3-3.5 head proportions), translated into stone bas-relief. Image 3 (portada.png) anchors render base and the canonical palette. Apply the canonical Pax palette with the addition of pale-dusty gold #D9C28A as the unique tone of ancestral memory.

[NEGATIVE]
Do not include: a living moving Pax in frame (this is a static carved fresco, NO breathing characters), a literal copy of any real-world Mayan/Quechua/Rapa Nui artifact (it is a Pax-universe interpretation), the carved Pax with two eyes (it must be cyclops single-eyed), the carved Pax with a white domed mask (this fresco is from the exposed-cyclops era of Pax-human cooperation), the carved human figure as a Pax (it must read as human with two eyes), 2D hand-drawn aesthetic, painterly Studio Ghibli style, photorealistic stone, anime stylization, cel-shaded flat coloring, Pixar/Disney generic look, glowing magic effects beyond the subtle cyan subsurface, magic circles, glowing portals, lightning bolts, modern tungsten light, surface daylight, RPG dungeon clichés (no torches, no skeletons), text or runes that read as legible English / Latin alphabet — only abstract pre-Columbian-inflected geometric glyph-language.
""".strip()

result = edit_image(
    prompt=PROMPT,
    input_image_paths=[
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-cave-stalagmites-reawakening.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\jiggy.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada.png",
    ],
    output_path=r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\content\storyboards\cap-2-fresco-close-up.png",
    size="1024x1024",
    quality="medium",
)
print(f"OK cap-2-fresco-close-up -> {result}")
