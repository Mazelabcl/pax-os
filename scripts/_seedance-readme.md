# Seedance via Replicate — Guia de uso

Script: `scripts/seedance.py`
Output: `content/videos/seedance/<timestamp>-<slug>.mp4`

> **Importante:** Seedance corre en **Replicate**. OpenRouter solo expone LLMs de ByteDance (`bytedance-seed/seed-2.0-*`), **no** modelos de generacion de video.

> **Migracion:** Antes este script usaba fal.ai. Cambio a Replicate por disponibilidad de keys del usuario. La firma publica de `generate_video()` se mantiene backwards-compatible — los scripts que ya importaban este modulo siguen funcionando, solo cambia la env var (`FAL_KEY` -> `REPLICATE_API_TOKEN`) y los alias de `quality` (se agrego `"pro-fast"`).

---

## 1. Variables de entorno

En `.env.local` (raiz del repo):

```
REPLICATE_API_TOKEN=r8_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Obtener el token:** https://replicate.com/account/api-tokens

> Replicate usa header `Authorization: Bearer <token>` (no `Token` ni `Key`). El script ya lo maneja correctamente.

---

## 2. Instalacion

```bash
pip install requests
```

Solo `requests` es obligatorio. El SDK `pip install replicate` no se usa aqui — el script habla REST puro contra `api.replicate.com`.

---

## 3. Como usar

### Desde terminal

```bash
# Desde la raiz del repo
python scripts/seedance.py
```

Ejecuta el test minimo definido en `__main__` (5 segundos, modelo Lite, sin imagen de referencia). Requiere `REPLICATE_API_TOKEN` configurado.

### Importado desde otro script

```python
from scripts.seedance import generate_video

# Text-to-video (sin imagen de referencia)
out_path = generate_video(
    prompt="A violet crystal pulsing on dark Pax basalt, 5s, cinematic.",
    ratio="16:9",
    duration_s=5,
    quality="lite",
    seed=42,
)
print(f"Video: {out_path}")

