"""
Genera avatares Paxearte de personas ficticias en 2 estilos:
- Full Pax (piel turquesa jade, ciclope)
- Humanizado (piel humana, outfit Pax, ciclope chibi)
Usa las refs de nuevos_gestos/ como Image references para gpt-image-2.
"""
import os
import sys

# Add repo root to path so we can import the module
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from scripts.openai_images import edit_image, generate_image

OUT_DIR = os.path.join(REPO, "gestos", "_backlog", "paxearte", "images")
REF_DIR = os.path.join(REPO, "nuevos_gestos")

# Reference images
REF_FULL_PAX = os.path.join(REF_DIR, "aldo-1.jpg")       # Full Pax style ref
REF_HUMANIZED_SHEET = os.path.join(REF_DIR, "pipez.jpg")  # Humanized char sheet ref
REF_HUMANIZED_SINGLE = os.path.join(REF_DIR, "aldo-2.jpg") # Humanized single + sheet ref

STYLE_BLOCK = (
    "Stylized 3D animation, semi-realistic PBR shading with subsurface scattering on skin, "
    "expressive cartoon proportions (cyclops 3-3.5 heads tall), high-contrast cinematic "
    "neon-magic lighting (magenta #E83FC8 + cyan #2EE0C8), saturated emissive violet crystals "
    "with bloom, slight film grain, color grading magenta/turquoise complementary, "
    "plain light gray studio background. Reads as premium mobile-game cinematic character art. "
    "Negative: photorealistic, anime, 2D hand-drawn, cel-shaded flat, Pixar/Disney generic look, "
    "fantasy battle cliches, game HUD, glamour beauty shot."
)

