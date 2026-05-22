"""
World-building image #12 — Aldea pascuense Pax: moai-resonadores subterraneos al atardecer.
Sin personajes en frame (o silueta lejana sin foco).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from openai_images import edit_image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REFS = [
    os.path.join(REPO, "public", "images", "portadas", "portada2.png"),
    os.path.join(REPO, "public", "images", "concepts", "concept-cave-wide-dark.png"),
]

OUTPUT = os.path.join(REPO, "content", "test-images", "world-pax-rapanui-village.png")

PROMPT = """A wide cinematic establishing shot of a subterranean ceremonial Pax village —
NO characters in the foreground, NO close-up figures. If any figures are visible at all,
they must be one or two distant silhouettes, very far in the background, blurred, out of focus.
This is pure world-building: locations and architecture only.

SUBJECT BLOCK:
A massive natural cavern with a vaulted rocky ceiling, repurposed by the Pax civilization as a
sacred ceremonial village. In the center and along the perimeter stand 5 to 7 monolithic
moai-resonators carved from black basaltic stone — silent stone heads, Easter Island Rapa Nui
silhouette but reinterpreted for the Pax universe. Some are enormous (4–6 meters tall, dwarfing
the cave floor); others are human-sized. Their surfaces bear engraved geometric Rapa Nui glyphs
fused with Pax visual vocabulary: spiraling jade-green lines that softly pulse with inner light,
small jade and magenta crystals embedded in the empty hollow eyes of each moai (not glowing
harshly — a deep luminous resonance, like cores).

Each moai-resonator is connected to the others by thin filaments of jade light running along
the cave floor, a vast organic network like a root system of pure light snaking between the
stones. Small ceremonial fire pits with warm amber flames burn between the moai, casting
diegetic warm light that contrasts beautifully with the cold jade glow of the crystals and
filaments. Subtle low-lying mist drifts near the floor; floating dust particles catch the
crystal light, illuminated like underwater plankton.

The cave ceiling has natural openings — vertical apertures in the vault — through which
shafts of cenital light fall into the chamber. Because it is sunset on the surface, that
falling light is amber-reddish, warm, dramatic. The Pax call this phenomenon "interior sunset."
The shafts cut through the dust, creating volumetric god-rays that intersect with the cold
jade network on the floor.

COMPOSITION BLOCK:
Wide cinematic establishing shot, ultra-wide angle but not distorted, deep depth of field.
Camera placed slightly low to convey the sense of scale — the giant moai loom upward.
Composition built on layers: foreground filaments and a small fire pit, midground 2–3 moai
catching light differently, background more moai dissolving into mist with the largest moai
silhouetted against a far amber light shaft. Strong sense of wonder, sense of scale, sense of
ancient sacred space.

LIGHT + PALETTE BLOCK:
Triple light source. (1) Cold jade-green emission from the embedded eye crystals and the floor
filaments. (2) Warm amber diegetic firelight from the fire pits. (3) Cenital amber-reddish
sunset shafts piercing the ceiling. The contrast between cold jade and warm amber is the
emotional heart of the image. Canonical Pax palette enforced: jade-green (#1FA882), warm-amber
(#E8A04A), basalt-dark (#1A1612), neon-magenta accents (#D8408E) only on a few crystal hot
points. Volumetric atmosphere, soft mist, light pollution from particles.

STYLE / RENDER BLOCK:
The render is stylized 3D animation with semi-realistic PBR shading and neon-magic lighting.
Stone has believable basaltic micro-detail; crystals have realistic refraction and subsurface
scattering; mist and god-rays are physically plausible. NOT 2D, NOT painterly, NOT illustration,
NOT anime, NOT photorealistic. Cinematic 3D feature-animation quality, Unreal-Engine-grade
lighting on stylized geometry.

REFERENCE INTEGRATION:
Image 1 (portada2.png) provides composition and palette anchor — match its sense of grouped
ceremonial Pax space and its emotional warm/cold lighting balance. Image 2 (concept-cave-wide-dark.png)
establishes cavern geometry, scale and atmospheric darkness — match the same kind of vaulted
volumetric cavern. Apply the canonical Pax palette: jade-green, warm-amber, basalt-dark, neon-magenta accents.

NEGATIVE PROMPT:
Do NOT include any Pax characters in the foreground or midground. Do not include any human
figures. No close-up creatures. No anime aesthetic. No 2D hand-drawn look. No painterly
brushstrokes. No photorealistic faces. No generic Easter Island tourism look — these are
Pax-universe moai-resonators, sacred and luminous, not stone tourist statues. No ethnographic
costumes. No surface-world architecture. No modern objects. Avoid fantasy-art tropes
(no overly busy ornament, no dragons, no swords).
"""


def main():
    print("[12] Generando world-pax-rapanui-village.png …")
    out = edit_image(
        prompt=PROMPT,
        input_image_paths=REFS,
        output_path=OUTPUT,
        size="1536x1024",
        quality="medium",
    )
    print(f"[12] OK -> {out}")


if __name__ == "__main__":
    main()
