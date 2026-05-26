"""
Generate all 38 frames (start+end) for the 9-min Mushin-Pax video + 1 thumbnail.
Uses edit_image (char sheet reference) for scenes with Pax characters.
Uses generate_image for scenes without identifiable characters.

Run: python scripts/gen_frames_9min.py
"""

import os
import sys
import asyncio

# Resolve paths
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from scripts.openai_images import edit_image, generate_image, edit_image_async, generate_batch_async
from openai import AsyncOpenAI

# Char sheet paths
JIGGY = os.path.join(REPO, "_lore", "personajes", "jiggy.png")
WIZ   = os.path.join(REPO, "_lore", "personajes", "wiz.png")
AGATHA = os.path.join(REPO, "_lore", "personajes", "agatha.png")
KZ    = os.path.join(REPO, "_lore", "personajes", "kz.png")

FRAMES_DIR = os.path.join(REPO, "gestos", "_backlog", "video-educativo", "frames-9min")
os.makedirs(FRAMES_DIR, exist_ok=True)

# Common style suffix
STYLE = "3D PBR render, stylized animation, neon-magic lighting, subsurface scattering on skin, bloom on crystal emissives, volumetric fog, cinematic composition, 16:9 aspect ratio"
SIZE = "1536x1024"  # 16:9 horizontal

def fp(name):
    return os.path.join(FRAMES_DIR, name)

# -----------------------------------------------------------------------
# Build jobs list: each job is a dict with keys for generate_batch_async
# or a special marker for generate_image (no reference).
# -----------------------------------------------------------------------

jobs = []

# --- Scene 01 — No characters, crystal only ---
jobs.append({
    "type": "generate",
    "prompt": f"A single ancient crystal formation in a black void, barely visible. A faint jade green pulse (#21D8B6) — one heartbeat of light. The crystal is rough, ancient, covered in mineral dust. Deep shadow. Only the crystal and darkness. Palette: near-black with a whisper of jade. Mood: ominous, still, lonely. {STYLE}",
    "output_path": fp("scene-01-start.png"),
})
jobs.append({
    "type": "generate",
    "prompt": f"Same single ancient crystal in a black void, but the pulse has stopped completely. The crystal is dark stone, dead. A hairline crack runs down its surface catching the last trace of ambient light. Total silence visualized. Palette: charcoal #2A2A2A, no color accents. Mood: loss, urgency. {STYLE}",
    "output_path": fp("scene-01-end.png"),
})

# --- Scene 02 — Jiggy (distant) ---
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference sheet for Jiggy. Generate a wide establishing shot of the Uray Pacha — vast underground cavern system. Towering basalt columns, crystal veins running through walls like circulatory systems. Most crystals are dim or dead. Bioluminescent moss on the floor provides faint green light. Scale is massive. In the far distance, a tiny Jiggy figure (maintaining identity from Image 1) sits cross-legged before a dark crystal. Palette: basalt grey #3D3D3D, dead jade #1A6B5C, distant magenta dot. Mood: grand, melancholic, vast. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-02-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference sheet for Jiggy. Generate a medium-wide shot inside a vast underground cavern. Camera has pushed in slightly. Jiggy (maintaining exact identity from Image 1) is visible — small turquoise-skinned cyclops figure hunched over a crystal that refuses to glow. His posture radiates frustration. Around him, other crystal formations are dark. The Uray Pacha feels like a city with a blackout. Palette: basalt grey, Jiggy's skin #21D8B6, his vest #7A3E2B. Mood: isolation within grandeur. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-02-end.png"),
})

