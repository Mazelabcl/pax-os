"""
Genera los assets PNG del juego Pax Flight 2D (public/game/2d/assets/)
con gpt-image-2 + background transparente.

Uso:
    python scripts/gen_game2d_assets.py            # genera todo
    python scripts/gen_game2d_assets.py jiggy-idle # regenera uno solo
"""

import os
import sys
import base64
import asyncio

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openai_images import AsyncOpenAI, _mime_for  # noqa: E402  (carga .env.local)

# gpt-image-2 NO soporta background transparente (verificado 2026-06-09:
# error 400 invalid_value). gpt-image-1 SI lo soporta -> sprites con alfa
# van por gpt-image-1; fondos opacos por gpt-image-2.
MODEL_TRANSPARENT = "gpt-image-1"
MODEL_OPAQUE = "gpt-image-2"

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(REPO, "public", "game", "2d", "assets")
JIGGY_REF = os.path.join(REPO, "_lore", "personajes", "jiggy.png")
os.makedirs(ASSETS, exist_ok=True)

JIGGY_BASE = (
    "Image 1 is the character reference. Game sprite of this turquoise cyclops "
    "character {pose}, side view facing right, TRANSPARENT background, clean "
    "silhouette, 3D Pixar style render, rim lighting jade, game asset"
)

OBSTACLE_BASE = (
    "Game asset sprite: organic dark basalt {form} rock formation {direction}, "
    "embedded glowing jade and magenta crystals, strong rim light on edges, "
    "dark stone with bright crystal accents, TRANSPARENT background, "
    "side-scroller game obstacle, 3D stylized render"
)

SOMBRA = (
    "Game enemy sprite: dark shadowy wispy creature, semi-transparent black "
    "smoke body, two glowing violet eyes, menacing but stylized for all ages, "
    "TRANSPARENT background, 3D stylized render{variant}"
)

# jobs: name -> dict(kind, prompt, size, background)
JOBS = {
    "jiggy-idle": dict(
        kind="edit", refs=[JIGGY_REF], size="1024x1024", background="transparent",
        prompt=JIGGY_BASE.format(
            pose="sitting cross-legged on a floating faceted jade crystal mount, relaxed pose"),
    ),
    "jiggy-pulse": dict(
        kind="edit", refs=[JIGGY_REF], size="1024x1024", background="transparent",
        prompt=JIGGY_BASE.format(
            pose="sitting on a floating faceted jade crystal mount, leaning forward "
                 "with arms raised, energy pulse pose, crystal glowing intensely"),
    ),
    "jiggy-fall": dict(
        kind="edit", refs=[JIGGY_REF], size="1024x1024", background="transparent",
        prompt=JIGGY_BASE.format(
            pose="sitting on a floating faceted jade crystal mount, tilted downward, "
                 "falling pose, worried expression"),
    ),
    "stalactite-1": dict(
        kind="gen", size="1024x1536", background="transparent",
        prompt=OBSTACLE_BASE.format(form="stalactite", direction="hanging downward from the top"),
    ),
    "stalactite-2": dict(
        kind="gen", size="1024x1536", background="transparent",
        prompt=OBSTACLE_BASE.format(
            form="stalactite", direction="hanging downward from the top, different jagged shape variation"),
    ),
    "stalagmite-1": dict(
        kind="gen", size="1024x1536", background="transparent",
        prompt=OBSTACLE_BASE.format(form="stalagmite", direction="rising upward from ground"),
    ),
    "stalagmite-2": dict(
        kind="gen", size="1024x1536", background="transparent",
        prompt=OBSTACLE_BASE.format(
            form="stalagmite", direction="rising upward from ground, different jagged shape variation"),
    ),
    "sombra-1": dict(
        kind="gen", size="1024x1024", background="transparent",
        prompt=SOMBRA.format(variant=""),
    ),
    "sombra-2": dict(
        kind="gen", size="1024x1024", background="transparent",
        prompt=SOMBRA.format(
            variant=", slightly different smoke wisps shape (animation frame 2 of the same creature)"),
    ),
    "bg-far": dict(
        kind="gen", size="1536x1024", background=None,
        prompt=(
            "Seamless HORIZONTALLY TILEABLE game background: deep dark underground "
            "cavern wall, very dark basalt #0F0F18, faint distant glowing crystals "
            "jade and magenta, atmospheric depth, the LEFT and RIGHT edges must "
            "connect perfectly when tiled, muted and dark (background layer, low contrast)"),
    ),
    "bg-mid": dict(
        kind="gen", size="1536x1024", background="transparent",
        prompt=(
            "Seamless HORIZONTALLY TILEABLE game background layer: mid-distance dark "
            "basalt rock formations and crystal clusters rising from the bottom, "
            "slightly more visible than a far layer but still dark and low contrast, "
            "faint jade and magenta crystal glints, the LEFT and RIGHT edges must "
            "connect perfectly when tiled, TRANSPARENT background on the top half "
            "of the image (only rocks on the lower part)"),
    ),
    "crystal-rare": dict(
        kind="gen", size="1024x1024", background="transparent",
        prompt=(
            "Game collectible sprite: large faceted magenta crystal, intense glow, "
            "TRANSPARENT background, 3D stylized render, game asset"),
    ),
}


async def run_job(client_async, sem, name, job):
    out = os.path.join(ASSETS, f"{name}.png")
    model = MODEL_TRANSPARENT if job["background"] == "transparent" else MODEL_OPAQUE
    async with sem:
        try:
            kwargs = dict(model=model, prompt=job["prompt"],
                          size=job["size"], quality="medium")
            if job["background"]:
                kwargs["background"] = job["background"]
            if job["kind"] == "edit":
                handles, tuples_ = [], []
                for p in job["refs"]:
                    fh = open(p, "rb")
                    handles.append(fh)
                    tuples_.append((os.path.basename(p), fh, _mime_for(p)))
                try:
                    kwargs["image"] = tuples_ if len(tuples_) > 1 else tuples_[0]
                    result = await client_async.images.edit(**kwargs)
                finally:
                    for fh in handles:
                        fh.close()
            else:
                result = await client_async.images.generate(**kwargs)
            with open(out, "wb") as f:
                f.write(base64.b64decode(result.data[0].b64_json))
            print(f"OK   {name} ({model})")
            return (name, "ok")
        except Exception as e:
            print(f"FAIL {name}: {e}")
            return (name, f"fail: {e}")


async def main(only=None):
    client_async = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
    sem = asyncio.Semaphore(4)
    jobs = {k: v for k, v in JOBS.items() if (only is None or k in only)}
    results = await asyncio.gather(*[run_job(client_async, sem, n, j) for n, j in jobs.items()])
    fails = [r for r in results if r[1] != "ok"]
    print(f"\n{len(results) - len(fails)}/{len(results)} ok")
    if fails:
        for n, msg in fails:
            print(f"  - {n}: {msg}")
        sys.exit(1)


if __name__ == "__main__":
    only = set(sys.argv[1:]) or None
    asyncio.run(main(only))
