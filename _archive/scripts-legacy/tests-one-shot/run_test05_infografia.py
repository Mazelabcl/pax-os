"""
Test 05 — Infografía vertical estilo cross-section / rayos X mostrando
el ciclo virtuoso de los cristales Pax (3 niveles conectados).
"""

import os
import sys

# Asegura que el repo raiz este en sys.path para 'from scripts.openai_images...'
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from scripts.openai_images import edit_image  # noqa: E402


PROMPT = """[IDENTITY LOCK — softened for silhouette]

The single Pax character at the bottom level of this scene is a member of the Pax — a subterranean civilization, NOT human, NOT Andean indigenous, NOT generic fantasy creature. Even rendered as a semi-transparent silhouette with internal light passing through, the Pax must visually match the cast vocabulary in the reference images: ONE central eye (NOT two), turquoise/teal skin tone visible through the translucency, elongated pointed elastic ears, FOUR fingers per hand (NOT five), 3.5-head proportions, slim build. The silhouette retains those anatomical reads even at low opacity — the eye is one luminous central point, the hand silhouette clearly shows four fingers extended toward the crystal. This Pax is kin/peer of Image 2 cast, not a different species.

[SUBJECT — vertical cinematic anatomical cross-section infographic, three connected horizontal bands]

A vertical cinematic cross-section diagram of the Pax virtuous-cycle, structured as three stacked horizontal bands occupying roughly equal thirds of the frame, all connected by visible energy flow lines. This is a single continuous 3D rendered scene, NOT a collage of separate panels — the bands transition into each other through visible strata of rock, sediment and cavern ceiling.

TOP BAND (upper third): the surface. A stylized 3D city street at twilight seen in cross-section, showing pedestrians performing small acts of solidarity — one person helping another lift a heavy box, a person smiling and offering something to a child, another picking up litter from the ground. Each act of kindness emits soft warm-amber filaments of light, like luminous threads of energy, drifting downward and seeping into the pavement and soil below. The humans are stylized 3D semi-translucent silhouettes — anatomy reads as fully human (two eyes, five fingers), light passing through them with internal glow.

MIDDLE BAND (center third): the planetary crust. The amber filaments descend through layered rock strata, sedimentary lines, mineral veins. They converge into a large central subterranean jade-green crystal cluster, anchored in basalt. The crystal shows a clear charging gradient — its lower portion is dim and dormant, its upper portion glows with progressively intensifying jade-green inner light. Around the crystal, very fine cyan and white blueprint-style guide lines indicate flow direction (arrows implied through tapered filaments, NOT written words, NOT text, NOT labels), reading as a technical infographic without any letters or numbers.

BOTTOM BAND (lower third): the deep Pax cavern. A single Pax — rendered as a semi-transparent silhouette in profile, kneeling or standing close to the crystal, one four-fingered hand extended toward it in a gesture of distillation. The silhouette is glassy turquoise-teal, the central single eye visible as a bright point of inner light, pointed elastic ears clearly silhouetted. Out of the crystal's top facet, a beam of vivid neon-magenta light shoots upward, piercing through the cavern ceiling and the rock strata above, finally reappearing at the surface (visible as the same beam touching the top band) where it manifests as a concrete real-world event: a young tree sprouting from cracked pavement, a small spring of water surfacing from a previously dry well, and a human hand being helped up. These three surface manifestations are placed along the trajectory of the magenta beam in the top band, completing the visual loop.

[COMPOSITION]

Vertical 1024x1536 portrait, three horizontal bands roughly 33% each, separated visually by rock strata transitions but connected by the descending amber filaments and the ascending magenta beam — both must be continuous from band to band, clearly visible crossing the boundaries. Symmetrical-ish vertical axis with the central crystal as the visual pivot in the middle band. Cinematic depth in each band, NOT flat panels — atmospheric perspective, parallax between foreground silhouettes and background environments. Style references: cinematic still from a Pixar internal pipeline diagram, premium Wired magazine 3D cross-section feature, stylized PBR architectural blueprint rendered in CG.

[LIGHT + PALETTE]

Canonical Pax palette: jade-green (the crystal core), warm-amber (descending solidarity filaments and surface lamps in top band), basalt-dark (deep blue to near-black background gradient and rock strata), neon-magenta (the ascending beam and surface manifestation accents). Background gradient runs from deep-blue at the top edge to basalt-dark at the bottom edge. Fine cyan/white blueprint guide lines as graphic overlays connecting the bands — these read as schematic flow indicators, very thin, low-opacity, cinematic NOT clinical. Volumetric light: amber haze descending in the upper transition, magenta haze rising in the lower transition. All silhouettes (humans top, Pax bottom) are translucent with rim lighting and internal glow.

[STYLE / RENDER — non-negotiable]

The render is stylized 3D animation with semi-realistic PBR shading and neon-magic lighting. Volumetric god rays, subsurface scattering on the translucent silhouettes, soft physically-based materials on rock and crystal, cinematic depth of field. NOT 2D, NOT painterly, NOT flat illustration, NOT vector infographic, NOT PowerPoint diagram, NOT anime, NOT photorealistic. Think Pixar production-quality cross-section concept frame with infographic overlays, NOT a graphic-design poster.

[REFERENCE INTEGRATION]

Image 1 (cave-stalagmites-reawakening) provides the jade crystal material, glow behavior, and cavern stalagmite vocabulary for the bottom band's environment and the central crystal in the middle band. Image 2 (portada) sets the canonical Pax palette baseline and establishes anatomical identity language for the Pax silhouette at the bottom band — match its proportional and facial vocabulary. Image 3 (cave-wide-dark) provides the deep cavern atmosphere, basalt rock strata language, and atmospheric depth for the middle and bottom bands. Apply the canonical Pax palette: jade-green, warm-amber, basalt-dark, neon-magenta accents.

[NEGATIVE PROMPT]

Do NOT include: any text, letters, numbers, labels, captions, callouts, arrows with words, legends, titles, watermarks, or written language of any kind anywhere in the image (zero words, zero glyphs). Do NOT make this a 2D flat illustration, a vector infographic, a PowerPoint slide, a textbook diagram, or a clinical schematic. Do NOT use painterly Studio Ghibli style, anime stylization, or photorealistic rendering. The Pax silhouette must NOT have two eyes (it has ONE central eye), must NOT have five fingers (it has FOUR), must NOT look like a human ethnographic figure. Do NOT separate the three bands as discrete framed panels — they must read as one continuous cross-section. Do NOT lose the continuity of the amber descending filaments or the magenta ascending beam — both must clearly connect across all three bands."""


OUTPUT_PATH = (
    r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\content\test-images"
    r"\test-05-infografia-ciclo.png"
)

INPUT_IMAGES = [
    r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-cave-stalagmites-reawakening.png",
    r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada.png",
    r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-cave-wide-dark.png",
]


if __name__ == "__main__":
    print("Generando test-05-infografia-ciclo.png ...")
    print(f"Output: {OUTPUT_PATH}")
    print(f"Refs: {len(INPUT_IMAGES)} imagenes")
    out = edit_image(
        prompt=PROMPT,
        input_image_paths=INPUT_IMAGES,
        output_path=OUTPUT_PATH,
        size="1024x1536",
        quality="medium",
    )
    print(f"Imagen creada: {out}")