# --- Scene 03 — Start: generic elders, End: Wiz ---
jobs.append({
    "type": "generate",
    "prompt": f"Temple interior — ancient, ornate. Three elder Pax beings (amber/gold skin tones, single large cyclops eye each, simple robes, turquoise skin with amber tint) stand around a massive crystal formation. Their hands glow. The crystal blazes with white-gold light. Carved walls behind them show geometric patterns. Everything is alive, warm, powerful. Palette: amber #D4A017, gold #FFD700, white crystal core, warm jade walls. Mood: power, harmony, ancient mastery. {STYLE}",
    "output_path": fp("scene-03-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference sheet for Wiz. Generate Wiz stepping into frame from the right side, emerging from shadow. Staff in hand, crystal atop it glowing faint violet #8A4DD1. His amber skin #D4A017 catches the light. White beard flows. His single cyclops eye looks directly at viewer — calm, knowing, slightly amused. Background: an ancient temple fades into darkness behind him. He is the bridge between past and present. Palette: amber Wiz, violet staff crystal, dark background. Mood: authority, warmth, invitation. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [WIZ],
    "output_path": fp("scene-03-end.png"),
})

# --- Scene 04 — Jiggy + KZ ---
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Image 2 is the character reference for KZ. Generate Jiggy lying on a crystal-bed (natural rock formation shaped like a hammock with embedded dead crystals). His single cyclops eye is open, staring at the ceiling. One arm dangles off the side. KZ — a small round bioluminescent creature (from Image 2) — bounces near his head trying to get attention. Jiggy's expression: bored, restless, slightly guilty. The alcove is messy — exploration maps on walls, food scraps, scattered crystal fragments. Warm ambient light from moss. Palette: Jiggy's skin #21D8B6, KZ glowing lime #6CF0D6, warm cave tones #5C4033. Mood: relatable lethargy. Maintaining exact character identities from reference images. {STYLE}",
    "input_image_paths": [JIGGY, KZ],
    "output_path": fp("scene-04-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate Jiggy at a charging station — a carved stone table with five dim crystals arranged in a row. He touches one with his index finger. Nothing happens. His expression is deflated. His other hand props up his chin. Behind him, a tunnel exit glows invitingly — adventure is RIGHT THERE but duty holds him here. Palette: dull crystals grey-jade #4A6B60, Jiggy's frustrated face, bright tunnel exit glow in background. Mood: trapped by obligation. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-04-end.png"),
})

# --- Scene 05 — Jiggy ---
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate Jiggy deep in an Uray Pacha tunnel system — far from the main cavern. He's mid-stride, one hand trailing along a wall of glowing mineral veins. His single cyclops eye is WIDE — pure wonder. Bioluminescent plants hang from the ceiling like chandeliers. The tunnel narrows ahead into unknown territory. His explorer bag bounces at his hip. Palette: deep teal tunnel #0D4F4F, bright mineral veins (amber #D4A017, magenta #FF49B4, cyan #3FE0C8), Jiggy lit from all sides by the glow. Mood: pure absorption, joy, discovery. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-05-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate Jiggy crouched at a new mineral vein, face inches from it, mouth slightly open in awe. The vein pulses with a deep violet-gold color. His hand reaches toward it instinctively. The tunnel around him is beautiful, alien, alive. He has been here for hours but has no concept of time. Palette: violet-gold vein #8A6DD1 + #D4A017, Jiggy's wonder-face, dark but rich tunnel. Mood: total flow, timelessness. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-05-end.png"),
})

# --- Scene 06 — Agatha + Jiggy ---
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Agatha. Image 2 is the character reference for Jiggy. Generate a scene at a charging station. Agatha (from Image 1) stands before Jiggy (from Image 2). She is taller, composed — green moss skin #4A7C59 with gold accents. Hands open, palms down (the Pax gesture for 'this is your task'). Behind her, a node map glows on the wall — a crystalline diagram showing lit and dark sectors of the Uray Pacha. Jiggy looks up at her, arms crossed, already checked out. Palette: Agatha's moss green, gold details, Jiggy's reluctant turquoise, cool blue node map. Mood: authority meets apathy. Maintaining exact character identities from reference images. {STYLE}",
    "input_image_paths": [AGATHA, JIGGY],
    "output_path": fp("scene-06-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate a close-up on Jiggy's face as someone walks away. His expression: 'Why should I care?' The crystals in front of him are dead. A node map behind shows Sector 7-South blinking dark, needing light. But Jiggy doesn't look at it. He looks at the tunnel exit. Palette: Jiggy's face flat and unengaged, blinking red node in soft focus background. Mood: disconnect, the direction problem visualized. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-06-end.png"),
})

