"""
Genera 10 frames (start + end) para 5 escenas del video educativo paxeado.
Usa edit_image con refs de Wiz y Jiggy para mantener consistencia de personaje.

Uso:
    cd pax-os
    python gestos/_backlog/video-educativo/gen_frames.py
"""

import os
import sys
import asyncio

# Agregar raiz del repo al path para importar scripts/openai_images
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, REPO_ROOT)

from scripts.openai_images import edit_image_async, _load_env
from openai import AsyncOpenAI

_load_env()

FRAMES_DIR = os.path.join(os.path.dirname(__file__), "frames")
os.makedirs(FRAMES_DIR, exist_ok=True)

WIZ_REF = os.path.join(REPO_ROOT, "public", "images", "personajes", "wiz.png")
JIGGY_REF = os.path.join(REPO_ROOT, "public", "images", "personajes", "jiggy.png")

# Bloque de estilo Pax canonico (del style-guide.md)
STYLE = (
    "Style: stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, "
    "expressive cartoon proportions (Pax cyclops 3-3.5 heads), "
    "high-contrast cinematic neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8), "
    "saturated emissive crystals with bloom, painterly volumetric backgrounds with dense dust motes "
    "and god rays, slight film grain, color grading magenta/turquesa complementario, 16:9 landscape. "
    "Reads as premium mobile-game cinematic / animated key art. "
    "Negative: photorealistic, anime, 2D hand-drawn, cel-shaded flat, Pixar generic, game HUD, "
    "thriller vignette, glamour beauty shot."
)

# Descripcion de Wiz para prompts
WIZ_DESC = (
    "Image 1 is Wiz — an elderly turquoise-green cyclops sage with a single large central eye, "
    "long white flowing beard, wearing a deep purple cloak with faint turquoise runes, "
    "holding a dark wooden staff topped with a glowing magenta-violet crystal. "
    "Short stature (2.8-3 heads proportion), wise serene expression."
)

# Descripcion de Jiggy para prompts
JIGGY_DESC = (
    "Image 2 is Jiggy — a young magenta-toned cyclops with a single large curious eye, "
    "slightly off-balance posture (always about to trip or run), mischievous grin, "
    "wearing a leather harness. Playful anti-hero energy."
)


