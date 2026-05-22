"""
Test 04 — Prueba de fuego pax-image-gen skill.
Two-shot Jiggy (Pax) + Mariela (humana) en caverna.
DOS IDENTITY LOCKS DIFERENCIADOS: Pax non-human anatomy vs human anatomy.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openai_images import edit_image  # noqa: E402


PROMPT = """IDENTITY LOCK — TWO DIFFERENT SPECIES IN THE SAME FRAME, MUST BE VISUALLY DISTINCT.

Image 1 establishes the IDENTITY LOCK for the LEFT character — Jiggy, a Pax. Pax are a subterranean civilization, NOT human. Jiggy must visually match Image 1 exactly: ONE single large central eye (NOT two eyes), turquoise / teal skin, elongated pointed elastic ears, FOUR fingers per hand (NOT five), 3.5-head proportions, slim youthful build, Pax costume vocabulary as in Image 1. Match Image 1 anatomy and costume exactly.

Image 2 establishes the IDENTITY LOCK for the RIGHT character — Mariela, a HUMAN surface dweller. She is fully HUMAN, NOT a Pax. Mariela must visually match Image 2 exactly: TWO normal human eyes (NOT one), normal human skin tone (NOT turquoise), normal rounded human ears (NOT pointed elastic), FIVE fingers per hand (NOT four), normal adult human proportions (around 7-head proportions), modern casual clothing as in Image 2. Match Image 2 anatomy and clothing exactly.

These are TWO DIFFERENT SPECIES sharing the same frame. The Pax (Jiggy) and the human (Mariela) must remain anatomically DISTINCT — do not blend them, do not give Mariela one eye, do not give Jiggy two eyes, do not normalize Jiggy's hand to five fingers, do not give Mariela four fingers.

SUBJECT — First contact between Jiggy and Mariela inside a dark cavern. Two-shot side composition, medium shot framing both at roughly chest-up to mid-thigh. Jiggy stands on the LEFT, slightly crouched, body angled forward in curiosity, his single central eye wide open in playful astonishment, one of his four-fingered hands extended slowly toward Mariela in a curious reaching gesture. Mariela stands on the RIGHT, upright, hands resting on her hips, eyebrows arched, half-smile of "what on earth are you" — astonished but amused, NOT scared. They lock gazes. Between them, suspended in mid-air, floats a small jade-green crystal pulsing with soft inner light, its glow underlighting both faces from below (diegetic uplight).

COMPOSITION — Lateral two-shot, both characters fully visible, rule-of-thirds: Jiggy on the left third, Mariela on the right third, the floating crystal on the central vertical axis. Camera at eye level. Both faces clearly visible in three-quarter view turned toward each other.

LIGHT + PALETTE — Primary light source is the floating jade-green crystal between them, casting a soft uplight on both faces and rim-lighting the edges of their bodies. Subtle warm-amber ambient bounce on rock walls in the background. Canonical Pax palette: jade-green crystal glow, basalt-dark cavern, warm-amber accents, hint of neon-magenta in deep shadows. The cave background is rendered in deep shadow with blurred stalactites in soft bokeh.

STYLE / RENDER — Stylized 3D animation render with semi-realistic PBR shading and neon-magic lighting. NOT 2D, NOT painterly, NOT illustration, NOT anime, NOT photorealistic. Same render language as Image 1 and Image 2 character sheets. Volumetric atmosphere with soft cave dust catching the crystal glow.

REFERENCE INTEGRATION — Image 1 = LEFT character (Jiggy / Pax — non-human anatomy). Image 2 = RIGHT character (Mariela / human — human anatomy). Image 3 = environment + atmosphere reference (dark cavern with depth and bokeh background). Apply the canonical Pax palette: jade-green, warm-amber, basalt-dark, neon-magenta accents.

MOOD — The exact moment two species discover each other: comic tension plus tender astonishment. Playful, NOT threatening. Both are curious about the other, neither is afraid.

NEGATIVE PROMPT — Do NOT blend the two characters' anatomies. Do NOT give Mariela a single central eye (she has TWO normal human eyes). Do NOT give Jiggy two eyes (he has ONE central eye). Do NOT give Jiggy five fingers (he has FOUR). Do NOT give Mariela four fingers (she has FIVE). Do NOT give Mariela turquoise skin (her skin is normal human). Do NOT give Jiggy normal human skin (his skin is turquoise/teal). Do NOT give Mariela pointed elastic ears (her ears are normal human). Do NOT make them the same species. Do NOT use 2D hand-drawn aesthetic, painterly Studio Ghibli style, anime stylization, or photorealistic skin. Do NOT use generic indigenous/ethnographic costume tropes. They are visually distinct species in the same frame."""


if __name__ == "__main__":
    out = edit_image(
        prompt=PROMPT,
        input_image_paths=[
            "C:\\Users\\aldot\\.gemini\\antigravity\\scratch\\pax-os\\public\\images\\personajes\\jiggy.png",
            "C:\\Users\\aldot\\.gemini\\antigravity\\scratch\\pax-os\\public\\images\\personajes\\mariela.png",
            "C:\\Users\\aldot\\.gemini\\antigravity\\scratch\\pax-os\\public\\images\\concepts\\concept-cave-wide-dark.png",
        ],
        output_path="C:\\Users\\aldot\\.gemini\\antigravity\\scratch\\pax-os\\content\\test-images\\test-04-jiggy-mariela-meet.png",
        size="1536x1024",
        quality="medium",
    )
    print(f"OK: {out}")
