"""
Genera 70 storyboards (caps 3..12 x 7 shots = 70 imagenes) en paralelo
usando generate_batch_async.

Quality=low (mismo tamano que cap 1+2 aprobados por aldot).
Mantiene IDENTITY LOCK + WARDROBE de gen_cap2_storyboard.py.

Uso:
    python scripts/gen_caps_3_to_12_async.py            # genera los 70
    python scripts/gen_caps_3_to_12_async.py 3          # solo cap 3
    python scripts/gen_caps_3_to_12_async.py 3 5        # caps 3..5
"""
import os
import sys
import time
import asyncio

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from scripts.openai_images import generate_batch_async  # noqa: E402

PERSONAJES = os.path.join(ROOT, "public", "images", "personajes")
CONCEPTS = os.path.join(ROOT, "public", "images", "concepts")
OUT = os.path.join(ROOT, "content", "storyboards")
os.makedirs(OUT, exist_ok=True)

# Refs
JIGGY = os.path.join(PERSONAJES, "jiggy.png")
WIZ = os.path.join(PERSONAJES, "wiz.png")
BYTE = os.path.join(PERSONAJES, "byte.png")
LUXA = os.path.join(PERSONAJES, "luxa.png")
KZ = os.path.join(PERSONAJES, "kz.png")
ONYX = os.path.join(PERSONAJES, "onyx.png")
AGATHA = os.path.join(PERSONAJES, "agatha.png")
MARIELA = os.path.join(PERSONAJES, "mariela.png")

CAVE_WIDE = os.path.join(CONCEPTS, "concept-cave-wide-dark.png")
CAVE_STAL = os.path.join(CONCEPTS, "concept-cave-stalagmites-reawakening.png")
GRATE = os.path.join(CONCEPTS, "concept-bilbao-grate-night.png")
METRO = os.path.join(CONCEPTS, "concept-metro-line5-evening.png")
OFFICE = os.path.join(CONCEPTS, "concept-office-cubicles-cool.png")
KITCHEN = os.path.join(CONCEPTS, "concept-mariela-kitchen-night.png")

# ---------------------------------------------------------------------------
# IDENTITY LOCK (igual que cap 1+2)
# ---------------------------------------------------------------------------
IDENTITY_LOCK = (
    "IDENTITY LOCK — CRITICAL: All characters in this scene that are Pax are "
    "non-human subterranean cyclops-type. Each Pax has ONE single central eye "
    "(cyclops anatomy), ONE pupil only, located inside the white area of that "
    "ONE eye. Do NOT draw two eyes. Do NOT draw two pupils. Do NOT draw two eye "
    "lines. Do NOT draw a second small eye anywhere on the face. Repeat: ONE "
    "eye total, ONE pupil total, per Pax character. Their reference char sheets "
    "are provided as Image inputs — match the proportions, skin tone, ear shape "
    "(elongated elastic pointed), and the FOUR fingers per hand exactly. They "
    "are 3 to 3.5 heads tall (KZ shortest at 1.05m, Onyx tallest at 1.70m). "
    "Humans in scene have TWO normal eyes — they are NOT Pax. "
)

STYLE_BLOCK = (
    "Style: stylized 3D animation, semi-realistic PBR shading with subsurface "
    "scattering on turquoise-teal Pax skin, expressive cartoon proportions, "
    "high-contrast cinematic neon-magic lighting, saturated emissive crystals "
    "with bloom, dense volumetric dust motes and god rays, slight film grain, "
    "color grading magenta/turquesa complementario, 16:9. Reads as premium "
    "mobile-game cinematic / animated key art. "
    "NEGATIVE: photorealistic, hyperrealistic, anime, moe, 2D hand-drawn, "
    "cel-shaded flat, Pixar/Disney/DreamWorks generic family-feature look, "
    "fantasy battle cliches, game HUD, thriller vignette, glamour beauty shot, "
    "loading-screen blinking pulse, two eyes per Pax, dual pupils, cartoon "
    "two-dot eyes on a Pax, accessories not present in reference char sheets."
)

WARDROBE = {
    "jiggy": (
        "Jiggy wears the leather harness with magenta crystal pendant from his "
        "char sheet (Image labeled Jiggy). Turquoise-teal skin, ONE central "
        "eye with turquoise iris and large round pupil."
    ),
    "wiz": (
        "Wiz is the elder: long white beard, deep purple-velvet hooded cloak "
        "with magenta crystal pendant, holds a wooden staff topped with "
        "magenta crystal. Slightly shorter, rounder proportions (2.8-3 heads). "
        "ONE central eye."
    ),
    "byte": (
        "Byte wears the lime-green LED neural headphones (the lime LEDs are "
        "EXCLUSIVE to Byte — no other Pax wears lime), tech hoodie with "
        "digital code patterns in jade-cyan. ONE central eye. Carries a small "
        "holo-tablet."
    ),
    "luxa": (
        "Luxa wears the purple bandana with golden detail and woven multicolor "
        "scarf, carries a warm-gold crystal lantern. Turquoise skin with "
        "subtle self-emission. ONE central eye."
    ),
    "kz": (
        "KZ is the smallest of the clan (1.05m), wearing a magenta-purple "
        "bandana with tribal beaded accessories and a magenta heart-shaped "
        "crystal pendant on chest. Innocent expression. ONE central eye."
    ),
    "onyx": (
        "Onyx is the tallest and most athletic (1.70m), bare strong torso "
        "with leather short kilt, copper-and-turquoise wrist bracelets, "
        "tribal markings on shoulders. ONE central eye."
    ),
    "agatha": (
        "Agatha has LIME-GREEN skin (NOT turquoise — emphasized lime, more "
        "yellow-green), long dark dreadlocks, wears a long flowing purple "
        "ceremonial robe with jade trim. Maternal, calm expression. ONE "
        "central eye."
    ),
    "mariela": (
        "Mariela is a HUMAN chilean woman in her 30s, two normal eyes, warm "
        "brown skin, dark wavy hair tied back, casual professional wear. She "
        "is NOT a Pax — she has TWO eyes."
    ),
    "sami": (
        "Sami is a HUMAN latina teenage girl (around 15-16), two normal eyes, "
        "warm tan skin, dark hair often in a messy bun or loose, hoodie + "
        "graphic tee, sneakers. Carries a spray-paint can or backpack. She "
        "is NOT a Pax — she has TWO eyes."
    ),
    "heriberto": (
        "Heriberto is a HUMAN elderly latino retired teacher in his 70s, "
        "two normal eyes, weathered warm brown skin, white short hair, neat "
        "but humble shirt with vest. He is NOT a Pax — he has TWO eyes."
    ),
    "kid": (
        "An anonymous HUMAN child of school age, two normal eyes — NOT a Pax."
    ),
    "older_woman": (
        "An elderly HUMAN woman with grocery bags, two normal eyes — NOT a Pax."
    ),
    "office_man": (
        "A HUMAN man in business suit and tie with coffee cup, two normal "
        "eyes — NOT a Pax. Indifferent expression."
    ),
    "young_helper": (
        "A young HUMAN adult of modest appearance, two normal eyes — NOT a "
        "Pax. Helping carry bags."
    ),
    "grandma": (
        "An elderly HUMAN woman, Sami's grandmother, two normal eyes — NOT a "
        "Pax. Warm and weathered."
    ),
    "homeless": (
        "A HUMAN man sleeping under a blanket on a sidewalk, two normal eyes "
        "(closed) — NOT a Pax."
    ),
}


def build_prompt(scene: str, characters, extra_negative: str = "") -> str:
    wardrobe_lines = "\n".join(WARDROBE[c] for c in characters)
    return (
        IDENTITY_LOCK
        + "\n\nWardrobe and identity per character (match the provided char "
          "sheet images exactly):\n"
        + wardrobe_lines
        + "\n\nSCENE: "
        + scene
        + "\n\n"
        + STYLE_BLOCK
        + (
            f" Additional negative for this shot: {extra_negative}"
            if extra_negative
            else ""
        )
    )


