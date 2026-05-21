"""
Piloto canon visual v2 - Jiggy.

Genera 6 imagenes (3 simples + 3 completas) para validar direccion visual
antes del bulk de los 7+5 personajes restantes.

Fases:
1. Paralelo: V1 simple, V2 simple, V3 simple
2. Paralelo: V1 completa, V2 completa, V3 completa (cada una con su simple)
"""

import os
import sys
import time
import asyncio
import base64
from openai import AsyncOpenAI

# Carga env
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openai_images import _load_env  # noqa: E402
_load_env()

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = "gpt-image-2"

TEMPLATE_SIMPLE = os.path.join(REPO, "Personajes-Fix", "Character-Sheet-Simple.webp")
TEMPLATE_DETAIL = os.path.join(REPO, "Personajes-Fix", "Character-Sheet-Detail.jpg")
JIGGY_REF = os.path.join(REPO, "public", "images", "personajes", "jiggy.png")

OUT_V1_SIMPLE = os.path.join(REPO, "content", "canon-v2", "jiggy", "v1-fix-actual", "simple.png")
OUT_V1_FULL = os.path.join(REPO, "content", "canon-v2", "jiggy", "v1-fix-actual", "completa.png")
OUT_V2_SIMPLE = os.path.join(REPO, "content", "canon-v2", "jiggy", "v2-jiggy-base", "simple.png")
OUT_V2_FULL = os.path.join(REPO, "content", "canon-v2", "jiggy", "v2-jiggy-base", "completa.png")
OUT_V3_SIMPLE = os.path.join(REPO, "content", "canon-v2", "jiggy", "v3-from-scratch", "simple.png")
OUT_V3_FULL = os.path.join(REPO, "content", "canon-v2", "jiggy", "v3-from-scratch", "completa.png")


# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

PROMPT_V1_V2_SIMPLE = """Image 1 shows the LAYOUT TEMPLATE to follow: a horizontal character sheet with three full-body views of the same character on a pure white background — front view, side profile (90 degrees), and back view, all at identical scale.

Image 2 shows JIGGY, the Pax tribe cyclops protagonist whose IDENTITY must be preserved.

Generate a NEW character design sheet using EXACTLY the layout of Image 1 (three full-body views: front + side + back, pure white background #FFFFFF, identical scale, neutral standing pose), depicting the character from Image 2 with the following CANON V2 UPDATES applied to every panel:

CANON V2 ADDITIONS (must appear in all three views):
- Worn purple bandana tied around the forehead — this is his SILHOUETTE ICON, must be clearly visible from front, side and back
- Small messy mini-dreadlocks sticking out below the bandana
- Small artisan metal hoop earrings on the pointed elastic ears
- Glowing violet crystal pendant hanging on the chest
- Light asymmetric leather + mineral-fiber garment (NOT a dress, NOT a tunic — fragmented tribal pieces)
- Subtle glowing bio-luminescent tribal tattoos on arms and legs
- Color palette: turquoise skin base #2BC8C8, violet accents #6B2FBF, magenta neon highlights #E91E80
- Huge expressive smile by default

IDENTITY LOCK (CRITICAL):
ONE single large central eye dominating the face. NEVER two eyes. NEVER eye sockets where a second eye would be. This is Pax tribe cyclops anatomy. ONE central eye only. ONE eye. ONE eye.

Render style: 3D PBR Pixar-quality animation, smooth glossy turquoise skin with subtle subsurface scattering, professional 3D animation reference sheet. NOT 2D, NOT anime, NOT painterly, NOT photorealistic. Cartoonish stylized proportions, large head, short limbs, three-fingered hands with thumb.

White seamless background everywhere, no environment, no floor shadows except subtle contact shadow under feet. No text labels anywhere in the image."""


