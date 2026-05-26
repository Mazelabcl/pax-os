# Modelos de generación de video IA — Investigación mayo 2026

> **Objetivo:** Identificar el mejor modelo para generar clips de 5–15 s como video de fondo en landings scrolleables del proyecto Pax (estilo 3D PBR neon-magic, control de start/end frame, precio razonable para ~20 clips).

---

## 1. Tabla comparativa — Top 8 modelos

| Modelo | Plataforma | I2V (start frame) | Start+End frame | T2V | Resolución máx | Duración máx | Precio aprox (5 s) | Velocidad | Calidad (Elo / notas) |
|---|---|---|---|---|---|---|---|---|---|
| **Wan 2.7 I2V** | Replicate (`wan-video/wan-2.7-i2v`) / fal.ai (`fal-ai/wan/v2.7`) | ✅ | ✅ first+last frame | ✅ (T2V separado) | 1080p | 15 s | ~$0.35–0.50 | Medio (2–4 min) | Alto — #1 open-weight, 27B MoE, flexible |
| **Kling 3.0 Pro** | Replicate (`kwaivgi/kling-v3-video`) / fal.ai (`fal-ai/kling-video/v3/pro/image-to-video`) | ✅ | ✅ start+end image | ✅ | 1080p | 15 s | ~$0.56 (sin audio) | Medio (2–3 min) | Muy alto — Elo 1243, #1 benchmark I2V |
| **Kling 3.0 Standard** | Replicate / fal.ai (`fal-ai/kling-video/v3/standard/image-to-video`) | ✅ | ✅ | ✅ | 1080p | 15 s | ~$0.42 (sin audio) | Rápido (1–2 min) | Alto |
| **Seedance 2.0** | Replicate (`bytedance/seedance-2.0`) | ✅ | ✅ last_frame en v2 | ✅ | 720p | 15 s | ~$1.24 (pro) / ~$0.45 (fast) | Rápido (fast: 1–2 min) | Muy alto — Elo 1349 I2V, #1 con audio |
| **Seedance 1 Lite** | Replicate (`bytedance/seedance-1-lite`) | ✅ | ❌ | ✅ | 720p | 10 s | ~$0.20–0.30 | Rápido | Medio-alto — ya en uso en Pax |
| **Hailuo 2.3 Pro (MiniMax)** | fal.ai (`fal-ai/minimax/hailuo-2.3/pro/image-to-video`) / Replicate (`minimax/video-01`) | ✅ | ✅ first+last frame | ✅ | 1080p | 6 s | ~$0.49 | Rápido (1–2 min) | Muy alto — #2 global en Artificial Analysis |
| **Hailuo 2.3 Standard** | fal.ai (`fal-ai/minimax/hailuo-2.3/standard/image-to-video`) | ✅ | ✅ | ✅ | 768p | 6 s | ~$0.28 | Rápido | Alto |
| **Veo 3.1 (Google)** | Replicate / fal.ai | ✅ | ❌ confirmado | ✅ | 1080p | 60 s | ~$0.15/s = $0.75 | Lento (3–5 min) | Muy alto — cinematic, coherencia larga |

### Modelos descartados o de menor relevancia

| Modelo | Razón de descarte |
|---|---|
| **CogVideoX** | Open source pero calidad inferior a Wan 2.7, sin soporte end frame en APIs |
| **Mochi** | Proyecto experimental, no disponible en producción estable |
| **Luma Dream Machine** | No disponible en Replicate/fal.ai como API directa |
| **Runway Gen-4.5** | Solo API propia (no Replicate/fal.ai), precio premium ($0.15/s+) |
| **Stable Video Diffusion** | Obsoleto frente a Wan 2.7 y Seedance 2.0, max 4 s |
| **Pika** | API propia, no disponible en Replicate/fal.ai |

---

## 2. Recomendación Top 3

### 🥇 #1 — Wan 2.7 I2V (Replicate: `wan-video/wan-2.7-i2v`)

**Por qué para Pax:**
- **Start + end frame nativo** — Exactamente lo que necesitas para scroll-driven video: defines frame A (inicio de sección) y frame B (fin de sección), el modelo genera la transición.
- **Open-weight** — Precios competitivos, múltiples proveedores (Replicate, fal.ai, Together AI, WaveSpeed).
- **1080p + 15 s** — Resolución y duración suficientes para background video.
- **Audio sync opcional** — Si en algún momento se quiere sonido ambiente.
- **Precio razonable** — ~$0.07–0.10/segundo, un clip de 5 s sale ~$0.35–0.50.
- **27B MoE** — Calidad de movimiento fluida, buena con escenas estilizadas y efectos de iluminación (cristales, neon, partículas).

