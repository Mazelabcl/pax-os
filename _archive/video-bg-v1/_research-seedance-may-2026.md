---
title: "Research Seedance 2 + hook design para video de fondo web — mayo 2026"
description: "Brief ejecutivo sintetizado de 5 consultas Perplexity (sonar-pro-search + sonar-reasoning-pro), pensado para diseño de 2 videos hero scroll-triggered del sitio Pax."
date: 2026-05-18
sources_run: 2026-05-18
director: pax-seedance-director
---

# TL;DR ejecutivo (10 lineas)

1. **Seedance 2.0 sigue siendo el estado del arte en mayo 2026** — recibió updates desde noviembre 2025 en multi-shot, multimodal (texto + 9 imagenes + 3 videos + 3 audios en un solo prompt), edicion/extension de video, adaptive duration y adaptive aspect ratio. La caracteristica diferencial mas relevante: audio + video generados en un solo pase con dual-channel audio.
2. **Aspect ratios confirmados nativos**: 16:9 (1280×720) y 9:16 (720×1280) ambos soportados a 720p — no hace falta crop manual. Tambien 4:3, 1:1, 3:4, 21:9.
3. **Duracion optima para hero background web: 10-15 segundos**. 12s es el sweet spot mas citado. Menos de 10s se siente "GIF-like" en pantallas grandes; mas de 15s pesa mucho para web (target 2-5 MB por video).
4. **Tier recomendado: Seedance 2 Pro** (no Lite). Pro tiene mejor coherencia de motion, menos jitter en camera moves complejos, mejor temporal consistency a 15s, menos artifacts post-compresion. Pro: ~$0.20-$0.40/seg a 1080p. Lite: ~$0.10-$0.20/seg. Para hero web la diferencia absoluta ($3-6 vs $1.50-3 por clip de 15s) es minima vs el salto de calidad.
5. **Audio nativo: incluirlo SI, aunque el sitio lo mutee.** Razon: el video puede reusarse en redes (Reels/Shorts) donde el audio importa, y el costo es el mismo. Para el sitio se sirve como WebM/MP4 sin audio track.
6. **Hook = primeros 1-3 segundos.** En 2026 el thumb-stop window cayó a 1-1.5s. El primer frame debe ser HIGH-IMPACT visual: macro extremo, alto contraste, foco unico claro, movimiento perceptible en 0.5-1s.
7. **Visual beat (rhythm sin audio)** es retention crítico. Cuts cada 0.5-1s simulan kick drums; cambios de escala simulan bass; pops de luz/color simulan cymbals. Mapear beats en una grilla de 120 BPM imaginaria (1 hit cada 0.5s).
8. **Seamless loop techniques**: motion ciclica (drift, particulas, light sweeps), cut on motion (alinear vector primer/ultimo frame), crossfade 8-15 frames en post, evitar eventos unicos no-ciclicos, mantener color/exposicion estable en bordes del loop.
9. **Sintaxis Seedance para camera moves complejos**: lenguaje natural director-style. Frases clave: "the camera performs a continuous deep zoom in", "smoothly dollies and zooms out from macro to wide", "abrupt cut to", "POV chase-cam from behind and above". Constraints en negativo afirmativo: "no cuts, no zoom, single continuous tracking shot" o "single hard cut only, no crossfades".
10. **Limit duro**: Seedance acepta 4-15s por clip. Para nuestros 2 videos de 15s usaremos multi-shot syntax con `lens switch to` o `abrupt cut to` para encapsular 2-3 sub-shots en un solo prompt, o partir en 3×5s y montar en post si el modelo colapsa coherencia.

---

# 1. Que cambio en Seedance 2 desde noviembre 2025

