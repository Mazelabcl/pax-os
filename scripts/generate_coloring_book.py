"""
Genera 12 paginas de coloring book Pax usando gpt-image-2.
Estilo: line art B&N, outlines gruesos, sin sombreado, fondo blanco.
Formato: 8.5x11 vertical (1024x1536).

Uso:
    python scripts/generate_coloring_book.py
"""

import os
import sys

# Agregar raiz del repo al path para importar openai_images
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.openai_images import generate_image

OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "gestos", "_backlog", "coloring-book", "pages",
)

STYLE_PREFIX = (
    "Black and white line art coloring book page for children and adults. "
    "Thick clean black outlines on pure white background. No shading, no color, "
    "no gray tones, no crosshatching. Simple clear shapes ready to color. "
    "Style reference: classic coloring book with bold outlines. "
)

PAGES = [
    # --- 4 personajes individuales ---
    {
        "filename": "01-jiggy-cristal.png",
        "prompt": (
            STYLE_PREFIX
            + "A playful cyclops character named Jiggy: short, stocky humanoid with ONE large eye, "
            "slightly unbalanced posture (about to trip), mischievous grin. He is running through "
            "a crystal cavern holding a glowing crystal above his head triumphantly. Stalactites and "
            "stalagmites surround him. Decorative border with small crystals in the corners."
        ),
    },
    {
        "filename": "02-wiz-meditando.png",
        "prompt": (
            STYLE_PREFIX
            + "An elderly wise cyclops character named Wiz: short, round body, ONE large deep eye, "
            "long mineral beard, wearing a flowing cloak. He sits cross-legged meditating peacefully "
            "surrounded by floating crystals arranged in a circle around him. Underground cavern "
            "background with crystal formations. Decorative border with ancient runes."
        ),
    },
    {
        "filename": "03-kz-inventando.png",
        "prompt": (
            STYLE_PREFIX
            + "A young clumsy-genius cyclops character named KZ: small, ONE big curious eye, messy "
            "appearance, surrounded by gadgets and crystal contraptions. He is tinkering with a "
            "crystal-powered device, tools scattered around, sparks flying. Underground workshop "
            "setting with shelves of crystals and inventions. Decorative border with gears and crystals."
        ),
    },
    {
        "filename": "04-fortis-protector.png",
        "prompt": (
            STYLE_PREFIX
            + "A strong protective cyclops character named Fortis: broad shoulders, muscular build, "
            "ONE determined eye, basalt-dark skin tone (shown as thicker outlines). He stands in a "
            "heroic pose shielding a tiny baby cyclops (Baba) who peeks from behind his leg. Crystal "
            "cavern background. Decorative border with shield and crystal motifs."
        ),
    },
    # --- 3 escenas del lore (templo, cristales, tribu) ---
    {
        "filename": "05-templo-olvidado.png",
        "prompt": (
            STYLE_PREFIX
            + "A grand forgotten underground temple scene: massive ancient stone archway covered in "
            "crystal formations and vines. A small cyclops character (Jiggy) stands at the entrance "
            "looking up in awe, dwarfed by the enormous structure. Ancient carved symbols on the walls. "
            "Large crystals growing from the floor emit light patterns. Mysterious and magical atmosphere. "
            "Decorative border with ancient temple motifs."
        ),
    },
    {
        "filename": "06-cristales-cargando.png",
        "prompt": (
            STYLE_PREFIX
            + "A collection of magical crystals in various shapes and sizes: tall pointed crystals, "
            "round cluster crystals, hexagonal columns, all arranged in a beautiful underground garden. "
            "Energy lines flow between the crystals showing them charging. Small decorative plants and "
            "mushrooms grow around the crystal bases. Mandala-style circular composition. "
            "Decorative border with crystal and vine patterns."
        ),
    },
    {
        "filename": "07-tribu-reunida.png",
        "prompt": (
            STYLE_PREFIX
            + "Seven cyclops characters gathered in a circle inside a crystal cavern: one wise old one "
            "with a beard (Wiz), one playful mischievous one (Jiggy), one with headphones and tech "
            "accessories (Byte), one joyful dancing one (Luxa), one strong broad-shouldered one (Onyx), "
            "one calm centered one (Agatha), one with a boombox (Zek). They all have ONE large eye each. "
            "A large central crystal glows between them. Decorative tribal border."
        ),
    },
    # --- 3 escenas del mundo de arriba (humanos + bondad + cristales) ---
    {
        "filename": "08-ayni-cafe.png",
        "prompt": (
            STYLE_PREFIX
            + "A heartwarming scene in a coffee shop: a kind person buying coffee for the person behind "
            "them in line. Below the floor (shown in cross-section), underground crystals pulse with "
            "energy responding to this act of kindness. The scene is split: top half shows the real world "
            "coffee shop, bottom half shows the underground crystal world. Hearts and kindness symbols. "
            "Decorative border with coffee cups and crystals."
        ),
    },
    {
        "filename": "09-ayni-playa.png",
        "prompt": (
            STYLE_PREFIX
            + "A beach cleanup scene: children and adults picking up trash from a beautiful beach. Below "
            "the sand (shown in cross-section), underground crystals glow brightly responding to this "
            "environmental kindness. Sea turtles and fish swim nearby. The scene splits between the sunny "
            "beach above and the magical crystal cavern below. Decorative border with waves and crystals."
        ),
    },
    {
        "filename": "10-ayni-ensenando.png",
        "prompt": (
            STYLE_PREFIX
            + "A teaching scene: a person sitting with a child, teaching them to read from a book under "
            "a big tree. Below the ground (shown in cross-section), underground crystals pulse with "
            "warm energy. A small cyclops character peeks from behind the tree trunk, watching with "
            "ONE large happy eye. Butterflies and flowers surround them. "
            "Decorative border with books, pencils and crystals."
        ),
    },
    # --- Portada ---
    {
        "filename": "00-portada.png",
        "prompt": (
            STYLE_PREFIX
            + "COVER PAGE for a coloring book titled 'PAX TRIBE - Crystal Keepers of Equilibrium'. "
            "Five cyclops characters arranged around a large central glowing crystal: one playful (Jiggy) "
            "at front, one wise with beard (Wiz) at back, one with headphones (Byte) on left, one strong "
            "(Fortis) on right, one joyful (Luxa) on top. All have ONE large eye. Underground crystal "
            "cavern background. The title 'PAX TRIBE' in large bold decorative letters at top, subtitle "
            "'Crystal Keepers of Equilibrium' below. Ornate decorative border with crystals and tribal patterns."
        ),
    },
    # --- Contraportada ---
    {
        "filename": "11-mapa-uray-pacha.png",
        "prompt": (
            STYLE_PREFIX
            + "BACK COVER: A fantasy map of the underground world called 'Uray Pacha'. Bird's eye view "
            "showing interconnected underground tunnels, crystal caverns, the forgotten temple, crystal "
            "gardens, the tribe's gathering hall, and vertical shafts connecting to the surface world above. "
            "Map style with labeled areas: 'Templo Olvidado', 'Jardin de Cristales', 'Gran Caverna'. "
            "Compass rose in corner. Small cyclops characters placed at various locations on the map. "
            "Title 'MAPA DEL URAY PACHA' at top in decorative letters. Ornate map border."
        ),
    },
]


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    total = len(PAGES)
    for i, page in enumerate(PAGES, 1):
        out_path = os.path.join(OUTPUT_DIR, page["filename"])
        if os.path.exists(out_path):
            print(f"[{i}/{total}] Ya existe, saltando: {page['filename']}")
            continue
        print(f"[{i}/{total}] Generando: {page['filename']}...")
        try:
            generate_image(
                prompt=page["prompt"],
                output_path=out_path,
                size="1024x1536",  # vertical 8.5x11 ratio
                quality="medium",
            )
            print(f"  -> OK: {out_path}")
        except Exception as e:
            print(f"  -> ERROR: {e}")
    print("\nGeneracion completa.")


if __name__ == "__main__":
    main()
