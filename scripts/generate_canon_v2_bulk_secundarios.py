"""
Bulk canon visual v2 - 5 secundarios Pax tribe (TIK, VEX, MIRA, ZIN, KOA).

Genera 20 imagenes:
- 5 chars x 2 variaciones (v-con-ref, v-sin-ref) x 2 sheets (simple, completa)

Fases:
1. Paralelo: 10 simples (Semaphore=4)
2. Paralelo: 10 completas (Semaphore=4)

V_con-ref:  edit_image con Character-Sheet-{Simple,Detail} + jiggy.png + onyx.png
            como referencia tribal (NO replicar — solo guia de estilo).
V_sin-ref:  generate_image puro con Tribe-DNA comprimido en el prompt.
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

TEMPLATE_SIMPLE = os.path.join(REPO, "Personajes-Fix", "Character-Sheet-Simple.webp")
TEMPLATE_DETAIL = os.path.join(REPO, "Personajes-Fix", "Character-Sheet-Detail.jpg")
JIGGY_REF = os.path.join(REPO, "public", "images", "personajes", "jiggy.png")
ONYX_REF = os.path.join(REPO, "public", "images", "personajes", "onyx.png")

OUT_ROOT = os.path.join(REPO, "content", "canon-v2", "secundarios")

CONCURRENCY = 4


# ---------------------------------------------------------------------------
# Tribe DNA condensed (used in V_sin-ref prompts)
# ---------------------------------------------------------------------------

TRIBE_DNA = """PAX TRIBE ANATOMY (identity lock, applies to every character):
- ONE single central eye dominating the face. NEVER two eyes. NO second eye. NO eye sockets where a second eye would be. ONE central eye only. Repeat: ONE eye. Cyclops anatomy. ONE eye.
- Turquoise-green skin base, smooth slightly-glossy PBR texture with subtle subsurface scattering.
- Wide flexible expressive mouth.
- Elastic pointed ears.
- Stylized cartoonish proportions, large head relative to body, short limbs, three-fingered hands with thumb.
- Faintly glowing bio-luminescent tribal tattoos on skin.
- Aesthetic: ancient tribal civilization fused with bioluminescent fantasy and crystal-mineral energy. Modern "cool" edge."""


# ---------------------------------------------------------------------------
# Per-character identity blocks
# ---------------------------------------------------------------------------

CHARS = {
    "tik": {
        "name": "TIK",
        "role_short": "Child apprentice crystal artisan, ~6-8 years Pax old",
        "anatomy": "Pax cyclops CHILD with a disproportionately large head (childlike trait), incipiently robust back from artisan apprenticeship. Smaller body than adult Pax.",
        "silhouette_icon": "Large head + small afro-tribal hair + WORK APRON COVERED IN COLLECTED CRYSTAL SAMPLES of many different colors hanging from leather strings.",
        "props": "Leather work apron with red, blue, green and golden crystal samples hanging from strings, tiny artisan tools tucked in apron pocket, imperfect hand-painted childlike tribal markings on cheeks.",
        "palette_swatches": "#2BC8C8 bright turquoise, #F5D547 crystal-yellow, #E63946 crystal-red, #C9A77E leather-light, #FFF6E0 white-highlights, #2A1F0A deep-accent",
        "palette_short": "bright turquoise + crystal-yellow + crystal-red + light leather",
        "default_pose": "curious leaning forward, hands near the crystals hanging from his apron",
        "default_expression": "wide curious smile, eye sparkling with wonder, mouth slightly open in amazement",
        "signature_pose": "kneeling next to a pile of raw crystals, examining one closely with a magnifying-crystal-tool, mouth open in concentration",
        "extra_traits": "Childlike, energetic body language. Obsessively focused for a kid.",
    },
    "vex": {
        "name": "VEX",
        "role_short": "Retired veteran Guardian and mentor, ~50-60 years Pax old, gruff but unwavering loyalty",
        "anatomy": "Pax cyclops AGED ADULT, muscular but weathered — defined musculature with skin marked by years of combat and life. Adult-sized body.",
        "silhouette_icon": "MINERAL EYE-PATCH covering half of the single central eye (lost partial vision in battle) + WARRIOR BRAID on one side of the head, shaved on the other side + short dark ceremonial cape.",
        "props": "Mineral eye-patch covering half the central eye, short dark ceremonial cape, heavy armor bracers with black and red crystal inlays, elaborate war tattoos covering one entire arm, heavy combat belt with pouches.",
        "palette_swatches": "#1F6868 aged-dark-turquoise, #5A5550 mineral-gray, #8C2E1A old-magma-red, #7A5A28 bronze-old, #D8D2C0 white-tooth, #1A0E0E deep-accent",
        "palette_short": "aged-dark-turquoise + mineral-gray + old-magma-red + old bronze",
        "default_pose": "firm stance, feet apart, hands near combat belt, veteran guardian posture",
        "default_expression": "stern gruff veteran look, mouth tight, single visible eye hard and focused, hint of past wisdom",
        "signature_pose": "standing at attention with one hand on weapon hilt, cape flowing slightly, single eye scanning horizon",
        "extra_traits": "Aged, weathered face. The eye-patch is non-removable identity.",
    },
    "mira": {
        "name": "MIRA",
        "role_short": "Elderly healer-midwife, ~70+ years Pax old, warm and patient",
        "anatomy": "Pax cyclops ELDERLY WOMAN, ROUND WARM single eye (not tired — she is in her prime as a healer), body slightly hunched from age only. Adult-sized.",
        "silhouette_icon": "FLOATING HEALING CRYSTALS PERMANENTLY ORBITING AROUND HER HANDS (one per ailment treated) + STRONGER FULL-BODY BIOLUMINESCENT GLOW than other Pax + long white hair gathered in a tall bun with thin braids.",
        "props": "Flowing layered robes embroidered with healing symbols, tall hair bun with thin braids, SPIRAL tribal markings on cheeks, necklace of dried healing herbs and tiny crystals, healing crystals floating around her hands.",
        "palette_swatches": "#8FD5D5 soft-turquoise, #4FB87C healing-green, #F0B5C7 soft-pink, #E8C26A golden-light, #FFFFFF bright-white, #1E2A3A deep-accent",
        "palette_short": "soft turquoise + healing green + soft pink + golden light",
        "default_pose": "open posture, hands visible with crystals floating between them",
        "default_expression": "warm patient maternal smile, eye soft and kind, slight wrinkles from years of smiling, gentle wisdom",
        "signature_pose": "kneeling next to an invisible patient with hands extended, crystals floating between her palms in a healing arc",
        "extra_traits": "Body luminescence stronger than other Pax. Floating crystals always orbiting hands.",
    },
    "zin": {
        "name": "ZIN",
        "role_short": "Young-adult tunnel scout explorer, ~18-22 years Pax old, solitary observer",
        "anatomy": "Pax cyclops YOUNG ADULT, SLIM and AGILE — NOT muscular, NOT robust. Lithe build for tunnel work.",
        "silhouette_icon": "EARS LONGER AND MORE POINTED than other Pax (animalistic trait) + EXPLORATION HARNESS crossing torso with fiber-rope and mineral hooks + MINER-STYLE CRYSTAL HEAD-LAMP on forehead held by a band.",
        "props": "Exploration harness with mineral hooks and fiber-ropes crossing chest, crystal head-lamp fixed by a forehead band, light leather scout boots, tattoos on legs shaped like MAPS AND PATHWAYS.",
        "palette_swatches": "#1F7A7A dark-turquoise, #FF7A2E tunnel-orange, #FFD93D lamp-yellow, #6A4830 explorer-leather, #F5F5DC white-highlights, #0E1A1A deep-accent",
        "palette_short": "dark turquoise + tunnel orange + lamp yellow + explorer leather",
        "default_pose": "slightly crouched in scout stance, alert and ready to move",
        "default_expression": "focused observant look, single eye sharp and alert, slight knowing smirk, ears perked forward",
        "signature_pose": "perched on a rock formation crouched scout-style, one hand on rock, ears perked, eye scanning forward",
        "extra_traits": "Animalistic ears (longer, pointier than others). Lean wiry build, never bulky.",
    },
    "koa": {
        "name": "KOA",
        "role_short": "Adult scribe and historian, ~30-35 years Pax old, meticulous and quiet, Wiz's support",
        "anatomy": "Pax cyclops ADULT WOMAN with ONE ELONGATED INDEX FINGER ON EACH HAND, almost pen-like — animalistic-functional trait for writing. Medium-large eye.",
        "silhouette_icon": "CRYSTAL-INK-WELLS hanging from her belt (crystals used as luminous ink) + MINERAL-FIBER HEADSCARF covering her hair + ELONGATED INDEX FINGER visible.",
        "props": "Ceremonial tunic with pockets for mineral parchments, mineral-fiber headscarf with symbols, crystal ink-wells hanging from belt, RUNE-SHAPED tribal markings on forehead.",
        "palette_swatches": "#4FB0B0 medium-turquoise, #2E2B6E indigo-ink, #D9974A amber-ink, #A07AB5 parchment-violet, #F0E5C9 parchment-white, #161422 deep-accent",
        "palette_short": "medium turquoise + indigo ink + amber ink + parchment violet",
        "default_pose": "upright and calm, one hand near belt ink-wells as if about to write",
        "default_expression": "calm observant quiet look, eye focused with deep attention, very faint serious smile, contemplative",
        "signature_pose": "seated cross-legged writing on a small floating mineral-parchment with her elongated index finger glowing",
        "extra_traits": "Elongated index finger on each hand — visible in every panel. Quiet, meticulous body language.",
    },
}


# ---------------------------------------------------------------------------
# Prompt builders
# ---------------------------------------------------------------------------

def build_v_con_ref_simple_prompt(c):
    return f"""Image 1 shows the LAYOUT TEMPLATE to follow: a horizontal character sheet with three full-body views of the same character on a pure white background — front view, side profile (90 degrees), and back view, all at identical scale.

