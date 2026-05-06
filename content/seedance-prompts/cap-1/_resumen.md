---
title: "Cap 1 — Plan Seedance"
date: 2026-05-04
status: prompts_listos_para_probar
---

# Cap 1 — Plan Seedance

## Total clips

- **Cantidad:** 16 clips totales
  - Shots 01, 02, 03, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15 → 1 clip cada uno = 14 clips
  - Shot 04 → split en 2 sub-clips (anti-patron 6 caras visibles) = 2 clips
- **Duracion total estimada:** ~95 segundos de video Seedance crudo
  - 5s × 8 clips = 40s
  - 7s × 8 clips = 56s
  - Total: ~96s (de los cuales el cap final dura 3 min — el resto es padding, edicion, beat de pausa, sound design, transiciones, voz, score)
- **Aspect ratios:** 14 clips en 16:9 (1536x1024 o equivalente Seedance), 1 clip en 9:16 vertical (shot 13)

## Costo estimado en Seedance

Pricing referencial publicado (process-log/15a):
- Lite/Fast 720p (~$0.10/min) → para drafts
- Pro 1080p audio nativo (~$0.30/min) → para masters

Costo de cap 1 completo:
- Drafts Lite: 96s × ($0.10 / 60s) = ~$0.16 USD
- Masters Pro: 96s × ($0.30 / 60s) = ~$0.48 USD
- Total con 1 reroll por shot estimado: **~$1.00 USD por cap completo**.

Costo del **shot recomendado para probar primero** (Scene 08 Onyx, 5s):
- Lite: $0.008 USD
- Pro: $0.025 USD
- Practicamente despreciable. Ideal para validar pipeline.

## Refs nuevas pre-generadas (en publicacion como pending_aldot_approval)

Ya generadas con `scripts/openai_images.py::edit_image()` quality=low. Todas viven en `public/images/concepts/` con prefijo `concept-cap1-*`:

1. `public\images\concepts\concept-cap1-tunel-vertical-pax.png` (1997 KB) — tunel vertical con manhole arriba, frontera cromatica magenta-jade abajo / sodium-orange arriba. Para shot 13.
2. `public\images\concepts\concept-cap1-camara-central-cristales-mapa.png` (2259 KB) — camara central + dais + mapa-constelacion holografico. Para shots 03, 04, 05, 06, 08, 09, 10, 11.
3. `public\images\concepts\concept-cap1-cristal-pale-cyan-vacio.png` (1367 KB) — el cristal vacio que entrega Wiz. Insert macro. Para shots 11, 12, 13, 15.
4. `public\images\concepts\concept-cap1-chispa-ancla-dorada.png` (1283 KB) — chispa-ancla dorada-palida easter-egg. Para shot 14.

**Pendiente:** aldot revisa estos concepts y los promueve (o pide reroll) antes de uso intensivo en producccion. Para HOY, sirven como refs de Seedance.

## Refs aun faltantes (no criticas)

- No quedan refs criticas faltantes para cap 1.
- A futuro (no bloquea HOY): pre-gen de char sheets adicionales por personaje (tres-cuartos + perfil), recomendado por skill (3 refs por personaje, no 1) para mejorar consistency en clips Pro. Hoy se trabaja con 1 ref/personaje por timing.

## Orden de produccion recomendado

**Pre-flight (ya hecho):**
- [x] Pre-gen de 4 refs faltantes via pax-image-gen (paralelo, 4 imagenes en ~3 min)

**Fase 1 — Validacion del pipeline (~10 minutos):**
1. Probar Scene 08 (Onyx) en Seedance Lite. 5s, 1 personaje, locacion canonica, plano fijo. Validar identidad + render + paleta.
2. Si pasa: confirmar pipeline y avanzar a Fase 2.
3. Si falla: identificar punto debil (identity drift / palette / 2 ojos / etc.) y ajustar prompts antes de batch.

**Fase 2 — Drafts batch (Lite, ~25 minutos de generacion):**
Orden lineal 1 → 15 con split del shot 04 en 4A y 4B.
- Shots facil-primero (1, 2, 8, 14) — establecer baseline
- Shots medianos (5, 6, 7, 9, 10, 11) — single/two-shot
- Shots dinamicos (12, 13) — accion + vertical
- Shot complejo (3) — Wiz + 6 siluetas
- Shot critico (4A + 4B) — split obligatorio
- Shot cliffhanger (15) — primera incursion warm palette

**Fase 3 — Aldot revisa drafts y aprueba composicion (~30 min review).**

**Fase 4 — Masters (Pro, mismo seed, ~30 min de generacion).**

**Fase 5 — Edicion + audio post.**
- Cuts duros entre clips, L/J-cuts en transiciones de dialogo
- Stripear audio Seedance util (ambient + SFX), reemplazar voces por dub humano o ElevenLabs
- Voz de Wiz "Otro" (shot 02) y voces dirigidas — todo en post

## Anti-patrones detectados con fix sugerido

| Shot | Anti-patron | Fix aplicado |
|---|---|---|
| 03 | 7 personajes en frame (Wiz + 6) | Wiz unico detallado, 6 siluetas borrosas de espaldas. Si falla, regenerar con 3 visibles maximo. |
| 04 | 6 caras visibles en frame | **Split obligatorio en 2 sub-clips de 2 personajes cada uno** (4A: Jiggy+KZ, 4B: Onyx+Agatha). |
| 09 | Holograma puede generar texto | Constraint explicito "no on-screen text on the hologram". |
| 10 | Cierre de ojo unico puede generar 2 parpados | Constraint explicito "ONE single curved zen line, NOT two eyelids". |
| 12 | Drift de prop (storyboard cap-1 ya lo flagged) | Constraint "no bandanas, no scarves, no extra accessories beyond what is in @Image1". |
| 14 | Color de chispa-ancla puede salir magenta | Constraint "pale dusty gold (#D9C28A), NOT magenta, NOT cyan, NOT pink". |
| 15 | Chromatic frontier puede romper identidad de Jiggy | Constraint explicito de mantener harness magenta + cristal pale-cyan reflejando warm. |

## Shot recomendado para PROBAR PRIMERO

### **Scene 08 — Onyx propone subir** (5 segundos, 1 personaje, locked-off)

**Por que:**
- 1 personaje canonico (Onyx) con char sheet existente
- Locacion canonica con concept-cave-wide-dark.png como ref
- Plano fijo (locked-off) — sin movimiento de camara complejo
- 5 segundos — el sweet spot Seedance
- Sin gestos rapidos, sin armas, sin handoff complejo
- Sin cristal cyan/dorado especial (evita riesgo de color drift)
- Sin texto on-screen
- Sin humanos surface
- Caso ideal para validar 3 cosas en un solo clip:
  1. **Identity lock funciona** — Onyx con UN ojo, harness con tirantes cruzados, marcas tribales canonicas
  2. **Render base canonico** — 3D PBR neon-magic, paleta jade-amber-basalt-magenta
  3. **Constraints en afirmativo se respetan** — no bandanas, no fast hand gestures, no on-screen text

**Costo de la prueba:** ~$0.008 USD en Lite (despreciable).

**Si pasa:** continuar batch. **Si falla:** ajustar la seccion Constraints comun antes de gastar el batch entero.

## Modelo usado en la generacion de prompts

- Skill aplicada: `pax-seedance-prompt` v0
- Manual canonico: `process-log/15a-research-seedance-deep.md`
- Refs visuales pre-gen: `pax-image-gen` skill via `scripts/openai_images.py` (modelo gpt-image-2)
- Modelo agente: claude-opus-4-7[1m]
