"""
Bulk canon visual v2 — Ambientales (17 imagenes).

Bloque A: 7 fondos solos (generate_image text-only, sin personajes).
Bloque B: 7 renders main-en-ambiente (edit con char canon-final + fondo recien generado).
Bloque C: 3 renders secundario-en-ambiente (edit con char secundario canon + fondo reusado).

Skip-if-exists (>50KB). Concurrency Semaphore=4.
Orden: FASE 1 fondos (A) primero (los renders dependen de los fondos).
       FASE 2 mains (B) + secundarios (C) en paralelo (ambos consumen fondos ya en disco).

Reintenta 1 vez en fallo (incluido moderation_blocked).
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
SIZE = "1536x1024"
QUALITY = "high"

FONDOS_DIR = os.path.join(REPO, "content", "canon-v2", "ambientales", "fondos")
RENDERS_MAINS_DIR = os.path.join(REPO, "content", "canon-v2", "ambientales", "renders-mains")
RENDERS_SECUNDARIOS_DIR = os.path.join(REPO, "content", "canon-v2", "ambientales", "renders-secundarios")


# ---------------------------------------------------------------------------
# BLOQUE A — 7 fondos solos (sin personajes)
# ---------------------------------------------------------------------------

FONDOS_DESC = {
    "jiggy": (
        "Tuneles laberinticos de la tribu Pax, paredes de roca volcanica con vetas de "
        "cristales violetas y magenta brillantes, parkour-friendly: cornisas, salientes y "
        "caidas verticales. Atmosfera energetica, polvo de cristal en el aire, luz indirecta "
        "violeta-magenta."
    ),
    "kz": (
        "Zona de juegos infantil de la tribu Pax, una caverna abierta con cristales pequenos "
        "de muchos colores brillantes (naranja, lima, turquesa) dispersos por el suelo y "
        "paredes, charcos luminosos, estalactitas frangibles, polvo de cristal flotando."
    ),
    "luxa": (
        "Jardin de cristales sagrados, una caverna interior llena de cristales "
        "bioluminescentes en tonos rosados, lavanda y turquesa suave brotando organicamente "
        "de plantas-cristal del suelo y techo, niebla luminosa, atmosfera mistica zen, "
        "agua que cae en cascada lenta."
    ),
    "agatha": (
        "Templo central ceremonial de la tribu Pax, una camara amplia con frescos antiguos "
        "pintados en paredes circulares, columnas de cristal turquesa-purpura iluminadas "
        "desde dentro, altar central con cristales dorados flotantes, atmosfera solemne y "
        "poderosa, luz cenital dorada."
    ),
    "byte": (
        "Taller-laboratorio mineral de la tribu Pax, una camara llena de herramientas "
        "mineral-tribales, bancos de trabajo con cristales fragmentados en uso, lentes "
        "minerales artesanales colgando, cristales-energia orbitando soportes, cables "
        "organicos de mineral colgando del techo, atmosfera nerd-tribal con iluminacion "
        "azul electrico y cobre."
    ),
    "onyx": (
        "Arena de entrenamiento de guerreros Pax, un coliseo subterraneo de piedra basalto "
        "oscura con cristales negros y rojos incrustados en paredes y suelo, marcas de "
        "combate en columnas, armas-cristal apoyadas en racks, atmosfera oscura imponente, "
        "iluminacion rojo-magma desde grietas en el suelo."
    ),
    "wiz": (
        "Archivo-biblioteca antigua de la tribu Pax, una camara circular con repisas de "
        "roca llenas de cristales-pergaminos (rollos minerales con runas brillantes), un "
        "pedestal central con cristal flotante de memoria, atmosfera melancolica y sabia, "
        "motas de polvo dorado, luz cenital blanca pura."
    ),
}


# ---------------------------------------------------------------------------
# BLOQUE B — 7 renders main-en-ambiente
# ---------------------------------------------------------------------------

RENDERS_MAINS = {
    "jiggy": {
        "char_ref": os.path.join(REPO, "content", "canon-v2", "jiggy", "v2-jiggy-base", "simple.png"),
        "fondo": "jiggy",
        "name": "Jiggy",
        "action": (
            "Jiggy in a mid-air parkour leap through a tunnel, dreadlocks flying, smiling, "
            "a violet crystal hanging from his neck, shallow depth of field with motion blur "
            "on the background"
        ),
    },
    "kz": {
        "char_ref": os.path.join(REPO, "content", "canon-v2", "kz", "v3-from-scratch", "simple.png"),
        "fondo": "kz",
        "name": "KZ",
        "action": (
            "KZ running with his huge feet stomping on small crystals that sparkle and burst "
            "with light at contact, laughing wildly, arms flailing"
        ),
    },
    "luxa": {
        "char_ref": os.path.join(REPO, "content", "canon-v2", "luxa", "v3-from-scratch", "simple.png"),
        "fondo": "luxa",
        "name": "Luxa",
        "action": (
            "Luxa in a floating meditation pose in the crystal garden, visible body aura "
            "glowing around her, crystals orbiting both her hands, eyes serene"
        ),
    },
    "agatha": {
        "char_ref": os.path.join(REPO, "content", "canon-v2", "agatha", "v1-fix-actual", "completa.png"),
        "fondo": "agatha",
        "name": "Agatha",
        "action": (
            "Agatha standing at the center of the temple, arms open wide, ceremonial cape "
            "spread behind her, tribal tattoos glowing softly, commanding powerful presence"
        ),
    },
    "byte": {
        "char_ref": os.path.join(REPO, "content", "canon-v2", "byte", "v3-from-scratch", "simple.png"),
        "fondo": "byte",
        "name": "Byte",
        "action": (
            "Byte at his workshop bench manipulating a crystal with his mineral glasses on, "
            "small crystals orbiting around him, focused-curious expression"
        ),
    },
    "onyx": {
        "char_ref": os.path.join(REPO, "content", "canon-v2", "onyx", "v2-jiggy-base", "simple.png"),
        "fondo": "onyx",
        "name": "Onyx",
        "action": (
            "Onyx in a combat stance in the arena, muscular body, visible scars, black "
            "crystals embedded in his armor, determined intense expression"
        ),
    },
    "wiz": {
        "char_ref": os.path.join(REPO, "content", "canon-v2", "wiz", "v2-jiggy-base", "simple.png"),
        "fondo": "wiz",
        "name": "Wiz",
        "action": (
            "Wiz reading a floating crystal-scroll in the archive, staff in one hand, white "
            "beard floating softly, contemplative wise expression"
        ),
    },
}


# ---------------------------------------------------------------------------
# BLOQUE C — 3 renders secundario-en-ambiente
# ---------------------------------------------------------------------------

RENDERS_SECUNDARIOS = {
    "tik": {
        "char_ref": os.path.join(REPO, "content", "canon-v2", "secundarios", "tik", "v-con-ref", "simple.png"),
        "fondo": "byte",  # taller artesano
        "name": "TIK",
        "action": (
            "TIK kneeling in the workshop examining a large crystal with a magnifying-"
            "crystal-tool in hand, apron with hanging small crystals, smile of wonder"
        ),
    },
    "vex": {
        "char_ref": os.path.join(REPO, "content", "canon-v2", "secundarios", "vex", "v-con-ref", "simple.png"),
        "fondo": "onyx",  # arena de combate
        "name": "VEX",
        "action": (
            "VEX standing in the combat arena with one hand on his belt, short cape behind, "
            "mineral eyepatch visible, hard veteran gaze"
        ),
    },
    "mira": {
        "char_ref": os.path.join(REPO, "content", "canon-v2", "secundarios", "mira", "v-con-ref", "simple.png"),
        "fondo": "luxa",  # jardin de cristales
        "name": "MIRA",
        "action": (
            "MIRA kneeling in the crystal garden with a floating crystal in each hand and a "
            "healing arc of light bridging her palms, warm maternal smile"
        ),
    },
}


# ---------------------------------------------------------------------------
# Prompt builders
# ---------------------------------------------------------------------------

def prompt_fondo(slug, desc):
    return f"""Cinematic wide-establishing environment shot of an iconic Pax tribe location. NO CHARACTERS in the scene, environment only.

