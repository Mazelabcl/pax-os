"""
Genera 15 shots del Cap 2 "El templo que nadie cuidó" en quality=low.
Cada shot tiene IDENTITY LOCK reforzado (1 ojo central, 4 dedos, anti dual-pupil).
Lectura del prompt construido per-shot abajo en SHOTS.

Uso:
    python scripts/gen_cap2_storyboard.py 1     # genera solo shot 1
    python scripts/gen_cap2_storyboard.py 1 5   # shots 1..5
    python scripts/gen_cap2_storyboard.py all   # los 15
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from scripts.openai_images import edit_image  # noqa: E402

PERSONAJES = os.path.join(ROOT, "public", "images", "personajes")
CONCEPTS = os.path.join(ROOT, "public", "images", "concepts")
OUT = os.path.join(ROOT, "content", "storyboards")
os.makedirs(OUT, exist_ok=True)

# Refs por personaje
JIGGY = os.path.join(PERSONAJES, "jiggy.png")
WIZ = os.path.join(PERSONAJES, "wiz.png")
BYTE = os.path.join(PERSONAJES, "byte.png")
LUXA = os.path.join(PERSONAJES, "luxa.png")
KZ = os.path.join(PERSONAJES, "kz.png")
ONYX = os.path.join(PERSONAJES, "onyx.png")
AGATHA = os.path.join(PERSONAJES, "agatha.png")
CAVE_WIDE = os.path.join(CONCEPTS, "concept-cave-wide-dark.png")
CAVE_STAL = os.path.join(CONCEPTS, "concept-cave-stalagmites-reawakening.png")

# ---------------------------------------------------------------------------
# IDENTITY LOCK universal — el bloque MÁS reforzado contra dual-pupil bug.
# ---------------------------------------------------------------------------
IDENTITY_LOCK = (
    "IDENTITY LOCK — CRITICAL: All characters in this scene are Pax, a non-human "
    "subterranean cyclops-type civilization. Each Pax has ONE single central eye "
    "(cyclops anatomy), ONE pupil only, located inside the white area of that ONE "
    "eye. Do NOT draw two eyes. Do NOT draw two pupils. Do NOT draw two eye lines. "
    "Do NOT draw a second small eye anywhere on the face. Repeat: ONE eye total, "
    "ONE pupil total, per Pax character. Their reference char sheets are provided "
    "as Image inputs — match the proportions, skin tone, ear shape (elongated "
    "elastic pointed), and the FOUR fingers per hand exactly. They are 3 to 3.5 "
    "heads tall (KZ shortest at 1.05m, Onyx tallest at 1.70m). "
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
    "fantasy battle clichés, game HUD, thriller vignette, glamour beauty shot, "
    "loading-screen blinking pulse, two eyes per Pax, dual pupils, cartoon "
    "two-dot eyes on a Pax, accessories not present in reference char sheets."
)

WARDROBE = {
    "jiggy": "Jiggy wears the leather harness with magenta crystal pendant from his char sheet (Image labeled Jiggy). Turquoise-teal skin, ONE central eye with turquoise iris and large round pupil.",
    "wiz": "Wiz is the elder: long white beard, deep purple-velvet hooded cloak with magenta crystal pendant, holds a wooden staff topped with magenta crystal. Slightly shorter, rounder proportions (2.8-3 heads). ONE central eye.",
    "byte": "Byte wears the lime-green LED neural headphones (the lime LEDs are EXCLUSIVE to Byte — no other Pax wears lime), tech hoodie with digital code patterns in jade-cyan. ONE central eye. Carries a small holo-tablet.",
    "luxa": "Luxa wears the purple bandana with golden detail and woven multicolor scarf, carries a warm-gold crystal lantern. Turquoise skin with subtle self-emission. ONE central eye.",
    "kz": "KZ is the smallest of the clan (1.05m), wearing a magenta-purple bandana with tribal beaded accessories and a magenta heart-shaped crystal pendant on chest. Innocent expression. ONE central eye.",
    "onyx": "Onyx is the tallest and most athletic (1.70m), bare strong torso with leather short kilt, copper-and-turquoise wrist bracelets, tribal markings on shoulders. ONE central eye.",
    "agatha": "Agatha has LIME-GREEN skin (NOT turquoise — emphasized lime, more yellow-green), long dark dreadlocks, wears a long flowing purple ceremonial robe with jade trim. Maternal, calm expression. ONE central eye.",
}


def build_prompt(scene_block: str, characters: list[str], extra_negative: str = "") -> str:
    wardrobe_lines = "\n".join(WARDROBE[c] for c in characters)
    return (
        IDENTITY_LOCK
        + "\n\nWardrobe and identity per character (match the provided char sheet images exactly):\n"
        + wardrobe_lines
        + "\n\nSCENE: "
        + scene_block
        + "\n\n"
        + STYLE_BLOCK
        + (f" Additional negative for this shot: {extra_negative}" if extra_negative else "")
    )


# ---------------------------------------------------------------------------
# 15 shots
# ---------------------------------------------------------------------------
SHOTS = [
    # 01 — Hook: Jiggy corriendo por túnel
    {
        "slug": "01-jiggy-running-tunnel",
        "characters": ["jiggy"],
        "refs": [JIGGY, CAVE_WIDE],
        "scene": (
            "Wide tracking shot, side angle, 28mm lens, lateral camera movement. "
            "Jiggy mid-stride running fast along a narrow rocky tunnel, leather harness "
            "and magenta crystal pendant bouncing with momentum. The tunnel walls are "
            "rough basalt with subtle magenta crystal veins emitting soft glow. Volumetric "
            "dust trailing behind him from his run. Composition: Jiggy on left third, the "
            "tunnel opening dark on the right third, leading lines of the rock walls "
            "converging. Lighting: rim magenta from crystal veins behind, fill turquoise "
            "from somewhere ahead off-frame."
        ),
        "size": "1536x1024",
    },
    # 02 — Hook: KZ choca con pared de raíces
    {
        "slug": "02-kz-collision-roots",
        "characters": ["kz"],
        "refs": [KZ, CAVE_WIDE],
        "scene": (
            "Medium shot, slight low angle, 35mm lens, locked-off. KZ — the smallest Pax "
            "of the clan with magenta-purple bandana and heart-crystal pendant — has just "
            "collided face-first into a wall of thick organic dark roots interwoven with "
            "earth and dust. Golden-amber dust particles explode outward in slow-motion "
            "around his head and shoulders. His expression: surprised cartoon wide-eye, "
            "mouth open in a small 'oh'. The wall is starting to crack and crumble. "
            "Composition: KZ centered slightly low, dust-burst filling upper third. "
            "Lighting: warm golden dust catching backlight, cool turquoise rim from tunnel behind."
        ),
        "size": "1536x1024",
    },
    # 03 — Pared cae, revela cámara antigua
    {
        "slug": "03-wall-collapse-reveal",
        "characters": ["kz", "jiggy"],
        "refs": [KZ, JIGGY, CAVE_STAL],
        "scene": (
            "Wide reveal shot, 24mm wide lens, slight low angle. The wall of roots and "
            "earth is collapsing in chunks, revealing a vast ancient chamber beyond — "
            "a forgotten Pax temple full of dormant crystals, golden-amber dust hanging "
            "in dense suspension, ancient stone carved walls visible in the background. "
            "KZ in the foreground left, recovering on hands and knees; Jiggy entering "
            "from foreground right with cautious stance. Both small in scale against the "
            "massive revealed chamber. Lighting: god rays of pale-cyan filtering through "
            "the new opening, dim magenta-amber ambient from dormant crystals deeper inside."
        ),
        "size": "1536x1024",
    },
    # 04 — Templo plano amplio
    {
        "slug": "04-temple-wide-establishing",
        "characters": [],
        "refs": [CAVE_STAL, CAVE_WIDE],
        "scene": (
            "Establishing wide shot, 24mm, slow descending crane perspective. An ancient "
            "abandoned Pax temple chamber — vaulted rocky ceiling with mineral veins, "
            "circular arrangement of dormant gray-purple crystals on stone pedestals, "
            "a central ceremonial dais of weathered carved stone, walls covered with "
            "faded multicolor frescoes depicting figures and crystals. Heavy golden-dusty "
            "atmosphere with thick volumetric haze, god-ray shafts from cracks in the "
            "ceiling, layers of dust on every surface. NO characters in frame — pure "
            "environment shot. Composition: rule of thirds with the dais on lower third, "
            "ceiling frescoes catching upper third light. Mood: contemplative, mystical, "
            "abandoned-but-sacred."
        ),
        "size": "1536x1024",
    },
    # 05 — Clan entrando con cautela
    {
        "slug": "05-clan-entering-temple",
        "characters": ["wiz", "byte", "jiggy", "kz"],
        "refs": [WIZ, BYTE, JIGGY, KZ],
        "scene": (
            "Medium-wide group shot, 35mm lens, locked-off slight low angle. Four Pax "
            "entering the ancient temple chamber from a broken-wall opening, in cautious "
            "exploratory poses. From left to right: Wiz (the elder with white beard, "
            "purple cloak, crystal staff held forward as illumination), Byte (with lime-green "
            "LED headphones glowing, holo-tablet scanning), Jiggy (forward leaning, magenta "
            "crystal pendant visible), KZ (small, peeking from behind Jiggy with curious eyes). "
            "Each character is small against the large dim chamber. Wiz's staff casts a soft "
            "magenta light pool on the dusty stone floor. Composition: rule of thirds, the "
            "clan grouped on left two-thirds, vast dark chamber opening on right third. "
            "Lighting: magenta from staff, cool turquoise rim from tunnel behind."
        ),
        "size": "1536x1024",
    },
    # 06 — Byte limpia inscripciones
    {
        "slug": "06-byte-cleaning-inscriptions",
        "characters": ["byte"],
        "refs": [BYTE, CAVE_STAL],
        "scene": (
            "Medium close-up, 50mm lens, slight 3/4 angle from side. Byte — the tech-Pax "
            "with lime-green LED headphones (LEDs glowing softly) and tech hoodie with "
            "digital cyan-code patterns — is gently brushing dust off an ancient stone "
            "wall covered in carved inscriptions. His ONE central eye is wide with focus, "
            "iris turquoise. He uses a small holo-tablet in one hand emitting a soft cyan "
            "scan-line over the wall. The inscriptions revealed are intricate geometric "
            "patterns mixed with what appear to be ancient human glyphs (abstract — do not "
            "render specific real-world script). Lighting: cyan from his tablet on the wall, "
            "warm amber ambient from dormant crystals far behind. Mood: archeological awe."
        ),
        "size": "1536x1024",
    },
    # 07 — Fresco de humanos+Pax cargando cristal juntos
    {
        "slug": "07-fresco-humans-pax-together",
        "characters": [],
        "refs": [CAVE_STAL, CAVE_WIDE],
        "scene": (
            "Medium shot of an ancient temple wall fresco, 50mm lens, slight angle "
            "showing the wall in 3/4 perspective. The fresco depicts stylized figures in "
            "weathered earthy pigment colors — on one side, two cyclops-type Pax figures "
            "(ONE eye each, turquoise skin tone faded), on the other side, two human-like "
            "figures with full faces (two eyes — these are humans, not Pax), and in the "
            "center between them, both groups have hands extended together holding a "
            "glowing magenta crystal between them. The composition of the fresco is "
            "ceremonial, symmetrical, like an old religious mural. The mural shows wear, "
            "cracks, faded color. Lighting on the wall: warm amber from a dormant crystal "
            "off-frame casting raking light, dust motes drifting across. NO live characters "
            "in foreground — this is a still pictorial shot of the wall art."
        ),
        "size": "1536x1024",
        "extra_negative": "do not render the figures in the fresco as realistic; they are weathered ancient mural style.",
    },
    # 08 — Close-up multilingual inscriptions
    {
        "slug": "08-byte-detail-multilingual",
        "characters": [],
        "refs": [CAVE_STAL],
        "scene": (
            "Extreme macro close-up, 100mm macro lens, locked-off. A close-up of carved "
            "stone inscriptions on ancient temple wall. The carvings are abstract glyphs "
            "in three distinct visual languages mixed together: blocky angular Maya-inspired "
            "stepped glyphs, flowing knot-like Quechua-inspired patterns, and bold linear "
            "Rapa-Nui-inspired figures (do NOT replicate real scripts — use abstract "
            "stylized non-readable equivalents). The three styles are interwoven into a "
            "single inscription panel, suggesting a multicultural ancient cooperation. "
            "Stone is rough basalt with mineral veins, faint golden dust caught in the "
            "carved grooves. Lighting: a single beam of pale-cyan light raking across "
            "the stone from upper-left, revealing depth of the carvings. NO characters "
            "in frame. Mood: archeological revelation."
        ),
        "size": "1536x1024",
    },
    # 09 — Wiz reconoce el lugar
    {
        "slug": "09-wiz-recognition",
        "characters": ["wiz"],
        "refs": [WIZ, CAVE_STAL],
        "scene": (
            "Close-up, 85mm lens, slight low angle, locked-off. Wiz — the elder Pax with "
            "long white beard, purple-velvet hooded cloak, magenta crystal pendant — "
            "stands before the temple wall (out of focus behind). His ONE central eye is "
            "narrowed with deep recognition and old memory, a slight gleam reflecting "
            "magenta light. His expression: he has seen this before, decades or generations "
            "ago. His left hand reaches up, fingers extended (FOUR fingers visible) to "
            "almost-but-not-quite touch the stone. Lighting: warm amber rim from a side "
            "crystal source, cool magenta backlight outlining his cloak silhouette. "
            "Background: temple wall fresco out-of-focus suggesting figures and a crystal. "
            "Mood: contemplative, mystical, ancestral memory."
        ),
        "size": "1536x1024",
    },
    # 10 — Agatha llega y observa
    {
        "slug": "10-agatha-arrives-observes",
        "characters": ["agatha"],
        "refs": [AGATHA, CAVE_STAL],
        "scene": (
            "Medium shot, 50mm lens, slight 3/4 from behind-right. Agatha — Pax with "
            "LIME-GREEN skin (clearly more yellow-green than the turquoise of other Pax — "
            "lime, not teal), long dark dreadlocks, flowing long purple ceremonial robe "
            "with jade trim — stands quietly in front of the wall fresco, observing it "
            "for a long moment. Her ONE central eye is calm, contemplative, with a "
            "single subtle highlight of moisture (not crying, just deeply moved). Her "
            "FOUR-fingered hands rest folded in front of her. The fresco of humans+Pax "
            "with the crystal is visible behind her, slightly out of focus. Lighting: "
            "soft jade from above, warm amber rim from off-frame crystal. Mood: profound, "
            "spiritual, recognition of something lost."
        ),
        "size": "1536x1024",
    },
    # 11 — Agatha realization line
    {
        "slug": "11-agatha-realization-line",
        "characters": ["agatha"],
        "refs": [AGATHA, CAVE_STAL],
        "scene": (
            "Close-up, 85mm lens, frontal slight 3/4. Agatha's face fills most of the "
            "frame: LIME-GREEN skin (emphasized yellow-green, not teal), ONE central eye "
            "looking off-camera with serene gravity, lips slightly parted as if just "
            "having spoken. A single dreadlock falls beside her face. Her expression: "
            "she has just said the line that nobody else wanted to say — calm, sad, "
            "wise. Her ONE eye holds the weight of historical memory. Lighting: soft "
            "key from upper-left in cool jade tone, warm amber rim from right shoulder. "
            "Background: out-of-focus fresco fragments suggesting human and Pax figures "
            "in faded pigment. Slight film grain. Mood: epiphany, gentle melancholy."
        ),
        "size": "1024x1024",
    },
    # 12 — Luxa rompe la tensión
    {
        "slug": "12-luxa-breaks-tension",
        "characters": ["luxa"],
        "refs": [LUXA, CAVE_STAL],
        "scene": (
            "Medium shot, 50mm lens, slight low angle. Luxa — Pax with purple-and-gold "
            "bandana, woven multicolor scarf, carrying her warm-gold crystal lantern in "
            "one hand — stands relaxed with weight on one hip in the temple chamber. "
            "Her ONE central eye is half-closed with mischievous good humor, a small "
            "lopsided grin on her mouth. She has just made a brief joke that landed and "
            "broke the heavy silence. Her free hand gestures lightly outward in a 'eh, "
            "what can you do' shrug. Background: dim temple, fresco visible out-of-focus. "
            "Lighting: warm gold from her lantern catching her face from below, cool "
            "magenta rim from the chamber. Mood: comic relief that lands tender, not "
            "loud — she is the necessary breath."
        ),
        "size": "1536x1024",
    },
    # 13 — KZ toca cristal viejo, parpadeo
    {
        "slug": "13-kz-touches-old-crystal",
        "characters": ["kz"],
        "refs": [KZ, CAVE_STAL],
        "scene": (
            "Close-up, 85mm lens, side angle. KZ — the smallest Pax with magenta-purple "
            "bandana and heart-shaped magenta crystal pendant on his chest — has placed "
            "his small FOUR-fingered hand gently against the side of an old dormant "
            "crystal mounted on a stone pedestal. The crystal, mostly dark-gray-purple, "
            "has just emitted a single faint magenta spark/blink right at the point of "
            "contact, light flowing as a tiny trail up his arm and reflecting in his "
            "ONE central eye, which is wide and surprised in a tender way. Lighting: "
            "the crystal-spark provides the key light, warm amber ambient elsewhere. "
            "Composition: KZ on left third, crystal pedestal on right third. Mood: "
            "tender wonder, the dormant is not dead."
        ),
        "size": "1536x1024",
    },
    # 14 — Byte: inscripción final "el que carga no carga solo"
    {
        "slug": "14-byte-final-inscription",
        "characters": ["byte"],
        "refs": [BYTE, CAVE_STAL],
        "scene": (
            "Medium close-up over-the-shoulder, 50mm lens, locked-off. Byte (back-3/4 "
            "view, lime-green LED headphones glowing, hoodie with cyan code patterns "
            "visible) is reading a single carved inscription panel on the temple wall, "
            "now cleaned of dust. The inscription is a single line of stylized abstract "
            "carved glyphs (do NOT render readable text — only abstract carved geometry) "
            "subtly highlighted by a soft cyan scan-glow from his holo-tablet held below "
            "frame. The panel is centered in the frame past Byte's shoulder. Lighting: "
            "cyan from tablet on the wall, warm amber rim ambient. Mood: the moment of "
            "translating a key sentence; a heavy realization about to land."
        ),
        "size": "1536x1024",
    },
    # 15 — Cliffhanger: símbolo del templo coincide con grafiti exterior
    {
        "slug": "15-cliffhanger-graffiti-symbol",
        "characters": ["jiggy"],
        "refs": [JIGGY, CAVE_WIDE],
        "scene": (
            "Medium-wide shot, 35mm lens, slight low angle. Jiggy stands at the mouth of "
            "an exit tunnel back toward the surface, looking off to camera-left at a "
            "rough wall surface where, scratched into the basalt, there is a small "
            "stylized geometric symbol — abstract circular-with-lines glyph (not a real "
            "logo, an invented Pax-temple symbol). On a separate panel of wall to the "
            "right (split-composition or overlay-style transition), the SAME symbol "
            "appears spray-painted in modern fluorescent orange-magenta as graffiti on "
            "an urban concrete wall. Both versions of the symbol are visible in the "
            "frame as a visual rhyme — ancient carving on left third, modern graffiti "
            "on right third — Jiggy in the foreground left looking right toward the "
            "rhyme. His ONE central eye widens with realization. Lighting: warm amber "
            "from temple side, cool sodium-orange from urban side. Mood: cliffhanger "
            "discovery, the past and present are the same symbol."
        ),
        "size": "1536x1024",
        "extra_negative": "do not render real-world brand logos or readable letters; only abstract invented glyph.",
    },
]


def gen_one(shot: dict) -> str:
    slug = shot["slug"]
    out_path = os.path.join(OUT, f"cap-2-shot-{slug}.png")
    prompt = build_prompt(
        scene_block=shot["scene"],
        characters=shot["characters"],
        extra_negative=shot.get("extra_negative", ""),
    )
    print(f"[gen] cap-2-shot-{slug} -> {out_path}", flush=True)
    edit_image(
        prompt=prompt,
        input_image_paths=shot["refs"],
        output_path=out_path,
        size=shot.get("size", "1536x1024"),
        quality="low",
    )
    # Companion .md
    md_path = out_path.replace(".png", ".md")
    md = (
        f"# Cap 2 — Shot {slug}\n\n"
        f"**Personajes en frame:** {', '.join(shot['characters']) or '(ambiente solo)'}\n\n"
        f"**References usadas (orden):**\n"
        + "\n".join(f"- {os.path.relpath(r, ROOT)}" for r in shot["refs"])
        + "\n\n## Prompt completo\n\n```\n"
        + prompt
        + "\n```\n\n## Tech\n\n- Modelo: gpt-image-2\n- Quality: low\n"
        f"- Size: {shot.get('size', '1536x1024')}\n"
        "- Generado por: scripts/gen_cap2_storyboard.py\n"
    )
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"[ok]  cap-2-shot-{slug}", flush=True)
    return out_path


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args == ["all"]:
        targets = list(range(1, 16))
    elif len(args) == 1:
        targets = [int(args[0])]
    elif len(args) == 2:
        targets = list(range(int(args[0]), int(args[1]) + 1))
    else:
        # lista explícita
        targets = [int(a) for a in args]

    for i in targets:
        if i < 1 or i > len(SHOTS):
            print(f"[skip] {i} out of range")
            continue
        try:
            gen_one(SHOTS[i - 1])
        except Exception as e:
            print(f"[ERR] shot {i}: {e}", flush=True)
