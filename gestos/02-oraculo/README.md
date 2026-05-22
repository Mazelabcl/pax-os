# Gesto 02 — Oráculo Pax

**Qué es:** producto web interactivo. El visitante ingresa fecha (+ opcionalmente hora y lugar) y recibe una "lectura" personalizada que cruza Tzolkin maya, arquetipo Pax derivado del nahual y carta astral opcional. Voz narrativa "abuelos pax". Output: tarjeta-lectura compartible con serial único.

**Status:** MVP funcional en producción (`/oraculo`). Backend: Claude Haiku 4.5 vía OpenRouter + free-astrology-api + Tzolkin local determinístico. Card design v1 definido.

**Monetización tentativa:** carta-lectura como producto digital de bajo ticket ($3-9). NFT-like serial único por persona. Upsell a "deep reading" más larga. Posible API B2B para integrar en otros productos místicos.

## Archivos clave

- `_lore.md` — lore diegético del Oráculo dentro del universo Pax.
- `_research.md` — research sobre Tzolkin, astrología, arquetipos + APIs.
- `_card-design.md` — spec del producto-carta para frontend.
- `_critica-mvp.md` — análisis crítico del MVP actual.
- `_variantes-visuales.md` — 5 propuestas estéticas + 20 prompts GPT Image 2.
- `visuals/` — 3 variantes de exploración visual (C, D, v3).

## Lore base

Canon narrativo en `../../_lore/canon.md`. Pax-core (esencia del proyecto) en `../../_lore/pax-core/pax-core.md`.