# --- Scene 07 — Jiggy ---
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate Jiggy standing in front of a crystalline node map on a cave wall, actually looking at it for the first time. His finger traces a dark corridor — Sector 7-South. Next to it, a small notation in Pax script: 'Luxa — solo route.' His expression shifts from boredom to recognition. Palette: cool blue map light on Jiggy's face, the dark sector glowing red, Luxa's name in soft gold script. Mood: the click, realization, purpose found. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-07-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate Jiggy with his hand on a crystal. This time the crystal emits a faint genuine jade glow #21D8B6. Jiggy's single eye widens. His mouth opens slightly. The crystal felt his intention. Behind him, an ancient temple mural is partially visible — warriors with crystals, each marked with a name. Palette: faint jade glow from crystal, warm amber from the mural, Jiggy's surprised face. Mood: breakthrough, hope. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-07-end.png"),
})

# --- Scene 08 — Jiggy + KZ ---
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Image 2 is the character reference for KZ. Generate a wide shot of Jiggy's alcove — CHAOS. Left side: charging station with crystals. Right side: hammock with KZ (from Image 2) sleeping on it. Center: a table covered with food, exploration maps, a broken compass, crystal fragments, a half-drawn tunnel sketch. Jiggy (from Image 1) sits in the middle, hands on a crystal, trying to charge. His eye darts between every object. A map falls. Palette: warm mess — browns #5C4033, scattered jade and magenta fragments, too many colors competing. Mood: visual overwhelm. Maintaining exact character identities from references. {STYLE}",
    "input_image_paths": [JIGGY, KZ],
    "output_path": fp("scene-08-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Image 2 is the character reference for KZ. Generate a close-up on Jiggy's hands on a crystal — they glow for a second, then KZ (from Image 2) jumps on his shoulder. The glow dies instantly. Jiggy's expression: frustrated rage held in check. The crystal goes dark. Food wrapper falls into his lap from a table. Everything in this space competes for his attention. Palette: dead crystal grey, KZ's lime glow intruding, Jiggy's clenched jaw. Mood: sabotage by environment. Maintaining exact character identities from references. {STYLE}",
    "input_image_paths": [JIGGY, KZ],
    "output_path": fp("scene-08-end.png"),
})

# --- Scene 09 — Jiggy (main hall, others in bg) ---
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate the main hall of the Uray Pacha — bustling. In the background, various Pax tribe members: one cyan-skinned Pax with a crystal boombox (visible sound waves as jade ripples), another dark basalt-skinned Pax hauling a massive mineral slab, two younger Pax chasing each other. Jiggy (from Image 1) in the foreground, trying to charge a crystal on a shared table. His eye twitches from the noise. Palette: cacophony of Pax colors — cyan, basalt-orange, magenta, jade — all competing. Mood: sensory overload. Maintaining Jiggy's exact identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-09-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate the scene from Jiggy's perspective. He looks up from his crystal (dead, no glow) and sees a tunnel entrance — deep, dark, quiet. The contrast between the noisy bright hall behind and the silent tunnel is stark. His body leans toward the tunnel. Decision forming. Palette: bright chaotic hall behind, dark inviting tunnel ahead, Jiggy silhouetted between. Mood: escape toward clarity. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-09-end.png"),
})

# --- Scene 10 — Jiggy ---
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate Jiggy in a forgotten chamber deep in the east tunnels. Small, low ceiling, smooth basalt walls. One natural crystal mount in the center — ancient, dust-covered. Jiggy brushes dust off with his hand. A puff of mineral dust catches light. The room is austere, clean, QUIET. No decorations. No distractions. Just stone and silence. Palette: monochrome basalt #3D3D3D with a single jade crystal mount #21D8B6 emerging from the dust. Mood: sanctuary, potential, sacred emptiness. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-10-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate the same sacred chamber, days later. The dust is gone. The crystal mount gleams. Jiggy sits before it, hands on crystal, and the glow is STRONGER than anything before — a steady jade pulse. His posture is upright, centered. His eye is calm. The chamber walls catch the crystal light and amplify it in gentle reflections. Above the door, barely visible: a carved ancient Pax glyph. Palette: jade glow #21D8B6 filling the room, Jiggy in silhouette, warm basalt reflections. Mood: the sacred space working. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-10-end.png"),
})

