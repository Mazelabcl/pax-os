# Pipeline de imagenes — gpt-image-2

Infraestructura para generar/editar imagenes contra la API de OpenAI desde
scripts locales del repo `pax-os`.

## Modelo verificado

Modelo confirmado funcionando contra la cuenta del usuario (org con
Individual Approved + Business Approved):

```
gpt-image-2
```

Verificado el 2026-05-04 con el endpoint `images.generate` (`size=1024x1024`,
`quality=low`). Devolvio PNG RGB 1024x1024 valido (~1.6 MB) en el primer
intento, sin necesidad de fallback al alias date-stamped
`gpt-image-2-2026-04-21`.

Si en el futuro OpenAI cambia el ID en limits, actualizar la constante
`MODEL` en `scripts/openai_images.py`.

## Setup

```bash
pip install openai
```

La key se lee de `.env.local` en la raiz del repo (`OPENAI_API_KEY`). El
parser es manual, no se requiere `python-dotenv`.

## API publica

`scripts/openai_images.py` expone dos funciones:

### `generate_image(prompt, output_path, size, quality)`

Genera imagen desde texto puro.

```python
from scripts.openai_images import generate_image

generate_image(
    prompt="Cinematic portrait of an old fisherman at golden hour, 35mm film grain.",
    output_path="content/v2/img-01-fisherman.png",
    size="1024x1024",   # tambien: 1024x1536 (vertical), 1536x1024 (horizontal)
    quality="medium",   # low | medium | high
)
```

### `edit_image(prompt, input_image_paths, output_path, size, quality)`

Genera imagen usando una o varias imagenes de referencia. Convencion: en el
prompt referirlas como `Image 1`, `Image 2`, etc. en el mismo orden que
aparecen en `input_image_paths`.

```python
from scripts.openai_images import edit_image

edit_image(
    prompt=(
        "Combine the lighting and color palette of Image 1 with the "
        "character pose and outfit of Image 2. Keep the camera angle of "
        "Image 1. Output a single cohesive scene."
    ),
    input_image_paths=[
        "content/v2/refs/lighting-ref.png",   # Image 1
        "content/v2/refs/character-ref.png",  # Image 2
    ],
    output_path="content/v2/img-02-composed.png",
    size="1024x1024",
    quality="medium",
)
```

Si solo necesitas una referencia:

```python
edit_image(
    prompt="Repaint Image 1 in oil-painting style, keep composition.",
    input_image_paths="content/v2/refs/base.png",
    output_path="content/v2/img-03-oil.png",
)
```

## Costos por tier

OpenAI cobra por imagen generada segun el tier de calidad. Valores
publicados de la familia `gpt-image-*` (referenciales — confirmar contra
`platform.openai.com/docs/pricing` antes de tirar batches grandes):

| Quality | 1024x1024 (aprox.) | Notas |
| ------- | ------------------ | ----- |
| low     | ~$0.011            | Util para iteracion rapida / smoke tests |
| medium  | ~$0.042            | Default razonable para entregables |
| high    | ~$0.167            | Reservar para imagenes ancla finales |

Resoluciones no cuadradas (`1024x1536`, `1536x1024`) suben proporcionalmente.
`gpt-image-2` mantiene la misma estructura de pricing que `gpt-image-1`,
pero **conviene revisar la pagina oficial el dia que se corra el batch
final** porque el modelo es nuevo y los precios pueden moverse.

## Smoke test

```bash
python scripts/openai_images.py
```

Genera `scripts/test-apple.png` (1024x1024, quality=low). Si el archivo se
crea y se abre correctamente, el pipeline esta listo.

## Output de verificacion inicial

- `scripts/test-gpt-image-2.png` — primera imagen generada durante la
  verificacion del modelo (PNG 1024x1024, ~1.6 MB).
- `scripts/test-apple.png` — output del smoke test ejecutando
  `openai_images.py` directo.

Ambos archivos son artefactos de validacion y se pueden borrar cuando
empiece la generacion de las 5 imagenes ancla.

## Convencion para el agente downstream

El agente que genere las 5 imagenes ancla del IP de Pax debe:

1. Leer `content/v2/image-prompts.md` (lo escribe el prompt engineer en
   paralelo).
2. Para cada uno de los 5 prompts, decidir si es `generate_image` (texto
   solo) o `edit_image` (con referencias).
3. Guardar outputs en `content/v2/anchors/img-0{1..5}-<slug>.png` con
   `quality="high"` para el render final.
4. Antes del batch final, correr cada prompt con `quality="low"` para
   validar composicion, y solo entonces re-generar en `high`.
