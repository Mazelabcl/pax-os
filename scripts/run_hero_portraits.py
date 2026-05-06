"""
Hero portraits del cast Pax — 5 imagenes en serie.
Aplica IDENTITY LOCK + cyclops vocabulary + brand DNA + negative anti-drift de props.

Output: content/test-images/char-{slug}-hero-portrait.png
Modelo: gpt-image-2, quality medium, 1024x1024
"""

import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from scripts.openai_images import edit_image  # noqa: E402


PERSONAJES_DIR = r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes"
PORTADAS_DIR = r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas"
OUT_DIR = r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\content\test-images"

PORTADA = os.path.join(PORTADAS_DIR, "portada.png")


# ---------------------------------------------------------------------------
# Bloques reusables del prompt
# ---------------------------------------------------------------------------

IDENTITY_LOCK_PAX = (
    "IDENTITY LOCK — CRITICAL FACIAL ANATOMY: The character in this scene is a Pax — a cyclops-type "
    "single-eyed humanoid. He / she has ONE — exactly ONE — single large central eye in the middle of "
    "the face. NOT two eyes. NOT a pair of eyes. NOT a second smaller eye to the side. Repeat: ONE big "
    "round central eye, dead center, no companion eye, no extra eye anywhere on the face. Cyclops-type "
    "anatomy. The character is a Pax — a member of a subterranean civilization, NOT a human surface "
    "dweller, NOT an Andean indigenous person, NOT a generic fantasy creature, NOT a two-eyed cartoon "
    "character. Match Image 1 exactly: same proportional language, same facial structure, same costume "
    "vocabulary, same skin color treatment, same accessories present in Image 1 (and ONLY those). Other "
    "non-human anatomy traits: turquoise / teal skin, elongated pointed elastic ears, FOUR fingers per "
    "hand (thumb plus three fingers, NOT five), 3.5-head body proportions. Kin of the Pax cast."
)

STYLE_RENDER = (
    "STYLE / RENDER: Stylized 3D animation, semi-realistic PBR shading, neon-magic lighting. Polished "
    "AAA marketing key-art render. Crisp specular highlights, subsurface scattering on the turquoise "
    "skin, glow from any crystal in frame. NOT 2D, NOT hand-drawn, NOT painterly, NOT illustration, "
    "NOT anime stylization, NOT photorealistic."
)

REFERENCE_INTEGRATION = (
    "REFERENCE INTEGRATION: Image 1 establishes IDENTITY LOCK for the character — match anatomy, "
    "proportions, facial structure, costume vocabulary, accessories and skin color exactly. Image 2 "
    "anchors the canonical color palette and overall render base of the Pax universe. Apply the "
    "canonical Pax palette across the frame: jade-green, warm-amber, basalt-dark, neon-magenta accents."
)

NEGATIVE_PROMPT = (
    "NEGATIVE PROMPT — STRICT: Do NOT draw two eyes. Do NOT draw a pair of eyes. Do NOT add a second "
    "smaller eye next to the main one. Do NOT add a side eye. Do NOT split the central eye into two. "
    "The face has exactly ONE eye, centered. Do NOT add accessories, jewelry, bandanas, scarves, "
    "amulets, hats, glasses, earrings or props that are not present in Image 1. Do NOT invent costume "
    "details. Also do NOT include: human anatomy with two eyes, generic indigenous or ethnographic "
    "costumes, 2D hand-drawn aesthetic, painterly Studio Ghibli style, photorealistic skin, "
    "five-fingered hands, twentieth-century human references, generic fantasy art tropes, anime "
    "big-eyes stylization, flat illustration, sticker style, cel-shaded toon, text, logos, watermarks, "
    "borders. Single eye only."
)


def build_prompt(subject_block: str, composition_block: str, light_block: str) -> str:
    return "\n\n".join([
        IDENTITY_LOCK_PAX,
        f"SUBJECT: {subject_block}",
        f"COMPOSITION: {composition_block}",
        f"LIGHT + PALETTE: {light_block}",
        STYLE_RENDER,
        REFERENCE_INTEGRATION,
        NEGATIVE_PROMPT,
    ])


# ---------------------------------------------------------------------------
# Definicion de las 5 imagenes
# ---------------------------------------------------------------------------

