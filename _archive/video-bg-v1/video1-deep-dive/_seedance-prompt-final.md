---
title: "Video 1 — Seedance 2 Pro prompt final (deep dive into Pax world)"
duration: "15 seconds, single continuous shot"
provider_recommended: "fal.ai or Replicate, model `seedance-2-pro`"
aspect_ratios: "16:9 (1280×720) primary + 9:16 (720×1280) secondary"
date: 2026-05-18
director: pax-seedance-director
---

# Estrategia de generacion

- **Modelo**: Seedance 2 Pro (1080p, 15s, native audio).
- **Una sola toma continua**. Sin `lens switch`, sin `abrupt cut`. La narrativa va dirigida por la paleta y por la profundidad del descenso, no por cortes.
- **2 generaciones** (16:9 y 9:16) con el MISMO prompt base — variar solo la frase de aspect/composition lock al final.
- **Refs pasadas a Seedance**: las imagenes claves generadas por el script Python en Phase 2, especificamente Frame 0 (hero hook), Frame 9 (Pax world wide reveal), Frame 16 (loop seam). Tres refs maximo para identity-locking de paleta y composition.

# Paths esperados de refs (Phase 2 generara estos)

Los siguientes paths absolutos seran usados como `@Image1`, `@Image2`, `@Image3` en el prompt Seedance una vez Phase 2 genere las imagenes. **Aun no existen** — el script Python los creara.

- `@Image1`: `C:/Users/aldot/.gemini/antigravity/scratch/pax-os/content/video-bg/video1-deep-dive/img/frame-00-surface-dewdrop_16x9.png`
- `@Image2`: `C:/Users/aldot/.gemini/antigravity/scratch/pax-os/content/video-bg/video1-deep-dive/img/frame-09-pax-world-reveal_16x9.png`
- `@Image3`: `C:/Users/aldot/.gemini/antigravity/scratch/pax-os/content/video-bg/video1-deep-dive/img/frame-16-loop-seam_16x9.png`

Para la version 9:16, swap a las variantes `_9x16.png`.

# Prompt 16:9 (master)

```
A single continuous 15-second descent shot diving from the surface of Earth deep into an underground magical world.

Start (0-2s): extreme macro close-up of a single dew droplet hanging from a glossy green leaf at dawn, reflecting a miniature inverted sky. Cool cyan and rose pastel palette. Reference @Image1 for opening color and tone.

The camera then performs a continuous deep zoom in and dolly forward, plunging through the droplet's surface into a forest canopy. Sunlight god rays pierce diagonally through dense green leaves with strong volumetric atmosphere (2-3s).

The camera continues downward, descending past mossy forest floor with gnarled roots and tiny bioluminescent mushrooms, then plunges into a vertical natural opening in the earth (3-5s). Walls of dark soil and protruding roots rush past the edges of the frame with strong parallax motion blur.

The descent passes through horizontal geological strata: layers of amber, ocre, and deep red mineral rock with embedded glowing semiprecious stones (5-7s). Palette warms from green to amber.

The camera emerges into a vast natural cavern with stalactites and early veins of magenta-pink crystal in the walls, then brushes past a wall densely packed with bioluminescent crystal veins glowing rose-magenta (7-9s).

Emerging through a dark crystal-lined corridor, the camera reveals a vast underground magical world (9-11s). Reference @Image2 for world reveal palette: giant magenta crystal pillars, jade-amber organic formations, floating crystal islands suspended mid-air connected by glowing bridges, a still reflective lake on the floor.

The camera floats laterally past the islands toward a central glowing crystal altar (11-13s). Small jade-skinned cyclops creatures with one single central eye, dreadlock hair, and tribal cloth gather at its base — kept at distance, silhouettes more than detail.

The camera cranes up slightly and pulls back to reveal the epic scale (13-15s). Reference @Image3 for the final hero composition: community small in frame, world cathedral-scale around them, a single luminous bioluminescent particle floating prominently in the foreground glowing white-magenta.

Camera: single continuous shot, no cuts, no lens switching, no random angle changes. Smooth physically plausible motion. Strong forward and downward parallax during descent, lateral float during world exploration, gentle crane up for final reveal.

Lighting: continuous warm-cool palette transition. Cyan-rose dawn at surface; volumetric green-gold canopy rays; warm amber geological strata; magenta-rose crystal veins; mixed jade-amber-magenta world reveal with subtle bloom and atmosphere haze. Soft subsurface scattering on organic surfaces.

Style: painterly stylized 3D animation, cinematic warm lighting, magical realism, epic scale, smooth shading, jewel-like detail on crystals, atmospheric depth. Identity lock on Pax characters: each has one single central round eye, no second eye, jade-green skin, short stocky stylized proportions.

Audio: ambient drone with soft cyan wind and dripping water at surface (0-3s), evolving into deep low rumble and granular earth textures during descent (3-7s), then warm bell-tones and shimmer rising as the crystal world reveals (7-12s), culminating in a low sub-bass drop with bioluminescent chime cluster and gentle community vocal hum at the final reveal (12-15s). Dual-channel stereo with depth panning matching camera position.

Constraints: no text, no logos, no watermarks, no on-screen captions, no second eyes on Pax characters, no realistic photography style, no cuts, no crossfades, single continuous shot. Aspect ratio 16:9, resolution 1280×720, duration exactly 15 seconds.

References: Reference @Image1 for opening macro palette and detail level. Reference @Image2 for Pax world environment palette, crystal pillar style, and bioluminescent geology design. Reference @Image3 for final hero composition, scale relationship, and loop seam particle placement. Keep environment style consistent across all 15 seconds.
```

