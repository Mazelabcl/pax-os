"""
Genera los 8 frames (start + end) para las 4 capsulas de video de gestos Pax.

Usa edit_image() con char sheets canonicos como referencia.
Para Paxearte start (foto humana generica), usa generate_image() ya que no hay personaje Pax.

Ejecutar desde la raiz del repo:
    python scripts/gen_capsule_frames.py
"""

import os
import sys
import asyncio

# Add repo root to path so we can import openai_images
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO_ROOT, "scripts"))

from openai_images import generate_image, edit_image, generate_batch_async

# Paths
CHARS = os.path.join(REPO_ROOT, "_lore", "personajes")
BACKLOG = os.path.join(REPO_ROOT, "gestos", "_backlog")
HUMANIZED_ALDOT = os.path.join(REPO_ROOT, "nuevos_gestos", "aldo-2.jpg")
HUMANIZED_PIPEZ = os.path.join(REPO_ROOT, "nuevos_gestos", "pipez.jpg")

JIGGY = os.path.join(CHARS, "jiggy.png")
WIZ = os.path.join(CHARS, "wiz.png")
KZ = os.path.join(CHARS, "kz.png")

SIZE = "1536x1024"  # 16:9-ish for video backgrounds
QUALITY = "high"


def main():
    print("=== Generando 8 capsule frames ===\n")

    # -----------------------------------------------------------------------
    # CAPSULE 1 — Paxearte (transformacion humano -> Pax)
    # -----------------------------------------------------------------------
    print("[1/8] Paxearte — start frame (retrato humano generico)")
    paxearte_start = os.path.join(BACKLOG, "paxearte", "capsule", "start.png")
    generate_image(
        prompt=(
            "A professional portrait photograph of a generic young woman around 25 years old, "
            "warm brown skin, dark hair, looking directly at camera with a slight smile. "
            "Clean neutral gray studio background. Natural studio lighting, soft shadows. "
            "Photorealistic, high quality portrait photography. No accessories, simple white t-shirt. "
            "Centered composition, head and shoulders framing."
        ),
        output_path=paxearte_start,
        size=SIZE,
        quality=QUALITY,
    )
    print(f"   -> {paxearte_start}")

    print("[2/8] Paxearte — end frame (misma persona paxeada, estilo humanizado)")
    paxearte_end = os.path.join(BACKLOG, "paxearte", "capsule", "end.png")
    edit_image(
        prompt=(
            "Image 1 is a humanized Pax tribe character reference (Aldot). Image 2 is another humanized Pax reference (Pipez). "
            "Generate a young woman (~25 years old) transformed into a Pax tribe member in the SAME humanized style as Image 1 and Image 2: "
            "HUMAN skin tone (warm brown, NOT green/turquoise), ONE SINGLE LARGE CYCLOPS EYE in the center of the face replacing both eyes, "
            "pointed elf ears, chibi proportions (large head ~40% of body height), "
            "turquoise geometric tattoos on arms and face, purple bandana with tribal patterns on head, "
            "tribal Pax outfit (cream vest with purple patterns, dark pants, leather sandals), "
            "purple crystal pendant necklace, bronze bracelets. "
            "Purple crystals swirling magically around her, background is a luminous underground crystal cave "
            "with jade and magenta glowing crystals. "
            "3D PBR stylized render, neon-magic lighting, cinematographic, Pixar-quality. "
            "The character must have EXACTLY ONE eye — this is critical."
        ),
        input_image_paths=[HUMANIZED_ALDOT, HUMANIZED_PIPEZ],
        output_path=paxearte_end,
        size=SIZE,
        quality=QUALITY,
    )
    print(f"   -> {paxearte_end}")

    # -----------------------------------------------------------------------
    # CAPSULE 2 — Coloring Book (pagina B&N cobra vida)
    # -----------------------------------------------------------------------
    print("[3/8] Coloring Book — start frame (pagina B&N line art)")
    coloring_start = os.path.join(BACKLOG, "coloring-book", "capsule", "start.png")
    edit_image(
        prompt=(
            "Image 1 is Jiggy, a Pax tribe cyclops character reference. "
            "Generate a BLACK AND WHITE coloring book page featuring the character from Image 1 (Jiggy). "
            "Clean line art style with thick black outlines on pure white background. "
            "Jiggy is running joyfully holding a crystal in his hand. Around him: large crystals growing from the ground, "
            "small floating sparkles, geometric tribal patterns as borders. "
            "The style is a children's coloring book page — NO color fill, ONLY black outlines on white. "
            "Clean, professional line art quality. Simple enough for a child to color. "
            "Centered composition on the page."
        ),
        input_image_paths=[JIGGY],
        output_path=coloring_start,
        size=SIZE,
        quality=QUALITY,
    )
    print(f"   -> {coloring_start}")

    print("[4/8] Coloring Book — end frame (misma composicion, full color 3D)")
    coloring_end = os.path.join(BACKLOG, "coloring-book", "capsule", "end.png")
    edit_image(
        prompt=(
            "Image 1 is Jiggy, a Pax tribe cyclops character reference. "
            "Generate the SAME composition as a coloring book page but NOW in FULL VIBRANT COLOR and 3D: "
            "Jiggy (matching Image 1 exactly — turquoise skin, single large cyclops eye, explorer vest) running joyfully "
            "holding a glowing magenta crystal. He appears to be stepping OUT of the coloring book page — "
            "the bottom edge of the image shows remnants of the black-and-white line art page curling up. "
            "Crystals around him glow brilliantly in jade (#2EE0C8) and magenta (#E83FC8), "
            "magical light particles and sparkles float everywhere. "
            "Background transitions from flat white (coloring book) at the edges to a deep purple crystal cave. "
            "3D PBR stylized render, neon-magic lighting, bloom and glow effects, cinematographic. "
            "Magical transformation moment — the page is coming alive."
        ),
        input_image_paths=[JIGGY],
        output_path=coloring_end,
        size=SIZE,
        quality=QUALITY,
    )
    print(f"   -> {coloring_end}")

    # -----------------------------------------------------------------------
    # CAPSULE 3 — Child Story (nino entra al mundo Pax)
    # -----------------------------------------------------------------------
    print("[5/8] Child Story — start frame (nino con libro magico)")
    child_start = os.path.join(BACKLOG, "child-story", "capsule", "start.png")
    edit_image(
        prompt=(
            "Image 1 is Jiggy and Image 2 is KZ — Pax tribe cyclops characters (for reference of the magical world). "
            "Generate a scene of a real human child (~7 years old boy, brown skin, dark hair, pajamas) "
            "sitting cross-legged on his bedroom floor at night. He holds an open book on his lap. "
            "The book GLOWS with intense jade-green and purple magical light emanating from its pages, "
            "illuminating the child's amazed face from below. "
            "The bedroom is cozy: bed with colorful blanket behind, toys on shelves, night lamp. "
            "Tiny sparkles and crystal-shaped light particles rise from the book pages. "
            "The child looks down at the book with WONDER and awe, mouth slightly open. "
            "Photorealistic child + magical book light effect. Warm bedroom lighting mixed with "
            "the cool jade/purple magic light from the book. Cinematic composition, front view."
        ),
        input_image_paths=[JIGGY, KZ],
        output_path=child_start,
        size=SIZE,
        quality=QUALITY,
    )
    print(f"   -> {child_start}")

    print("[6/8] Child Story — end frame (nino dentro del mundo Pax)")
    child_end = os.path.join(BACKLOG, "child-story", "capsule", "end.png")
    edit_image(
        prompt=(
            "Image 1 is Jiggy, Image 2 is KZ — canonical Pax tribe cyclops characters. "
            "Generate: the SAME child (~7 year old boy, brown skin, dark hair) but NOW he is INSIDE the Pax world. "
            "He stands in a magnificent underground crystal cave, surrounded by giant glowing crystals "
            "in jade (#2EE0C8) and magenta (#E83FC8). "
            "Jiggy (matching Image 1 — turquoise skin cyclops with explorer vest) stands to his LEFT, smiling warmly. "
            "KZ (matching Image 2 — smaller, younger turquoise cyclops) stands to his RIGHT, waving excitedly. "
            "The child now wears a small purple Pax bandana on his head and looks amazed. "
            "The cave ceiling has crystal stalactites that emit soft purple and jade light. "
            "God rays / volumetric light shafts come from above. "
            "3D PBR stylized render, neon-magic lighting, cinematographic, magical atmosphere. "
            "The child is photorealistic while the Pax characters and environment are in stylized 3D."
        ),
        input_image_paths=[JIGGY, KZ],
        output_path=child_end,
        size=SIZE,
        quality=QUALITY,
    )
    print(f"   -> {child_end}")

    # -----------------------------------------------------------------------
    # CAPSULE 4 — Video Educativo (Wiz ensena, cristales se encienden)
    # -----------------------------------------------------------------------
    print("[7/8] Video Educativo — start frame (cueva oscura, Wiz y Jiggy)")
    edu_start = os.path.join(BACKLOG, "video-educativo", "capsule", "start.png")
    edit_image(
        prompt=(
            "Image 1 is Wiz, an elderly Pax sage (turquoise cyclops with long white beard, purple robe, crystal staff). "
            "Image 2 is Jiggy, a young Pax explorer (turquoise cyclops with explorer vest). "
            "Generate a DARK underground crystal cave scene. The cave is mostly in shadow — very dim lighting. "
            "Large crystals grow from walls and ceiling but they are UNLIT, dull, grayish-purple, dormant. "
            "Wiz (matching Image 1 exactly) sits cross-legged on the left, his staff resting across his lap, "
            "the crystal on top is DIM and barely glowing. His expression is patient, waiting. "
            "Jiggy (matching Image 2 exactly) sits across from Wiz on the right, but he is DISTRACTED — "
            "looking away to the side, fidgeting, not paying attention. "
            "The only light sources: very faint ambient purple from the dormant crystals, "
            "and a tiny warm glow from Wiz's staff crystal. "
            "Mood: quiet, expectant, the lesson hasn't started yet. "
            "3D PBR stylized render, dark moody cinematic lighting, subtle volumetric haze."
        ),
        input_image_paths=[WIZ, JIGGY],
        output_path=edu_start,
        size=SIZE,
        quality=QUALITY,
    )
    print(f"   -> {edu_start}")

    print("[8/8] Video Educativo — end frame (cueva iluminada, Jiggy concentrado)")
    edu_end = os.path.join(BACKLOG, "video-educativo", "capsule", "end.png")
    edit_image(
        prompt=(
            "Image 1 is Wiz, an elderly Pax sage (turquoise cyclops with long white beard, purple robe, crystal staff). "
            "Image 2 is Jiggy, a young Pax explorer (turquoise cyclops with explorer vest). "
            "Generate the SAME underground crystal cave but NOW fully ILLUMINATED with brilliant light. "
            "Every crystal in the cave is ALIVE and GLOWING intensely — jade (#2EE0C8) and magenta (#E83FC8) "
            "light fills the entire cavern. God rays stream through crystal formations. "
            "Jiggy (matching Image 2) now sits cross-legged in deep CONCENTRATION, eyes closed peacefully, "
            "both hands placed on a large crystal in front of him that BLAZES with intense jade-white light. "
            "Energy particles swirl upward from the crystal through his hands. "
            "Wiz (matching Image 1) observes from the left with a subtle proud SMILE, staff now glowing brightly, "
            "his posture relaxed — the student has learned. "
            "The cave is TRANSFORMED: magical, warm, every surface reflecting prismatic crystal light. "
            "3D PBR stylized render, brilliant neon-magic lighting, heavy bloom, volumetric god rays, "
            "cinematographic, triumphant magical atmosphere."
        ),
        input_image_paths=[WIZ, JIGGY],
        output_path=edu_end,
        size=SIZE,
        quality=QUALITY,
    )
    print(f"   -> {edu_end}")

    print("\n=== 8/8 frames generados exitosamente ===")


if __name__ == "__main__":
    main()
