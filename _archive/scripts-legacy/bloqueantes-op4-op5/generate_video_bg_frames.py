"""
Bulk video-bg frames generator — 2 videos x 17 frames x 2 ratios = 68 imagenes.

Source: content/video-bg/video{1-deep-dive,2-gem-chase}/_storyboard.md
Output: content/video-bg/video{1-deep-dive,2-gem-chase}/{16x9,9x16}/frame-NN.png

- GPT Image 2, quality=high.
- Skip-if-exists (>50KB).
- Retry once on failure (incluido moderation_blocked).
- Concurrency=4 via Semaphore.
- Verbose print con timestamp HH:MM:SS por cada OK/SKIP/FAIL.
"""

import os
import sys
import time
import asyncio
import base64
from openai import AsyncOpenAI

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openai_images import _load_env  # noqa: E402
_load_env()

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = "gpt-image-2"
CONCURRENCY = 4
QUALITY = "high"

# Aspect ratios soportados por GPT Image 2
SIZES = {
    "16x9": "1536x1024",
    "9x16": "1024x1536",
}

# Refs canonicas
JIGGY_REF = os.path.join(REPO, "personajes finales", "Jiggy_Character.png")


# ---------------------------------------------------------------------------
# VIDEO 1 — Deep dive into Pax world (17 frames, sin personajes hasta frame 13)
# ---------------------------------------------------------------------------