PROMPT_V3_SIMPLE = """Single character design reference sheet on pure white background (#FFFFFF), horizontal layout, three full-body views of the SAME character at identical scale and neutral standing pose:
[1] FRONT view — facing camera, arms relaxed at sides
[2] SIDE view — full 90-degree profile facing right, arms relaxed
[3] BACK view — facing away from camera, arms relaxed

CHARACTER: JIGGY of the Pax tribe.

PAX TRIBE ANATOMY (identity lock):
- ONE single large central eye dominating the face. NEVER two eyes. NO second eye. NO eye sockets where a second eye would be. ONE central eye only.
- ONE central eye. Repeat: ONE eye. Cyclops anatomy. ONE eye.
- Turquoise-green skin (#2BC8C8 base), smooth slightly-glossy PBR texture with subtle subsurface scattering
- Wide flexible expressive mouth
- Elastic pointed ears
- Stylized cartoonish proportions: large head relative to body, short limbs, three-fingered hands with thumb
- Faintly glowing bio-luminescent tribal tattoos on skin
- Aesthetic: ancient tribal civilization fused with bioluminescent fantasy and crystal-mineral energy

JIGGY CHARACTER-SPECIFIC:
- Worn purple bandana tied around forehead (this is his silhouette icon — must be clearly visible in every view, front side and back)
- Small messy mini-dreadlocks sticking out below the bandana
- Small artisan metal hoop earrings on pointed ears
- Glowing violet crystal pendant on chest
- Light asymmetric tribal garment made of leather and mineral-fibers, fragmented pieces (not a full dress, not a tunic)
- Subtle glowing tribal tattoos on arms and legs
- Color palette: turquoise base + violet accents + magenta neon highlights
- Huge expressive smile by default
- Kinetic energetic body language, slight forward lean even in neutral pose
- Approx 1.6m tall, young-adult proportions

RENDER STYLE: 3D PBR Pixar/Disney-quality animation, professional production-bible character reference sheet. NOT 2D, NOT anime, NOT painterly, NOT photorealistic. Three-point studio lighting, neutral white balance.

White seamless background, no environment, no floor shadows except subtle contact shadows under feet. No text labels anywhere."""


PROMPT_COMPLETA = """Image 1 shows the LAYOUT TEMPLATE structure to mimic: a multi-row professional character design sheet with three base views in row 1, action poses in row 2, facial expressions in row 3, details strip and color palette below — all on a clean light background.

Image 2 shows JIGGY of the Pax tribe — preserve his identity, anatomy, colors, outfit and accessories EXACTLY as shown.

Generate a NEW full character design sheet for JIGGY using the multi-row layout structure of Image 1, on a pure white background (#FFFFFF), professional 3D animation production-bible style.

IDENTITY LOCK (Pax tribe-wide):
ONE single large central eye dominating the face. NO second eye, NO eye sockets where a second eye would be. ONE eye only. Turquoise-green skin base #2BC8C8 with smooth slightly-glossy PBR texture and subtle subsurface scattering. Wide flexible expressive mouth. Elastic pointed ears. Stylized cartoonish proportions, large head relative to body, short limbs, three-fingered hands with thumb. Faintly glowing bio-luminescent tribal tattoos.

JIGGY-SPECIFIC IDENTITY (must be preserved in every panel):
Worn purple bandana on forehead (silhouette icon — clearly visible in every panel), small messy mini-dreadlocks below bandana, small artisan metal hoop earrings, glowing violet crystal pendant on chest, light asymmetric leather + mineral-fiber garment, subtle glowing tribal tattoos on arms and legs, huge expressive smile by default, kinetic energetic posture.

LAYOUT (panels arranged in rows on white background):

ROW 1 — THREE BASE VIEWS (full body, identical scale, neutral pose):
[1] Front view — facing camera, arms relaxed.
[2] Side view — 90-degree profile facing right, arms relaxed.
[3] Back view — facing away, head slightly turned 3/4 to read.

ROW 2 — FIVE ACTION POSES (full body, dynamic):
[4] Walking 3/4 — mid-stride, casual motion.
[5] Running profile — full sprint side-view, one foot off ground.
[6] Signature pose — parkour mid-air leap, one hand reaching forward, violet crystal pendant swinging out, dreadlocks trailing, big smile.
[7] Interaction pose — Jiggy holding the violet crystal pendant with both hands, examining with wonder.
[8] Iconic personality pose — Jiggy crouched on a rock platform, confident hero pose, arms wide, smiling.

ROW 3 — FIVE FACIAL EXPRESSIONS (close-up head-and-shoulders):
[9] Happy joyful — wide smile, eye sparkle.
[10] Angry determined — furrowed brow, eye narrowed.
[11] Surprised — eye wide open, mouth O-shape.
[12] Sad melancholic — droopy eye, mouth corners down.
[13] Dialog gesture — neutral-thoughtful, hand visible at chest gesturing.

ROW 4 — DETAILS STRIP (small isolated icons):
- Purple bandana shown flat.
- Violet pendant crystal close-up.
- Metal hoop earrings pair.
- Tribal tattoo detail close-up.

ROW 5 — COLOR PALETTE STRIP:
Six color swatches: #2BC8C8 turquoise, #6B2FBF violet, #E91E80 magenta-neon, #5A3A1F leather-brown, #F0F0F0 white, #0D0D14 deep-accent.

UNIFORM CONSTRAINTS:
- Same Jiggy, same age, same outfit across every panel.
- Same 3-point studio lighting, neutral white balance.
- Pure white seamless background everywhere, no environment, no floor shadows except subtle contact shadow under feet on full-body shots.
- Bandana visibly PURPLE in every panel (silhouette critical).
- ONE central eye in every panel, no exceptions. NEVER two eyes.
- Render style: 3D PBR Pixar/Disney quality animation. NOT 2D, NOT anime, NOT painterly, NOT photorealistic.
- Avoid text labels except the six small hex codes in the palette strip."""