## Confirmaciones (mantienen vigencia)
- 6-part canonical syntax: Subject → Motion → Camera → Environment → Lighting → Style.
- Max ~80-100 palabras efectivas por prompt. Pasarse de 250 satura prioridades.
- Una accion primaria + una secundaria ambiental por clip (no apilar competing actions).
- Soporta seed entero para reproducibilidad.
- Multi-shot sintaxis `lens switch to` (max 3 sub-shots).
- Sistema `@Image1`, `@Image2`, `@Video1`, `@Audio1` para referencias.
- Limites: 9 imagenes, 3 videos, 3 audios por prompt (max 12 archivos).
- Aspect ratios: 21:9, 16:9, 4:3, 1:1, 3:4, 9:16.
- Duracion: 4-15 segundos por clip.

## Lo nuevo / refinado en mayo 2026
- **Generacion conjunta audio-video nativa con dual-channel audio** — antes era mono-ish, ahora estereo real. Util para video que reusaras en plataformas con sonido.
- **Adaptive duration y adaptive aspect ratio**: el modelo puede ajustar internamente la duracion final a lo que la composicion necesita (dentro del rango 4-15s) si lo dejas en `auto`.
- **Video editing y video extension**: puedes pasar un video como input y pedirle al modelo que extienda 5s más o edite un segmento. Util si un clip generado queda corto.
- **Multi-shot mejorado**: la comunidad reporta que las transiciones tipo `abrupt cut to` son mas confiables que en 1.5 — antes a veces hacia crossfade involuntario.
- **Mejor motion physics**: agua, particulas, telas, pelo — fisicas mas consistentes.
- **Lip-sync a nivel de fonema en 8+ idiomas** (incluye español).

## Tiers actualizados mayo 2026

| Tier | Resolucion | Duracion max | Audio nativo | Costo aprox |
|---|---|---|---|---|
| Lite / Fast | 480p-720p | 10 s | basico | $0.10-$0.20/seg (12 credits/seg en algunos pricing pages) |
| Pro (2.0) | 1080p | 15 s | si + dual-channel | $0.20-$0.40/seg (14 credits/seg, ~$0.247/seg en provider de referencia) |
| Cinema | 2K | 15 s | si + multi-shot avanzado | ~$0.80/seg |

**Para Pax hero videos: Pro.** Cinema solo si el budget lo permite y queremos 2K nativo (lo cual para hero web es overkill).

---

# 2. Camera moves complejos — sintaxis validada mayo 2026

Seedance es como dirigir un Steadicam/drone virtual. Spell out cada move con start/end targets, timing, constraints.

## Template universal

```
[Scene + subject]
[Primary camera move with start → end]
[Secondary move or transition]
[Speed + duration hints: slow / medium / fast]
[Constraints: "no cuts" / "abrupt cut to X" / "single continuous shot"]
```

## Patrones para nuestros 2 videos

### Deep zoom into surface (Video 1)
```
The camera performs a continuous deep zoom in, pushing closer
until [target] fills the entire frame, then continues to zoom into
[next layer]. Smooth motion, no cuts, non-fixed camera.
```

### Macro to wide pull back (Video 2 inicio)
```
Start on extreme macro of [subject].
The camera smoothly dollies and zooms out from macro → to medium
shot → to wide environmental shot.
Continuous zoom, no camera cuts, speed ramps from slow to fast.
```

### Drone follow chase cam (Video 2 final)
```
POV chase-cam from slightly behind and above the runner's head,
looking forward down the [tunnel/path].
The camera tracks and follows continuously, keeping subject
centered as they dodge left and right.
Very fast forward motion, slight handheld wobble, motion blur on
walls. No cuts, no zoom, single continuous tracking shot.
```

### Abrupt transition (entre beats del Video 2)
```
[Shot A description], abrupt cut to [Shot B description].
Fast snappy cut, no crossfade, no slow dissolve.
```

## Constraints utiles (lo que NO hace la camara)
- "No cuts, no zoom, single continuous tracking shot."
- "No orbiting, camera only moves forward along the tunnel axis."
- "No random angle changes."
- "Non-fixed camera, strong forward dolly motion."
- "Single hard cut only, no crossfades, no extra angle changes."