VIDEO1 = {
    "frame-00": {
        "prompt": (
            "Extreme macro close-up of a single dew droplet hanging from the curved edge of a "
            "glossy green leaf at dawn. The droplet is hyper-sharp with crystalline clarity, "
            "reflecting a miniature inverted sky inside. Soft golden rim light from behind, "
            "cool cyan key light from above-left, ultra shallow depth of field with creamy "
            "bokeh of a pastel cyan and rose dawn sky in background. Visible suspended "
            "particles of pollen and dust catching sunlight rays. Stylized 3D animation, "
            "smooth shading, painterly background, soft subsurface scattering on the leaf, "
            "cinematic warm-cool lighting contrast. No text, no logos. Aspect ratio variant "
            "16:9 OR 9:16: same composition, droplet always centered, only background "
            "framing adjusts."
        ),
        "refs": [],
    },
    "frame-01": {
        "prompt": (
            "Hyper-realistic stylized 3D close-up of the interior surface of a water droplet, "
            "the camera pushing through its curved skin. Refracted caustic light patterns "
            "dance across the frame in cool cyan and silver tones. Microscopic particles "
            "suspended inside the water glow softly. The boundary between water and air "
            "shimmers. Painterly stylized 3D animation, dreamy atmospheric quality, soft "
            "volumetric light rays. No characters, no text, no logos. Works for both 16:9 "
            "and 9:16: composition is radially symmetric around the center."
        ),
        "refs": [],
    },
    "frame-02": {
        "prompt": {
            "16x9": (
                "Wide angle 24mm tilted aerial top-down view descending through a dense forest "
                "canopy. Strong volumetric god rays of warm green-gold sunlight pierce through "
                "gaps in the leaves at diagonal angles. Branches and leaves rush past the edges "
                "of the frame with motion blur, suggesting fast downward camera movement. "
                "Floating pollen and dust particles glow in the light shafts. Painterly "
                "stylized 3D animation, lush organic textures, cinematic depth, no characters, "
                "no text, no logos. 16:9 composition: horizontal canopy spread."
            ),
            "9x16": (
                "Wide angle 24mm tilted aerial top-down view descending through a dense forest "
                "canopy. Strong volumetric god rays of warm green-gold sunlight pierce through "
                "gaps in the leaves at diagonal angles. Branches and leaves rush past the edges "
                "of the frame with motion blur, suggesting fast downward camera movement. "
                "Floating pollen and dust particles glow in the light shafts. Painterly "
                "stylized 3D animation, lush organic textures, cinematic depth, no characters, "
                "no text, no logos. 9:16 composition: vertical tunnel of branches framing the "
                "center."
            ),
        },
        "refs": [],
    },
    "frame-03": {
        "prompt": {
            "16x9": (
                "Wide angle low descending shot over a mossy forest floor with thick gnarled "
                "roots forming a radial pattern that leads the eye to a central dark crack in "
                "the earth. Tiny bioluminescent mushrooms with subtle pink-cyan glow nestle "
                "between the roots, hinting at a hidden world below. Warm-cool lighting: green "
                "moss fill light with golden top light from canopy and deep shadows inside the "
                "central crack. Painterly stylized 3D animation, rich organic detail, soft "
                "subsurface scattering on moss and mushrooms. No characters, no text, no "
                "logos. 16:9 horizontal root spread."
            ),
            "9x16": (
                "Wide angle low descending shot over a mossy forest floor with thick gnarled "
                "roots forming a radial pattern that leads the eye to a central dark crack in "
                "the earth. Tiny bioluminescent mushrooms with subtle pink-cyan glow nestle "
                "between the roots, hinting at a hidden world below. Warm-cool lighting: green "
                "moss fill light with golden top light from canopy and deep shadows inside the "
                "central crack. Painterly stylized 3D animation, rich organic detail, soft "
                "subsurface scattering on moss and mushrooms. No characters, no text, no "
                "logos. 9:16 vertical descent emphasis."
            ),
        },
        "refs": [],
    },
    "frame-04": {
        "prompt": {
            "16x9": (
                "Plunging first-person vertical descent shot through a tunnel of dark earth "
                "and protruding roots. The camera falls down a natural opening in the ground; "
                "walls rush past the edges of the frame with strong parallax. Top of the frame "
                "fades from green forest canopy light into warm amber tones emerging from "
                "below. Tumbling pebbles and dust particles fall alongside. Painterly stylized "
                "3D animation, dramatic vertical motion blur, cinematic chiaroscuro. No "
                "characters, no text, no logos. 16:9 frame widens the tunnel walls "
                "horizontally."
            ),
            "9x16": (
                "Plunging first-person vertical descent shot through a tunnel of dark earth "
                "and protruding roots. The camera falls down a natural opening in the ground; "
                "walls rush past the edges of the frame with strong parallax. Top of the frame "
                "fades from green forest canopy light into warm amber tones emerging from "
                "below. Tumbling pebbles and dust particles fall alongside. Painterly stylized "
                "3D animation, dramatic vertical motion blur, cinematic chiaroscuro. No "
                "characters, no text, no logos. 9:16 emphasizes vertical drop length."
            ),
        },
        "refs": [],
    },
    "frame-05": {
        "prompt": {
            "16x9": (
                "Continuing vertical descent past horizontal geological strata: layers of "
                "amber, ocre, deep red and dark brown rock with visible stratification. Tiny "
                "embedded semiprecious stones in the walls catch the light and begin to softly "
                "glow. Warm amber key light from below, fading cyan rim from above. Painterly "
                "stylized 3D animation, rich mineral textures, dramatic depth, cinematic "
                "warm-cool gradient. No characters, no text, no logos. 16:9 widens horizontal "
                "strata."
            ),
            "9x16": (
                "Continuing vertical descent past horizontal geological strata: layers of "
                "amber, ocre, deep red and dark brown rock with visible stratification. Tiny "
                "embedded semiprecious stones in the walls catch the light and begin to softly "
                "glow. Warm amber key light from below, fading cyan rim from above. Painterly "
                "stylized 3D animation, rich mineral textures, dramatic depth, cinematic "
                "warm-cool gradient. No characters, no text, no logos. 9:16 emphasizes "
                "vertical layering."
            ),
        },
        "refs": [],
    },
    "frame-06": {
        "prompt": {
            "16x9": (
                "Wide cinematic view of the descent opening into a vast natural cavern. "
                "Stalactites hang from the ceiling, stalagmites rise from the floor, walls "
                "show early veins of glowing magenta-pink crystal embedded in dark rock. "
                "Ambient warm amber light fills the space; sparkles of crystal bioluminescence "
                "dot the walls. Painterly stylized 3D animation, dramatic scale, "
                "cathedral-like atmosphere, soft volumetric light rays. No characters, no "
                "text, no logos. 16:9 emphasizes horizontal cavern breadth."
            ),
            "9x16": (
                "Wide cinematic view of the descent opening into a vast natural cavern. "
                "Stalactites hang from the ceiling, stalagmites rise from the floor, walls "
                "show early veins of glowing magenta-pink crystal embedded in dark rock. "
                "Ambient warm amber light fills the space; sparkles of crystal bioluminescence "
                "dot the walls. Painterly stylized 3D animation, dramatic scale, "
                "cathedral-like atmosphere, soft volumetric light rays. No characters, no "
                "text, no logos. 9:16 emphasizes vertical cathedral height."
            ),
        },
        "refs": [],
    },
    "frame-07": {
        "prompt": {
            "16x9": (
                "Close tracking shot brushing past a cavern wall densely packed with veins of "
                "magenta-pink bioluminescent crystal. The crystal pulses with internal light, "
                "soft subsurface scattering visible. Foreground crystal formations crisp, "
                "background sliding past with subtle motion blur. The crystal light itself is "
                "the primary illumination source, casting rose-tinted reflections on adjacent "
                "rock. Painterly stylized 3D animation, jewel-like detail, cinematic "
                "magic-realism. No characters, no text, no logos. 16:9 emphasizes horizontal "
                "sweep."
            ),
            "9x16": (
                "Close tracking shot brushing past a cavern wall densely packed with veins of "
                "magenta-pink bioluminescent crystal. The crystal pulses with internal light, "
                "soft subsurface scattering visible. Foreground crystal formations crisp, "
                "background sliding past with subtle motion blur. The crystal light itself is "
                "the primary illumination source, casting rose-tinted reflections on adjacent "
                "rock. Painterly stylized 3D animation, jewel-like detail, cinematic "
                "magic-realism. No characters, no text, no logos. 9:16 emphasizes vertical "
                "column of crystal."
            ),
        },
        "refs": [],
    },
    "frame-08": {
        "prompt": {
            "16x9": (
                "Wide 18mm shot emerging from a dark crystal-lined corridor into a vast open "
                "space. Foreground: dark silhouetted natural arch of crystal formations "
                "framing the view. Background: blurred glimpse of a magical underground world "
                "with giant crystal pillars, amber-jade bioluminescence, and soft volumetric "
                "light. Strong depth layering. Painterly stylized 3D animation, cinematic "
                "threshold moment, awe and discovery atmosphere. No characters, no text, no "
                "logos. 16:9 wide reveal."
            ),
            "9x16": (
                "Wide 18mm shot emerging from a dark crystal-lined corridor into a vast open "
                "space. Foreground: dark silhouetted natural arch of crystal formations "
                "framing the view. Background: blurred glimpse of a magical underground world "
                "with giant crystal pillars, amber-jade bioluminescence, and soft volumetric "
                "light. Strong depth layering. Painterly stylized 3D animation, cinematic "
                "threshold moment, awe and discovery atmosphere. No characters, no text, no "
                "logos. 9:16 framed by vertical archway."
            ),
        },
        "refs": [],
    },
    "frame-09": {
        "prompt": {
            "16x9": (
                "Vast wide establishing shot of an underground magical world: giant "
                "magenta-pink crystal pillars rising hundreds of meters, jade-amber organic "
                "formations, a still reflective subterranean lake in the foreground, floating "
                "bioluminescent particles in the air. Mixed ambient jade-amber and magenta "
                "crystal accent lighting, soft volumetric god rays from hidden upper sources. "
                "Painterly stylized 3D animation, epic scale, cathedral-of-nature atmosphere, "
                "magic-realism. No characters in this shot, focus on world reveal. No text, "
                "no logos. 16:9 horizontal panorama."
            ),
            "9x16": (
                "Vast wide establishing shot of an underground magical world: giant "
                "magenta-pink crystal pillars rising hundreds of meters, jade-amber organic "
                "formations, a still reflective subterranean lake in the foreground, floating "
                "bioluminescent particles in the air. Mixed ambient jade-amber and magenta "
                "crystal accent lighting, soft volumetric god rays from hidden upper sources. "
                "Painterly stylized 3D animation, epic scale, cathedral-of-nature atmosphere, "
                "magic-realism. No characters in this shot, focus on world reveal. No text, "
                "no logos. 9:16 vertical cathedral emphasis."
            ),
        },
        "refs": [],
    },
    "frame-10": {
        "prompt": {
            "16x9": (
                "Smooth drone-like exploration shot weaving between floating crystal islands "
                "suspended mid-air, connected by glowing bridges of light and magical roots. "
                "Foreground island sharp, background islands receding with atmospheric haze. "
                "Golden-jade rim light from below, magenta crystal accents. Distant tiny "
                "bioluminescent insects drifting like fireflies. Painterly stylized 3D "
                "animation, epic floating archipelago atmosphere, fantasy-grounded. No "
                "characters, no text, no logos. 16:9 horizontal sweep across islands."
            ),
            "9x16": (
                "Smooth drone-like exploration shot weaving between floating crystal islands "
                "suspended mid-air, connected by glowing bridges of light and magical roots. "
                "Foreground island sharp, background islands receding with atmospheric haze. "
                "Golden-jade rim light from below, magenta crystal accents. Distant tiny "
                "bioluminescent insects drifting like fireflies. Painterly stylized 3D "
                "animation, epic floating archipelago atmosphere, fantasy-grounded. No "
                "characters, no text, no logos. 9:16 vertical stacking of islands."
            ),
        },
        "refs": [],
    },
    "frame-11": {
        "prompt": (
            "Centered architectural shot of a massive central crystal altar in the heart of "
            "an underground magical world, beams of golden-jade light emanating outward. "
            "Around its base, faint tiny silhouetted figures suggesting inhabitants at extreme "
            "distance. Surrounding cavern is darker; all illumination radiates from the "
            "central feature. Painterly stylized 3D animation, sacred cathedral atmosphere, "
            "epic centerpiece, mystery. No characters in detail, only distant silhouettes. No "
            "text, no logos. Composition radially symmetric: works for 16:9 wide centered and "
            "9:16 tall centered."
        ),
        "refs": [],
    },
    "frame-12": {
        "prompt": {
            "16x9": (
                "Medium-long shot, slight low angle, of a small community of 3 to 5 small "
                "humanoid one-eyed cyclops creatures gathered near the base of a glowing "
                "crystal altar in a vast underground cavern. Each figure has a single central "
                "round eye, jade-green skin tones, tribal cloth and feather accessories, "
                "short stocky stylized proportions. Backlit by magenta crystal glow, soft "
                "warm key from the altar. Painterly stylized 3D animation, "
                "intimate-community atmosphere, magical realism. Silhouettes more than full "
                "detail, characters as gentle reveal. No text, no logos. 16:9 horizontal "
                "grouping."
            ),
            "9x16": (
                "Medium-long shot, slight low angle, of a small community of 3 to 5 small "
                "humanoid one-eyed cyclops creatures gathered near the base of a glowing "
                "crystal altar in a vast underground cavern. Each figure has a single central "
                "round eye, jade-green skin tones, tribal cloth and feather accessories, "
                "short stocky stylized proportions. Backlit by magenta crystal glow, soft "
                "warm key from the altar. Painterly stylized 3D animation, "
                "intimate-community atmosphere, magical realism. Silhouettes more than full "
                "detail, characters as gentle reveal. No text, no logos. 9:16 stacked "
                "grouping."
            ),
        },
        "refs": [],
    },
    "frame-13": {
        "prompt": {
            "16x9": (
                "Medium 50mm shot of a small jade-green cyclops creature with one large "
                "central round eye (purple iris), wearing a purple tribal headband with "
                "embroidered patterns, dreadlock hair, a small pink crystal pendant on a "
                "leather strap across the chest, tribal cloth wrap around waist, pointed "
                "elf-like ears. Character stands in foreground-left, turning slightly toward "
                "camera with a soft curious expression. Background: blurred bokeh of more "
                "cyclops figures gathered near a glowing altar. Magenta crystal rim light on "
                "left side, warm amber key light on right, soft subsurface scattering on jade "
                "skin. Painterly stylized 3D animation, character-introduction warmth, "
                "Pixar-quality NOT named, soft cinematic lighting. Identity lock: one single "
                "central eye, no second eye. No text, no logos. 16:9 character left of "
                "center."
            ),
            "9x16": (
                "Medium 50mm shot of a small jade-green cyclops creature with one large "
                "central round eye (purple iris), wearing a purple tribal headband with "
                "embroidered patterns, dreadlock hair, a small pink crystal pendant on a "
                "leather strap across the chest, tribal cloth wrap around waist, pointed "
                "elf-like ears. Character stands in foreground-lower-center, turning slightly "
                "toward camera with a soft curious expression. Background: blurred bokeh of "
                "more cyclops figures gathered near a glowing altar. Magenta crystal rim "
                "light on left side, warm amber key light on right, soft subsurface "
                "scattering on jade skin. Painterly stylized 3D animation, "
                "character-introduction warmth, Pixar-quality NOT named, soft cinematic "
                "lighting. Identity lock: one single central eye, no second eye. No text, no "
                "logos. 9:16 character lower-center."
            ),
        },
        "refs": [JIGGY_REF],
    },
    "frame-14": {
        "prompt": {
            "16x9": (
                "Epic wide establishing shot from slight high angle of a small Pax community "
                "of 5 to 8 jade-skinned cyclops creatures gathered around a glowing magenta "
                "crystal altar at the floor of a vast cathedral-scale underground world. "
                "Floating crystal islands above, giant crystal pillars rising on the sides. "
                "Pax figures small in frame, world overwhelming. Mixed lighting: magenta "
                "crystal accents, golden-jade ambient, warm altar glow. Painterly stylized 3D "
                "animation, awe-inspiring cathedral-of-nature reveal, magical realism. Each "
                "character has one single central eye consistent with Pax anatomy. No text, "
                "no logos. 16:9 horizontal panorama."
            ),
            "9x16": (
                "Epic wide establishing shot from slight high angle of a small Pax community "
                "of 5 to 8 jade-skinned cyclops creatures gathered around a glowing magenta "
                "crystal altar at the floor of a vast cathedral-scale underground world. "
                "Floating crystal islands above, giant crystal pillars rising on the sides. "
                "Pax figures small in frame, world overwhelming. Mixed lighting: magenta "
                "crystal accents, golden-jade ambient, warm altar glow. Painterly stylized 3D "
                "animation, awe-inspiring cathedral-of-nature reveal, magical realism. Each "
                "character has one single central eye consistent with Pax anatomy. No text, "
                "no logos. 9:16 vertical scale emphasis with world towering."
            ),
        },
        "refs": [],
    },
    "frame-15": {
        "prompt": {
            "16x9": (
                "Final hero key-art: slight high angle wide of the Pax community gathered "
                "around the glowing crystal altar in the vast underground cathedral world. In "
                "the immediate foreground, a single large luminous bioluminescent particle "
                "floats prominently, glowing soft white-magenta, slightly out of focus, "
                "dominating the lower-third of frame and inviting eye to focal point. "
                "Background: same epic scale as before. Lighting: cinematic mixed "
                "magenta-jade-amber with subtle bloom. Painterly stylized 3D animation, "
                "satisfying conclusive yet inviting atmosphere, sets up loop. Each Pax has "
                "one single central eye. No text, no logos. 16:9 particle lower-third."
            ),
            "9x16": (
                "Final hero key-art: slight high angle wide of the Pax community gathered "
                "around the glowing crystal altar in the vast underground cathedral world. In "
                "the immediate foreground, a single large luminous bioluminescent particle "
                "floats prominently, glowing soft white-magenta, slightly out of focus, "
                "dominating the lower-center of frame and inviting eye to focal point. "
                "Background: same epic scale as before. Lighting: cinematic mixed "
                "magenta-jade-amber with subtle bloom. Painterly stylized 3D animation, "
                "satisfying conclusive yet inviting atmosphere, sets up loop. Each Pax has "
                "one single central eye. No text, no logos. 9:16 particle lower-center, "
                "world above."
            ),
        },
        "refs": [],
    },
    "frame-16": {
        "prompt": (
            "Final polished hero key-art for marketing and loop seam: vast underground Pax "
            "world with community of cyclops creatures gathered around glowing magenta "
            "crystal altar. Foreground floating bioluminescent particle prominently glowing "
            "white-magenta. Slight high angle wide composition. Full Pixar-quality NOT named "
            "cinematic painterly stylized 3D animation, rich magical realism, deep field, "
            "cathedral lighting, color grading final with magenta-jade-amber palette, subtle "
            "bloom and atmosphere haze. Single-eye Pax anatomy on all characters. No text, "
            "no logos. Designed for 16:9 and 9:16 dual delivery."
        ),
        "refs": [],
    },
}