JOBS = [
    {
        "slug": "jiggy",
        "char_png": "jiggy.png",
        "subject": (
            "Jiggy, the young Pax runner of the cast, in a confident hero pose. Plano medio frontal "
            "three-quarter angle. His single large central cyclops eye is open and looking slightly "
            "upward in a heroic gaze. A subtle lateral half-smile reads confident. One of his "
            "four-fingered hands rests on his hip; the other holds, between his fingers, a small "
            "floating jade-green crystal that hovers and glows softly, casting cool rim-light on his "
            "fingertips. Posture is relaxed but assertive — shoulders open, chin slightly up. Costume "
            "and accessories EXACTLY as in Image 1, no additions."
        ),
        "composition": (
            "Square 1024x1024 hero portrait. Medium shot framing him from mid-thigh up. Three-quarter "
            "angle of the body, face turned slightly toward camera. Rule-of-thirds: eye on the upper "
            "third line. Generous headroom above the head for a future title overlay. Subject occupies "
            "roughly the central 60 percent of the frame, centered horizontally."
        ),
        "light": (
            "Primary key light: the small floating jade crystal in his hand, emitting cool jade-green "
            "neon-magic glow that rim-lights his hand and the underside of his jaw. Secondary fill: "
            "warm magenta-neon backlight from the gradient background washing the silhouette. "
            "Background: smooth gradient from deep basalt-dark at the bottom to neon-magenta at the "
            "top, with a few subtle Pax-vocabulary geometric shapes (hex tiles, faint runic lines) "
            "floating very softly out of focus. Canonical Pax palette readable: jade-green, "
            "warm-amber accents, basalt-dark, neon-magenta."
        ),
        "out": "char-jiggy-hero-portrait.png",
    },
    {
        "slug": "wiz",
        "char_png": "wiz.png",
        "subject": (
            "Wiz, the elder sage of the Pax cast — older Pax with white beard, hood pulled up over "
            "the head, EXACTLY as in Image 1. He carries his staff topped with a magenta-neon crystal "
            "clearly visible in frame. Expression: serious-yet-kind, wisdom-and-warmth. His single "
            "large central cyclops eye is very expressive, slightly squinted in a knowing way. The "
            "staff is held diagonally across the body. Costume and accessories EXACTLY as in Image 1, "
            "no additions, no invented amulets, no extra jewelry."
        ),
        "composition": (
            "Square 1024x1024 hero portrait. Medium shot framing him from mid-chest up, with the "
            "crystal-topped staff visible reaching into the upper portion of the frame. Three-quarter "
            "frontal angle. Rule-of-thirds: the single central eye on the upper third intersection. "
            "Headroom above the hood and the crystal for title overlay. Centered composition with the "
            "staff anchoring the right vertical."
        ),
        "light": (
            "Primary key light: the magenta-neon crystal on top of the staff, emitting warm-magenta "
            "neon-magic glow that uplights his face from above and rim-lights the hood edge. "
            "Secondary fill: warm-amber from the gradient background. Background: smooth gradient "
            "from warm-amber at the top to deep basalt-dark at the bottom, with very subtle glowing "
            "Pax-vocabulary runic etchings barely visible behind him, slightly out of focus. "
            "Canonical Pax palette readable: warm-amber dominant, basalt-dark, neon-magenta accent, "
            "jade-green hint."
        ),
        "out": "char-wiz-hero-portrait.png",
    },
    {
        "slug": "byte",
        "char_png": "byte.png",
        "subject": (
            "Byte, the young Pax hacker / techie of the cast, EXACTLY matching Image 1. Headphones "
            "hanging around the neck (not on the ears). Hooded technical jacket as worn in Image 1. "
            "In his four-fingered hands he holds a flat device-card / handheld interface panel "
            "displaying a glowing neon-magenta UI of grids and small graphs. His single central "
            "cyclops eye is on the device, then flicks half-confidently to the camera. Expression: "
            "confident-cool, half-smile. Posture relaxed, leaning slightly forward. Costume and "
            "accessories EXACTLY as in Image 1, no additions."
        ),
        "composition": (
            "Square 1024x1024 hero portrait. Medium shot framing from mid-chest up, hands and the "
            "device-card visible in the lower third of the frame. Three-quarter frontal angle, body "
            "slightly turned, face toward camera. Rule-of-thirds: eye on upper third, device on lower "
            "third. Headroom above the hood for title overlay."
        ),
        "light": (
            "Primary key light: the neon-magenta UI on the device-card uplighting his hands and the "
            "underside of his jaw with cool magenta accents. Secondary fill: jade-cyan rim-light from "
            "the gradient background. Background: smooth gradient from jade-cyan at the top to "
            "basalt-dark at the bottom, with a very subtle digital grid pattern (faint thin lines, "
            "slightly out of focus) implying a technical / data atmosphere. Canonical Pax palette "
            "readable: jade-green dominant in the gradient, basalt-dark, neon-magenta accent on the "
            "device, warm-amber hint."
        ),
        "out": "char-byte-hero-portrait.png",
    },
    {
        "slug": "luxa",
        "char_png": "luxa.png",
        "subject": (
            "Luxa, the female Pax of the cast, EXACTLY matching Image 1 — same costume, same hair / "
            "head silhouette, same accessories present in Image 1, no inventions. Expression: serene "
            "yet firm — composed, grounded, with quiet authority. Her single large central cyclops "
            "eye is open and direct. One of her four-fingered hands holds, near chest height, a small "
            "jade-magenta crystal that lights her face from below in a subtle uplight. Posture: "
            "upright, shoulders back, dignified."
        ),
        "composition": (
            "Square 1024x1024 hero portrait. Medium shot framing from mid-chest up, with the hand "
            "holding the small crystal visible in the lower third. Three-quarter frontal angle. "
            "Rule-of-thirds: eye on upper third intersection. Headroom above the head for title "
            "overlay. Centered subject."
        ),
        "light": (
            "Primary key light: the small crystal in her hand uplighting her face from below with a "
            "subtle magenta-jade neon-magic glow, catching her chin, the underside of her cheekbone, "
            "and the lower edge of her central eye. Secondary fill: warm magenta-rose from the "
            "gradient background. Background: smooth gradient from neon-magenta-rose at the top to "
            "deep basalt-dark at the bottom, with very subtle Pax-vocabulary architectural elements "
            "(arches, faint pillars, hex motifs) barely readable, out of focus. Canonical Pax palette "
            "readable: neon-magenta dominant, basalt-dark, jade-green accent on the crystal, "
            "warm-amber hint."
        ),
        "out": "char-luxa-hero-portrait.png",
    },
    {
        "slug": "zek",
        "char_png": "zek.png",
        "subject": (
            "Zek, the lateral-cool Pax of the cast, EXACTLY matching Image 1 — same costume, same "
            "hair / head silhouette, same accessories present in Image 1 (including any headphones "
            "or signature gear shown in Image 1), no inventions, no extra props. Expression: "
            "confident with a relaxed, slightly mischievous half-smile. His single central cyclops "
            "eye looks toward the camera with attitude. Posture: relaxed-confident, one shoulder "
            "slightly forward, body angled, very slight lateral lean — vibe-cool body language."
        ),
        "composition": (
            "Square 1024x1024 hero portrait. Medium shot framing from mid-chest up. Three-quarter "
            "angle with body slightly more turned (lateral) than the other characters to read "
            "vibe-cool. Rule-of-thirds: eye on upper third. Headroom above the head for title "
            "overlay. Centered subject."
        ),
        "light": (
            "Primary key light: warm-amber rim-light from the upper-left, catching the silhouette "
            "and the cheekbone. Secondary fill: subtle magenta accent from the lower-right. "
            "Background: smooth gradient from warm-amber-orange at the top to deep basalt-dark at "
            "the bottom, with very subtle motion lines / streaks in the background (soft, blurred, "
            "out of focus) implying dynamic energy. Canonical Pax palette readable: warm-amber "
            "dominant, basalt-dark, neon-magenta accent, jade-green hint."
        ),
        "out": "char-zek-hero-portrait.png",
    },
]


