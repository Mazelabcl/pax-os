"""
Genera asset-crystal-charging-macro.png — macro extreme close-up de
cristal jade cargandose desde abajo. Vertical 1024x1536.

Sin personajes Pax visibles: aplica brand DNA (render base + paleta) sin
IDENTITY LOCK de personaje.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openai_images import edit_image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROMPT = """[SUBJECT]
Extreme macro close-up of a single subterranean jade-green crystal, occupying roughly 90% of the vertical frame. The crystal is NOT a solid rock — it is a geode-like structure with intricate fibrous internal filaments visible through its translucent shell, like luminous veins or roots inside glass. Texture is tactile: faceted outer planes, micro-cracks, ancient mineral patina, with the inner fibers clearly visible.

[KEY MOMENT — CRITICAL]
The crystal is captured at the precise instant of charging. A warm amber-honey light is rising up through the inner filaments from the bottom, like sap or molten gold ascending root by root. The lower third of the crystal is dim, opaque, dormant — basalt-dark, almost cold. The upper two-thirds are increasingly alive: amber transitioning into bright pulsing jade-green at the top. The contrast between the dormant base and the awakening top must be VERY CLEAR — the metaphor of "charging from below" must read instantly. The transition zone where amber becomes jade is the focal point of the frame.

[ATMOSPHERE]
Tiny luminous dust particles float in the immediate space around the crystal, lit by its inner glow — fine bokeh, depth of field very shallow. The background is a basalt-dark cavern, completely out of focus, suggested rather than shown — only hints of dark stone walls, faint distant glints of other crystals far away.

[COMPOSITION]
Vertical aspect ratio. Crystal centered with a slight diagonal tilt for dynamic energy (axis tilted ~10-15 degrees). Rule of thirds applied: the amber-to-jade transition zone sits at the upper-third intersection — that is the gravity center of the image. Macro lens feel — extreme magnification, micro-detail visible.

[LIGHT + PALETTE]
Light is fully internal-diegetic: it comes from inside the crystal itself. No external light source. Warm amber rising from below, transitioning into bright jade-green at the top. Basalt-dark surrounds. Faintest neon-magenta accents possible in the background bokeh dust as far-away crystal glints. Canonical Pax palette in full: jade-green, warm-amber, basalt-dark, with subtle neon-magenta accents.

[MOOD]
Meditative, momentum, awe. The viewer feels they are witnessing something private and ancient quietly waking up — the visible metaphor of charging.

[STYLE / RENDER]
The render is stylized 3D animation with semi-realistic PBR shading and neon-magic lighting. Subsurface scattering on the crystal is essential — light must travel through translucent material believably. NOT 2D, NOT painterly, NOT anime, NOT flat photorealistic crystal-stock-photo. Think Pixar/Arcane macro VFX shot crossed with the textural intimacy of nature documentary macro photography.

[REFERENCE INTEGRATION]
Image 1 (concept-cave-stalagmites-reawakening) establishes the canonical Pax crystal language — match the type of crystal, the type of cave, the type of glow. Image 2 (portada) confirms the canonical palette and the 3D PBR neon-magic render base — match its material treatment.

[NEGATIVE PROMPT]
Do not include: any people, any characters, any hands, any tools, any text, any UI overlay, any obvious VFX swirls or rays of light, any flat 2D illustration, any anime crystal stylization, any photorealistic stock-photo flatness, any cartoon outlines. The dim-bottom / bright-top contrast must be unmistakable. The crystal must NOT look uniformly lit. The crystal must NOT look like a generic fantasy gem — it must read as part of the Pax universe.
"""

REFS = [
    os.path.join(REPO, "public", "images", "concepts", "concept-cave-stalagmites-reawakening.png"),
    os.path.join(REPO, "public", "images", "portadas", "portada.png"),
]

OUT = os.path.join(REPO, "content", "test-images", "asset-crystal-charging-macro.png")

if __name__ == "__main__":
    print("Generando asset-crystal-charging-macro.png ...")
    edit_image(
        prompt=PROMPT,
        input_image_paths=REFS,
        output_path=OUT,
        size="1024x1536",
        quality="medium",
    )
    print(f"OK: {OUT}")
