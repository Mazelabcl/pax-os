"""Char sheet de KZ — el más joven del clan Pax. Torpe pero genio."""

from openai_images import edit_image

PROMPT = """
[IDENTITY LOCK]
The character is KZ, a young Pax — a non-human cave-dwelling humanoid species. KZ visually MUST match Image 1 (his canonical reference): turquoise-teal smooth skin (#21D8B6 base, #2EE0C8 highlights), elongated pointed elastic ears that flare outward like leaves, FOUR fingers per hand (not five), 3.5-head proportions. CRITICAL FACIAL ANATOMY of KZ: the upper half of his face is a smooth, white, matte, dome-shaped mask-like surface (NOT human skin) covering his forehead, brow and eye area entirely; his eyes are NOT visible as separate eyeballs — they read either as a single softly-curved closed line drawn across that white dome (sleeping/zen aspect) or as expressive small round dark dots painted on the white dome (cartoon-awake aspect); below the white dome the lower face shows the turquoise skin with a small soft mouth. Geometric golden tribal markings (small dashes, dots, sun-like glyphs) on the cheekbones and brow area, just under the white dome. Long thin feathers hanging from each ear-tip like earrings (one per ear, dangling). KZ wears a small leather strap-harness around the neck holding a single magenta-pink crystal pendant on his chest. Light golden tribal glyph tattoos visible on forearms. KZ is the same species and design language as Image 4 (jiggy.png) — same Pax DNA, same proportions, same skin treatment — but with KZ's distinctive white dome mask face instead of an exposed eye.

[SUBJECT]
KZ in a 3/4 medium hero portrait, head and torso visible. He is the youngest of the clan, pure-hearted, intuitive, joyful, clumsy-but-genius. Pose conveys his playful clumsiness: a slightly off-balance, loose, unposed stance with one shoulder higher than the other, head tilted softly to one side, one hand mid-gesture upward as if about to say something silly while juggling the other. A small mischievous-yet-surprised half-smile on his lower face. His expression is joyful and curious. Body language is light, almost about-to-trip, but radiating warmth and openness.

[COMPOSITION]
3/4 medium hero portrait, centered subject framed slightly off-thirds, eye level, head and torso visible to mid-belly, full feet not shown. Background: smooth gradient mixing warm amber (#F59E0B) and soft neon magenta (#EC4899) on a dark basalt vignette (#1E1E2E), with subtle floating Pax glyphs and tiny dust motes in suspension. Background non-distracting, characters reads cleanly.

[LIGHT + PALETTE]
Stylized 3D PBR semi-realistic shading with subsurface scattering on the turquoise skin and on the white dome of his face. Neon-magic cinematic lighting: warm amber rim from camera-right, magenta rim from camera-left-back, cool turquoise fill from above. Bloom on the magenta crystal pendant. Slight volumetric haze with dust motes. Palette weighted toward AMBER + MAGENTA to identify KZ as the young, warm-hearted member, jade and basalt as supporting tones.

[STYLE / RENDER]
Stylized 3D animation render, premium mobile-game cinematic / animated key art quality, semi-realistic PBR materials, slight film grain, 16:9-equivalent square 1024x1024 character sheet hero portrait. NOT 2D, NOT painterly, NOT illustration, NOT anime, NOT photorealistic, NOT cel-shaded flat, NOT Pixar/Disney generic family-feature look.

[REFERENCE INTEGRATION]
Image 1 (kz-ref-2) and Image 2 (kz-ref-1) are the canonical identity references for KZ — match his silhouette, white-dome face, turquoise skin, ear-feathers, golden facial markings and crystal pendant exactly, but render him with smoother surfaces, more elegant proportions, better PBR shading, and refined facial geometry that reads as expressive and youthful. Image 3 (jiggy.png) anchors the Pax species anatomy and proportional language. Image 4 (portada.png) anchors the canonical Pax palette, render base and atmospheric quality. Improve significantly on the original references' stiffness while preserving identity.

[NEGATIVE]
Do not include: human anatomy with exposed two human eyes, a single visible cyclops eyeball replacing the white dome, generic indigenous costumes, 2D hand-drawn aesthetic, painterly Studio Ghibli style, photorealistic skin, five-fingered hands, anime stylization, cel-shaded flat coloring, Pixar/Disney generic look, fantasy battle clichés, accessories not present in the references (no swords, no staves, no elaborate jewelry beyond the single magenta pendant and ear-feathers), no second eye, no goggles, no helmet, no sunglasses.
""".strip()

result = edit_image(
    prompt=PROMPT,
    input_image_paths=[
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\refs\kz-ref-2.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\refs\kz-ref-1.jpeg",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\jiggy.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada.png",
    ],
    output_path=r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\kz.png",
    size="1024x1024",
    quality="medium",
)
print(f"OK kz -> {result}")
