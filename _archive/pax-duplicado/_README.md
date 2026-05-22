# pax-duplicado/ — duplicado histórico de `content/`

## Qué hay aquí

Una copia espejo de `content/` con:
- `lore.md`, `principles.md`, `roadmap.md`, `canon-status.md`, `episodios-12-outline.md`, `storyboards.md`
- 12 capítulos (`cap-1.md` ... `cap-12.md`)
- Subcarpeta `personajes/` con char sheets
- `INDEX.md` propio y `publish.css`
- Un `.obsidian/` con configuración local

## Por qué se archivó

La app Next.js de este repo (`lib/docs.ts`) solo lee de `content/`. Esta carpeta `pax/` nunca estuvo conectada a ningún render ni a ningún agente. Era un espejo que duplicaba contenido y aumentaba el riesgo de divergencia (editar acá y olvidar `content/` o viceversa).

Aldot no recuerda haber creado esta carpeta deliberadamente — probablemente quedó como subproducto de un copy temprano cuando se separó el proyecto Pax en su propio repo.

## Reemplazo vigente

- `content/` durante la reorganización (Fase 1, mayo 2026).
- `_lore/` + `gestos/` una vez completada la Fase 2.

## Archivado

2026-05-21 — Fase 1 de reorganización del repo Pax.