def main():
    # Validar que todas las references existen
    missing = []
    for job in JOBS:
        char_path = os.path.join(PERSONAJES_DIR, job["char_png"])
        if not os.path.exists(char_path):
            missing.append(char_path)
    if not os.path.exists(PORTADA):
        missing.append(PORTADA)
    if missing:
        print("FALTAN REFERENCIAS:")
        for m in missing:
            print(f"  - {m}")
        sys.exit(2)

    os.makedirs(OUT_DIR, exist_ok=True)

    results = []
    for i, job in enumerate(JOBS, 1):
        char_path = os.path.join(PERSONAJES_DIR, job["char_png"])
        out_path = os.path.join(OUT_DIR, job["out"])

        prompt = build_prompt(job["subject"], job["composition"], job["light"])

        print(f"\n[{i}/{len(JOBS)}] Generando {job['slug']} -> {job['out']}")
        t0 = time.time()
        try:
            result = edit_image(
                prompt=prompt,
                input_image_paths=[char_path, PORTADA],
                output_path=out_path,
                size="1024x1024",
                quality="medium",
            )
            dt = time.time() - t0
            print(f"  OK -> {result}  ({dt:.1f}s)")
            results.append((job["slug"], "OK", out_path, dt))
        except Exception as e:
            dt = time.time() - t0
            print(f"  ERROR ({dt:.1f}s): {e}")
            results.append((job["slug"], "ERROR", str(e), dt))

    print("\n=== RESUMEN ===")
    for slug, status, info, dt in results:
        print(f"  {slug:8s}  {status:6s}  {dt:5.1f}s  {info}")


if __name__ == "__main__":
    main()
