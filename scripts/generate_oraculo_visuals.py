"""
Oraculo Pax - generador de 8 imagenes top-prioridad (Variante D + Variante C).

Variante D - Glassmorphic Cinematic (RECOMENDADA como base del MVP):
- D1 hero shot         1536x1024
- D2 background texture 1024x1024
- D3 decorative element 1536x1024 (horizontal banner per .md)
- D4 card mockup        1024x1536

Variante C - Runic Pax Glow (FALLBACK Pax-canon):
- C1 hero shot         1536x1024
- C2 background texture 1024x1024
- C3 decorative element 1024x1024
- C4 card mockup        1024x1536

Output: content/pax-oraculo/visuals/{D,C}/{hero,texture,decorative,card}.png

Skip-if-exists (>50KB). Concurrency Semaphore=4. Retry-once en moderation/rate/500.
Prompts extraidos LITERALES de content/pax-oraculo/_variantes-visuales.md.
"""

import os
import sys
import time
import asyncio
import base64

from openai import AsyncOpenAI

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openai_images import _load_env  # noqa: E402
_load_env()

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = "gpt-image-2"
QUALITY = "high"
CONCURRENCY = 4

# Tamanos por tipo de asset (definidos por el .md de variantes)
SIZE_HERO = "1536x1024"       # horizontal hero
SIZE_TEXTURE = "1024x1024"    # square tileable
SIZE_DECO_SQUARE = "1024x1024"   # square decorative (C3)
SIZE_DECO_HORIZONTAL = "1536x1024"  # horizontal banner decorative (D3)
SIZE_CARD = "1024x1536"       # vertical card


