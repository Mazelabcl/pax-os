"""
Test 01 — Jiggy endless-runner mockup.
Aplica IDENTITY LOCK pattern + brand DNA Pax para generar UNA imagen.
"""

import os
import sys
import time

# Asegurar que podemos importar scripts.openai_images
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from scripts.openai_images import edit_image  # noqa: E402

PROMPT = """IDENTITY LOCK — CRITICAL FACIAL ANATOMY: The character in this scene is Jiggy, a Pax. He is a CYCLOPS-TYPE being. He has ONE — exactly ONE — single large central eye in the middle of his face. He does NOT have two eyes. He does NOT have a second small eye. He does NOT have a pair of eyes. Repeat: ONE big round central eye, dead center, no second eye, no companion eye, no smaller eye to the side. Treat the face like a single-eyed creature reference (think one-eyed minion / one-eyed alien anatomy), but using the exact face structure of Image 1. The character is a Pax — a member of a subterranean civilization, NOT a human surface dweller, NOT an Andean indigenous person, NOT a generic fantasy creature, NOT a two-eyed cartoon character. Match Image 1 exactly: same proportional language, same facial structure, same costume vocabulary, same skin color treatment. Other non-human anatomy: turquoise / teal skin, elongated pointed elastic ears, FOUR fingers per hand (not five — count them: thumb plus three fingers), 3.5-head body proportions, young runner build. He is kin to the cast in Image 1.

SUBJECT: Jiggy frozen mid-air in a dynamic jump, body diagonal to the camera, one arm fully outstretched upward and forward, his four-fingered hand (clearly readable: thumb + three fingers, NOT five) closing around a floating jade-green crystal that glows from within. The opposite arm is swung back in a counter-balance impulse pose, fist clenched. Legs tucked in a sprinting tuck — knees bent, feet trailing, mid-stride captured at peak height. His single big central cyclops eye is locked on the crystal — one single eye only, perfectly centered, no second eye visible anywhere on the face. Subtle motion blur on the trailing leg and a small dust puff below his feet sells the speed and the takeoff a split second ago.

COMPOSITION: Mobile portrait orientation, vertical 2:3 framing built like a screenshot of an endless-runner mobile game. Side-3/4 camera angle, low angle pushing slightly upward so Jiggy reads heroic. Foreground: Jiggy mid-jump with the big jade crystal in hand, occupying the lower-middle third of the frame. Mid-ground: a curving subterranean tunnel track sweeping into the depth of the frame, with smaller jade crystals floating along the lane and basalt rock obstacles staggered in perspective. Background: the tunnel narrowing into glowing depth, hinting at more lanes ahead. Strong perspective lines guide the eye into the distance — classic endless-runner depth-of-field language.

LIGHT + PALETTE: Primary diegetic light source is the large jade crystal in Jiggy's hand, emitting soft neon-magic glow that wraps his hand, forearm, and rim-lights his face and torso in cool jade-green. Secondary fill from amber-warm crystal embers along the tunnel walls. Deep basalt-dark rock tones for the cave structure. Magenta-neon accent flickers from one or two distant crystals far down the tunnel. Canonical Pax palette: jade-green, warm-amber, basalt-dark, neon-magenta accents — all four readable in frame.

STYLE / RENDER: Stylized 3D animation, semi-realistic PBR shading, neon-magic lighting. Polished AAA mobile game render aesthetic, like a high-budget Subway-Surfers-meets-Crash-Bandicoot key visual, but with the Pax universe DNA. Crisp specular highlights on the crystal, subsurface scattering on Jiggy's turquoise skin, fine subsurface glow inside the jade crystal. NOT 2D, NOT hand-drawn, NOT painterly, NOT illustration, NOT anime stylization, NOT photorealistic.

REFERENCE INTEGRATION: Image 1 establishes IDENTITY LOCK for Jiggy — match anatomy, proportions, facial structure, costume vocabulary, and skin color exactly. Image 2 provides the cave atmosphere, crystal lighting language, and stalagmite geometry vocabulary for the tunnel environment. Image 3 anchors the canonical color palette and overall render base. Apply the canonical Pax palette across the whole frame: jade-green, warm-amber, basalt-dark, neon-magenta accents.

NEGATIVE PROMPT — STRICT: Do NOT draw two eyes. Do NOT draw a pair of eyes. Do NOT add a second smaller eye next to the main one. Do NOT add a side eye. Do NOT split the central eye into two. The face has exactly ONE eye, centered. Also do not include: human anatomy with two eyes (the character is a cyclops-type Pax with ONE central eye), generic indigenous or ethnographic costumes, 2D hand-drawn aesthetic, painterly Studio Ghibli style, photorealistic skin, five-fingered hands, twentieth-century human references, generic fantasy art tropes, anime big-eyes stylization, flat illustration, sticker style, cel-shaded toon. The character must NOT read as a two-eyed humanoid or a two-eyed cartoon character. Single eye only."""


def main():
    out_path = r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\content\test-images\test-01-jiggy-runner-v2.png"
    refs = [
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\jiggy.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-cave-stalagmites-reawakening.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada.png",
    ]

    for p in refs:
        if not os.path.exists(p):
            print(f"FALTA REFERENCIA: {p}")
            sys.exit(2)

    print("Generando test-01-jiggy-runner.png ...")
    t0 = time.time()
    result = edit_image(
        prompt=PROMPT,
        input_image_paths=refs,
        output_path=out_path,
        size="1024x1536",
        quality="medium",
    )
    dt = time.time() - t0
    print(f"OK -> {result}  ({dt:.1f}s)")


if __name__ == "__main__":
    main()