# ---------------------------------------------------------------------------
# 7 SHOTS x 10 CAPS = 70 SHOTS
# Estructura por cap: [hook, setup, catalizador, desarrollo, climax, accion, cliffhanger]
# ---------------------------------------------------------------------------
CAPS = {
    # =====================================================================
    # CAP 3 — El grafiti
    # =====================================================================
    3: {
        "title": "El grafiti",
        "shots": [
            {
                "slug": "01-manhole-eye-peek",
                "characters": ["jiggy"],
                "refs": [JIGGY, GRATE],
                "scene": (
                    "Extreme close-up, 100mm macro lens, locked-off, slight "
                    "low angle. A heavy iron manhole cover lifts about four "
                    "centimeters off the wet asphalt. From the dark slit "
                    "below, ONE single huge turquoise-teal central eye (this "
                    "is Jiggy peeking out) fills the gap, iris turquoise and "
                    "the round pupil dilated wide with adrenaline. The "
                    "manhole metal has fresh raindrops, the surrounding "
                    "asphalt reflects warm sodium streetlight orange. Mood: "
                    "first contact, adrenaline, slightly comic in scale. "
                    "Composition: rule of thirds with the eye in upper third "
                    "framed by the dark slit."
                ),
            },
            {
                "slug": "02-jiggy-tiny-vs-city",
                "characters": ["jiggy"],
                "refs": [JIGGY, GRATE],
                "scene": (
                    "Wide-low shot, 24mm lens, very low angle from ground. "
                    "Jiggy stands tiny on a wet city sidewalk in foreground "
                    "lower-left, his body small against towering urban "
                    "architecture: graffiti-covered concrete walls, a rusted "
                    "fire escape, distant office tower lights blurred behind. "
                    "Streetlights cast warm sodium-orange pools, contrasted "
                    "with cool turquoise night sky. His ONE central eye looks "
                    "up, mouth slightly open in awe. Latinoamerican city "
                    "feel — crooked power lines, hand-painted shop signs in "
                    "spanish (do not render readable text). Mood: scale shock, "
                    "wonder, fear in good measure."
                ),
                "extra_negative": (
                    "do not render readable real-world brand logos or specific "
                    "store names; signs should be abstract."
                ),
            },
            {
                "slug": "03-symbol-trail-collage",
                "characters": [],
                "refs": [GRATE, CAVE_STAL],
                "scene": (
                    "Medium shot, split-composition montage feel, 35mm lens. "
                    "A wet city alley wall covered in stickers, posters and "
                    "spray-paint. Among the chaos, the SAME stylized "
                    "circular-with-lines Pax glyph repeats four times across "
                    "the frame: as a sticker on a leaning bicycle handlebar, "
                    "scribbled on a crumpled coffee napkin in a puddle, drawn "
                    "in chalk by a child on a low wall, and on the back of a "
                    "denim jacket hanging from a balcony above. The symbol is "
                    "scattered, not pointing to anyone — it lives in the city. "
                    "Lighting: warm sodium with cool magenta neon spill from "
                    "an off-frame sign. NO live characters in foreground. "
                    "Mood: mystery, residue, repetition."
                ),
                "extra_negative": (
                    "the Pax glyph is an abstract circular-with-lines invented "
                    "symbol, not a real-world logo."
                ),
            },
            {
                "slug": "04-sami-painting-fresh",
                "characters": ["sami"],
                "refs": [GRATE],
                "scene": (
                    "Medium shot, 50mm lens, slight 3/4 angle. Sami — a "
                    "human latina teenage girl, hoodie up, dark hair messy "
                    "tied — has just finished spray-painting the same Pax "
                    "glyph on a low concrete wall in the alley, a thin trail "
                    "of fluorescent magenta paint running from the glyph. She "
                    "holds the spray can in one hand, her other thumb wiping "
                    "a paint smudge on her cheek. Her TWO normal human eyes "
                    "are focused, calm, like she's in flow. Streetlight casts "
                    "warm orange sidelight; cool magenta paint mark glows. "
                    "Composition: wall on left two-thirds with fresh glyph, "
                    "Sami in right third looking at her work."
                ),
            },
            {
                "slug": "05-jiggy-hides-behind-dumpster",
                "characters": ["jiggy"],
                "refs": [JIGGY, GRATE],
                "scene": (
                    "Medium shot, 50mm lens, side-3/4 angle. Jiggy crouches "
                    "behind a battered green metal dumpster in the alley, "
                    "peeking out with ONE turquoise central eye visible past "
                    "the dumpster edge. Jiggy is small in scale — the dumpster "
                    "is taller than him. Beyond him, slightly out of focus, a "
                    "blurred silhouette suggests Sami leaning down placing a "
                    "wrapped sandwich on the sidewalk next to a sleeping "
                    "homeless figure under a blanket (no one we can read "
                    "individually — silhouette only). Lighting: warm sodium "
                    "key on the dumpster, cool magenta rim from off-frame "
                    "neon. Mood: tender voyeur, witness without intrusion."
                ),
            },
            {
                "slug": "06-crystal-first-spark",
                "characters": ["jiggy"],
                "refs": [JIGGY, CAVE_STAL],
                "scene": (
                    "Extreme close-up, 100mm macro, locked-off. Jiggy's open "
                    "FOUR-fingered hand cradles the empty magenta crystal "
                    "from cap 1. A single tiny magenta spark/blink has just "
                    "lit inside the crystal — a hairline of warm light "
                    "running through one facet. The reflection of the spark "
                    "shows in the corner of the frame on Jiggy's ONE turquoise "
                    "central eye, slightly out of focus behind. Background: "
                    "dark wet alley out-of-focus with cool turquoise shadow. "
                    "Mood: first proof, tender wonder, the system works."
                ),
            },
            {
                "slug": "07-cliffhanger-wiz-pockets-spark",
                "characters": ["wiz", "jiggy"],
                "refs": [WIZ, JIGGY, CAVE_STAL],
                "scene": (
                    "Medium shot, 50mm lens, slight low angle, locked-off. "
                    "Inside the central crystal cavern. Wiz holds the just-"
                    "returned magenta crystal in his FOUR-fingered hand, "
                    "examining its faint warm spark. Jiggy stands slightly "
                    "behind Wiz, back-3/4 to camera, looking at Wiz. With "
                    "Wiz's other hand — barely in frame — he is sliding a "
                    "second, older, golden-pale spark into a hidden fold of "
                    "his purple cloak. The camera holds on this small "
                    "secretive gesture for a beat too long. Lighting: warm "
                    "magenta key from new spark, cool basalt ambient, single "
                    "amber rim. Mood: mystery seed, narrative breadcrumb."
                ),
            },
        ],
    },
    # =====================================================================
    # CAP 4 — La clase del lunes
    # =====================================================================
    4: {
        "title": "La clase del lunes",
        "shots": [
            {
                "slug": "01-balcony-class-pov",
                "characters": ["heriberto", "kid"],
                "refs": [GRATE],
                "scene": (
                    "Wide shot, 35mm lens, slight high angle from a tree "
                    "branch POV. A modest urban balcony with tile floor, "
                    "potted plants and a small portable green chalkboard. "
                    "Heriberto — an elderly latino human teacher with white "
                    "hair, two normal eyes, neat shirt + vest — stands by the "
                    "board mid-explanation. Three children sit cross-legged "
                    "on the floor with notebooks; one child has a hand raised "
                    "high. Warm afternoon light on the tile, cool shaded "
                    "leaves frame the upper edge. Composition: balcony "
                    "centered, the foreground branches blurred at top edge "
                    "(setup for next shot). Mood: humble, ordinary, sacred."
                ),
            },
            {
                "slug": "02-byte-luxa-upside-down",
                "characters": ["byte", "luxa"],
                "refs": [BYTE, LUXA, GRATE],
                "scene": (
                    "Medium close-up, 50mm lens, frame upside-down or canted. "
                    "Byte (lime-green LED headphones glowing softly) and Luxa "
                    "(purple-gold bandana, multicolor scarf, gold lantern) "
                    "hang upside-down from a tree branch above the balcony, "
                    "their bodies in playful relaxed grip on the branch. "
                    "Byte is focused listening, holo-tablet pointed down "
                    "toward the balcony. Luxa giggles silently with one hand "
                    "covering her mouth. Both have ONE central eye, FOUR "
                    "fingers. Sunlight filters magenta-warm through leaves "
                    "behind them. Composition: characters in upper half of "
                    "frame, lower out-of-focus balcony tile visible. Mood: "
                    "comic-curious, light, inviting."
                ),
            },
            {
                "slug": "03-byte-detects-frequency",
                "characters": ["byte"],
                "refs": [BYTE, GRATE],
                "scene": (
                    "Close-up, 85mm lens, side angle. Byte's face fills the "
                    "frame: ONE central eye narrowed in concentration, lime-"
                    "green LED on his headphones glowing brighter, a faint "
                    "cyan scan-line of holographic data flickering across his "
                    "cheek and temple from a small holo-tablet held just below "
                    "frame. Background: leafy out-of-focus branches with warm "
                    "afternoon backlight. Mood: detection moment, ordered "
                    "energy registered."
                ),
            },
            {
                "slug": "04-heriberto-doubt",
                "characters": ["heriberto"],
                "refs": [GRATE],
                "scene": (
                    "Medium close-up, 50mm lens, slight low angle. Heriberto "
                    "leans heavily on the small chalkboard, two normal human "
                    "eyes downcast in fatigue. Chalk dust in his fingers. "
                    "Behind him, the children are out-of-focus still copying "
                    "from the board. His expression: a man on the verge of "
                    "quitting, unsure if anything he gives still matters. "
                    "Warm afternoon light, dust motes drifting in a single "
                    "shaft of sun. Mood: melancholy, on the edge of giving "
                    "up. NO Pax in frame."
                ),
            },
            {
                "slug": "05-girl-gives-drawing",
                "characters": ["heriberto", "kid"],
                "refs": [GRATE],
                "scene": (
                    "Medium shot, 35mm lens, slight low angle from below "
                    "balcony rail. The class has finished — the chalkboard is "
                    "behind them. A small human girl (TWO normal eyes) holds "
                    "out a folded paper drawing to Heriberto, who is now "
                    "seated on a low stool. The drawing depicts him at the "
                    "board with three smiling kids in front. Heriberto's "
                    "weathered hand reaches to take it; his expression "
                    "softens, a slow surprised smile. Other two children "
                    "watching out-of-focus behind. Warm late-afternoon golden "
                    "light. Mood: small grace, silent gratitude."
                ),
            },
            {
                "slug": "06-byte-crystal-charges",
                "characters": ["byte"],
                "refs": [BYTE, CAVE_STAL],
                "scene": (
                    "Close-up, 85mm lens, side angle. Byte's open FOUR-"
                    "fingered hand holds a small magenta crystal pendant. "
                    "The crystal has just emitted a single visible warm pulse "
                    "of light, a tiny magenta spark visible inside one facet, "
                    "with soft bloom. Reflection in his ONE central eye "
                    "off-focus behind. Background: blurred green leaves "
                    "fading to dark — they are still on the branch above the "
                    "balcony. Mood: confirmation, the ruca-clase has charged."
                ),
            },
            {
                "slug": "07-cliffhanger-ant-on-symbol",
                "characters": [],
                "refs": [GRATE, CAVE_STAL],
                "scene": (
                    "Extreme macro close-up, 100mm macro lens, locked-off. "
                    "On a child's open notebook page (resting on the balcony "
                    "tile floor), a small ant walks across a hand-drawn Pax "
                    "glyph in pencil — the same circular-with-lines symbol. "
                    "The ant is in sharp focus crossing the symbol's center; "
                    "the notebook paper is slightly textured. Beyond the "
                    "notebook edge, blurred, a hint of the balcony floor and "
                    "the children's feet. Lighting: warm afternoon ambient. "
                    "NO Pax, NO humans clearly in frame. Mood: small thread "
                    "to next cap, cosmic-tiny."
                ),
                "extra_negative": (
                    "do not render readable text in the notebook; only "
                    "abstract scribbles and the Pax glyph."
                ),
            },
        ],
    },
    # =====================================================================
    # CAP 5 — El que no quiso
    # =====================================================================
    5: {
        "title": "El que no quiso",
        "shots": [
            {
                "slug": "01-onyx-pokes-head",
                "characters": ["onyx"],
                "refs": [ONYX, GRATE],
                "scene": (
                    "Medium close-up, 50mm lens, low angle from street level. "
                    "A heavy manhole cover is pushed up just enough to show "
                    "Onyx's head emerging — bare athletic shoulders, ONE "
                    "central eye, copper-and-turquoise wrist bracelet visible "
                    "on a hand gripping the rim. A blurry bicycle whips past "
                    "in foreground left, motion-streak trail. Onyx's "
                    "expression is startled-cautious, mouth open in a small "
                    "'oh'. Cool morning city light, warm streetlight glow "
                    "fading. Mood: comic first contact, bigger Pax in a "
                    "narrow gap."
                ),
            },
            {
                "slug": "02-jiggy-onyx-walking-rich-zone",
                "characters": ["jiggy", "onyx"],
                "refs": [JIGGY, ONYX, OFFICE],
                "scene": (
                    "Wide shot, 24mm lens, low angle. Jiggy and Onyx walk "
                    "side-by-side along an early-morning sidewalk in a "
                    "wealthier business district — clean glass-and-steel "
                    "office tower bases, manicured potted trees, polished "
                    "stone tiles. Both Pax are tiny against the towers. "
                    "Jiggy in front, Onyx behind covering. Both have ONE "
                    "central eye, FOUR fingers visible. Pre-rush hour, soft "
                    "blue-cool ambient with warm magenta sunrise rim from "
                    "between buildings. Mood: out of place, recon mode."
                ),
            },
            {
                "slug": "03-woman-falls-bags",
                "characters": ["older_woman", "office_man"],
                "refs": [OFFICE],
                "scene": (
                    "Medium-wide shot, 35mm lens, slight high angle. An "
                    "elderly human woman (TWO normal eyes) has just stumbled "
                    "and fallen forward on the sidewalk, grocery bags "
                    "scattering — apples rolling, a baguette, a plastic bag "
                    "torn. In the same frame, on the right, a human "
                    "businessman in a tailored suit and tie holding a coffee "
                    "cup (TWO normal eyes) is mid-stride, looking down at her "
                    "but already walking past. His expression: blank, "
                    "indifferent, slightly annoyed. Cool blue-grey morning "
                    "light. NO Pax in this shot. Mood: chill, judgmental."
                ),
            },
            {
                "slug": "04-onyx-stops-jiggy",
                "characters": ["onyx", "jiggy"],
                "refs": [ONYX, JIGGY, OFFICE],
                "scene": (
                    "Medium close-up, 50mm lens, slight low angle. Onyx's "
                    "broad FOUR-fingered hand presses gently across Jiggy's "
                    "chest, holding him back from leaving. Both characters "
                    "in 3/4 from behind, looking off-camera right at "
                    "something out of frame (the fallen woman). Their backs "
                    "are to us, so each ONE central eye is implied by the "
                    "head turn. Onyx's posture: still, watching, deciding to "
                    "wait. Jiggy: tense, unsatisfied, but accepting the "
                    "pause. Lighting: cool from sidewalk, warm rim from "
                    "sunrise. Mood: pause that says 'wait, watch'."
                ),
            },
            {
                "slug": "05-young-helper-helps",
                "characters": ["young_helper", "older_woman"],
                "refs": [OFFICE],
                "scene": (
                    "Medium shot, 50mm lens, slight low angle. A young human "
                    "of modest appearance (worn jacket, scuffed shoes, TWO "
                    "normal eyes) is bent down picking up the fallen "
                    "groceries, gently placing the apples back into the bag. "
                    "The elderly woman (TWO normal eyes) has one hand on the "
                    "young person's shoulder for balance, expression "
                    "grateful, soft. The young helper does not look at her — "
                    "focused on the bag, calm. The expensive office buildings "
                    "blurred behind them. Warm amber sunrise light on the "
                    "scene contrasted with cool shadow. Mood: quiet kindness "
                    "without spectacle."
                ),
            },
            {
                "slug": "06-onyx-processing-silent",
                "characters": ["onyx"],
                "refs": [ONYX, OFFICE],
                "scene": (
                    "Close-up, 85mm lens, slight 3/4 frontal. Onyx's face "
                    "fills the frame: athletic build implied, copper-and-"
                    "turquoise bracelet on shoulder visible, tribal markings "
                    "on shoulder. His ONE central eye is fixed off-camera "
                    "right (where the helping happened), iris turquoise, "
                    "pupil contracted in deep focus. Lips slightly parted as "
                    "if about to speak but not. Lighting: warm key from "
                    "sunrise on his face, cool rim from shadow side. "
                    "Background: out-of-focus office tower base in cool blue. "
                    "Mood: processing a contradiction, recalibration."
                ),
            },
            {
                "slug": "07-cliffhanger-vuelve-graffiti",
                "characters": ["onyx"],
                "refs": [ONYX, GRATE],
                "scene": (
                    "Medium shot, 50mm lens, side angle. Onyx is back near a "
                    "tunnel entrance in an alley wall, stopped, looking at "
                    "fresh graffiti. The graffiti shows the Pax circular-"
                    "with-lines glyph, painted recently in fluorescent "
                    "magenta. Next to it, written in marker in a different "
                    "hand, a single simple spanish word reading 'VUELVE' "
                    "(must be readable as the word 'vuelve'). Onyx's ONE "
                    "central eye is fixed on the word, head slightly tilted, "
                    "trying to understand. Lighting: cool morning shadow, "
                    "warm sodium streetlamp residue from the night. Mood: "
                    "someone is watching, someone above knows."
                ),
                "extra_negative": (
                    "ONLY render the single spanish word 'vuelve' next to the "
                    "glyph, no other readable text or brand logos."
                ),
            },
        ],
    },
    # =====================================================================
    # CAP 6 — La pregunta de Mariela
    # =====================================================================
    6: {
        "title": "La pregunta de Mariela",
        "shots": [
            {
                "slug": "01-new-crystal-born",
                "characters": [],
                "refs": [CAVE_STAL, CAVE_WIDE],
                "scene": (
                    "Medium close-up, 85mm lens, locked-off. Inside the dark "
                    "central crystal cavern at night. Between two old dim "
                    "crystals, a brand-new magenta crystal has just emerged "
                    "from the rocky floor, still partially encased in basalt, "
                    "glowing with a steady warm pulse. Soft warm subsurface "
                    "scatter visible inside the crystal. Floor and stalagmite "
                    "rocks around it in cool deep purple shadow with magenta "
                    "rim. NO characters in frame. Mood: birth, mystery, "
                    "delicate. Composition: new crystal centered with old "
                    "crystals as out-of-focus framing on left and right."
                ),
            },
            {
                "slug": "02-wiz-discovers-new-crystal",
                "characters": ["wiz"],
                "refs": [WIZ, CAVE_STAL],
                "scene": (
                    "Medium close-up, 50mm lens, side angle, slight low. Wiz "
                    "stands beside the new crystal, his FOUR-fingered hand "
                    "extended just over it without touching. His ONE central "
                    "eye is wide with calm awe, white beard catching warm "
                    "magenta light from the crystal. Purple-velvet hooded "
                    "cloak drapes; staff held loose in his other hand. "
                    "Background: cavern darkness with old crystals out of "
                    "focus. Lighting: magenta key from new crystal, cool "
                    "ambient. Mood: revered surprise."
                ),
            },
            {
                "slug": "03-mariela-laptop-night",
                "characters": ["mariela"],
                "refs": [MARIELA, KITCHEN],
                "scene": (
                    "Medium shot, 50mm lens, slight 3/4 angle. Mariela — a "
                    "human chilean woman in her 30s, two normal eyes, dark "
                    "wavy hair tied back, casual hoodie — sits at a small "
                    "kitchen table in a modest apartment at night. The only "
                    "light source is the closed laptop screen reflecting "
                    "blue-cool on her face from below. A mug of tea sits "
                    "beside her. Her expression: thoughtful, hesitant, "
                    "exhaling slowly. Window behind her shows blurred night "
                    "city with sodium lights. NO Pax in frame. Mood: solo "
                    "reflection, the question that won't leave."
                ),
            },
            {
                "slug": "04-mariela-types-deletes",
                "characters": ["mariela"],
                "refs": [MARIELA, KITCHEN],
                "scene": (
                    "Close-up, 85mm lens, slight high angle over her "
                    "shoulder. Mariela's hands hover over the keyboard, "
                    "TWO normal human eyes focused on the laptop screen "
                    "(which displays a generic email composer with "
                    "non-readable abstract text — do not render real text). "
                    "Her right finger has just lifted from the delete key. "
                    "Cool blue laptop glow on her face and hands. Mood: "
                    "indecision, the third draft, almost ready."
                ),
                "extra_negative": (
                    "do not render readable email text on the screen — show "
                    "blurred or abstract paragraph blocks only."
                ),
            },
            {
                "slug": "05-jiggy-bilbao-ushnu",
                "characters": ["jiggy"],
                "refs": [JIGGY, GRATE],
                "scene": (
                    "Wide-medium shot, 35mm lens, low angle. Jiggy walks "
                    "alone through a small empty plaza on a quiet city "
                    "avenue at late night. In the center of the plaza, an "
                    "ancient andean ushnu — a small flat stone ceremonial "
                    "platform — sits weathered, half-forgotten among modern "
                    "concrete benches. Jiggy approaches it cautiously, his "
                    "ONE central eye scanning. He carries the magenta crystal "
                    "in one FOUR-fingered hand, glowing warm. Streetlights "
                    "warm sodium overhead, cool turquoise night sky above. "
                    "No other people in frame. Mood: solemn passage, "
                    "transition between ancient and modern."
                ),
            },
            {
                "slug": "06-jiggy-leaves-crystal-mariela",
                "characters": ["jiggy", "mariela"],
                "refs": [JIGGY, MARIELA, KITCHEN],
                "scene": (
                    "Close-up, 85mm lens, slight high angle. Mariela is "
                    "asleep, head resting sideways on the kitchen table next "
                    "to the closed laptop, two normal human eyes closed. Her "
                    "open palm rests upturned on the table. Jiggy stands "
                    "tiny on the edge of the table, his ONE central eye "
                    "fixed on her face with reverent care. He gently lowers "
                    "the warm-glowing magenta crystal into her open palm "
                    "with both FOUR-fingered hands. Cool moonlight from a "
                    "window, warm magenta from the crystal acting as key "
                    "light on both. Mood: tender, reverential, almost "
                    "religious."
                ),
            },
            {
                "slug": "07-cliffhanger-te-vimos",
                "characters": ["jiggy"],
                "refs": [JIGGY, GRATE],
                "scene": (
                    "Medium shot, 50mm lens, slight low angle. Jiggy stands "
                    "back near the alley tunnel entrance, looking at the "
                    "wall. The graffiti from cap 5 is still there: the Pax "
                    "circular-with-lines glyph and next to it the marker "
                    "writing — but now the writing has changed. Where it "
                    "said 'VUELVE' before, fresh marker has added two more "
                    "spanish words: now it reads clearly 'TE VIMOS' (the "
                    "spanish phrase 'te vimos' must be readable). Jiggy's "
                    "ONE central eye is wide with realization, pupil "
                    "contracted. Lighting: cool pre-dawn blue, warm sodium "
                    "from overhead lamp. Mood: someone is consciously "
                    "watching."
                ),
                "extra_negative": (
                    "ONLY render the spanish phrase 'te vimos' next to the "
                    "glyph, no other readable text."
                ),
            },
        ],
    },
    # =====================================================================
    # CAP 7 — El observador
    # =====================================================================
    7: {
        "title": "El observador",
        "shots": [
            {
                "slug": "01-hand-marker-symbol",
                "characters": [],
                "refs": [METRO],
                "scene": (
                    "Extreme close-up, 100mm macro lens, locked-off. A human "
                    "hand (two-eyed implied, but only the hand is visible — "
                    "young, slim, with paint stains on the fingers) is "
                    "drawing the Pax circular-with-lines glyph on a metro "
                    "station tile wall with a fat black marker. Below the "
                    "glyph the same hand has just written the spanish phrase "
                    "'LOS VEO' (must be readable). The marker tip is still "
                    "in contact with the wall completing a stroke. Cool "
                    "fluorescent metro lighting blue-white from above. NO "
                    "characters' faces in frame, just the hand and the wall. "
                    "Mood: secret declaration, the observer reveals herself."
                ),
                "extra_negative": (
                    "ONLY render the spanish phrase 'los veo' and the abstract "
                    "Pax glyph; no other readable text."
                ),
            },
            {
                "slug": "02-byte-triangulates-map",
                "characters": ["byte"],
                "refs": [BYTE, CAVE_STAL],
                "scene": (
                    "Medium close-up, 50mm lens, slight 3/4. Byte stands in "
                    "the cavern near a flat rocky surface where his holo-"
                    "tablet is projecting a glowing cyan map of the city "
                    "above with red dots marking the locations of the "
                    "graffitis — the dots form a clear pattern around tunnel "
                    "exit points. Byte's ONE central eye reflects the cyan "
                    "data, lime-green LED headphones glowing. His FOUR-"
                    "fingered hand zooms a node on the holographic map. "
                    "Lighting: cyan key from hologram, magenta rim from "
                    "distant cavern crystals. Mood: detective uncovering "
                    "pattern."
                ),
                "extra_negative": (
                    "the holographic map should show abstract dots and lines, "
                    "not readable real-world maps or text."
                ),
            },
            {
                "slug": "03-bakery-exterior",
                "characters": [],
                "refs": [METRO],
                "scene": (
                    "Wide shot, 28mm lens, slight low angle. Exterior of a "
                    "humble neighborhood bakery (panaderia) at evening. "
                    "Hand-painted spanish-style sign reading 'PANADERIA' "
                    "(must be readable as exactly that single word) over "
                    "the door, warm yellow incandescent light spilling out "
                    "onto the wet sidewalk. Through the window, blurred "
                    "silhouettes inside. Outside, a man under a thin blanket "
                    "sleeping against a wall to one side. The same Pax glyph "
                    "appears as a small chalk mark on the corner of the "
                    "doorframe, easy to miss. NO Pax in frame. Mood: humble, "
                    "warm, threshold."
                ),
                "extra_negative": (
                    "render only the single word 'PANADERIA' on the sign; no "
                    "other readable text or real-world brand logos."
                ),
            },
            {
                "slug": "04-sami-grandma-bread",
                "characters": ["sami", "grandma"],
                "refs": [METRO],
                "scene": (
                    "Medium shot, 50mm lens, eye-level. Inside a warm bakery "
                    "kitchen at night. Sami — human latina teen with messy "
                    "bun, hoodie, two normal eyes — and her grandmother (an "
                    "elderly human woman, two normal eyes, apron, weathered "
                    "warm hands) are wrapping leftover bread into small "
                    "paper bags on a wooden counter. On the counter, next to "
                    "a steaming mug of tea, a paper napkin shows the Pax "
                    "glyph drawn in pencil in the corner — the grandmother's "
                    "old habit. Warm yellow incandescent light, dust-like "
                    "flour particles in the air. Mood: ancestral inheritance "
                    "of the symbol, family work."
                ),
            },
            {
                "slug": "05-sami-bread-homeless",
                "characters": ["sami", "homeless"],
                "refs": [METRO],
                "scene": (
                    "Medium shot, 50mm lens, slight 3/4 angle. Outside the "
                    "bakery, on the sidewalk. Sami crouches gently next to a "
                    "human man sleeping under a thin blanket against the "
                    "wall, two normal eyes closed. She places a small paper "
                    "bag of bread beside him without waking him, no signature "
                    "no witness, expression soft. Behind her, the bakery "
                    "warm window glow; above, cool sodium streetlight. Mood: "
                    "kindness without performance, ruca-gesto."
                ),
            },
            {
                "slug": "06-byte-agatha-realize",
                "characters": ["byte", "agatha"],
                "refs": [BYTE, AGATHA, METRO],
                "scene": (
                    "Medium two-shot, 50mm lens, slight low angle. Byte and "
                    "Agatha stand in a dim alley near the bakery, both Pax "
                    "with ONE central eye, FOUR fingers. Byte's holo-tablet "
                    "still scanning, faint cyan light on his face. Agatha — "
                    "lime-green skin (emphasized yellow-green NOT teal), "
                    "long dark dreadlocks, purple ceremonial robe — has her "
                    "free hand on Byte's shoulder, her expression calm and "
                    "soft. Both look toward Sami's direction off-camera. "
                    "Behind them on the wall, a fresh painted Pax glyph "
                    "with the spanish phrase 'GRACIAS POR VENIR' below "
                    "(must be readable). Lighting: warm sodium from "
                    "streetlight, cool magenta from a far neon. Mood: "
                    "revelation softens — they are not being hunted, they "
                    "are being thanked."
                ),
                "extra_negative": (
                    "render only the spanish phrase 'gracias por venir' on the "
                    "wall, no other readable text."
                ),
            },
            {
                "slug": "07-cliffhanger-sami-draws-jiggy",
                "characters": ["sami"],
                "refs": [METRO],
                "scene": (
                    "Medium shot, 50mm lens, slight 3/4 angle from behind "
                    "Sami's shoulder. Sami stands facing a concrete alley "
                    "wall, spray can in hand, two normal eyes focused. On "
                    "the wall, just finished, she has drawn — in fluorescent "
                    "magenta and turquoise — a small stylized Pax character "
                    "that clearly resembles Jiggy: ONE central eye, leather "
                    "harness, magenta crystal pendant, mid-stride. The "
                    "drawing is graffiti-style but unmistakable. Warm "
                    "sodium streetlight on her back, cool magenta paint "
                    "glow on the wall. Mood: she remembers him from cap 3, "
                    "she always saw him."
                ),
            },
        ],
    },
    # =====================================================================
    # CAP 8 — Se rompe algo
    # =====================================================================
    8: {
        "title": "Se rompe algo",
        "shots": [
            {
                "slug": "01-temple-crystal-cracks",
                "characters": [],
                "refs": [CAVE_STAL],
                "scene": (
                    "Extreme close-up, 100mm macro, locked-off. A single "
                    "ancient dormant crystal in the abandoned temple chamber "
                    "from cap 2. A new fresh crack runs across one face, a "
                    "thin hairline of magenta light bleeding from inside the "
                    "crack. Tiny crystal dust particles drift around the "
                    "fissure. The rest of the chamber out of focus in dark "
                    "warm amber. Lighting: only the crack itself emits the "
                    "magenta glow, ambient is deep shadow. NO characters in "
                    "frame. Mood: alarm bell, something just broke that "
                    "shouldn't have."
                ),
            },
            {
                "slug": "02-cavern-crystals-dim",
                "characters": [],
                "refs": [CAVE_WIDE, CAVE_STAL],
                "scene": (
                    "Wide establishing shot, 24mm lens, slow descending "
                    "crane angle. The central crystal cavern. Half a dozen "
                    "magenta crystals are simultaneously losing brightness, "
                    "fading from saturated magenta to pale grey-purple in "
                    "real time. Volumetric dust hangs heavy. The wider "
                    "background still has some healthy crystals glowing "
                    "faintly. NO characters in frame. Mood: cascade failure, "
                    "the network is bleeding."
                ),
            },
            {
                "slug": "03-clan-panic-contained",
                "characters": ["wiz", "jiggy", "onyx", "agatha"],
                "refs": [WIZ, JIGGY, ONYX, AGATHA, CAVE_WIDE],
                "scene": (
                    "Medium-wide group shot, 35mm lens, slight low angle. "
                    "Wiz, Jiggy, Onyx and Agatha stand in a loose semicircle "
                    "in the dimming cavern, faces turned toward an off-frame "
                    "fading crystal. Each Pax has ONE central eye, FOUR "
                    "fingers. Onyx's posture: tense, leaning forward — about "
                    "to act. Agatha's hand raised gently to slow him. Wiz "
                    "stands silent at center, expression unreadable, gripping "
                    "his staff tighter. Jiggy in foreground, cradling the "
                    "small charged crystal. Lighting: dimming magenta from "
                    "around the cavern, cool basalt shadow. Mood: contained "
                    "panic, the leaders without a script."
                ),
            },
            {
                "slug": "04-byte-studies-fracture",
                "characters": ["byte"],
                "refs": [BYTE, CAVE_STAL],
                "scene": (
                    "Close-up, 85mm lens, slight 3/4. Byte kneels close to "
                    "the cracked temple crystal from shot 1, his holo-tablet "
                    "casting cyan scan-lines across the fissure. His ONE "
                    "central eye narrows in concentration, lime-green LED "
                    "headphones glowing soft. His FOUR-fingered hand hovers "
                    "near the crack, not touching. Holographic data "
                    "abstract patterns floating in the air around the "
                    "tablet. Lighting: cyan key from hologram on crystal, "
                    "warm magenta bleed from the crack. Mood: the technician "
                    "discovers something deeply wrong."
                ),
                "extra_negative": (
                    "the holographic data should be abstract glyphs and dots, "
                    "not readable text or real numbers."
                ),
            },
            {
                "slug": "05-kz-cries-without-knowing",
                "characters": ["kz"],
                "refs": [KZ, CAVE_STAL],
                "scene": (
                    "Close-up, 85mm lens, slight low angle. KZ — the "
                    "smallest Pax with magenta-purple bandana and heart-"
                    "shaped magenta crystal pendant — has his small FOUR-"
                    "fingered hand pressed flat against the side of the "
                    "cracked old crystal. A single tear has just rolled "
                    "down his cheek, catching warm magenta light from the "
                    "crystal, his ONE central eye wide and confused, mouth "
                    "slightly open in a soundless small sob. He doesn't "
                    "understand why he's crying. Lighting: warm magenta key "
                    "from the crack on his hand and face, cool ambient "
                    "behind. Mood: tender, mysterious empathy, the smallest "
                    "feels what the others can't yet."
                ),
            },
            {
                "slug": "06-wiz-recognizes-spark-mark",
                "characters": ["wiz"],
                "refs": [WIZ, CAVE_STAL],
                "scene": (
                    "Close-up, 85mm lens, slight low angle, locked-off. "
                    "Wiz's FOUR-fingered hand holds out a small golden-pale "
                    "old spark/crystal in the foreground (sharply in focus). "
                    "Behind, slightly out of focus, the cracked temple "
                    "crystal — and the crack pattern visibly mirrors the "
                    "shape of the golden spark. The two shapes rhyme. Wiz's "
                    "ONE central eye visible in upper third of frame, looking "
                    "down at the spark with weight of memory. White beard, "
                    "purple cloak. Lighting: warm key on the spark, magenta "
                    "rim from the crystal behind. Mood: recognition of a "
                    "buried truth."
                ),
            },
            {
                "slug": "07-cliffhanger-wiz-confesses",
                "characters": ["wiz", "jiggy", "agatha", "kz", "onyx"],
                "refs": [WIZ, JIGGY, AGATHA, KZ, ONYX, CAVE_WIDE],
                "scene": (
                    "Medium-wide ensemble shot, 35mm lens, slight low angle. "
                    "Wiz stands at center foreground, cloak heavy, white "
                    "beard catching warm magenta light, ONE central eye "
                    "lowered. The clan core around him in a loose ring "
                    "(Jiggy, Agatha, KZ, Onyx visible — each ONE central "
                    "eye, FOUR fingers). Their faces are turned toward Wiz. "
                    "Wiz's mouth is slightly open as if having just said the "
                    "unresolved opening line of a confession — the moment is "
                    "captured in suspense. The cavern dim, several crystals "
                    "dark in the background. Lighting: single warm magenta "
                    "key on Wiz, cool blue rim on the others. Mood: "
                    "vulnerability, the elder cracks for the first time."
                ),
            },
        ],
    },
    # =====================================================================
    # CAP 9 — Lo que Wiz guardó
    # =====================================================================
    9: {
        "title": "Lo que Wiz guardó",
        "shots": [
            {
                "slug": "01-wiz-opens-hand-spark",
                "characters": ["wiz"],
                "refs": [WIZ, CAVE_STAL],
                "scene": (
                    "Extreme close-up, 100mm macro lens, locked-off. Wiz's "
                    "open FOUR-fingered hand fills the frame, palm up. "
                    "Resting on his palm, the small golden-pale ancient "
                    "spark/crystal pulses with steady warm light — its glow "
                    "is delicate, almost amber-gold. The hand's skin shows "
                    "fine wrinkles and aged texture. Background: blurred "
                    "cavern dark with faint magenta. Lighting: the spark "
                    "itself is the key light, casting upward warm glow on "
                    "the palm and out of frame on his face. Mood: "
                    "confession-as-ritual, the long-kept secret revealed."
                ),
            },
            {
                "slug": "02-flashback-pax-humans-hands-united",
                "characters": [],
                "refs": [CAVE_STAL, CAVE_WIDE],
                "scene": (
                    "Medium-wide stylized flashback shot, 35mm lens, slight "
                    "low angle. Filtered with golden sepia haze and slight "
                    "film grain to read as memory. Two stylized cyclops Pax "
                    "figures (turquoise skin, ONE eye each, FOUR fingers) "
                    "and two human-like figures (TWO eyes each) stand around "
                    "a glowing magenta crystal on a stone pedestal, all four "
                    "of them with hands joined together over the crystal. "
                    "The atmosphere is reverent, ceremonial. Setting: an "
                    "ancient temple chamber. Visible weathered stone with "
                    "carved inscriptions on walls. NO modern elements. "
                    "Lighting: warm magenta from crystal, golden ceremonial "
                    "torchlight ambient, sepia filter overlay. Mood: lost "
                    "communion, the way it used to be."
                ),
            },
            {
                "slug": "03-young-wiz-pockets-spark",
                "characters": ["wiz"],
                "refs": [WIZ, CAVE_STAL],
                "scene": (
                    "Medium close-up, 50mm lens, slight 3/4. A younger "
                    "version of Wiz — same purple cloak, magenta crystal "
                    "pendant, but white beard much shorter (almost just "
                    "stubble), face less weathered, ONE central eye still "
                    "deeply turquoise, body posture more upright. He stands "
                    "alone in a dim ancient temple chamber and is sliding "
                    "the same golden-pale spark into a hidden fold of his "
                    "cloak. His expression: conflicted, choosing wrongly out "
                    "of fear. Lighting: warm spark glow on his hand, cool "
                    "blue ambient deep cavern, sepia slight overlay (still a "
                    "memory). Mood: the original sin, a small wrong choice."
                ),
            },
            {
                "slug": "04-sami-rain-symbol-fading",
                "characters": ["sami"],
                "refs": [METRO],
                "scene": (
                    "Medium close-up, 50mm lens, slight low angle. A young "
                    "human hand (Sami's, two normal eyes implied — only "
                    "shoulder and back visible to camera-3/4) passes its "
                    "palm gently across a wall where the Pax glyph has been "
                    "painted in fluorescent magenta. The paint is half-"
                    "washed away by rain, streaks of magenta running down "
                    "the wall in trails. Her hand traces over the fading "
                    "symbol with care. Wet pavement reflects warm sodium "
                    "streetlight. Mood: tenderness toward the symbol, the "
                    "human counterpart of Wiz's hand on the spark. This is "
                    "a micro-cut to the surface during Wiz's confession."
                ),
            },
            {
                "slug": "05-mariela-looks-at-hand",
                "characters": ["mariela"],
                "refs": [MARIELA, OFFICE],
                "scene": (
                    "Close-up, 85mm lens, slight high angle. Mariela sits at "
                    "her office desk, two normal human eyes looking down at "
                    "her own open right palm, expression contemplative, as "
                    "if remembering something from a dream. Her other hand "
                    "rests on a desk keyboard. Soft cool fluorescent office "
                    "light from above, warm rim from a desk lamp. Background: "
                    "out-of-focus office cubicle partition. NO Pax in frame "
                    "(she does not see them). Mood: silent echo of cap 6, "
                    "the spark left in her hand still pulses in memory."
                ),
            },
            {
                "slug": "06-clan-hands-on-wiz",
                "characters": ["wiz", "agatha", "luxa", "onyx", "jiggy"],
                "refs": [WIZ, AGATHA, LUXA, ONYX, JIGGY, CAVE_STAL],
                "scene": (
                    "Medium-wide group shot, 35mm lens, eye-level. Wiz "
                    "seated at center on a low stone, ONE central eye "
                    "downcast. Agatha (lime-green skin, dreadlocks, purple "
                    "robe) kneels to his right, her FOUR-fingered hand on "
                    "his arm; Luxa stands behind on his left, her hand on "
                    "his shoulder; Onyx kneels in front of him, his large "
                    "FOUR-fingered hand placed gently over Wiz's hand that "
                    "still holds the golden spark. Jiggy stands further back, "
                    "watching. Each Pax has ONE central eye. Lighting: warm "
                    "spark key from Wiz's hand at center, cool blue rim "
                    "around the group. Mood: the clan absorbs his weight, "
                    "shared burden."
                ),
            },
            {
                "slug": "07-cliffhanger-wiz-passes-spark-jiggy",
                "characters": ["wiz", "jiggy"],
                "refs": [WIZ, JIGGY, CAVE_STAL],
                "scene": (
                    "Close two-shot, 85mm lens, side angle. Wiz and Jiggy "
                    "face each other in profile. Wiz's open FOUR-fingered "
                    "hand extends toward Jiggy, the golden-pale spark "
                    "resting on his palm. Jiggy's open FOUR-fingered hand "
                    "rises to meet it. Both ONE central eye visible, locked "
                    "onto each other. The spark hovers in the negative "
                    "space between them at the visual center of the frame. "
                    "Lighting: warm gold spark as key, magenta rim from "
                    "cavern. Mood: handover, trust, this time you don't go "
                    "alone."
                ),
            },
        ],
    },
    # =====================================================================
    # CAP 10 — Subir todos
    # =====================================================================
    10: {
        "title": "Subir todos",
        "shots": [
            {
                "slug": "01-clan-emerges-row",
                "characters": ["jiggy", "kz", "onyx", "agatha", "byte", "luxa", "wiz"],
                "refs": [JIGGY, KZ, ONYX, AGATHA, BYTE, LUXA, WIZ, GRATE],
                "scene": (
                    "Wide ensemble shot, 24mm lens, slight low angle. A "
                    "deserted urban street at dawn. A heavy iron manhole "
                    "cover is open. Emerging out of it in single file: "
                    "Jiggy first (leather harness, magenta pendant), then "
                    "KZ (smallest, magenta-purple bandana), then Onyx "
                    "(athletic, copper bracelets), then Agatha (lime-green "
                    "skin, dark dreadlocks, purple robe), then Byte (lime "
                    "LED headphones), then Luxa (purple-gold bandana), then "
                    "Wiz (white beard, purple hooded cloak, staff). All "
                    "seven Pax in a clear line, each ONE central eye, FOUR "
                    "fingers. Pre-dawn cool turquoise sky, warm sodium "
                    "streetlight. The street empty. Mood: ridiculous, "
                    "tender, historic — the first time all seven are "
                    "outside together."
                ),
            },
            {
                "slug": "02-clan-coral-crossing-city",
                "characters": ["jiggy", "kz", "onyx", "agatha", "byte", "luxa", "wiz"],
                "refs": [JIGGY, KZ, ONYX, AGATHA, BYTE, LUXA, WIZ, GRATE],
                "scene": (
                    "Wide tracking shot, 28mm lens, lateral camera move. The "
                    "seven Pax move as a group through a narrow side street "
                    "before sunrise. Onyx leads at front, broad-shouldered "
                    "clearing the path. Byte beside him with holo-tablet "
                    "softly glowing cyan, navigating. Agatha walks with KZ "
                    "next to her, her FOUR-fingered hand on KZ's shoulder "
                    "calming his overstimulated wide ONE eye. Jiggy in the "
                    "middle holding the golden-pale spark in front of him "
                    "as a guide. Luxa and Wiz at the rear. Empty street, "
                    "shuttered shops, low sodium streetlight pools. Cool "
                    "magenta sunrise rim from far end of street. Mood: "
                    "coral choreography, mission, breath held."
                ),
            },
            {
                "slug": "03-arrive-plaza",
                "characters": ["jiggy", "wiz", "agatha", "kz", "onyx", "byte", "luxa"],
                "refs": [JIGGY, WIZ, AGATHA, KZ, ONYX, BYTE, LUXA, GRATE],
                "scene": (
                    "Wide shot, 24mm lens, slight low angle. The clan of "
                    "seven Pax stands at the edge of a small ordinary "
                    "neighborhood plaza at sunrise — concrete benches, a "
                    "weathered ancient flat stone in the center (an old "
                    "andean ushnu integrated into the plaza), graffiti-"
                    "covered concrete walls bordering. They're tiny in the "
                    "open space. Jiggy in front holding the golden-pale "
                    "spark glowing warm. Each ONE central eye visible. The "
                    "soft pink-gold light of dawn floods the plaza. Mood: "
                    "arrival, ceremony, this is the place."
                ),
            },
            {
                "slug": "04-sami-painting-wall-mural",
                "characters": ["sami"],
                "refs": [GRATE, METRO],
                "scene": (
                    "Medium shot, 50mm lens, slight 3/4 from behind. Sami — "
                    "human latina teen with messy bun, hoodie, two normal "
                    "eyes — stands alone at the plaza wall finishing a large "
                    "mural in fluorescent magenta and turquoise spray paint. "
                    "The mural depicts a stylized Pax figure on one side "
                    "and a stylized human figure on the other, both with "
                    "their hands joined over a glowing crystal between them "
                    "(the same composition as the cap 2 fresco). She is "
                    "intent, focused. Behind her, paint cans on the ground. "
                    "Soft pink-gold dawn light, cool wall in shadow with "
                    "magenta paint glow. Mood: she has been preparing this "
                    "for them."
                ),
            },
            {
                "slug": "05-sami-turns-sees-clan",
                "characters": ["sami"],
                "refs": [GRATE],
                "scene": (
                    "Close-up, 85mm lens, frontal. Sami's face fills the "
                    "frame: TWO normal human eyes wide with awe and "
                    "recognition (not fear), spray can dropped from her "
                    "hand visible blurred at lower edge falling. She has "
                    "just turned around. Hood pushed back, dark hair messy. "
                    "Soft warm dawn light from her left. Mood: 'I knew you "
                    "were real'."
                ),
            },
            {
                "slug": "06-clan-faces-sami-frontal",
                "characters": ["jiggy", "kz", "onyx", "agatha", "byte", "luxa", "wiz"],
                "refs": [JIGGY, KZ, ONYX, AGATHA, BYTE, LUXA, WIZ, GRATE],
                "scene": (
                    "Wide-medium ensemble shot, 28mm lens, slight low angle "
                    "from Sami's POV (camera at her height). The seven Pax "
                    "stand frontally facing the camera in a loose row, "
                    "Jiggy slightly forward holding the golden-pale spark. "
                    "Each Pax has ONE central eye, FOUR fingers. Their "
                    "expressions vary: KZ openly curious mouth open small "
                    "smile, Wiz softly smiling for the first time, Agatha "
                    "calm-warm, Onyx alert, Byte respectful, Luxa amused, "
                    "Jiggy reverent. Soft pink-gold dawn light bathes them "
                    "from camera-right. Plaza wall mural visible behind. "
                    "Mood: visible without shame, the doctrine breaks."
                ),
            },
            {
                "slug": "07-cliffhanger-spark-fully-lit",
                "characters": ["jiggy"],
                "refs": [JIGGY, CAVE_STAL],
                "scene": (
                    "Extreme close-up, 100mm macro lens, locked-off. Jiggy's "
                    "open FOUR-fingered hand cradles the golden-pale spark, "
                    "which has just fully ignited — now glowing a deep "
                    "saturated warm gold-magenta, much brighter than before, "
                    "with internal subsurface light flowing through every "
                    "facet. Tiny dust particles swirl warmly around. Out of "
                    "focus behind: a hint of Sami and the clan's silhouettes "
                    "in soft warm glow. Mood: the anchor is alive again, "
                    "visibility itself was the missing charge."
                ),
            },
        ],
    },
    # =====================================================================
    # CAP 11 — La ruca de las rucas
    # =====================================================================
    11: {
        "title": "La ruca de las rucas",
        "shots": [
            {
                "slug": "01-sami-paints-new-stroke",
                "characters": ["sami"],
                "refs": [GRATE, METRO],
                "scene": (
                    "Close-up, 85mm lens, slight 3/4 angle. Sami's hand "
                    "(two-eyed implied — only her hand and lower face "
                    "visible) finishes painting the Pax circular-with-lines "
                    "glyph on a wall. With her other hand she now adds, in "
                    "single short decisive strokes, a NEW small geometric "
                    "trace next to it — a simple compact two-stroke "
                    "abstract mark (like a small angled line + dot, an "
                    "invented tally-style sigil, NOT a letter, NOT a real "
                    "logo). Spray paint dripping fluorescent magenta. Her "
                    "lips are slightly parted, focused. Warm afternoon "
                    "sodium light. Mood: deliberate invention of a new "
                    "shared sign."
                ),
                "extra_negative": (
                    "the new mark must be an invented abstract two-stroke "
                    "sigil, not a real letter or known symbol."
                ),
            },
            {
                "slug": "02-onyx-discovers-icecream",
                "characters": ["onyx"],
                "refs": [ONYX, GRATE],
                "scene": (
                    "Medium close-up, 50mm lens, slight low angle. Onyx — "
                    "tallest Pax, athletic, copper-and-turquoise bracelets, "
                    "ONE central eye — stands on a sunny street licking a "
                    "scoop of pink-and-cream ice cream on a cone. His ONE "
                    "central eye is wide with delighted surprise, mouth "
                    "open in mid-lick. A small drip of ice cream on his "
                    "wrist. Warm midday sunlight, blurred urban background. "
                    "Mood: comic relief, joyous discovery, a giant Pax "
                    "tasting sugar for the first time."
                ),
            },
            {
                "slug": "03-byte-sami-design-sign",
                "characters": ["byte", "sami"],
                "refs": [BYTE, GRATE],
                "scene": (
                    "Medium shot, 50mm lens, slight high angle (over-the-"
                    "table view). Byte (lime LED headphones, lime LEDs only "
                    "exclusive to him, ONE central eye) and Sami (human "
                    "latina teen, two normal eyes) sit across a small low "
                    "wooden cafe table strewn with sketches on paper "
                    "napkins. Byte's holo-tablet floats a translucent cyan "
                    "preview of the new two-stroke sigil. Sami draws "
                    "variations on a napkin with a pencil. Their two heads "
                    "lean inward over the table, collaborating. Warm "
                    "afternoon light, magenta neon spill from a far sign. "
                    "Mood: design partnership, gentle co-invention."
                ),
            },
            {
                "slug": "04-heriberto-draws-on-board",
                "characters": ["heriberto", "kid"],
                "refs": [GRATE],
                "scene": (
                    "Medium shot, 50mm lens, eye-level. The same balcony as "
                    "cap 4. Heriberto stands at his small green chalkboard, "
                    "two normal human eyes, vest unchanged. He has just "
                    "drawn the Pax glyph and the new two-stroke sigil next "
                    "to it on the board in white chalk. He turns toward the "
                    "three children sitting on the floor (two-eyed humans), "
                    "one of whom is already starting to copy the sigil into "
                    "their notebook. Warm afternoon light. Mood: the sign "
                    "spreads through the unaware."
                ),
            },
            {
                "slug": "05-mariela-draws-note-monitor",
                "characters": ["mariela"],
                "refs": [MARIELA, OFFICE],
                "scene": (
                    "Close-up, 85mm lens, slight high angle. Mariela's hand "
                    "(two-eyed human implied) draws the new two-stroke "
                    "sigil with a black pen on a small yellow sticky note "
                    "stuck on the side of her office monitor. Visible "
                    "behind the monitor: a screen showing a social media "
                    "feed thumbnail with a photo of a wall painted with the "
                    "Pax glyph and the same sigil (abstract, no readable "
                    "real-world content). She smiles softly to herself. "
                    "Cool office fluorescent light, warm desk lamp. Mood: "
                    "the sign reaches farther than the city it was born in."
                ),
                "extra_negative": (
                    "do not render readable real-world social media brands or "
                    "real text on the monitor; abstract feed only."
                ),
            },
            {
                "slug": "06-cavern-crystals-cascade",
                "characters": [],
                "refs": [CAVE_WIDE, CAVE_STAL],
                "scene": (
                    "Wide shot, 24mm lens, slow rising crane angle. The "
                    "central crystal cavern. Multiple crystals throughout "
                    "the cavern are lighting up in a cascading wave — "
                    "magenta light flowing from one to the next in a chain "
                    "across the cavern, not all at once. Pulses ripple "
                    "outward visibly. Dust motes catch the cascading glow. "
                    "Each crystal glows brighter than the previous. NO "
                    "characters in frame. Mood: chain reaction, the network "
                    "is awake, the system feeds itself."
                ),
            },
            {
                "slug": "07-cliffhanger-wiz-jiggy-smile",
                "characters": ["wiz", "jiggy"],
                "refs": [WIZ, JIGGY, CAVE_STAL],
                "scene": (
                    "Medium two-shot, 50mm lens, side angle. Wiz and Jiggy "
                    "stand side by side in the cavern, their faces in "
                    "profile turned slightly toward each other. Both ONE "
                    "central eye visible, both with small soft smiles, no "
                    "words exchanged. Behind them in deep focus, the largest "
                    "central crystal of the cavern is starting to vibrate "
                    "visibly with a faint growing magenta pulse, hairlines "
                    "of light running through it. Lighting: warm key from "
                    "the activating crystal behind them, soft cool ambient. "
                    "Mood: the silent acknowledgment between teacher and "
                    "student, and the threshold of activation."
                ),
            },
        ],
    },
    # =====================================================================
    # CAP 12 — Lo que aparece arriba
    # =====================================================================
    12: {
        "title": "Lo que aparece arriba",
        "shots": [
            {
                "slug": "01-wiz-hands-on-big-crystal",
                "characters": ["wiz"],
                "refs": [WIZ, CAVE_STAL],
                "scene": (
                    "Medium shot, 50mm lens, slight low angle. Wiz stands "
                    "before the largest central crystal of the cavern, "
                    "now glowing with a steady deep magenta pulse, taller "
                    "than him. His FOUR-fingered hands rest flat against "
                    "its surface in a ceremonial pose. His ONE central eye "
                    "is half-closed in concentration, white beard catching "
                    "magenta light, purple-velvet hooded cloak draped. "
                    "Behind him, blurred, the rest of the clan visible in "
                    "a half-circle. Lighting: bright magenta key from the "
                    "crystal, cool basalt rim. Mood: ritual, the activation "
                    "begins."
                ),
            },
            {
                "slug": "02-clan-channels-energy",
                "characters": ["wiz", "jiggy", "byte", "onyx", "agatha", "kz", "luxa"],
                "refs": [WIZ, JIGGY, BYTE, ONYX, AGATHA, KZ, LUXA, CAVE_STAL],
                "scene": (
                    "Wide ensemble shot, 28mm lens, slight low angle. The "
                    "seven Pax stand in a circle around the activating "
                    "central crystal. Their FOUR-fingered hands extended "
                    "outward palms up, ribbons of bright magenta-and-"
                    "turquoise energy flowing from the crystal through them "
                    "and outward upward to the cavern ceiling. Each Pax has "
                    "ONE central eye, expressions a mix of focus and awe. "
                    "Onyx and Byte channel the strongest streams; Jiggy, "
                    "KZ, Agatha and Luxa support; Wiz at the center. "
                    "Lighting: hyper-saturated magenta-turquoise from the "
                    "energy ribbons, warm amber spill on faces. Mood: "
                    "coral choreography, no single hero."
                ),
            },
            {
                "slug": "03-water-truck-village",
                "characters": [],
                "refs": [GRATE],
                "scene": (
                    "Wide shot, 35mm lens, slight low angle. A small dusty "
                    "rural village at golden-hour. A water truck has just "
                    "arrived, parked on a dry dirt road. People (humans, "
                    "two normal eyes — anonymous in slight blur) gather "
                    "with plastic jugs filling them from a tap. A child "
                    "watches with awe. Warm dust haze in golden afternoon "
                    "light. The Pax glyph visible faintly painted on the "
                    "side of the truck. NO Pax in frame. Mood: small "
                    "concrete miracle, the result above."
                ),
                "extra_negative": (
                    "do not render real-world brand logos on the truck — only "
                    "the abstract Pax glyph."
                ),
            },
            {
                "slug": "04-mariela-email-accepted",
                "characters": ["mariela"],
                "refs": [MARIELA, OFFICE],
                "scene": (
                    "Close-up, 85mm lens, slight high angle. Mariela sits "
                    "at her office desk, two normal human eyes wide with "
                    "joy, a small relieved smile breaking on her face. The "
                    "monitor in front of her shows an email window with a "
                    "green abstract checkmark/banner indicating acceptance "
                    "(do not render readable text). Her hand near her "
                    "mouth in a quiet gesture of disbelief-relief. Cool "
                    "office light, warm sunset orange streaming through "
                    "window behind her. NO Pax in frame. Mood: solo "
                    "private joy, the question paid off."
                ),
                "extra_negative": (
                    "do not render readable email text — only abstract banners "
                    "and a generic green check icon."
                ),
            },
            {
                "slug": "05-sami-paints-with-strangers",
                "characters": ["sami"],
                "refs": [GRATE, METRO],
                "scene": (
                    "Wide shot, 35mm lens, slight low angle. Sami at her "
                    "plaza wall mural, but no longer alone — three other "
                    "human strangers (two-eyed, varied ages and types, two "
                    "adults and a child, who don't know each other) are "
                    "painting the Pax glyph + the new two-stroke sigil on "
                    "different sections of the wall, each with their own "
                    "spray can or marker. Sami in middle ground turning to "
                    "look at one of them with a soft smile. Warm afternoon "
                    "sun. Mood: the meme spreads, strangers as kin, "
                    "decentralized."
                ),
            },
            {
                "slug": "06-coral-vignette-grid",
                "characters": [],
                "refs": [GRATE, METRO, OFFICE],
                "scene": (
                    "Composite split-screen visualization, 35mm equivalent, "
                    "soft transitions. Four small simultaneous vignettes "
                    "tiled in the frame: TOP-LEFT = a stray dog being lifted "
                    "into a woman's arms on a sidewalk (anonymous human, "
                    "two-eyed); TOP-RIGHT = a hand placing a phone with a "
                    "smiling text-message icon (no readable text) on a "
                    "lonely person's table; BOTTOM-LEFT = a doctor in "
                    "scrubs giving thumbs up to a family in a hospital "
                    "hallway (all humans two-eyed); BOTTOM-RIGHT = water "
                    "truck delivery from shot 3 reprised as small inset. "
                    "Each vignette has the Pax glyph subtly somewhere in "
                    "frame (a sticker, a chalk mark, a graffiti corner). "
                    "Warm golden-hour palette across all four. NO Pax in "
                    "any vignette. Mood: coral montage, small concrete "
                    "miracles in many places at once."
                ),
                "extra_negative": (
                    "do not render any readable real-world logos or text in "
                    "any of the four vignettes."
                ),
            },
            {
                "slug": "07-cliffhanger-sami-fourth-wall",
                "characters": ["sami"],
                "refs": [GRATE],
                "scene": (
                    "Close-up, 85mm lens, frontal head-on. Sami's face fills "
                    "the frame: TWO normal human eyes looking directly into "
                    "the camera lens (breaking the fourth wall), soft "
                    "knowing smile, dark hair messy. Her hand is raised in "
                    "front of her to chest level, drawing the new two-"
                    "stroke sigil in the air with her finger — the gesture "
                    "is mid-completion, finger trailing a faint translucent "
                    "magenta light residue (very subtle motion path of the "
                    "stroke). Soft warm golden hour light from camera-left. "
                    "Background: out-of-focus painted plaza wall. Mood: "
                    "invitation, you are the tribe."
                ),
            },
        ],
    },
}


