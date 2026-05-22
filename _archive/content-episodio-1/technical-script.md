# PAX — Episode 1: "The Notebook with the Crack"
## Technical Script — Seedance 2.0 Production Bible

> **Owner:** `pax-seedance-director`
> **Source narrative:** `script_ep01_v2.md` + `beat_sheet_ep01_v2.md`
> **Source lore:** `lore_v3.md`
> **Source visuals:** `character_sheet_visual.md`
> **Research base:** `research_seedance_2026.md` (hard rules: brand-name table, prompt template, continuity techniques, negative prompt block)
> **Render target:** Seedance 2.0 — 16:9 — 15 seconds per clip — stylized 3D animation
> **Date:** 2026-04-28

---

## HEADER — TOTALS

| Item | Count |
|---|---|
| Seedance narrative clips | **15** (B1, B2, B3, B4, B5, B6, B7, B8-A, B8-B, B9, B10, B11, B12, B13A, B14) |
| Seedance seed-clips (identity locks) | **3** (Seed-Jiggy, Seed-Wiz, Seed-Mariela) |
| **Total Seedance generations** | **18** |
| Post-production manual assets | **3** (B13B insert, handwritten overlay shared B6+B14, audio editorial) |
| Narrative duration (B1-B14) | **3:45** (15 narrative segments × 15s) |
| Production duration with seed-clips | **3:45 narrative + 0:45 seed-clip overhead = 4:30 generation** |

### Budget estimate (3 variations per clip, USD 1.50-2.00 per generation)

- 18 generations × 3 variations = **54 Seedance jobs**
- @ USD 1.50/job low end → **USD 81**
- @ USD 2.00/job high end → **USD 108**
- **Working budget: USD 81 — 108** (excluding re-generations for drift / flag failures; reserve 20% buffer → **USD 97 — 130 total**)

### Copyright status

- **Zero brand names in any prompt.** Replacement table from `research_seedance_2026.md` Eje 3 applied throughout (no "Pixar", "Ghibli", "Disney", "Marvel", "anime", "claymation", etc.).
- All clips flagged **Copyright risk: low**.

---

## CHARACTER SHEETS — LITERAL CONSTANTS (paste verbatim into prompts)

> **Hard rule (Eje 2.1 of research):** The 15-25 word literal char sheet must be repeated WORD-BY-WORD in every prompt where the character appears. Do not paraphrase between clips.

### `@Jiggy` (Pax chasqui-runner)
```
@Jiggy, a small cyclops underground-tribe character, single large central eye with turquoise iris and double specular highlight, smooth turquoise-green skin (#21D8B6), elastic pointed ears, four-fingered hands, brown-red leather chest harness with metal buckle, leather satchel at hip, no headwear, 3.5 head proportions, expressive curious face
```

### `@Wiz` (Pax custodio)
```
@Wiz, an elder cyclops underground-tribe character, single central eye with droopy upper lid, long voluminous white beard covering chest, bushy white eyebrows, deep purple hooded robe with subtle turquoise rune trim, circular violet-crystal medallion on chest, dark wood staff topped with magenta-violet crystal, four-fingered weathered hands, 2.8 head proportions, serene wise posture
```

### `@Byte` (Pax traductor)
```
@Byte, a young cyclops underground-tribe character, single central turquoise eye, smooth turquoise-green skin (#21D8B6), dark purple hoodie with lime-green neon trim, large over-ear neural headphones with bright lime-green LED rings, four-fingered hands, 3.5 head proportions, focused concentrated expression
```

### `@Luxa` (Pax calidez)
```
@Luxa, a slender cyclops underground-tribe character, single large central eye with cyan-turquoise iris and gentle lashes, faint luminous turquoise-green skin (#21D8B6), purple headband tied behind with hanging ends, multicolor tribal-patterned poncho with purple gold turquoise magenta geometry, woven shoulder satchel, beaded wrist and ankle bracelets, four-fingered hands, 3.5 head proportions, warm open expression
```

### `@Zek` (Pax pulso)
```
@Zek, a cyclops underground-tribe character, single central turquoise eye, smooth turquoise-green skin (#21D8B6), purple cap tilted sideways, purple t-shirt with tribal logo, magenta-violet crystal pendant on tribal cord, retro analog boombox at hip, four-fingered hands, 3.5 head proportions, playful relaxed expression
```

### `@Mariela` (human protagonist)
```
@Mariela, a 36-year-old Latin-American woman, brown hair pulled back in a low ponytail, light office blouse, thin metal-framed glasses, no makeup, calm tired competent expression, naturalistic skin tones, stylized human proportions matched to 3D animation style of the Pax universe (slightly softened features, not photoreal)
```

### Style block — CONSTANT (copy verbatim every clip)
```
Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.
```

### Negative block — CONSTANT (copy verbatim every clip)
```
Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic human proportions for Pax characters, no extra limbs, no distorted faces, no fast motion.
```

---

## SUMMARY TABLE — 15 NARRATIVE CLIPS

| # | Time | Title | Characters | Camera | Audio | Risk |
|---|---|---|---|---|---|---|
| B1 | 0:00-0:15 | Cold open — dying spark | none on-screen (Pax silhouette far back) | slow dolly-down toward crystal | low arrhythmic pulse, granular cave reverb | low |
| B2 | 0:15-0:30 | The waiting (3 silhouettes) | @Wiz, @Byte, @Zek (silhouettes) | static wide reverse | sustained low cello, pulse softer | medium (3 figures, but silhouetted) |
| B3 | 0:30-0:45 | Office — Mariela introduced | @Mariela, coworker (background) | slow pan right | distant copier, AC hum, dialogue | low |
| B4 | 0:45-1:00 | Metro — the notebook | @Mariela | static + subtle handheld sway | metro rumble, faint pulse, single piano note | low |
| B5 | 1:00-1:15 | Kitchen — kettle, pause | @Mariela | slow dolly-in | kettle hum, soft pulse, piano holds | low |
| B6 | 1:15-1:45 | Writing the question (30s = SPLIT in template? See note) | @Mariela | tight ECU + subtle push | high cyan chime, heartbeat sync | medium (text legibility) |
| B7 | 1:45-2:00 | Byte detects | @Wiz, @Byte | static medium | headphone ping, staff ring on stone | medium (2 figures) |
| B8-A | 2:00-2:03 | Mariela's hand grips pencil | @Mariela (hand only) | static extreme close-up | total quiet, paper pressure crackle | low |
| B8-B | 2:03-2:15 | Wiz's palm — crystal forms | @Wiz (palm + eye in BG) | static extreme close-up | 1 frame silence, then crystal-formation cooling-glass sound | medium (formation timing critical) |
| B9 | 2:15-2:30 | Relay handoff (3 figures) | @Wiz, @Jiggy, @Luxa | static medium | quiet score, breath, footsteps | **high** (3 Pax in one plate) |
| B10 | 2:30-2:45 | Storm-drain + drone drift | @Jiggy, @Zek (background) | tight follow then static | drone hum mechanical, sub-tone shift, boombox pulse | medium (2 figures + 2 drones, drift behavior) |
| B11 | 2:45-3:00 | Kitchen — Jiggy delivers warmth | @Jiggy, @Mariela | slow dolly-in | clock tick, neighbor TV, faint crystal-sound memory | **high** (dual-palette + 2 chars, paste-in risk) |
| B12 | 3:00-3:15 | "...okay." | @Mariela | static medium | kettle hum, sustained warm major chord, single line | low |
| B13A | 3:15-3:30 | Wiz silhouette + Jiggy returns | @Wiz, @Jiggy | slow dolly-down along Wiz back | warm score swell, near-normal heartbeat, dialogue | medium (must EXCLUDE pocket/2nd crystal) |
| B14 | 3:30-3:45 | Cliffhanger — glowing notebook | none (props only) | slow dolly-in on notebook | single low cello, synced pulse, fade to silence | medium (text legibility — post-pro overlay) |

> **Note on B6 (30s):** Seedance native unit is 15s. B6 is staged as a **single 15s clip** that covers only the writing+chime+heartbeat-sync moment. The full 30s of script time is achieved by holding the previous beat (B5) lighter and letting the editor pace B6 with audio + the placeholder writing motion. The handwritten line is a **post-pro overlay** (not Seedance-rendered). See ASSETS NO-SEEDANCE.

---

# SEED-CLIPS PRELIMINARES (3)

> **Why these exist:** Per `research_seedance_2026.md` HALLAZGO 2.2 — generate one identity-lock seed clip per recurring character BEFORE narrative clips. Save the seed number. Reuse in every clip where the character appears. Without these, drift is guaranteed by clip 4-5.

---

## SEED-JIGGY — 15s — neutral 360 turn

### Prompt Seedance (English, copy-paste ready)

```
@Jiggy, a small cyclops underground-tribe character, single large central eye with turquoise iris and double specular highlight, smooth turquoise-green skin (#21D8B6), elastic pointed ears, four-fingered hands, brown-red leather chest harness with metal buckle, leather satchel at hip, no headwear, 3.5 head proportions, expressive curious face.

Action: @Jiggy stands in idle neutral pose at scene center. For the first 8 seconds: he slowly rotates 180 degrees to his right at controlled pace, expression neutral, arms relaxed. Then for the final 7 seconds: he completes the 360 turn back to facing camera, holds neutral idle.

Camera: static shot, locked tripod, framed full body medium-wide, no camera movement, no shake.

Setting: completely neutral seamless studio backdrop in soft mid-gray (#888888), empty floor, no props, no environment.

Lighting: flat three-point neutral studio lighting, soft key from upper-front, gentle fill from camera-right, soft rim from above-back, no colored gels, no atmospheric effects.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic human proportions for Pax characters, no extra limbs, no distorted faces, no fast motion, no environment, no props, no colored lighting, no expression changes.
```

