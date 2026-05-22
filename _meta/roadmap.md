---
title: "Pax — Roadmap"
description: "Por dónde va el proyecto: completado, actual, futuro."
date: 2026-05-05
version: roadmap-v0
---

# Pax — Roadmap

Este roadmap se actualiza con cuidado. Cada quest es chica. No se salta de quest 2 a quest 5.

---

## Quest 1 — Primer borrador completo (CERRADA 2026-05-04)

### Lo que se hizo

- Pitch corto + largo (rechazado por jerga densa y falta de claridad)
- Lore v4 con 6 naciones, "runners alquimistas", lung-gom-pa, anti-pulso (rechazado por densidad sin onboarding)
- Episodio 1 v2 (escenas técnicamente OK, narrativamente desconectadas del concepto core)
- 5 imágenes ancla generadas con GPT Image 2 (R1 + R2 + R3 imagen 1) — rechazadas por no respetar el DNA del cast
- Web app `/v2` deployada en Vercel con todo lo anterior
- 26 confidence-loops corridos, scores 87-89/100 que NO se correspondieron con calidad real percibida por aldot

### Lo que se rescata

- **Char sheets visuales del cast:** `public/images/personajes/{jiggy,wiz,byte,luxa,zek,mariela,itzel}.png`
- **Style-guide canónico:** `content/style-guide.md`
- **Concept arts Block A** (sesión anterior): `public/images/concepts/*.png`
- **Portadas:** `public/images/portadas/*.png`
- **Lecciones loggeadas en memoria persistente:** `~/.claude/projects/.../memory/lessons/`

### Lo que se aprendió (lecciones)

- **L1:** cold open mítico necesita pitch.md separado para lector cold (`lessons_screenwriting.md`)
- **L2:** protocolo "DIFF de pérdidas + mapeo must-fix" para todo R2+ de architect (`lessons_lore.md`)
- **L3:** pipeline visual debe atarse al style-guide canónico antes de aplicar referencias estéticas externas (`lessons_screenwriting.md`)
- **L4:** confidence loop falla si el critic optimiza por coherencia interna sin gate de cold-reader independiente (a loguearse en `lessons_orchestration.md`)
- **L5:** cuando el lore declara especie no-humana, el prompt visual debe declarar IDENTITY LOCK con char sheet específico al inicio del prompt (a loguearse en `lessons_pax_pipeline.md`)

### Archivado en

`archive/quest-1/` — todos los pitches, lore v4, episodio v2, imágenes, anchors fallidas, prompts. Ver `archive/quest-1/README.md` para detalle.

---

## Quest 2 — Reset a primeros principios (EMPIEZA 2026-05-05)

**Premisa:** construir Pax desde los primeros principios documentados en `content/principles.md`. Empezar chiquito. Cada pieza validada antes de avanzar.

### Fase 2.1 — Documentación canónica (esta sesión)
- [x] `content/principles.md` — primeros principios canónicos con visión dual sistema+historia
- [x] `content/roadmap.md` — este documento
- [x] `archive/quest-1/README.md` — snapshot honesto de Quest 1
- [ ] Loguear L4 + L5 en lecciones de orquestación
- [ ] **Diseñar nuevo pipeline de agentes** con: first-principles-aware reading obligatorio, cold-reader gate independiente al final, model tracking en cada output, rúbrica externa no self-confirming

### Fase 2.2 — Pitch reseteado (próximo turno tras OK de aldot)
- [ ] **Pitch corto (60s) escrito DIRECTO en conversación con aldot**, no por agente, basado SOLO en primeros principios. Cero herencia de Quest 1.
- [ ] Validación cold-reader: aldot mismo lee el pitch. Si emociona, GO. Si no, iteramos en chat hasta que sí.
- [ ] Solo cuando el pitch corto cierre, escalar a versión larga + lore más detallado.

