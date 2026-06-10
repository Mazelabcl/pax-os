"""
Funciones reusables para generar y editar imagenes con gpt-image-2.

Uso:
    from scripts.openai_images import generate_image, edit_image

    # Texto -> imagen
    generate_image("foto de una manzana roja", "out.png", quality="medium")

    # Texto + imagenes de referencia (Image 1, Image 2, ...)
    edit_image(
        prompt="combina el estilo de Image 1 con el personaje de Image 2",
        input_image_paths=["ref1.png", "ref2.png"],
        output_path="composed.png",
        quality="medium",
    )

Requisitos:
    pip install openai
    OPENAI_API_KEY definida en .env.local en la raiz del repo.
"""

import os
import asyncio
import base64
from openai import OpenAI, AsyncOpenAI


# ---------------------------------------------------------------------------
# Mimetype helper — el SDK de OpenAI no infiere content-type del nombre
# cuando se le pasa solo un file handle. Para .webp termina enviando
# application/octet-stream y la API lo rechaza. Construimos tuples
# (filename, fileobj, mimetype) explicitos para cada input.
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
# Carga de .env y .env.local sin python-dotenv (parser manual).
# Precedencia Next.js: .env primero (defaults), .env.local sobrescribe.
# ---------------------------------------------------------------------------
def _load_env():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for filename in (".env", ".env.local"):  # .env.local gana por orden
        env_path = os.path.join(repo_root, filename)
        if os.path.exists(env_path):
            with open(env_path, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        os.environ[k.strip()] = v.strip()


_load_env()


# ---------------------------------------------------------------------------
# Modelo verificado contra la cuenta del usuario (org Individual + Business
# Approved). Confirmado funcionando: gpt-image-2 (paso 3 del verificador).
# ---------------------------------------------------------------------------
MODEL = "gpt-image-2"

import httpx as _httpx
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    timeout=_httpx.Timeout(180.0, connect=30.0),
)


def generate_image(
    prompt: str,
    output_path: str = "output.png",
    size: str = "1024x1024",
    quality: str = "medium",
    background: str = None,
) -> str:
    """
    Genera una imagen desde texto puro.

    Args:
        prompt: Texto descriptivo en ingles (recomendado por OpenAI).
        output_path: Ruta donde guardar el PNG resultante.
        size: "1024x1024", "1024x1536" (vertical) o "1536x1024" (horizontal).
        quality: "low", "medium" o "high".
        background: "transparent", "opaque" o None (auto). Con "transparent"
            la API devuelve PNG con canal alfa real (soportado por gpt-image).

    Returns:
        output_path tal como se entrego.
    """
    kwargs = dict(model=MODEL, prompt=prompt, size=size, quality=quality)
    if background:
        kwargs["background"] = background
    result = client.images.generate(**kwargs)
    image_base64 = result.data[0].b64_json
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(image_base64))
    return output_path


def edit_image(
    prompt: str,
    input_image_paths,
    output_path: str = "edited.png",
    size: str = "1024x1024",
    quality: str = "medium",
    background: str = None,
) -> str:
    """
    Genera una imagen usando una o varias imagenes de referencia.

    En el prompt referirlas explicitamente como "Image 1, Image 2, ..." en el
    mismo orden que aparecen en input_image_paths. Esa convencion es la que
    gpt-image-2 espera para editar/componer con multiples referencias.

    Args:
        prompt: Texto que describe la edicion / composicion deseada.
        input_image_paths: Lista de rutas a imagenes de referencia
            (PNG/JPG/WEBP). Si pasas solo una, tambien funciona.
        output_path: Ruta del PNG resultante.
        size: idem generate_image.
        quality: idem generate_image.

    Returns:
        output_path tal como se entrego.
    """
    if isinstance(input_image_paths, str):
        input_image_paths = [input_image_paths]

    file_handles = []
    file_tuples = []
    for p in input_image_paths:
        fh = open(p, "rb")
        file_handles.append(fh)
        file_tuples.append((os.path.basename(p), fh, _mime_for(p)))
    try:
        kwargs = dict(
            model=MODEL,
            image=file_tuples if len(file_tuples) > 1 else file_tuples[0],
            prompt=prompt,
            size=size,
            quality=quality,
        )
        if background:
            kwargs["background"] = background
        result = client.images.edit(**kwargs)
    finally:
        for fh in file_handles:
            fh.close()

    image_base64 = result.data[0].b64_json
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(image_base64))
    return output_path


# ---------------------------------------------------------------------------
# Async batch — paralelismo masivo via asyncio.gather + Semaphore
# ---------------------------------------------------------------------------
async def edit_image_async(
    client_async: AsyncOpenAI,
    prompt: str,
    input_image_paths,
    output_path: str,
    size: str = "1024x1024",
    quality: str = "medium",
    background: str = None,
) -> str:
    """Async version of edit_image. Mantiene la misma firma logica."""
    if isinstance(input_image_paths, str):
        input_image_paths = [input_image_paths]

    file_handles = []
    file_tuples = []
    for p in input_image_paths:
        fh = open(p, "rb")
        file_handles.append(fh)
        file_tuples.append((os.path.basename(p), fh, _mime_for(p)))
    try:
        kwargs = dict(
            model=MODEL,
            image=file_tuples if len(file_tuples) > 1 else file_tuples[0],
            prompt=prompt,
            size=size,
            quality=quality,
        )
        if background:
            kwargs["background"] = background
        result = await client_async.images.edit(**kwargs)
    finally:
        for fh in file_handles:
            fh.close()

    image_base64 = result.data[0].b64_json
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(image_base64))
    return output_path


async def generate_batch_async(jobs, max_concurrent: int = 8):
    """
    Ejecuta N jobs de edit_image en paralelo con limite de concurrencia.

    Args:
        jobs: lista de dicts con keys:
            - prompt (str)
            - input_image_paths (list[str])
            - output_path (str)
            - size (str, opcional)
            - quality (str, opcional)
        max_concurrent: limite simultaneo (default 8 para evitar rate limit).

    Returns:
        Lista paralela a jobs con el output_path o la Exception capturada
        (return_exceptions=True para no romper el batch ante 1 error).
    """
    client_async = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
    sem = asyncio.Semaphore(max_concurrent)

    async def with_sem(job):
        async with sem:
            return await edit_image_async(
                client_async=client_async,
                prompt=job["prompt"],
                input_image_paths=job["input_image_paths"],
                output_path=job["output_path"],
                size=job.get("size", "1024x1024"),
                quality=job.get("quality", "medium"),
                background=job.get("background"),
            )

    results = await asyncio.gather(
        *[with_sem(j) for j in jobs],
        return_exceptions=True,
    )
    return results


if __name__ == "__main__":
    # Smoke test end-to-end
    out = generate_image(
        "A simple realistic photo of a red apple on a wooden table.",
        output_path=os.path.join(os.path.dirname(__file__), "test-apple.png"),
        quality="low",
    )
    print(f"Imagen creada: {out}")
