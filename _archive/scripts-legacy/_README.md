# scripts-legacy — scripts one-shot ya ejecutados + bloqueantes Op 4/5

Archivo de scripts del pipeline de generacion de assets Pax que ya cumplieron su funcion. Quedan aqui por trazabilidad y para poder rescatar codigo si hay que regenerar algo.

## Estructura

### `bloqueantes-op4-op5/`
Scripts que bloqueaban la finalizacion de las operaciones Op 4 y Op 5 del pipeline (R2 set, anchors pass 1, img01 r3, concept arts, video-bg frames). Estan rotos o referencian rutas que ya no existen.

- `generate_r2_set.py`
- `run_pass1_anchors.py`
- `run_img01_r3.py`
- `generate-concept-arts.mjs`
- `generate_video_bg_frames.py` — apunta a `content/video-bg/` que no existe.

### `cap-generators/`
Generadores one-shot de storyboards de capitulos. Su output ya esta commiteado en `content/storyboards/cap-1-shot-*.md` y siguientes. No correr de nuevo a menos que se quiera regenerar imagenes desde cero.

### `char-sheets-individuales/`
Generadores one-shot de char sheets individuales (Kz, Onyx, Agatha) y retratos heroe. Output en `content/canon-v2/`.

### `world-scenes/`
Generadores one-shot de world scenes y assets sueltos (Pax Highway tunnel, Rapanui village, escenas con moneda/musico, asset crystal charging).

### `tests-one-shot/`
Tests one-shot del pipeline (test01 Jiggy runner, test04 Jiggy/Mariela meet, test05 infografia, subpipeline test). Ya no aplican al pipeline vigente.

### `gen_obsidian_vault.cjs` (suelto)
Regenera la carpeta `pax/` (vault Obsidian con los markdowns del proyecto). Esa carpeta fue archivada como duplicado en `_archive/pax-duplicado/`. **Si se ejecuta, recrea el duplicado y reintroduce el problema.** No correr.

## Scripts que SI siguen vivos en `scripts/`

Estos son los unicos que se mantienen activos para el pipeline en curso:

- `generate_canon_v2_bulk_mains.py`
- `generate_canon_v2_bulk_secundarios.py`
- `generate_canon_v2_bulk_ambientales.py`
- `generate_jiggy_canon_v2.py`
- `generate_oraculo_v3_images.py`
- `generate_oraculo_ritual.py`
- `generate_oraculo_visuals.py`
- `generate_video_bg_v2.py`
- `generate_video_bg_v2_hero_only.py`
- `openai_images.py` (libreria core)
- `seedance.py` (libreria core)