# ---------------------------------------------------------------------------
# Build all jobs
# ---------------------------------------------------------------------------
def build_jobs(cap_filter=None):
    jobs = []
    for cap_num, cap_data in CAPS.items():
        if cap_filter and cap_num not in cap_filter:
            continue
        for shot in cap_data["shots"]:
            slug_full = f"cap-{cap_num}-shot-{shot['slug']}"
            out_path = os.path.join(OUT, f"{slug_full}.png")
            prompt = build_prompt(
                scene=shot["scene"],
                characters=shot["characters"],
                extra_negative=shot.get("extra_negative", ""),
            )
            jobs.append({
                "cap": cap_num,
                "slug": shot["slug"],
                "characters": shot["characters"],
                "refs": shot["refs"],
                "prompt": prompt,
                "input_image_paths": shot["refs"],
                "output_path": out_path,
                "size": shot.get("size", "1536x1024"),
                "quality": "low",
            })
    return jobs


def write_companion_md(job, model="gpt-image-2"):
    """Genera el .md companion despues de la generacion exitosa."""
    md_path = job["output_path"].replace(".png", ".md")
    rel_refs = "\n".join(
        f"- {os.path.relpath(r, ROOT)}" for r in job["refs"]
    )
    chars = ", ".join(job["characters"]) or "(ambiente solo)"
    md = (
        f"# Cap {job['cap']} — Shot {job['slug']}\n\n"
        f"**Personajes en frame:** {chars}\n\n"
        f"**References usadas (orden):**\n{rel_refs}\n\n"
        f"## Prompt completo\n\n```\n{job['prompt']}\n```\n\n"
        f"## Tech\n\n"
        f"- Modelo: {model}\n"
        f"- Quality: {job['quality']}\n"
        f"- Size: {job['size']}\n"
        f"- Generado por: scripts/gen_caps_3_to_12_async.py (paralelo asyncio)\n\n"
        f"---\n"
        f"canonization_status: pending_aldot_approval\n"
    )
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)


