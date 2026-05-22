# content/ — solo archivos servidos por la webapp

Desde la Fase 2 de reorganización (2026-05-22), `content/` dejó de ser el dump de todo el material narrativo. Ahora **solo contiene archivos que la webapp lee en runtime** o assets operacionales generados.

## Qué vive aquí

- `CHANGELOG.md` — leído por `lib/changelog.ts`. Se muestra en la sección "Cambios" del sitio.
- `videos/` — outputs Seedance generados (untracked en git, ~47MB). Excluidos del bundle serverless vía `next.config.ts`. Son referencia operacional para Aldot, no se sirven en la webapp por ahora.

## A dónde fue el resto

- Lore canónico → `../_lore/` (canon, principles, style-guide, personajes, pax-core, etc.).
- Gestos (manifestaciones monetizables) → `../gestos/` (01-miniserie, 02-oraculo, 03-game, 04-video-bg, _backlog).
- Roadmap del proyecto → `../_meta/roadmap.md`.
- Versiones obsoletas + tests + canon-v2 + episodio-1 → `../_archive/`.

Ver `../INDEX.md` para el mapa completo del repo.
