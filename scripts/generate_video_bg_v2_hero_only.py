"""
Hero-only video-bg-v2 generator — solo `inicial` y `final` de cada video.

Genera 8 imagenes maximas: 2 videos x 2 prompts (inicial, final) x 2 ratios (16x9, 9x16).
Skip-if-exists (>50KB) — reusa V1 iniciales ya generados.

NO genera frames intermedios, NO compone grids, NO copia a _final/.

Usage:
    python scripts/generate_video_bg_v2_hero_only.py
"""

import os
import sys
import time
import asyncio
import base64

from openai import AsyncOpenAI

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openai_images import _load_env  # noqa: E402
from generate_video_bg_v2 import (  # noqa: E402
    REPO, MODEL, SIZES, QUALITY, VIDEOS, _mime_for, parse_prompts_md,
)

_load_env()

CONCURRENCY = 4
HERO_KEYS = {"prompt-inicial", "prompt-final"}


async def gen_hero(client, sem, video_slug, prompt_key, prompt_text, refs_abs, ratio):
    async with sem:
        filename = f"{prompt_key.replace('prompt-', '')}.png"
        out_dir = os.path.join(REPO, "content", "video-bg-v2", video_slug, ratio)
        out_path = os.path.join(out_dir, filename)

        if os.path.exists(out_path) and os.path.getsize(out_path) > 50_000:
            print(f"SKIP {video_slug}/{ratio}/{filename}")
            return ("SKIP", out_path)

        os.makedirs(out_dir, exist_ok=True)
        size = SIZES[ratio]

        for attempt in range(2):
            try:
                t0 = time.time()
                if refs_abs:
                    file_handles = []
                    file_tuples = []
                    for p in refs_abs:
                        if not os.path.exists(p):
                            print(f"WARN ref missing: {p}")
                            continue
                        fh = open(p, "rb")
                        file_handles.append(fh)
                        file_tuples.append((os.path.basename(p), fh, _mime_for(p)))

                    if file_tuples:
                        result = await client.images.edit(
                            image=file_tuples if len(file_tuples) > 1 else file_tuples[0],
                            prompt=prompt_text,
                            model=MODEL,
                            size=size,
                            quality=QUALITY,
                            n=1,
                        )
                    else:
                        result = await client.images.generate(
                            prompt=prompt_text, model=MODEL, size=size, quality=QUALITY, n=1,
                        )
                    for fh in file_handles:
                        fh.close()
                else:
                    result = await client.images.generate(
                        prompt=prompt_text, model=MODEL, size=size, quality=QUALITY, n=1,
                    )

                b64 = result.data[0].b64_json
                with open(out_path, "wb") as f:
                    f.write(base64.b64decode(b64))
                elapsed = time.time() - t0
                kb = os.path.getsize(out_path) // 1024
                print(f"OK  [{time.strftime('%H:%M:%S')}] {video_slug}/{ratio}/{filename} - {elapsed:.1f}s - {kb}KB")
                return ("OK", out_path)
            except Exception as e:
                msg = str(e)[:200]
                if attempt == 0 and any(x in msg.lower() for x in ("moderation", "rate", "500", "timeout", "server")):
                    print(f"RETRY {video_slug}/{ratio}/{filename}: {msg}")
                    await asyncio.sleep(2)
                    continue
                print(f"FAIL {video_slug}/{ratio}/{filename}: {msg}")
                return ("FAIL", msg)


async def main():
    client = AsyncOpenAI()
    sem = asyncio.Semaphore(CONCURRENCY)

    tasks = []
    for video_slug, _, _ in VIDEOS:
        md_path = os.path.join(REPO, "content", "video-bg-v2", video_slug, "_prompts.md")
        prompts = parse_prompts_md(md_path)
        for key in HERO_KEYS:
            if key not in prompts:
                print(f"WARN: {video_slug} no tiene {key}")
                continue
            pdata = prompts[key]
            refs_abs = [os.path.join(REPO, p) for p in pdata.get("refs", [])]
            for ratio in SIZES.keys():
                tasks.append(gen_hero(client, sem, video_slug, key, pdata["prompt"], refs_abs, ratio))

    print(f"Lanzando {len(tasks)} hero generations (max 8, skip-if-exists)...")
    results = await asyncio.gather(*tasks, return_exceptions=True)

    ok = sum(1 for r in results if isinstance(r, tuple) and r[0] == "OK")
    skip = sum(1 for r in results if isinstance(r, tuple) and r[0] == "SKIP")
    fail = sum(1 for r in results if isinstance(r, tuple) and r[0] == "FAIL")
    print("=" * 70)
    print(f"HERO RESUMEN: OK={ok} SKIP={skip} FAIL={fail} TOTAL={len(tasks)}")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())