# ---------------------------------------------------------------------------
# Data-driven: 8 prompts extraidos LITERALES de _variantes-visuales.md
# ---------------------------------------------------------------------------
PROMPTS = {
    # --- Variante D - Glassmorphic Cinematic ------------------------------
    "D": {
        "hero": {
            "size": SIZE_HERO,
            "prompt": (
                "A cinematic noir hero scene of a single Pax crystal floating in pitch-black void, "
                "the crystal slowly rotating, faceted translucent surface catching warm amber and "
                "coral key light from upper-right, golden volumetric mist drifting softly in the "
                "background, deep black negative space dominates 70% of the frame ready for "
                "editorial typography overlay, subtle film grain across the whole image.\n\n"
                "Composition: hero off-center crystal positioned on right third, vast negative "
                "space on left two-thirds for typography, 85mm equivalent lens for compressed "
                "cinematic feel, shallow depth of field with mist slightly out of focus.\n"
                "Lighting: single warm key light from upper-right at #F59E0B catching the crystal "
                "facets, secondary coral rim at #FF6B4A on the left edge of the crystal, deep "
                "occlusion at #08070A everywhere else, no fill light.\n"
                "Color palette: #08070A, #1A1820, #FF6B4A, #F59E0B, #F4EFE6, #B43FFF at 20% opacity in mist.\n"
                "Texture/Material: faceted translucent crystal with strong subsurface scattering, "
                "sharp specular highlights, golden volumetric mist with realistic density falloff, "
                "film grain at 10% intensity, NOT clean-digital, NOT cartoon.\n"
                "Style: cinematic noir photography aesthetic, premium editorial, NOT illustration, "
                "NOT cartoon, NOT high-key bright.\n"
                "Constraints: no on-screen text (left negative space is for future typography "
                "overlay), no logos, no copyrighted IP, no characters in this hero, deep black 70% of frame.\n\n"
                "Aspect ratio: 1536x1024 horizontal."
            ),
        },
        "texture": {
            "size": SIZE_TEXTURE,
            "prompt": (
                "Seamless tileable texture of deep black noir with subtle drifting golden mist "
                "particles, very low contrast, slight film grain overlay, occasional tiny warm "
                "light flecks at #F59E0B at very low intensity, evokes the inside of a dark "
                "cinematic chamber.\n\n"
                "Composition: flat top-down orthographic, no focal point, uniform across the frame, "
                "perfectly tileable on all edges.\n"
                "Lighting: ambient darkness at #08070A base with extremely subtle warm haze at "
                "#F59E0B at 5% intensity, no directional source.\n"
                "Color palette: #08070A, #1A1820, #F59E0B sparingly, #F4EFE6 tiny flecks.\n"
                "Texture/Material: volumetric mist particles, film grain, NOT high-contrast, NOT "
                "clearly visible features that would break tiling.\n"
                "Style: cinematic noir texture, premium subtle, NOT illustration, NOT photoreal-mundane.\n"
                "Constraints: must tile seamlessly on all edges, no focal subject, no readable text, "
                "no logos, very low frequency variation.\n\n"
                "Aspect ratio: 1024x1024 square."
            ),
        },
        "decorative": {
            "size": SIZE_DECO_HORIZONTAL,
            "prompt": (
                "A premium glassmorphic UI panel separator, a horizontal pane of frosted translucent "
                "glass with a single 1px ivory border, soft interior shadow, faint amber backlight "
                "glowing through from behind suggesting a Pax crystal source out of frame, subtle "
                "film grain overlay, deep noir background.\n\n"
                "Composition: horizontal banner, glass pane centered, deep black space above and "
                "below, the glow source implied from behind.\n"
                "Lighting: amber backlight at #F59E0B diffused through the frosted glass, coral "
                "accent at #FF6B4A at one edge, deep noir at #08070A surrounding.\n"
                "Color palette: #08070A, #1A1820, #FF6B4A, #F59E0B, #F4EFE6 border.\n"
                "Texture/Material: frosted glass with backdrop blur effect, 1px solid border, soft "
                "inner shadow, film grain overlay at 8%, NOT clear glass, NOT decorative-ornamental.\n"
                "Style: modern glassmorphic UI element, premium editorial, NOT skeuomorphic, NOT "
                "cartoon, NOT illustrated.\n"
                "Constraints: must function as a horizontal divider in a website, no readable text, "
                "no logos, geometric minimalist shape only.\n\n"
                "Aspect ratio: 1536x1024 horizontal (panel occupies central horizontal band)."
            ),
        },
        "card": {
            "size": SIZE_CARD,
            "prompt": (
                "A single Pax Oracle reading card as a premium vertical glassmorphic panel floating "
                "in noir space, frosted translucent glass with 1px ivory border, soft inner shadow, "
                "behind the glass a stylized 3D rendering of a small Pax cyclopean character with "
                "one large central eye holding a glowing amber crystal (the character is the only "
                "colorful element, everything else is dark), an editorial serif typography area at "
                "the top reserved for archetype name (currently empty placeholder), a thin coral "
                "horizontal accent line, subtle film grain across the whole composition.\n\n"
                "Composition: vertical portrait card centered in frame, the character occupies the "
                "central two-thirds of the card behind the glass, empty serif title area at top, "
                "accent line below the character, isolated on deep noir background with subtle mist.\n"
                "Lighting: warm amber key at #F59E0B from upper-right lighting the character, coral "
                "rim at #FF6B4A on character left edge, deep noir at #08070A everywhere else, the "
                "glass surface catches a single thin highlight at #F4EFE6.\n"
                "Color palette: #08070A, #1A1820, #FF6B4A, #F59E0B, #F4EFE6, #3DCCA3 subtle on character skin only.\n"
                "Texture/Material: frosted glass front surface with backdrop blur, faceted translucent "
                "crystal in character hands, character rendered as stylized 3D PBR, film grain "
                "overlay at 10%, NOT flat illustration, NOT cartoon-outlined.\n"
                "Style: cinematic premium editorial with glassmorphic UI overlay, stylized 3D "
                "character behind glass, NOT photoreal-mundane, NOT anime, NOT flat 2D.\n"
                "Constraints: no readable text (empty placeholder area at top), no logos, ONE single "
                "central eye on the Pax character (never two eyes), 3 fingers per hand, "
                "jade-turquoise skin, deep noir dominant.\n\n"
                "Aspect ratio: 1024x1536 vertical."
            ),
        },
    },
    # --- Variante C - Runic Pax Glow --------------------------------------
    "C": {
        "hero": {
            "size": SIZE_HERO,
            "prompt": (
                "A central Pax Oracle altar in a cavern chamber, a circular violet basalt pedestal "
                "with carved invented runes glowing from within in magenta and amber, three faceted "
                "translucent crystals (one violet, one magenta, one jade) suspended in mid-air above "
                "the pedestal rotating slowly, golden volumetric mist swirling at floor level, "
                "particles of warm light drifting through the air, cavern walls visible in deep "
                "violet basalt with smaller crystal clusters embedded.\n\n"
                "Composition: hero centered medium shot, 35mm equivalent, slight low angle "
                "suggesting reverence, the altar at center, the three suspended crystals at "
                "upper-third forming a triangle, cavern depth falling off into atmospheric haze.\n"
                "Lighting: primary inner glow from runes at #EC4899 and #F59E0B casting "
                "magenta-amber gradients onto the pedestal surface, secondary glow from the three "
                "crystals (#B43FFF, #EC4899, #3DCCA3) each casting their own colored light, "
                "volumetric god-rays of #FFE9C2 cutting through the mist from cavern ceiling.\n"
                "Color palette: #B43FFF, #EC4899, #F59E0B, #3DCCA3, #1E1E2E, #3A2845, #FFE9C2.\n"
                "Texture/Material: rough violet basalt for the pedestal and walls, polished facets "
                "on the floating crystals with subsurface scattering, golden mist with volumetric "
                "density, particles with soft bloom, NOT photoreal-mundane, NOT cartoon-flat.\n"
                "Style: stylized 3D PBR cinematic, neon-magical, painterly atmosphere, NOT "
                "cartoonish, NOT photoreal-cold, NOT anime, NOT flat illustration.\n"
                "Constraints: no on-screen text, no readable letters, only invented Pax runes "
                "glowing on the pedestal, no logos, no copyrighted IP, no characters visible in "
                "this hero shot (altar only).\n\n"
                "Aspect ratio: 1536x1024 horizontal."
            ),
        },
        "texture": {
            "size": SIZE_TEXTURE,
            "prompt": (
                "Seamless tileable texture of violet Pax basalt stone surface with subtle carved "
                "invented runes glowing faintly from within, low contrast, runes spaced organically "
                "across the surface, slight golden mist haze on top.\n\n"
                "Composition: flat top-down orthographic, perfectly even lighting for tiling, no "
                "focal point, uniform distribution of rune carvings.\n"
                "Lighting: ambient cool at #3A2845 base, internal rune glow at #EC4899 and #F59E0B "
                "at low intensity, no directional shadows.\n"
                "Color palette: #1E1E2E, #3A2845, #B43FFF subtle, #EC4899 subtle, #F59E0B subtle.\n"
                "Texture/Material: rough basalt with carved rune relief, glow contained within the "
                "carved grooves only, NOT polished, NOT high-contrast.\n"
                "Style: stylized 3D PBR seamless texture, magical-canon Pax, NOT cartoon, NOT "
                "photoreal, NOT high-contrast.\n"
                "Constraints: must tile seamlessly on all edges, no focal subject, runes are "
                "invented script only, no logos, low frequency variation.\n\n"
                "Aspect ratio: 1024x1024 square."
            ),
        },
        "decorative": {
            "size": SIZE_DECO_SQUARE,
            "prompt": (
                "A single Pax Oracle rune sigil floating in space, an invented circular glyph "
                "combining a central eye motif with surrounding crystal-shape strokes and curving "
                "tribal lines (echoing the tribal markings on Pax characters' skin), carved in "
                "violet basalt and glowing magenta-amber from within, faint golden mist drifting "
                "around it.\n\n"
                "Composition: square frame, sigil centered, isolated on dark gradient background, "
                "slight tilt to suggest the sigil floats forward toward viewer.\n"
                "Lighting: internal rune glow at #EC4899 and #F59E0B as primary source, rim light "
                "at #B43FFF on the stone edges, deep background at #1E1E2E.\n"
                "Color palette: #B43FFF, #EC4899, #F59E0B, #1E1E2E, #FFE9C2 highlight.\n"
                "Texture/Material: carved basalt stone with glowing interior, soft bloom around the "
                "glow, slight volumetric mist, NOT flat vector, NOT cartoon-outline.\n"
                "Style: stylized 3D PBR magical icon, cinematic, NOT 2D vector, NOT flat illustration.\n"
                "Constraints: must function as a UI icon, no readable text, ONE central eye motif "
                "inside the sigil, no logos, isolated on dark background.\n\n"
                "Aspect ratio: 1024x1024 square."
            ),
        },
        "card": {
            "size": SIZE_CARD,
            "prompt": (
                "A single Pax Oracle reading card as a vertical violet basalt slab with glowing "
                "magenta-amber runes, central illustration shows a small Pax cyclopean character "
                "with one large central eye sitting cross-legged on a small floating rock, the "
                "character holds a faceted magenta crystal that emits soft light onto their face, "
                "three smaller crystals (violet, magenta, jade) orbit slowly around the character, "
                "the card border is carved with invented Pax runes glowing softly, the bottom of "
                "the card has a darker recessed panel ready for an archetype name but currently empty.\n\n"
                "Composition: vertical portrait card centered in frame, slight three-quarter tilt "
                "to show depth, isolated on dark gradient background with subtle golden mist at the base.\n"
                "Lighting: primary glow from the central crystal in the character's hands at "
                "#EC4899 lighting the face from below, rim light from the orbiting crystals each "
                "in their own color, runes around the border glowing at #F59E0B, deep ambient at #1E1E2E.\n"
                "Color palette: #B43FFF, #EC4899, #F59E0B, #3DCCA3, #1E1E2E, #3A2845, #FFE9C2.\n"
                "Texture/Material: violet basalt slab with carved glowing rune border, faceted "
                "translucent crystals with subsurface scattering, the Pax character rendered as a "
                "small 3D figure embedded into or sitting on the card surface, soft volumetric mist, "
                "NOT flat illustration, NOT cartoon-outlined.\n"
                "Style: stylized 3D PBR cinematic Pax canon, neon-magical, NOT photoreal-cold, NOT "
                "anime, NOT flat 2D.\n"
                "Constraints: no readable text, only invented Pax runes, no logos, ONE single "
                "central eye on the Pax character (never two eyes), 3 fingers per hand, "
                "jade-turquoise skin, empty recessed panel at bottom for archetype name.\n\n"
                "Aspect ratio: 1024x1536 vertical."
            ),
        },
    },
}


