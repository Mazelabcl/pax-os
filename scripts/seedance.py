"""
Seedance via Replicate — wrapper para generar videos a partir de prompts + refs.

Plataforma: Replicate (https://replicate.com). El usuario tiene cuenta Replicate
con `REPLICATE_API_TOKEN`. Antes este script usaba fal.ai — cambio a Replicate
por disponibilidad de keys del usuario.

NO usar OpenRouter: OpenRouter solo expone LLMs de ByteDance, no modelos de video.

Uso basico:
    python scripts/seedance.py

    O importado desde otro script:
        from scripts.seedance import generate_video
        path = generate_video(
            "A violet crystal pulsing on dark rock",
            ratio="16:9",
            duration_s=5,
            quality="lite",
        )

Requiere:
    - REPLICATE_API_TOKEN en .env.local en la raiz del repo.
      Obtener en: https://replicate.com/account/api-tokens
    - pip install requests (obligatorio).
    - pip install replicate (opcional, SDK oficial; el script no la usa pero
      podria sumarse en el futuro). Funciona 100% con REST + requests.

Modelos disponibles en Replicate (mayo 2026):
    Seedance 1 (estable, soporta text-to-video y image-to-video en el mismo endpoint):
      - bytedance/seedance-1-pro            (480p / 1080p, 5s o 10s)
      - bytedance/seedance-1-pro-fast       (Pro mas rapido, 30-60% mas barato que Pro)
      - bytedance/seedance-1-lite           (480p / 720p, 5s o 10s)

    Seedance 2.0 (audio nativo, refs multi-modales, duracion inteligente):
      - bytedance/seedance-2.0              (480p / 720p, multimodal: image, last_frame,
                                             reference_images x9, reference_videos x3,
                                             reference_audios x3, audio nativo)
      - bytedance/seedance-2.0-fast         (variante rapida, misma API)

Por defecto se usa Seedance 1 Lite (cheapest). Para Pro pasar quality="pro",
para Seedance 2.0 pasar quality="v2" o quality="v2-fast".
"""

import os
import sys
import time
import datetime
import re
import base64

# Importar _load_env desde openai_images (carga .env.local sin python-dotenv)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openai_images import _load_env  # noqa: E402

try:
    import requests
except ImportError as e:
    raise ImportError(
        "requests no esta instalado. Ejecuta: pip install requests"
    ) from e


# ---------------------------------------------------------------------------
# Configuracion
# ---------------------------------------------------------------------------

REPLICATE_API_BASE = "https://api.replicate.com/v1"

# Aliases -> model slug en Replicate + default resolution.
# Replicate usa un solo endpoint por modelo. Text-to-video vs image-to-video
# se decide pasando (o no) el campo `image` en el input.
SEEDANCE_MODELS = {
    "lite": {
        "model":      "bytedance/seedance-1-lite",
        "resolution": "720p",
        "version":    "v1",
    },
    "pro": {
        "model":      "bytedance/seedance-1-pro",
        "resolution": "1080p",
        "version":    "v1",
    },
    "pro-fast": {
        "model":      "bytedance/seedance-1-pro-fast",
        "resolution": "1080p",
        "version":    "v1",
    },
    "v2": {
        "model":      "bytedance/seedance-2.0",
        "resolution": "720p",
        "version":    "v2",
    },
    "v2-fast": {
        "model":      "bytedance/seedance-2.0-fast",
        "resolution": "720p",
        "version":    "v2",
    },
}

# Directorio de salida para videos descargados
OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "content", "videos", "seedance",
)

# Polling
POLL_INTERVAL_S = 4
POLL_TIMEOUT_S = 600  # 10 minutos


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _get_api_token() -> str:
    """Carga REPLICATE_API_TOKEN desde env."""
    _load_env()
    token = os.environ.get("REPLICATE_API_TOKEN", "").strip()
    if not token:
        raise EnvironmentError(
            "REPLICATE_API_TOKEN no esta definida. Agregala en .env.local:\n"
            "  REPLICATE_API_TOKEN=r8_...\n"
            "Obtener token en: https://replicate.com/account/api-tokens"
        )
    return token


def _headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type":  "application/json",
    }


