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
import base64
from openai import OpenAI


# ---------------------------------------------------------------------------
# Carga de .env.local sin python-dotenv (parser manual)
# ---------------------------------------------------------------------------
def _load_env():
    env_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        ".env.local",
    )
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

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def generate_image(
    prompt: str,
    output_path: str = "output.png",
    size: str = "1024x1024",
    quality: str = "medium",
) -> str:
    """
    Genera una imagen desde texto puro.

    Args:
        prompt: Texto descriptivo en ingles (recomendado por OpenAI).
        output_path: Ruta donde guardar el PNG resultante.
        size: "1024x1024", "1024x1536" (vertical) o "1536x1024" (horizontal).
        quality: "low", "medium" o "high".

    Returns:
        output_path tal como se entrego.
    """
    result = client.images.generate(
        model=MODEL,
        prompt=prompt,
        size=size,
        quality=quality,
    )
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

    files = [open(p, "rb") for p in input_image_paths]
    try:
        result = client.images.edit(
            model=MODEL,
            image=files if len(files) > 1 else files[0],
            prompt=prompt,
            size=size,
            quality=quality,
        )
    finally:
        for f in files:
            f.close()

    image_base64 = result.data[0].b64_json
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(image_base64))
    return output_path


if __name__ == "__main__":
    # Smoke test end-to-end
    out = generate_image(
        "A simple realistic photo of a red apple on a wooden table.",
        output_path=os.path.join(os.path.dirname(__file__), "test-apple.png"),
        quality="low",
    )
    print(f"Imagen creada: {out}")
