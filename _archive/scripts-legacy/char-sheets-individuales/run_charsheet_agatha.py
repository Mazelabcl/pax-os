"""Char sheet de Agatha — la espiritual-maternal del clan Pax."""

from openai_images import edit_image

PROMPT = """
[IDENTITY LOCK]
The character is Agatha, the spiritual-maternal Pax — a non-human cave-dwelling humanoid species. Agatha visually MUST match Image 1 (her canonical reference). UNIQUE TO AGATHA: her skin is GREEN-LIME (#7DD957 base, #A8E075 highlights, #4F9A2D shadow) — distinct from the turquoise of the rest of the clan. Elongated pointed elastic ears, FOUR fingers per hand (not five), 3.5-head proportions, slightly softer feminine silhouette. CRITICAL FACIAL ANATOMY of Agatha: the upper half of her face is a smooth, white, matte, dome-shaped mask-like surface covering her forehead, brow and eye area entirely; her eyes read as a single softly-curved closed line drawn across that white dome — serene and maternal. Below the white dome the lower face shows the green-lime skin with soft full lips and a warm gentle half-smile. Golden geometric markings (small dots, arched lines, sun-glyphs) painted around the mouth, chin and cheekbones. Above the white dome she has a thick voluminous mane of deep auburn-red dreadlocks/twists styled UPWARD and back like a flame-crown, held by a copper-brown leather headband around the forehead. Magenta diamond-shaped earrings hanging from each ear. A single magenta-pink crystal pendant on a thin cord around her neck, resting at her chest. Agatha is the same species template as Image 2 (jiggy.png) — same Pax anatomy DNA, same proportions — but green-skinned, female-coded, with her distinctive auburn dread-mane.

[SUBJECT]
Agatha in a 3/4 medium hero portrait, head and torso visible. She is the most spiritual and maternal of the clan — keeper of emotional balance, watchful guardian of the mission's focus, the clan's emotional anchor and compass. Pose conveys her serene maternal presence: half-frontal 3/4, calm centered posture, hands held together at the chest in a soft prayer/anjali gesture OR one hand raised slightly in a gesture of blessing/care. Shoulders relaxed and open, body language inviting and protective. A serene maternal calm in the closed eye-line, a gentle warm half-smile on her lips. She radiates ancient wisdom and tender care.

[COMPOSITION]
3/4 medium hero portrait, centered subject framed slightly off-thirds, eye level, head and torso visible to mid-belly with hands at chest. Background: smooth gradient mixing soft jade green (#10B981) and muted dusty magenta (#A0427A) with subtle warm amber/gold accents glowing like distant temple light, faint floating Pax glyphs and gentle volumetric dust motes. Background spiritual, warm-cool balanced.

[LIGHT + PALETTE]
Stylized 3D PBR semi-realistic shading with subsurface scattering on the green skin and on the white dome face. Neon-magic cinematic lighting: warm amber-gold rim from above-right (temple-light feel), soft magenta back-rim from camera-left, cool jade fill from below-front. Bloom on the magenta pendant and earrings. Subtle volumetric haze. Palette weighted toward SOFT JADE + MUTED MAGENTA + AMBER-GOLD ACCENTS to identify Agatha as the spiritual-maternal anchor of the clan.

[STYLE / RENDER]
Stylized 3D animation render, premium mobile-game cinematic / animated key art quality, semi-realistic PBR materials, slight film grain, square 1024x1024 character sheet hero portrait. NOT 2D, NOT painterly, NOT illustration, NOT anime, NOT photorealistic, NOT cel-shaded flat, NOT Pixar/Disney generic family-feature look.

[REFERENCE INTEGRATION]
Image 1 (agatha-ref-1) is the canonical identity lock — match her silhouette, white dome face, GREEN-LIME skin (NOT turquoise — Agatha is the only green Pax), auburn dread-crown, leather headband, golden mouth markings, magenta diamond earrings, and magenta crystal pendant exactly, but render her with smoother surfaces, more elegant feminine proportions, better dread hair geometry, refined PBR shading. Image 2 (jiggy.png) anchors Pax species anatomy and proportional language. Image 3 (portada.png) anchors palette and render base. Improve significantly on the original reference's stiffness while preserving identity.

[NEGATIVE]
Do not include: turquoise skin (Agatha is GREEN-LIME, this is unique to her), human anatomy with exposed two human eyes, a single visible cyclops eyeball replacing the white dome, generic indigenous/ethnographic costumes, 2D hand-drawn aesthetic, painterly Studio Ghibli style, photorealistic skin, five-fingered hands, anime stylization, cel-shaded flat coloring, Pixar/Disney generic look, no second eye anywhere, no glamour beauty-shot lighting, no fantasy priestess clichés, no robe-and-staff trope, no halo, no wings, accessories not present in the reference.
""".strip()

result = edit_image(
    prompt=PROMPT,
    input_image_paths=[
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\refs\agatha-ref-1.jpeg",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\jiggy.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada.png",
    ],
    output_path=r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\agatha.png",
    size="1024x1024",
    quality="medium",
)
print(f"OK agatha -> {result}")
