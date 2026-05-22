# Pax — mapa maestro del repositorio

> **Estado:** Reorganización completa al 2026-05-22. Fases 0-4 commiteadas, Fase 5 en ejecución (sync canon a `pax-game/`).

Este repo es el **hub** del proyecto Pax. Contiene el meta-manifesto, el lore canónico, varios gestos, la webapp showcase y el archivo histórico.

Si vienes de cero, lee en este orden:
1. [`_meta/manifesto.md`](./_meta/manifesto.md) — qué es Pax (idea + lore + gestos)
2. [`_lore/canon.md`](./_lore/canon.md) — la mitología vigente (anuraK + Ayni + cristales)
3. [`_lore/personajes/_index.md`](./_lore/personajes/_index.md) — el cast (22 .md + 16 PNGs)
4. [`gestos/*/README.md`](./gestos/) — qué es cada gesto monetizable

---

## Estructura del repo

```
pax-os/
├── INDEX.md              ← este archivo
├── CLAUDE.md             ← instrucciones para Claude
├── README.md             ← onboarding humano
│
├── _meta/                ← LA IDEA (propuesta de valor del proyecto)
│   ├── manifesto.md      ✅
│   └── roadmap.md        ✅
│
├── _lore/                ← EL UNIVERSO (canon narrativo)
│   ├── canon.md          ✅ (era lore_final.md)
│   ├── principles.md     ✅
│   ├── style-guide.md    ✅
│   ├── lore-amigable.md  ✅
│   ├── canon-status.md   ✅
│   ├── _index.md         ✅
│   ├── personajes/       ✅ (22 .md + 16 PNGs)
│   │   ├── _canon.md, _index.md
│   │   ├── jiggy, wiz, byte, kz, zek, luxa, agatha, onyx, mariela
│   │   └── alma, aura, baba, brizk, cyfer, fortis, iris, kif, ludus, luz
│   └── pax-core/         ✅ (pax-core.md + naming-rukla.md)
│
├── gestos/               ← LAS MANIFESTACIONES MONETIZABLES
│   ├── 01-miniserie/     ✅ (episodios-12-outline + storyboards/ + seedance-prompts/)
│   ├── 02-oraculo/       ✅ (5 .md + visuals/)
│   ├── 03-game/          ✅ (README; gesto vive en ../pax-game/)
│   ├── 04-video-bg/      ✅ (_FINAL + beat-sheet + deep-dives)
│   └── _backlog/         ✅ (research/gestos.html con 15 candidatos)
│
├── content/              ← solo lo que la webapp sirve
│   ├── CHANGELOG.md      (leído por lib/changelog.ts → /docs en webapp)
│   ├── README.md
│   └── videos/           (outputs Seedance, untracked)
│
├── app/, lib/,           ← webapp Next.js (la webapp = "gesto showcase")
│   components/, public/
│
├── scripts/              ← 11 generators activos (openai_images, seedance, oraculo, canon_v2, video_bg)
│
├── research/             ← investigaciones vivas
│   ├── gestos-candidatos-2026-05-21.md ✅
│   └── gestos.html       ✅ (visualizador self-contained)
│
├── process-log/          ← historia de iteraciones (38 archivos)
│
└── _archive/             ← lo deprecado, recuperable, READMEs por subcarpeta
    ├── pax-duplicado/, lore-versions/, content-v2/, content-episodio-1/
    ├── app-disabled-routes/, scripts-legacy/, app-legacy-disabled/
    ├── personajes-fix-txt/, content-test-images/, content-exploratory-images/
    ├── canon-v2/, video-bg-v1/, content-indices-viejos/
    └── backups-comprimidos/ (.gitignored, .rar/.zip locales)
```

---

## Proyectos vecinos relacionados

- **`../pax-game/`** — Starter Template Mazelab v3 (NO un game terminado todavía, pero con plan futuro de game). Reusa canon de Pax vía `scripts/sync-canon.js`. Ver [`gestos/03-game/README.md`](./gestos/03-game/README.md).
- **`../pax-miniserie/`** — archivo histórico Quest 1 (2026-04-28). Lore Pachamama / Fisher King, terminología obsoleta. **NO usar para contenido nuevo.** Ver `../pax-miniserie/_README_HISTORICO.md`.

---

## Fases de la reorganización (2026-05-21 al 2026-05-22)

| Fase | Status | Qué se hizo | Commit |
|------|--------|-------------|--------|
| 0 | ✅ | Meta-archivos: INDEX, manifesto, _archive/README, MEMORY.md | (incluido en Fase 1) |
| 1 | ✅ | Mover duplicados a `_archive/` + consolidar PNGs personajes | `48c26fc` |
| 1c | ✅ | Cleanup disabled routes + scripts one-shot + content/v2 + content/episodio-1 | `c9c5d24` |
| 2 | ✅ | Reorganizar `content/` → `_lore/` + `gestos/` + actualizar `lib/*` | `29022a7` |
| storyboards | ✅ | 6 huérfanos a `_huerfanos/` con README | `f6f326d` |
| 3 | ✅ | 10 chars nuevos + enriquecer jiggy/kz + mapa de vínculos | `f08e2f8` |
| 4 | ✅ | CLAUDE.md alineado al modelo de 3 capas + README histórico en pax-miniserie | `f08e2f8` |
| 5 | en curso | Sync canon a `pax-game/` (parchando sync-canon.js + bridge agent) | — |
| research | ✅ | 15 candidatos de gestos rentables 2026 + HTML visualizador (96/100 confidence) | `e5b58f9` |

---

## Para Claude / agentes

Antes de cualquier trabajo en este repo:
1. Carga la memoria `pax_meta_concept.md` (modelo de las 3 capas)
2. Carga la memoria `pax_current_canon.md` (lore vigente)
3. Lee `_meta/manifesto.md` y `_lore/canon.md`
4. Identifica qué gesto se está alimentando
5. Si la tarea no alimenta ningún gesto, evalúa si va a `gestos/_backlog/` o si es trabajo del lore común

**Idioma del proyecto:** español neutro. No voseo argentino.