def _slugify(text: str, max_len: int = 40) -> str:
    """Convierte texto a slug para nombres de archivo."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text[:max_len].rstrip("-")


def _mime_for(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    return {
        ".png":  "image/png",
        ".jpg":  "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".gif":  "image/gif",
    }.get(ext, "image/png")


def _image_to_data_url(path: str) -> str:
    """
    Encoda una imagen local como data URL base64 para enviar a Replicate.
    Replicate acepta data URLs en cualquier campo de tipo file (recomendado para
    imagenes <10 MB). Para imagenes mas grandes, usar Replicate Files API (no
    implementado aqui — agregar si surge la necesidad).
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Imagen de referencia no encontrada: {path}")

    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    mime = _mime_for(path)
    return f"data:{mime};base64,{b64}"


# ---------------------------------------------------------------------------
# Core
# ---------------------------------------------------------------------------

def generate_video(
    prompt: str,
    ref_image_path: str = None,
    ratio: str = "16:9",
    duration_s: int = 5,
    quality: str = "lite",
    seed: int = None,
    resolution: str = None,
    generate_audio: bool = None,
) -> str:
    """
    Genera un video Seedance via Replicate.

    Args:
        prompt:          Descripcion del video (ingles, formato Pax-Seedance canonico).
        ref_image_path:  Path local a imagen de referencia. Si se pasa, el modelo
                         opera en modo image-to-video (primer frame fijado a la imagen).
                         Si no, text-to-video puro.
        ratio:           "16:9" / "9:16" / "1:1" / "4:3" / "3:4" / "21:9" / "adaptive".
        duration_s:      5 o 10 en v1; en v2.0 acepta -1 (intelligent) o 4-15.
        quality:         "lite" / "pro" / "pro-fast" / "v2" / "v2-fast".
        seed:            Seed para reproducibilidad (opcional).
        resolution:      "480p" / "720p" / "1080p". Si None, usa el default del modelo.
        generate_audio:  Solo Seedance 2.0 — true/false. Si None, default del modelo.

    Returns:
        Path local al video descargado en content/videos/seedance/.

    Raises:
        EnvironmentError:   Si REPLICATE_API_TOKEN no esta definida.
        FileNotFoundError:  Si ref_image_path no existe.
        RuntimeError:       Si el job falla o timeout.
        requests.HTTPError: Si la API responde con error HTTP.
    """
    token = _get_api_token()

    cfg = SEEDANCE_MODELS.get(quality)
    if cfg is None:
        raise ValueError(
            f"quality='{quality}' invalido. Opciones: {list(SEEDANCE_MODELS.keys())}"
        )

    model_slug = cfg["model"]
    final_res = resolution or cfg["resolution"]

    # Construir input del modelo
    model_input: dict = {
        "prompt":       prompt,
        "aspect_ratio": ratio,
        "resolution":   final_res,
        # Replicate Seedance recibe duration como int (segundos)
        "duration":     int(duration_s),
    }
    if seed is not None:
        model_input["seed"] = seed
    if generate_audio is not None and cfg["version"] == "v2":
        # Seedance 2.0 expone audio nativo. El nombre del campo en Replicate es
        # `audio` (boolean). Si en alguna version se llama `generate_audio`,
        # ajustar aqui.
        model_input["audio"] = generate_audio

    if ref_image_path:
        model_input["image"] = _image_to_data_url(ref_image_path)

    print(f"[seedance] Job — model={model_slug} ratio={ratio} duration={duration_s}s res={final_res}")
    print(f"[seedance] Prompt: {prompt[:80]}{'...' if len(prompt) > 80 else ''}")

    result = _run_prediction(model_slug, model_input, token)

    video_url = _extract_video_url(result)
    if not video_url:
        raise RuntimeError(f"Job completado pero sin URL de video. Output: {result.get('output')}")

    return _download_video(video_url, prompt)