### Negative prompt
(included in prompt above — neutral identity baseline)

### Camera & motion
- Start: full-body medium-wide, character facing camera
- During 15s: 360-degree rotation in place
- End: same pose facing camera

### Audio
- **Music cue:** none (silent reference clip)
- **SFX:** silent
- **Dialogue:** none

### Continuity anchors
- Previous clip: N/A (this is reference baseline)
- This clip: defines the canonical identity of @Jiggy
- Element to persist: every visual detail of the char sheet — to be reused as keyframe injection slot 1 in every Jiggy narrative clip

### Risk flags
- Copyright risk: low
- Continuity risk: this IS the continuity source
- Generation risk: low — neutral pose, single character, no environment

### Fallback if Seedance fails
- Re-prompt with simpler turn (just 180 degrees, not 360)
- Worst case: generate 4 still-frame portraits (front / right profile / 3/4 / back) and stitch in editor as a slow morph

---

## SEED-WIZ — 15s — neutral 360 turn

### Prompt Seedance (English, copy-paste ready)

```
@Wiz, an elder cyclops underground-tribe character, single central eye with droopy upper lid, long voluminous white beard covering chest, bushy white eyebrows, deep purple hooded robe with subtle turquoise rune trim, circular violet-crystal medallion on chest, dark wood staff topped with magenta-violet crystal, four-fingered weathered hands, 2.8 head proportions, serene wise posture.

Action: @Wiz stands at scene center leaning slightly on his staff in idle neutral pose. For the first 8 seconds: he slowly rotates 180 degrees to his right at controlled pace, expression serene neutral. Then for the final 7 seconds: he completes the 360 turn back to facing camera, holds neutral idle, staff vertical.

Camera: static shot, locked tripod, framed full body medium-wide, no camera movement, no shake.

Setting: completely neutral seamless studio backdrop in soft mid-gray (#888888), empty floor, no props beyond his own staff, no environment.

Lighting: flat three-point neutral studio lighting, soft key from upper-front, gentle fill from camera-right, soft rim from above-back, no colored gels, no atmospheric effects, the medallion crystal and staff crystal at low ambient glow only.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic human proportions for Pax characters, no extra limbs, no distorted faces, no fast motion, no environment beyond gray backdrop, no colored lighting, no expression changes, no glowing emissive overload on crystals.
```

### Camera & motion
- Static medium-wide. 360 rotation in place.

### Audio
- Silent reference clip.

### Continuity anchors
- Defines canonical @Wiz identity. Reused in B2, B7, B8-B, B9, B13A.

### Risk flags
- Copyright risk: low
- Continuity risk: source-of-truth
- Generation risk: low-medium — staff + medallion are extra geometry, watch for crystal-glow over-bloom

### Fallback if Seedance fails
- Drop the staff in a second iteration (he holds it static at his side, no motion)
- Or generate 180-degree turn only and mirror in editor

---

## SEED-MARIELA — 15s — neutral 360 turn

### Prompt Seedance (English, copy-paste ready)

```
@Mariela, a 36-year-old Latin-American woman, brown hair pulled back in a low ponytail, light office blouse, thin metal-framed glasses, no makeup, calm tired competent expression, naturalistic skin tones, stylized human proportions matched to 3D animation style of the Pax universe (slightly softened features, not photoreal).

Action: @Mariela stands at scene center in idle neutral pose, hands at sides. For the first 8 seconds: she slowly rotates 180 degrees to her right at controlled pace, expression neutral. Then for the final 7 seconds: she completes the 360 turn back to facing camera, holds neutral idle.

Camera: static shot, locked tripod, framed full body medium-wide, no camera movement, no shake.

Setting: completely neutral seamless studio backdrop in soft mid-gray (#888888), empty floor, no props, no environment.

Lighting: flat three-point neutral studio lighting, soft key from upper-front, gentle fill from camera-right, soft rim from above-back, no colored gels, no atmospheric effects.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic photoreal human face, no extra limbs, no distorted faces, no fast motion, no environment, no props, no colored lighting, no expression changes, no makeup, no jewelry.
```

### Camera & motion
- Static medium-wide. 360 rotation in place.

### Audio
- Silent reference clip.

### Continuity anchors
- Defines canonical @Mariela identity. Reused in B3, B4, B5, B6, B8-A, B11, B12.