### Fase 2.3 — Skill `pax-image-gen` (después del pitch)
- [ ] Spec de skill con: brand DNA + char sheets baked como references obligatorias + IDENTITY LOCK pattern
- [ ] Implementación que invoca GPT Image 2 con character locking: "create image of {personaje}, use {personaje}_charactersheet.png as IDENTITY LOCK"
- [ ] Test con un personaje conocido (Jiggy) para validar consistencia
- [ ] Esta skill rompe el ciclo de "el agente olvida el DNA" — el DNA está en la skill, no en cada prompt manual

### Fase 2.4 — Web reset
- [ ] Decidir suerte de `/v2` actual (matar / dejar como archivo / redirigir)
- [ ] Nueva landing minimal con solo el pitch v2 + principios + char sheets visibles
- [ ] Crecer desde ahí

---

## Quest 3 — Visualización del proceso (FUTURO CERCANO)

**Premisa:** documentar y visualizar cómo se construye Pax es PARTE de Pax. La gente debe poder ver el proceso vivo.

### Ideas (sin compromiso de orden)
- [ ] Integrar [paperclip](https://github.com/paperclipai/paperclip) para visualizar agentes trabajando, deliverables, feed de actividad como "energía generada en el ecosistema"
- [ ] Considerar Obsidian para grafo de conocimiento de Pax (sinapsis de neuronas de data)
- [ ] Track explícito de qué modelo usó cada agente (Opus / Sonnet / Haiku) en cada output, para evaluar costo vs calidad
- [ ] Dashboard de scores de confidence-loops vs satisfacción real de aldot (calibrar si los scores correlacionan con quality real)

---

## Quest 4 — Marketplace de agentes financiables (FUTURO)

**Premisa:** cualquier persona puede "financiar" un agente Pax con su propio system prompt y dinero, y ese agente entra a la arena a debatir / iterar / proponer ideas.

### Ideas
- [ ] Pool de ideas generada por agentes que iteran/mejoran ideas de otros
- [ ] Integración con OpenAI Codex para que ideas se conviertan en código vibe-codeado en vivo
- [ ] Cada agente reporta modelo, costo y impacto (¿su idea fue adoptada? ¿generó valor?)
- [ ] Aldot + Pipez + Claude (yo) somos los 3 agentes core fundadores. Después se abre.

### Paperclip como backend candidato

[Paperclip](https://github.com/paperclipai/paperclip) — OS open-source MIT para flotas de agentes IA con orgcharts, presupuestos, governanza, audit logs. Su sub-producto `paperclipskills.com` ya implementa pagos M2M con x402 + USDC en Base + splits 80/20.

**Encaje narrativo:** la tribu Pax subterránea ES una empresa zero-human ejecutando impacto material. La metáfora se cierra.

**Decisión Quest 2:** postergado, no descartado. Validar ratio issues/commits del repo más cerca de Quest 4 antes de comprometer integración.

**Research completo:** `process-log/11a-research-paperclip.md`

---

## Quest 5 — Producto real (LA MAGIA HECHA REAL)

**Premisa:** el primer micro-producto Pax que demuestra que 1 USD generado = 1 USD de impacto.

Probablemente arranca con uno de:
- Un mini-juego endless runner con publicidad
- Un challenge social viral (gema gigante de píxeles)
- Un curso comprable cuyo 100% va a impacto

Definir cuando los anteriores estén sólidos y haya tracción demostrable.

---

## Principios del roadmap

1. **Cada quest es chiquita.** Si no se puede demostrar en 1-2 semanas, está mal scopeada.
2. **Cada quest tiene cold-reader test antes de cerrarse** (aldot, Pipez, o agente cold-reader independiente).
3. **Documentamos el proceso de cada una.** Los aprendizajes (lessons) se cargan al sistema canónico de memoria.
4. **No saltamos quests.** Si Quest 2 no está sólida, no empezamos Quest 3.
5. **El proceso ES el producto.** Quest 3 (visualización del proceso) no es accesoria — es parte de demostrar que Pax funciona.

---

## Pendientes post-reorg 2026-05-22

Esta sección agrupa los TODOs que quedaron documentados al cierre de la reorganización mayor del repo (8 commits, fases 0-5). No están priorizados — Aldot decide cuál atacar primero.

### Operativos (heredados de Fase 5)

1. **🟡 Actualizar system prompt de `src/canon_validator.js` en pax-game/** (líneas 102-130). Todavía describe a Pax como "cíclopes turquesa" con paleta `#E83FC8`. No rompe paths ni sync, pero el modelo Sonnet usa esos términos en sus razones de validación. Alinear al `_lore/style-guide.md` vigente (anuraK / Ayni / Pax intraterrestres alquimistas / cristales comunes-raros). **Quick win.**

2. **🟢 Resetear `pax-game/memory/canon-kpi.json`**. Tiene `fail_rate: 66.7%` de validaciones contra snapshot viejo (Quest 2 R4). Reset para que las métricas adelante reflejen el canon nuevo limpio. **5 min de trabajo.**

3. **🟢 Verificar git identity local en pax-game/**. El agente Fase 5 puso `aldo@mazelab.cl` / `aldot` (igual que pax-os, solo config local). Si Aldot prefiere otro user/email para ese repo: `git config --unset user.email && git config --unset user.name` desde `pax-game/`.

### Procesos y herramientas

4. **🟡 Skill `pax-research-to-html`**. El patrón "tomar .md de research con scores + confidence-loop y convertir a HTML self-contained con paleta Pax + top N hero + tabla expandible + changelog timeline" es reusable. Si Aldot anticipa más research (de gestos, capítulos, personajes), vale la pena empaquetar la skill en `~/.claude/skills/pax-research-to-html/`. **~30 min de trabajo cuando tenga prioridad.**

5. **🟢 Hook pre-commit "archivos M sin staged"**. En Fase 2 el agente reescribió 7 archivos de `lib/` pero solo se commitearon los renames porque mi `git add` específico no los incluyó. El build local funcionaba con archivos modificados sin commitear — caso silencioso. Vale la pena un hook `.git/hooks/pre-commit` que avise si hay archivos M no staged en el commit. **~15 min de trabajo.**

### Contenido (decisiones pendientes de Aldot)

6. **Storyboards huérfanos en `gestos/01-miniserie/storyboards/_huerfanos/`** (6 pares .md+.png con nombres `otros (1-6)`). Pendiente decidir por cada uno: asignar a un capítulo, descartar a `_archive/`, o mantener como semilla.

7. **`content/videos/`** (~47MB de outputs Seedance, untracked). Decidir: publicar a `public/videos/` para servirlos en la webapp, dejar como assets locales, o archivar.

8. **`mariela.md` sin PNG**. Memoria dice "Mariela NO comprometer hasta confirmación". Resolver: generar PNG cuando se confirme el rol, o eliminar la ficha si se descarta.

9. **`luxa.md`, `zek.md` sin PNG canónico**. Tienen .md pero no imagen final en `_lore/personajes/`. Generar con `scripts/generate_canon_v2_bulk_mains.py` cuando convenga.

### Estratégicos (research de gestos)

10. **Decisión de inversión sobre el top 3 del research** (Patreon + Audio-drama + Verticals). Los 3 son frágiles a pausas — solo Audio-drama tiene cola pasiva en plataformas abiertas. Aldot debe decidir: comprometerse a cadencia 6 meses (trío completo) vs empezar solo por Audio-drama (resiliente). Ver `research/gestos.html`.

---

## Versionado

- **v0 (2026-05-05):** primer roadmap post-reset Quest 2. Escrito por aldot+Claude en conversación principal, sin agentes.
- **v1 (2026-05-22):** agregada sección "Pendientes post-reorg" tras la reorganización mayor del repo (8 commits, fases 0-5, separación meta+lore+gestos).
