# _nuevos-pendientes-md/ — PNGs canónicos sin `.md` de lore todavía

## Qué hay aquí

PNGs de personajes que Aldot generó como renders finales (canon visual confirmado) pero que aún **no tienen su archivo `.md` de lore** en `content/personajes/`.

### PNGs presentes

- `alma.png`
- `aura.png`
- `baba.png`
- `brizk.png`
- `cyfer.png`
- `fortis.png`
- `iris.png`
- `kif.png`
- `ludus.png` (original: `Lūdus_Character.png`)
- `luz.png`

## Por qué están aparte

Los PNGs que SÍ tienen `.md` correspondiente viven directamente en `content/personajes/<nombre>.png` junto a su `<nombre>.md`. Los de esta carpeta esperan la Fase 3 de la reorganización, en la que Aldot va a:

1. Dar rol + 1 línea de personalidad por personaje.
2. Generar el `.md` mínimo (canon textual) con esa info.
3. Mover el PNG desde aquí a `content/personajes/<nombre>.png`.

## Reglas para agentes

**NO inventes lore** para estos personajes hasta que Aldot dé rol + 1 línea de personalidad explícita. Esto incluye:
- No inferir personalidad desde el render.
- No deducir Tribu o rol desde la paleta o props del PNG.
- No agregarlos a documentos canónicos (`lore_final.md`, listas de personajes) hasta tener su `.md`.

Si un agente necesita referenciar visualmente a uno de estos personajes (ej. en un prompt de image-gen), úsalo solo como referencia visual literal, sin atribuirle backstory.

## Cuándo se vacía esta carpeta

Cuando los 10 PNGs hayan migrado a `content/personajes/` con su `.md` correspondiente. En ese punto se elimina la carpeta entera (no se archiva — fue siempre staging).

## Origen

PNGs movidos el 2026-05-21 desde `personajes finales/` (raíz del repo, untracked) como parte de la Op 7 de la Fase 1 de reorganización.
