"""Storyboard Cap 1 — Establishing shot tribu Pax. Wiz reúne al clan core en la cámara central de cristales para mostrar el mapa: muchos cristales opacos, pocos vivos. Asombro contenido."""

from openai_images import edit_image

PROMPT = """
[IDENTITY LOCK]
The characters in this scene are Pax — a subterranean civilization, NOT human, NOT generic fantasy creatures, NOT Andean indigenous people. There are TWO distinct visual sub-archetypes among them and BOTH must be respected exactly.

Sub-archetype A — exposed-cyclops Pax: Wiz, Jiggy, Byte, Luxa. They are cyclops-type single-eyed humanoids with ONE central eye visible (no second eye, no companion eye), turquoise-teal skin, elongated pointed elastic ears, FOUR fingers per hand, 3-3.5-head proportions. Wiz at 2.8-3 heads (older, stockier), with long voluminous white beard, thick white tufted brow, deep purple velvet hooded robe, dark wooden staff topped with a magenta-violet glowing crystal — match Image 1 (wiz.png) exactly. Jiggy at 3.5 heads, with brown leather chest harness and explorer satchel, no head accessory, no bandana — match Image 2 (jiggy.png) exactly.

Sub-archetype B — domed-mask Pax: KZ, Onyx, Agatha. They have a smooth white matte dome-shaped mask covering the upper half of the face entirely (forehead, brow, eye area), with eyes rendered either as a single softly-curved closed zen line or as small round dark painted dots on the white dome — NOT as visible cyclops eyeballs. Below the dome, lower face shows turquoise skin (Agatha's body skin is LIME-GREEN #A7F432-leaning, NOT turquoise — emphasized lime). Same elongated pointed elastic ears, same four-fingered hands, same proportional language. KZ has long thin feathers hanging from each ear-tip and a single magenta-pink crystal pendant on a leather harness — match Image 3 (kz.png). Onyx has a stronger atletic build, basalt-dark muscular tone, jade accents — match Image 4 (onyx.png). Agatha has lime-green skin (NOT teal), maternal posture, jade and amber accents — match Image 5 (agatha.png).

Repeat: NEVER mix sub-archetypes — Wiz/Jiggy/Byte/Luxa show ONE exposed central eye; KZ/Onyx/Agatha show the white domed mask with NO visible eyeballs.

[SUBJECT]
Establishing council scene of Episode 1. The Pax clan core is gathered in the central crystal chamber of Uray Pacha. Wiz stands at center-left, weight on his magenta-violet staff, his single central cyclops eye half-closed with concern, his other hand gesturing toward a constellation-like map of crystals embedded in the cavern wall and floor — many of those crystals are visibly opaque and dim, only a few still pulse healthy magenta. Around Wiz in a loose semi-circle: Jiggy stands closest, lean and ready, leather harness across his torso, his single central eye wide and alert; KZ slightly behind, white domed mask tilted in childlike concern, hand reaching for his magenta pendant; Onyx solid behind Wiz, white-domed mask stoic, arms crossed, basalt-dark muscular frame; Agatha to the right with her lime-green skin and white-domed mask, hands resting open at her sides in a maternal calming gesture; Byte at the far back, single cyclops eye intent, holding up a small holographic device; Luxa at the right edge with her purple headband and warm golden cristal-lantern in hand, the only warm color in the scene. The composition reads as a clan council weighing a decision. The mood is grave but warm, NOT panicked.

[COMPOSITION]
Landscape 1536x1024 wide ensemble shot, eye level slightly low to give the cavern monumentality without making it grandiose. Wiz on the left third with the crystal map visible behind him, the clan arrayed across the middle and right thirds in a loose semi-circle, leading lines from cavern stalagmites converging toward Wiz and the wall-map. Headroom above the group reserved for subtitles. Rule of thirds dominant.

[LIGHT + PALETTE]
Stylized 3D PBR semi-realistic shading with subsurface scattering on all turquoise and lime-green Pax skin, on the white domed masks, and inside the crystals. Primary key light: a mix of healthy magenta crystals casting magenta rim light from behind the group and dimmer cool turquoise fill from above. Luxa's golden cristal-lantern (#FFE34D / #F1E3AA) is the only warm accent — visible as a localized warm pool on Luxa's hands and face only. Dense volumetric haze, dust motes catching the magenta and turquoise. Bloom moderate on emissives. Palette: jade-magenta-basalt-dominant, with one localized amber accent on Luxa. Deep blue-violet shadows #0E0820 / #1A1340. NO surface light, NO tungsten elsewhere.

[STYLE / RENDER]
Stylized 3D animation render, premium mobile-game cinematic / animated key art quality, semi-realistic PBR materials, slight film grain, 16:9 landscape 1536x1024 storyboard frame. NOT 2D, NOT painterly, NOT illustration, NOT anime, NOT photorealistic, NOT cel-shaded flat, NOT Pixar/Disney generic family-feature look.

[REFERENCE INTEGRATION]
Image 1 (wiz.png) establishes IDENTITY LOCK for Wiz. Image 2 (jiggy.png) establishes IDENTITY LOCK for Jiggy and the exposed-cyclops Pax anatomy. Image 3 (kz.png) establishes the domed-mask Pax sub-archetype and KZ specifically. Image 4 (onyx.png) anchors Onyx's atletic build and basalt accents. Image 5 (agatha.png) anchors Agatha's lime-green skin and maternal posture. Match all character anatomies exactly. Apply the canonical Pax palette: jade-green, basalt-dark, neon-magenta dominant, single warm-amber accent only on Luxa's lantern.

[NEGATIVE]
Do not include: any Pax of sub-archetype A drawn with a white domed mask, any Pax of sub-archetype B drawn with an exposed cyclops eye, two human eyes on any character, generic Andean indigenous costumes, 2D hand-drawn aesthetic, painterly Studio Ghibli style, photorealistic skin, five-fingered hands, anime stylization, cel-shaded flat coloring, Pixar/Disney generic look, fantasy battle clichés, magic circles, glowing portals, lightning bolts, accessories not present in the character references, no swords, no shields, no helmets, no bandanas on Jiggy, no extra jewelry beyond what each char sheet shows, HUD overlays, game UI, gem counters, surface daylight, warm tungsten beyond Luxa's lantern.
""".strip()

result = edit_image(
    prompt=PROMPT,
    input_image_paths=[
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\wiz.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\jiggy.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\kz.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\onyx.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\agatha.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada2.png",
    ],
    output_path=r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\content\storyboards\cap-1-clan-council.png",
    size="1536x1024",
    quality="medium",
)
print(f"OK cap-1-clan-council -> {result}")