# --- Scene 11 — Jiggy ---
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate Jiggy's sacred chamber with SEVEN alchemical instruments on a table: a resonance tuner (tuning fork, amber glow), a crystal polisher (jade cloth on handle), a frequency diviner (spinning compass with crystal needle), a charge meter (vertical tube with floating particles), an alignment rod (thin, metallic), a stabilizing clamp (brass, mechanical), a purification cloth (iridescent weave). All neatly arranged. Jiggy (from Image 1) is polishing the polisher. Each tool glows its own color, creating a rainbow mess. The actual charging crystal sits center, DARK, ignored. Palette: amber, jade, brass, iridescent tools around a dead crystal center. Mood: ironic productivity, beautiful distraction. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-11-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate a tight shot on a dark crystal in the center of a table, surrounded by seven glowing alchemical tools. The crystal is the ONLY dark object in the scene. Visual metaphor: everything shines except the thing that matters. Jiggy's hands (from Image 1) are on a charge meter, reading numbers, NOT on the crystal. Palette: glowing tool ring around dead dark crystal center. Mood: the subtraction problem crystallized. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-11-end.png"),
})

# --- Scene 12 — Jiggy ---
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate Jiggy at night, standing at the entrance of his chamber, arms full of alchemical tools. He walks them to a storage cave — a natural shelf in the tunnel wall. He sets them down one by one. Each tool dims as it leaves his hands, as if it only had power when he held it. His expression: determined, slightly scared. Letting go of control. Palette: dim tunnel #2A2A2A, tools losing their glow as they're shelved, Jiggy's face lit only by the last tool's fading light. Mood: ritual sacrifice, letting go. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-12-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate Jiggy back in his chamber. Empty table. Empty hands. He sits. Places his bare palms on the crystal. His HANDS glow — jade light #21D8B6 bleeding from his palms into the crystal. The crystal responds with a deep warm pulse. No intermediaries. Direct connection. The chamber is austere, monastic. Palette: jade hand-glow, warm crystal pulse, dark minimal room. Mood: breakthrough through simplicity, the beauty of less. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-12-end.png"),
})

# --- Scene 13 — Wiz (young + elder) ---
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Wiz. Generate a flashback/memory scene: a younger version of Wiz (smaller, no beard, same amber skin but brighter, maintaining identity from Image 1) sitting beside an ancient elder Pax. The elder is ancient — deep amber, mineral striations in their skin like tree rings. They sit in a simple chamber — raw rock, one crystal, nothing else. The elder's bare hands glow gold on the crystal. No tools anywhere. Peaceful. Palette: warm amber #D4A017, gold glow, ancient stone, golden-hour lighting inside the earth. Mood: ancestral wisdom, simplicity as power. {STYLE}",
    "input_image_paths": [WIZ],
    "output_path": fp("scene-13-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Wiz. Generate the same scene: the elder Pax has turned to young Wiz (from Image 1, younger version without beard) and is smiling — a knowing gentle smile. The message is wordless: 'This is all you need.' The crystal between them is fully charged, blazing gold. Young Wiz's eye is wide with understanding. Palette: gold-saturated, warm, intimate. Mood: transmission of knowledge, master to student. {STYLE}",
    "input_image_paths": [WIZ],
    "output_path": fp("scene-13-end.png"),
})

# --- Scene 14 — Jiggy ---
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate Jiggy in his sacred chamber, late afternoon (bioluminescent moss shifts to warmer tones). He sits perfectly still. Hands on crystal. Clear target. Sacred space. No tools. But his body VIBRATES — visible tremor in his shoulders, his leg bouncing rapidly, his single eye darting. The crystal flickers but can't hold a charge. Energy radiating from his body like heat shimmer, visible as faint magenta distortion around his silhouette. Palette: warm afternoon tones, Jiggy's skin with magenta energy aura #FF49B4 flickering, unstable crystal glow. Mood: caged energy, frustration. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-14-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate an extreme close-up on Jiggy's hands on a crystal. They glow, stutter, glow, stutter — like a light with a bad connection. The energy can't flow smoothly. Between his fingers, tiny sparks of unused physical energy escape upward, wasted. His knuckles are white from pressing too hard. Palette: jade glow stuttering, magenta sparks escaping, dark crystal surface. Mood: the body-mind disconnect made visible. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-14-end.png"),
})

