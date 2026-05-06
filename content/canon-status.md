---
title: "Canon vs exploratorio — registro de decisiones"
description: "Solo aldot promueve assets a canon. Por defecto, todo nuevo es exploratorio."
date: 2026-05-05
version: canon-v0
---

# Canon vs exploratorio

> **Regla única:** todo asset (imagen, lore, personaje, mecánica, locación) parte como **exploratorio**. Solo aldot promueve a **canon** con decisión explícita.
>
> Los agentes y skills NO pueden auto-promover.

---

## Por qué este registro existe

Sin un criterio claro, los agentes asumen que todo lo que se genera con buena calidad es canon. Eso introduce elementos al lore que aldot nunca aprobó. Ejemplo: durante Quest 2 visual sprint, se generaron 5 imágenes (un enemigo, hongos, una aldea pascuense, un túnel runner, un cristal cargándose) y un agente las promovió automáticamente a `public/images/concepts/`. Aldot las rechazó como canon — eran solo exploraciones para validar la skill `pax-image-gen`.

Este archivo es la fuente de verdad sobre qué pertenece al universo Pax oficial.

---

## Estados

| Estado | Significado | Dónde viven |
|---|---|---|
| **Canon** | Aprobado por aldot. Es Pax oficial. Reusable como reference. | `public/images/concepts/concept-*.png` (visual) o `content/lore.md`, `content/personajes/*.md` (texto) |
| **Exploratorio** | Generado para probar mecánicas, ideas, agentes. NO oficial. NO usar como reference de producción. | `content/exploratory-images/exp-*.png` (visual) o `content/exploratory/` (texto) |
| **Archivado** | Quest 1 (cerrada) o intentos descartados. | `archive/quest-1/...` |

---

## Cómo se promueve algo a canon

1. Aldot revisa el asset.
2. Aldot dice explícitamente "esto es canon" / "promovamos esto" / "agreguémoslo al universo Pax".
3. Orquestador (yo) ejecuta el housekeeping:
   - Mover archivo de `exploratory-images/` a `public/images/concepts/`
   - Renombrar `exp-X.png` → `concept-X.png`
   - Agregar fila a la tabla de assets canónicos en `~/.claude/skills/pax-image-gen/SKILL.md`
   - Registrar en este archivo (debajo) qué se promovió y cuándo
4. Si hay implicaciones de lore (ej. "el enemigo es canon → existe en el universo"), agregar también a `content/lore.md` o crear nodo en `content/personajes/`.

---

## Registro de promociones a canon

### v0 — 2026-05-05
**Canon visual heredado** (de Quest 1, validado por aldot):
- Char sheets del cast: jiggy, wiz, byte, luxa, zek, mariela, itzel
- Portadas: portada, portada2
- Concept arts Block A previos: cave-wide-dark, cave-stalagmites-reawakening, notebook-hero, mariela-kitchen-{table-hero,dusk,night}, office-cubicles-cool, metro-line5-evening, bilbao-grate-night

**Canon texto heredado:**
- `content/style-guide.md` (DNA visual)
- `content/principles.md` (Quest 2 first principles)
- `content/personajes/_canon.md`

### v1 — 2026-05-05 (sesión Quest 2 reset, lore + cast completo)
**Promovido a canon por aldot directamente:**
- `public/images/personajes/kz.png` — char sheet KZ generado y aprobado por aldot
- `public/images/personajes/onyx.png` — char sheet Onyx generado y aprobado por aldot
- `public/images/personajes/agatha.png` — char sheet Agatha generado y aprobado por aldot

**Canon texto Quest 2:**
- `content/lore.md` (lore reset Quest 2 con cast completo + rucas + storytelling Pipez)
- `content/personajes/{kz,onyx,agatha}.md` — fichas nuevas
- `content/personajes/{byte,luxa}.md` — fichas redefinidas Quest 2

**Canon decisiones:**
- Byte y Luxa NO se regeneran visualmente (decisión aldot). Solo cambia la descripción/vibra.
- Luxa = exploradora + cómica (NO solo cómica).
- Sub-arquetipos visuales Pax oficiales: "exposed-cyclops" (Jiggy, Wiz) vs "domed-mask" (KZ, Onyx, Agatha).
- Anchors Quest 1 archivadas en `archive/quest-1/anchors-rejected/`.

---

## Exploratorios actuales (NO canon)

Generados durante Quest 2 visual sprint (2026-05-05). Buenos para entender la skill funciona, no para asumir como universo oficial:

| Asset | Path | Estado |
|---|---|---|
| Enemigo "Sombra Pulsora" | `content/exploratory-images/exp-pax-enemy.png` | Exploración. NO canon. Si aldot quiere antagonistas en el lore, debe diseñarlos desde principios — esta imagen fue solo para probar pre-gen pipeline. |
| Hongos Pax bioluminiscentes | `content/exploratory-images/exp-pax-mushrooms.png` | Exploración. Idea visual interesante; canonización pendiente de aldot. |
| Aldea pascuense Pax | `content/exploratory-images/exp-pax-rapanui-village.png` | Exploración. Útil como inspiración de "cómo se ve una nación Pax", pero no canonizado todavía. |
| Highway runner túnel | `content/exploratory-images/exp-pax-highway-tunnel.png` | Exploración. Idea visual de infraestructura Pax; canonización pendiente. |
| Cristal cargándose macro | `content/exploratory-images/exp-pax-crystal-charging.png` | Exploración. Útil como ilustración del mecánica; canonización pendiente. |

Plus las 15 imágenes en `content/test-images/` (retratos hero, escenas, brand wordmark, cripta, etc.) — todas exploratorias.

---

## Reglas para agentes downstream

1. **Antes de usar un asset como reference**, verificar acá si es canon o exploratorio.
2. **Si un brief pide "el enemigo de Pax" o "los hongos de Pax"** y solo existe asset exploratorio, frenar y preguntar al orquestador. NO asumir que el exploratorio es la versión oficial.
3. **Al generar imagen nueva**, default = exploratorio en `content/exploratory-images/exp-*.png`. Solo aldot mueve a canon.
4. **Al sugerir promoción**, redactar la propuesta en este archivo bajo "Pendientes de promoción a canon" (sección abajo). Aldot la aprueba o rechaza.

---

## Pendientes de promoción a canon (cola para aldot)

[Vacío hoy. Cuando los agentes propongan promociones, se listarán acá con justificación.]

---

## Versionado

- **v0 (2026-05-05):** primer registro post-Quest 2 visual sprint. Establece la regla canon vs exploratorio.