Estas constraints son first-class conditioning en Seedance 2 — funcionan, no son ruido.

## Time-coded variant (opcional)
```
Single continuous shot, [N] seconds.
First [N/2] seconds: [behavior A].
Last [N/2] seconds: [behavior B].
No cuts, single continuous movement.
```

Seedance no obedece timestamps exactos pero respeta "first half / second half" suficientemente para staged behavior.

---

# 3. Hook design para video de fondo web scroll-triggered

## Especificaciones tecnicas hero background (web)

- **Duracion loop**: 10-15s (sweet spot 12s). 5s se siente GIF-like, >15s pesa demasiado.
- **File size**: 2-5 MB target, max 10 MB en desktop.
- **Resolucion**: 720p a 24-30 fps suficiente. 1080p solo si full-screen en monitores grandes y el tamaño aguanta.
- **Autoplay**: muted, looped, sin controles (browsers solo permiten autoplay mute).
- **Trigger scroll**: Intersection Observer dispara play cuando hero entra al viewport. Static poster image antes del play.
- **Mobile**: muchos teams desactivan video y muestran static image. Recomendamos respetar `prefers-reduced-motion`.
- **Formato**: WebM + MP4 fallback. Sin audio track (silenciar en encode).

## Hook = primeros 1-3 segundos

El thumb-stop window en 2026 es 1-1.5s. El primer frame y el primer segundo deciden retention.

### Tipos de visual hook que funcionan
1. **Macro extremo**: textura imposible que solo se ve a esa escala — gem, ojo, particula. Genera intriga "que es eso?".
2. **Pattern break / movimiento inesperado**: elemento que entra desde un borde no convencional (abajo arriba, diagonal).
3. **High contrast con foco unico**: sujeto unico iluminado contra fondo oscuro. Cero clutter.
4. **Curiosidad "after first"**: mostrar el resultado primero, dejar al usuario querer ver el "como".
5. **Movimiento perceptible en 0.5-1s**: algo CAMBIA visiblemente en el primer segundo. Estatico = scroll.

### Anti-patterns
- Cargar con titulo de texto que distrae del visual (en hero background NO hay texto sobre el video).
- Animation pesada que sature lectura del header HTML overlay.
- Loop con evento unico no-ciclico (persona caminando una vez de izq a der).
- Color shifts violentos en bordes del loop.

## Visual rhythm sin audio

Mapear el video a una grilla imaginaria de 120 BPM (1 beat cada 0.5s). Cada beat = un evento visual:
- **Cuts as drum hits** (kick/snare): cambios de plano o de escala dura.
- **Scale/position changes as bass**: pushes grandes, slides, depth shifts.
- **Contrast/color pops as cymbals**: flashes breves de brillo, exposicion.
- **Sub-motion as hi-hats**: micro-bounces, pulse glows, parallax suave.

Estructura recomendada para 12-15s:
- **Hook (0-3s)**: primer evento high-impact en <1s. Establece tono.
- **Groove (3-9s)**: rhythm constante, cuts/cambios cada 1s, variaciones cada bar (~4s).
- **Payoff (9-12s)**: o burst rapido (4 cuts en 0.5s) o hold sostenido con micro-pulse.
- **Loop seam (12-15s)**: motion ciclica que conecta con el primer frame.

## Seamless loop checklist

- Motion ciclica no-lineal (drift, particulas, gradients flowing).
- Cut on motion: vector del ultimo frame matchea vector del primero.
- Crossfade 8-15 frames en post si el modelo no lo logra solo.
- Exposicion y color stable en bordes del loop (sin shifts).
- Sin eventos one-time (persona que entra y sale = NO loop).
- Si hay personaje, que entre mid-motion y salga mid-motion (no inicio ni fin completo de movimiento).

---

# 4. Audio nativo Seedance — vale la pena para video que se muestra mute?

