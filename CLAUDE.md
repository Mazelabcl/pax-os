# Pax web app — instrucciones project-level

App de showcase y feedback del proyecto Pax. Pax es un meta-proyecto de 3 capas:
1. **Idea-meta**: ideas → IA + comunidad → consumo → $ → donación.
2. **Universo narrativo (lore)**: el canon en `_lore/canon.md` (anuraK + Ayni + cristales).
3. **Gestos**: manifestaciones monetizables. Hoy: mini-serie, oráculo, game, video-bg.

Esta webapp Next.js es UN gesto más (el "showcase"). No es el proyecto entero.

## Lectura inicial obligatoria (en orden)

1. `INDEX.md` — mapa maestro del repo
2. `_meta/manifesto.md` — qué es Pax
3. `_lore/canon.md` — el universo narrativo vigente
4. `gestos/*/README.md` — cada gesto vigente (01-miniserie, 02-oraculo, 03-game, 04-video-bg)

Memoria persistente clave (Claude):
- `~/.claude/projects/C--Users-aldot--gemini-antigravity-scratch-pax-os/memory/pax_meta_concept.md`
- `~/.claude/projects/C--Users-aldot--gemini-antigravity-scratch-pax-os/memory/pax_current_canon.md`

## Scope de la webapp

App es read-only + copy-friendly. NO chat con IA, NO tools de acción, NO Agent Studio, NO form de feedback (Pipez usa WhatsApp).

Rutas activas hoy: `/` (home), `/oraculo`, `/docs/[slug]`. Otras rutas (lore, personajes, episodios, etc.) están archivadas en `_archive/app-disabled-routes/`.

## Stack

Next.js 15 App Router + TypeScript + Tailwind + shadcn/ui + react-markdown.
Vercel Password Protection. Sin backend de IA, sin DB, sin form.

## Estructura del repo (post-reorg 2026-05-22)

```
pax-os/
├── INDEX.md, CLAUDE.md, README.md
├── _meta/        ← la idea (manifesto, roadmap)
├── _lore/        ← el universo (canon, personajes, pax-core, style-guide, principles)
├── gestos/       ← las manifestaciones ($): 01-miniserie, 02-oraculo, 03-game, 04-video-bg, _backlog
├── content/      ← solo lo que la webapp sirve (CHANGELOG.md, README.md, videos/)
├── app/, lib/, components/, public/   ← webapp Next.js
├── scripts/      ← generadores activos (imágenes + video: openai_images, seedance, oraculo, canon_v2, video_bg)
├── research/     ← investigaciones vivas
├── process-log/  ← logs históricos del proceso
└── _archive/     ← lo deprecado, recuperable, READMEs por subcarpeta
```

## Source of truth

`_lore/`, `gestos/` y `_meta/` en este repo son el contenido canónico vigente. `content/` solo sirve a la webapp (CHANGELOG, videos).

La carpeta `../pax-miniserie/` (afuera del repo) es snapshot histórico Quest 1 con terminología obsoleta (Pachamama, rucas, Fisher King) — **NO leer para contenido nuevo**. Ver `pax-miniserie/_README_HISTORICO.md`.

`../pax-game/` es repo separado del gesto 03-game. Su canon debe sincronizar contra `_lore/canon.md`.

## Cuando recibo feedback de Pipez

Llega vía WhatsApp a Aldot. Aldot lo procesa localmente con Claude Code en este repo usando los agentes Pax disponibles (`~/.claude/agents/pax-*.md`). Editar archivos en `_lore/` o `gestos/<gesto>/`, commit, push. Vercel auto-deploya.

## Idioma

Todo el contenido del proyecto: español neutro (sin voseo argentino). UI mobile-first.
