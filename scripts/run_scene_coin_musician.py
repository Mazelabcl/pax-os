"""
Genera scene-coin-musician-pov.png — gesto cotidiano de solidaridad
(POV primera persona, mano humana soltando moneda en sombrero de musico).

Mundo de superficie: NO IDENTITY LOCK no-humano.
SI brand DNA: render 3D PBR neon-magic, paleta canonica.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openai_images import edit_image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROMPT = """[SUBJECT]
Extreme close-up first-person POV: a human hand entering the frame from the lower-left, fingers extended in the exact moment of releasing a small gold-copper coin. The coin is captured mid-air, just released, slightly tilted, catching the warm light. The hand is adult, casual, ordinary — no jewelry, no ostentation, just an everyday gesture. Below, on the urban sidewalk, sits a worn dark-felt hat upturned with several coins already inside (mixed copper and silver tones). Beside the hat, partially in frame and out of focus, the curved wooden body of a guitar case (or violin case) lies open. The ground is real urban pavement: cracked concrete, scattered dry leaves, faint dust. Above and behind, deeply out of focus, the legs and feet of the street musician stand in a playing posture — only knees-down visible, no face. The whole frame breathes intimacy, not spectacle.

[COMPOSITION]
First-person POV, low camera angle, close-up macro on the moment of release. Rule of thirds: the falling coin sits at the upper-right intersection, the hat at the lower-third. Strong foreground / midground / background depth. Shallow depth of field — coin and hat in focus, musician legs blurred.

[LIGHT + PALETTE]
Late golden hour light, warm low-angle sun raking across the sidewalk from screen-right, casting long soft shadows. Warm amber-honey tones dominate the surface light. Subtle basalt-dark in the deeper sidewalk shadows. CRITICAL DETAIL — HANDLE WITH RESTRAINT: at the precise moment the coin would land in the hat, an almost imperceptible jade-green sub-resonance pulses faintly from where the coin will fall, radiating softly into the sidewalk fibers. This jade glow must be EXTREMELY SUBTLE — barely visible, like a faint reflection in a dust particle, not a magical aura. It should read as "did I just see something?" not as obvious VFX. If it cannot be made subtle, omit it entirely. The canonical Pax palette breathes through: warm-amber dominant, basalt-dark shadows, the faintest jade-green hint, no neon-magenta in this scene.

[STYLE / RENDER]
The render is stylized 3D animation with semi-realistic PBR shading and neon-magic lighting sensibility — but applied with restraint to a real human-world scene. NOT 2D, NOT painterly, NOT anime, NOT flat photorealistic stock photography. Think Pixar Soul or Arcane in cinematic close-up: real materials, tactile textures, cinematic lensing, warm controlled palette.

[REFERENCE INTEGRATION]
Image 1 (portada) establishes the canonical Pax palette and the 3D PBR neon-magic render base — match its material treatment, its warmth, its level of stylization. Image 2 (concept-bilbao-grate-night) provides urban texture reference — the cracked concrete, the worn surfaces, the way light falls on real city ground. Apply both to a daytime golden-hour scene of human surface life.

[NEGATIVE PROMPT]
Do not include: any face, any musician's face, any human eyes, any second hand, any text or signage, any jewelry, any modern smartphone, any dramatic magical glow, any obvious VFX swirls, any 2D illustration aesthetic, any flat photo-stock look, any anime stylization, any cartoon flatness, any neon-magenta, any green that is loud or obvious. The jade sub-resonance must be almost imperceptible — if in doubt, less is more.
"""

REFS = [
    os.path.join(REPO, "public", "images", "portadas", "portada.png"),
    os.path.join(REPO, "public", "images", "concepts", "concept-bilbao-grate-night.png"),
]

OUT = os.path.join(REPO, "content", "test-images", "scene-coin-musician-pov.png")

if __name__ == "__main__":
    print("Generando scene-coin-musician-pov.png ...")
    edit_image(
        prompt=PROMPT,
        input_image_paths=REFS,
        output_path=OUT,
        size="1536x1024",
        quality="medium",
    )
    print(f"OK: {OUT}")