# Prompt 9:16 (mobile variant)

Identical al prompt 16:9, con estos cambios al final:

```
Constraints (override): Aspect ratio 9:16, resolution 720×1280, duration exactly 15 seconds.

Composition adjustments for 9:16:
- Opening macro frame: droplet centered in upper-third, leaf descending diagonally to lower-third.
- Descent phase: emphasize vertical motion, walls of tunnel hug both sides of frame tightly.
- Cavern reveal: vertical cathedral framing, stalactites stretched upward.
- Pax world reveal: stack crystal pillars vertically, central altar in lower-third, community at very bottom.
- Final hero: foreground bioluminescent particle in lower-center, world towering above filling upper two-thirds.
```

Refs swap a `_9x16.png` variants en `@Image1`, `@Image2`, `@Image3`.

# Audio nativo (incluido en generacion, removido al servir web)

Generacion con audio dual-channel para reuso en redes. Al servir como hero web background:

```bash
# Ejemplo conversion (lo hace el orquestador en Phase 3, no aqui)
ffmpeg -i video1-deep-dive_16x9_master.mp4 -an -c:v libvpx-vp9 -crf 32 -b:v 2M video1-deep-dive_16x9_web.webm
ffmpeg -i video1-deep-dive_16x9_master.mp4 -an -c:v libx264 -crf 23 -preset slow video1-deep-dive_16x9_web.mp4
```

# Fallback strategy si Seedance colapsa coherencia a 15s

Si el modelo no sostiene la transicion de paletas en una sola toma, plan B:

**3 clips encadenados** de 5s cada uno, con motion vector matching en bordes:

- **Clip A (0-5s)**: surface to forest floor to crack. Termina con descent vertical en plena aceleracion.
- **Clip B (5-10s)**: tunnel descent + geological strata + cavern emerging. Empieza con descent vertical, termina con camera saliendo de cristal corridor.
- **Clip C (10-15s)**: Pax world reveal + community + hero final. Empieza con threshold, termina con loop hero frame.

Editado en post con cortes camuflados (match-cut en motion vector). Cada clip generado con su propio prompt sintetizado del bloque master, manteniendo el mismo identity-lock y palette descriptors.

# QA antes de deploy

- [ ] Loop seam invisible (ultimos 8-15 frames crossfade hacia frame 0 en post).
- [ ] Color/exposicion estable en bordes del loop.
- [ ] Sin Pax con 2 ojos (identity lock fail = regenerar).
- [ ] Sin texto en pantalla, sin logos, sin watermarks.
- [ ] File size <5 MB para WebM, <8 MB para MP4 fallback.
- [ ] WebM + MP4 ambos exportados sin audio track.
- [ ] Variante 9:16 verificada para mobile.
- [ ] Test en Chrome, Safari, Firefox con autoplay muted.
- [ ] Respect `prefers-reduced-motion`: fallback a hero key-art frame 16 estatico.
