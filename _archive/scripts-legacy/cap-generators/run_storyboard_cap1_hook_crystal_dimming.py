"""Storyboard Cap 1 — Hook 0:08. Cristal magenta apagándose, Wiz observa."""

from openai_images import edit_image

PROMPT = """
[IDENTITY LOCK]
The character in this scene is Wiz, an elder Pax — a non-human, subterranean cyclops-type single-eyed humanoid species, NOT human, NOT generic fantasy wizard, NOT Andean indigenous shaman. Wiz visually MUST match Image 1 (his canonical reference): cyclops-type single-eyed humanoid with ONE central eye (no second eye, no companion eye, no extra eye anywhere on the face), turquoise-teal slightly weathered skin, elongated pointed elastic ears, FOUR fingers per hand (not five), 2.8-3-head old-stocky proportions, long voluminous white beard from below the eye to chest, thick white tufted brow above the single eye, deep purple velvet hooded robe (#3D2A66 / #4B2E80) with subtle turquoise rune trim, central chest medallion with small violet crystal, dark wooden staff topped with a glowing magenta-violet crystal. Repeat: ONE central eye, cyclops-type anatomy, no second eye. He is a peer/elder of the same Pax species shown in Image 4 (jiggy.png) — same skin tone, same four-fingered hands, same elastic pointed ears, same proportional language.

[SUBJECT]
Hook 0:08 of Episode 1. Tight foreground close-up of a magenta crystal (#E83FC8 rim, #FF49B4 core) growing from the cavern floor in vertical orientation, faceted glassy surface with a hairline cooling crack visible, internal subsurface emission visibly LATING / pulsing slow — caught at the precise moment its light is dimming, the magenta glow noticeably weaker than the other crystals around it, with a subtle pale-cyan #7FFFD4 ghost-light flickering subliminally inside it. In the mid-ground, slightly out of focus, Wiz stands looking down at the crystal with his single central eye half-closed in concern, his weathered turquoise hand resting near the crystal, his staff with its still-glowing magenta-violet crystal-tip held in the other hand. His expression is grave, contemplative, paternal — not panicked. Behind him, blurred and deeper in the cavern, several other crystals can be seen, some bright and pulsing healthy magenta, two or three visibly dimmer, opaque, dying.

[COMPOSITION]
Vertical 1024x1536 portrait orientation, low angle from below the dimming crystal looking slightly upward past it toward Wiz. Foreground: dimming crystal hero element occupying the lower-left third (rule of thirds). Mid-ground: Wiz in 3/4 medium framing, head and shoulders visible upper-right third, slightly out of focus to keep the crystal as anchor. Background: deep purple basalt cavern walls (#0E0820 / #4B2E80) with bokeh of distant magenta crystals. Headroom above Wiz reserved for possible subtitle overlay. Leading lines from cavern stalagmites converge toward the dying crystal.

[LIGHT + PALETTE]
Stylized 3D PBR semi-realistic shading with subsurface scattering on Wiz's turquoise skin and the crystal interior. Primary key light: the magenta emission from the dimming crystal itself, weak and faltering, casting soft magenta rim light upward across Wiz's beard and lower face. Secondary fill: distant healthy magenta crystals casting cool fill across the cavern walls. Cool turquoise atmospheric fill from above. Dense volumetric haze with floating dust motes catching the magenta glow. Bloom moderate on the dying crystal — fading. Slight pale-cyan #7FFFD4 ghost flicker inside the dying crystal. Palette dominated by jade-magenta-basalt with deep purple shadows. NO warm tungsten, NO surface daylight.

[STYLE / RENDER]
Stylized 3D animation render, premium mobile-game cinematic / animated key art quality, semi-realistic PBR materials, slight film grain, 16:9-equivalent vertical 1024x1536 storyboard frame. NOT 2D, NOT painterly, NOT illustration, NOT anime, NOT photorealistic, NOT cel-shaded flat, NOT Pixar/Disney generic family-feature look, NOT thriller-grade vignetting.

[REFERENCE INTEGRATION]
Image 1 (wiz.png) establishes IDENTITY LOCK for Wiz — match his cyclops single-eyed anatomy, beard volume, robe design, staff, and proportions exactly. Image 2 (concept-cave-stalagmites-reawakening.png) establishes the cavern setting — match the cavern wall material, crystal formation language, and atmospheric volumetric quality. Image 3 (concept-cave-wide-dark.png) anchors deep-cavern darkness and basalt palette. Image 4 (portada.png) anchors render base and overall Pax visual DNA. Apply the canonical Pax palette: jade-green, warm-amber (avoided here — cavern only), basalt-dark, neon-magenta dominant.

[NEGATIVE]
Do not include: human anatomy with two eyes (Wiz has ONE central cyclops eye), a second smaller eye anywhere on the face, generic Gandalf-style wizard, generic Andean indigenous costume, 2D hand-drawn aesthetic, painterly Studio Ghibli style, photorealistic skin, five-fingered hands, anime stylization, cel-shaded flat coloring, Pixar/Disney generic look, fantasy battle clichés, magic circles, glowing portals, lightning bolts, runes floating in air, accessories not present in Image 1 (no extra jewelry, no bandanas, no gems on forehead, no goggles, no helmet), HUD overlays, game UI, gem counters, health bars, twentieth-century human references, fully bright cavern (it must read dim and dying), warm tungsten light (this is pure subterranean cavern), surface daylight.
""".strip()

result = edit_image(
    prompt=PROMPT,
    input_image_paths=[
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\wiz.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-cave-stalagmites-reawakening.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-cave-wide-dark.png",
        r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada.png",
    ],
    output_path=r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os\content\storyboards\cap-1-hook-crystal-dimming.png",
    size="1024x1536",
    quality="medium",
)
print(f"OK cap-1-hook-crystal-dimming -> {result}")