def _run_prediction(model_slug: str, model_input: dict, token: str) -> dict:
    """
    Crea una prediction en Replicate y espera a que termine.

    Usa el endpoint `/v1/models/{owner}/{name}/predictions` (no requiere `version`
    si se llama via path del modelo — Replicate usa la version mas reciente).

    Returns:
        dict con la prediction final (`status`, `output`, etc.).
    """
    create_url = f"{REPLICATE_API_BASE}/models/{model_slug}/predictions"
    body = {"input": model_input}

    print(f"[seedance] POST {create_url}")
    resp = requests.post(
        create_url,
        headers=_headers(token),
        json=body,
        timeout=60,
    )

    if resp.status_code == 401:
        raise RuntimeError(
            "401 Unauthorized — REPLICATE_API_TOKEN invalido o expirado. "
            "Regenera el token en https://replicate.com/account/api-tokens"
        )
    if resp.status_code == 402:
        raise RuntimeError(
            "402 Payment Required — sin saldo en Replicate. "
            "Recarga en https://replicate.com/account/billing"
        )
    if resp.status_code == 422:
        raise RuntimeError(
            f"422 Unprocessable Entity — input invalido para {model_slug}. "
            f"Revisa aspect_ratio/resolution/duration segun el model card. "
            f"Detalle: {resp.text}"
        )
    if resp.status_code == 429:
        raise RuntimeError(
            "429 Rate Limit — demasiados requests a Replicate. Espera 30s y reintenta."
        )
    resp.raise_for_status()

    prediction = resp.json()
    prediction_id = prediction.get("id")
    if not prediction_id:
        raise RuntimeError(f"Respuesta de Replicate sin id: {prediction}")

    get_url = prediction.get("urls", {}).get("get") or f"{REPLICATE_API_BASE}/predictions/{prediction_id}"
    print(f"[seedance] prediction id={prediction_id}")

    # Polling
    deadline = time.time() + POLL_TIMEOUT_S
    last_status = None
    while time.time() < deadline:
        time.sleep(POLL_INTERVAL_S)

        poll = requests.get(get_url, headers=_headers(token), timeout=30)
        poll.raise_for_status()
        prediction = poll.json()
        status = prediction.get("status", "")

        if status != last_status:
            print(f"[seedance] status: {status}")
            last_status = status

        if status == "succeeded":
            return prediction
        if status in ("failed", "canceled"):
            err = prediction.get("error") or prediction
            raise RuntimeError(f"Prediction {prediction_id} fallo ({status}): {err}")

    raise RuntimeError(f"Timeout: prediction {prediction_id} no completo en {POLL_TIMEOUT_S}s")


def _extract_video_url(prediction: dict) -> str:
    """
    Extrae la URL del video del campo `output` de una prediction de Replicate.

    Replicate Seedance puede devolver:
      - string directo:        "https://replicate.delivery/.../out.mp4"
      - lista de strings:      ["https://...mp4"]
      - dict con video field:  { "video": "https://...mp4" }
    """
    output = prediction.get("output")
    if isinstance(output, str):
        return output
    if isinstance(output, list) and output:
        first = output[0]
        if isinstance(first, str):
            return first
        if isinstance(first, dict):
            return first.get("url") or first.get("video") or ""
    if isinstance(output, dict):
        return output.get("video") or output.get("url") or ""
    return ""


def _download_video(url: str, prompt: str) -> str:
    """Descarga el .mp4 a OUTPUT_DIR. Devuelve el path local."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    slug = _slugify(prompt)
    filename = f"{timestamp}-{slug}.mp4"
    out_path = os.path.join(OUTPUT_DIR, filename)

    print(f"[seedance] Descargando video -> {out_path}")
    with requests.get(url, stream=True, timeout=180) as r:
        r.raise_for_status()
        with open(out_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    size_mb = os.path.getsize(out_path) / (1024 * 1024)
    print(f"[seedance] Descarga completa: {size_mb:.1f} MB -> {out_path}")
    return out_path


# ---------------------------------------------------------------------------
# CLI / test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Test minimo Pax-canonico. NO ejecutar sin confirmar (consume creditos
    # de Replicate). Requiere REPLICATE_API_TOKEN configurado en .env.local.
    test_prompt = (
        "Subject: A violet-magenta crystal pulsing on dark Pax rock, alone in a void.\n"
        "Action: Slow zoom-out from extreme macro to medium close-up. Single take, no cuts.\n"
        "Camera: One continuous take. No multi-shot.\n"
        "Environment: Subterranean Pax cavern. Dark violet rock with bioluminescent vein patterns.\n"
        "Lighting: Single crystal as only light source. Dark violet void background (#1A0B2E).\n"
        "Style: Stylized 3D PBR animation, painterly cinematic lighting, NOT photorealistic.\n"
        "Constraints: NO surface, NO humans, NO text on screen.\n"
        "Audio: Soft cavern ambient hum, crystal heartbeat at low frequency.\n"
        "Duration: 5 seconds."
    )
    path = generate_video(
        test_prompt,
        ratio="16:9",
        duration_s=5,
        quality="lite",
    )
    print(f"Video generado en: {path}")
