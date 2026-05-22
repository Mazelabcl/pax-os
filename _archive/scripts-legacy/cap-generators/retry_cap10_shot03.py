"""
Re-genera cap-10-shot-03-arrive-plaza con prompt suavizado para evitar
rechazo del safety system. Quita "andean ushnu" + "ceremonial" — usa una
piedra plana redondeada generica.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from scripts.openai_images import edit_image  # noqa: E402
from scripts.gen_caps_3_to_12_async import (  # noqa: E402
    JIGGY, WIZ, AGATHA, KZ, ONYX, BYTE, LUXA, GRATE,
    build_prompt, OUT,
)

scene = (
    "Wide shot, 24mm lens, slight low angle. The clan of seven Pax stands "
    "at the edge of a small ordinary neighborhood plaza at sunrise — "
    "concrete benches, a weathered round flat stone in the center of the "
    "plaza, graffiti-covered concrete walls bordering. They are tiny in "
    "the open space. Jiggy in front holding the golden-pale spark glowing "
    "warm. Each ONE central eye visible. The soft pink-gold light of dawn "
    "floods the plaza. Mood: arrival, stillness, this is the place."
)

prompt = build_prompt(
    scene=scene,
    characters=["jiggy", "wiz", "agatha", "kz", "onyx", "byte", "luxa"],
)

out_path = os.path.join(OUT, "cap-10-shot-03-arrive-plaza.png")
print(f"[retry] cap-10-shot-03-arrive-plaza -> {out_path}", flush=True)

edit_image(
    prompt=prompt,
    input_image_paths=[JIGGY, WIZ, AGATHA, KZ, ONYX, BYTE, LUXA, GRATE],
    output_path=out_path,
    size="1536x1024",
    quality="low",
)

# md companion
md_path = out_path.replace(".png", ".md")
md = (
    f"# Cap 10 — Shot 03-arrive-plaza\n\n"
    f"**Personajes en frame:** jiggy, wiz, agatha, kz, onyx, byte, luxa\n\n"
    f"## Prompt completo\n\n```\n{prompt}\n```\n\n"
    f"## Tech\n\n"
    f"- Modelo: gpt-image-2\n"
    f"- Quality: low\n"
    f"- Size: 1536x1024\n"
    f"- Generado por: scripts/retry_cap10_shot03.py "
    f"(prompt suavizado tras moderation block del run paralelo original)\n\n"
    f"---\n"
    f"canonization_status: pending_aldot_approval\n"
)
with open(md_path, "w", encoding="utf-8") as f:
    f.write(md)
print("[ok] retry done", flush=True)
