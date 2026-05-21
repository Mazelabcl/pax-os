"""
Video BG v2 generator — 2 videos x 17 prompts x 2 ratios = 68 generations
+ 4 storyboards grid composition with PIL.

Reads:
- content/video-bg-v2/video1-deep-dive/_prompts.md
- content/video-bg-v2/video2-gem-chase/_prompts.md

Outputs:
- content/video-bg-v2/video{1,2}-*/{16x9,9x16}/{inicial,frame-01..frame-15,final}.png
- content/video-bg-v2/video{1,2}-*/{16x9,9x16}/storyboard-grid.png (composed)
- content/video-bg-v2/_final/v{1,2}-{16x9,9x16}-{inicial,final,storyboard}.png (entregables limpios)

Skip-if-exists (>50KB). Concurrency Semaphore=4. Retry-once en moderation/rate/500.

Requires:
    pip install openai pillow
    OPENAI_API_KEY definida en .env.local en la raiz del repo.
"""

import os
import sys
import re
import time
import asyncio
import base64
import shutil

from openai import AsyncOpenAI
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openai_images import _load_env  # noqa: E402
_load_env()

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = "gpt-image-2"
CONCURRENCY = 4
QUALITY = "high"

SIZES = {
    "16x9": "1536x1024",
    "9x16": "1024x1536",
}

VIDEOS = [
    ("video1-deep-dive", "VIDEO 1 - DEEP DIVE INTO PAX WORLD", "v1"),
    ("video2-gem-chase", "VIDEO 2 - GEM MACRO TO CHASE", "v2"),
]


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
# Parser de _prompts.md
# ---------------------------------------------------------------------------
PROMPT_HEADER_RE = re.compile(
    r"^##\s+(prompt-(?:inicial|final|frame-\d{2}))\b",
    re.MULTILINE,
)
CODEBLOCK_RE = re.compile(r"```(?:\w+)?\s*\n(.*?)```", re.DOTALL)
REFS_LINE_RE = re.compile(r"^\s*refs?\s*:\s*\[(.*?)\]\s*$", re.MULTILINE | re.IGNORECASE)
REF_ITEM_RE = re.compile(r'"([^"]+)"|\'([^\']+)\'')


def parse_prompts_md(md_path):
    """Parse a _prompts.md file.

    Returns dict like:
        {
          "prompt-inicial":  {"prompt": "...", "refs": ["public/images/..."]},
          "prompt-frame-01": {"prompt": "...", "refs": [...]},
          ...
          "prompt-final":    {"prompt": "...", "refs": [...]},
        }
    """
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Localizar todos los headers + el rango de texto que les corresponde
    headers = list(PROMPT_HEADER_RE.finditer(text))
    if not headers:
        raise RuntimeError(f"parse: no encontre headers prompt-* en {md_path}")

    out = {}
    for i, m in enumerate(headers):
        key = m.group(1)
        start = m.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        section = text[start:end]

        # Codeblock con el cuerpo
        cb_match = CODEBLOCK_RE.search(section)
        if not cb_match:
            print(f"WARN parse: {key} sin codeblock en {md_path}")
            continue
        body = cb_match.group(1).strip()

        # Refs (linea "refs: [...]" dentro del codeblock)
        refs = []
        refs_match = REFS_LINE_RE.search(body)
        if refs_match:
            for it in REF_ITEM_RE.finditer(refs_match.group(1)):
                ref = it.group(1) or it.group(2)
                if ref:
                    # Normalizar separadores a OS-native
                    refs.append(ref.replace("/", os.sep).replace("\\", os.sep))
            # Quitar la linea refs del prompt body para que no contamine al modelo
            body = REFS_LINE_RE.sub("", body).strip()

        # Quitar tambien notas adyacentes que no son prompt-content
        # ("note for refs:" / "note:") al final.
        body = re.sub(
            r"^\s*note(?:\s+for\s+refs)?\s*:.*$",
            "",
            body,
            flags=re.MULTILINE | re.IGNORECASE,
        ).strip()

        out[key] = {"prompt": body, "refs": refs}

    return out