# Image-to-video (con imagen de referencia)
out_path = generate_video(
    prompt="The character slowly turns its head, crystal in hand glows brighter.",
    ref_image_path="personajes finales/Jiggy_Character.png",
    ratio="16:9",
    duration_s=5,
    quality="pro",
)
```

### Parametros

| Parametro | Tipo | Default | Descripcion |
|---|---|---|---|
| `prompt` | str | requerido | Descripcion del video. Ingles, formato Pax-Seedance canonico. |
| `ref_image_path` | str | None | Path local a imagen de referencia. Si se pasa, el modelo opera en modo **image-to-video** (primer frame fijado a la imagen). Si no, **text-to-video**. La imagen se enconda como data URL base64 inline. Para imagenes >10 MB, sube manualmente via Replicate Files API y pasa la URL. |
| `ratio` | str | `"16:9"` | `"16:9"` / `"9:16"` / `"1:1"` / `"4:3"` / `"3:4"` / `"21:9"` / `"adaptive"` (v2). |
| `duration_s` | int | `5` | Segundos: 5 o 10 en v1; en v2.0 acepta 4-15 o `-1` (intelligent). |
| `quality` | str | `"lite"` | `"lite"` / `"pro"` / `"pro-fast"` / `"v2"` / `"v2-fast"`. Ver tabla de modelos. |
| `seed` | int | None | Seed para reproducibilidad. |
| `resolution` | str | None | `"480p"` / `"720p"` / `"1080p"`. Si None, usa el default del modelo. |
| `generate_audio` | bool | None | Solo Seedance 2.0. Audio nativo (mapea a campo `audio` en input). |

---

## 4. Modelos disponibles en Replicate (mayo 2026)

### Seedance 1 — estable, text-to-video + image-to-video en el mismo endpoint

| Alias | Replicate slug | Resoluciones | Duracion |
|---|---|---|---|
| `"lite"` | `bytedance/seedance-1-lite` | 480p, 720p | 5s, 10s |
| `"pro"` | `bytedance/seedance-1-pro` | 480p, 1080p | 5s, 10s |
| `"pro-fast"` | `bytedance/seedance-1-pro-fast` | 480p, 1080p | 5s, 10s |

Replicate consolido text-to-video y image-to-video en un solo endpoint por modelo. Si pasas `ref_image_path`, el script setea el campo `image` del input y el modelo opera en modo image-to-video automaticamente.

### Seedance 2.0 — multimodal, audio nativo

| Alias | Replicate slug | Resolucion | Duracion |
|---|---|---|---|
| `"v2"` | `bytedance/seedance-2.0` | 480p, 720p | 4-15s o `-1` (intelligent) |
| `"v2-fast"` | `bytedance/seedance-2.0-fast` | 480p, 720p | 4-15s o `-1` |

Seedance 2.0 expone refs multi-modales (`reference_images` x9, `reference_videos` x3, `reference_audios` x3, `last_frame_image`) y `audio: true/false` para audio nativo. Este wrapper expone solo el campo `image` y `audio` — para los demas campos avanzados, llama Replicate directamente o extiende `model_input` en `generate_video()`.

---

## 5. Costos aproximados en Replicate (mayo 2026)

Replicate factura Seedance por segundo de video generado. Precios oficiales en cada model card; valores aproximados al cierre de mayo 2026:

| Modelo | Precio aprox. | 5s | 10s |
|---|---|---|---|
| Seedance 1 Lite (720p) | ~$0.03 / s | ~$0.15 | ~$0.30 |
| Seedance 1 Pro (1080p) | ~$0.10 / s | ~$0.50 | ~$1.00 |
| Seedance 1 Pro Fast (1080p) | ~$0.04 / s | ~$0.20 | ~$0.40 |
| Seedance 2.0 (720p) | ~$0.18 / s | ~$0.90 | ~$1.80 |
| Seedance 2.0 Fast (720p) | ~$0.08 / s | ~$0.40 | ~$0.80 |

> Replicate publica precios reales en cada model card. Verifica antes de correr lotes grandes:
> - https://replicate.com/bytedance/seedance-1-pro
> - https://replicate.com/bytedance/seedance-1-pro-fast
> - https://replicate.com/bytedance/seedance-1-lite
> - https://replicate.com/bytedance/seedance-2.0
> - https://replicate.com/bytedance/seedance-2.0-fast

---

## 6. Rate limits y limitaciones

- **Rate limits Replicate:** no hay limite duro publicado; en practica las predictions se encolan. Si recibes 429, esperar 30s y reintentar.
- **Tamano de imagen de referencia:** data URLs base64 son comodas hasta ~10 MB. Para imagenes mas grandes, sube manualmente via Replicate Files API y pasa la URL HTTPS en lugar del path local (modificacion menor de `_image_to_data_url`).
- **Duracion maxima:** 10s en Seedance v1; 15s en v2.0 (o `-1` para intelligent duration en v2).
- **Idioma del prompt:** ingles. Otros idiomas son aceptados pero la calidad puede caer.
- **Timeout del script:** 10 minutos de polling. Si tu job tarda mas, aumenta `POLL_TIMEOUT_S`.

---

## 7. Ejemplo curl (endpoint REST Replicate)

Para debugging o integracion en otros lenguajes:

```bash
# 1. Crear prediction (Replicate auto-selecciona la version mas reciente del modelo)
curl -X POST "https://api.replicate.com/v1/models/bytedance/seedance-1-lite/predictions" \
  -H "Authorization: Bearer $REPLICATE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "prompt": "A violet crystal pulsing on dark basalt, cinematic",
      "aspect_ratio": "16:9",
      "resolution": "720p",
      "duration": 5
    }
  }'
# Respuesta: { "id": "...", "status": "starting", "urls": { "get": "...", "cancel": "..." }, ... }

# 2. Poll status
curl "https://api.replicate.com/v1/predictions/<PREDICTION_ID>" \
  -H "Authorization: Bearer $REPLICATE_API_TOKEN"