# --- Scene 15 — No characters (mural) ---
jobs.append({
    "type": "generate",
    "prompt": f"Temple mural carved and painted on stone. Depicts a sequence: ancient Pax beings (turquoise cyclops creatures) doing physical labor — hauling crystal formations through tunnels, carrying water vessels, climbing vertical shafts. Their bodies are in motion, muscles visible, expressions focused. The art style is ancient — simplified, symbolic, like Nazca lines meets Aztec codex. Each figure labeled with a Pax glyph. Palette: stone-carved tones — amber ochre, basalt grey, jade green inlay, flat ancient art style. Mood: instructional, ancestral, rhythmic. {STYLE}",
    "output_path": fp("scene-15-start.png"),
})
jobs.append({
    "type": "generate",
    "prompt": f"Second panel of a stone temple mural: AFTER physical labor, the same ancient Pax beings (turquoise cyclops creatures) sit before crystals. Now they are calm. Hands glow. Crystals blaze. The visual sequence is unmistakable — move FIRST, then charge. A carved phrase below in alien glyphs with subtle translation overlay: 'The mind follows the body's lead.' Palette: same ancient art style but the charging panel has added gold and jade glow to the carved figures. Mood: the answer was always here, written in stone. {STYLE}",
    "output_path": fp("scene-15-end.png"),
})

# --- Scene 16 — Jiggy ---
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate Jiggy sprinting through a tunnel. Not exploring — RUNNING. Arms pumping, legs driving, expression fierce and free. The tunnel walls blur past. Bioluminescent plants streak into light trails. Crystal veins in the walls flash as he passes. He's burning energy. Palette: motion blur — streaks of jade #21D8B6, magenta #FF49B4, amber #D4A017. Jiggy sharp in the center, everything else blurred with speed. Mood: release, primal movement, joyful exertion. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-16-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate Jiggy walking back into his sacred chamber. Breathing settling. He sits down. Hands on crystal. INSTANT glow — strong, steady, immediate. No stutter. No shimmer. Clean jade light. His body is calm and his mind follows. His expression: quiet surprise then acceptance. The chamber is lit by his charge, warm. Palette: steady jade glow, warm basalt catching light, Jiggy's calm face. Mood: earned focus, physical-mental harmony. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-16-end.png"),
})

# --- Scene 17 — Jiggy + KZ ---
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Generate: Tuesday morning. Jiggy enters his chamber. He's already run (slightly damp, breathing settled), the room is bare (no tools), the crystal mount is clean, and on the wall he's scratched a note — 'Sector 7-South / Luxa'. He sits. Hands on crystal. No hesitation. No ritual. Just action. His eye is half-closed, calm. Palette: morning tones — cooler blues and jades. Clean, minimal, intentional. Mood: routine mastery, the system working. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [JIGGY],
    "output_path": fp("scene-17-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Jiggy. Image 2 is the character reference for KZ. Generate: three hours later. SEVEN crystals glow on the mount. All fully charged. Jade, amber, magenta, gold — a spectrum of light fills the small chamber. Jiggy (from Image 1) looks up confused — it felt like five minutes. His expression is stunned then a slow grin. KZ (from Image 2) peeks through the door opening, sees the light show, and quietly backs away. Palette: FULL spectrum — jade #21D8B6, amber #D4A017, magenta #FF49B4, gold #FFD700 — all blazing. Jiggy's grinning face in the glow. Mood: triumph, effortless mastery, Mushin achieved. Maintaining exact character identities from references. {STYLE}",
    "input_image_paths": [JIGGY, KZ],
    "output_path": fp("scene-17-end.png"),
})