PROMPT_V3_COMPLETA = """Image 1 shows JIGGY of the Pax tribe — preserve his identity, anatomy, colors, outfit and accessories EXACTLY as shown.

Generate a NEW full character design sheet for JIGGY in professional 3D animation production-bible style, multi-row layout on pure white background (#FFFFFF).

IDENTITY LOCK (Pax tribe-wide):
ONE single large central eye dominating the face. NO second eye, NO eye sockets where a second eye would be. ONE eye only. Turquoise-green skin base #2BC8C8 with smooth slightly-glossy PBR texture and subtle subsurface scattering. Wide flexible expressive mouth. Elastic pointed ears. Stylized cartoonish proportions, large head, short limbs, three-fingered hands with thumb. Faintly glowing bio-luminescent tribal tattoos.

JIGGY-SPECIFIC IDENTITY (must be preserved in every panel):
Worn purple bandana on forehead (silhouette icon — clearly visible in every panel), small messy mini-dreadlocks below bandana, small artisan metal hoop earrings, glowing violet crystal pendant on chest, light asymmetric leather + mineral-fiber garment, subtle glowing tribal tattoos on arms and legs, huge expressive smile by default, kinetic energetic posture.

LAYOUT (panels arranged in rows on white background):

ROW 1 — THREE BASE VIEWS (full body, identical scale, neutral pose):
[1] Front view — facing camera, arms relaxed.
[2] Side view — 90-degree profile facing right, arms relaxed.
[3] Back view — facing away, head slightly turned 3/4 to read.

ROW 2 — FIVE ACTION POSES (full body, dynamic):
[4] Walking 3/4 — mid-stride, casual motion.
[5] Running profile — full sprint side-view, one foot off ground.
[6] Signature pose — parkour mid-air leap, one hand reaching forward, violet crystal pendant swinging out, dreadlocks trailing, big smile.
[7] Interaction pose — Jiggy holding the violet crystal pendant with both hands, examining with wonder.
[8] Iconic personality pose — Jiggy crouched on a rock platform, confident hero pose, arms wide, smiling.

ROW 3 — FIVE FACIAL EXPRESSIONS (close-up head-and-shoulders):
[9] Happy joyful — wide smile, eye sparkle.
[10] Angry determined — furrowed brow, eye narrowed.
[11] Surprised — eye wide open, mouth O-shape.
[12] Sad melancholic — droopy eye, mouth corners down.
[13] Dialog gesture — neutral-thoughtful, hand visible at chest gesturing.

ROW 4 — DETAILS STRIP (small isolated icons):
- Purple bandana shown flat.
- Violet pendant crystal close-up.
- Metal hoop earrings pair.
- Tribal tattoo detail close-up.

ROW 5 — COLOR PALETTE STRIP:
Six color swatches: #2BC8C8 turquoise, #6B2FBF violet, #E91E80 magenta-neon, #5A3A1F leather-brown, #F0F0F0 white, #0D0D14 deep-accent.

UNIFORM CONSTRAINTS:
- Same Jiggy, same age, same outfit across every panel.
- Pure white seamless background everywhere, no environment, no floor shadows except subtle contact shadow under feet on full-body shots.
- Bandana visibly PURPLE in every panel.
- ONE central eye in every panel, no exceptions. NEVER two eyes.
- Render style: 3D PBR Pixar/Disney quality animation. NOT 2D, NOT anime, NOT painterly, NOT photorealistic.
- Avoid text labels except the six small hex codes in the palette strip."""