**Limitación:** No es el #1 absoluto en calidad cinematográfica (eso es Kling 3.0), pero la relación calidad/precio/flexibilidad es la mejor.

### 🥈 #2 — Kling 3.0 Standard (fal.ai: `fal-ai/kling-video/v3/standard/image-to-video`)

**Por qué:**
- **#1 en benchmarks de calidad** — Elo 1243, el más alto de todos los modelos de video.
- **Start + end frame** — Soporte completo.
- **Movimiento cinematográfico** — Excelente para tomas lentas, zooms suaves, paneos (ideal para backgrounds).
- **1080p nativo** — Sin upscaling.

**Limitación:** Más caro que Wan (~$0.084/s sin audio). Para 20 clips se nota.

### 🥉 #3 — Seedance 2.0 Fast (Replicate: `bytedance/seedance-2.0-fast`)

**Por qué:**
- **Ya integrado en el proyecto** — El script `scripts/seedance.py` ya funciona con Replicate y el patrón de código es idéntico.
- **Soporte last_frame en v2** — Permite control de destino.
- **Precio competitivo** — ~$0.09/s, un clip de 5 s sale ~$0.45.
- **Audio nativo** — Si quieres sonido ambiente integrado.

**Limitación:** Resolución máxima 720p (suficiente para background pero no para hero video). Inferior a Kling 3.0 en calidad de movimiento cinematográfico.

---

## 3. Modelo recomendado para Pax

### **Wan 2.7 I2V** en Replicate — la mejor opción global

**Justificación específica para el proyecto:**

1. **Control start+end frame es CLAVE para scroll-driven video.** Pax necesita que cada clip sea una transición predecible entre dos estados visuales (ej: cristal apagado → cristal encendido, cueva oscura → cueva iluminada). Wan 2.7 es el modelo open-weight que mejor maneja esto.

2. **Estilo 3D PBR neon-magic.** Wan 2.7 maneja bien escenas estilizadas con iluminación dramática. No es fotorrealista por defecto (lo cual es exactamente lo que Pax necesita).

3. **Precio para 20 clips.** A $0.07–0.10/s, 20 clips de 7 s promedio = ~$10–14. Muy razonable para experimentar.

4. **Ya tienes cuenta Replicate** con `REPLICATE_API_TOKEN` configurado.

5. **Fallback plan:** Si algún clip no queda bien con Wan, usa Kling 3.0 Standard para ese clip específico (~$0.42/clip de 5s). Mix de modelos, no lock-in.

**Estrategia propuesta:**
- Wan 2.7 I2V para el 80% de clips (transiciones genéricas, ambientes, texturas).
- Kling 3.0 Standard para el 20% restante (clips hero, tomas de personajes, movimiento complejo).
- Seedance 2.0 como backup ya que el script ya existe.

---

## 4. Ejemplo de código — Wan 2.7 I2V en Replicate

Script siguiendo el patrón de `scripts/seedance.py`:

```python
"""
Wan 2.7 I2V via Replicate — genera video con control de start + end frame.

Uso:
    python scripts/wan_video.py

    O importado:
        from scripts.wan_video import generate_wan_video
        path = generate_wan_video(
            prompt="Slow zoom out from glowing crystal",
            start_image="public/pax/crystal-start.png",
            end_image="public/pax/crystal-end.png",
            duration_s=7,
        )

Requiere:
    - REPLICATE_API_TOKEN en .env.local
    - pip install requests
"""

import os
import sys
import time
import datetime
import re
import base64

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openai_images import _load_env  # noqa: E402

try:
    import requests
except ImportError as e:
    raise ImportError("requests no esta instalado. Ejecuta: pip install requests") from e


# ---------------------------------------------------------------------------
# Configuracion
# ---------------------------------------------------------------------------

REPLICATE_API_BASE = "https://api.replicate.com/v1"

# Modelo principal: Wan 2.7 I2V (image-to-video con first+last frame)
WAN_MODEL = "wan-video/wan-2.7-i2v"

# Directorio de salida
OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "content", "videos", "wan",
)

POLL_INTERVAL_S = 5
POLL_TIMEOUT_S = 600  # 10 min


# ---------------------------------------------------------------------------
# Helpers (reutilizados de seedance.py)
# ---------------------------------------------------------------------------

def _get_api_token() -> str:
    _load_env()
    token = os.environ.get("REPLICATE_API_TOKEN", "").strip()
    if not token:
        raise EnvironmentError(
            "REPLICATE_API_TOKEN no esta definida. Agregala en .env.local"
        )
    return token


def _headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }


def _slugify(text: str, max_len: int = 40) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text[:max_len].rstrip("-")


def _mime_for(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    return {
        ".png": "image/png", ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg", ".webp": "image/webp",
    }.get(ext, "image/png")


def _image_to_data_url(path: str) -> str:
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Imagen no encontrada: {path}")
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f"data:{_mime_for(path)};base64,{b64}"


# ---------------------------------------------------------------------------
# Core
# ---------------------------------------------------------------------------

def generate_wan_video(
    prompt: str,
    start_image: str = None,
    end_image: str = None,
    duration_s: int = 7,
    resolution: str = "720p",
    aspect_ratio: str = "16:9",
    seed: int = None,
) -> str:
    """
    Genera video con Wan 2.7 I2V via Replicate.

    Args:
        prompt:       Descripcion del movimiento/escena.
        start_image:  Path local a imagen de inicio (first frame).
        end_image:    Path local a imagen final (last frame). Opcional.
        duration_s:   Duracion en segundos (3–15).
        resolution:   "480p" / "720p" / "1080p".
        aspect_ratio: "16:9" / "9:16" / "1:1".
        seed:         Seed para reproducibilidad.

    Returns:
        Path local al video descargado.
    """
    token = _get_api_token()

    model_input = {
        "prompt": prompt,
        "duration": duration_s,
        "resolution": resolution,
        "aspect_ratio": aspect_ratio,
    }

    if start_image:
        model_input["image"] = _image_to_data_url(start_image)

    if end_image:
        model_input["last_frame"] = _image_to_data_url(end_image)

    if seed is not None:
        model_input["seed"] = seed

    print(f"[wan] Job — model={WAN_MODEL} ratio={aspect_ratio} "
          f"duration={duration_s}s res={resolution}")
    print(f"[wan] Prompt: {prompt[:80]}{'...' if len(prompt) > 80 else ''}")
    if start_image:
        print(f"[wan] Start frame: {start_image}")
    if end_image:
        print(f"[wan] End frame: {end_image}")

    # Crear prediction
    create_url = f"{REPLICATE_API_BASE}/models/{WAN_MODEL}/predictions"
    resp = requests.post(
        create_url, headers=_headers(token),
        json={"input": model_input}, timeout=60,
    )

    if resp.status_code in (401, 402, 422, 429):
        raise RuntimeError(f"{resp.status_code}: {resp.text}")
    resp.raise_for_status()

    prediction = resp.json()
    prediction_id = prediction.get("id")
    get_url = (prediction.get("urls", {}).get("get")
               or f"{REPLICATE_API_BASE}/predictions/{prediction_id}")

    print(f"[wan] prediction id={prediction_id}")

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
            print(f"[wan] status: {status}")
            last_status = status
        if status == "succeeded":
            break
        if status in ("failed", "canceled"):
            raise RuntimeError(
                f"Prediction {prediction_id} fallo: {prediction.get('error')}"
            )
    else:
        raise RuntimeError(f"Timeout: {prediction_id} no completo en {POLL_TIMEOUT_S}s")

    # Extraer URL del video
    output = prediction.get("output")
    video_url = ""
    if isinstance(output, str):
        video_url = output
    elif isinstance(output, list) and output:
        video_url = output[0] if isinstance(output[0], str) else ""
    elif isinstance(output, dict):
        video_url = output.get("video") or output.get("url") or ""

    if not video_url:
        raise RuntimeError(f"Sin URL de video en output: {output}")

    # Descargar
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{ts}-{_slugify(prompt)}.mp4"
    out_path = os.path.join(OUTPUT_DIR, filename)

    print(f"[wan] Descargando -> {out_path}")
    with requests.get(video_url, stream=True, timeout=180) as r:
        r.raise_for_status()
        with open(out_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    size_mb = os.path.getsize(out_path) / (1024 * 1024)
    print(f"[wan] Listo: {size_mb:.1f} MB -> {out_path}")
    return out_path


# ---------------------------------------------------------------------------
# CLI / test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    test_prompt = (
        "Slow push-in through dark crystalline cavern. "
        "Violet and jade bioluminescent veins pulse rhythmically on basalt walls. "
        "A single amber crystal floats at center, rotating slowly. "
        "Volumetric fog, particles. Stylized 3D PBR look, NOT photorealistic. "
        "Cinematic, single continuous take, no cuts."
    )
    path = generate_wan_video(
        prompt=test_prompt,
        duration_s=7,
        resolution="720p",
        aspect_ratio="16:9",
    )
    print(f"Video generado en: {path}")
```