# --- Scene 18 — Start: Luxa (distant, no sheet needed), End: Wiz ---
jobs.append({
    "type": "generate",
    "prompt": f"Sector 7-South — an underground tunnel that was once dark, now lined with charged crystals glowing jade and amber. The corridor is beautiful — jade and amber light painting basalt walls in warm patterns. Water trickles along a channel in the floor catching crystal reflections. In the distance, a small purple-skinned cyclops figure walks through the light — safe, the tunnel bright around her. She doesn't know who charged these. Palette: jade and amber light corridor, purple silhouette #9B30FF, sparkling water reflections. Mood: quiet impact, the ripple effect of focused work. {STYLE}",
    "output_path": fp("scene-18-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Wiz. Generate Wiz in the main hall, standing before a crystalline node map on the wall. More sectors glow now. Sector 7-South: bright. Other sectors: charging. His hand rests on his staff. His expression: a small quiet smile. Not pride — recognition. He touches the map where work is visible and nods. The violet crystal on his staff pulses once, warm. Palette: Wiz's amber against the glowing blue-jade node map. More lit sectors than before. Mood: mentor's satisfaction, silent acknowledgment. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [WIZ],
    "output_path": fp("scene-18-end.png"),
})

# --- Scene 19 — Start: crystal (no chars), End: Wiz ---
jobs.append({
    "type": "generate",
    "prompt": f"Return to the same crystal from the opening shot — same angle, same void. But now it BLAZES. Jade, gold, magenta light pouring from it. The crack from the opening is still there — but light bleeds through the crack now, making it beautiful rather than broken. The crystal is alive. The pulse is strong and steady. Palette: jade #21D8B6, gold #FFD700, magenta #FF49B4 radiating from center, dark void around. Mood: resurrection, completion, the cycle closed. {STYLE}",
    "output_path": fp("scene-19-start.png"),
})
jobs.append({
    "type": "edit",
    "prompt": f"Image 1 is the character reference for Wiz. Generate Wiz in medium shot, dark background, lit only by his staff crystal. He looks directly at the viewer. His expression is calm, warm, challenging — 'Now you know. What will you do?' Behind him, barely visible, an ancient temple inscription glows: the final Pax glyph. Below frame: the Pax logo materializes in jade light. Subtitle text: 'What will you charge today?' Palette: Wiz amber, violet staff, jade logo, black background. Mood: call to action, quiet power. Maintaining exact character identity from Image 1. {STYLE}",
    "input_image_paths": [WIZ],
    "output_path": fp("scene-19-end.png"),
})

# --- THUMBNAIL ---
jobs.append({
    "type": "edit",
    "prompt": "Image 1 is the character reference for Jiggy. Generate a YouTube thumbnail: Jiggy looking intensely focused with a glowing crystal held in both hands near his face, dramatic lighting with strong amber and basalt contrast, cinematic close-up shot. The crystal blazes jade and gold light that illuminates his face from below. His single cyclops eye is intense, determined. Bold text overlay: 'FOCUS LIKE A PAX' in thick white letters with jade glow outline. Dark moody background with faint crystal formations. 3D PBR render, stylized animation, hyper-dramatic lighting, YouTube thumbnail style — bold, clickable, high contrast. The image should feel dramatic and clickable.",
    "input_image_paths": [JIGGY],
    "output_path": os.path.join(REPO, "gestos", "_backlog", "video-educativo", "thumbnail.png"),
    "size": "1536x1024",  # 16:9 for YT thumbnail
})


# -----------------------------------------------------------------------
# Execute
# -----------------------------------------------------------------------
async def main():
    client_async = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
    sem = asyncio.Semaphore(5)  # conservative to avoid rate limits

    results = []
    total = len(jobs)

    async def run_job(idx, job):
        async with sem:
            name = os.path.basename(job["output_path"])
            print(f"[{idx+1}/{total}] Generating {name}...")
            try:
                if job["type"] == "generate":
                    # Use sync generate_image in executor
                    loop = asyncio.get_event_loop()
                    result = await loop.run_in_executor(
                        None,
                        lambda: generate_image(
                            prompt=job["prompt"],
                            output_path=job["output_path"],
                            size=job.get("size", SIZE),
                            quality="medium",
                        )
                    )
                else:
                    result = await edit_image_async(
                        client_async=client_async,
                        prompt=job["prompt"],
                        input_image_paths=job["input_image_paths"],
                        output_path=job["output_path"],
                        size=job.get("size", SIZE),
                        quality="medium",
                    )
                print(f"  OK: {name}")
                return result
            except Exception as e:
                print(f"  ERROR {name}: {e}")
                return e

    tasks = [run_job(i, j) for i, j in enumerate(jobs)]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Summary
    ok = sum(1 for r in results if not isinstance(r, Exception))
    fail = sum(1 for r in results if isinstance(r, Exception))
    print(f"\nDone: {ok} OK, {fail} failed out of {total}")

    if fail > 0:
        print("\nFailed jobs:")
        for i, r in enumerate(results):
            if isinstance(r, Exception):
                print(f"  {os.path.basename(jobs[i]['output_path'])}: {r}")

if __name__ == "__main__":
    asyncio.run(main())