SCENE: {desc}

PAX TRIBE WORLD DNA: ancient tribal civilization fused with bioluminescent crystal-mineral fantasy. Crystal energy as life-source. Volcanic rock, organic geometry, glowing crystal formations.

Camera: medium-wide cinematic shot, slight low angle to convey scale, depth visible from foreground to background. Atmospheric perspective with subtle volumetric haze.
Lighting: as described in the scene, with soft global illumination and visible volumetric light shafts.
Style: stylized 3D PBR animation, Pixar/Disney quality, NOT 2D, NOT anime, NOT painterly, NOT photorealistic. Production-bible environment art.
Constraints: NO characters of any kind, NO humanoids, NO Pax tribe members visible. Environment plate only. No on-screen text. Aspect 1536x1024."""


def prompt_render(name, action):
    return f"""Cinematic render of {name} of the Pax tribe in their iconic environment. Use the first reference for the character identity (match exactly: anatomy, ONE central eye, props, palette, outfit). Use the second reference for the environment (match atmosphere, lighting, palette, scale).

Scene: {action}.

Camera: medium-wide shot, slight low angle for heroic read, cinematic framing.
Lighting: matches the environment reference. Soft global illumination, subtle volumetric haze.
Style: stylized 3D PBR animation, Pixar/Disney quality, NOT 2D, NOT anime, NOT painterly, NOT photorealistic.
Constraints: ONE central eye, never two eyes. Character is instantly recognizable as the canon design from the first reference. No on-screen text."""


# ---------------------------------------------------------------------------
# Mime helper
# ---------------------------------------------------------------------------

def _mime_for(path):
    ext = os.path.splitext(path)[1].lower()
    return {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }.get(ext, "image/png")


# ---------------------------------------------------------------------------
# Async core generators
# ---------------------------------------------------------------------------

async def _do_generate(client, prompt, output_path):
    result = await client.images.generate(
        model=MODEL,
        prompt=prompt,
        size=SIZE,
        quality=QUALITY,
        n=1,
    )
    b64 = result.data[0].b64_json
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(b64))


async def _do_edit(client, prompt, ref_paths, output_path):
    file_handles = []
    file_tuples = []
    for p in ref_paths:
        fh = open(p, "rb")
        file_handles.append(fh)
        file_tuples.append((os.path.basename(p), fh, _mime_for(p)))
    try:
        result = await client.images.edit(
            model=MODEL,
            image=file_tuples if len(file_tuples) > 1 else file_tuples[0],
            prompt=prompt,
            size=SIZE,
            quality=QUALITY,
            n=1,
        )
    finally:
        for fh in file_handles:
            fh.close()
    b64 = result.data[0].b64_json
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(b64))


# ---------------------------------------------------------------------------
# Job wrappers (skip + retry-once + logging)
# ---------------------------------------------------------------------------

def _skip(output_path, label):
    if os.path.exists(output_path) and os.path.getsize(output_path) > 50_000:
        print(f"  [SKIP] {label}: ya existe ({os.path.getsize(output_path)/1024:.0f} KB)")
        return True
    return False


async def gen_fondo(client, sem, slug, desc):
    label = f"fondo/{slug}"
    out_path = os.path.join(FONDOS_DIR, f"{slug}.png")
    if _skip(out_path, label):
        return {"label": label, "status": "SKIP", "path": out_path}

    prompt = prompt_fondo(slug, desc)
    async with sem:
        t0 = time.time()
        ts = time.strftime("%H:%M:%S")
        print(f"  [START {ts}] {label}")
        for attempt in (1, 2):
            try:
                await _do_generate(client, prompt, out_path)
                dt = time.time() - t0
                kb = os.path.getsize(out_path) / 1024
                print(f"  [OK    {time.strftime('%H:%M:%S')}] {label} - {dt:.1f}s - {kb:.0f}KB")
                return {"label": label, "status": "OK", "path": out_path, "time": dt}
            except Exception as e:
                err = str(e)
                if attempt == 1:
                    print(f"  [RETRY] {label}: {err[:120]}")
                    await asyncio.sleep(2)
                else:
                    print(f"  [FAIL ] {label}: {err[:200]}")
                    return {"label": label, "status": "FAIL", "path": out_path, "error": err}


async def gen_render(client, sem, slug, char_ref, fondo_slug, name, action, render_type):
    label = f"{render_type}/{slug}"
    fondo_path = os.path.join(FONDOS_DIR, f"{fondo_slug}.png")
    out_dir = RENDERS_MAINS_DIR if render_type == "mains" else RENDERS_SECUNDARIOS_DIR
    out_path = os.path.join(out_dir, f"{slug}.png")

    if _skip(out_path, label):
        return {"label": label, "status": "SKIP", "path": out_path}

    # Verificar inputs
    missing = [p for p in [char_ref, fondo_path] if not os.path.exists(p)]
    if missing:
        print(f"  [MISS ] {label}: faltan refs -> {missing}")
        return {"label": label, "status": "MISSING_REF", "path": out_path, "missing": missing}

    prompt = prompt_render(name, action)
    async with sem:
        t0 = time.time()
        ts = time.strftime("%H:%M:%S")
        print(f"  [START {ts}] {label}")
        for attempt in (1, 2):
            try:
                await _do_edit(client, prompt, [char_ref, fondo_path], out_path)
                dt = time.time() - t0
                kb = os.path.getsize(out_path) / 1024
                print(f"  [OK    {time.strftime('%H:%M:%S')}] {label} - {dt:.1f}s - {kb:.0f}KB")
                return {"label": label, "status": "OK", "path": out_path, "time": dt}
            except Exception as e:
                err = str(e)
                if attempt == 1:
                    print(f"  [RETRY] {label}: {err[:120]}")
                    await asyncio.sleep(2)
                else:
                    print(f"  [FAIL ] {label}: {err[:200]}")
                    return {"label": label, "status": "FAIL", "path": out_path, "error": err}


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------

async def main():
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
    sem = asyncio.Semaphore(CONCURRENCY)

    os.makedirs(FONDOS_DIR, exist_ok=True)
    os.makedirs(RENDERS_MAINS_DIR, exist_ok=True)
    os.makedirs(RENDERS_SECUNDARIOS_DIR, exist_ok=True)

    total_planned = len(FONDOS_DESC) + len(RENDERS_MAINS) + len(RENDERS_SECUNDARIOS)
    print(f"\n{'='*70}")
    print(f"AMBIENTALES CANON V2 — total {total_planned} imagenes")
    print(f"  Bloque A: {len(FONDOS_DESC)} fondos solos")
    print(f"  Bloque B: {len(RENDERS_MAINS)} renders main-en-ambiente")
    print(f"  Bloque C: {len(RENDERS_SECUNDARIOS)} renders secundario-en-ambiente")
    print(f"  Concurrency: {CONCURRENCY}")
    print(f"{'='*70}\n")

    t_start = time.time()

    # ---------------------------------------------------------------
    # FASE 1 — Fondos (Bloque A)
    # ---------------------------------------------------------------
    print(f"=== FASE 1: {len(FONDOS_DESC)} fondos solos ===")
    fondos_tasks = [
        gen_fondo(client, sem, slug, desc)
        for slug, desc in FONDOS_DESC.items()
    ]
    fondos_results = await asyncio.gather(*fondos_tasks, return_exceptions=True)

    # ---------------------------------------------------------------
    # FASE 2 — Renders mains + secundarios en paralelo
    # ---------------------------------------------------------------
    print(f"\n=== FASE 2: {len(RENDERS_MAINS)} renders mains + {len(RENDERS_SECUNDARIOS)} secundarios ===")
    render_tasks = []
    for slug, data in RENDERS_MAINS.items():
        render_tasks.append(gen_render(
            client, sem, slug,
            data["char_ref"], data["fondo"], data["name"], data["action"],
            "mains",
        ))
    for slug, data in RENDERS_SECUNDARIOS.items():
        render_tasks.append(gen_render(
            client, sem, slug,
            data["char_ref"], data["fondo"], data["name"], data["action"],
            "secundarios",
        ))
    render_results = await asyncio.gather(*render_tasks, return_exceptions=True)

    # ---------------------------------------------------------------
    # Reporte final
    # ---------------------------------------------------------------
    t_total = time.time() - t_start

    def _summarize(results, title):
        ok = sum(1 for r in results if isinstance(r, dict) and r.get("status") == "OK")
        skip = sum(1 for r in results if isinstance(r, dict) and r.get("status") == "SKIP")
        fail = sum(1 for r in results if isinstance(r, dict) and r.get("status") in ("FAIL", "MISSING_REF"))
        exc = sum(1 for r in results if isinstance(r, Exception))
        print(f"  {title:<35} OK={ok}  SKIP={skip}  FAIL={fail}  EXC={exc}")
        return ok, skip, fail, exc

    print("\n" + "=" * 70)
    print("RESUMEN FINAL")
    print("=" * 70)
    a_ok, a_sk, a_fl, a_ex = _summarize(fondos_results, "Bloque A (fondos)")
    bc_ok, bc_sk, bc_fl, bc_ex = _summarize(render_results, "Bloque B+C (renders)")

    total_ok = a_ok + bc_ok
    total_sk = a_sk + bc_sk
    total_fl = a_fl + bc_fl + a_ex + bc_ex
    print("-" * 70)
    print(f"  TOTAL                               OK={total_ok}  SKIP={total_sk}  FAIL={total_fl}")
    print(f"  Tiempo total: {t_total/60:.1f} min")

    # Detalle de fallas
    fails_detail = []
    for r in list(fondos_results) + list(render_results):
        if isinstance(r, dict) and r.get("status") in ("FAIL", "MISSING_REF"):
            fails_detail.append(r)
        elif isinstance(r, Exception):
            fails_detail.append({"label": "?", "status": "EXC", "error": str(r)})
    if fails_detail:
        print("\nFallas:")
        for f in fails_detail:
            print(f"  - {f.get('label')} [{f.get('status')}] {f.get('error', f.get('missing', ''))}"[:200])

    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())