---

## 5. Estimacion de costo — 20 clips de 5–10 s

### Escenario A: Solo Wan 2.7 I2V (recomendado)

| Parametro | Valor |
|---|---|
| Clips | 20 |
| Duracion promedio | 7 s |
| Resolucion | 720p |
| Costo por segundo | ~$0.08 |
| **Costo total** | **20 x 7 x $0.08 = $11.20** |

Considerando 1–2 re-generaciones por clip (no todo queda bien al primer intento):

| Con retries (x1.5) | **~$16.80** |
|---|---|

### Escenario B: Mix Wan 2.7 (80%) + Kling 3.0 Standard (20%)

| Modelo | Clips | Dur. prom. | Costo/s | Subtotal |
|---|---|---|---|---|
| Wan 2.7 I2V | 16 | 7 s | $0.08 | $8.96 |
| Kling 3.0 Std | 4 | 7 s | $0.084 | $2.35 |
| **Total** | 20 | — | — | **$11.31** |

Con retries (x1.5): **~$16.97**

### Escenario C: Solo Seedance 2.0 Fast (si se quiere usar el script existente)

| Parametro | Valor |
|---|---|
| Clips | 20 |
| Duracion promedio | 7 s |
| Costo por segundo | ~$0.09 |
| **Costo total** | **20 x 7 x $0.09 = $12.60** |

Con retries: **~$18.90**

### Resumen de costos

| Estrategia | Costo base | Con retries |
|---|---|---|
| Solo Wan 2.7 | $11.20 | ~$16.80 |
| Mix Wan + Kling | $11.31 | ~$16.97 |
| Solo Seedance 2.0 Fast | $12.60 | ~$18.90 |

**Conclusion:** Cualquier estrategia cuesta entre $11–19 para 20 clips. Extremadamente accesible.

---

## 6. Fuentes

- [10 Best Image-To-Video Generators In 2026 — fal.ai](https://fal.ai/learn/tools/ai-image-to-video-generators)
- [AI API Comparison 2026: FAL.AI vs Replicate — TeamDay.ai](https://www.teamday.ai/blog/ai-image-video-api-providers-comparison-2026)
- [Best AI Video Generation Models 2025-2026 — DualView](https://www.dualview.ai/blog/ai-tools/best-ai-video-models.html)
- [Replicate: Kling Video 3.0](https://replicate.com/kwaivgi/kling-v3-video)
- [Replicate: Wan Video collection](https://replicate.com/collections/wan-video)
- [Replicate: wan-video/wan-2.7-i2v](https://replicate.com/wan-video/wan-2.7-i2v)
- [fal.ai: Kling Video v3 Pro I2V](https://fal.ai/models/fal-ai/kling-video/v3/pro/image-to-video)
- [fal.ai: MiniMax Hailuo 2.3 Pro I2V](https://fal.ai/models/fal-ai/minimax/hailuo-2.3/pro/image-to-video)
- [fal.ai: Wan 2.7](https://fal.ai/wan-2.7)
- [AI Video Generation API Pricing April 2026 — BuildMVPFast](https://www.buildmvpfast.com/api-costs/ai-video)
- [Cheapest AI Video Generation APIs 2026 — Atlas Cloud](https://www.atlascloud.ai/blog/guides/cheapest-ai-video-generation-api-2026)
- [Wan 2.7 vs Seedance 2.0 vs Kling 3.0 — Atlas Cloud](https://www.atlascloud.ai/blog/guides/wan-2.7-vs-seedance-2.0-vs-kling-3.0-which-video-api-should-developers-choose)
- [Image-to-Video Leaderboard — Artificial Analysis](https://artificialanalysis.ai/video/leaderboard/image-to-video)
- [AI Video API Pricing 2026 — DevTk](https://devtk.ai/en/blog/ai-video-generation-pricing-2026/)
