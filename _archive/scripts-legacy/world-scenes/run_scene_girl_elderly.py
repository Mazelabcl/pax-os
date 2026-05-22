"""
Genera scene-girl-elderly-crossing.png — nina ayudando a anciano a cruzar.
Composicion desde atras, calle latinoamericana cotidiana.

Mundo de superficie: NO IDENTITY LOCK no-humano.
SI brand DNA: render 3D PBR neon-magic, paleta canonica.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openai_images import edit_image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROMPT = """[SUBJECT]
Rear-view shot: from behind we see a young girl (around 10-12 years old, school backpack on her back, casual clothes, dark hair) walking across a pedestrian zebra crossing, her arm extended sideways gently holding the elbow of an elderly man (around 75, slightly hunched, simple shirt, walking cane in his other hand). Their faces are NOT visible — only their backs and the side of the girl's profile partially. The gesture is small, unposed, real. They walk together at the elder's pace.

[SETTING]
A typical Latin American everyday street: low concrete buildings on both sides, a few light posts, a couple of parked or stopped cars patiently waiting at the crossing. Power cables crossing above. A small kiosk or fruit stand barely visible at the far right background. The vibe is lived-in, working-class, ordinary — not touristy, not glamorized.

[COMPOSITION]
Rule of thirds: the girl and elder occupy the left-vertical-third intersection, the open street and waiting cars stretch to the right. Camera is at adult shoulder height, slightly elevated, looking forward past them as they cross. Their backs frame the lower-left foreground. The zebra crossing white stripes lead the eye diagonally into the depth of the street.

[LIGHT + PALETTE]
Early evening golden-hour light. Warm amber sun raking from the right side, casting long elongated shadows of the two figures on the asphalt. The street surfaces glow with warm honey tones, the building walls catch reflected amber. Cooler basalt-dark shadows in the corners and under the cars. CRITICAL DETAIL — HANDLE WITH EXTREME RESTRAINT: beneath the zebra crossing, almost as if dreamt rather than seen, an extremely faint jade-green luminous root-like filament pulses underneath the asphalt, following their path as they walk. This must read as "is there something glowing underneath?" — barely perceptible, like a thin vein of light suggested through cracks in the asphalt, not an obvious magical effect. If the model cannot keep it subtle, omit entirely. Canonical Pax palette: warm-amber dominant, basalt-dark shadows, the barest jade hint, no neon-magenta.

[STYLE / RENDER]
The render is stylized 3D animation with semi-realistic PBR shading and neon-magic lighting sensibility, applied with cinematic restraint. NOT 2D, NOT painterly, NOT anime, NOT flat photorealistic. Think Pixar Coco's street scenes, or Arcane's quieter moments: real materials, tactile textures, cinematic lensing, warm dignified palette. Tender everyday — never melodramatic, never sentimentalized, never staged.

[REFERENCE INTEGRATION]
Image 1 (portada) establishes the canonical Pax palette and the 3D PBR neon-magic render base — match its material treatment, its warmth, its level of stylization. Image 2 (concept-metro-line5-evening) provides urban Latin-American texture reference — the way evening light falls on working-class architecture, the colors of streets at dusk, the dignity of ordinary places. Apply both to a tender ordinary act of solidarity.

[NEGATIVE PROMPT]
Do not include: any visible faces, any front-facing portraits, any text or readable signage, any branded logos, any cinematic dramatic posing, any tear-jerking sentimental staging, any 2D illustration aesthetic, any anime stylization, any cartoon flatness, any neon-magenta, any green glow that is loud or obvious. The jade sub-resonance must be almost imperceptible — if in doubt, less is more. Do not stylize the elder as fragile-pitiful; he is dignified.
"""

REFS = [
    os.path.join(REPO, "public", "images", "portadas", "portada.png"),
    os.path.join(REPO, "public", "images", "concepts", "concept-metro-line5-evening.png"),
]

OUT = os.path.join(REPO, "content", "test-images", "scene-girl-elderly-crossing.png")

if __name__ == "__main__":
    print("Generando scene-girl-elderly-crossing.png ...")
    edit_image(
        prompt=PROMPT,
        input_image_paths=REFS,
        output_path=OUT,
        size="1536x1024",
        quality="medium",
    )
    print(f"OK: {OUT}")
