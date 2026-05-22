"""
World-building image #13 — Highway runner Pax: tunel cilindrico subterraneo.
Sin personajes en frame.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from openai_images import edit_image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REFS = [
    os.path.join(REPO, "public", "images", "concepts", "concept-cave-wide-dark.png"),
    os.path.join(REPO, "public", "images", "portadas", "portada.png"),
]

OUTPUT = os.path.join(REPO, "content", "test-images", "world-pax-highway-tunnel.png")

PROMPT = """A cinematic establishing shot of a Pax highway runner tunnel — a perfectly cylindrical
underground passage carved by the Pax civilization, NOT a raw natural cave. NO characters anywhere
in frame. Pure world-building location shot.

SUBJECT BLOCK:
A perfectly circular cylindrical tunnel, clearly engineered and tooled, carved into deep
black basaltic rock. The walls of the cylinder show subtle tool marks that prove construction —
evenly faceted basalt panels, geometric precision — this is NOT a raw natural cave, this is
Pax infrastructure. Every 3 to 4 meters along the cylinder walls, small embedded crystals act
as track lights: alternating jade-green crystals and neon-magenta crystals, regularly spaced,
glowing softly inward toward the tunnel core like runway lights. Their light catches the
faceted basalt and reflects in long subtle gradients along the cylinder.

The tunnel floor is flat and polished, basalt black, smooth like obsidian. Down the dead center
of the floor runs a single brilliant jade-green light strip — a continuous luminous line,
like a glowing track or a magnetic-rail of pure light, extending all the way to the vanishing
point. On the curved walls, etched at low contrast and catching the ambient light, are subtle
Pax glyphs — spirals, radial line motifs, geometric runes — as ambient detail, not foreground
focus.

At the far end of the tunnel, perfectly centered on the vanishing point, a brilliant magenta
light source glows — bright but not blown out — indicating the next node, the next Pax nation,
the next stop on the network. It looks like a destination, a beacon.

A subtle static motion-blur haze hangs in the air at mid-tunnel — not animated streaks, just a
faint atmospheric blur, as if a Pax runner just sprinted through and the air still carries a
trace of their passage. Very subtle particle dust suspended in the lights.

COMPOSITION BLOCK:
Vanishing-point composition, dead-center symmetrical. Camera positioned slightly low (subtle
low angle) to exaggerate the cylindrical perspective and convey speed and scale. Strong forced
perspective — the embedded crystals on the walls form converging lines that all meet at the
distant magenta beacon. One-point perspective, tunnel infinity shot. Frame uses the curve of
the cylinder symmetrically (left-right mirror). Sense of speed implied by composition only,
not by motion lines.

LIGHT + PALETTE BLOCK:
Two dominant light sources: (1) the alternating jade-green and neon-magenta crystal track
lights on the walls, providing rhythmic ambient illumination; (2) the central jade floor strip
as primary light source warming the tunnel floor and bouncing off the basalt walls. Far
background magenta beacon adds depth and color contrast at the vanishing point. Cool dark
atmosphere overall, with vivid neon-magic accents. Canonical Pax palette enforced: jade-green
(#1FA882) dominant, neon-magenta (#D8408E) secondary, basalt-dark (#1A1612) for walls and
floor, warm-amber accents minimal or absent. Subtle volumetric lighting, slight haze for depth.

STYLE / RENDER BLOCK:
The render is stylized 3D animation with semi-realistic PBR shading and neon-magic lighting.
Believable basalt material with PBR specular and slight micro-roughness; crystal materials with
realistic emission, subsurface scattering, and refraction; floor light strip with believable
emissive falloff; volumetric haze physically plausible. NOT 2D, NOT painterly, NOT illustration,
NOT anime, NOT photorealistic. Feature-animation 3D rendering, sci-fi-meets-mystic look,
Unreal-Engine-grade lighting on stylized geometry.

REFERENCE INTEGRATION:
Image 1 (concept-cave-wide-dark.png) anchors the basalt material and dark cavernous palette —
match the same stone treatment but applied to a constructed cylindrical tunnel rather than a
natural cave. Image 2 (portada.png) anchors the canonical Pax palette and 3D PBR neon-magic
render style — match the same color treatment of jade-green and magenta accents. Apply the
canonical Pax palette: jade-green, basalt-dark, neon-magenta. Warm-amber should be minimal
or absent in this shot.

NEGATIVE PROMPT:
Do NOT include any characters of any kind — no Pax, no humans, no creatures, no silhouettes.
No motion lines, no speed-line illustration tropes. No anime aesthetic. No 2D hand-drawn look.
No painterly brushstrokes. No photorealistic surfaces. No raw natural cave look — this is
clearly engineered architecture. No hieroglyphs that look ethnographic or Mesoamerican; the
glyphs are subtle, geometric, Pax-original. No surface-world infrastructure (no train tracks,
no cars, no signage). No five-fingered handprints. No fantasy ornament. Keep the geometry
clean, the perspective razor-sharp, and the focus on the vanishing point beacon.
"""


def main():
    print("[13] Generando world-pax-highway-tunnel.png …")
    out = edit_image(
        prompt=PROMPT,
        input_image_paths=REFS,
        output_path=OUTPUT,
        size="1536x1024",
        quality="medium",
    )
    print(f"[13] OK -> {out}")


if __name__ == "__main__":
    main()