async def run(cap_filter=None, max_concurrent=8):
    jobs = build_jobs(cap_filter=cap_filter)
    total = len(jobs)
    print(f"[BATCH] {total} jobs total | concurrencia={max_concurrent}", flush=True)
    print(f"[BATCH] empezando wall-clock...", flush=True)
    t0 = time.time()
    results = await generate_batch_async(jobs, max_concurrent=max_concurrent)
    elapsed = time.time() - t0

    ok = 0
    failures = []
    for job, result in zip(jobs, results):
        if isinstance(result, Exception):
            failures.append((job, result))
            print(f"[ERR ] cap-{job['cap']}-shot-{job['slug']}: {type(result).__name__}: {result}", flush=True)
        else:
            ok += 1
            try:
                write_companion_md(job)
            except Exception as md_err:
                print(f"[WARN] md companion failed for {job['output_path']}: {md_err}", flush=True)

    print(f"\n[BATCH] {ok}/{total} OK | {len(failures)} ERRORS | {elapsed:.1f}s wall clock", flush=True)
    return {"ok": ok, "total": total, "elapsed": elapsed, "failures": failures}


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        cap_filter = None
    elif len(args) == 1:
        cap_filter = {int(args[0])}
    elif len(args) == 2:
        cap_filter = set(range(int(args[0]), int(args[1]) + 1))
    else:
        cap_filter = {int(a) for a in args}

    summary = asyncio.run(run(cap_filter=cap_filter, max_concurrent=8))
    print(f"\n[SUMMARY] {summary['ok']}/{summary['total']} OK in {summary['elapsed']:.1f}s")
    if summary["failures"]:
        print(f"[SUMMARY] failures:")
        for job, err in summary["failures"]:
            print(f"  cap-{job['cap']}-shot-{job['slug']}: {err}")
