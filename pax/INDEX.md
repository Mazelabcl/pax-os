---
title: "Pax — Index del proyecto"
description: "Tabla de contenidos. Lee solo los archivos relevantes a tu tarea."
date: 2026-05-05
version: index-v0
---

# Pax — Index del proyecto

Este archivo es un **mapa**, no contenido. Si eres un agente, no leas todos los archivos del repo. Identifica tu tarea, mira la sección "Cuándo cargar qué", y carga solo lo que necesitas.

---

## Identidad y dirección

| Archivo | Qué tiene | Cuándo leerlo |
|---|---|---|
| `content/principles.md` | Qué es Pax (canónico). Visión dual sistema+historia, tono, feedback Pipez integrado, reglas para agentes. | **SIEMPRE** primero. Lectura obligatoria para todo agente. |
| `content/roadmap.md` | Quests pasadas, actual, futuras. | Si tu tarea afecta el plan general o necesitas saber dónde estamos. |
| `archive/quest-1/README.md` | Snapshot de qué se intentó en Quest 1 y por qué se cerró. | Si necesitas contexto histórico de errores pasados. NO uses contenido Quest 1 como source-of-truth. |

---

## Lore y narrativa

| Archivo | Qué tiene | Cuándo leerlo |
|---|---|---|
| `content/pitch-largo.md` (en construcción Quest 2) | Pitch maestro del IP, ~300 palabras, sin jerga. | Tareas narrativas, marketing, web, presentación. |
| `content/lore.md` | Lore completo (en construcción Quest 2 — versión Quest 1 está archivada). | Tareas que requieren cosmología detallada. |

> Nota Quest 2: el lore detallado se está reescribiendo después de validar el pitch. Mientras tanto, principles.md tiene la versión condensada. Si tu tarea no requiere detalles más allá de principles, NO leas el lore detallado.

---

## Personajes

| Archivo / Asset | Qué tiene | Cuándo leerlo |
|---|---|---|
| `content/personajes/_canon.md` | Char sheet visual canónico del cast. | Cualquier tarea con personajes. |
| `content/personajes/{jiggy,wiz,byte,luxa,zek}.md` | Fichas individuales de los Pax. | Cuando ese personaje específico aparece. |
| `content/personajes/{mariela,itzel}.md` | Humanos de superficie (NO Pax). | Cuando aparecen en tu tarea. |
| `public/images/personajes/{slug}.png` | Char sheet visual (PNG). | **Si tu tarea es visual** — usar como reference de IDENTITY LOCK. |

---

## Visual

| Archivo / Asset | Qué tiene | Cuándo leerlo |
|---|---|---|
| `content/style-guide.md` | DNA visual no negociable: render 3D PBR neon-magic, paleta canónica, anti-2D. | **SIEMPRE** si tu tarea es visual. |
| `public/images/portadas/{portada,portada2}.png` | Portadas del proyecto, paleta + render base reference. | Tareas visuales como reference contextual. |
| `public/images/concepts/concept-*.png` | Concept arts canónicos (cuevas, notebook, etc.). | Tareas visuales que necesitan ambientes. |
| `~/.claude/skills/pax-image-gen/SKILL.md` | Skill que genera imágenes con IDENTITY LOCK. | Si tu tarea es generar imagen Pax — usar la skill, no inventar prompt. |

---

## Decisiones del director

| Archivo | Qué tiene | Cuándo leerlo |
|---|---|---|
| `process-log/00-aldot-decisions.md` | Decisiones D1, D2, D3 tomadas por aldot durante el proyecto. | Si tu tarea puede chocar con una decisión existente — verificar primero. |

---

## Lecciones aprendidas (memoria persistente)

| Archivo | Qué tiene | Cuándo leerlo |
|---|---|---|
| `~/.claude/projects/C--Users-aldot/memory/lessons/lessons_orchestration.md` | Reglas de orquestación, incluyendo cold-reader gate (L4) y IDENTITY LOCK (L5). | Si eres orquestador o haces pipeline de agentes. |
| `~/.claude/projects/C--Users-aldot/memory/lessons/lessons_screenwriting.md` | Lecciones de guion y onboarding (L1, L3). | Tareas narrativas. |
| `~/.claude/projects/C--Users-aldot/memory/lessons/lessons_lore.md` | Lecciones de worldbuilding (L2 = DIFF de pérdidas). | Tareas de lore. |
| `~/.claude/projects/.../memory/pax_agent_pipeline_v2.md` | Arquitectura del pipeline Quest 2 con cold-reader gate + INDEX router. | Si eres orquestador. |

---

## Cuándo cargar qué (cheat sheet)

| Tarea | Carga obligatoria | Carga si aplica |
|---|---|---|
| **Pitch / texto narrativo** | principles + INDEX | pitch-largo, lore, glosario (cuando exista) |
| **Visual** | principles + style-guide + char sheets relevantes | concept arts contextuales |
| **Personaje nuevo** | principles + lore + _canon + personajes existentes | research mítico si requiere ancla cultural |
| **Marketing / social** | principles + pitch-largo + style-guide | portadas como reference |
| **Producto / juego** | principles + roadmap | lecciones aprendidas si hay precedente |
| **Decisión arquitectónica de proyecto** | principles + roadmap + decisiones aldot | lecciones de orquestación |

---

## Reglas de uso del INDEX

1. **No leas archivos no listados aquí** salvo que el orquestador te dé un path explícito en tu brief.
2. **Si te falta info**, pregunta al orquestador antes de hacer Glob/Grep arbitrario.
3. **Si descubres archivos canónicos no listados aquí**, repórtalos para que se agreguen.
4. **Token budget:** apunta a leer ≤ 5 archivos del INDEX por tarea. Si necesitas más, probablemente la tarea está mal scopeada.

---

## Mantenimiento

Este archivo lo mantiene **el orquestador (Claude / Opus en main thread)**. Cada vez que se agrega un archivo canónico al proyecto, debe agregarse aquí.

Versionado:
- **v0 (2026-05-05):** primer INDEX post-reset Quest 2.
