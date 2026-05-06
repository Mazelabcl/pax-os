---
title: "Quest 1 — archivo histórico"
description: "Snapshot honesto del primer intento Pax. Qué se hizo, qué falló, qué se aprendió."
date_archived: 2026-05-05
status: archivado
---

# Quest 1 — Archivo

Esta carpeta es el museo. No es source-of-truth.

## Qué fue Quest 1

Primer intento completo de definir Pax como mini-serie animada con web app de feedback para Pipez. Trabajo realizado entre 2026-04-25 y 2026-05-04.

### Lo que se intentó construir

1. **Lore v4** — civilización subterránea de "runners alquimistas" con 6 naciones (Apus, Itzam, Sahasi, Aos, Mimi, Rapa), mecánica lung-gom-pa, anti-pulso, cristales kuya, Pax Wayra como rol humano puente. ~2750 palabras.

2. **Protagonista** — 4 candidatos al "elegido inesperado" (Toño Riroroko, Itzel Pat Canul, Daniel Mamani Quispe, Camila Reyes Huenchupan). Itzel finalista — 14 años, guía junior de cenotes en Pisté, Yucatán.

3. **Episodio 1 piloto v2** — 13 escenas, 3:48 minutos, cold open Apu con cristal quebrándose, detonante Itzel limpiando cenote Sak Ek' sola post-tormenta.

4. **Pitch maestro** — corto cinematográfico (148 palabras), corto segunda persona alternativa (149 palabras), largo (1199 palabras). Tagline lockeada: *"El mundo no se sostiene con héroes. Se sostiene con quien limpia algo que nadie va a ver."*

5. **5 imágenes ancla** generadas con GPT Image 2:
   - Imagen 1: La piedra apagándose (cold open)
   - Imagen 2: Red de gemas latiendo bajo las 6 naciones
   - Imagen 3: Ola muda de ausencia atravesando una calle
   - Imagen 4: Objeto roto sobre piedra al amanecer (cierre piloto)
   - Imagen 5: Itzel saliendo del cenote
   
   Rondas: R1 text-only (rechazada), R2 con references locales (rechazada parcial), R3 imagen 1 con IDENTITY LOCK Pax (aprobada).

6. **Web app `/v2`** desplegada en Vercel con: landing, lore, personajes, episodio, proceso, pitch ilustrado.

### Por qué se cerró Quest 1

Aldot leyó el output final y dijo:
- *"em cuesta entenderlo todavia .. siento que no está explicado de forma winner..vendedora .. no lo enceuntro memorable la verdad y me quedan mas dudas y pregunta que claridad"*
- *"no me gustaron nada las fotos..no se basaste nada en ningun personaje ni DNA"*
- *"la historia tampcoo me calza..q es eso de que la maya fue vestida..eso es cmo un dato super irrelevante"*
- *"se ausmen cosas 'los pax son corredores-alquimistas...q es eso?? se asume cmo que la persona que lee entiende todo y no es asi"*

**El diagnóstico final:** Quest 1 construyó un castillo de jerga interna (runners alquimistas, kuya, Pax Wayra, lung-gom-pa, Sak Ek', anti-pulso, 6 naciones con mecánicas distintas) que fue rechazado por densidad incomprensible para lector cold. Los confidence-loops marcaron 87-89/100 pero no correlacionaron con calidad percibida — el critic medía coherencia interna, no claridad externa.

### Lo que SÍ funcionó (rescate)

- **Char sheets visuales del cast:** Jiggy, Wiz, Byte, Luxa, Zek, Mariela, Itzel — siguen siendo canónicos. Permanecen en `public/images/personajes/`.
- **Style-guide visual:** `content/style-guide.md` — render base 3D PBR neon-magic. Sigue siendo canónico.
- **Concept arts Block A** (sesión anterior): cueva, notebook, kitchen, etc. Útiles como references.
- **Portadas:** `public/images/portadas/`.
- **Infraestructura técnica:** scripts/openai_images.py (`generate_image()` + `edit_image()`), web app Next.js base, deploy Vercel funcionando.

### Lecciones loggeadas

- **L1** (`lessons_screenwriting.md`): cold open mítico necesita pitch.md separado para lector cold
- **L2** (`lessons_lore.md`): protocolo "DIFF de pérdidas + mapeo must-fix" para todo R2+ de architect
- **L3** (`lessons_screenwriting.md`): pipeline visual debe atarse al style-guide canónico antes de aplicar referencias estéticas externas
- **L4** (a loguearse en `lessons_orchestration.md`): confidence loop falla si el critic optimiza por coherencia interna sin gate de cold-reader independiente
- **L5** (a loguearse en `lessons_pax_pipeline.md`): cuando el lore declara especie no-humana, el prompt visual debe declarar IDENTITY LOCK con char sheet específico al inicio del prompt

### Costo monetario aproximado

- Perplexity research: ~$0.50
- GPT Image 2 (Quest 1 completo, R1+R2+R3): ~$0.65
- **Total: ~$1.15 USD** + tokens de agentes (cubiertos por plan Pro de aldot)

### Tiempo invertido

~3 sesiones de Claude Code, ~6-8 horas wall clock con paralelismo de agentes.

## Estructura de esta carpeta

Pendiente de mover (cuando aldot decida):
- `content/v2/` (todo el contenido v2 fallido) → `archive/quest-1/content-v2/`
- `app/v2/` (rutas Next.js de la web v2) → `archive/quest-1/app-v2/` o eliminar y dejar redirect
- `process-log/` (debates entre agentes, scores, validaciones) → `archive/quest-1/process-log/` o mantener como gitignored

Por ahora esos archivos siguen en su ubicación original. Aldot decide cuándo nuke o mover físicamente.

## Cómo ver Quest 1 públicamente

Mientras no se mueva, sigue accesible en:
- `https://pax-os.vercel.app/v2` (landing Quest 1)
- `https://pax-os.vercel.app/v2/lore` (lore v4)
- `https://pax-os.vercel.app/v2/pitch` (pitch corto ilustrado)
- `https://pax-os.vercel.app/v2/episodio-1` (episodio v2)
- `https://pax-os.vercel.app/v2/proceso` (cómo se llegó)

Cuando se "nuke", esos URLs caerán o redirigirán al nuevo home Quest 2.

## Mensaje al futuro

Quest 1 no fue un fracaso — fue la primera vuelta del prensil. Sin ella no había forma de saber que el camino era doble (sistema + historia, no solo historia), que el tono debía ser juguetón en vez de melancólico, ni que los confidence-loops necesitaban gate de cold-reader independiente.

Quest 2 nace de estos errores. Honor a los errores que enseñan.

— Aldot + Claude (Opus 4.7), 2026-05-05