jobs = [
    # --- FULL PAX (turquoise skin) ---
    {
        "name": "full-pax-woman-latina.png",
        "refs": [REF_FULL_PAX],
        "prompt": (
            f"{STYLE_BLOCK} "
            "Full-body character portrait of a fictional young Latina woman transformed into a Pax tribe member — "
            "FULL PAX style like Image 1. Her skin is entirely jade-turquoise mineral (#21D8B6) with subtle "
            "subsurface scattering glow. She has ONE single large cyclops eye in the center of her face "
            "(big, expressive, turquoise iris #3FE0C8 with black pupil and double specular highlight), "
            "NO nose visible, wide elastic mouth. Pointed elf ears curving back. "
            "Her black curly hair is pulled up with a purple tribal bandana (#7A3FB2) with geometric diamond patterns. "
            "Jade geometric tribal tattoos across arms and neck. "
            "Outfit: cream-and-purple tribal vest with geometric embroidery, brown leather belt with hanging "
            "violet crystal pendants (#8A4DD1 emissive), leather wrist bracers with bronze buckles, "
            "dark blue baggy shorts, brown leather sandals with crystal accents. "
            "She holds a twisted wooden staff topped with a large glowing violet crystal. "
            "Confident adventurer pose, one hand on hip. Plain light gray background."
        ),
    },
    {
        "name": "full-pax-man-asian.png",
        "refs": [REF_FULL_PAX],
        "prompt": (
            f"{STYLE_BLOCK} "
            "Full-body character portrait of a fictional young East Asian man transformed into a Pax tribe member — "
            "FULL PAX style like Image 1. His skin is entirely jade-turquoise mineral (#21D8B6) with subtle "
            "subsurface scattering glow. He has ONE single large cyclops eye centered on his face "
            "(big, expressive, turquoise iris #3FE0C8 with black pupil and double specular highlight), "
            "NO nose visible, wide elastic mouth with small white teeth. Pointed elf ears. "
            "Short spiky black hair. Jade geometric tribal tattoos on arms, chest and legs. "
            "Outfit: sleeveless cream tribal tunic with purple geometric borders, leather harness across chest "
            "with a glowing violet crystal pendant (#8A4DD1 emissive), brown leather belt with hanging "
            "crystal vials and pouches, dark navy shorts, leather wrap sandals. "
            "He holds a glowing magenta crystal (#FF49B4) in his raised right hand triumphantly. "
            "Dynamic action pose, mid-stride. Plain light gray background."
        ),
    },
    # --- HUMANIZED (human skin + Pax outfit) ---
    {
        "name": "humanized-woman-african.png",
        "refs": [REF_HUMANIZED_SINGLE],
        "prompt": (
            f"{STYLE_BLOCK} "
            "Full-body character portrait of a fictional young Black/African woman transformed into a Pax tribe member — "
            "HUMANIZED style like Image 1. She keeps her natural dark brown human skin tone (NOT turquoise). "
            "She has ONE single large cyclops eye centered on her face "
            "(big, warm brown iris with black pupil and double specular highlight), NO nose or very subtle nose. "
            "Pointed elf ears. Short natural afro hair. "
            "Jade-turquoise geometric tribal tattoos across arms, shoulders and neck. "
            "Outfit: cream-and-purple tribal vest with geometric diamond embroidery, "
            "purple tribal bandana (#7A3FB2) with geometric patterns tied on forehead, "
            "violet crystal pendant necklace (#8A4DD1 glowing), bronze and bead bracelets on wrists, "
            "brown leather belt with crystal vials hanging, dark baggy pants, leather sandals. "
            "She holds a twisted wooden staff with a glowing violet crystal on top. "
            "Chibi proportions (3 heads tall). Warm smile. Plain light gray background."
        ),
    },
    {
        "name": "humanized-man-european.png",
        "refs": [REF_HUMANIZED_SINGLE],
        "prompt": (
            f"{STYLE_BLOCK} "
            "Full-body character portrait of a fictional young European man with light skin and red-auburn beard "
            "transformed into a Pax tribe member — HUMANIZED style like Image 1. "
            "He keeps his natural pale/fair human skin tone (NOT turquoise). "
            "He has ONE single large cyclops eye centered on his face "
            "(big, green iris with black pupil and double specular highlight), NO visible nose. "
            "Pointed elf ears poking through messy auburn hair. Short red beard. "
            "Jade-turquoise geometric tribal tattoos across arms and chest. "
            "Outfit: cream sleeveless tribal vest with purple geometric borders, "
            "purple tribal bandana (#7A3FB2) tied on forehead with geometric diamond patterns, "
            "violet crystal earring hanging from left ear, bronze bracelets, "
            "brown leather belt with crystal pendants, dark navy shorts, brown leather sandals. "
            "He carries a leather satchel bag on his hip. "
            "Chibi proportions (3 heads tall). Relaxed standing pose with one hand waving. "
            "Plain light gray background."
        ),
    },
    # --- CHARACTER SHEET (5 poses) ---
    {
        "name": "charsheet-woman-middle-eastern.png",
        "refs": [REF_HUMANIZED_SHEET],
        "prompt": (
            f"{STYLE_BLOCK} "
            "Character sheet with 5 poses of a fictional young Middle Eastern woman transformed into a Pax "
            "tribe member — HUMANIZED style like Image 1. Layout: top-left full body standing, "
            "top-right close-up portrait bust, bottom-left sitting cross-legged reading a book, "
            "bottom-center standing with staff, bottom-right running action pose. "
            "She keeps her natural olive/tan human skin tone (NOT turquoise). "
            "She has ONE single large cyclops eye centered on her face "
            "(big, dark brown iris with black pupil and double highlight), NO nose or very subtle. "
            "Pointed elf ears. Long black wavy hair flowing down. "
            "Jade-turquoise geometric tribal tattoos on arms and neck. "
            "Outfit: cream-and-purple tribal vest with geometric diamond embroidery, "
            "purple bandana (#7A3FB2) with geometric patterns on forehead, "
            "violet crystal pendant necklace (#8A4DD1 glowing), bronze bracelets, "
            "brown leather belt with crystal vials, dark baggy pants, leather sandals. "
            "Chibi proportions (3 heads tall). Warm expressions. Plain white background. "
            "All 5 poses show the SAME character with consistent design."
        ),
    },
    # --- BONUS: Full Pax character sheet ---
    {
        "name": "charsheet-full-pax-kid.png",
        "refs": [REF_HUMANIZED_SHEET, REF_FULL_PAX],
        "prompt": (
            f"{STYLE_BLOCK} "
            "Character sheet with 5 poses of a fictional young boy (about 10 years old) transformed into a Pax "
            "tribe member — FULL PAX style with turquoise jade mineral skin like Image 2. "
            "Layout: top-left full body standing, "
            "top-right close-up portrait bust, bottom-left sitting cross-legged reading a book, "
            "bottom-center standing with staff holding a glowing violet crystal, "
            "bottom-right running action pose. "
            "His skin is entirely jade-turquoise (#21D8B6) with subsurface scattering glow. "
            "He has ONE single large cyclops eye centered on his face "
            "(big, expressive, turquoise iris #3FE0C8 with black pupil and double highlight), "
            "NO nose, wide elastic mouth. Pointed elf ears. Short messy dark hair. "
            "Jade geometric tribal tattoos on arms. "
            "Outfit: cream tribal vest with purple geometric borders, leather harness, "
            "violet crystal pendant (#8A4DD1 emissive), brown leather belt with pouches, "
            "dark shorts, leather sandals. "
            "Chibi proportions (3 heads tall) like the character sheet layout in Image 1. "
            "Playful energetic expressions. Plain white background. "
            "All 5 poses show the SAME character with consistent design."
        ),
    },
]

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    for i, job in enumerate(jobs):
        out_path = os.path.join(OUT_DIR, job["name"])
        print(f"[{i+1}/{len(jobs)}] Generating {job['name']}...")
        try:
            edit_image(
                prompt=job["prompt"],
                input_image_paths=job["refs"],
                output_path=out_path,
                size="1024x1024",
                quality="medium",
            )
            print(f"  -> OK: {out_path}")
        except Exception as e:
            print(f"  -> ERROR: {e}")
    print("\nDone!")