# ---------------------------------------------------------------------------
# Async helpers
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
        with open(output_path, "wb") as f:
            f.write(base64.b64decode(image_b64))
        dt = time.time() - t0
        size_kb = os.path.getsize(output_path) / 1024
        return {"path": output_path, "status": "OK", "time": dt, "size_kb": size_kb}
    except Exception as e:
        return {"path": output_path, "status": "FAIL", "error": str(e), "time": time.time() - t0}


def _mime_for(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    return {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }.get(ext, "image/png")


async def gen_edit(client, prompt, input_paths, output_path, size="1536x1024", quality="high"):
    t0 = time.time()
    try:
        # Build file tuples (filename, fileobj, mimetype) so the SDK forwards
        # the correct content-type even for .webp (otherwise SDK sends
        # application/octet-stream and the API rejects it).
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
        with open(output_path, "wb") as f:
            f.write(base64.b64decode(image_b64))
        dt = time.time() - t0
        size_kb = os.path.getsize(output_path) / 1024
        return {"path": output_path, "status": "OK", "time": dt, "size_kb": size_kb}
    except Exception as e:
        return {"path": output_path, "status": "FAIL", "error": str(e), "time": time.time() - t0}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def main():
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

    print("=" * 70)
    print("FASE 1: Generando SIMPLES en paralelo (solo los faltantes)...")
    print("=" * 70)

    phase1_jobs = []
    phase1_labels = []
    if not os.path.exists(OUT_V1_SIMPLE):
        phase1_jobs.append(gen_edit(client, PROMPT_V1_V2_SIMPLE, [TEMPLATE_SIMPLE, JIGGY_REF], OUT_V1_SIMPLE))
        phase1_labels.append("V1 simple")
    else:
        print(f"  SKIP V1 simple (ya existe)")
    if not os.path.exists(OUT_V2_SIMPLE):
        phase1_jobs.append(gen_edit(client, PROMPT_V1_V2_SIMPLE, [TEMPLATE_SIMPLE, JIGGY_REF], OUT_V2_SIMPLE))
        phase1_labels.append("V2 simple")
    else:
        print(f"  SKIP V2 simple (ya existe)")
    if not os.path.exists(OUT_V3_SIMPLE):
        phase1_jobs.append(gen_text(client, PROMPT_V3_SIMPLE, OUT_V3_SIMPLE))
        phase1_labels.append("V3 simple")
    else:
        print(f"  SKIP V3 simple (ya existe)")

    phase1 = await asyncio.gather(*phase1_jobs, return_exceptions=True) if phase1_jobs else []

    for r in phase1:
        if isinstance(r, dict):
            print(f"  [{r['status']}] {os.path.basename(os.path.dirname(r['path']))}/{os.path.basename(r['path'])} - {r.get('time', 0):.1f}s - {r.get('size_kb', 0):.0f}KB")
            if r['status'] == 'FAIL':
                print(f"    ERROR: {r.get('error')}")
        else:
            print(f"  EXCEPTION: {r}")

    # Verificar que los 3 simples existen
    missing = []
    for p in [OUT_V1_SIMPLE, OUT_V2_SIMPLE, OUT_V3_SIMPLE]:
        if not os.path.exists(p):
            missing.append(p)
    if missing:
        print(f"\nFASE 1 FALLO. Faltan: {missing}")
        print("Reintentando los faltantes UNA vez...")
        retry_jobs = []
        if not os.path.exists(OUT_V1_SIMPLE):
            retry_jobs.append(gen_edit(client, PROMPT_V1_V2_SIMPLE, [TEMPLATE_SIMPLE, JIGGY_REF], OUT_V1_SIMPLE))
        if not os.path.exists(OUT_V2_SIMPLE):
            retry_jobs.append(gen_edit(client, PROMPT_V1_V2_SIMPLE, [TEMPLATE_SIMPLE, JIGGY_REF], OUT_V2_SIMPLE))
        if not os.path.exists(OUT_V3_SIMPLE):
            retry_jobs.append(gen_text(client, PROMPT_V3_SIMPLE, OUT_V3_SIMPLE))
        retries = await asyncio.gather(*retry_jobs, return_exceptions=True)
        for r in retries:
            if isinstance(r, dict):
                print(f"  RETRY [{r['status']}] {r['path']} - {r.get('time', 0):.1f}s")

        # Verificar de nuevo
        still_missing = [p for p in [OUT_V1_SIMPLE, OUT_V2_SIMPLE, OUT_V3_SIMPLE] if not os.path.exists(p)]
        if still_missing:
            print(f"\nABORT: simples siguen faltando despues de retry: {still_missing}")
            return

    print("\n" + "=" * 70)
    print("FASE 2: Generando COMPLETAS en paralelo (solo las faltantes)...")
    print("=" * 70)

    phase2_jobs = []
    if not os.path.exists(OUT_V1_FULL):
        phase2_jobs.append(gen_edit(client, PROMPT_COMPLETA, [TEMPLATE_DETAIL, OUT_V1_SIMPLE], OUT_V1_FULL))
    else:
        print(f"  SKIP V1 completa (ya existe)")
    if not os.path.exists(OUT_V2_FULL):
        phase2_jobs.append(gen_edit(client, PROMPT_COMPLETA, [TEMPLATE_DETAIL, OUT_V2_SIMPLE], OUT_V2_FULL))
    else:
        print(f"  SKIP V2 completa (ya existe)")
    if not os.path.exists(OUT_V3_FULL):
        phase2_jobs.append(gen_edit(client, PROMPT_V3_COMPLETA, [OUT_V3_SIMPLE], OUT_V3_FULL))
    else:
        print(f"  SKIP V3 completa (ya existe)")

    phase2 = await asyncio.gather(*phase2_jobs, return_exceptions=True) if phase2_jobs else []

    for r in phase2:
        if isinstance(r, dict):
            print(f"  [{r['status']}] {os.path.basename(os.path.dirname(r['path']))}/{os.path.basename(r['path'])} - {r.get('time', 0):.1f}s - {r.get('size_kb', 0):.0f}KB")
            if r['status'] == 'FAIL':
                print(f"    ERROR: {r.get('error')}")
        else:
            print(f"  EXCEPTION: {r}")

    # Retry completas si fallaron
    missing2 = []
    for p in [OUT_V1_FULL, OUT_V2_FULL, OUT_V3_FULL]:
        if not os.path.exists(p):
            missing2.append(p)
    if missing2:
        print(f"\nFASE 2 falla parcial: {missing2}. Reintentando UNA vez...")
        retry_jobs = []
        if not os.path.exists(OUT_V1_FULL):
            retry_jobs.append(gen_edit(client, PROMPT_COMPLETA, [TEMPLATE_DETAIL, OUT_V1_SIMPLE], OUT_V1_FULL))
        if not os.path.exists(OUT_V2_FULL):
            retry_jobs.append(gen_edit(client, PROMPT_COMPLETA, [TEMPLATE_DETAIL, OUT_V2_SIMPLE], OUT_V2_FULL))
        if not os.path.exists(OUT_V3_FULL):
            retry_jobs.append(gen_edit(client, PROMPT_V3_COMPLETA, [OUT_V3_SIMPLE], OUT_V3_FULL))
        retries = await asyncio.gather(*retry_jobs, return_exceptions=True)
        for r in retries:
            if isinstance(r, dict):
                print(f"  RETRY [{r['status']}] {r['path']} - {r.get('time', 0):.1f}s")

    print("\n" + "=" * 70)
    print("RESUMEN FINAL")
    print("=" * 70)
    for p in [OUT_V1_SIMPLE, OUT_V1_FULL, OUT_V2_SIMPLE, OUT_V2_FULL, OUT_V3_SIMPLE, OUT_V3_FULL]:
        rel = os.path.relpath(p, REPO).replace("\\", "/")
        if os.path.exists(p):
            kb = os.path.getsize(p) / 1024
            print(f"  OK   {rel} ({kb:.0f} KB)")
        else:
            print(f"  FAIL {rel}")


if __name__ == "__main__":
    asyncio.run(main())
