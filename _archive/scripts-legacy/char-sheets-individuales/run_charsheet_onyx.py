"""Char sheet de Onyx — el atleta-guerrero del clan Pax."""

from openai_images import edit_image

PROMPT = """
[IDENTITY LOCK]
The character is Onyx, an athletic Pax warrior — a non-human cave-dwelling humanoid species. Onyx visually MUST match Images 1, 2, 3 (his canonical references): turquoise-teal smooth skin (#21D8B6 base, #2EE0C8 highlights), elongated pointed elastic ears that flare outward, FOUR fingers per hand (not five), 3.5-head proportions, athletic lean-muscled build (not bulky, lithe-strong like a runner-warrior). CRITICAL FACIAL ANATOMY of Onyx: the upper half of his face is a smooth, white, matte, dome-shaped mask-like surface covering his forehead, brow and eye area entirely; his eyes read as a single softly-curved closed line drawn across that white dome — calm, focused, ready. Below the white dome the lower face shows turquoise skin with a small firm half-smile. Geometric WHITE tribal markings (sharp angular lines, dashes, dots) painted across his cheekbones, brow ridge, shoulders, forearms and torso — these are warrior-glyph tattoos. A small cyan-pale crystal hanging as a pendant from one ear. A few small brown feathers dangling from the other ear-tip. Onyx is the same species and design language as Image 4 (jiggy.png) — same Pax DNA, same proportions — but with Onyx's distinctive warrior tribal-white markings and athletic build.

[SUBJECT]
Onyx in a 3/4 medium hero portrait, head and torso visible. He is the athletic, powerful, energetic warrior of the clan — the physical engine, fiercely loyal. Pose conveys quiet confident strength: front-facing 3/4, upright confident posture, arms either crossed across the chest OR one arm relaxed at side and the other hand resting on hip, shoulders broad and squared, weight balanced, feet planted (though not visible in frame). Vibe: "always ready to run, always ready to defend." A focused, contained half-smile — short, firm, sure. Eye area calm and locked-in.

[COMPOSITION]
3/4 medium hero portrait, centered subject framed slightly off-thirds, eye level, head and torso visible to mid-belly. Background: smooth gradient mixing deep basalt purple (#1E1E2E), deep jade green (#0D7A5F), and a touch of cool teal, with subtle floating Pax glyphs and faint volumetric dust. Background dark, gravitas-heavy, non-distracting.

[LIGHT + PALETTE]
Stylized 3D PBR semi-realistic shading with subsurface scattering on the turquoise skin and on the white dome face. Neon-magic cinematic lighting: cool jade rim from camera-left-back, deep magenta-violet ambient from below, cool turquoise key from above-front. Bloom on the cyan ear-crystal. Slight volumetric haze. Palette weighted toward DEEP BASALT + DEEP JADE to identify Onyx as the gravitas-physical member of the clan, with magenta only as background ambient accent.

[STYLE / RENDER]
Stylized 3D animation render, premium mobile-game cinematic / animated key art quality, semi-realistic PBR materials, slight film grain, square 1024x1024 character sheet hero portrait. NOT 2D, NOT painterly, NOT illustration, NOT anime, NOT photorealistic, NOT cel-shaded flat, NOT Pixar/Disney generic family-feature look.

[REFERENCE INTEGRATION]
Image 1 (onyx-ref-1) is the primary identity lock — match the floating yoga-warrior pose's overall look BUT in the new portrait pose described above. Image 2 (onyx-ref-2) shows Onyx's face/markings detail. Image 3 (onyx-ref-3) shows him in dynamic body posture for proportion reference. Match the white dome face, turquoise skin, white tribal markings, ear-pendants, and lean athletic build exactly, but render him with smoother surfaces, more elegant warrior proportions, refined PBR shading, sharper-but-elegant marking lines. Image 4 (jiggy.png) anchors Pax species anatomy. Image 5 (portada.png) anchors palette and render base.

[NEGATIVE]
Do not include: human anatomy with exposed two human eyes, a single visible cyclops eyeball replacing the white dome, generic tribal-warrior cliché armor, 2D hand-drawn aesthetic, painterly Studio Ghibli style, photorealistic skin, five-fingered hands, anime stylization, cel-shaded flat coloring, Pixar/Disney generic look, fantasy battle weapons (no swords, axes, spears, shields), no helmet, no goggles, no second eye anywhere, no body-builder bulk muscle, no excessive jewelry beyond the single ear-crystal and ear-feathers.
""".strip()

result = edit_image(
    prompt=PROMPT,
    input_image_paths=[
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\refs\onyx-ref-1.jpeg",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\refs\onyx-ref-2.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\refs\onyx-ref-3.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\jiggy.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada.png",
    ],
    output_path=r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\onyx.png",
    size="1024x1024",
    quality="medium",
)
print(f"OK onyx -> {result}")