# status: "starting" -> "processing" -> "succeeded" | "failed" | "canceled"

# 3. Cuando status == "succeeded", el campo "output" trae la URL del .mp4
# Output puede ser string, lista de strings, o dict — el script normaliza los 3 casos.
```

> El header de auth de Replicate es `Authorization: Bearer <token>` (literal `Bearer`, NO `Token` ni `Key`).

---

## 8. Ejemplo Python completo — prompt Pax-canonico

```python
from scripts.seedance import generate_video

prompt = """
Jiggy, a young Pax cyclops with jade-green skin and a large single eye, running through
an underground crystal cavern. Crystals glowing violet-magenta and amber.
Dark basalt walls, dramatic depth. 3D PBR stylized Pixar quality, neon-magical lighting.
Camera: wide tracking shot following Jiggy. Duration: 5 seconds.
Color palette: jade #3DCCA3, amber #F59E0B, basalt #1E1E2E, magenta #EC4899, violet #B43FFF.
Style: 3D stylized, cinematic, no 2D, no anime, no photorealistic.
"""

out = generate_video(
    prompt=prompt,
    ref_image_path="personajes finales/Jiggy_Character.png",
    ratio="16:9",
    duration_s=5,
    quality="pro",
    seed=42,
)
print(f"Video guardado en: {out}")
```

---

## 9. Solucion de problemas

| Error | Causa probable | Solucion |
|---|---|---|
| `EnvironmentError: REPLICATE_API_TOKEN no esta definida` | Falta el token en `.env.local` | Agregar `REPLICATE_API_TOKEN=r8_...` |
| `RuntimeError: 401 Unauthorized` | Token invalido o expirado | Regenerar en https://replicate.com/account/api-tokens |
| `RuntimeError: 402 Payment Required` | Sin saldo en Replicate | Recargar en https://replicate.com/account/billing |
| `RuntimeError: 422 Unprocessable Entity` | Input invalido (aspect_ratio, resolution, duration fuera del schema del modelo) | Revisar la tabla de modelos arriba y el model card en replicate.com |
| `RuntimeError: 429 Rate Limit` | Demasiados requests concurrentes | Esperar 30s y reintentar |
| `RuntimeError: Prediction ... fallo (failed)` | Error del modelo (prompt bloqueado, imagen invalida, etc.) | Revisar el campo `error` que devuelve Replicate, simplificar prompt |
| `RuntimeError: Timeout` | Job no completo en 10 min | Aumentar `POLL_TIMEOUT_S` o reintentar mas tarde |
| `ModuleNotFoundError: requests` | Falta `requests` | `pip install requests` |

---

## 10. Diferencias clave vs el script anterior (fal.ai)

| Aspecto | fal.ai (anterior) | Replicate (actual) |
|---|---|---|
| Plataforma | fal.ai | Replicate |
| Env var | `FAL_KEY` / `FAL_API_KEY` | `REPLICATE_API_TOKEN` |
| Header auth | `Authorization: Key <key>` | `Authorization: Bearer <token>` |
| Endpoint | `queue.fal.run/<model>` | `api.replicate.com/v1/models/<owner>/<model>/predictions` |
| SDK opcional | `pip install fal-client` | `pip install replicate` (no usada aqui, REST puro) |
| t2v vs i2v | Endpoints separados por modelo (`/text-to-video` vs `/image-to-video`) | Un solo endpoint por modelo, presencia del campo `image` decide el modo |
| Polling | `status_url` + `result_url` separados | un solo `urls.get` que retorna prediction completa con `output` |
| Output dir | `content/videos/seedance/` | `content/videos/seedance/` (sin cambios) |
| Firma publica `generate_video()` | igual | igual (backwards-compatible) |
| Aliases de `quality` | `lite`, `pro`, `v2`, `v2-fast` | `lite`, `pro`, **`pro-fast` (nuevo)**, `v2`, `v2-fast` |