# ---------------------------------------------------------------------------
# VIDEO 2 — Gem macro to Subway Surfers chase (17 frames, Jiggy en 4-13 + 16)
# ---------------------------------------------------------------------------

VIDEO2 = {
    "frame-00": {
        "prompt": (
            "Extreme macro 100mm shot of a single rose-magenta crystal gemstone floating "
            "against pure black void. The gem fills 70% of the frame, hyper-sharp detail of "
            "geometric facets, intense internal bioluminescent glow pulsing from a bright "
            "magenta-white core. Visible micro-particles suspended inside the crystal. Strong "
            "subsurface scattering, soft outer bloom halo radiating rose-magenta. The gem is "
            "its own light source. Painterly stylized 3D animation, jewel-like ultra-detail, "
            "dramatic chiaroscuro, magic-realism. Composition radially symmetric: works "
            "identical for 16:9 and 9:16, the gem always centered."
        ),
        "refs": [],
    },
    "frame-01": {
        "prompt": (
            "Continuation of the extreme macro shot: the same rose-magenta crystal gemstone "
            "rotated slightly to reveal new facets. Internal bioluminescent core pulses "
            "brighter, larger bloom halo, micro-particles inside the gem now visibly "
            "drifting. Still pure black void background. Subtle camera-breathing zoom of 1mm "
            "push-in. Painterly stylized 3D animation, increasing magical intensity, "
            "ultra-detailed crystal facets. Composition centered, works for 16:9 and 9:16."
        ),
        "refs": [],
    },
    "frame-02": {
        "prompt": {
            "16x9": (
                "Medium macro pull-back shot: the rose-magenta crystal gemstone now rests on "
                "a natural organic stone pedestal at frame center, occupying about 40% of the "
                "image. The gem is still the primary light source, casting magenta tinted "
                "illumination onto the pedestal and immediate surroundings. Background "
                "transitions from pure black void to dark cave tones with subtle ambient "
                "texture. Floating ambient dust particles visible in the gem light. Painterly "
                "stylized 3D animation, cinematic emerging-context, sense of discovery. 16:9 "
                "horizontal pedestal framing."
            ),
            "9x16": (
                "Medium macro pull-back shot: the rose-magenta crystal gemstone now rests on "
                "a natural organic stone pedestal at frame center, occupying about 40% of the "
                "image. The gem is still the primary light source, casting magenta tinted "
                "illumination onto the pedestal and immediate surroundings. Background "
                "transitions from pure black void to dark cave tones with subtle ambient "
                "texture. Floating ambient dust particles visible in the gem light. Painterly "
                "stylized 3D animation, cinematic emerging-context, sense of discovery. 9:16 "
                "vertical pedestal with the gem in upper-third."
            ),
        },
        "refs": [],
    },
    "frame-03": {
        "prompt": {
            "16x9": (
                "Continuing pull-back: the rose-magenta crystal gemstone on its stone "
                "pedestal now visible within a small Pax cave gallery. Mid-distance walls "
                "show veins of bioluminescent crystal and organic textures. Ambient "
                "jade-amber fill light emerging from off-frame, the gem still the brightest "
                "source. Depth layers: foreground pedestal, midground gem, background cave "
                "walls. Painterly stylized 3D animation, cinematic depth, magical realism "
                "atmosphere. 16:9 wide tunnel framing."
            ),
            "9x16": (
                "Continuing pull-back: the rose-magenta crystal gemstone on its stone "
                "pedestal now visible within a small Pax cave gallery. Mid-distance walls "
                "show veins of bioluminescent crystal and organic textures. Ambient "
                "jade-amber fill light emerging from off-frame, the gem still the brightest "
                "source. Depth layers: foreground pedestal, midground gem, background cave "
                "walls. Painterly stylized 3D animation, cinematic depth, magical realism "
                "atmosphere. 9:16 vertical column emphasis with tunnel stretching upward."
            ),
        },
        "refs": [],
    },
    "frame-04": {
        "prompt": {
            "16x9": (
                "Same Pax cave gallery composition: the rose-magenta crystal gemstone on its "
                "stone pedestal at frame center. From the lower-right edge of the frame, a "
                "small jade-green hand with stubby cartoonish fingers enters slowly, palm "
                "facing up, approaching the gem. The hand wears a small tribal cloth "
                "wristband with embroidered patterns. Magenta rim light from the gem "
                "illuminates the fingers, cool jade ambient rim from behind. Hand in sharp "
                "focus, gem slightly defocused to lead the eye. Painterly stylized 3D "
                "animation, anticipation moment, character introduction via body part. "
                "Identity lock: jade-green skin tone, stylized stocky Pax proportions. No "
                "second hand visible. 16:9 hand from right."
            ),
            "9x16": (
                "Same Pax cave gallery composition: the rose-magenta crystal gemstone on its "
                "stone pedestal at frame center. From the bottom-right edge of the frame, a "
                "small jade-green hand with stubby cartoonish fingers enters slowly, palm "
                "facing up, approaching the gem. The hand wears a small tribal cloth "
                "wristband with embroidered patterns. Magenta rim light from the gem "
                "illuminates the fingers, cool jade ambient rim from behind. Hand in sharp "
                "focus, gem slightly defocused to lead the eye. Painterly stylized 3D "
                "animation, anticipation moment, character introduction via body part. "
                "Identity lock: jade-green skin tone, stylized stocky Pax proportions. No "
                "second hand visible. 9:16 hand from bottom-right."
            ),
        },
        "refs": [JIGGY_REF],
    },
    "frame-05": {
        "prompt": {
            "16x9": (
                "Close 50mm impact shot: the small jade-green Pax hand closes around the "
                "rose-magenta crystal gemstone in a firm grip. A bright magenta-white flare "
                "bursts from the gem at the moment of contact, flooding the frame with "
                "intense rose-magenta light. Foreground hand and gem crisp in focus. Behind, "
                "a soft out-of-focus hint of a Pax character face (one central eye, "
                "suggestive only). Bloom expansion radiating outward. Painterly stylized 3D "
                "animation, peak emotional impact, drop moment, intense bioluminescent flare. "
                "Identity lock: single jade-green hand, no second hand visible. No text, no "
                "logos. 16:9 horizontal flare spread."
            ),
            "9x16": (
                "Close 50mm impact shot: the small jade-green Pax hand closes around the "
                "rose-magenta crystal gemstone in a firm grip. A bright magenta-white flare "
                "bursts from the gem at the moment of contact, flooding the frame with "
                "intense rose-magenta light. Foreground hand and gem crisp in focus. Behind, "
                "a soft out-of-focus hint of a Pax character face (one central eye, "
                "suggestive only). Bloom expansion radiating outward. Painterly stylized 3D "
                "animation, peak emotional impact, drop moment, intense bioluminescent flare. "
                "Identity lock: single jade-green hand, no second hand visible. No text, no "
                "logos. 9:16 vertical flare column."
            ),
        },
        "refs": [JIGGY_REF],
    },
    "frame-06": {
        "prompt": {
            "16x9": (
                "Wide 35mm drone chase-cam from slightly behind and above. Jiggy, a small "
                "jade-green cyclops Pax creature with one single central round eye (purple "
                "iris), purple tribal headband with embroidered patterns, dreadlock hair, "
                "pink crystal pendant on leather strap across chest, tribal cloth wrap, "
                "pointed elf-like ears, runs forward energetically down a Pax cave tunnel. "
                "Centered in frame, viewed from behind and slightly above. Walls of the "
                "tunnel covered in magenta crystal veins glowing rim-light, jade-amber "
                "ambient key light, motion blur on the peripheral walls suggesting fast "
                "forward motion. Painterly stylized 3D animation, action-adventure energy, "
                "dynamic. Identity lock: one single central eye, no second eye, Pax cyclops "
                "anatomy. No text, no logos. 16:9 horizontal tunnel spread."
            ),
            "9x16": (
                "Wide 35mm drone chase-cam from slightly behind and above. Jiggy, a small "
                "jade-green cyclops Pax creature with one single central round eye (purple "
                "iris), purple tribal headband with embroidered patterns, dreadlock hair, "
                "pink crystal pendant on leather strap across chest, tribal cloth wrap, "
                "pointed elf-like ears, runs forward energetically down a Pax cave tunnel. "
                "Centered in frame, viewed from behind and slightly above. Walls of the "
                "tunnel covered in magenta crystal veins glowing rim-light, jade-amber "
                "ambient key light, motion blur on the peripheral walls suggesting fast "
                "forward motion. Painterly stylized 3D animation, action-adventure energy, "
                "dynamic. Identity lock: one single central eye, no second eye, Pax cyclops "
                "anatomy. No text, no logos. 9:16 vertical tunnel emphasizing depth ahead."
            ),
        },
        "refs": [JIGGY_REF],
    },
    "frame-07": {
        "prompt": {
            "16x9": (
                "Drone chase-cam tracking forward: Jiggy (jade-green cyclops with single "
                "central eye, purple headband, dreadlocks, pink crystal pendant, tribal "
                "cloth) runs forward through Pax cave tunnel, centered. A large rose-magenta "
                "crystal formation whip-passes through the right foreground with strong "
                "motion blur and parallax, emitting a bright magenta flash as it passes. "
                "Background tunnel continues to recede with crystal veins on walls. "
                "Painterly stylized 3D animation, peak chase energy, dynamic parallax, "
                "cinematic action. Identity lock: one central eye only. 16:9 crystal "
                "foreground right."
            ),
            "9x16": (
                "Drone chase-cam tracking forward: Jiggy (jade-green cyclops with single "
                "central eye, purple headband, dreadlocks, pink crystal pendant, tribal "
                "cloth) runs forward through Pax cave tunnel, centered. A large rose-magenta "
                "crystal formation whip-passes through the bottom-right foreground with "
                "strong motion blur and parallax, emitting a bright magenta flash as it "
                "passes. Background tunnel continues to recede with crystal veins on walls. "
                "Painterly stylized 3D animation, peak chase energy, dynamic parallax, "
                "cinematic action. Identity lock: one central eye only. 9:16 crystal "
                "foreground bottom-right."
            ),
        },
        "refs": [JIGGY_REF],
    },
    "frame-08": {
        "prompt": {
            "16x9": (
                "Drone chase-cam: Jiggy (small jade-green cyclops, single central round eye "
                "with purple iris, purple tribal headband, dreadlocks, pink crystal pendant "
                "on chest, tribal cloth wrap, pointed ears) glances briefly over his "
                "shoulder mid-run, looking back toward the camera. Subtle playful curious "
                "expression. Forward momentum preserved, tunnel continues to recede. Magenta "
                "rim from cave crystals lights his face, soft amber key on the side. "
                "Painterly stylized 3D animation, character moment within action, charm. "
                "Identity lock: one single central eye only, never two. No text, no logos. "
                "16:9 face quarter-turn."
            ),
            "9x16": (
                "Drone chase-cam: Jiggy (small jade-green cyclops, single central round eye "
                "with purple iris, purple tribal headband, dreadlocks, pink crystal pendant "
                "on chest, tribal cloth wrap, pointed ears) glances briefly over his "
                "shoulder mid-run, looking back toward the camera. Subtle playful curious "
                "expression. Forward momentum preserved, tunnel continues to recede. Magenta "
                "rim from cave crystals lights his face, soft amber key on the side. "
                "Painterly stylized 3D animation, character moment within action, charm. "
                "Identity lock: one single central eye only, never two. No text, no logos. "
                "9:16 face quarter-turn fitting vertical frame."
            ),
        },
        "refs": [JIGGY_REF],
    },
    "frame-09": {
        "prompt": {
            "16x9": (
                "Drone chase-cam slightly elevated: Jiggy in mid-air, having just jumped over "
                "a fallen magenta crystal log obstacle. Arms extended for balance, body "
                "arched dynamically, single central eye focused forward. Magenta crystal log "
                "below him, tunnel walls continuing behind. Dust particles kicked up from his "
                "takeoff. Key light catches him in air; rim magenta from crystals. Painterly "
                "stylized 3D animation, heroic action beat, energetic. Identity lock: "
                "jade-green skin, one single central eye, dreadlocks, purple headband, pink "
                "crystal pendant, tribal cloth. No text, no logos. 16:9 horizontal action "
                "spread."
            ),
            "9x16": (
                "Drone chase-cam slightly elevated: Jiggy in mid-air, having just jumped over "
                "a fallen magenta crystal log obstacle. Arms extended for balance, body "
                "arched dynamically, single central eye focused forward. Magenta crystal log "
                "below him, tunnel walls continuing behind. Dust particles kicked up from his "
                "takeoff. Key light catches him in air; rim magenta from crystals. Painterly "
                "stylized 3D animation, heroic action beat, energetic. Identity lock: "
                "jade-green skin, one single central eye, dreadlocks, purple headband, pink "
                "crystal pendant, tribal cloth. No text, no logos. 9:16 vertical arc "
                "emphasis."
            ),
        },
        "refs": [JIGGY_REF],
    },
    "frame-10": {
        "prompt": {
            "16x9": (
                "Drone chase-cam elevated: Jiggy continues running forward, the tunnel exit "
                "visible ahead as a brilliant opening into a vast cathedral-scale Pax "
                "underground space with jade-amber-magenta light. Last meters of tunnel walls "
                "frame the bright reveal. Strong contrast between dim tunnel and bright "
                "opening. Painterly stylized 3D animation, anticipation peak, threshold "
                "moment. Identity lock: Pax cyclops anatomy, single central eye, jade skin, "
                "dreadlocks, purple headband, pink pendant. No text, no logos. 16:9 "
                "horizontal exit spread."
            ),
            "9x16": (
                "Drone chase-cam elevated: Jiggy continues running forward, the tunnel exit "
                "visible ahead as a brilliant opening into a vast cathedral-scale Pax "
                "underground space with jade-amber-magenta light. Last meters of tunnel walls "
                "frame the bright reveal. Strong contrast between dim tunnel and bright "
                "opening. Painterly stylized 3D animation, anticipation peak, threshold "
                "moment. Identity lock: Pax cyclops anatomy, single central eye, jade skin, "
                "dreadlocks, purple headband, pink pendant. No text, no logos. 9:16 vertical "
                "exit emphasis with light beam."
            ),
        },
        "refs": [JIGGY_REF],
    },
    "frame-11": {
        "prompt": {
            "16x9": (
                "Drone chase-cam wide 24mm pull-back-and-up: Jiggy small in mid-frame, still "
                "running forward, now revealed within an epic cathedral-scale Pax underground "
                "cavern. Floating crystal islands suspended mid-air, giant magenta-rose "
                "crystal pillars rising hundreds of meters, jade-amber organic formations. "
                "Mixed bright ambient lighting. Painterly stylized 3D animation, cinematic "
                "epic reveal, scale impact. Identity lock: Jiggy retains single central eye, "
                "jade skin, dreadlocks, purple headband, pink pendant, tribal cloth - visible "
                "even at smaller frame size. No text, no logos. 16:9 horizontal cathedral "
                "spread."
            ),
            "9x16": (
                "Drone chase-cam wide 24mm pull-back-and-up: Jiggy small in mid-frame, still "
                "running forward, now revealed within an epic cathedral-scale Pax underground "
                "cavern. Floating crystal islands suspended mid-air, giant magenta-rose "
                "crystal pillars rising hundreds of meters, jade-amber organic formations. "
                "Mixed bright ambient lighting. Painterly stylized 3D animation, cinematic "
                "epic reveal, scale impact. Identity lock: Jiggy retains single central eye, "
                "jade skin, dreadlocks, purple headband, pink pendant, tribal cloth - visible "
                "even at smaller frame size. No text, no logos. 9:16 vertical cathedral "
                "emphasis."
            ),
        },
        "refs": [JIGGY_REF],
    },
    "frame-12": {
        "prompt": {
            "16x9": (
                "Drone chase-cam swooping back down close to Jiggy: small jade-green Pax "
                "cyclops with single central eye, purple headband, dreadlocks, pink crystal "
                "pendant runs forward, centered. Foreground giant crystal pillars on both "
                "left and right edges of frame parallax past with motion blur. Mixed "
                "jade-amber-magenta lighting. Painterly stylized 3D animation, action chase "
                "peak. Identity lock: one central eye. No text, no logos. 16:9 horizontal "
                "columns flanking."
            ),
            "9x16": (
                "Drone chase-cam swooping back down close to Jiggy: small jade-green Pax "
                "cyclops with single central eye, purple headband, dreadlocks, pink crystal "
                "pendant runs forward, centered. Foreground giant crystal pillars squeezed "
                "close to both left and right sides of the frame parallax past with motion "
                "blur. Mixed jade-amber-magenta lighting. Painterly stylized 3D animation, "
                "action chase peak. Identity lock: one central eye. No text, no logos. 9:16 "
                "columns squeezed close to sides."
            ),
        },
        "refs": [JIGGY_REF],
    },
    "frame-13": {
        "prompt": {
            "16x9": (
                "Drone chase-cam with slight tilt following the action: Jiggy weaves left to "
                "dodge a tall magenta crystal column in his path. Column dominates mid-frame "
                "right of center, Jiggy slightly left-of-center, body angled in dodge motion, "
                "single central eye focused. Column emits magenta glow lighting Jiggy from "
                "the right side. Painterly stylized 3D animation, athletic agile beat. "
                "Identity lock: jade skin, single eye, dreadlocks, purple headband, pink "
                "pendant. No text, no logos. 16:9 column right of center."
            ),
            "9x16": (
                "Drone chase-cam with slight tilt following the action: Jiggy weaves to dodge "
                "a tall magenta crystal column in his path. Column dominates upper area of "
                "frame, Jiggy lower in frame, body angled in dodge motion, single central eye "
                "focused. Column emits magenta glow lighting Jiggy from the side. Painterly "
                "stylized 3D animation, athletic agile beat. Identity lock: jade skin, single "
                "eye, dreadlocks, purple headband, pink pendant. No text, no logos. 9:16 "
                "column upper, Jiggy lower."
            ),
        },
        "refs": [JIGGY_REF],
    },
    "frame-14": {
        "prompt": {
            "16x9": (
                "Drone chase-cam continues: a tall magenta crystal column dominates the "
                "frame, glowing intensely with internal bioluminescence. Jiggy is just a "
                "fading sliver on the left edge of frame as he passes behind. The column "
                "itself becomes the visual subject, its surface showing geometric facets and "
                "internal pulse. Background out of focus, fading to soft bloom. Painterly "
                "stylized 3D animation, transitional reveal moment, magic intensity peak. No "
                "text, no logos. 16:9 column vertical filling frame."
            ),
            "9x16": (
                "Drone chase-cam continues: a tall magenta crystal column dominates the "
                "frame, glowing intensely with internal bioluminescence. Jiggy is just a "
                "fading sliver on the left edge of frame as he passes behind. The column "
                "itself becomes the visual subject, its surface showing geometric facets and "
                "internal pulse. Background out of focus, fading to soft bloom. Painterly "
                "stylized 3D animation, transitional reveal moment, magic intensity peak. No "
                "text, no logos. 9:16 column central vertical filling frame."
            ),
        },
        "refs": [],
    },
    "frame-15": {
        "prompt": (
            "Final transition frame: the magenta crystal column glow has expanded to "
            "dominate the frame as a bright magenta-white luminous core surrounded by soft "
            "bloom against fading black void. Centered focal point that visually echoes the "
            "opening macro gem composition. Micro-particles drifting inward toward the core. "
            "Painterly stylized 3D animation, loop-seam frame, satisfying conclusive yet "
            "inviting another viewing. No text, no logos. Composition radially symmetric: "
            "identical for 16:9 centered core and 9:16 centered core."
        ),
        "refs": [],
    },
    "frame-16": {
        "prompt": {
            "16x9": (
                "Hero key-art portrait: medium 50mm slight low angle of Jiggy mid-run, body "
                "dynamically angled, single central round eye with purple iris focused "
                "forward determined, dreadlocks flying behind, purple tribal headband, pink "
                "crystal gemstone clutched in one outstretched hand glowing magenta, tribal "
                "cloth wrap rippling with motion, leather strap with chest crystal pendant. "
                "Background: blurred Pax underground cathedral world with crystal pillars "
                "and bioluminescence. Cinematic key light upper-right, magenta crystal rim "
                "from left, jade-amber bounce fill. Painterly stylized 3D animation, iconic "
                "hero portrait, character poster quality. Identity lock: single central eye "
                "only, no second eye, jade-green skin. No text, no logos. 16:9 horizontal "
                "hero spread with background visible."
            ),
            "9x16": (
                "Hero key-art portrait: medium 50mm slight low angle of Jiggy mid-run, body "
                "dynamically angled, single central round eye with purple iris focused "
                "forward determined, dreadlocks flying behind, purple tribal headband, pink "
                "crystal gemstone clutched in one outstretched hand glowing magenta, tribal "
                "cloth wrap rippling with motion, leather strap with chest crystal pendant. "
                "Background: blurred Pax underground cathedral world with crystal pillars "
                "and bioluminescence. Cinematic key light upper-right, magenta crystal rim "
                "from left, jade-amber bounce fill. Painterly stylized 3D animation, iconic "
                "hero portrait, character poster quality. Identity lock: single central eye "
                "only, no second eye, jade-green skin. No text, no logos. 9:16 vertical hero "
                "filling frame."
            ),
        },
        "refs": [JIGGY_REF],
    },
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _mime(path):
    ext = path.lower().rsplit(".", 1)[-1]
    return {
        "png": "image/png",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "webp": "image/webp",
    }.get(ext, "image/png")


def _resolve_prompt(prompt_or_dict, ratio):
    if isinstance(prompt_or_dict, dict):
        return prompt_or_dict[ratio]
    return prompt_or_dict


# ---------------------------------------------------------------------------
# Core generator (skip + retry-once)
# ---------------------------------------------------------------------------

async def gen_frame(client, sem, video, frame_name, prompt_or_dict, refs, ratio):
    out_path = os.path.join(REPO, "content", "video-bg", video, ratio, f"{frame_name}.png")
    label = f"{video}/{ratio}/{frame_name}"

    if os.path.exists(out_path) and os.path.getsize(out_path) > 50_000:
        kb = os.path.getsize(out_path) // 1024
        print(f"[SKIP {time.strftime('%H:%M:%S')}] {label} ({kb}KB)")
        return ("SKIP", out_path)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    prompt = _resolve_prompt(prompt_or_dict, ratio)
    size = SIZES[ratio]

    async with sem:
        for attempt in (1, 2):
            t0 = time.time()
            try:
                if refs:
                    file_handles = []
                    file_tuples = []
                    for p in refs:
                        fh = open(p, "rb")
                        file_handles.append(fh)
                        file_tuples.append((os.path.basename(p), fh, _mime(p)))
                    try:
                        result = await client.images.edit(
                            image=file_tuples if len(file_tuples) > 1 else file_tuples[0],
                            prompt=prompt,
                            model=MODEL,
                            size=size,
                            quality=QUALITY,
                            n=1,
                        )
                    finally:
                        for fh in file_handles:
                            fh.close()
                else:
                    result = await client.images.generate(
                        prompt=prompt,
                        model=MODEL,
                        size=size,
                        quality=QUALITY,
                        n=1,
                    )

                b64 = result.data[0].b64_json
                with open(out_path, "wb") as f:
                    f.write(base64.b64decode(b64))

                elapsed = time.time() - t0
                kb = os.path.getsize(out_path) // 1024
                print(f"[OK   {time.strftime('%H:%M:%S')}] {label} - {elapsed:.1f}s - {kb}KB")
                return ("OK", out_path)

            except Exception as e:
                err = str(e)
                if attempt == 1:
                    print(f"[RETRY {time.strftime('%H:%M:%S')}] {label}: {err[:120]}")
                    await asyncio.sleep(2)
                else:
                    print(f"[FAIL {time.strftime('%H:%M:%S')}] {label}: {err[:200]}")
                    return ("FAIL", err)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def main():
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
    sem = asyncio.Semaphore(CONCURRENCY)

    tasks = []
    for video_name, video_data in [("video1-deep-dive", VIDEO1), ("video2-gem-chase", VIDEO2)]:
        for frame_name, frame_data in video_data.items():
            for ratio in SIZES.keys():
                tasks.append(gen_frame(
                    client, sem, video_name, frame_name,
                    frame_data["prompt"], frame_data["refs"], ratio,
                ))

    print("=" * 70)
    print(f"VIDEO-BG FRAMES — total {len(tasks)} tareas (2 videos x 17 frames x 2 ratios)")
    print(f"Concurrency: {CONCURRENCY}")
    print("=" * 70)

    t_start = time.time()
    results = await asyncio.gather(*tasks, return_exceptions=True)
    elapsed = time.time() - t_start

    ok = sum(1 for r in results if isinstance(r, tuple) and r[0] == "OK")
    skip = sum(1 for r in results if isinstance(r, tuple) and r[0] == "SKIP")
    fail = sum(1 for r in results if isinstance(r, tuple) and r[0] == "FAIL")
    exc = sum(1 for r in results if isinstance(r, Exception))

    print("=" * 70)
    print(f"RESUMEN: OK={ok} SKIP={skip} FAIL={fail} EXC={exc} TOTAL={len(tasks)}")
    print(f"Tiempo total: {elapsed/60:.1f} min")
    print("=" * 70)

    if fail or exc:
        print("\nFallas:")
        for r in results:
            if isinstance(r, tuple) and r[0] == "FAIL":
                print(f"  - FAIL: {r[1][:200]}")
            elif isinstance(r, Exception):
                print(f"  - EXC: {str(r)[:200]}")


if __name__ == "__main__":
    asyncio.run(main())