**Si, incluirlo.** Razones:
1. El costo de generacion es el mismo (Seedance hace audio+video en un pase, no es un cargo extra).
2. Si el video se reusa en redes (Reels/Shorts/TikTok) donde tiene sonido, ya esta resuelto.
3. Permite versionado: el master con audio se guarda; al servir en web se extrae el video track sin audio.
4. Garantiza que el "sound design implicito" del modelo coincida con el visual — frames mas coherentes ritmicamente porque el modelo los compuso pensando en un beat.

**Notas tecnicas**:
- Pedir audio en el prompt: "Audio: [description]" o "with synchronized ambient soundscape of [...]".
- Para Pax: ambient pad + textura cueva + cristal bell tones + heartbeat low-end. Cero dialogo en estos hero videos.
- Al servir en web: `<video muted>` y exportar version sin track de audio para reducir size.

---

# 5. SFX / musica viral 2026 — sonido que coincide con visual

Aunque el video corra mute, el "sentir musical" que tendria con audio fortalece la composicion visual:

- **Drop sintetico grave + sub-bass**: para reveals (frame final video 1, frame de Jiggy en video 2).
- **Cristal bell tones, granular textures**: para macro shots, cristales, atmosfera Pax.
- **Heartbeat low end**: ancla emocional, frecuencia organica.
- **Risers**: anticipan reveals.
- **Hard impact + reverse cymbal**: marca el corte abrupto en video 2 (macro → chase).
- **Ambient drone con shimmer**: groove sostenido en partes lentas.

Para los frames visuales, el equivalente visual:
- Drop → cambio de escala / camera punch in.
- Bell tone → particula iluminada / chispazo.
- Heartbeat → pulse de luz que late.
- Riser → camera acceleration / zoom-in continuo.
- Impact → cut duro / flash.
- Drone → motion sostenida lenta.

---

# 6. Costo y tier recomendado para Pax

**Recomendacion: Seedance 2 Pro para los 2 videos hero.**

Justificacion:
- Hero web = usuarios miran fijo. Artifacts y jitter de Lite se notan en loop.
- Camera moves complejos (deep zoom continuo, macro→chase) requieren motion coherence de Pro.
- Pixar 3D PBR style necesita lighting nuances que Lite aplana.
- Jiggy debe mantener identity lock 15s — temporal consistency de Pro reduce drift facial.
- Diferencia absoluta de costo es minima: ~$3-6 por clip de 15s Pro vs $1.5-3 Lite. Para 2 videos × 3 retries promedio = ~$18-36 extra. Negligible vs calidad.

Lite solo si:
- Generamos batch de prototipos para ideacion.
- Camera move es muy simple (gentle dolly, slow pan).
- Background es abstracto/blurred y artifacts no se notan.

**Provider sugerido**: fal.ai o Replicate (ambos exponen Seedance 2 Pro estable). BytePlus ModelArk si se quiere ir directo al origen ByteDance.

---

# 7. Aplicacion concreta a nuestros 2 videos

## Video 1 — Deep dive into Pax world
- Duracion: 15s.
- Multi-shot: single continuous camera move (deep zoom/dolly through earth layers). NO `lens switch`, NO `abrupt cut`. Una sola toma.
- Visual rhythm: groove sostenido. Cambios de palette cada 3s (superficie → corteza → cuevas → cristales → mundo Pax revelado).
- Hook frame: superficie con detalle ultra-nitido (gota de rocio, hoja, textura piedra). Camera zoom inmediato.
- Final frame: reveal wide del mundo Pax con bioluminiscencia + posible Jiggy o grupo en silueta lejana.
- Loop: motion descendente continua. Para loop seam, el ultimo segundo "se vuelve a abrir" hacia superficie (motion vector matchea primer frame).
- Audio nativo: ambient drone → granular textures → bell tones risers → drop final con sub-bass.

