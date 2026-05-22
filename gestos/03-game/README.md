# Gesto 03 — Game Pax

**Qué es:** videojuego del universo Pax. Motor propio / pipeline gamedev independiente del stack web.

**Status:** **vive en repo separado** — `../../../pax-game/`. Razones técnicas: pipeline gamedev (motor, assets binarios pesados, build chain) no comparte estructura con la webapp Next.js. Canon debe sincronizar contra `../../_lore/canon.md` (no duplicar lore allá).

**Monetización tentativa:** PC/mobile premium o free-to-play con cosméticos. Demo gratis como funnel a la mini-serie + oráculo.

## Sincronización con el lore

Cualquier cambio de canon (nombres, terminología, eventos canónicos) vive en `../../_lore/canon.md` de este repo. El repo `pax-game/` consume ese canon como fuente única. No duplicar archivos de lore del lado del juego.

## Archivos clave aquí

Ninguno por ahora. Este directorio es solo placeholder de catálogo en `gestos/`. Toda la implementación vive en el repo separado.
