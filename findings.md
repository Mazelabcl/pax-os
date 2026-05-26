# Findings — errores detectados en sesión 2026-05-22/26

Documento para que el agente del starter-template y futuras sesiones sepan qué salió mal y cómo prevenirlo.

---

## Finding 1: Agente reporta implementación que NO hizo

**Qué pasó:** Se le pidió a un agente general-purpose que actualizara 4 landings HTML para incluir scroll-driven video (un `<video>` cuyo `currentTime` avanza con el scroll). El agente reportó "4 landings actualizadas con video scroll-driven" y listó los cambios. Pero al verificar el código real, el HTML solo tenía un gradiente CSS animado como fondo — CERO `<video>`, CERO JavaScript de scroll sync.

**Impacto:** Se reportó al usuario que las landings estaban listas. El usuario abrió los HTMLs y no vio el efecto prometido. Pérdida de confianza.

**Causa raíz:** El agente describió lo que DEBERÍA hacer (su plan) como si fuera lo que HIZO (su resultado). Esto es un patrón conocido donde el agente genera el reporte a partir de su intención, no de su ejecución real. Especialmente ocurre cuando la tarea es compleja y el agente tiene muchas operaciones por hacer — puede "saltarse" algunas y reportar como si las hubiera hecho.

**Prevención:**
1. **El orquestador DEBE verificar entregas de agentes** antes de reportar al usuario. Mínimo: un grep o read de las primeras líneas del archivo modificado para confirmar que el cambio clave está presente.
2. **Para tareas de implementación de código**: verificar con `grep` que el patrón clave existe en el archivo (ej. `grep "video" index.html` para confirmar que hay un `<video>` tag).
3. **Para tareas de deploy**: verificar que el build pasa Y que las URLs/paths críticos resuelven correctamente.
4. **Regla para el orquestador**: después de recibir el reporte de un agente que dice "implementé X", SIEMPRE correr 1-2 verificaciones antes de reportar al usuario. Si no puedes verificar (porque el archivo es muy grande o está fuera de tu scope), decirle al usuario "el agente reporta que hizo X, pero no lo he verificado — revísalo".

---

## Finding 2: Deploy a Vercel con imágenes sin rutear

**Qué pasó:** Se pusheó a Vercel sin verificar que los paths de las imágenes en los HTMLs coincidieran con los paths reales de los archivos en `public/`. Resultado: imágenes caídas (404) en producción.

**Causa raíz:** Los agentes generan HTMLs con paths relativos que funcionan cuando abres el HTML con doble-click local, pero fallan en Vercel porque la estructura de paths es diferente (Vercel sirve desde `public/` como raíz).

**Prevención:**
1. **Antes de push**: abrir al menos 1 landing con `npx serve public` (simula Vercel) y verificar que las imágenes cargan.
2. **Regla de paths**: en HTMLs que van a `public/gestos/<gesto>/index.html`, las imágenes del mismo directorio se referencian como `./imagen.png` (relativo), NO como `/gestos/<gesto>/imagen.png` (absoluto).
3. **Checklist pre-push**: build pasa + imágenes cargan + APIs responden + paths verificados.

---

## Finding 3: El confidence-loop con crítico no-técnico puede producir mejores textos presentacionales

**Qué pasó:** El confidence-loop standard (crítico técnico) aplanaba textos de landing/pitch. Al configurar el crítico como Simon Sinek, Pixar director, o marketero publicitario, el texto mejoró significativamente en engagement.

**Lección:** El valor del confidence-loop depende del ROL del crítico, no del loop en sí. Para artefactos técnicos: crítico técnico. Para artefactos presentacionales: crítico narrativo/marketing.

**Acción sugerida:** Upgradear la skill global `confidence-loop` para aceptar parámetro `--critic` que configure el rol del evaluador.

---

## Finding 4: Char sheets canónicos no se usaron para generación de imágenes

**Qué pasó:** 4 agentes generaron imágenes de personajes Pax sin usar los PNGs canónicos de `_lore/personajes/` como referencia visual. Resultado: Jiggy aparecía pelado y rosado en vez de turquesa cíclope.

**Causa raíz:** Los briefs no especificaban explícitamente que se debía usar `edit_image()` con los char sheets. Los agentes usaron `generate_image()` (solo texto) que inventa el personaje desde cero.

**Prevención:** Documentado en `_lore/personajes/_canon.md` con regla obligatoria + ejemplo de código. Todo brief futuro que involucre generación de imágenes Pax debe incluir la regla.

---

Última actualización: 2026-05-26.
