"""
Pre-genera las 4 refs faltantes para cap 1 Seedance.

Refs:
1. concept-cap1-tunel-vertical-pax — tunel vertical pax con manhole arriba
2. concept-cap1-camara-central-cristales-mapa — cámara central con mapa holografico
3. concept-cap1-cristal-pale-cyan-vacio — cristal vacio pale-cyan que entrega Wiz
4. concept-cap1-chispa-ancla-dorada — chispa-ancla pale-dusty-gold de Wiz

Quality: low (draft rápido — aldot quiere probar HOY).
Marca canon: pending_aldot_approval — flagged en filename con prefijo concept-cap1-*.
"""

import os
import sys
import asyncio

# Asegurar import del modulo openai_images
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from openai_images import generate_batch_async

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONCEPTS_DIR = os.path.join(REPO_ROOT, "public", "images", "concepts")
PORTADA = os.path.join(REPO_ROOT, "public", "images", "portadas", "portada.png")
CAVE_WIDE = os.path.join(CONCEPTS_DIR, "concept-cave-wide-dark.png")
CAVE_STAL = os.path.join(CONCEPTS_DIR, "concept-cave-stalagmites-reawakening.png")
BILBAO = os.path.join(CONCEPTS_DIR, "concept-bilbao-grate-night.png")

# Brand DNA (paleta canonica + render base) - bloque comun
BRAND_DNA_BLOCK = (
    "The render is stylized 3D animation with semi-realistic PBR shading and "
    "neon-magic lighting. NOT 2D, NOT painterly, NOT illustration, NOT anime, "
    "NOT photorealistic. Apply the canonical Pax palette: jade-green, warm-amber, "
    "basalt-dark, neon-magenta accents. Same universe as Image 1 (palette and "
    "render reference). Subtle volumetric haze, bloom on light sources, "
    "subsurface glow on crystals."
)

NEGATIVE_BLOCK = (
    "Do not include: text overlays, captions, logos, signage, characters, "
    "people, faces, modern technology like smartphones, photorealistic skin, "
    "2D hand-drawn aesthetic, painterly Studio Ghibli style."
)

JOBS = [
    {
        "prompt": (
            "Concept art of a vertical Pax tunnel: a roughly cylindrical "
            "underground rocky shaft going UP, basalt-dark walls scattered "
            "with small magenta glow-crystals embedded in the rock. At the "
            "very top of the frame, a distant disc of warm sodium-orange "
            "light filtering through a circular street manhole grate from a "
            "Latin American city above. Cool magenta-jade caverness below "
            "transitioning to warm orange above — the chromatic frontier "
            "between Pax world and surface world. Low angle, dramatic, "
            "wide 24mm lens feel. Empty composition (no characters). "
            f"{BRAND_DNA_BLOCK} {NEGATIVE_BLOCK}"
        ),
        "input_image_paths": [CAVE_WIDE, BILBAO],
        "output_path": os.path.join(
            CONCEPTS_DIR, "concept-cap1-tunel-vertical-pax.png"
        ),
        "size": "1024x1536",  # vertical to emphasize ascent
        "quality": "low",
    },
    {
        "prompt": (
            "Concept art of the central crystal chamber of the Pax clan: a "
            "vast subterranean cavern with dozens of magenta and cyan "
            "crystal stalagmites jutting from the floor. A small rocky dais "
            "in the foreground (where Wiz stands during clan councils, but "
            "no characters in this concept). Floating above the dais, a "
            "softly glowing holographic constellation map made of luminous "
            "magenta and dim points connected by faint thread-lines — many "
            "points are dim, a few still bright. God-rays of cyan light "
            "filter from cracks in the cavern ceiling. Mid-wide establishing "
            "view. Composition empty of characters, room for a council to "
            "stand. "
            f"{BRAND_DNA_BLOCK} {NEGATIVE_BLOCK}"
        ),
        "input_image_paths": [CAVE_STAL, CAVE_WIDE],
        "output_path": os.path.join(
            CONCEPTS_DIR, "concept-cap1-camara-central-cristales-mapa.png"
        ),
        "size": "1536x1024",
        "quality": "low",
    },
    {
        "prompt": (
            "Insert macro shot — a small uncharged Pax crystal resting on a "
            "neutral dark basalt surface. The crystal is faceted, "
            "translucent, with a very pale cyan tint (almost colorless, "
            "dormant) — clearly DIFFERENT from the dominant magenta crystals "
            "of Image 1. Soft subsurface scattering, subtle inner haze, no "
            "glow, no pulse — this crystal is EMPTY, waiting to be charged. "
            "Shallow depth of field, macro 100mm feel, dramatic side light "
            "with faint magenta rim from off-frame ambient. Composition "
            "centered. "
            f"{BRAND_DNA_BLOCK} {NEGATIVE_BLOCK}"
        ),
        "input_image_paths": [CAVE_STAL, PORTADA],
        "output_path": os.path.join(
            CONCEPTS_DIR, "concept-cap1-cristal-pale-cyan-vacio.png"
        ),
        "size": "1024x1024",
        "quality": "low",
    },
    {
        "prompt": (
            "Insert macro shot — a tiny Pax spark-crystal cradled in shadow. "
            "The crystal is small, faceted, with a distinctive pale "
            "dusty-gold glow (#D9C28A) — warm amber tone, NOT magenta, NOT "
            "cyan. It pulses softly with inner amber light, looking "
            "ancient, almost weary, an heirloom-quality artifact. Subtle "
            "volumetric haze around it. Macro 100mm extreme close-up, very "
            "shallow depth of field, dark basalt-purple fabric of a velvet "
            "cloak fold visible behind it (suggesting it is hidden in a "
            "pocket). No characters, no hands, only the crystal and fabric. "
            f"{BRAND_DNA_BLOCK} {NEGATIVE_BLOCK}"
        ),
        "input_image_paths": [CAVE_STAL, PORTADA],
        "output_path": os.path.join(
            CONCEPTS_DIR, "concept-cap1-chispa-ancla-dorada.png"
        ),
        "size": "1024x1024",
        "quality": "low",
    },
]


async def main():
    print(f"Lanzando {len(JOBS)} pre-gens en paralelo...")
    results = await generate_batch_async(JOBS, max_concurrent=4)
    for job, res in zip(JOBS, results):
        out = job["output_path"]
        if isinstance(res, Exception):
            print(f"FAIL  {os.path.basename(out)}: {res}")
        else:
            size_kb = (
                os.path.getsize(out) / 1024 if os.path.exists(out) else 0
            )
            print(f"OK    {os.path.basename(out)} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    asyncio.run(main())