### Risk flags
- Copyright risk: low (Mariela is fictional; do NOT use any actor's name)
- Continuity risk: source-of-truth
- Generation risk: medium — human face stylized but not photoreal is the hardest balance for Seedance. Generate 5 variations and pick the one that lands closest to "stylized human within Pax 3D world".

### Fallback if Seedance fails
- Re-prompt with explicit "matched to soft-shaded 3D animation style, not photoreal, slightly larger eyes than realistic, simplified facial geometry"
- Worst case: 4 still portraits front/profiles + slow morph in editor

---

# NARRATIVE CLIPS (15)

---

## Clip B1 — 0:00-0:15 — Cold open: the dying spark

### Prompt Seedance (English, copy-paste ready)

```
A single small fist-sized magenta-violet crystal embedded low on a stalagmite, pulsing very faintly like a slowed heartbeat about to stop. The cavern around it is pitch dark except for one thin sliver of bioluminescent ambient light catching slow vertical lines of falling dust. Hundreds of empty stalagmites that should hold sparks fade into deep shadow. One distant Pax silhouette stands very still far in the back, motionless, not approaching.

Action: For the full 15 seconds, the camera drifts slowly downward through the dust toward the dying crystal, settling at extreme close-up at the end. The crystal pulse is barely alive, dimming and brightening once across the full duration. Dust drifts down at constant slow pace.

Camera: gentle slow dolly-down from wide cavern view to extreme close-up of the crystal over 15 seconds, locked horizon, no shake, no zoom.

Setting: vast underground cavern Uray Pacha, organic-mineral floor with crystalline outcroppings, a single thin shaft of cold ambient bioluminescence, deep purple-black walls.

Lighting: near-darkness, single weak emissive from the crystal itself in dim magenta (#E83FC8 at low intensity), one cold pale-cyan ambient sliver from above, no fill, deep volumetric haze with slow falling dust motes.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic human proportions for Pax characters, no extra limbs, no distorted faces, no fast motion, no characters facing camera, no bright lighting, no warm gold glow.
```

### Camera & motion
- Start frame: wide cavern, crystal small in lower-third
- Motion: slow dolly-down 15 seconds
- End frame: extreme close-up of pulsing crystal

### Audio
- **Music cue:** none (no music yet)
- **SFX:** soft low arrhythmic pulse, granular distant cave reverb, dust-falling whisper
- **Dialogue:** none

### Continuity anchors
- Previous clip: N/A (opening)
- This clip ends with: extreme close-up of crystal at low pulse — establishes the canonical pulse rhythm to be mirrored in B14
- Element MUST persist into next clip: cool magenta + cool turquoise palette, near-darkness, the slow pulse

### Risk flags
- Copyright risk: low
- Continuity risk: this clip SETS the continuity for the entire cavern look
- Generation risk: low — minimal subject, no character ID

### Fallback if Seedance fails
- Re-prompt with even simpler scene: just the crystal + dust, no distant silhouette
- Use a still-image render and animate camera move + dust + crystal pulse in After Effects

---

## Clip B2 — 0:15-0:30 — The waiting (3 silhouettes)

### Prompt Seedance (English, copy-paste ready)

```
@Wiz, an elder cyclops underground-tribe character, single central eye with droopy upper lid, long voluminous white beard covering chest, bushy white eyebrows, deep purple hooded robe with subtle turquoise rune trim, circular violet-crystal medallion on chest, dark wood staff topped with magenta-violet crystal, four-fingered weathered hands, 2.8 head proportions, serene wise posture, in foreground silhouette leaning on his staff.

Behind @Wiz, two more Pax silhouettes far back: @Byte, a young cyclops underground-tribe character with large over-ear neural headphones with bright lime-green LED rings (only the LED glow visible in silhouette); and @Zek, a cyclops underground-tribe character with purple cap tilted sideways (only the cap brim catching one tiny edge of light).

Action: For the full 15 seconds, all three figures are nearly still. @Wiz looks at the dying crystal off-frame lower-left, then very slowly tilts his head upward toward a thin crack in the cavern ceiling barely visible. After 10 seconds he lowers his head one inch. Byte and Zek do not move at all.

Camera: static wide reverse shot, locked tripod, no movement, no zoom.

Setting: same vast cavern Uray Pacha as previous clip, the three figures positioned in the depth of the cavern, dust still drifting down in vertical lines, hairline crack in cavern ceiling visible high frame-left.

Lighting: near-darkness as before, magenta crystal off-frame casts faint rim on Wiz's silhouette, lime-green LED glow from Byte's headphones is the only secondary emissive, deep cold ambient.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic human proportions for Pax characters, no extra limbs, no distorted faces, no fast motion, no four characters, no Luxa in frame, no warm gold glow, no facial detail visible on silhouettes beyond LED and cap brim.
```

### Camera & motion
- Static wide reverse, locked.

### Audio
- **Music cue:** sustained low cello note, mournful but not heavy, enters at second 2 and holds
- **SFX:** same pulse from B1, softer
- **Dialogue:** none

### Continuity anchors
- Previous clip: B1 ended on extreme close-up of dying crystal at low pulse
- This clip starts with: hard-left of the same crystal off-frame, the figures revealed behind
- Element MUST persist: cool magenta + turquoise palette, dust motes, the low pulse rhythm

### Risk flags
- Copyright risk: low
- Continuity risk: low — silhouettes do not require facial ID, but the LED + cap-brim identifiers must read
- Generation risk: medium — three figures in same plate, but silhouetted reduces drift risk

### Fallback if Seedance fails
- Split into 2 micro-shots: (a) Wiz silhouette in foreground only, 10s; (b) reverse with Byte and Zek silhouettes, 5s. Cut between in editor.
- If LED glow is missing on Byte: composite a small lime emissive in After Effects over the ear position.

---

## Clip B3 — 0:30-0:45 — Office: Mariela introduced

### Prompt Seedance (English, copy-paste ready)

```
@Mariela, a 36-year-old Latin-American woman, brown hair pulled back in a low ponytail, light office blouse, thin metal-framed glasses, no makeup, calm tired competent expression, naturalistic skin tones, stylized human proportions matched to 3D animation style of the Pax universe (slightly softened features, not photoreal). She sits in front of a computer screen showing a spreadsheet with pivot tables, cells highlighted yellow and red. A mug of cold coffee and a small framed photo of a young niece are on her desk.

Action: For the first 8 seconds: @Mariela works on the spreadsheet, vacant competent face. A coworker (background, mid-30s, generic office attire, soft focus) walks past camera-left to camera-right and drops a folder on her desk without stopping. Then for the final 7 seconds: @Mariela closes the spreadsheet with a click, opens another, the wall clock visible behind her reads 6:47 PM.

Camera: gentle slow pan right across the office cubicles starting on Mariela and ending on her workstation tighter, over 15 seconds, locked horizon, no shake.

Setting: small open-plan office in Providencia Santiago, nine cubicles, fluorescent overhead lighting, beige walls, plants on shelves, a wall clock visible reading 6:47 PM, distant copier visible in background blur.

Lighting: clinical fluorescent overhead key, neutral cool white, soft fill, very mild ambient — clinical not warm, no magenta, no turquoise.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic photoreal face, no extra limbs, no distorted faces, no fast motion, no magenta lighting, no fantasy elements, no Pax characters in frame, no readable text on monitor.
```

### Camera & motion
- Slow pan right.

### Audio
- **Music cue:** the cello from B2 has faded; we are in a different sound-world
- **SFX:** distant copier, AC hum, ambient office chatter very low
- **Dialogue:**
  - COWORKER (barely looking up): "Thanks, Mari." — voice direction: distracted, transactional
  - MARIELA (without looking back): "Sure." — voice direction: flat, automatic

### Continuity anchors
- Previous clip: B2 ended on cold cavern silhouettes
- This clip starts with: hard cut to bright fluorescent — total tonal break
- Element MUST persist into B4: Mariela's identity baseline (hair, blouse, glasses)

### Risk flags
- Copyright risk: low
- Continuity risk: medium — Mariela's face must match seed-clip and persist across all her clips
- Generation risk: medium — lipsync on two short lines; keep both off-camera-mouth if possible (line "Sure" with her not looking, line "Thanks Mari" with coworker walking past)

### Fallback if Seedance fails
- If lipsync fails: re-frame Mariela's "Sure" with her looking down at screen, mouth not visible. Audio added in post.
- If coworker drift: shoot coworker as silhouette walking through.

---

## Clip B4 — 0:45-1:00 — Metro: the notebook

### Prompt Seedance (English, copy-paste ready)

```
@Mariela, a 36-year-old Latin-American woman, brown hair pulled back in a low ponytail, light office blouse, thin metal-framed glasses, no makeup, calm tired competent expression, naturalistic skin tones, stylized human proportions matched to 3D animation style of the Pax universe (slightly softened features, not photoreal). She stands holding a metal grab-strap on a crowded urban metro car. The car is full of indistinct silhouetted commuters around her, but the camera frames her alone in soft isolation.

Action: For the first 6 seconds: @Mariela glances at her phone, sees a notification, dismisses it without engaging. Then for the final 9 seconds: she reaches into her shoulder bag and pulls out a small A6 brown leather-bound notebook with a faded elastic band and a thin crack running along the spine. She thumbs back to the last written entry — a page dated six months ago in her own handwriting, three short lines of mundane to-do reminders. She stares at it one second too long, closes the notebook, places it back into the bag without writing.

Camera: static medium close-up framing on Mariela centered, with very subtle handheld sway suggesting metro motion, over 15 seconds, no zoom.

Setting: interior of Santiago Metro Line 5 car, evening, cool fluorescent ceiling lighting, blurred urban motion through windows, indistinct silhouetted passengers in soft focus, metal grab-straps and rails.

Lighting: cool fluorescent overhead, slight blue-shift from passing exterior city lights through windows, neutral fill on Mariela's face, no warm color, no magenta.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic photoreal face, no extra limbs, no distorted faces, no fast motion, no readable text on phone screen, no readable text in notebook, no readable signage.
```

### Camera & motion
- Static medium close-up + subtle handheld sway.

### Audio
- **Music cue:** single low piano note enters at second 9 when she opens the notebook
- **SFX:** metro rumble, faint pulse from B1 returns when camera frames the notebook (only when on the notebook)
- **Dialogue:** none

### Continuity anchors
- Previous clip: B3 ended on Mariela closing/opening spreadsheets at 6:47 PM
- This clip starts with: she's now on the metro home, same outfit, same hair
- Element MUST persist into B5: the notebook (A6, brown, faded elastic, cracked spine) — this is the canonical hero prop, do not let Seedance change its proportions or material

### Risk flags
- Copyright risk: low
- Continuity risk: medium — notebook must look identical in B4, B5, B6, B11, B14
- Generation risk: low-medium — handwritten text on the page is post-pro overlay; the text in this clip (the 6-month-old entry) is also overlay if Seedance generates garbled letters

### Fallback if Seedance fails
- The 6-month-old entry text can also be a post-pro overlay using the same hand-style asset family as the B6/B14 overlay
- If notebook proportions drift: prompt next clip with explicit "same notebook from previous clip, A6 brown leather, faded elastic, cracked spine"

---

## Clip B5 — 1:00-1:15 — Kitchen, kettle, pause

### Prompt Seedance (English, copy-paste ready)

```
@Mariela, a 36-year-old Latin-American woman, brown hair pulled back in a low ponytail, light office blouse, thin metal-framed glasses, no makeup, calm tired competent expression, naturalistic skin tones, stylized human proportions matched to 3D animation style of the Pax universe (slightly softened features, not photoreal). She stands in a small Santiago apartment kitchen with tiled floor, a single hanging tungsten bulb, a window showing the city at dusk with the Andes silhouette barely visible behind smog-pink sky.

Action: For the first 5 seconds: @Mariela places a kettle on the stove and stands without moving. For the next 5 seconds: she catches her own reflection in the window glass and holds it. Then for the final 5 seconds: she reaches into her shoulder bag, takes out the same A6 brown leather notebook with faded elastic and cracked spine, sets it on the small kitchen table, picks up a pencil from a jar, sits down at the table.

Camera: gentle slow dolly-in from medium-wide to medium close-up over 15 seconds, locked horizon, no shake.

Setting: small Santiago apartment kitchen, tiled floor in muted earth tones, single hanging tungsten bulb at 3000K, kettle on stove, small wooden table, pencil jar with three pencils, window with dusk view of Andes mountains and pink-smog Santiago sky in background.

Lighting: warm tungsten hanging bulb (#FFD08A 3000K) as primary key, cool dusk window light from camera-left as fill, soft gentle volumetric haze, no magenta or turquoise yet.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic photoreal face, no extra limbs, no distorted faces, no fast motion, no Pax characters in frame, no fantasy lighting.
```

### Camera & motion
- Slow dolly-in.

### Audio
- **Music cue:** piano holds from B4
- **SFX:** kettle hum starts at second 4, soft pulse from B1 very faint underneath
- **Dialogue:** none

### Continuity anchors
- Previous clip: B4 ended on Mariela returning the notebook to her bag in the metro
- This clip starts with: she's now home, same outfit, same hair, same notebook still in bag
- Element MUST persist into B6: the kitchen geometry (table, hanging bulb, window), the notebook on the table, the pencil in her hand

### Risk flags
- Copyright risk: low
- Continuity risk: medium — kitchen layout must persist into B6 / B11 / B12 / B14
- Generation risk: low — slow contemplative shot, single character, simple action

### Fallback if Seedance fails
- If reflection in window fails: drop the reflection beat, just have her stand, then go to the bag
- Re-prompt with simpler "single hanging bulb, table, kettle, window with dusk view" if environment morphs

---

## Clip B6 — 1:15-1:45 — Writing the question (15s Seedance + held in edit)

### Prompt Seedance (English, copy-paste ready)

```
@Mariela, a 36-year-old Latin-American woman, brown hair pulled back in a low ponytail, light office blouse, thin metal-framed glasses, no makeup, calm tired competent expression with subtle hesitation, naturalistic skin tones, stylized human proportions matched to 3D animation style of the Pax universe (slightly softened features, not photoreal). Tight on her hand holding a wooden pencil over an open A6 brown leather notebook with faded elastic and a thin crack along the spine, on the small kitchen table.

Action: For the first 6 seconds: @Mariela's hand holds the pencil over the blank page after the older 6-month entry, hesitating, the pencil tip not yet touching the page. Then for the final 9 seconds: she lowers the pencil and writes slowly with the unsteady hand of someone out of practice — placeholder cursive squiggles in soft graphite (real text will be added in post-production overlay), then lifts the pencil, stares at the line, does not write more. The kettle clicks off in the background — she does not react. The crack along the notebook spine emits, for less than half a second around the 12-second mark, a thin soft cyan glow then fades — almost imperceptible.

Camera: tight extreme close-up over the notebook page and her hand, with very subtle slow push-in toward the page over 15 seconds, locked horizon, no shake, no zoom.

Setting: same small Santiago apartment kitchen, same table, same notebook, same pencil. Background out-of-focus showing kitchen elements.

Lighting: warm tungsten hanging bulb (#FFD08A 3000K) as primary key from upper-right, cool dusk window fill from camera-left at low intensity, the brief cyan glow on the spine is a soft pale-cyan emissive at very low intensity, lasts under 0.5 seconds total.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic photoreal face, no extra limbs, no distorted faces, no fast motion, no readable English text on the page (placeholder squiggles only — real text added in post), no bright cyan flash, no obvious magic effect, no glowing portal, no Pax characters in frame, no fantasy aesthetic.
```

### Camera & motion
- Tight ECU + subtle slow push-in.

### Audio
- **Music cue:** piano from B5 holds, very low
- **SFX:** the cave pulse from B1 momentarily synchronizes with her heartbeat then fades; a single high cyan-toned chime — the kind dismissable as a neighbor's pot falling — at second 12 when the spine glows
- **Dialogue:** none

### Continuity anchors
- Previous clip: B5 ended with her sitting at table with pencil in hand, notebook on table
- This clip starts with: same hand position, same pencil, same notebook
- Element MUST persist into B7 (cut to Uray Pacha): the audio pulse — Byte detects the pressing-pencil moment in the next clip
- **Critical post-pro element:** the handwritten line "Why did I stop writing here?" must appear on the page as a POST-PRO OVERLAY (After Effects / DaVinci) on top of the placeholder squiggles. Same overlay asset reused in B14. See ASSETS NO-SEEDANCE below.

### Risk flags
- Copyright risk: low
- Continuity risk: high — the post-pro overlay text must be IDENTICAL in B6 and B14
- Generation risk: medium — Seedance is unreliable with handwritten English text legibility; we explicitly prompt placeholder squiggles. The brief cyan glow on the spine may be over-rendered — keep prompt language at "for less than half a second" and "almost imperceptible"

### Fallback if Seedance fails
- If cyan glow over-renders: composite a masked cyan emissive in After Effects over the spine for ~12 frames, exclude the Seedance glow
- If handwriting motion looks wrong: cover the actual writing with the overlay asset; only the hand motion needs to read

---

## Clip B7 — 1:45-2:00 — Byte detects

### Prompt Seedance (English, copy-paste ready)

```
@Byte, a young cyclops underground-tribe character, single central turquoise eye, smooth turquoise-green skin (#21D8B6), dark purple hoodie with lime-green neon trim, large over-ear neural headphones with bright lime-green LED rings, four-fingered hands, 3.5 head proportions, focused concentrated expression. Beside him, @Wiz, an elder cyclops underground-tribe character, single central eye with droopy upper lid, long voluminous white beard covering chest, bushy white eyebrows, deep purple hooded robe with subtle turquoise rune trim, circular violet-crystal medallion on chest, dark wood staff topped with magenta-violet crystal.

Action: For the first 5 seconds: @Byte stands still, his elastic pointed ears twitch once subtly, his lime-green LED headphones pulse a single ping of brighter green light, then he places two fingers on the side of one earcup. Then for the next 5 seconds: his single turquoise eye widens, he turns his head toward @Wiz beside him, and speaks with calm urgency. Then for the final 5 seconds: @Wiz closes his eye for one second, opens it, and without speaking lifts his staff and points it toward a dark passage to his right, but does not move yet — the staff rings against stone with one clear note as it taps down.

Camera: static medium two-shot, locked tripod, framed Byte foreground-left and Wiz foreground-right, no movement, no zoom.

Setting: same Uray Pacha cavern from earlier, deep purple-black walls, magenta crystals dimly visible far in background, dark passage opening visible to camera-right.

Lighting: cool magenta primary from cavern crystals (#E83FC8 low intensity), lime-green emissive from Byte's headphone LEDs as accent, faint warm tungsten torchlight off-screen above, deep ambient.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic human proportions for Pax characters, no extra limbs, no distorted faces, no fast motion, no third character in frame, no warm gold glow, no Mariela.
```

### Camera & motion
- Static medium two-shot.

### Audio
- **Music cue:** sound design starts breathing — a soft layered ambient that wasn't there since B1
- **SFX:** Byte's headphone ping (single soft electronic tone), Wiz's staff rings against stone (one clear bell-like note)
- **Dialogue:**
  - BYTE (low, urgent, factual): "She's pressing the pencil. The question arrived." — voice direction: matter-of-fact, observational, not melodramatic. Pirahã-compatible — describes only what is observable. 7 words.

### Continuity anchors
- Previous clip: B6 ended with Mariela's hand pressing the pencil
- This clip starts with: HARD CUT to Uray Pacha — the pulse from her hand becomes Byte's detection
- Element MUST persist into B8-A: the next clip is the match-cut start (Mariela's hand) — this clip ends on Wiz pointing his staff toward a passage, signaling the upcoming relay

### Risk flags
- Copyright risk: low
- Continuity risk: medium — Byte's LED + headphones must match seed-clip and B2
- Generation risk: medium — 2 figures + dialogue + ear-twitch animation. Lipsync on Byte's 7 words must be tight; if it fails, re-prompt with him slightly side-angled so mouth is partially obscured

### Fallback if Seedance fails
- Split into 2 micro-shots: (a) Byte alone with line ~9s; (b) Wiz reaction with staff-point ~6s
- If lipsync drifts: keep the line as VO (Byte not on-camera-mouth) and re-render with Byte slightly turned away

---

## Clip B8-A — 2:00-2:03 — Mariela's hand grips pencil (3-second extreme close-up)

### Prompt Seedance (English, copy-paste ready)

```
@Mariela, a 36-year-old Latin-American woman with naturalistic skin tones, stylized human proportions matched to 3D animation style of the Pax universe. Extreme close-up on her left hand only — fingers gripping a wooden pencil hard enough that the paper underneath shows visible pressure-mark indentation just below a written line of placeholder cursive squiggles on the page of an open A6 brown leather notebook with faded elastic and cracked spine.

Action: For the full 3 seconds, the hand holds the pencil tightly, the fingertips white from pressure, the hand trembles a quarter-millimeter, a tiny grain of graphite catches the warm tungsten light. The dent in the page just below the squiggles is visible. No other movement.

Camera: static extreme close-up locked, no movement, no zoom, framed only on hand and pencil and page.

Setting: same kitchen table from B5/B6, brown leather notebook page in frame, warm tungsten light fall from upper-right.

Lighting: warm tungsten key (#FFD08A 3000K) from upper-right, soft cool dusk fill from camera-left, no magenta, no cyan glow.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 3 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no readable English text, no full face, no extra limbs, no distorted hands, no Pax characters in frame, no magic glow.
```

> **Important note for the producer/orchestrator:** Seedance native unit is 15s; this clip is **3 seconds**. Generate as a 15s clip with the static hand pose holding the entire duration, then trim to the first 3 seconds in the editor. Alternative: request Seedance with a duration parameter override if the API supports sub-15s — the research confirms native 15s is the unit, so trimming is the safer path.

### Camera & motion
- Locked extreme close-up. Static. No movement.

### Audio
- **Music cue:** kitchen quiet — the faint memory of B5/B6 score, almost silence
- **SFX:** paper pressure-mark crackle barely audible, a single shallow breath
- **Dialogue:** none

### Continuity anchors
- Previous clip: B7 ended on Wiz pointing staff toward dark passage
- This clip starts with: total hard tonal break — back to kitchen, extreme close-up of her hand
- Element MUST persist (and IMMEDIATELY break) into B8-B: the warm tungsten temperature of this shot is the EXACT thing the next clip's hard cut will rupture. Editor must NOT smooth the transition.

### Risk flags
- Copyright risk: low
- Continuity risk: low — only hand and pencil, no face
- Generation risk: low — single hand on a page, very simple

### Fallback if Seedance fails
- If hand drifts: render as a still image and add subtle micro-tremor in After Effects
- The page squiggles can be replaced via post-pro overlay if Seedance generates legible English text accidentally

---

## Clip B8-B — 2:03-2:15 — Wiz's palm: crystal materializes (12-second extreme close-up)

### Prompt Seedance (English, copy-paste ready)

```
@Wiz, an elder cyclops underground-tribe character, single central eye with droopy upper lid, long voluminous white beard, bushy white eyebrows, deep purple hooded robe with subtle turquoise rune trim, four-fingered weathered hand. Extreme close-up on @Wiz's open right palm in the dark of the qhocha cavern, his single eye visible in soft focus behind and slightly above the hand watching the palm intently.

Action: For the first 0.5 seconds the open palm is empty in dark cavern silence. Then for the next 5 seconds: above the palm, out of nothing, a small new magenta-violet crystal begins materializing — granular formation building from the air, frame-by-frame readable formation, dense small crystal coalescing molecule by molecule, NOT instant pop-in, NOT abstract magic blur, the formation timing is the visual idea, the crystal grows from invisible particles into solid geometry over these 5 seconds. Then for the next 4 seconds: the now-formed crystal pulses bright magenta once strongly, then settles to a steady soft pulse, floating two centimeters above his skin. Then for the final 2.5 seconds: the camera holds, @Wiz's eye in soft background focus watches the floating crystal, no movement.

Camera: static extreme close-up locked on the palm and the air above it, @Wiz's eye soft-focus in background, no movement, no zoom, over 12 seconds.

Setting: dark Uray Pacha qhocha cavern, near total darkness around the palm, deep purple-black ambient.

Lighting: the magenta-violet crystal as it forms is the primary emissive (#E83FC8), starting at zero intensity and growing to medium-bright at second 5, settling to gentle pulse, faint cool ambient cave fill on @Wiz's eye and beard, no warm tungsten, no other lighting.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 12 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic human proportions for Pax characters, no extra limbs, no distorted faces, no fast motion, no instant pop-in formation, no abstract magical sparkle blur, no warm tungsten light, no kitchen, no Mariela, no other characters, no Pax characters beyond Wiz's palm and eye.
```

> **Note:** Generate as 15s and trim to 12 seconds in the editor.

### Camera & motion
- Static extreme close-up. Locked.

### Audio
- **Music cue:** total silence for 1 frame at the cut from B8-A, then no music
- **SFX:** crystal formation sound — a small pane of glass cooling, with a warm undertone, mid-clip; sound design carries the moment
- **Dialogue:** none

### Continuity anchors
- Previous clip: B8-A ended on the warm-tungsten extreme close-up of Mariela's hand and the pressed pencil
- This clip starts with: HARD CUT — 1 frame of total silence, then the cool magenta-on-black palm
- Element MUST persist into B9: the just-formed magenta crystal, floating two centimeters above Wiz's palm — this exact crystal is what Wiz hands to Jiggy in the next clip. Same size, same density, same pulse rhythm.

### Risk flags
- Copyright risk: low
- Continuity risk: high — the crystal in this clip must equal the crystal in B9 (Wiz hands it over) and B11 (Jiggy delivers it to Mariela)
- Generation risk: high — the formation timing is the visual idea. If Seedance does instant pop-in or abstract sparkle, the magic system reads wrong. The prompt explicitly negates these. **Generate 5 variations minimum and pick the one with most readable molecule-by-molecule formation.**

### Fallback if Seedance fails
- Re-prompt with even more explicit slow formation: "the crystal builds visibly from particles over 5 seconds, each particle visible, like dust accreting"
- If formation is unreadable: shoot it as 2 sub-shots — (a) empty palm, 1s; (b) crystal already partway formed, then completing, 11s — and dissolve between
- Worst case: render the formation in After Effects with particle simulation, composite over a Seedance-generated still palm

---

## Clip B9 — 2:15-2:30 — Relay handoff (Wiz + Jiggy + Luxa)

### Prompt Seedance (English, copy-paste ready)

```
@Wiz, an elder cyclops with single central eye droopy upper lid, long voluminous white beard, deep purple hooded robe with turquoise rune trim, dark wood staff with magenta-violet crystal, in foreground-center holding a small new magenta-violet crystal floating above his open right palm, single tear running from corner of eye into white beard. @Jiggy, a small cyclops with single central turquoise eye, smooth turquoise-green skin, brown-red leather chest harness, leather hip satchel, no headwear, enters from frame-left with raised open right hand. @Luxa, a slender cyclops with single central eye, faint luminous turquoise-green skin, purple headband, multicolor tribal poncho with purple-gold-turquoise-magenta geometry, holding a warm golden-yellow crystal (#FFE34D), enters from frame-right.

Action: For the first 5 seconds: @Wiz holds the magenta crystal close to his chest, his single tear falls into beard, he closes fingers briefly around it. Then for the next 5 seconds: @Jiggy steps into frame-left already moving, raises right palm, @Wiz places the magenta crystal into Jiggy's right palm. Then for the final 5 seconds: @Luxa silently arrives from frame-right, presses the golden crystal into Jiggy's LEFT palm without breaking stride, falls back into shadow; @Jiggy turns toward a dark passage with magenta crystal in right palm and golden crystal in left palm, and exits frame.

Camera: static medium-wide three-shot composition, locked tripod, framed wide enough to hold all three figures with action staged across full width, no movement, no zoom.

Setting: dark Uray Pacha qhocha cavern, deep purple-black walls, faint magenta crystal ambient in background, dark passage opening visible frame-right.

Lighting: cool magenta primary from cavern (#E83FC8 low-medium), Luxa's golden crystal (#FFE34D) as a 5-second warm gold accent visiting the cool palette during her arrival, faint cool fill on Wiz's beard and tear, deep ambient.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic human proportions for Pax characters, no extra limbs, no distorted faces, no fast motion, no characters touching faces or overlapping body silhouettes, no fourth character, no Mariela, no humans.
```

### Camera & motion
- Static medium-wide three-shot.

### Audio
- **Music cue:** quiet sustained low score, warm undertone
- **SFX:** Wiz's audible breath, Luxa's footsteps as soft brush of cloth (no impact), Jiggy's first stride away with one slightly stronger heartbeat of cave pulse
- **Dialogue:**
  - WIZ (quiet, to himself, almost an exhale): "Still warm. Should burn me — and it doesn't." — voice direction: barely audible, weighty recognition not melodrama. 8 words.

### Continuity anchors
- Previous clip: B8-B ended on the floating magenta crystal above Wiz's palm
- This clip starts with: same crystal still above his palm, now we pull back to medium-wide
- Element MUST persist into B10: Jiggy carries magenta in right palm, golden in left palm

### Risk flags
- Copyright risk: low
- Continuity risk: high — three Pax characters with distinct identity must each match their seed-clip
- Generation risk: **high** — three figures in same plate is at the limit of Seedance's reliability. Per research Eje 5, this is the single highest-risk clip of the episode.

### Fallback if Seedance fails (DOCUMENTED IN BEAT SHEET)
- **Split into 2 micro-shots:**
  - **B9a (~6s):** @Wiz alone — tear + line "Still warm. Should burn me — and it doesn't." + closes fingers around crystal
  - **B9b (~9s):** @Jiggy enters left, @Wiz hands crystal, @Luxa intercepts from right with gold, @Jiggy exits — staged with tighter framing on the hands and exchange
- Cut between in editor with continuity match on Wiz's posture
- This fallback is documented in the script v2 explicitly; do not hesitate to invoke it

---

## Clip B10 — 2:30-2:45 — Storm-drain + drone drift (gold crystal demonstrates anti-drone)

### Prompt Seedance (English, copy-paste ready)

```
@Jiggy, a small cyclops underground-tribe character with single central turquoise eye, smooth turquoise-green skin, brown-red leather chest harness, leather hip satchel, no headwear, four-fingered hands, holding a small magenta-violet crystal closed in his right fist and a warm golden-yellow crystal cupped in his left palm. Behind him in the tunnel, @Zek, a cyclops with purple cap tilted sideways, retro analog boombox at hip, magenta-violet crystal pendant on tribal cord.

Three stories above on the urban street, two small black spherical antibody-drones with single magenta LED each, drifting on a slow patrol pattern. The drones are utility surveillance tech, not menacing. Their LEDs sweep slowly. Below them, a rectangular storm drain grate under a streetlamp on an empty Santiago street, around 10 PM.

Action: For the first 5 seconds: @Jiggy crouches below the grate in shadow, looks up at the patrolling drones, the nearest drone's LED begins to swing toward the grate. Then for the next 5 seconds: without taking his eyes off them, @Jiggy brushes the surface of the golden crystal once with his left thumb; the gold pulses almost imperceptibly; the two nearest drones drift exactly 30 degrees off-axis, mechanical re-pathing, oblivious system response, NOT fleeing in fear, NOT panicked, simply scan-target shifting as if their algorithm re-targeted, they continue patrol oblivious to him. Then for the final 5 seconds: behind @Jiggy in the tunnel, @Zek taps his boombox once and a single low subwoofer pulse vibrates the air; @Jiggy syncs his breathing to it then climbs up through the grate and exits frame upward.

Camera: starts as tight follow tracking on Jiggy from behind during the first 5 seconds, then becomes static medium-wide for the drone-drift moment and Jiggy's climb.

Setting: street level Av. Bilbao Ñuñoa Santiago at night, rectangular storm drain grate under a streetlamp, empty asphalt, mild fog, three stories above the patrolling drones drift in cool urban night blue.

Lighting: urban night blue ambient, single warm streetlamp pool above the grate (#FFD08A 3000K), cool magenta drone LEDs sweeping, the golden crystal in Jiggy's left palm casting a warm golden rim around his left hand, no fantasy lighting beyond crystal glow.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic human proportions for Pax characters, no extra limbs, no distorted faces, no fast motion, no menacing drone behavior, no drones fleeing in fear, no drone explosion, no aggressive sting in audio, no third Pax beyond Jiggy and Zek, no Mariela, no humans on street.
```

### Camera & motion
- Tight follow tracking → static medium-wide.

### Audio
- **Music cue:** none, sound design carries
- **SFX:** drone hum mechanical not menacing, subtle sub-tone shift the moment the gold crystal pulses (almost subliminal, like a frequency dropping out of the room), Zek's boombox subwoofer pulse felt more than heard
- **Dialogue:** none

### Continuity anchors
- Previous clip: B9 ended with Jiggy exiting frame magenta-right + gold-left
- This clip starts with: Jiggy at the grate with both crystals, identical to B9 exit
- Element MUST persist into B11: Jiggy still has the magenta crystal in his right hand (gold consumed/pocketed off-screen by end of B10)

### Risk flags
- Copyright risk: low
- Continuity risk: medium — drones must read as "system re-pathing" not "fleeing in fear"
- Generation risk: medium — drift behavior of drones is the load-bearing visual. Per research and script v2, the drones must read MECHANICAL OBLIVIOUS not FEARFUL. This is the highest prompt-engineering risk in the episode. The prompt explicitly negates fear/panic and explicitly sets "mechanical re-pathing".

### Fallback if Seedance fails
- If drones read as "fleeing": re-prompt with "drones rotate 30 degrees on a slow servo, no panic, no rapid escape, scan beam shifts away, drones continue prior trajectory unchanged in pace"
- If 30-degree drift is unclear: split clip into (a) Jiggy sees drones approaching, (b) thumb-brush + drone drift in tighter framing, (c) Zek boombox + climb

---

## Clip B11 — 2:45-3:00 — Kitchen: Jiggy delivers warmth (dual-palette, dual rim-light)

### Prompt Seedance (English, copy-paste ready)

```
@Mariela, a 36-year-old Latin-American woman, brown hair pulled back in a low ponytail, light office blouse, thin metal-framed glasses, naturalistic skin tones, stylized human proportions matched to 3D animation style of the Pax universe (slightly softened features, not photoreal). @Jiggy, a small cyclops with single central turquoise eye, smooth turquoise-green skin (#21D8B6), brown-red leather chest harness, leather hip satchel, no headwear, four-fingered hands, holding a small magenta-violet crystal in his open right palm.

Action: For the first 5 seconds: @Mariela sits at the small kitchen table, the open notebook visible, she reaches forward to close the notebook. Then for the next 5 seconds: @Jiggy appears from behind the refrigerator on the side of the kitchen — invisible to her but fully solid to camera — moves with calm purpose toward her left hand which rests on the table, opens his own palm with the magenta crystal in it, places the crystal gently against her palm. Then for the final 5 seconds: @Mariela's hand twitches once, she lifts it slowly looks at it, there is nothing visible to her but her face shifts into a tiny surprised softening, she brings her palm closer to her chest holds it, a small warmth registers; @Jiggy is already gone from frame.

Camera: gentle slow dolly-in from medium-wide to medium close-up over 15 seconds, locked horizon, no shake, framed to hold both Jiggy and Mariela in single plate without overlapping silhouettes.

Setting: same small Santiago apartment kitchen, same tiled floor, same hanging tungsten bulb, same table with notebook, refrigerator visible camera-left.

Lighting: warm tungsten hanging bulb (#FFD08A 3000K) as primary key on Mariela and the kitchen room — this is the room's palette. @Jiggy receives a SPECIFIC dual rim-light treatment: a thin magenta rim (#E83FC8) on his LEFT side from his own crystal aura, and a warm tungsten rim (#FFD08A 3000K) on his RIGHT side catching the kitchen's hanging-bulb fall-off; the two rims blend into a single warm-cool integrated outline along his shoulder and arm. @Jiggy reads as belonging in the kitchen plate, lit by the room he is in, NOT a CG paste-in. Soft volumetric haze.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic photoreal face for Mariela, no realistic human proportions for Jiggy, no extra limbs, no distorted faces, no fast motion, no flat key-light on Jiggy with no warm wrap, no saturated turquoise skin against warm walls without rim integration, no silhouette that screams CG compositing layer, no overlap of Jiggy and Mariela bodies, no Jiggy facing camera staring at viewer.
```

### Camera & motion
- Slow dolly-in.

### Audio
- **Music cue:** no music
- **SFX:** wall clock ticking, neighbor's TV through the wall very faint, the crystal-formation sound from B8-B barely there as a memory
- **Dialogue:** none

### Continuity anchors
- Previous clip: B10 ended with Jiggy climbing up through the storm-drain grate
- This clip starts with: he's now in the kitchen — match on the magenta crystal in his right hand (same crystal from B8-B → B9 → B10 → B11)
- Element MUST persist into B12: Mariela's hand closed over the warmth, the open notebook on the table

### Risk flags
- Copyright risk: low
- Continuity risk: **high** — Mariela's identity + Jiggy's identity must both match their seed-clips, in the same plate. The dual-palette is the only beat in the episode where both palettes coexist.
- Generation risk: **high** — paste-in risk on Jiggy. Per script v2, this is one of the two most-engineered prompts of the episode. The image contract is explicit in the prompt.

### Fallback if Seedance fails
- If Jiggy reads as paste-in: regenerate with explicit instruction "render Jiggy with environmental light reading on him — warm tungsten on his right shoulder, his own magenta on his left — like he is physically in the room"
- If overlap occurs: re-frame with Jiggy on the LEFT side of the kitchen near the refrigerator, Mariela on the RIGHT at the table, distance of ~1 meter between silhouettes
- Worst case: render Jiggy alone in a 15s clip with the dual rim-light, render Mariela alone in a 15s clip looking at her own hand, composite both in After Effects with matched warm-tungsten background

---

## Clip B12 — 3:00-3:15 — "...okay."

### Prompt Seedance (English, copy-paste ready)

```
@Mariela, a 36-year-old Latin-American woman, brown hair pulled back in a low ponytail, light office blouse, thin metal-framed glasses, no makeup, calm tired competent expression with subtle micro-shift, naturalistic skin tones, stylized human proportions matched to 3D animation style of the Pax universe (slightly softened features, not photoreal).

Action: For the first 4 seconds: @Mariela closes her fingers over the warmth in her left palm, looks at the open notebook with the handwritten line, her face holds — corners of mouth move half a centimeter then settle, something smaller and more real than crying happens to her face. Then for the next 6 seconds: she stands, picks up a mug of cold tea from the table, walks to the sink camera-left, pours the cold tea out, refills the kettle. Then for the final 5 seconds: she sits back down at the table, looks ahead, does not open the notebook again, just sits, the kettle starts to heat.

Camera: static medium shot on Mariela centered, locked tripod, no movement, no zoom.

Setting: same small Santiago apartment kitchen, same tiled floor, same hanging tungsten bulb, same table, sink visible camera-left, kettle on stove camera-left.

Lighting: warm tungsten hanging bulb (#FFD08A 3000K) as primary key, slightly brighter than previous kitchen scenes — this is the first major-key visual moment of the episode, the room reads warmer, soft fill, gentle volumetric.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic photoreal face, no extra limbs, no distorted faces, no fast motion, no Pax characters in frame, no crying, no melodramatic expression, no big smile.
```

### Camera & motion
- Static medium shot.

### Audio
- **Music cue:** a single sustained warm chord — the FIRST major-key moment of the episode — enters at second 8 and sustains through end
- **SFX:** kettle hum starts at second 11
- **Dialogue:**
  - MARIELA (to no one, almost inaudible): "...okay." — voice direction: barely a whisper, to herself, micro-acceptance not relief. 1 word.

### Continuity anchors
- Previous clip: B11 ended with Mariela holding her palm against her chest, Jiggy gone
- This clip starts with: same posture, hand still closed
- Element MUST persist into B13A: Mariela's emotional baseline (settled, not transformed)

### Risk flags
- Copyright risk: low
- Continuity risk: medium — face must match seed-clip and previous Mariela clips
- Generation risk: low — single character, simple actions, one whispered word

### Fallback if Seedance fails
- If "okay" lipsync fails: keep her face slightly turned away from camera when speaking; line is whispered, treat as VO
- If micro-expression doesn't read: regenerate with "subtle softening of mouth corners, no smile, no tear, just settling"

---

## Clip B13A — 3:15-3:30 — Wiz silhouette + Jiggy returns (NO POCKET CAMEO HERE)

### Prompt Seedance (English, copy-paste ready)

```
@Wiz, an elder cyclops underground-tribe character, single central eye with droopy upper lid, long voluminous white beard, bushy white eyebrows, deep purple hooded robe with subtle turquoise rune trim, dark wood staff topped with magenta-violet crystal, four-fingered weathered hands, 2.8 head proportions. He stands with his back partly to camera, observing a fine wayra-current — fine motes of dust spiraling upward through a cracked cavern ceiling, a near-invisible pressure shift moving up. @Jiggy, a small cyclops with single central turquoise eye, smooth turquoise-green skin, brown-red leather chest harness, leather hip satchel, no headwear, runs back into the qhocha breathing hard, both hands now empty.

Action: For the first 7 seconds: the camera holds low-and-slow drifting down across @Wiz's silhouette from behind — the deep purple robe, the staff, the back of the white-bearded head — while the upward dust spirals through the cracked ceiling. Then for the next 4 seconds: @Jiggy runs into frame from camera-left already breathing hard, stops in front of @Wiz; @Wiz pauses, then turns slowly toward @Jiggy. Then for the final 4 seconds: @Wiz finishes turning to face @Jiggy as two of the empty stalagmites near him begin to glow faintly magenta — just two, tiny, but they were dark in earlier scenes.

Camera: gentle slow dolly-down across Wiz's back-silhouette over the first 7 seconds, then static medium two-shot for the final 8 seconds, locked horizon, no shake, no zoom.

Setting: Uray Pacha qhocha cavern brighter than earlier scenes, deep purple-black walls, hairline crack in cavern ceiling visible high frame-center with thin shaft of upward-flowing dust, two stalagmites near Wiz beginning to glow soft magenta, warm tungsten torchlight off-screen.

Lighting: warm tungsten torchlight off-screen as ambient cave fill, soft magenta from the two awakening stalagmites near Wiz, deep cool ambient elsewhere, gentle volumetric haze with upward-spiraling dust through ceiling crack.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic human proportions for Pax characters, no extra limbs, no distorted faces, no fast motion, NO close-up of Wiz's pocket, NO second crystal in Wiz's hand or pocket, NO pinky finger detail, NO anchor-spark cameo, NO additional crystal artifacts in frame beyond Wiz's staff crystal and the two awakening stalagmites, no Luxa, no Byte, no Zek, no Mariela.
```

### Camera & motion
- Slow dolly-down → static medium two-shot.

### Audio
- **Music cue:** score swells gently, warm not triumphant
- **SFX:** the cavern pulse is now almost a normal heartbeat (steady), Jiggy's breathing audible
- **Dialogue:**
  - JIGGY (catching breath): "Do I pass it to the next runner?" — voice direction: tired, dutiful, genuinely asking. 8 words.
  - WIZ (turning slowly, looking at Jiggy): "Wait. This one stays a while." — voice direction: warm certainty, no smile, the closest Wiz comes to tenderness. 6 words.

### Continuity anchors
- Previous clip: B12 ended with Mariela sitting at the kitchen table
- This clip starts with: HARD CUT back to the cavern — Wiz facing the wayra-current
- Element MUST persist into B14 (and into editorial): the upward dust spiral is the visual rhyme to the upcoming cliffhanger glowing line
- **Critical post-pro element:** the B13B insert (≈83ms = 2 frames at 24fps) is composited into THIS clip's timeline at second 7.0 (= 3:22 of episode master). See ASSETS NO-SEEDANCE.

### Risk flags
- Copyright risk: low
- Continuity risk: high — Wiz must NOT be holding any second crystal in this clip; the prompt explicitly excludes it
- Generation risk: medium — Seedance may spontaneously generate a second crystal (model bias toward "elder character + magic" pattern). Negative prompt is aggressive against this.

### Fallback if Seedance fails
- If a second crystal appears: regenerate with even stricter negative — "no items in Wiz's left hand, no items in any pocket, his left hand is empty and at his side"
- If Wiz turn-around drifts: split into (a) silhouette dolly-down with upward dust ~8s; (b) Jiggy enters Wiz turns ~7s

---

## Clip B14 — 3:30-3:45 — Cliffhanger: glowing notebook

### Prompt Seedance (English, copy-paste ready)

```
The same small Santiago apartment kitchen, now empty of people. A second mug of tea drained sits beside the kettle on the counter. The hanging tungsten light over the table is still on. The same A6 brown leather notebook with faded elastic and cracked spine lies open on the table, facing up — the page with the handwritten question visible (placeholder cursive squiggles in the Seedance generation; the real legible line will be added in post-production overlay).

A bedroom door is closed at frame-right and a thin strip of warm light spills under it across the floor — Mariela is asleep beyond it.

Action: For the full 15 seconds, the camera slowly pushes in on the open notebook page from medium-wide to extreme close-up of the placeholder writing. The handwritten line on the page is glowing softly cyan with a slow pulse synced to roughly 60 beats per minute heartbeat rhythm — the glow is on the line of writing only, not the rest of the page. The pulse is gentle, alive, NOT static, NOT blinking, NOT loading-screen aesthetic, NOT a flat strobe — it is a soft slow living breath of light, mirroring the opening cavern crystal pulse. The kitchen is otherwise still. Hold final 5 seconds at extreme close-up.

Camera: slow gentle dolly-in from medium-wide of the table to extreme close-up of the writing line over 12 seconds, then locked hold for the final 3 seconds, no shake, no zoom.

Setting: same kitchen, table with open notebook, kettle, drained mug, closed bedroom door at frame-right with light spilling under, Santiago night through the window in deep blue.

Lighting: warm tungsten hanging bulb (#FFD08A 3000K) as ambient kitchen key, the cyan glow on the handwritten line (#3FE0C8 at low-medium intensity, soft pulse 60bpm) as the only emissive element in frame, deep night blue from window, soft volumetric.

Style: stylized 3D animation, smooth shading, expressive proportions, soft subsurface scattering on skin, painterly background, cinematic warm-melancholic palette, 16:9, 15 seconds.

Negative: no cuts, no zoom, no rapid camera movement, no shaky cam, no text overlay, no watermark, no brand logos, no realistic photoreal anything, no extra limbs, no distorted faces, no fast motion, no readable English text on the page (placeholder squiggles only — real text added in post), no static glow, no blinking light, no loading-screen flash, no neon strobe, no Pax characters in frame, no Mariela visible, no humans in frame, no fantasy aesthetic.
```

### Camera & motion
- Slow dolly-in over 12s → locked hold 3s.

### Audio
- **Music cue:** a single low cello note — the same as the cold open in B1 — enters at second 1 and sustains
- **SFX:** the cavern pulse from B1 and the cyan pulse on the page are the same rhythm now; they sync once at second 8, then silence after second 13 leading into fade-to-black
- **Dialogue:** none
- **End card** (post-pro overlay after fade): "the wind starts somewhere." in small lowercase under the PAX logo. Single warm wind sound. Then silence.

### Continuity anchors
- Previous clip: B13A ended with Wiz turning to Jiggy and two stalagmites starting to glow
- This clip starts with: HARD CUT back to kitchen empty
- Element MUST persist: the SAME handwritten line ("Why did I stop writing here?") that was overlay-composited in B6 must be the EXACT same overlay asset here, now with cyan emissive. Reuse the identical asset; do not redraw.
- **Critical post-pro element:** the handwritten line is rendered in B14's Seedance plate as placeholder squiggles. The legible line is added in post via the SAME overlay asset used in B6, with a masked cyan emissive layer pulsing at 60bpm over the letterforms. See ASSETS NO-SEEDANCE.

### Risk flags
- Copyright risk: low
- Continuity risk: **high** — the handwritten line MUST be identical in B6 and B14; the cliffhanger lives or dies on the viewer recognizing the same words
- Generation risk: medium — Seedance with glowing cyan handwritten English text is unreliable. We negate the legible text, render placeholder, and overlay in post. The pulse rhythm is also better in post than in Seedance.

### Fallback if Seedance fails
- If cyan pulse over-renders: composite the entire glow in After Effects via masked emissive layer over the overlay asset, exclude any Seedance glow
- If notebook proportions drift: regenerate with "same notebook from previous clips, A6 brown leather, faded elastic, cracked spine, lying flat open"

---

# ENSAMBLADO POST-PRODUCCIÓN

## Order of clips (final timeline)

1. **B1** (0:00-0:15) — cold open
2. **B2** (0:15-0:30) — three silhouettes
3. **B3** (0:30-0:45) — office Mariela
4. **B4** (0:45-1:00) — metro notebook
5. **B5** (1:00-1:15) — kitchen pause
6. **B6** (1:15-1:45) — writing the question (Seedance 15s + extended hold)
7. **B7** (1:45-2:00) — Byte detects
8. **B8-A** (2:00-2:03) — Mariela's hand
9. **B8-B** (2:03-2:15) — Wiz's palm crystal forms
10. **B9** (2:15-2:30) — relay handoff
11. **B10** (2:30-2:45) — storm-drain + drone drift
12. **B11** (2:45-3:00) — kitchen warmth delivery
13. **B12** (3:00-3:15) — "...okay."
14. **B13A** (3:15-3:30) — Wiz silhouette + Jiggy returns + B13B inserted at 3:22
15. **B14** (3:30-3:45) — cliffhanger glowing notebook + end card

## Recommended transitions

| From → To | Transition | Reason |
|---|---|---|
| B1 → B2 | continuity cut | same cavern, camera reveals figures behind crystal |
| B2 → B3 | **HARD CUT** | total tonal break: cold cavern → bright fluorescent office. Editor must NOT smooth |
| B3 → B4 | match cut on Mariela | she's leaving the office, on the metro |
| B4 → B5 | dissolve (optional) | time passes, she's home now |
| B5 → B6 | continuity cut | same scene, push in on her writing |
| B6 → B7 | **HARD CUT** | match-pulse cut: her pencil press = Byte's detection |
| B7 → B8-A | **HARD CUT** | jump back to kitchen, extreme close-up |
| **B8-A → B8-B** | **HARD CUT — 1 FRAME OF TOTAL SILENCE — load-bearing** | the entire match-cut idea of the episode lives here. **DO NOT smooth, do not dissolve, do not insert any transition. 1 frame of black/silence between the two shots is OK and recommended.** |
| B8-B → B9 | continuity cut | same crystal, pull back to medium-wide three-shot |
| B9 → B10 | match cut on Jiggy exiting frame | he's running toward surface |
| B10 → B11 | match cut on Jiggy climbing up | he's now in the kitchen |
| B11 → B12 | continuity cut | same scene, Jiggy is gone |
| B12 → B13A | **HARD CUT** | back to the cavern |
| B13A → B14 | **HARD CUT** | back to empty kitchen |
| B14 → end card | fade to black | hold black for 2 seconds, then PAX logo |

## Audio editorial

- **Master pulse track:** a single audio asset of the slowed-heartbeat pulse from B1. This same track is reused (at varying volumes/filters) in B2, B4, B5, B6, B11 (very faint), and B14 (synced with the cyan glow). Maintain the same tempo across all uses — the climactic sync between cave-pulse and notebook-pulse in B14 only works if the rhythm is identical to B1.
- **Cello motif:** sustained low cello in B2; absent through urban/kitchen middle; returns as single low note in B14.
- **Piano motif:** single low piano note from B4 → B5 → B6, fading.
- **Major-key chord:** introduced ONLY in B12 — the first major key in the episode. Sustain from B12 through silence at B13A start.
- **Crystal-formation sound:** B8-B (primary), B11 (memory, very faint).
- **Drone hum:** B10 only. Sub-tone shift on the gold crystal pulse at B10 second 6-8.
- **Boombox subwoofer pulse:** B10 only.
- **Foley:** kettle (B5, B12), wall clock (B11, B12), neighbor TV (B11), dust (B1, B13A), staff-on-stone (B7), Pax footsteps (B9, B11).
- **Mix philosophy:** the silence is as important as the sound. B1, B6, B8-A→B8-B transition, B14 fade — all carry deliberate quiet that lets the next note breathe.

## Frame insert manual — B13B (cameo crystal-anchor)

> **NOT Seedance. Editor task ONLY.**

- **Position in master timeline:** at second **7.0** of B13A (i.e., **3:22** of the episode master)
- **Duration:** 2 frames at 24 fps = **≈83 ms**
- **Content:** extreme close-up of the inside of Wiz's left robe pocket — visible inside the deep fold of purple cloth (#3D2A66), a second crystal older than the magenta one, **dusty pale-gold (#D9C28A)**, low saturation, slight grain, about 60% the size of the new spark; Wiz's pinky finger barely brushes its surface; the crystal is slightly off-frame to lower-right, NOT highlighted by any rim light beyond the ambient cave glow already established in B13A
- **Tools:** Premiere Pro / DaVinci Resolve / After Effects. Composite as 2-frame insert layered over the B13A timeline at second 7.0
- **Color match:** apply the same LUT and grain as B13A so the insert feels "stolen" from the same world; if the hard 2-frame cut feels too abrupt in dailies, add 1-frame fade-in / 1-frame fade-out
- **Source asset:** **manually rendered or photographed close-up — NOT Seedance generated.** A still illustration of the robe-pocket interior with the off-gold crystal and pinky-finger detail is sufficient (the viewer registers this for ≈83ms; conscious recognition is not required)
- **Owner:** `pax-visual-designer` produces the single PNG / single-frame asset; the editor places it
- **Hard rule:** do NOT extend duration "so the audience sees it"; the entire point is felt-not-seen

## Handwritten overlay reused between B6 and B14

> **NOT Seedance. Post-production overlay asset.**

- **Asset:** a single handwritten line of the words **"Why did I stop writing here?"** — handwritten in unsteady English cursive, in soft graphite (for B6) and with a masked cyan emissive layer (for B14)
- **Why it must be the same asset:** the cliffhanger lives or dies on the viewer recognizing the IDENTICAL handwriting + IDENTICAL words across both beats
- **B6 use:** composite the asset on the notebook page over the Seedance placeholder squiggles — graphite color, no glow, fully written and visible by ~second 11 of B6's 15s
- **B14 use:** composite the SAME asset on the notebook page over the Seedance placeholder squiggles — add a masked cyan emissive layer (#3FE0C8 low-medium) over the letterforms, pulsing at 60bpm in sync with the cavern pulse audio
- **Tool:** After Effects (preferred for the cyan emissive masking) / DaVinci Resolve (acceptable)
- **Owner:** `pax-visual-designer` produces the asset (one PNG with alpha for the writing + one mask layer for B14 cyan emissive); editor composites in both beats

---

# ASSETS NO-SEEDANCE

## 1. B13B — frame insert ≈83ms

**Source:** manual illustration or composited photograph of Wiz's robe pocket interior with pale-gold crystal + pinky-finger detail
**Color spec:** pocket cloth #3D2A66, crystal #D9C28A low saturation, slight grain
**Format:** PNG (single frame) or PNG sequence (2 frames if subtle motion is desired)
**Tooling:** Photoshop / Procreate / Krita / Blender still render — owner's choice
**Placement:** Premiere/DaVinci/AfterEffects timeline, frame insert at second 7.0 of B13A
**Owner:** `pax-visual-designer`
**Status:** required asset, blocking on B13A delivery

## 2. Handwritten overlay (shared B6 + B14)

**Source:** hand-drawn cursive English line "Why did I stop writing here?"
**Color specs:**
- B6 version: soft graphite (#3A3A3A on alpha)
- B14 version: same graphite layer + masked cyan emissive (#3FE0C8) over letterforms with 60bpm pulse keyframes
**Format:** PNG with alpha (graphite layer) + masked emissive layer (.aep or .drp project file with the pulse animation)
**Tooling:** Photoshop / Procreate (handwriting capture) + After Effects (cyan emissive + pulse animation)
**Placement:** composite over Seedance plates of B6 (no glow) and B14 (with glow)
**Owner:** `pax-visual-designer`
**Status:** required asset, blocking on B6 + B14 final delivery

## 3. Audio editorial assets

**Master pulse track:** single audio file, slowed-heartbeat pulse, used in B1/B2/B4/B5/B6/B11/B14
**Cello sustain:** low cello note, used in B2 and B14
**Piano single note:** used in B4/B5/B6
**Warm major chord:** B12 only
**Crystal-formation sound:** small pane of glass cooling with warm undertone — B8-B and B11 (memory)
**Drone hum + sub-tone shift:** B10
**Boombox sub pulse:** B10
**End-card wind:** single warm wind sound
**Owner:** sound designer (TBD by orchestrator)
**Tooling:** DAW of choice (Pro Tools / Logic / Reaper)

---

## OUTPUT DEL AGENTE

```
ESTADO: COMPLETO
ARCHIVO: C:\Users\aldot\.gemini\antigravity\scratch\pax-miniserie\technical_script_ep01.md
NÚMERO DE CLIPS SEEDANCE NARRATIVOS: 15
NÚMERO DE SEED-CLIPS DE IDENTIDAD: 3
TOTAL GENERACIONES SEEDANCE: 18
NÚMERO DE TAREAS POST-PRO: 3 (B13B insert, handwritten overlay shared B6+B14, audio editorial)
DURACIÓN NARRATIVA TOTAL: 3:45
COPYRIGHT FLAGS: 0 high, 0 medium, 18 low (zero brand names; replacement table aplicada)
CONTINUIDAD FLAGS: 4 high (B8-B crystal must equal B9/B11 crystal; B11 dual-palette dual-rim-light; B14 handwritten line must equal B6; Mariela face must persist across 7 clips), 6 medium, 8 low
PRESUPUESTO USD: 81-108 base + 20% buffer = 97-130 total

TOP 5 RIESGOS A REVISAR ANTES DE GENERAR:

  1. B8-B (Wiz's palm + crystal formation) — la formación granular molecule-by-molecule
     es load-bearing. Si Seedance hace pop-in instantáneo o sparkle abstracto, la regla
     mágica del piloto se rompe. Generar 5 variaciones mínimo y elegir la más legible.
     Plan B: render de partículas en After Effects sobre still de palma generada.

  2. B11 (kitchen + Jiggy paste-in) — el dual-palette image contract es el único shot
     del piloto donde dos paletas conviven. Riesgo alto de que Jiggy lea como overlay CG.
     Negative prompt agresivo. Plan B: render Jiggy y Mariela en clips separados y
     compositar en post con tungsteno cálido matched.

  3. B9 (relay handoff con 3 figuras Pax) — al límite de la confiabilidad de Seedance
     según research Eje 5. Fallback documentado: split en 2 micro-shots (B9a Wiz tear+line,
     B9b Jiggy entra/Wiz entrega/Luxa intercepta/Jiggy sale). No dudar en invocar fallback
     si la primera generación tiene morph de identidad.

  4. B10 (drones drift 30°) — el comportamiento mecánico-oblivio es load-bearing. Si los
     drones leen como "fleeing in fear" o si el audio mete sting amenazante, el tono se
     rompe (lore 4.4 violado). Prompt y negative prompt explícitos. Vigilar el output
     antes de aprobar.

  5. B14 + B6 (handwritten line cyan glow) — el cliffhanger lee la frase. Estrategia:
     Seedance genera placeholder squiggles, post-pro composita la frase legible (asset
     compartido entre B6 y B14). Verificar que el asset es UN ÚNICO archivo reutilizado,
     no dos diseños distintos. La cyan emissive con pulso 60bpm va en post, no en
     Seedance.

RIESGOS SECUNDARIOS A MONITOREAR:
  - B13A: Seedance puede generar espontáneamente un segundo cristal en la mano de Wiz.
    Negative prompt es agresivo pero el modelo tiene bias "elder + magic". Verificar.
  - B6: el brillo cyan en el lomo de la libreta debe ser "almost imperceptible". Si
    Seedance lo over-renderiza, removerlo del Seedance plate y compositar en post.
  - Mariela face drift: 7 clips con su cara. Aplicar las 4 piezas de identidad (seed-clip,
    @Mariela tag literal, char sheet textual idéntico, keyframe injection del start frame).

SIGUIENTE: orquestador → ejecutar generación clip-a-clip. Recomendación: empezar por
los 3 seed-clips (Mariela, Jiggy, Wiz) ANTES de cualquier clip narrativo, porque sin
seed lock el drift está garantizado desde clip 4-5.
```
