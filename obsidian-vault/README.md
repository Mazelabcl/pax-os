---
title: "Obsidian vault — Pax"
description: "Setup instructions + estructura del vault. Edita esto cuando descargues la app."
date: 2026-05-05
---

# Obsidian — vault Pax

Este vault es el cerebro vivo del proyecto Pax. Funciona localmente con la app Obsidian (gratis) y eventualmente se publica a la web con Obsidian Publish ($8/mes).

---

## Cómo abrir el vault

1. Descarga Obsidian gratis: https://obsidian.md/download
2. Abre la app.
3. Click "Open folder as vault".
4. Apunta a: `C:\Users\aldot\.gemini\antigravity\scratch\pax-os\` (la raíz del repo, NO esta subcarpeta).

Esto convierte TODO el repo en un vault Obsidian. Todos los `.md` se vuelven nodos navegables. El grafo (View → Graph view) muestra las conexiones — sinapsis del proyecto Pax.

---

## Estructura del vault (interpretación de carpetas existentes)

| Carpeta | Qué contiene en Obsidian |
|---|---|
| `content/` | Notas principales: principles, roadmap, INDEX, lore, pitch |
| `content/personajes/` | Nodos por personaje |
| `archive/` | Historia (Quest 1) |
| `process-log/` (gitignored) | Decisiones del director, debates internos |
| `obsidian-vault/` | Esta carpeta — config y estilo del vault |
| `~/.claude/projects/.../memory/lessons/` | Lecciones (cargables como vault external) |

---

## Convenciones de linking

Para que el grafo se vea rico, usar `[[doble corchete]]` cuando referenciar otra nota:

```markdown
Los Pax son [[runners alquimistas]] que viven en [[túneles subterráneos]].
Itzel, definida en [[personajes/itzel]], es protagonista del [[piloto]].
```

Cuando aparezca `[[X]]` y no exista una nota X.md, Obsidian lo marca en gris — invitación a crear esa nota.

---

## Plugins recomendados (todos gratis)

Una vez abierto el vault:

1. **Settings → Community Plugins → Browse**
2. Instalar:
   - **Dataview** — queries sobre tu vault (ej. listar todas las decisiones por fecha)
   - **Excalidraw** — whiteboards para mapas mentales del lore
   - **Templater** — templates para nuevas notas
   - **Graph Analysis** — métricas del grafo (qué nota es más central, etc.)

---

## Branding Pax — `publish.css`

Cuando actives Obsidian Publish, sube este archivo CSS para que el sitio público tenga look-and-feel Pax (paleta canónica + tipografía + grafo en colores del proyecto).

Ver: `obsidian-vault/publish.css` (en construcción cuando confirmes pago de Publish).

---

## Próximos pasos para mí (orquestador)

1. Confirmar que abres el vault correctamente.
2. Crear template de "decisión" (Templater) para que cada decisión nueva siga formato consistente.
3. Crear `glosario.md` como nodo central de términos canónicos.
4. Cuando pagues Publish: diseñar `publish.css` Pax + connect to Vercel preview.

---

## Mantenimiento

Este vault es solo lectura/escritura desde Obsidian o desde el editor del repo (VS Code, etc.). Los archivos `.md` son los mismos que el repo Git ve. Cuando hagas commit en git, los cambios viajan al vault y viceversa.

**No instalar Obsidian Sync.** No lo necesitamos — git ES nuestro sync.
