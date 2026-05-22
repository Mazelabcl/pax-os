# app-legacy-disabled/ — rutas v2 deshabilitadas de la webapp

## Qué hay aquí

La subcarpeta `v2/` con 6 `page.tsx`:
- `v2/page.tsx` (landing del intento v2)
- `v2/episodio-1/page.tsx`
- `v2/lore/page.tsx`
- `v2/personajes/page.tsx`
- `v2/pitch/page.tsx`
- `v2/proceso/page.tsx`

Estos `.tsx` formaban un set de rutas paralelo `/v2/*` durante una iteración intermedia de la webapp Pax (mayo 2026). En ese momento `app/_legacy-disabled/` se usó para "apagar" estas rutas sin borrarlas (Next.js ignora carpetas que empiezan con `_`).

## Por qué se archivó

La webapp actual vive directamente en `app/` con las rutas activas. Estas páginas referenciaban `content/v2/*.md`, que ya no es la fuente canónica (queda en `_archive/content-v2/` o sigue en `content/v2/` pendiente de archivar en Fase 2 si los scripts que la referencian no se actualizan antes).

Quedan también, sin tocar todavía, varias carpetas `app/_<nombre>-disabled/` (cambios, episodio-1, episodios, estilo, lore, personajes, principles, roadmap). Esas siguen un patrón distinto y se evaluarán en Fase 2 junto con el rediseño de la webapp.

## Reemplazo vigente

- Webapp actual en `app/` (rutas activas sin prefijo `_`).
- `app/oraculo/`, `app/docs/`, `app/api/`, `app/page.tsx`.

## Archivado

2026-05-21 — Fase 1 de reorganización del repo Pax.
