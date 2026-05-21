"""
Bulk canon visual v2 — 6 personajes principales (KZ, Luxa, Agatha, Byte, Onyx, Wiz).

Genera 36 imagenes (6 personajes x 3 variaciones x 2 sheets = 36).

Fases:
1. Paralelo (Semaphore 4): 18 simples (6 chars x 3 variaciones)
2. Paralelo (Semaphore 4): 18 completas (6 chars x 3 variaciones, cada una usa su simple)

Variaciones por personaje:
- V1 (fix-actual)   : edit con template + char actual <x>.png
- V2 (jiggy-base)   : edit con template + jiggy.png (transformar a otro personaje)
- V3 (from-scratch) : generate text-only (sin ref), identity lock triplicado
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
CONCURRENCY = 4

TEMPLATE_SIMPLE = os.path.join(REPO, "Personajes-Fix", "Character-Sheet-Simple.webp")
TEMPLATE_DETAIL = os.path.join(REPO, "Personajes-Fix", "Character-Sheet-Detail.jpg")
JIGGY_REF = os.path.join(REPO, "public", "images", "personajes", "jiggy.png")
CHAR_REF_DIR = os.path.join(REPO, "public", "images", "personajes")


# ---------------------------------------------------------------------------
# Canon v2 per character (data-driven so we can templatize all prompts)
# ---------------------------------------------------------------------------

CHARS = {
    "kz": {
        "name": "KZ",
        "ref": os.path.join(CHAR_REF_DIR, "kz.png"),
        "identity_lock": (
            "- Short spiky hedgehog-style hair (NOT long dreadlocks, NOT purple — short and spiky)\n"
            "- Disproportionately HUGE feet, much larger than normal Pax feet — silhouette icon\n"
            "- Ears noticeably LARGER than other Pax tribe members\n"
            "- Separated teeth with imperfect childish smile\n"
            "- Bracelets made of small teeth and stones on both wrists\n"
            "- Tiny tribal mini-tattoos painted 'by hand' (imperfect, childlike — not elaborate)\n"
            "- Small crystals stuck onto clothes and a small backpack\n"
            "- Smaller body scale (he is the youngest of the tribe)\n"
            "- Color palette: turquoise skin #2BC8C8 base, orange accents #FF8A3D, lime green highlights #BFFF4D, leather-brown #5A3A1F, white highlights #F0F0F0, deep accent #0D0D14"
        ),
        "default_expression": "open big joyful smile with separated teeth visible, energetic chaotic eye expression, wide grin",
        "signature_pose": "running wild and tripping over his own giant feet, mouth wide open laughing, arms flailing for balance",
        "palette_swatches": "#2BC8C8 turquoise, #FF8A3D orange, #BFFF4D lime, #5A3A1F leather-brown, #F0F0F0 white, #0D0D14 deep-accent",
        "details_strip": "- Tooth-and-stone bracelet flat\n- Small backpack with stuck crystals\n- Childlike tribal tattoo close-up\n- Huge bare foot detail (silhouette icon)",
    },
    "luxa": {
        "name": "LUXA",
        "ref": os.path.join(CHAR_REF_DIR, "luxa.png"),
        "identity_lock": (
            "- Central single eye noticeably LARGER and brighter than other Pax tribe members — luminous gleaming eye\n"
            "- Subtle body aura — a faint luminous halo visible around the entire body silhouette\n"
            "- Hair like soft luminous glowing fibers, flowing softly as if suspended in water\n"
            "- Crystals growing ORGANICALLY out of accessories (sprouting like plants from cuffs and neck — NOT just embedded)\n"
            "- Soft long tunic with luminous flowing patterns\n"
            "- Necklace of mineral seeds\n"
            "- Delicate tribal face paint, fine soft lines\n"
            "- NO bandana (do not confuse her with Jiggy)\n"
            "- NO lamp or external light source — the light EMANATES from her body\n"
            "- Color palette: soft turquoise #6FE0E0 skin base, pink #FFB3C7 accents, lavender #B89DE6 highlights, light leather #C9A77E, white highlights #FFFFFF, deep accent #2C1A45"
        ),
        "default_expression": "open big gentle smile, dreamy serene eye, joyful but peaceful",
        "signature_pose": "floating meditation pose, legs crossed mid-air, both hands raised palms-up with small crystals orbiting around them, aura glowing",
        "palette_swatches": "#6FE0E0 turquoise-soft, #FFB3C7 pink, #B89DE6 lavender, #C9A77E light-leather, #FFFFFF white, #2C1A45 deep-accent",
        "details_strip": "- Sprouting crystal detail (growing organically from a cuff)\n- Mineral seed necklace\n- Luminous hair-fiber detail close-up\n- Body aura halo example",
    },
    "agatha": {
        "name": "AGATHA",
        "ref": os.path.join(CHAR_REF_DIR, "agatha.png"),
        "identity_lock": (
            "- Adult Pax cyclops, sharp expressive single central eye (NOT round baby-eye — almond-shaped, focused)\n"
            "- Upright dignified posture, powerful even at rest\n"
            "- Long ritual braids — multiple decorated braids along the back of her head (silhouette icon)\n"
            "- Large mineral earrings made of carved minerals hanging from pointed ears\n"
            "- Short ceremonial cape draped over shoulders (NOT a long witch-tunic — a short ritual cape)\n"
            "- Elaborate luminous tribal tattoos covering arms — the most worked of the whole tribe\n"
            "- Crystals embedded into bracelets on both wrists\n"
            "- Color palette: deep turquoise skin #1F8A8A base, purple #5B2C82 accents, mineral gold #C9A14A highlights, bronze accent #7A4A1E, warm white highlights #F8E9C4, deep accent #1A0E2E"
        ),
        "default_expression": "serene confident closed-lip smile, dignified eye gaze, calm spiritual leader expression",
        "signature_pose": "standing tall with arms crossed, ceremonial short cape flaring slightly behind her, tribal tattoos glowing softly, sharp gaze forward",
        "palette_swatches": "#1F8A8A turquoise-deep, #5B2C82 purple, #C9A14A mineral-gold, #7A4A1E bronze, #F8E9C4 warm-white, #1A0E2E deep-accent",
        "details_strip": "- Mineral earring close-up\n- Ritual braid detail\n- Elaborate luminous tribal tattoo close-up\n- Crystal bracelet close-up",
    },
    "byte": {
        "name": "BYTE",
        "ref": os.path.join(CHAR_REF_DIR, "byte.png"),
        "identity_lock": (
            "- Single central eye visible BEHIND artisan mineral glasses (round mineral-lens spectacles, hand-crafted look)\n"
            "- Mineral glasses are his SILHOUETTE ICON — must be visible in every panel\n"
            "- Hair tied up / orderly (a small knot or back ponytail)\n"
            "- 2 to 4 small crystals ORBITING around his head and shoulders (floating, slowly rotating)\n"
            "- GEOMETRIC tribal tattoos (sharp angles, grid patterns — NOT organic like the rest of the tribe)\n"
            "- Tribal-mineral mechanical accessories: small gears, mineral-tech bracelet, gadget pouch\n"
            "- Pockets and a belt-bag full of small tools and crystal-mineral tech\n"
            "- NO laptop, NO modern headphones, NO modern earbuds — only tribal-mineral hand-crafted tech\n"
            "- Color palette: turquoise #2BC8C8 skin base, electric blue #2E7DFF accents, copper #C97D3A highlights, bronze accent #7A4A1E, pale blue-white highlights #E0F0FF, deep accent #0A1428"
        ),
        "default_expression": "curious nervous slightly open mouth half-smile, eager fascinated single eye behind glasses, eyebrow-equivalent raised",
        "signature_pose": "crouched fixing a small tribal-mineral gadget held between three-fingered hands, glasses pushed up to forehead, 3 crystals orbiting his head",
        "palette_swatches": "#2BC8C8 turquoise, #2E7DFF electric-blue, #C97D3A copper, #7A4A1E bronze, #E0F0FF pale-blue-white, #0A1428 deep-accent",
        "details_strip": "- Mineral glasses close-up (icon)\n- Orbiting crystal cluster\n- Geometric tribal tattoo pattern\n- Tribal-mineral gadget detail",
    },
    "onyx": {
        "name": "ONYX",
        "ref": os.path.join(CHAR_REF_DIR, "onyx.png"),
        "identity_lock": (
            "- Pax cyclops MUCH more muscular and physically larger than other Pax — broad shoulders, thick arms, robust torso\n"
            "- Visible battle scars across face, arms and chest (one diagonal scar across the cheek next to the central eye is signature)\n"
            "- Small VISIBLE fangs poking from the mouth corners (silhouette icon)\n"
            "- Short cropped or partly shaved hair\n"
            "- DARK BLACK crystals embedded into armor and bracers (unique in the tribe — only Onyx uses black crystals)\n"
            "- Mineral armor on shoulders and chest\n"
            "- DARK OPAQUE tribal markings on skin — NOT luminous like the other Pax — matte black-grey war paint\n"
            "- Heavy bracers and gauntlets with embedded black crystals\n"
            "- Color palette: dark turquoise #1A6B6B skin base, mineral black #16161E armor, magma red #D43A1F accent, old bronze #5A3520 leather, tooth-white #E0DCC9 fangs and highlights, deep accent #050808"
        ),
        "default_expression": "determined intense focused look, mouth closed firm or in slight snarl with fangs barely showing, warrior gaze locked forward — NEVER a wide smile",
        "signature_pose": "battle stance with one fist raised forward and the other clenched at hip, body angled in combat readiness, armor visible, dark tribal war marks across torso, intense focused gaze",
        "palette_swatches": "#1A6B6B turquoise-dark, #16161E mineral-black, #D43A1F magma-red, #5A3520 old-bronze, #E0DCC9 tooth-white, #050808 deep-accent",
        "details_strip": "- Black crystal embedded in bracer\n- Heavy gauntlet detail\n- Face scar close-up\n- Dark opaque tribal war mark pattern",
    },
    "wiz": {
        "name": "WIZ",
        "ref": os.path.join(CHAR_REF_DIR, "wiz.png"),
        "identity_lock": (
            "- Elder Pax cyclops — single tired expressive central eye with droopy eyelid and visible wrinkles around it\n"
            "- Smaller body scale, slightly stooped/hunched posture\n"
            "- Long FLOATING WHITE BEARD — the beard floats softly around his face as a magical effect, NOT hanging straight down (silhouette icon)\n"
            "- Carved root staff with a glowing crystal at the tip (silhouette icon)\n"
            "- Long ceremonial tunic with multiple small crystals embedded along the fabric\n"
            "- Old aged turquoise skin with subtle wrinkles\n"
            "- Color palette: aged turquoise #6B9E9E skin base, dark violet #3C2A5C robe accents, bright white #F8F8F8 beard, aged leather #5A4628, old amber #B58A4A crystal glow, deep accent #1A1228"
        ),
        "default_expression": "serene wise gaze, slight gentle grandfather smile, melancholic eye with a tiny sparkle of wisdom — NEVER a wide joyful smile",
        "signature_pose": "leaning on his root-and-crystal staff with one hand, other hand raised palm-up with a small floating crystal, white beard floating softly, central eye closed in meditation",
        "palette_swatches": "#6B9E9E turquoise-aged, #3C2A5C dark-violet, #F8F8F8 white, #5A4628 aged-leather, #B58A4A old-amber, #1A1228 deep-accent",
        "details_strip": "- Root-and-crystal staff close-up\n- Floating white beard wisps\n- Embedded crystal on tunic\n- Wrinkled eye close-up",
    },
}


# ---------------------------------------------------------------------------
# Prompt builders
# ---------------------------------------------------------------------------

TRIBE_DNA_INLINE = (
    "PAX TRIBE DNA (universal): ancient tribal civilization fused with bioluminescent fantasy. "
    "Mineral and crystal energy as life-source. Single dominant central eye anatomy. "
    "Tribal aesthetic + modern cool details for young audiences. Faintly glowing bio-luminescent "
    "tribal tattoos on skin where appropriate."
)


def prompt_simple_v1(c):
    """V1 — edit using template + char actual. Fix the existing character."""
    return f"""Image 1 shows the LAYOUT TEMPLATE to follow: a horizontal character sheet with three full-body views of the same character on a pure white background — front view, side profile (90 degrees), and back view, all at identical scale.