SCENES = [
    # Escena 1: La cueva silenciosa
    {
        "name": "e01-cueva-silenciosa",
        "refs": [WIZ_REF],
        "ref_desc": WIZ_DESC.replace("Image 1", "Image 1"),
        "start": (
            f"{STYLE}\n\n"
            "Scene: Deep underground cave in the Uray Pacha. {ref_desc}\n\n"
            "Render Image 1 (Wiz) sitting cross-legged on dark basalt rock in front of a large "
            "dim crystal formation. The crystal glows very faintly magenta, almost dormant. "
            "Dense volumetric dust motes float in god rays coming from cracks above. "
            "Deep purple-blue shadows dominate. Wiz's staff rests beside him. "
            "Serene, meditative atmosphere. Wide shot, rule of thirds, Wiz on left third."
        ),
        "end": (
            f"{STYLE}\n\n"
            "Scene: Same deep underground cave. {ref_desc}\n\n"
            "Same composition as before but now the crystal in front of Wiz pulses with soft "
            "magenta light, casting warm glow on Wiz's face. His single eye is open, looking "
            "directly at camera with knowing expression. Volumetric light rays are now tinted "
            "magenta-pink from the crystal's awakening glow. Slightly brighter atmosphere. "
            "Wide shot, Wiz on left third."
        ),
    },
    # Escena 2: Jiggy no puede enfocarse
    {
        "name": "e02-jiggy-frustrado",
        "refs": [WIZ_REF, JIGGY_REF],
        "ref_desc": f"{WIZ_DESC} {JIGGY_DESC}",
        "start": (
            f"{STYLE}\n\n"
            "Scene: Underground cave chamber with a dark unlit crystal. {ref_desc}\n\n"
            "Render Image 2 (Jiggy) standing in front of a completely dark/unlit crystal, "
            "looking frustrated and confused. He scratches his head with one hand, his body "
            "slightly off-balance. Comic frustration pose. The crystal is completely dark — "
            "no glow at all. Medium shot from slightly low angle. Cave background with "
            "faint ambient purple-blue light from distant crystals."
        ),
        "end": (
            f"{STYLE}\n\n"
            "Scene: Same cave chamber. {ref_desc}\n\n"
            "Render Image 2 (Jiggy) in foreground looking startled/surprised, turning around. "
            "Behind him, Image 1 (Wiz) emerges from the shadows, staff glowing softly, "
            "with a calm knowing expression. The unlit crystal between them stays dark. "
            "Dramatic rim-light from Wiz's staff crystal. Medium-wide shot."
        ),
    },
    # Escena 3: Vaciar y Anclar
    {
        "name": "e03-vaciar-anclar",
        "refs": [WIZ_REF],
        "ref_desc": WIZ_DESC,
        "start": (
            f"{STYLE}\n\n"
            "Scene: Close-up of Wiz's hand touching a crystal. {ref_desc}\n\n"
            "Extreme close-up: Image 1 (Wiz)'s aged turquoise hand with 4 fingers gently placed "
            "on a large crystal formation. The crystal just begins to glow — the faintest "
            "magenta-pink light emanating from where his fingers touch the surface. "
            "Subsurface scattering visible in both skin and crystal. Macro shot, shallow depth "
            "of field. Background is dark cave blur with purple-blue tones."
        ),
        "end": (
            f"{STYLE}\n\n"
            "Scene: Medium shot of Wiz teaching. {ref_desc}\n\n"
            "Image 1 (Wiz) stands beside the crystal which now glows with steady soft magenta "
            "light. His hand still on the crystal. He looks calm, centered, almost meditative. "
            "His staff behind him. The crystal casts rim-light on his face. "
            "Light text overlay area at bottom for subtitles. Medium shot."
        ),
    },
    # Escena 4: Jiggy practica — cristal se enciende
    {
        "name": "e04-jiggy-practica",
        "refs": [WIZ_REF, JIGGY_REF],
        "ref_desc": f"{WIZ_DESC} {JIGGY_DESC}",
        "start": (
            f"{STYLE}\n\n"
            "Scene: Jiggy imitating Wiz's technique. {ref_desc}\n\n"
            "Image 2 (Jiggy) places both hands on the crystal, eye closed in deep concentration. "
            "His usual mischievous expression is replaced by genuine focus. The crystal shows "
            "a warm pulsing glow building from the inside — mid-intensity magenta with cyan "
            "flecks. Image 1 (Wiz) watches from background, slightly out of focus, nodding. "
            "Medium shot, Jiggy in center."
        ),
        "end": (
            f"{STYLE}\n\n"
            "Scene: Crystal activation moment. {ref_desc}\n\n"
            "Dramatic moment: the crystal emits a powerful pulse of magenta-pink light that "
            "fills the entire cave. Image 2 (Jiggy) opens his eye wide in amazement, hands "
            "still on the now-brilliantly-glowing crystal. Light rays radiate outward. "
            "Dense bloom effect on the crystal. Image 1 (Wiz) in background smiles proudly. "
            "Volumetric god rays in magenta-pink. Wide-medium shot, slightly low angle heroic."
        ),
    },
    # Escena 5: Cristal encendido, cierre
    {
        "name": "e05-cristal-encendido",
        "refs": [WIZ_REF, JIGGY_REF],
        "ref_desc": f"{WIZ_DESC} {JIGGY_DESC}",
        "start": (
            f"{STYLE}\n\n"
            "Scene: Triumphant moment in the cave. {ref_desc}\n\n"
            "Image 2 (Jiggy) and Image 1 (Wiz) stand side by side in front of the fully "
            "activated crystal, which blazes with intense magenta-pink and cyan-white light. "
            "Jiggy smiles genuinely (not mischievous — truly happy). Wiz nods with serene "
            "approval. The crystal's light casts long shadows and fills the cave with warm "
            "volumetric glow. Multiple smaller crystals in the background also pulse in response. "
            "Wide shot, both characters in center, epic scale."
        ),
        "end": (
            f"{STYLE}\n\n"
            "Scene: Closing frame — the world lights up. {ref_desc}\n\n"
            "Epic wide establishing shot of the Uray Pacha cave network. Multiple crystal "
            "formations throughout the cavern now glow with magenta, cyan, and gold light — "
            "a chain reaction. Image 2 (Jiggy) and Image 1 (Wiz) are small figures in the "
            "lower third, silhouetted against the crystal light. Dense volumetric atmosphere "
            "with dust motes and god rays. Sense of wonder and scale. "
            "Cinematic wide shot, 16:9. Space at top for end-title text."
        ),
    },
]


async def main():
    client_async = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
    sem = asyncio.Semaphore(4)  # Concurrencia moderada para no pegar rate-limit

    async def gen(scene_name, frame_type, prompt, refs):
        output_path = os.path.join(FRAMES_DIR, f"{scene_name}_{frame_type}.png")
        if os.path.exists(output_path):
            print(f"  SKIP (ya existe): {output_path}")
            return output_path
        async with sem:
            print(f"  Generando: {scene_name}_{frame_type}...")
            try:
                result = await edit_image_async(
                    client_async=client_async,
                    prompt=prompt,
                    input_image_paths=refs,
                    output_path=output_path,
                    size="1536x1024",  # 16:9 landscape
                    quality="medium",
                )
                print(f"  OK: {result}")
                return result
            except Exception as e:
                print(f"  ERROR en {scene_name}_{frame_type}: {e}")
                return str(e)

    tasks = []
    for s in SCENES:
        ref_desc = s["ref_desc"]
        start_prompt = s["start"].replace("{ref_desc}", ref_desc)
        end_prompt = s["end"].replace("{ref_desc}", ref_desc)
        tasks.append(gen(s["name"], "start", start_prompt, s["refs"]))
        tasks.append(gen(s["name"], "end", end_prompt, s["refs"]))

    results = await asyncio.gather(*tasks)
    print(f"\nCompletados: {len([r for r in results if r and 'ERROR' not in str(r)])}/10")
    return results


if __name__ == "__main__":
    asyncio.run(main())