## Video 2 — Gem macro to chase
- Duracion: 15s.
- Multi-shot SI: 3 sub-shots con `lens switch` y `abrupt cut`.
  - Sub-shot 1 (0-5s): macro gema + pull back lento.
  - Sub-shot 2 (5-7s): Jiggy entra y toma gema. Punch in dramatico.
  - Sub-shot 3 (7-15s): abrupt cut to drone chase cam siguiendo Jiggy corriendo.
- Visual rhythm: hook macro 0-1s → groove pull back 1-5s → impact cut 5s → energy chase 5-15s.
- Hook frame: macro extremo de gema rosada (cristal Pax) con bioluminiscencia interna. Foco unico, fondo negro.
- Final frame: Jiggy corriendo en wide tunnel cueva con cristales pasando rapido por foreground (parallax fuerte).
- Loop: ultimo segundo Jiggy desaparece tras una columna de cristal → fade-to-bright que matchea con la gema del primer frame.
- Audio nativo: bell tone solo macro → riser durante pull back → hard impact en cut → fast percussive beat durante chase.

---

# 8. Riesgos identificados antes de generacion

| Riesgo | Severidad | Mitigacion |
|---|---|---|
| Identity lock Jiggy a lo largo de 15s con camera move violento | alta | Pasar 3 refs Jiggy (front, 3/4, perfil) + identity-lock phrase obligatoria + considerar partir video 2 en 2 clips de 7.5s |
| Abrupt cut Seedance puede meter crossfade involuntario | media | Phrasing literal: "single hard cut only, no crossfade, no dissolve" — confirmado en 2.0 |
| Deep zoom continuo 15s pierde coherencia geologica | media | Anclar paleta + describir cada layer en orden temporal explicito ("first... then... followed by... finally") |
| Multi-shot >3 sub-shots colapsa | alta | Mantenerse en 3 sub-shots max para video 2 |
| Aspect ratio 9:16 mismo prompt 16:9 | baja | Mismo prompt funciona, pero recomponer mentalmente: en 9:16 los reveals horizontales se cortan. Hacer variantes minimas donde la composicion cambie dramaticamente |
| Audio dual-channel sin uso final en web | nula | Generamos con audio; al servir, encode sin audio track |
| Loop seam visible | media | Crossfade 8-15 frames en post (DaVinci/Premiere). Motion vector matching en prompt |
| Copyright flag por "Pixar style" | alta | Reemplazar siempre por "stylized 3D animation, smooth shading, Pixar-inspired NOT used, cinematic warm lighting, painterly background, soft subsurface scattering" |

---

# Fuentes citables

1. ByteDance Seedance 2.0 official launch announcement (Feb 2026) — multimodal, 9 images + 3 videos + 3 audios, 15s multi-shot, dual-channel audio.
2. Replicate Seedance 2.0 docs — adaptive duration, adaptive aspect ratio, video editing/extension, supported resolution table (1280×720 a 16:9, 720×1280 a 9:16).
3. fal.ai API reference Seedance 2 — limites de input, @ mention syntax, per-second pricing 14 credits/seg Pro, 12 credits/seg Fast.
4. MindStudio comparativa Seedance vs Sora vs Runway mayo 2026.
5. Reddit r/StableDiffusion thread "Seedance 2 Lite vs Pro real-world test" (~marzo 2026) — feedback comunitario.
6. Artlist blog "Background video best practices 2026" — 8-15s, 2-5MB, autoplay muted, intersection observer.
7. WordStream / Sprout Social retention data 2026 — <15s reach 92% completion con strong hooks; thumb-stop window 1-1.5s.
8. LinkedIn / Meta autoplay muted defaults 2026 — 80-90% views are muted.
9. Motion designer guides 2026 — visual rhythm as drums/bass/cymbals, 120 BPM grid mental model.
10. Pax internal research noviembre 2025: `process-log/15a-research-seedance-deep.md` — canonical 6-part syntax, 5/7/10/15s heuristic.

(URLs especificas vienen embebidas en los outputs Perplexity raw; archivados en task logs.)
