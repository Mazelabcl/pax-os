# Gesto 03 — Game Pax

**Qué es hoy:** repo separado en `../../../pax-game/` que **NO es un game terminado todavía**. Su `package.json` se llama `aldot-starter-template` — es el **Starter Template Mazelab v3**: un framework de agentes Claude Code con councils, kickoff, pipeline-v2 y multimodal-validation. Reusa el canon Pax (`_lore/canon.md`) para validar imágenes generadas por IA contra los char sheets oficiales.

**Qué será:** el template ya tiene en `package.json` dependencias de game (`three`, `pixi.js`, `matter-js`, `cannon-es`). El plan futuro es desarrollar un game real sobre esa base. Por eso lo mantenemos categorizado como "gesto 03-game" aunque hoy sea framework.

**Status:** framework activo + game como promesa futura. **NO** te apoyes en este gesto para revenue de corto plazo — su rol actual es soporte a otros gestos (validación visual de chars).

## Monetización tentativa (cuando el game exista)

- PC/mobile premium o free-to-play con cosméticos.
- Demo gratis como funnel a la mini-serie + oráculo.
- Hoy: $0 — el framework no monetiza por sí mismo.

## Sincronización con el lore

Cualquier cambio de canon (nombres, terminología, eventos canónicos) vive en `../../_lore/canon.md` de este repo. El repo `pax-game/` consume ese canon como fuente única via `pax-game/scripts/sync-canon.js` (sincroniza a `pax-game/content/canon-snapshot/`). **No duplicar archivos de lore del lado del juego.**

El agente `pax-game/.claude/agents/pax-canon-bridge.md` traduce el canon a specs accionables para los demás agentes del game (no transcribe, traduce).

## Archivos clave aquí

Ninguno por ahora. Este directorio es solo placeholder de catálogo en `gestos/`. Toda la implementación vive en el repo separado.

## Si retomas el desarrollo del game

1. Verifica que el sync del canon esté al día (`cd ../../../pax-game && npm run sync-canon`)
2. Lee `pax-game/.claude/agents/pax-canon-bridge.md` para entender cómo el framework consume el lore
3. Revisa `pax-game/content/canon-snapshot/manifest.json` para confirmar versión del lore sincronizada