Image 2 (Jiggy) and Image 3 (Onyx) are EXAMPLES of existing Pax tribe members — provided ONLY so you understand Pax tribe visual style, anatomy and proportions (young-adult range and warrior-adult range). DO NOT REPLICATE Jiggy or Onyx. {c['name']} is a DIFFERENT, NEW Pax tribe character that does not exist yet.

Generate a NEW character design sheet for {c['name']} using EXACTLY the layout of Image 1 (three full-body views: front + side + back, pure white background #FFFFFF, identical scale, neutral standing pose adapted to character — see default pose).

{c['name']} IDENTITY (this is the character to render — NOT Jiggy, NOT Onyx):
- Role: {c['role_short']}
- Anatomy: {c['anatomy']}
- Silhouette icon (must be clearly visible in front, side AND back views): {c['silhouette_icon']}
- Props / outfit: {c['props']}
- Color palette: {c['palette_short']}
- Default body posture: {c['default_pose']}
- Default facial expression: {c['default_expression']}
- Extra: {c['extra_traits']}

PAX TRIBE IDENTITY LOCK (CRITICAL):
ONE single central eye dominating the face. NEVER two eyes. NEVER eye sockets where a second eye would be. This is Pax tribe cyclops anatomy. ONE central eye only. ONE eye. ONE eye.

Render style: 3D PBR Pixar/Disney-quality animation, smooth glossy turquoise skin with subtle subsurface scattering, professional 3D animation reference sheet. NOT 2D, NOT anime, NOT painterly, NOT photorealistic. Cartoonish stylized proportions, three-fingered hands with thumb.

White seamless background everywhere, no environment, no floor shadows except subtle contact shadow under feet. No text labels anywhere in the image.

REMINDER: {c['name']} is a UNIQUE new character. Do NOT replicate Jiggy or Onyx — they are only references for tribe-wide style guidance."""


def build_v_sin_ref_simple_prompt(c):
    return f"""Single character design reference sheet on pure white background (#FFFFFF), horizontal layout, three full-body views of the SAME character at identical scale:
[1] FRONT view — facing camera, in default body posture described below.
[2] SIDE view — full 90-degree profile facing right.
[3] BACK view — facing away from camera.

{TRIBE_DNA}

CHARACTER: {c['name']} of the Pax tribe.

{c['name']} CHARACTER-SPECIFIC IDENTITY:
- Role: {c['role_short']}
- Anatomy: {c['anatomy']}
- Silhouette icon (must be clearly visible in front, side AND back views): {c['silhouette_icon']}
- Props / outfit: {c['props']}
- Color palette: {c['palette_short']}
- Default body posture: {c['default_pose']}
- Default facial expression: {c['default_expression']}
- Extra: {c['extra_traits']}

IDENTITY LOCK (triplicated — this is CRITICAL):
ONE single central eye dominating the face. NEVER two eyes. NO second eye. NO eye sockets where a second eye would be. ONE central eye only.
ONE single central eye. Repeat: ONE eye. Cyclops anatomy. ONE eye.
ONE eye, not two, not zero. Just one large central cyclops eye.

RENDER STYLE: 3D PBR Pixar/Disney-quality animation, professional production-bible character reference sheet. NOT 2D, NOT anime, NOT painterly, NOT photorealistic. Three-point studio lighting, neutral white balance.

White seamless background, no environment, no floor shadows except subtle contact shadows under feet. No text labels anywhere."""


def build_completa_with_simple_prompt(c, is_v_con_ref: bool):
    """Prompt for the COMPLETA sheet that uses (Image 1: template_detail OR simple) + (Image 2: simple)."""
    if is_v_con_ref:
        intro = f"""Image 1 shows the LAYOUT TEMPLATE structure to mimic: a multi-row professional character design sheet with three base views in row 1, action poses in row 2, facial expressions in row 3, details strip and color palette below — all on a clean light background.

Image 2 shows {c['name']} of the Pax tribe — preserve {c['name']}'s identity, anatomy, colors, outfit and accessories EXACTLY as shown in Image 2. {c['name']} is a UNIQUE Pax tribe character (not Jiggy, not Onyx).

Generate a NEW full character design sheet for {c['name']} using the multi-row layout structure of Image 1, on a pure white background (#FFFFFF), professional 3D animation production-bible style."""
    else:
        intro = f"""Image 1 shows {c['name']} of the Pax tribe — preserve {c['name']}'s identity, anatomy, colors, outfit and accessories EXACTLY as shown in Image 1.

Generate a NEW full character design sheet for {c['name']} in professional 3D animation production-bible style, multi-row layout on pure white background (#FFFFFF)."""

    return f"""{intro}

PAX TRIBE IDENTITY LOCK (CRITICAL — repeat in every panel):
ONE single central eye dominating the face. NO second eye, NO eye sockets where a second eye would be. ONE eye only. ONE eye. ONE eye.
Turquoise-green skin base, smooth slightly-glossy PBR texture with subtle subsurface scattering. Wide flexible expressive mouth. Elastic pointed ears. Stylized cartoonish proportions, three-fingered hands with thumb. Faintly glowing bio-luminescent tribal tattoos.

{c['name']}-SPECIFIC IDENTITY (must be preserved in every panel):
- Role: {c['role_short']}
- Anatomy: {c['anatomy']}
- Silhouette icon (must read in every panel): {c['silhouette_icon']}
- Props / outfit: {c['props']}
- Default expression: {c['default_expression']}
- Extra: {c['extra_traits']}

LAYOUT (panels arranged in rows on white background):

ROW 1 — THREE BASE VIEWS (full body, identical scale, default neutral pose):
[1] Front view — facing camera.
[2] Side view — 90-degree profile facing right.
[3] Back view — facing away, head slightly turned 3/4 to read.

ROW 2 — FIVE ACTION POSES (full body, dynamic, role-appropriate):
[4] Walking 3/4 — mid-stride, in-character motion.
[5] Working pose — {c['name']} doing their role activity (apprentice crafting / guarding / healing / scouting / writing).
[6] Signature pose — {c['signature_pose']}.
[7] Interaction pose — {c['name']} interacting with their key prop (crystal / weapon / healing crystals / harness / ink-well).
[8] Iconic personality pose — {c['name']} in a posture that reads their personality at a glance.

ROW 3 — FIVE FACIAL EXPRESSIONS (close-up head-and-shoulders):
[9] Default expression — {c['default_expression']}.
[10] Stronger version of default — same vibe pushed.
[11] Surprised — eye wide open, mouth O-shape.
[12] Sad/concerned — eye droopy, mouth corners down.
[13] Dialog gesture — hand visible at chest gesturing.

ROW 4 — DETAILS STRIP (small isolated icons):
- Silhouette icon item shown isolated.
- Key prop close-up.
- Tribal tattoo or marking detail close-up.
- One additional outfit detail.

ROW 5 — COLOR PALETTE STRIP:
Six color swatches: {c['palette_swatches']}.

UNIFORM CONSTRAINTS:
- Same {c['name']}, same age, same outfit across every panel.
- Same 3-point studio lighting, neutral white balance.
- Pure white seamless background everywhere, no environment, no floor shadows except subtle contact shadow under feet on full-body shots.
- Silhouette icon visibly present in EVERY panel.
- ONE central eye in every panel, no exceptions. NEVER two eyes.
- Render style: 3D PBR Pixar/Disney quality animation. NOT 2D, NOT anime, NOT painterly, NOT photorealistic.
- Avoid text labels except the six small hex codes in the palette strip."""


# ---------------------------------------------------------------------------
# Async helpers
# ---------------------------------------------------------------------------

def _mime_for(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    return {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }.get(ext, "image/png")


async def gen_text(client, sem, label, prompt, output_path, size="1536x1024", quality="high"):
    async with sem:
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
            return {"label": label, "path": output_path, "status": "OK", "time": dt, "size_kb": size_kb}
        except Exception as e:
            return {"label": label, "path": output_path, "status": "FAIL", "error": str(e), "time": time.time() - t0}


async def gen_edit(client, sem, label, prompt, input_paths, output_path, size="1536x1024", quality="high"):
    async with sem:
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
            with open(output_path, "wb") as f:
                f.write(base64.b64decode(image_b64))
            dt = time.time() - t0
            size_kb = os.path.getsize(output_path) / 1024
            return {"label": label, "path": output_path, "status": "OK", "time": dt, "size_kb": size_kb}
        except Exception as e:
            return {"label": label, "path": output_path, "status": "FAIL", "error": str(e), "time": time.time() - t0}


# ---------------------------------------------------------------------------
# Job definitions
# ---------------------------------------------------------------------------

def out_path(slug, variation, sheet):
    return os.path.join(OUT_ROOT, slug, variation, f"{sheet}.png")


def build_simple_jobs(client, sem):
    jobs = []
    for slug, c in CHARS.items():
        # V_con-ref simple
        p1 = out_path(slug, "v-con-ref", "simple")
        if not os.path.exists(p1):
            jobs.append(("simple", slug, "v-con-ref", gen_edit(
                client, sem, f"{c['name']} v-con-ref simple",
                build_v_con_ref_simple_prompt(c),
                [TEMPLATE_SIMPLE, JIGGY_REF, ONYX_REF],
                p1,
            )))
        # V_sin-ref simple
        p2 = out_path(slug, "v-sin-ref", "simple")
        if not os.path.exists(p2):
            jobs.append(("simple", slug, "v-sin-ref", gen_text(
                client, sem, f"{c['name']} v-sin-ref simple",
                build_v_sin_ref_simple_prompt(c),
                p2,
            )))
    return jobs


def build_completa_jobs(client, sem):
    jobs = []
    for slug, c in CHARS.items():
        # V_con-ref completa: needs simple of same variation as the character reference
        simple_con = out_path(slug, "v-con-ref", "simple")
        p1 = out_path(slug, "v-con-ref", "completa")
        if not os.path.exists(p1) and os.path.exists(simple_con):
            jobs.append(("completa", slug, "v-con-ref", gen_edit(
                client, sem, f"{c['name']} v-con-ref completa",
                build_completa_with_simple_prompt(c, is_v_con_ref=True),
                [TEMPLATE_DETAIL, simple_con],
                p1,
            )))
        # V_sin-ref completa: uses ONLY its own simple as reference (image 1 = simple)
        simple_sin = out_path(slug, "v-sin-ref", "simple")
        p2 = out_path(slug, "v-sin-ref", "completa")
        if not os.path.exists(p2) and os.path.exists(simple_sin):
            jobs.append(("completa", slug, "v-sin-ref", gen_edit(
                client, sem, f"{c['name']} v-sin-ref completa",
                build_completa_with_simple_prompt(c, is_v_con_ref=False),
                [simple_sin],
                p2,
            )))
    return jobs


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def run_phase(name, job_tuples):
    if not job_tuples:
        print(f"  (Nothing to do in {name})")
        return []
    print(f"  Dispatching {len(job_tuples)} jobs in parallel (Semaphore={CONCURRENCY})...")
    coros = [t[3] for t in job_tuples]
    results = await asyncio.gather(*coros, return_exceptions=True)
    enriched = []
    for (sheet, slug, variation, _), r in zip(job_tuples, results):
        if isinstance(r, dict):
            r["sheet"] = sheet
            r["slug"] = slug
            r["variation"] = variation
            enriched.append(r)
            tag = r["status"]
            print(f"    [{tag}] {slug}/{variation}/{sheet} - {r.get('time', 0):.1f}s - {r.get('size_kb', 0):.0f}KB")
            if tag == "FAIL":
                print(f"      ERROR: {r.get('error')}")
        else:
            enriched.append({"sheet": sheet, "slug": slug, "variation": variation, "status": "EXC", "error": str(r)})
            print(f"    EXC {slug}/{variation}/{sheet}: {r}")
    return enriched


async def main():
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
    sem = asyncio.Semaphore(CONCURRENCY)

    print("=" * 70)
    print("FASE 1: SIMPLES (10 jobs max — 5 chars x 2 variations)")
    print("=" * 70)
    simple_jobs = build_simple_jobs(client, sem)
    phase1 = await run_phase("FASE 1", simple_jobs)

    # Retry simples faltantes una vez
    missing = []
    for slug in CHARS:
        for variation in ("v-con-ref", "v-sin-ref"):
            p = out_path(slug, variation, "simple")
            if not os.path.exists(p):
                missing.append((slug, variation))
    if missing:
        print(f"\n  RETRY round 1 for {len(missing)} missing simples...")
        retry_jobs = []
        for slug, variation in missing:
            c = CHARS[slug]
            p = out_path(slug, variation, "simple")
            if variation == "v-con-ref":
                retry_jobs.append(("simple", slug, variation, gen_edit(
                    client, sem, f"RETRY {c['name']} {variation} simple",
                    build_v_con_ref_simple_prompt(c),
                    [TEMPLATE_SIMPLE, JIGGY_REF, ONYX_REF],
                    p,
                )))
            else:
                retry_jobs.append(("simple", slug, variation, gen_text(
                    client, sem, f"RETRY {c['name']} {variation} simple",
                    build_v_sin_ref_simple_prompt(c),
                    p,
                )))
        await run_phase("RETRY simples", retry_jobs)

    print()
    print("=" * 70)
    print("FASE 2: COMPLETAS (10 jobs max — 5 chars x 2 variations)")
    print("=" * 70)
    completa_jobs = build_completa_jobs(client, sem)
    phase2 = await run_phase("FASE 2", completa_jobs)

    # Retry completas faltantes una vez
    missing = []
    for slug in CHARS:
        for variation in ("v-con-ref", "v-sin-ref"):
            p = out_path(slug, variation, "completa")
            if not os.path.exists(p):
                missing.append((slug, variation))
    if missing:
        print(f"\n  RETRY round 1 for {len(missing)} missing completas...")
        retry_jobs = []
        for slug, variation in missing:
            c = CHARS[slug]
            p = out_path(slug, variation, "completa")
            simple_p = out_path(slug, variation, "simple")
            if not os.path.exists(simple_p):
                print(f"    SKIP {slug}/{variation}/completa - simple does not exist")
                continue
            if variation == "v-con-ref":
                retry_jobs.append(("completa", slug, variation, gen_edit(
                    client, sem, f"RETRY {c['name']} {variation} completa",
                    build_completa_with_simple_prompt(c, is_v_con_ref=True),
                    [TEMPLATE_DETAIL, simple_p],
                    p,
                )))
            else:
                retry_jobs.append(("completa", slug, variation, gen_edit(
                    client, sem, f"RETRY {c['name']} {variation} completa",
                    build_completa_with_simple_prompt(c, is_v_con_ref=False),
                    [simple_p],
                    p,
                )))
        await run_phase("RETRY completas", retry_jobs)

    # Final summary
    print()
    print("=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)
    rows = []
    for slug in CHARS:
        for variation in ("v-con-ref", "v-sin-ref"):
            for sheet in ("simple", "completa"):
                p = out_path(slug, variation, sheet)
                exists = os.path.exists(p)
                kb = (os.path.getsize(p) / 1024) if exists else 0
                rel = os.path.relpath(p, REPO).replace("\\", "/")
                tag = "OK" if exists else "FAIL"
                rows.append((slug, variation, sheet, rel, tag, kb))
                print(f"  {tag:4}  {rel}  ({kb:.0f} KB)")

    ok = sum(1 for r in rows if r[4] == "OK")
    fail = sum(1 for r in rows if r[4] == "FAIL")
    print(f"\nTOTAL: {ok}/20 OK, {fail}/20 FAIL")


if __name__ == "__main__":
    asyncio.run(main())
