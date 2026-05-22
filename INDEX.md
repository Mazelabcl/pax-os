# Pax — mapa maestro del repositorio

> **Estado:** REORGANIZACIÓN EN PROGRESO (2026-05-21). Algunas rutas mencionadas abajo se completan durante las fases 1-5. Lo marcado con ⏳ está pendiente.

Este repo es el **hub** del proyecto Pax. Contiene el meta-manifesto, el lore canónico, varios gestos, la webapp showcase y el archivo histórico.

Si vienes de cero, lee en este orden:
1. [`_meta/manifesto.md`](./_meta/manifesto.md) — qué es Pax (idea + lore + gestos)
2. [`_lore/canon.md`](./_lore/canon.md) — la mitología vigente ⏳ (hoy en `content/lore_final.md`)
3. [`gestos/`](./gestos/) — las manifestaciones monetizables ⏳

---

## Estructura del repo (post-reorganización)

```
pax-os/
├── INDEX.md              ← este archivo
├── CANON.md              ← lista plana CANON / DEPRECATED / WIP ⏳
├── CLAUDE.md             ← instrucciones para Claude
├── README.md             ← onboarding humano
├── CHANGELOG.md          ← historial visible en la webapp
│
├── _meta/                ← LA IDEA (propuesta de valor del proyecto)
│   ├── manifesto.md      ✅
│   └── modelo-negocio.md ⏳
│
├── _lore/                ← EL UNIVERSO (canon narrativo)
│   ├── canon.md          ⏳ (hoy lore_final.md)
│   ├── personajes/       ⏳
│   ├── style-guide.md    ⏳
│   └── principles.md     ⏳
│
├── gestos/               ← LAS MANIFESTACIONES MONETIZABLES
│   ├── 01-miniserie/     ⏳
│   ├── 02-oraculo/       ⏳
│   ├── 03-game/          ⏳ (apunta a ../pax-game/)
│   ├── 04-video-bg/      ⏳
│   └── _backlog/         ⏳ (gestos candidatos por research)
│
├── app/, lib/,           ← la webapp = "gesto showcase"
│   components/, public/
│
├── content/              ← FUENTE de la webapp (lib/docs.ts lee de acá)
│                            durante la reorg: source of truth de lore/personajes/storyboards
│                            post reorg: solo lo que la app necesita servir
│
├── research/             ← research vivo
│   └── gestos-candidatos-2026-05-21.md ⏳ (research en background)
│
├── process-log/          ← historia de iteraciones del proyecto
│
└── _archive/             ← lo deprecado, recuperable, NO borrado
    ├── pax-duplicado/    ⏳
    ├── lore-versions/    ⏳
    ├── content-v2/       ⏳
    ├── app-legacy-disabled/ ⏳
    ├── personajes-fix-txt/  ⏳
    ├── episodio-1-antiguo/  ⏳
    └── backups-comprimidos/ ⏳
```

---

## Proyectos vecinos relacionados

- **`../pax-game/`** — el gesto 03-game vive en repo separado por razones técnicas (motor de juego, scripts propios). Su canon DEBE sincronizar contra `_lore/canon.md`.
- **`../pax-miniserie/`** — archivo histórico Quest 1 (2026-04-28). Lore Pachamama / Fisher King, terminología obsoleta. **NO usar para contenido nuevo.**

---

## Fases de la reorganización

| Fase | Status | Qué |
|------|--------|-----|
| 0 | en curso | Meta-archivos (manifesto, INDEX, CANON, política de archive) |
| 1 | pendiente | Mover archivos seguros (no tocan app) a `_archive/` |
| 1b | pendiente | Consolidar `personajes finales/` PNGs en `content/personajes/` |
| 2 | pendiente | Mover content/ a `_lore/` + `gestos/` + actualizar `lib/docs.ts` |
| 3 | pendiente | `.md` mínimo para los 6 personajes nuevos sin lore |
| 4 | pendiente | Actualizar `CLAUDE.md` + crear `_README_HISTORICO.md` en pax-miniserie |
| 5 | pendiente | Auditar `pax-game/` y sincronizar canon |

---

## Para Claude / agentes

Antes de cualquier trabajo en este repo:
1. Carga la memoria `pax_meta_concept.md` (modelo de las 3 capas)
2. Carga la memoria `pax_current_canon.md` (lore vigente)
3. Identifica qué gesto se está alimentando
4. Si la tarea no alimenta ningún gesto, evalúa si va a `gestos/_backlog/` o si es trabajo del lore común
