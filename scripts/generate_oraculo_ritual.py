"""
Genera 1 imagen: "Ritual de los místicos Pax"
1536x1024 horizontal, GPT Image 2, quality=high.

Concepto: caverna Pax nocturna, Wiz + Kif + 2-3 ancianos Pax
leyendo cartas talladas y cristales flotantes sobre una mesa de piedra,
constelacion proyectada en el techo. Paleta canon jade+violet+magenta+dorado.

Output dual:
  - public/images/oraculo-v3/ritual-misticos-pax.png
  - content/pax-oraculo/visuals/v3/ritual-misticos-pax.png
"""

import os
import sys
import time
import asyncio
import base64
import shutil

from openai import AsyncOpenAI

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openai_images import _load_env  # noqa: E402
_load_env()

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = "ritual-misticos-pax"

OUT_PATHS = [
    os.path.join(REPO, "public", "images", "oraculo-v3", f"{SLUG}.png"),
    os.path.join(REPO, "content", "pax-oraculo", "visuals", "v3", f"{SLUG}.png"),
]

PROMPT = """
A wide horizontal cinematic scene inside a Pax clan cavern at night,
rendered in stylized 3D PBR Pax-canon style (jade, violet, magenta, gold palette).

Scene: 4 to 5 Pax elders gathered around a circular stone table performing a
mystical reading ritual. The elders are ancient Pax beings — each with ONE single
large central eye (IDENTITY LOCK: exactly one eye per character, never two, never
side-by-side eyes — a single cyclopean eye centered in the face), teal-jade skin,
long white flowing beards on at least two of them, ceremonial robes in deep violet
and purple with golden embroidered trim. Two of the figures closely resemble:
- An elder wise Pax (Wiz-type): short and stout, large single central eye with
  golden amber iris, long white beard, holding a tall crystal staff topped with a
  glowing violet crystal, wearing a deep violet-purple hooded robe with ornate golden
  geometric patterns, pointed ears.
- A mystic Pax (Kif-type): slightly taller, large single central eye, flowing white
  beard, wearing layered ceremonial robes in dark violet and brown leather trim,
  holding a carved stone tablet with glowing runes.
The other 2-3 elders are variations — same cyclopean anatomy, different robes,
different details (one has amber-tipped crystal earrings, one holds a glowing crystal
orb, one traces glowing rune patterns in the air with a finger).

The stone table:
- Circular, carved from dark organic basalt with bioluminescent jade veins running
  through it.
- On the table surface: 5-7 stone tablets carved with Mayan-inspired + astrological
  rune symbols, the carvings glow faint magenta from within.
- 4-6 violet-magenta faceted crystals floating a few inches above the table surface,
  slowly rotating, emitting soft glow onto the elders' faces.
- A faint holographic star-constellation projected upward from the center of the
  table, reaching the cavern ceiling.

The cavern:
- Underground night ambiance, dome-shaped cavern ceiling with glowing crystal needles
  embedded in the walls.
- The cavern ceiling shows a projected constellation map in gold-amber light,
  swirling above the table.
- Stalactites of violet-basalt with bioluminescent jade tips frame the upper edges.
- Deep noir background — #08070A — fading to deep violet at the periphery.

Composition: horizontal wide shot, all 4-5 figures seated/standing around the central
table in roughly equal spacing, the table is the focal center of the frame, medium
shot showing figures from waist up clearly, slight cinematic depth of field softening
the edges and background.

Lighting:
- Primary: warm golden key light #D4A857 from the constellation above, casting
  dramatic top-down illumination on the table and elders.
- Secondary: violet-magenta glow #B43FFF from the floating crystals creating soft
  colored fill on faces and robes.
- Rim: jade-turquoise #3DCCA3 from bioluminescent cavern walls, outlining the figures.
- Deep ambient occlusion #08070A in the background and cavern floor.

Color palette canon:
#B43FFF (violet crystals), #EC4899 (magenta glyph glow), #3DCCA3 (jade skin and
rim), #D4A857 (dorado constellation light), #F59E0B (amber accents), #1E1E2E
(basalt surfaces), #08070A (deep noir background), #F4EFE6 (white beard highlights).

Style: stylized 3D PBR painterly cinematic, Pax-canon animation quality
(think Pixar/DreamWorks quality but neon-magic sacred), NOT photoreal-mundane,
NOT cartoon-flat, NOT anime. Solemn, mystical, alchemical atmosphere — this is a
council of mages reading destiny over a stone table, not spooky, but ceremonial
and warm.

ABSOLUTE CONSTRAINTS:
- Every Pax character has EXACTLY ONE single large central eye. No exceptions.
  Never two eyes, never two eye sockets. ONE eye per face, centered.
- 3 fingers per hand (canonical Pax anatomy).
- Teal-jade skin on all Pax characters.
- No readable text or logos.
- Horizontal aspect ratio 1536x1024.
- The atmosphere is solemn-mystical-alchemical, NOT horror, NOT dark fantasy,
  NOT menacing.

Aspect ratio: 1536x1024 horizontal.
""".strip()


async def generate():
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

    # Crear directorios si no existen
    for out_path in OUT_PATHS:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)

    primary = OUT_PATHS[0]

    # Skip si ya existe y es grande
    if os.path.exists(primary) and os.path.getsize(primary) > 50_000:
        kb = os.path.getsize(primary) // 1024
        print(f"SKIP {SLUG}.png ya existe ({kb}KB)")
        return primary

    print(f"Generando {SLUG}.png — quality=high 1536x1024...")
    t0 = time.time()

    result = await client.images.generate(
        prompt=PROMPT,
        model="gpt-image-2",
        size="1536x1024",
        quality="high",
        n=1,
    )

    b64 = result.data[0].b64_json
    with open(primary, "wb") as f:
        f.write(base64.b64decode(b64))

    elapsed = time.time() - t0
    kb = os.path.getsize(primary) // 1024
    print(f"OK  [{time.strftime('%H:%M:%S')}] {SLUG}.png — {elapsed:.1f}s — {kb}KB")

    # Copiar al segundo destino
    shutil.copy2(primary, OUT_PATHS[1])
    print(f"Copiado a: {OUT_PATHS[1]}")

    return primary


if __name__ == "__main__":
    asyncio.run(generate())