# ---------------------------------------------------------------------------
# Generador async
# ---------------------------------------------------------------------------
async def gen_image(client, sem, variante, asset_type, prompt, size):
    """Genera 1 imagen via images.generate (concepts puros, sin refs)."""
    async with sem:
        out_dir = os.path.join(REPO, "content", "pax-oraculo", "visuals", variante)
        out_path = os.path.join(out_dir, f"{asset_type}.png")

        if os.path.exists(out_path) and os.path.getsize(out_path) > 50_000:
            print(f"SKIP {variante}/{asset_type}.png")
            return ("SKIP", out_path)

        os.makedirs(out_dir, exist_ok=True)

        for attempt in range(2):
            try:
                t0 = time.time()
                result = await client.images.generate(
                    prompt=prompt,
                    model=MODEL,
                    size=size,
                    quality=QUALITY,
                    n=1,
                )
                b64 = result.data[0].b64_json
                with open(out_path, "wb") as f:
                    f.write(base64.b64decode(b64))
                elapsed = time.time() - t0
                kb = os.path.getsize(out_path) // 1024
                print(
                    f"OK  [{time.strftime('%H:%M:%S')}] "
                    f"{variante}/{asset_type} - {elapsed:.1f}s - {kb}KB"
                )
                return ("OK", out_path)
            except Exception as e:
                msg = str(e)[:200]
                retryable = any(
                    x in msg.lower()
                    for x in ("moderation", "rate", "500", "timeout", "server")
                )
                if attempt == 0 and retryable:
                    print(f"RETRY {variante}/{asset_type}: {msg}")
                    await asyncio.sleep(2)
                    continue
                print(f"FAIL {variante}/{asset_type}: {msg}")
                return ("FAIL", msg)


async def main():
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
    sem = asyncio.Semaphore(CONCURRENCY)

    tasks = []
    for variante, assets in PROMPTS.items():
        for asset_type, data in assets.items():
            tasks.append(
                gen_image(
                    client,
                    sem,
                    variante,
                    asset_type,
                    data["prompt"],
                    data["size"],
                )
            )

    print(f"Lanzando {len(tasks)} generaciones (target: 8 = 4 D + 4 C)...")
    t_start = time.time()
    results = await asyncio.gather(*tasks, return_exceptions=True)
    elapsed_total = time.time() - t_start

    ok = sum(1 for r in results if isinstance(r, tuple) and r[0] == "OK")
    skip = sum(1 for r in results if isinstance(r, tuple) and r[0] == "SKIP")
    fail = sum(1 for r in results if isinstance(r, tuple) and r[0] == "FAIL")
    print("=" * 70)
    print(
        f"RESUMEN: OK={ok} SKIP={skip} FAIL={fail} "
        f"TOTAL={len(tasks)} - {elapsed_total:.1f}s"
    )
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())