# ---------------------------------------------------------------------------
# Image generation core
# ---------------------------------------------------------------------------
async def gen_image(client, sem, video_slug, prompt_key, prompt_text, refs_abs, ratio):
    """Genera 1 imagen via edit (con refs) o generate (sin refs)."""
    async with sem:
        # Filename: inicial.png, frame-01.png ... frame-15.png, final.png
        filename = prompt_key.replace("prompt-", "") + ".png"
        out_dir = os.path.join(REPO, "content", "video-bg-v2", video_slug, ratio)
        out_path = os.path.join(out_dir, filename)
        label = f"{video_slug}/{ratio}/{filename}"

        if os.path.exists(out_path) and os.path.getsize(out_path) > 50_000:
            print(f"  [SKIP] {label} ({os.path.getsize(out_path)//1024} KB)")
            return ("SKIP", out_path)

        os.makedirs(out_dir, exist_ok=True)
        size = SIZES[ratio]

        # Verificar refs existen
        usable_refs = [p for p in refs_abs if os.path.exists(p)]
        missing = [p for p in refs_abs if not os.path.exists(p)]
        if missing:
            print(f"  [WARN] {label} refs missing: {missing}")

        for attempt in (1, 2):
            t0 = time.time()
            ts = time.strftime("%H:%M:%S")
            try:
                if usable_refs:
                    file_handles = []
                    file_tuples = []
                    for p in usable_refs:
                        fh = open(p, "rb")
                        file_handles.append(fh)
                        file_tuples.append((os.path.basename(p), fh, _mime_for(p)))
                    try:
                        result = await client.images.edit(
                            model=MODEL,
                            image=file_tuples if len(file_tuples) > 1 else file_tuples[0],
                            prompt=prompt_text,
                            size=size,
                            quality=QUALITY,
                            n=1,
                        )
                    finally:
                        for fh in file_handles:
                            fh.close()
                else:
                    result = await client.images.generate(
                        model=MODEL,
                        prompt=prompt_text,
                        size=size,
                        quality=QUALITY,
                        n=1,
                    )

                b64 = result.data[0].b64_json
                with open(out_path, "wb") as f:
                    f.write(base64.b64decode(b64))

                elapsed = time.time() - t0
                kb = os.path.getsize(out_path) // 1024
                print(f"  [OK  {time.strftime('%H:%M:%S')}] {label} - {elapsed:.1f}s - {kb}KB")
                return ("OK", out_path)
            except Exception as e:
                msg = str(e)
                retriable = (
                    "moderation" in msg.lower()
                    or "rate" in msg.lower()
                    or "500" in msg
                    or "timeout" in msg.lower()
                    or "server" in msg.lower()
                )
                if attempt == 1 and retriable:
                    print(f"  [RETRY {ts}] {label}: {msg[:160]}")
                    await asyncio.sleep(2)
                    continue
                print(f"  [FAIL {ts}] {label}: {msg[:200]}")
                return ("FAIL", msg)


# ---------------------------------------------------------------------------
# Storyboard grid composer (PIL)
# ---------------------------------------------------------------------------
def _load_font(size):
    """Best-effort font load with fallback."""
    for fname in ("arial.ttf", "Arial.ttf", "DejaVuSans.ttf", "verdana.ttf"):
        try:
            return ImageFont.truetype(fname, size)
        except Exception:
            continue
    return ImageFont.load_default()


def compose_storyboard_grid(video_slug, title, ratio):
    """Compose 15 frame-NN.png into a grid (5x3 for 16x9, 3x5 for 9x16).

    Output: content/video-bg-v2/<video_slug>/<ratio>/storyboard-grid.png
    """
    in_dir = os.path.join(REPO, "content", "video-bg-v2", video_slug, ratio)
    frame_paths = [os.path.join(in_dir, f"frame-{i:02d}.png") for i in range(1, 16)]

    missing = [p for p in frame_paths if not os.path.exists(p)]
    if missing:
        print(f"  [SKIP grid] {video_slug}/{ratio}: faltan {len(missing)} frames")
        return None

    if ratio == "16x9":
        cols, rows = 5, 3
    else:  # 9x16
        cols, rows = 3, 5

    first = Image.open(frame_paths[0])
    fw, fh = first.size  # 1536x1024 o 1024x1536

    # Cell size: reducir a la mitad para que el grid total quede manejable.
    cell_w = fw // 2
    cell_h = fh // 2
    margin = 20
    title_h = 80

    total_w = cols * cell_w + (cols + 1) * margin
    total_h = rows * cell_h + (rows + 1) * margin + title_h

    bg_color = (15, 8, 30)  # violeta-oscuro Pax canonico
    grid_img = Image.new("RGB", (total_w, total_h), bg_color)
    draw = ImageDraw.Draw(grid_img)

    # Titulo
    title_font = _load_font(36)
    try:
        bbox = draw.textbbox((0, 0), title, font=title_font)
        title_w = bbox[2] - bbox[0]
    except Exception:
        title_w = len(title) * 18
    draw.text(((total_w - title_w) / 2, 20), title, fill=(230, 200, 120), font=title_font)

    num_font = _load_font(32)

    for i, fp in enumerate(frame_paths):
        col = i % cols
        row = i // cols
        x = margin + col * (cell_w + margin)
        y = title_h + margin + row * (cell_h + margin)

        frame = Image.open(fp).convert("RGB")
        frame_resized = frame.resize((cell_w, cell_h), Image.LANCZOS)
        grid_img.paste(frame_resized, (x, y))

        # Numero del frame en circulo (estilo ejemplo_story)
        num_text = str(i + 1)
        circle_r = 28
        cx = x + 15 + circle_r
        cy = y + 15 + circle_r
        draw.ellipse(
            (cx - circle_r, cy - circle_r, cx + circle_r, cy + circle_r),
            fill=(15, 8, 30),
            outline=(230, 200, 120),
            width=3,
        )
        try:
            nbbox = draw.textbbox((0, 0), num_text, font=num_font)
            nw = nbbox[2] - nbbox[0]
            nh = nbbox[3] - nbbox[1]
        except Exception:
            nw = len(num_text) * 16
            nh = 24
        draw.text((cx - nw / 2, cy - nh / 2 - 4), num_text, fill=(230, 200, 120), font=num_font)

    out_path = os.path.join(in_dir, "storyboard-grid.png")
    grid_img.save(out_path, "PNG")
    kb = os.path.getsize(out_path) // 1024
    print(f"  [GRID OK] {out_path} ({kb} KB, {total_w}x{total_h})")
    return out_path


