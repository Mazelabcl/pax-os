# _archive — política y contenido

Esta carpeta contiene material que **ya no es canon vigente** pero **NO se borra**. Razones:
- Git tiene historial pero el `_archive/` lo hace visible y consultable sin comandos.
- Cualquier referencia futura ("cómo era el lore en abril", "qué decía la versión vieja del Oráculo") se resuelve mirando acá.
- Si algo se archivó por error, se rescata con `git mv` desde `_archive/` a su lugar.

## Reglas

1. **Nada se borra de `_archive/`** sin discusión con Aldot.
2. **Cada subcarpeta tiene su propio README** explicando: (a) qué hay adentro, (b) por qué se archivó, (c) cuál es el reemplazo vigente, (d) fecha de archivado.
3. **Si encuentras algo en `_archive/` que debería ser canon**, abrí una discusión — no lo muevas silenciosamente.
4. **Los agentes que escriben contenido (lore, guion, image-gen) NO leen de `_archive/`** salvo instrucción explícita.

## Subcarpetas previstas (se llenan durante reorganización 2026-05-21)

| Subcarpeta | Contenido | Reemplaza por |
|---|---|---|
| `pax-duplicado/` | La carpeta `/pax/` entera que duplicaba `/content/` | `content/` (fuente única) |
| `lore-versions/` | `lore.md` antiguo, `content/v2/lore.md`, otros lore.md históricos | `_lore/canon.md` |
| `content-v2/` | La carpeta `content/v2/` entera (rama intermedia abandonada) | `_lore/` + `gestos/` |
| `app-legacy-disabled/` | `app/_legacy-disabled/` (12 carpetas de la webapp deshabilitadas) | webapp actual |
| `personajes-fix-txt/` | `Personajes-Fix/*.txt` (drafts de char sheets) | `content/personajes/*.md` |
| `episodio-1-antiguo/` | `content/episodio-1/` (estructura antigua) | `gestos/01-miniserie/storyboards/cap-1/` |
| `backups-comprimidos/` | `canon-v2.rar`, `content.rar`, `content.zip` (backups locales antes de cambios grandes) | el repo en sí, versionado |

Cada subcarpeta se llena en la Fase 1 de la reorganización con su propio `README.md`.
