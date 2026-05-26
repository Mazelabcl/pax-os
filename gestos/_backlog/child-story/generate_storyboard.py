"""
Genera las 7 páginas del storyboard para el gesto "Child Story with Pax".
Usa un niño ejemplo inventado (~7 años, genérico).
Estilo: 3D Pixar/DreamWorks cálido, paleta Pax.
"""
import os
import sys

# Add repo root to path so we can import the shared module
repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, repo_root)

from scripts.openai_images import generate_image

OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "storyboard")
os.makedirs(OUTDIR, exist_ok=True)

STYLE_BLOCK = (
    "Style: stylized 3D animation similar to Pixar and DreamWorks quality, "
    "warm cinematic lighting, semi-realistic PBR shading with subsurface scattering, "
    "expressive cartoon proportions, high-contrast neon-magic lighting with "
    "magenta #E83FC8, cyan #2EE0C8, warm gold #FFE34D accents, "
    "saturated emissive crystals with bloom, painterly volumetric backgrounds "
    "with dense dust motes and god rays, slight film grain, 16:9 composition. "
    "Characters are small cyclops beings (one large eye, green-turquoise skin, "
    "3-3.5 head proportions, tribal clothing with purple geometric patterns). "
    "The child character is a human boy around 7 years old with brown skin, "
    "dark curly hair, wearing a red hoodie and jeans — warm and relatable. "
    "Setting is the Uray Pacha: vast underground caverns with glowing crystals, "
    "basalt walls, luminous roots, and mineral formations. "
    "Mood: warm, magical, hopeful, child-friendly but not childish. "
    "Negative: photorealistic, anime, 2D, cel-shaded, horror, dark, scary, violent."
)

PAGES = [
    {
        "filename": "pag1-llegada.png",
        "prompt": (
            f"{STYLE_BLOCK} "
            "Scene: A 7-year-old boy with brown skin and dark curly hair, wearing a red hoodie, "
            "floating gently downward through a crack in the earth into a vast underground cavern. "
            "He is seen from behind, arms slightly outstretched, looking down in wonder. "
            "Below him: a spectacular cavern filled with glowing magenta and cyan crystals, "
            "luminous roots weaving through basalt walls, god rays pouring from the crack above. "
            "Dust motes and crystal particles sparkle in the air. The mood is pure wonder and discovery. "
            "Wide shot, cinematic composition."
        ),
    },
    {
        "filename": "pag2-jiggy-kz.png",
        "prompt": (
            f"{STYLE_BLOCK} "
            "Scene: Inside the Uray Pacha cavern. A small green-turquoise cyclops character named Jiggy "
            "(one big eye, purple bandana, mischievous grin, tribal vest with geometric patterns, always "
            "looks like he is about to trip) is jumping excitedly toward a 7-year-old human boy with brown skin "
            "and dark curly hair wearing a red hoodie. Behind Jiggy, another smaller cyclops named KZ peeks "
            "shyly from behind a glowing crystal formation. The boy looks amazed, a small smile forming. "
            "Warm magenta and cyan crystal light illuminates the scene. Medium shot, eye-level with the boy."
        ),
    },
    {
        "filename": "pag3-cristal-enfermo.png",
        "prompt": (
            f"{STYLE_BLOCK} "
            "Scene: A circular underground chamber with stalactites and stalagmites made of crystal. "
            "In the center stands a large crystal (as tall as a 7-year-old child) that is flickering weakly — "
            "its magenta glow is dim, fading, with irregular pulses like a dying heartbeat. "
            "On one side: Jiggy (green-turquoise cyclops with purple bandana) looking worried, scratching his head. "
            "KZ (smaller cyclops) holds a tiny crystal, looking anxious. The human boy in red hoodie stands "
            "facing the big crystal, expression of empathy and concern. The atmosphere is tense but not dark — "
            "surrounding crystals still glow softly. Volumetric dust in the air."
        ),
    },
    {
        "filename": "pag4-superpoder.png",
        "prompt": (
            f"{STYLE_BLOCK} "
            "Scene: Intimate moment. A 7-year-old boy with brown skin and dark curly hair in a red hoodie "
            "stands close to a large dim crystal in an underground chamber. He places both hands gently on "
            "the crystal surface, eyes closed, with a brave and tender expression. A tiny spark of warm golden "
            "light begins to bloom inside the crystal where his hands touch it. Behind him, Jiggy (green cyclops "
            "with purple bandana) and KZ (smaller cyclops) watch with wide-eyed surprise, mouths open. "
            "The spark illuminates the boy's face with a soft magenta-gold glow. Close-medium shot, "
            "focused on the emotional connection between boy and crystal."
        ),
    },
    {
        "filename": "pag5-cristal-despierta.png",
        "prompt": (
            f"{STYLE_BLOCK} "
            "Scene: THE BIG MOMENT. The large crystal in the center of the underground chamber is now fully "
            "alive and radiant — blazing with deep magenta, cyan sparks, and waves of golden light that climb "
            "the cavern walls like living roots. The 7-year-old boy in red hoodie stands before it, bathed in "
            "brilliant light, arms slightly raised, face full of awe and joy. Jiggy (green cyclops) is jumping "
            "and celebrating behind him. KZ is bouncing with happiness. Brilliant particles and crystal dust "
            "float everywhere. The whole cavern is lit up like a festival. Epic magical atmosphere. "
            "Wide-medium shot showing the full spectacle."
        ),
    },
    {
        "filename": "pag6-celebracion.png",
        "prompt": (
            f"{STYLE_BLOCK} "
            "Scene: A grand celebration inside a wide Uray Pacha cavern. Multiple Pax cyclops characters are "
            "dancing and celebrating. The 7-year-old human boy in red hoodie dances with Jiggy (green cyclops "
            "with purple bandana). Surrounding them: Wiz (an elderly golden-amber cyclops with mineral beard, "
            "smiling wisely), Byte (cyclops with lime-green LED headphones), Luxa (purple cyclops laughing hard), "
            "Onyx (large dark basalt cyclops with orange veins, arms crossed but smiling). Crystals all around "
            "the cavern pulse rhythmically like party lights in magenta, cyan, and gold. The atmosphere is pure "
            "joy, warmth, and community. Wide shot showing the full celebration."
        ),
    },
    {
        "filename": "pag7-recuerdo.png",
        "prompt": (
            f"{STYLE_BLOCK} "
            "Scene: Split composition. TOP HALF: A 7-year-old boy with brown skin and curly dark hair lies in "
            "his bed at night in a cozy bedroom. He holds a small glowing crystal (marble-sized) in his open "
            "palm, looking at it with a peaceful, wonder-filled smile. The crystal casts a soft magenta-cyan "
            "glow on his face and the bedsheets. BOTTOM HALF (or subtly visible below, like through the floor): "
            "Jiggy and KZ in the Uray Pacha look upward with warm smiles, bathed in crystal light. "
            "The mood is emotional, hopeful, a warm goodbye. Soft lighting, intimate close-medium shot. "
            "The small crystal connects both worlds visually."
        ),
    },
]


if __name__ == "__main__":
    for i, page in enumerate(PAGES, 1):
        outpath = os.path.join(OUTDIR, page["filename"])
        print(f"Generando pagina {i}/7: {page['filename']}...")
        try:
            generate_image(
                prompt=page["prompt"],
                output_path=outpath,
                size="1536x1024",  # horizontal / landscape for book pages
                quality="medium",
            )
            print(f"  OK -> {outpath}")
        except Exception as e:
            print(f"  ERROR: {e}")
    print("Done.")
