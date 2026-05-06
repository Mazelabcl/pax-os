"""Storyboard Cap 2 — Reacción del clan. Agatha + clan procesando los frescos: 'Esto ya pasó. Los humanos sabían. Y se les olvidó.' Asombro + responsabilidad. Beat emocional clave."""

from openai_images import edit_image

PROMPT = """
[IDENTITY LOCK]
The characters in this scene are FOUR Pax — Agatha, Wiz, Jiggy, KZ — of MIXED visual sub-archetypes. BOTH sub-archetypes must be respected exactly.

Sub-archetype A — exposed-cyclops Pax: Wiz, Jiggy. They are cyclops-type single-eyed humanoids with ONE central eye visible (no second eye), turquoise-teal skin, elongated pointed elastic ears, FOUR fingers per hand, 3.5-head proportions (Wiz 2.8-3 heads). Wiz must match Image 1 (wiz.png) exactly. Jiggy must match Image 2 (jiggy.png) exactly — NO bandana, NO head accessory.

Sub-archetype B — domed-mask Pax: Agatha, KZ. Smooth white matte dome-shaped mask covering the upper half of the face entirely (NO visible eyeballs, NO cyclops single eye showing through), eyes rendered as small round dark painted dots OR a softly-curved closed zen line on the white dome. Same elongated pointed elastic ears, same four-fingered hands.

Agatha specifically: LIME-GREEN skin (#A7F432-leaning, NOT turquoise — emphasized lime), white domed mask, maternal-spiritual posture, jade and amber accents on her wraps. Match Image 3 (agatha.png) exactly. Her body skin is unmistakably lime-green, not teal.

KZ specifically: turquoise body skin, white domed mask, long thin feathers from each ear-tip, single magenta-pink crystal pendant on leather strap-harness, golden tribal cheek markings just under the dome. Match Image 4 (kz.png) exactly.

Repeat: NEVER mix sub-archetypes. Wiz/Jiggy show ONE exposed central cyclops eye each. Agatha/KZ show the white domed mask with NO visible eyeballs. Agatha is LIME-GREEN, the others are TURQUOISE.

[SUBJECT]
Reaction beat of Episode 2. Agatha stands in the foreground, hand half-raised toward the carved fresco wall, her white-domed mask tilted in slow contemplative recognition, lime-green hand poised mid-gesture, expression communicated through body language and posture rather than facial detail (the dome cannot show eyes opening wide). She has just spoken the line that lands: 'Esto ya pasó. Los humanos sabían. Y se les olvidó.' Wiz next to her, his single cyclops eye half-closed in old grief — he recognizes this place even though he has never seen it. Jiggy slightly behind, single cyclops eye wide with awe and a touch of confusion — this is bigger than he expected. KZ at the right, white-domed mask tilted in childlike wonder, one hand still touching the wall — the wall crystal under his palm shows the faintest pale-cyan flicker (the canon: 'la memoria también es energía'). The carved fresco wall fills the background — humans and Pax figures working together with crystals — visible but slightly out of focus. Mood: contemplative, mystical, ternura histórica with weight of responsibility.

[COMPOSITION]
Landscape 1536x1024 medium ensemble shot, eye level slightly low. Agatha as foreground hero on the left third, slightly closer to camera. Wiz, Jiggy, KZ in mid-ground arrayed across the middle and right thirds in a loose receding line. Carved fresco wall fills the entire background plane, slightly soft-focus. Leading lines from the carved fresco grooves converge toward Agatha's gesture. Headroom above the group reserved for subtitles. Rule of thirds dominant.

[LIGHT + PALETTE]
Stylized 3D PBR semi-realistic shading with subsurface scattering on lime-green and turquoise skin and on the white domed masks. Primary key light: warm pale-dusty gold #D9C28A from above-left (the ancestral memory tone), falling on Agatha's mask and Wiz's beard, on the fresco wall. Secondary rim: residual magenta from off-frame healthy crystal, on the right side of all four characters. Cool turquoise atmospheric fill from above. The wall crystal under KZ's palm shows a subtle pale-cyan #7FFFD4 flicker — only 10% intensity, subliminal. Bloom moderate on KZ's crystal pendant and the fresco-wall residual crystal. Dense volumetric haze, thick golden dust motes. Palette: jade-magenta-basalt with strong pale-dusty-gold accent on the fresco and Agatha's amber wraps. Deep blue-violet shadows #0E0820. NO modern tungsten, NO surface daylight.

[STYLE / RENDER]
Stylized 3D animation render, premium mobile-game cinematic / animated key art quality, semi-realistic PBR materials, slight film grain, 16:9 landscape 1536x1024 storyboard frame. NOT 2D, NOT painterly, NOT illustration, NOT anime, NOT photorealistic, NOT cel-shaded flat, NOT Pixar/Disney generic family-feature look.

[REFERENCE INTEGRATION]
Image 1 (wiz.png) establishes IDENTITY LOCK for Wiz. Image 2 (jiggy.png) establishes IDENTITY LOCK for Jiggy and the exposed-cyclops anatomy. Image 3 (agatha.png) establishes IDENTITY LOCK for Agatha — match her LIME-GREEN skin, white domed mask, maternal posture exactly. Image 4 (kz.png) establishes IDENTITY LOCK for KZ. Image 5 (concept-cave-stalagmites-reawakening.png) anchors cavern atmosphere and crystal language. Image 6 (portada.png) anchors render base and Pax palette. Apply the canonical Pax palette with the addition of pale-dusty gold #D9C28A as the ancestral memory accent.

[NEGATIVE]
Do not include: any Pax of sub-archetype A drawn with a white domed mask, any Pax of sub-archetype B drawn with an exposed cyclops eye, Agatha drawn with turquoise skin (she MUST be lime-green), two human eyes on any character, generic Andean indigenous costumes on the characters (the carvings on the wall are stylized but the living Pax wear their own visual vocabulary), 2D hand-drawn aesthetic, painterly Studio Ghibli style, photorealistic skin, five-fingered hands, anime stylization, cel-shaded flat coloring, Pixar/Disney generic look, fantasy battle clichés, magic circles, glowing portals, lightning bolts, accessories not present in the character references (no bandana on Jiggy, no helmets, no swords), HUD overlays, game UI, surface daylight, modern tungsten light, RPG dungeon clichés.
""".strip()

result = edit_image(
    prompt=PROMPT,
    input_image_paths=[
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\wiz.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\jiggy.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\agatha.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\kz.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-cave-stalagmites-reawakening.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada.png",
    ],
    output_path=r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\content\storyboards\cap-2-clan-processing.png",
    size="1536x1024",
    quality="medium",
)
print(f"OK cap-2-clan-processing -> {result}")
