"""Storyboard Cap 1 — Cliffhanger / decisión de subir. Wiz le entrega un cristal vacío a Jiggy. 'Lo cargas allá arriba. Si vuelves, vuelve cargado.' Jiggy listo para salir corriendo como un chasqui antiguo."""

from openai_images import edit_image

PROMPT = """
[IDENTITY LOCK]
The characters in this scene are TWO Pax of the exposed-cyclops sub-archetype — Wiz and Jiggy. They are cyclops-type single-eyed humanoids with ONE central eye each (NO second eye, NO companion eye anywhere on the face), turquoise-teal skin, elongated pointed elastic ears, FOUR fingers per hand (not five), 3.5-head proportions for Jiggy and 2.8-3-head proportions for Wiz. Repeat: ONE central eye each, cyclops-type anatomy.

Wiz visually MUST match Image 1 (wiz.png): older, stocky, long voluminous white beard from below the single eye to chest, thick white tufted brow above the eye, deep purple velvet hooded robe (#3D2A66 / #4B2E80) with subtle turquoise rune trim, central chest medallion with small violet crystal, dark wooden staff topped with a glowing magenta-violet crystal. Match weathered, paternal, decisive expression.

Jiggy visually MUST match Image 2 (jiggy.png): lean, agile, single central eye wide and alert, brown leather chest harness with metal buckle, brown leather explorer satchel at the hip, brown shorts. NO head accessory, NO bandana, NO gem on forehead — silhouette is clean from above. Match the slight forward lean of an eager runner.

[SUBJECT]
Cliffhanger of Episode 1. Mid-shot of Wiz extending an UNLIT, dark, faceted crystal — palm-sized, dormant, with NO emission, no internal glow — toward Jiggy's open four-fingered hand. Jiggy stands ready, weight already shifted to the back foot as if he is about to bolt the moment the crystal touches his palm — an old-world chasqui (Andean ancestral runner-messenger) energy, but with Pax anatomy and Pax visual vocabulary. Wiz's expression is grave-paternal, his single eye half-closed, decision made. Jiggy's expression is determined, single eye wide, mouth slightly open as if about to say something but holding back. The dormant crystal between them is the visual anchor — its dormancy contrasts sharply with the healthy magenta crystals visible in the deep background of the cavern.

[COMPOSITION]
Landscape 1536x1024, eye level, two-shot framing both characters. Wiz on the left third in 3/4 turn toward Jiggy, Jiggy on the right third in 3/4 turn toward Wiz, the dormant crystal precisely centered on the middle vertical line, hands meeting at the dead center of the frame. Background: blurred cavern interior with bokeh of distant healthy magenta crystals on the left and a dark tunnel mouth opening upward on the right edge — the mouth Jiggy is about to run into. Headroom above both characters reserved for subtitles. Rule of thirds dominant.

[LIGHT + PALETTE]
Stylized 3D PBR semi-realistic shading with subsurface scattering on both Pax skins. Primary key light: cool turquoise fill from above-front. Secondary rim: distant healthy magenta crystals casting magenta rim light from behind both characters. The dormant crystal between them is conspicuously LIGHTLESS — it does NOT emit, it absorbs the ambient light and looks like dark glass. Wiz's staff-crystal glows softly magenta-violet in his other hand. Dense volumetric haze, dust motes. Bloom moderate on the staff-crystal only. Deep blue-violet shadows #0E0820. Palette: jade-magenta-basalt-dominant. NO warm tungsten, NO surface daylight.

[STYLE / RENDER]
Stylized 3D animation render, premium mobile-game cinematic / animated key art quality, semi-realistic PBR materials, slight film grain, 16:9 landscape 1536x1024 storyboard frame. NOT 2D, NOT painterly, NOT illustration, NOT anime, NOT photorealistic, NOT cel-shaded flat, NOT Pixar/Disney generic family-feature look.

[REFERENCE INTEGRATION]
Image 1 (wiz.png) establishes IDENTITY LOCK for Wiz — match his cyclops single eye, beard, robe, staff. Image 2 (jiggy.png) establishes IDENTITY LOCK for Jiggy — match his cyclops single eye, leather harness, satchel, shorts, clean silhouette without bandana. Image 3 (concept-cave-wide-dark.png) anchors deep-cavern atmosphere and the tunnel-mouth visual language. Image 4 (portada.png) anchors render base and Pax palette. Apply the canonical Pax palette.

[NEGATIVE]
Do not include: human anatomy with two eyes (Wiz and Jiggy each have ONE central cyclops eye), a second smaller eye anywhere on either face, white domed masks on either character, a glowing/lit crystal in the handoff (the crystal MUST be dormant and unlit — this is the central narrative point), generic Gandalf-style wizard, generic Andean indigenous costume, 2D hand-drawn aesthetic, painterly Studio Ghibli style, photorealistic skin, five-fingered hands, anime stylization, cel-shaded flat coloring, Pixar/Disney generic look, fantasy battle clichés, magic circles, accessories not present in Image 1 or Image 2 (no bandana on Jiggy, no goggles, no helmet, no gems on forehead, no extra jewelry), HUD overlays, game UI, surface daylight, warm tungsten light.
""".strip()

result = edit_image(
    prompt=PROMPT,
    input_image_paths=[
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\wiz.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\jiggy.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-cave-wide-dark.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada.png",
    ],
    output_path=r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\content\storyboards\cap-1-jiggy-receives-crystal.png",
    size="1536x1024",
    quality="medium",
)
print(f"OK cap-1-jiggy-receives-crystal -> {result}")