Image 2 shows the CURRENT design of {c['name']} of the Pax tribe whose base identity (single central eye, skin tone, general silhouette) must be preserved while applying the canonical v2 updates below.

Generate a NEW character design sheet using EXACTLY the layout of Image 1 (three full-body views: front + side + back, pure white background #FFFFFF, identical scale, neutral standing pose), depicting the character from Image 2 with the following CANON V2 UPDATES applied to every panel:

CANON V2 IDENTITY LOCK for {c['name']} (must appear in all three views):
{c['identity_lock']}

DEFAULT EXPRESSION: {c['default_expression']}

PAX TRIBE ANATOMY (CRITICAL — never break):
ONE single large central eye dominating the face. NEVER two eyes. NEVER eye sockets where a second eye would be. Pax tribe cyclops anatomy. ONE central eye only. Wide flexible expressive mouth. Elastic pointed ears. Stylized cartoonish proportions, large head relative to body, three-fingered hands with thumb. Faintly glowing bio-luminescent tribal tattoos.

Render style: 3D PBR Pixar-quality animation, smooth slightly-glossy skin with subtle subsurface scattering, professional 3D animation reference sheet. NOT 2D, NOT anime, NOT painterly, NOT photorealistic.

White seamless background everywhere, no environment, no floor shadows except subtle contact shadow under feet. No text labels anywhere in the image. The character must be instantly recognizable in silhouette across all three views."""


def prompt_simple_v2(c):
    """V2 — edit using template + jiggy.png as base. Transform jiggy into <char>."""
    return f"""Image 1 shows the LAYOUT TEMPLATE to follow: a horizontal character sheet with three full-body views of the same character on a pure white background — front view, side profile (90 degrees), and back view, all at identical scale.

Image 2 shows JIGGY, another Pax tribe member. Use JIGGY's general proportions, rendering style, skin texture quality and 3D animation feel as a base — but TRANSFORM the character entirely into {c['name']} with the specific traits listed below. The OUTPUT IS NOT JIGGY: it is {c['name']} of the Pax tribe.

Generate a NEW character design sheet using EXACTLY the layout of Image 1 (three full-body views: front + side + back, pure white background #FFFFFF, identical scale, neutral standing pose), depicting {c['name']} with the following CANON V2 IDENTITY applied to every panel:

CANON V2 IDENTITY LOCK for {c['name']}:
{c['identity_lock']}

DEFAULT EXPRESSION: {c['default_expression']}

PAX TRIBE ANATOMY (CRITICAL — never break):
ONE single large central eye dominating the face. NEVER two eyes. NEVER eye sockets where a second eye would be. Pax tribe cyclops anatomy. ONE central eye only. Wide flexible expressive mouth. Elastic pointed ears. Stylized cartoonish proportions, large head relative to body, three-fingered hands with thumb. Faintly glowing bio-luminescent tribal tattoos.

IMPORTANT: the final character must NOT look like Jiggy. Replace the bandana, hair, outfit, accessories and palette with {c['name']}'s canonical ones above. Use Jiggy only as a style/proportion reference, never as an identity reference.

Render style: 3D PBR Pixar-quality animation, smooth slightly-glossy skin with subtle subsurface scattering, professional 3D animation reference sheet. NOT 2D, NOT anime, NOT painterly, NOT photorealistic.

White seamless background everywhere, no environment, no floor shadows except subtle contact shadow under feet. No text labels anywhere in the image. The character must be instantly recognizable as {c['name']} in silhouette across all three views."""


def prompt_simple_v3(c):
    """V3 — from scratch (no ref). Triple identity lock."""
    return f"""Single character design reference sheet on pure white background (#FFFFFF), horizontal layout, three full-body views of the SAME character at identical scale and neutral standing pose:
[1] FRONT view — facing camera, arms relaxed at sides
[2] SIDE view — full 90-degree profile facing right, arms relaxed
[3] BACK view — facing away from camera, arms relaxed

CHARACTER: {c['name']} of the Pax tribe.

{TRIBE_DNA_INLINE}

PAX TRIBE ANATOMY (IDENTITY LOCK — triple emphasis):
- ONE single large central eye dominating the face. NEVER two eyes. NO second eye. NO eye sockets where a second eye would be. ONE central eye only.
- ONE central eye. Repeat: ONE eye. Cyclops anatomy. ONE eye.
- Pax cyclops have ONE central eye and NEVER two eyes. ONE eye. Single central eye. Cyclops.
- Smooth slightly-glossy PBR skin texture with subtle subsurface scattering
- Wide flexible expressive mouth
- Elastic pointed ears
- Stylized cartoonish proportions: large head relative to body, short limbs, three-fingered hands with thumb
- Faintly glowing bio-luminescent tribal tattoos on skin

{c['name']} CHARACTER-SPECIFIC IDENTITY:
{c['identity_lock']}

DEFAULT EXPRESSION: {c['default_expression']}

RENDER STYLE: 3D PBR Pixar/Disney-quality animation, professional production-bible character reference sheet. NOT 2D, NOT anime, NOT painterly, NOT photorealistic. Three-point studio lighting, neutral white balance.

White seamless background, no environment, no floor shadows except subtle contact shadows under feet. No text labels anywhere. The character must be instantly recognizable as {c['name']} in silhouette across all three views.

Final reminder: ONE central eye in every view, no exceptions, this is a Pax tribe cyclops."""


def prompt_full_v1_v2(c, char_token_label):
    """
    V1 and V2 completa — edit using template-detail + a simple sheet.
    char_token_label distinguishes V1 vs V2 just in narration.
    """
    return f"""Image 1 shows the LAYOUT TEMPLATE structure to mimic: a multi-row professional character design sheet with three base views in row 1, action poses in row 2, facial expressions in row 3, details strip and color palette below — all on a clean light background.

Image 2 shows {c['name']} of the Pax tribe ({char_token_label}) — preserve his/her identity, anatomy, colors, outfit and accessories EXACTLY as shown.

Generate a NEW full character design sheet for {c['name']} using the multi-row layout structure of Image 1, on a pure white background (#FFFFFF), professional 3D animation production-bible style.

IDENTITY LOCK (Pax tribe-wide):
ONE single large central eye dominating the face. NO second eye, NO eye sockets where a second eye would be. ONE eye only. Smooth slightly-glossy PBR skin with subtle subsurface scattering. Wide flexible expressive mouth. Elastic pointed ears. Stylized cartoonish proportions, large head relative to body, short limbs, three-fingered hands with thumb. Faintly glowing bio-luminescent tribal tattoos.

{c['name']}-SPECIFIC IDENTITY (must be preserved in every panel — silhouette critical):
{c['identity_lock']}

DEFAULT EXPRESSION (use for all neutral panels): {c['default_expression']}

LAYOUT (panels arranged in rows on white background):

ROW 1 — THREE BASE VIEWS (full body, identical scale, neutral pose):
[1] Front view — facing camera, arms relaxed.
[2] Side view — 90-degree profile facing right, arms relaxed.
[3] Back view — facing away, head slightly turned 3/4 to read.

ROW 2 — FIVE ACTION POSES (full body, dynamic):
[4] Walking 3/4 — mid-stride, casual motion.
[5] Running profile — full sprint side-view, one foot off ground.
[6] Signature pose — {c['signature_pose']}.
[7] Interaction pose — {c['name']} examining or handling a small canonical prop with both hands, focused expression.
[8] Iconic personality pose — {c['name']} in their most characteristic stance reflecting personality.

ROW 3 — FIVE FACIAL EXPRESSIONS (close-up head-and-shoulders, single central eye in EVERY one):
[9] Default/Happy — {c['default_expression']}.
[10] Angry/Determined — furrowed brow-equivalent, eye narrowed.
[11] Surprised — eye wide open, mouth O-shape.
[12] Sad/Melancholic — droopy eye, mouth corners down.
[13] Dialog gesture — neutral-thoughtful, hand visible at chest gesturing.

ROW 4 — DETAILS STRIP (small isolated icons, no character body):
{c['details_strip']}

ROW 5 — COLOR PALETTE STRIP:
Six color swatches in a row: {c['palette_swatches']}.

UNIFORM CONSTRAINTS:
- Same {c['name']}, same age, same outfit across every panel.
- Same 3-point studio lighting, neutral white balance.
- Pure white seamless background everywhere, no environment, no floor shadows except subtle contact shadow under feet on full-body shots.
- Silhouette icon ({c['name']}'s most distinctive trait) visibly present in every full-body and close-up panel.
- ONE central eye in every panel, no exceptions. NEVER two eyes.
- Render style: 3D PBR Pixar/Disney quality animation. NOT 2D, NOT anime, NOT painterly, NOT photorealistic.
- Avoid text labels except the six small hex codes in the palette strip."""


def prompt_full_v3(c):
    """V3 completa — uses V3 simple as the only reference."""
    return f"""Image 1 shows {c['name']} of the Pax tribe — preserve his/her identity, anatomy, colors, outfit and accessories EXACTLY as shown.

Generate a NEW full character design sheet for {c['name']} in professional 3D animation production-bible style, multi-row layout on pure white background (#FFFFFF).

IDENTITY LOCK (Pax tribe-wide — triple emphasis):
ONE single large central eye dominating the face. NO second eye, NO eye sockets where a second eye would be. ONE eye only. Pax cyclops anatomy. Repeat: ONE central eye, never two. Smooth slightly-glossy PBR skin with subtle subsurface scattering. Wide flexible expressive mouth. Elastic pointed ears. Stylized cartoonish proportions, large head, short limbs, three-fingered hands with thumb. Faintly glowing bio-luminescent tribal tattoos.

{c['name']}-SPECIFIC IDENTITY (must be preserved in every panel — silhouette critical):
{c['identity_lock']}

DEFAULT EXPRESSION (use for all neutral panels): {c['default_expression']}

LAYOUT (panels arranged in rows on white background):

ROW 1 — THREE BASE VIEWS (full body, identical scale, neutral pose):
[1] Front view — facing camera, arms relaxed.
[2] Side view — 90-degree profile facing right, arms relaxed.
[3] Back view — facing away, head slightly turned 3/4 to read.

ROW 2 — FIVE ACTION POSES (full body, dynamic):
[4] Walking 3/4 — mid-stride, casual motion.
[5] Running profile — full sprint side-view, one foot off ground.
[6] Signature pose — {c['signature_pose']}.
[7] Interaction pose — {c['name']} handling a canonical prop with both hands, focused expression.
[8] Iconic personality pose — {c['name']} in their most characteristic stance.

ROW 3 — FIVE FACIAL EXPRESSIONS (close-up head-and-shoulders, single central eye in EVERY one):
[9] Default/Happy — {c['default_expression']}.
[10] Angry/Determined — furrowed brow-equivalent, eye narrowed.
[11] Surprised — eye wide open, mouth O-shape.
[12] Sad/Melancholic — droopy eye, mouth corners down.
[13] Dialog gesture — neutral-thoughtful, hand visible at chest gesturing.

ROW 4 — DETAILS STRIP (small isolated icons, no character body):
{c['details_strip']}

ROW 5 — COLOR PALETTE STRIP:
Six color swatches in a row: {c['palette_swatches']}.

UNIFORM CONSTRAINTS:
- Same {c['name']}, same age, same outfit across every panel.
- Pure white seamless background everywhere, no environment, no floor shadows except subtle contact shadow under feet on full-body shots.
- Silhouette icon ({c['name']}'s most distinctive trait) visibly present in every full-body and close-up panel.
- ONE central eye in every panel, no exceptions. NEVER two eyes. Pax cyclops anatomy.
- Render style: 3D PBR Pixar/Disney quality animation. NOT 2D, NOT anime, NOT painterly, NOT photorealistic.
- Avoid text labels except the six small hex codes in the palette strip."""


# ---------------------------------------------------------------------------
# Mime helper (local)
# ---------------------------------------------------------------------------

def _mime_for(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    return {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }.get(ext, "image/png")


# ---------------------------------------------------------------------------
# Async generation helpers
# ---------------------------------------------------------------------------

async def gen_text(client, prompt, output_path, size="1536x1024", quality="high"):
    t0 = time.time()
    try:
        result = await client.images.generate(
            model=MODEL,
            prompt=prompt,
            size=size,
            quality=quality,
        )
        image_b64 = result.data[0].b64_json
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(base64.b64decode(image_b64))
        dt = time.time() - t0
        size_kb = os.path.getsize(output_path) / 1024
        return {"path": output_path, "status": "OK", "time": dt, "size_kb": size_kb}
    except Exception as e:
        return {"path": output_path, "status": "FAIL", "error": str(e), "time": time.time() - t0}


async def gen_edit(client, prompt, input_paths, output_path, size="1536x1024", quality="high"):
    t0 = time.time()
    try:
        file_handles = []
        file_tuples = []
        for p in input_paths:
            fh = open(p, "rb")
            file_handles.append(fh)
            file_tuples.append((os.path.basename(p), fh, _mime_for(p)))
        try:
            result = await client.images.edit(
                model=MODEL,
                image=file_tuples if len(file_tuples) > 1 else file_tuples[0],
                prompt=prompt,
                size=size,
                quality=quality,
            )
        finally:
            for fh in file_handles:
                fh.close()
        image_b64 = result.data[0].b64_json
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(base64.b64decode(image_b64))
        dt = time.time() - t0
        size_kb = os.path.getsize(output_path) / 1024
        return {"path": output_path, "status": "OK", "time": dt, "size_kb": size_kb}
    except Exception as e:
        return {"path": output_path, "status": "FAIL", "error": str(e), "time": time.time() - t0}


# ---------------------------------------------------------------------------
# Job orchestration
# ---------------------------------------------------------------------------

def build_jobs():
    """Returns (simple_jobs, full_jobs_template). full needs simple outputs to exist."""
    simple_jobs = []
    full_jobs_template = []  # will become real jobs after simples exist

    for key, c in CHARS.items():
        out_v1_simple = os.path.join(REPO, "content", "canon-v2", key, "v1-fix-actual", "simple.png")
        out_v2_simple = os.path.join(REPO, "content", "canon-v2", key, "v2-jiggy-base", "simple.png")
        out_v3_simple = os.path.join(REPO, "content", "canon-v2", key, "v3-from-scratch", "simple.png")
        out_v1_full = os.path.join(REPO, "content", "canon-v2", key, "v1-fix-actual", "completa.png")
        out_v2_full = os.path.join(REPO, "content", "canon-v2", key, "v2-jiggy-base", "completa.png")
        out_v3_full = os.path.join(REPO, "content", "canon-v2", key, "v3-from-scratch", "completa.png")

        # Simples
        simple_jobs.append({
            "label": f"{key}/v1-simple",
            "kind": "edit",
            "prompt": prompt_simple_v1(c),
            "inputs": [TEMPLATE_SIMPLE, c["ref"]],
            "output": out_v1_simple,
        })
        simple_jobs.append({
            "label": f"{key}/v2-simple",
            "kind": "edit",
            "prompt": prompt_simple_v2(c),
            "inputs": [TEMPLATE_SIMPLE, JIGGY_REF],
            "output": out_v2_simple,
        })
        simple_jobs.append({
            "label": f"{key}/v3-simple",
            "kind": "text",
            "prompt": prompt_simple_v3(c),
            "inputs": [],
            "output": out_v3_simple,
        })

        # Completas (template depends on simple existence; we still queue them)
        full_jobs_template.append({
            "label": f"{key}/v1-full",
            "kind": "edit",
            "prompt": prompt_full_v1_v2(c, "current canonical pose"),
            "inputs": [TEMPLATE_DETAIL, out_v1_simple],
            "output": out_v1_full,
        })
        full_jobs_template.append({
            "label": f"{key}/v2-full",
            "kind": "edit",
            "prompt": prompt_full_v1_v2(c, "jiggy-base derivation"),
            "inputs": [TEMPLATE_DETAIL, out_v2_simple],
            "output": out_v2_full,
        })
        full_jobs_template.append({
            "label": f"{key}/v3-full",
            "kind": "edit",
            "prompt": prompt_full_v3(c),
            "inputs": [out_v3_simple],
            "output": out_v3_full,
        })

    return simple_jobs, full_jobs_template


async def run_jobs(client, jobs, label, concurrency=CONCURRENCY):
    """Run jobs with Semaphore. Skip already-existing outputs."""
    sem = asyncio.Semaphore(concurrency)
    pending = []
    skipped = []
    for j in jobs:
        if os.path.exists(j["output"]) and os.path.getsize(j["output"]) > 50_000:
            skipped.append(j)
        else:
            pending.append(j)

    print(f"\n{'='*70}\n{label}: {len(pending)} pending, {len(skipped)} skipped (already exist)\n{'='*70}")

    async def run_one(j):
        async with sem:
            print(f"  [START] {j['label']}")
            if j["kind"] == "text":
                r = await gen_text(client, j["prompt"], j["output"])
            else:
                r = await gen_edit(client, j["prompt"], j["inputs"], j["output"])
            r["label"] = j["label"]
            status = r["status"]
            t = r.get("time", 0)
            kb = r.get("size_kb", 0)
            print(f"  [{status}] {j['label']} - {t:.1f}s - {kb:.0f}KB")
            if status == "FAIL":
                print(f"    ERROR: {r.get('error')}")
            return r

    results = await asyncio.gather(*[run_one(j) for j in pending], return_exceptions=True)

    # Retry FAILS once
    fails = []
    for j, r in zip(pending, results):
        if isinstance(r, Exception) or (isinstance(r, dict) and r["status"] == "FAIL"):
            fails.append(j)
    if fails:
        print(f"\n  Retrying {len(fails)} failed jobs...")
        async def retry_one(j):
            async with sem:
                print(f"  [RETRY] {j['label']}")
                if j["kind"] == "text":
                    r = await gen_text(client, j["prompt"], j["output"])
                else:
                    r = await gen_edit(client, j["prompt"], j["inputs"], j["output"])
                r["label"] = j["label"]
                print(f"  [RETRY {r['status']}] {j['label']} - {r.get('time', 0):.1f}s")
                return r
        retry_results = await asyncio.gather(*[retry_one(j) for j in fails], return_exceptions=True)
        # Merge retry results back
        retry_map = {j["label"]: r for j, r in zip(fails, retry_results)}
        merged = []
        for j, r in zip(pending, results):
            if j["label"] in retry_map:
                merged.append(retry_map[j["label"]])
            else:
                merged.append(r)
        results = merged

    return results, skipped


async def main():
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

    simple_jobs, full_jobs = build_jobs()

    print(f"Total jobs: {len(simple_jobs)} simples + {len(full_jobs)} completas = {len(simple_jobs) + len(full_jobs)}")

    t_start = time.time()

    # Phase 1: simples
    simple_results, simple_skipped = await run_jobs(client, simple_jobs, "FASE 1 — SIMPLES")

    # Phase 2: full (depends on simples)
    # Filter out full jobs whose simple is still missing
    valid_full = []
    invalid_full = []
    for j in full_jobs:
        ok = True
        for inp in j["inputs"]:
            if not os.path.exists(inp):
                ok = False
                break
        if ok:
            valid_full.append(j)
        else:
            invalid_full.append(j)
    if invalid_full:
        print(f"\nSKIPPING {len(invalid_full)} completas because their dependency simple is missing:")
        for j in invalid_full:
            print(f"  - {j['label']} (missing: {[i for i in j['inputs'] if not os.path.exists(i)]})")

    full_results, full_skipped = await run_jobs(client, valid_full, "FASE 2 — COMPLETAS")

    t_total = time.time() - t_start

    # Final report
    print("\n" + "=" * 70)
    print("RESUMEN FINAL")
    print("=" * 70)
    all_outs = []
    for key in CHARS.keys():
        for variation in ["v1-fix-actual", "v2-jiggy-base", "v3-from-scratch"]:
            for sheet in ["simple.png", "completa.png"]:
                p = os.path.join(REPO, "content", "canon-v2", key, variation, sheet)
                rel = os.path.relpath(p, REPO).replace("\\", "/")
                if os.path.exists(p):
                    kb = os.path.getsize(p) / 1024
                    all_outs.append((rel, "OK", kb))
                    print(f"  OK   {rel} ({kb:.0f} KB)")
                else:
                    all_outs.append((rel, "FAIL", 0))
                    print(f"  FAIL {rel}")

    ok_count = sum(1 for _, s, _ in all_outs if s == "OK")
    print(f"\nTotal OK: {ok_count}/{len(all_outs)}")
    print(f"Tiempo total: {t_total/60:.1f} min")


if __name__ == "__main__":
    asyncio.run(main())
