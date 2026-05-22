---
title: "Video 2 — Seedance 2 Pro prompt final (gem macro to chase)"
duration: "15 seconds, 3 sub-shots with lens switch and abrupt cut"
provider_recommended: "fal.ai or Replicate, model `seedance-2-pro`"
aspect_ratios: "16:9 (1280×720) primary + 9:16 (720×1280) secondary"
date: 2026-05-18
director: pax-seedance-director
---

# Estrategia de generacion

- **Modelo**: Seedance 2 Pro (1080p, 15s, native audio, multi-shot).
- **3 sub-shots dentro de un solo prompt** con multi-shot syntax:
  - Sub-shot A (0-5s): macro gem + slow pull back. Lens switch al final.
  - Sub-shot B (5-7s): Jiggy hand entering + grab + flare. **Abrupt cut** al final.
  - Sub-shot C (7-15s): drone chase cam continuous following Jiggy through Pax cathedral cave.
- **Identity lock Jiggy critico**: incluir char sheet description completa + frase "Identity lock" + refs `@Image1`, `@Image2`.
- **2 generaciones** (16:9 y 9:16) con mismo prompt base + composition lock al final.

# Paths esperados de refs (Phase 2 generara estos)

`@Image1`: Jiggy character canonical reference.
- `C:/Users/aldot/.gemini/antigravity/scratch/pax-os/personajes finales/Jiggy_Character.png` (EXISTE — char sheet final del usuario).

`@Image2`: Frame 0 hero macro gem (Phase 2 image gen lo creara).
- `C:/Users/aldot/.gemini/antigravity/scratch/pax-os/content/video-bg/video2-gem-chase/img/frame-00-macro-gem_16x9.png`

`@Image3`: Frame 11 cathedral wide reveal (Phase 2 image gen lo creara).
- `C:/Users/aldot/.gemini/antigravity/scratch/pax-os/content/video-bg/video2-gem-chase/img/frame-11-cathedral-wide_16x9.png`

Para 9:16, swap a `_9x16.png` variants.

# Prompt 16:9 (master)

```
A 15-second cinematic action sequence with three connected sub-shots: macro gem reveal, character entry with abrupt cut, then continuous drone chase through underground crystal caves.

Sub-shot A — 0 to 5 seconds, macro reveal:
Extreme macro 100mm close-up of a single rose-magenta crystal gemstone floating against pure black void, hyper-sharp facet detail, intense internal bioluminescent core pulsing magenta-white, strong subsurface scattering, soft outer bloom halo. The camera holds for 1 second on the gem rotating slowly. Then the camera performs a smooth continuous dolly out and pull-back, zooming out from extreme macro to medium macro, revealing the gem now resting on a natural stone pedestal inside a small Pax cave gallery with bioluminescent crystal vein walls in the background. The gem remains the primary light source. Mid-distance jade-amber ambient fill emerges. Reference @Image2 for opening macro composition and color.

Lens switch to:

Sub-shot B — 5 to 7 seconds, character entry:
Tight 50mm shot of the same gem on the pedestal. From the lower-right edge of frame, a small jade-green Pax hand with stubby cartoonish fingers and a tribal cloth wristband enters and closes around the gem in a firm grip. At the moment of contact, a bright magenta-white flare bursts from the gem flooding the frame with intense rose-magenta light. Foreground hand crisp in focus, soft suggestion of a Pax character face out of focus behind. Reference @Image1 for Pax hand skin tone, proportions, and tribal cloth detail.

Abrupt cut to:

Sub-shot C — 7 to 15 seconds, drone chase cam:
Wide 35mm drone chase-cam from slightly behind and above Jiggy, a small jade-green cyclops Pax creature with one single central round eye with purple iris, purple tribal headband with embroidered patterns, dreadlock hair, pink crystal pendant on a leather strap across the chest, tribal cloth wrap around waist, pointed elf-like ears. Jiggy runs forward energetically down a Pax cave tunnel, then bursts into a vast cathedral-scale underground cavern with floating crystal islands, giant magenta-rose crystal pillars rising hundreds of meters, and jade-amber organic formations. The camera tracks continuously behind and above, keeping Jiggy centered while he weaves left and right to dodge crystal columns, jumps over a fallen crystal log obstacle, and glances briefly over his shoulder once mid-run with a playful expression. Foreground crystal pillars whip past both sides of the frame with strong parallax and motion blur. The chase ends with the camera following Jiggy as he passes behind a tall magenta crystal column that fills the frame with its intense bioluminescent glow. Reference @Image3 for the cathedral environment palette and crystal pillar style.

Camera summary: sub-shot A is a continuous macro pull-back. Sub-shot B is a static tight push with a flare. Sub-shot C is a continuous drone chase tracking shot, no internal cuts within sub-shot C, smooth physically plausible motion with side-to-side sway following the runner.

Transitions: between A and B use a soft lens switch within continuous action of the gem reveal. Between B and C use an abrupt hard cut. Single hard cut only between B and C, no crossfade, no slow dissolve, no extra cuts within any sub-shot.

Lighting: sub-shot A is gem-as-key-light, chiaroscuro deep black void, magenta-rose. Sub-shot B is gem-flare drop moment, intense magenta-white bloom flooding the frame. Sub-shot C is mixed jade-amber ambient with magenta crystal rim accents, motion blur on peripheral walls and pillars.

Style: painterly stylized 3D animation, smooth shading, soft subsurface scattering on jade skin and crystals, cinematic warm-magenta lighting, magic-realism, jewel-like crystal detail, action-adventure energy. Pixar-quality NOT named. Identity lock: Jiggy always has one single central round eye, never two, jade-green skin tones, stylized stocky Pax proportions. Consistent character identity across all shots in which Jiggy appears.

Audio: sub-shot A opens with a single soft crystal bell tone with shimmer reverb, evolving into ambient drone with low rumble as the pull-back reveals context. Sub-shot B includes a quick rising tension swell ending in a sharp magical impact-flare hit. Sub-shot C is energetic percussive beat with deep sub-bass and rhythmic crystal chime cluster, fast-paced and physically dynamic, with subtle whoosh-bys on foreground parallax pillars. Dual-channel stereo with depth panning matching camera position.

Constraints: no text, no logos, no watermarks, no on-screen captions, no second eye on Jiggy, no realistic photography style, single hard cut only between sub-shot B and sub-shot C, no extra cuts, no crossfades. Aspect ratio 16:9, resolution 1280×720, duration exactly 15 seconds.

References: Reference @Image1 for Jiggy character identity, facial structure, accessories, and skin tone — keep facial proportions identical across all frames Jiggy appears in. Reference @Image2 for opening macro gem composition and rose-magenta crystal palette. Reference @Image3 for cathedral cave environment style and crystal pillar design. Keep visual style consistent across all 15 seconds.
```

