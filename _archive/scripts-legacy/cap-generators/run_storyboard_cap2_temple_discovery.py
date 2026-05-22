"""Storyboard Cap 2 — Encuentro con templo ushnu ancestral. Tras la pared de raíces que KZ derribó, una cámara antigua llena de polvo dorado y cristales apagados con escritura tallada. Jiggy, KZ, Byte y Wiz entrando."""

from openai_images import edit_image

PROMPT = """
[IDENTITY LOCK]
The characters in this scene are FOUR Pax — Jiggy, KZ, Byte, Wiz — of MIXED visual sub-archetypes. BOTH sub-archetypes must be respected exactly.

Sub-archetype A — exposed-cyclops Pax: Jiggy, Byte, Wiz. They are cyclops-type single-eyed humanoids with ONE central eye visible (no second eye), turquoise-teal skin, elongated pointed elastic ears, FOUR fingers per hand, 3.5-head proportions (Wiz 2.8-3 heads). Jiggy must match Image 1 (jiggy.png) exactly — leather chest harness, satchel, brown shorts, NO bandana, NO head accessory. Wiz must match Image 2 (wiz.png) exactly — long white beard, deep purple velvet hooded robe, magenta-violet staff. Byte must match Image 3 (byte.png) exactly — same cyclops single eye, his canonical outfit and accessories.

Sub-archetype B — domed-mask Pax: KZ. Smooth white matte dome-shaped mask covering the upper half of the face entirely (NO visible eyeballs, NO cyclops single eye showing through), eyes rendered as small round dark painted dots OR a softly-curved closed line on the white dome. Below the dome, lower face shows turquoise skin. Long thin feathers hanging from each ear-tip, single magenta-pink crystal pendant on a leather strap-harness, golden tribal cheek markings just under the white dome. Match Image 4 (kz.png) exactly.

Repeat: NEVER mix sub-archetypes. Jiggy/Byte/Wiz show ONE exposed central cyclops eye each. KZ shows the white domed mask with NO visible eyeballs.

[SUBJECT]
Discovery moment of Episode 2. The four Pax stand inside the threshold of a recently-revealed ancient subterranean ushnu — an Andean ancestral ceremonial platform-temple, but interpreted into the Pax visual vocabulary. The walls are carved with dense stone bas-relief frescos showing humans and Pax-like figures working side by side around a central crystal — pre-Columbian stylized linework that mixes Mayan glyph-like patterns, Quechua geometric chevrons, and Rapa Nui-style faces, intermixed but not photorealistically replicated from real-world cultures. Dormant, opaque, dark crystals embedded in the walls and floor — many. Golden-pale dust motes (#D9C28A pale-dusty gold) floating thick in the volumetric air, catching the cavern's residual magenta light. A torn-open root-wall on the left edge — fresh raw roots and stone debris — marks where KZ accidentally broke through. Wiz stands in the foreground with his staff lowered, his single cyclops eye wide with recognition. Jiggy half-step behind him, single eye lit with awe. KZ to the right, white-domed mask tilted in childlike wonder, one hand still on a piece of fallen rock (he caused this). Byte at the back-left, cyclops eye scanning, his holographic device throwing a faint cyan-green readout onto the nearest fresco. Mood: contemplative, mystical, ternura histórica — NOT thriller, NOT action.

[COMPOSITION]
Landscape 1536x1024 wide environmental shot, eye level slightly low to give scale to the ushnu chamber. Wiz on the left third with the broken root-wall behind him, the four Pax arrayed in depth across the middle and right thirds, the carved fresco wall as the dominant background plane filling the upper two thirds. Leading lines from the carved fresco grooves and the cavern stalactites converge toward the four Pax. Headroom above the group reserved for subtitles. Rule of thirds dominant. Foreground out-of-focus golden-pale dust motes in suspension as framing device.

[LIGHT + PALETTE]
Stylized 3D PBR semi-realistic shading with subsurface scattering on Pax skin and on KZ's white dome mask. Primary key light: warm pale-dusty gold (#D9C28A — anchor-spark hint, this is canonically the unique gold of ancestral Pax memory) shafting through the broken root-wall on the left, falling onto the carved fresco wall and the floor. Secondary rim: residual magenta from a single still-faintly-pulsing wall crystal in the back, casting magenta rim on the four Pax from behind. Cool turquoise fill from above. Bloom moderate on the residual crystal. Dense volumetric haze with thick golden dust motes. Palette: jade-magenta-basalt with a strong but localized warm pale-dusty-gold accent — gold dominates the historical-fresco wall, magenta and jade dominate the Pax. Deep blue-violet shadows #0E0820. NO surface daylight, NO modern tungsten.

[STYLE / RENDER]
Stylized 3D animation render, premium mobile-game cinematic / animated key art quality, semi-realistic PBR materials, slight film grain, 16:9 landscape 1536x1024 storyboard frame. NOT 2D, NOT painterly, NOT illustration, NOT anime, NOT photorealistic, NOT cel-shaded flat, NOT Pixar/Disney generic family-feature look.

[REFERENCE INTEGRATION]
Image 1 (jiggy.png) establishes IDENTITY LOCK for Jiggy and the exposed-cyclops Pax anatomy. Image 2 (wiz.png) establishes IDENTITY LOCK for Wiz. Image 3 (byte.png) establishes IDENTITY LOCK for Byte. Image 4 (kz.png) establishes IDENTITY LOCK for KZ and the domed-mask sub-archetype. Image 5 (concept-cave-stalagmites-reawakening.png) anchors cavern atmosphere and crystal language. Image 6 (portada.png) anchors render base and Pax palette. Apply the canonical Pax palette with the addition of pale-dusty gold #D9C28A as the unique tone of ancestral memory.

[NEGATIVE]
Do not include: any Pax of sub-archetype A drawn with a white domed mask, any Pax of sub-archetype B drawn with an exposed cyclops eye, two human eyes on any character, photographic reproductions of real Mayan/Quechua/Rapa Nui artifacts (the frescos must be Pax-stylized interpretations, not literal copies), 2D hand-drawn aesthetic, painterly Studio Ghibli style, photorealistic skin, five-fingered hands, anime stylization, cel-shaded flat coloring, Pixar/Disney generic look, fantasy battle clichés, magic circles, glowing portals, lightning bolts, accessories not present in the character references (no bandana on Jiggy, no helmets), HUD overlays, game UI, surface daylight, modern tungsten light, RPG dungeon clichés (no torches on sconces, no chests, no skeletons, no swords).
""".strip()

result = edit_image(
    prompt=PROMPT,
    input_image_paths=[
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\jiggy.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\wiz.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\byte.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\kz.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-cave-stalagmites-reawakening.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada.png",
    ],
    output_path=r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\content\storyboards\cap-2-temple-discovery.png",
    size="1536x1024",
    quality="medium",
)
print(f"OK cap-2-temple-discovery -> {result}")