# ---------------------------------------------------------------------------
# Copy entregables a _final/
# ---------------------------------------------------------------------------
def copy_to_final(video_slug, v_short, ratio):
    """Copia inicial.png, final.png, storyboard-grid.png a _final/ con naming claro."""
    src_dir = os.path.join(REPO, "content", "video-bg-v2", video_slug, ratio)
    dst_dir = os.path.join(REPO, "content", "video-bg-v2", "_final")
    os.makedirs(dst_dir, exist_ok=True)

    for src_name, dst_name in [
        ("inicial.png", f"{v_short}-{ratio}-inicial.png"),
        ("final.png", f"{v_short}-{ratio}-final.png"),
        ("storyboard-grid.png", f"{v_short}-{ratio}-storyboard.png"),
    ]:
        src = os.path.join(src_dir, src_name)
        if os.path.exists(src):
            dst = os.path.join(dst_dir, dst_name)
            shutil.copy2(src, dst)
            print(f"  [COPY] {dst_name}")
        else:
            print(f"  [SKIP copy] no existe {src_name} para {video_slug}/{ratio}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
async def main():
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
    sem = asyncio.Semaphore(CONCURRENCY)

    # Parse ambos .md
    parsed = {}
    for video_slug, _title, _short in VIDEOS:
        md_path = os.path.join(REPO, "content", "video-bg-v2", video_slug, "_prompts.md")
        prompts_dict = parse_prompts_md(md_path)
        parsed[video_slug] = prompts_dict
        print(f"  [PARSED] {video_slug}: {len(prompts_dict)} prompts")

    # Construir tareas: 17 prompts x 2 ratios x 2 videos = 68
    tasks = []
    for video_slug, _title, _short in VIDEOS:
        prompts_dict = parsed[video_slug]
        for prompt_key, prompt_data in prompts_dict.items():
            refs_abs = [os.path.join(REPO, p) for p in prompt_data.get("refs", [])]
            for ratio in SIZES.keys():
                tasks.append(
                    gen_image(
                        client, sem,
                        video_slug, prompt_key,
                        prompt_data["prompt"], refs_abs, ratio,
                    )
                )

    print(f"\n{'=' * 70}")
    print(f"VIDEO BG v2 — lanzando {len(tasks)} generaciones de imagenes")
    print(f"  Concurrency: {CONCURRENCY}")
    print(f"{'=' * 70}\n")

    t_start = time.time()
    results = await asyncio.gather(*tasks, return_exceptions=True)
    t_gen = time.time() - t_start

    ok = sum(1 for r in results if isinstance(r, tuple) and r[0] == "OK")
    skip = sum(1 for r in results if isinstance(r, tuple) and r[0] == "SKIP")
    fail = sum(1 for r in results if isinstance(r, tuple) and r[0] == "FAIL")
    exc = sum(1 for r in results if isinstance(r, Exception))
    print(f"\nGenerations: OK={ok} SKIP={skip} FAIL={fail} EXC={exc} TOTAL={len(tasks)} - {t_gen/60:.1f} min")

    # Compose grids (4 totales: 2 videos x 2 ratios)
    print(f"\n{'=' * 70}")
    print("Componiendo storyboards grids...")
    print(f"{'=' * 70}")
    for video_slug, title, _short in VIDEOS:
        for ratio in SIZES.keys():
            try:
                compose_storyboard_grid(video_slug, title, ratio)
            except Exception as e:
                print(f"  [GRID FAIL] {video_slug}/{ratio}: {str(e)[:200]}")

    # Copy entregables a _final/ (12 totales: 2 videos x 2 ratios x 3 archivos)
    print(f"\n{'=' * 70}")
    print("Copiando entregables a _final/ ...")
    print(f"{'=' * 70}")
    for video_slug, _title, v_short in VIDEOS:
        for ratio in SIZES.keys():
            copy_to_final(video_slug, v_short, ratio)

    print(f"\n{'=' * 70}")
    print("DONE - entregables en content/video-bg-v2/_final/")
    print(f"Tiempo total: {(time.time() - t_start)/60:.1f} min")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    asyncio.run(main())