# Prompt 9:16 (mobile variant)

Identical al prompt 16:9, con estos cambios al final:

```
Constraints (override): Aspect ratio 9:16, resolution 720×1280, duration exactly 15 seconds.

Composition adjustments for 9:16:
- Sub-shot A: gem centered, vertical bloom emphasis, pedestal reveal in lower portion of frame.
- Sub-shot B: hand enters from bottom-right corner, gem in upper-center, flare expanding vertically.
- Sub-shot C: drone chase emphasizes vertical depth ahead, tunnel and pillars stretch upward, Jiggy in lower-third of frame, foreground crystals frame the sides closer to the center.
- Final column eclipse: column rises vertically filling frame from bottom to top, Jiggy disappearing on the left edge.
```

Refs swap a `_9x16.png` variants en `@Image2`, `@Image3`. `@Image1` (Jiggy_Character.png) sirve para ambos ratios.

# Audio nativo (incluido en generacion, removido al servir web)

Mismo planteo que Video 1: generar con audio dual-channel para reuso en redes; al servir hero web extraer track sin audio.

```bash
# Phase 3 conversion (orquestador, no aqui)
ffmpeg -i video2-gem-chase_16x9_master.mp4 -an -c:v libvpx-vp9 -crf 32 -b:v 2M video2-gem-chase_16x9_web.webm
ffmpeg -i video2-gem-chase_16x9_master.mp4 -an -c:v libx264 -crf 23 -preset slow video2-gem-chase_16x9_web.mp4
```

# Fallback strategy si Seedance colapsa multi-shot a 15s

Si el modelo no sostiene los 3 sub-shots en una sola generacion (riesgo medio dado que multi-shot mejoro en 2.0 pero sigue siendo el caso mas dificil):

**Plan B — 3 clips separados encadenados en post**:

- **Clip A (0-5s, single shot)**: macro gem + pull back. Sin lens switch. Prompt corto, identidad pura.
- **Clip B (0-3s, single shot)**: hand entry + grab + flare. Termina en flash blanco saturado.
- **Clip C (0-7s, single shot)**: drone chase cam con Jiggy desde el principio (asumir continuidad post-flash). Empieza con magenta flash residual.

Editado en post (DaVinci/Premiere) con cortes en flash blanco (frame 5 → frame 0 de B y frame final de B → frame 0 de C usan el flash como camuflaje del corte).

**Plan C — 2 clips de 7.5s** si plan B sigue rompiendo identity lock de Jiggy:
- Clip 1 (0-7.5s): macro gem + Jiggy hand grab + flare + cut to start of chase.
- Clip 2 (0-7.5s): chase cam Jiggy hasta el column eclipse + loop seam.

# QA antes de deploy

- [ ] Identity lock Jiggy verificado en cada frame que aparece: 1 ojo central, jade skin, headband morado, dreadlocks, pendiente cristal rosa, taparrabos tribal.
- [ ] Abrupt cut entre sub-shot B y C realmente abrupto (sin crossfade).
- [ ] Flare blanco-magenta del sub-shot B no se "come" la cara de Jiggy.
- [ ] Loop seam invisible (ultimo frame magenta-white core matchea frame 0 macro gem, crossfade 8-15 frames en post).
- [ ] Sin texto en pantalla, sin logos, sin watermarks.
- [ ] File size <5 MB WebM, <8 MB MP4.
- [ ] Variante 9:16 verificada para mobile (Jiggy visible y reconocible en frame vertical).
- [ ] Test cross-browser autoplay muted.
- [ ] Respect `prefers-reduced-motion`: fallback a Frame 16 hero portrait estatico.
- [ ] Copyright check: prompt NO menciona Pixar / Disney / Subway Surfers / Sonic — solo descripciones generic-style.

# Notas director — riesgos especificos Video 2

1. **Mayor riesgo: drift de Jiggy entre sub-shot B y sub-shot C.** El abrupt cut hace que Seedance regenere la escena C casi de cero. Mitigacion: en el prompt, repetir la descripcion completa de Jiggy en la seccion de sub-shot C, y referenciar `@Image1` (char sheet final) en ambos.
2. **Riesgo medio: multi-shot a 15s con 3 sub-shots colapsa.** Si el primer intento muestra coherencia floja, ir a Plan B (3 clips separados).
3. **Riesgo bajo: aspect 9:16 pierde detalle de chase periferico.** Acceptable — diseñar 9:16 con foco vertical en Jiggy + pillar.
4. **Riesgo bajo: audio nativo genera sonido inapropiado** (musica licenciada accidental). Mitigacion: prompt explicito describe SFX y ambient, no menciona generos musicales con copyright.
