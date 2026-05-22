"""
Sub-pipeline TEST — pre-generacion de assets faltantes (enemigo + hongos)
y consumo en escena final (Jiggy peleando enemigo en cueva con hongos).

Secuencia:
  1) IMG6: concept-pax-enemy.png       (asset canonico)
  2) IMG7: concept-pax-mushrooms.png   (asset canonico)
  3) IMG8: scene-jiggy-vs-enemy-mushroom-cave.png
            usa AMBOS pre-gens + jiggy.png + portada.png como references

Quality medium, size 1536x1024, modelo gpt-image-2.
"""
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor

# Asegurar imports del repo
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from scripts.openai_images import edit_image, generate_image  # noqa: E402

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PORTADA = os.path.join(ROOT, "public", "images", "portadas", "portada.png")
CAVE_WIDE = os.path.join(ROOT, "public", "images", "concepts", "concept-cave-wide-dark.png")
CAVE_STAL = os.path.join(ROOT, "public", "images", "concepts", "concept-cave-stalagmites-reawakening.png")
JIGGY = os.path.join(ROOT, "public", "images", "personajes", "jiggy.png")

OUT_ENEMY = os.path.join(ROOT, "public", "images", "concepts", "concept-pax-enemy.png")
OUT_MUSH = os.path.join(ROOT, "public", "images", "concepts", "concept-pax-mushrooms.png")
OUT_SCENE = os.path.join(ROOT, "content", "test-images", "scene-jiggy-vs-enemy-mushroom-cave.png")

SIZE = "1536x1024"
QUALITY = "medium"


# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------
PROMPT_ENEMY = """Concept art turn-around character sheet of a hostile native subterranean creature from the Pax universe. This entity is NOT a Pax — it does NOT share the friendly Pax silhouette: NO single central eye, NO turquoise skin, NO pointed elastic ears, NO 4-fingered humanoid hands. This is a different species, antagonistic.

CORE IDEA: an "anti-pulse" entity — a creature that feeds on the resonant transmuted energy that Pax beings cultivate. Its body literally absorbs and dampens light.

ANATOMY:
- Organic body with textures of black coral, opaque cracked crystal, fossilized obsidian-like growths.
- Multiple small clustered eyes (six to ten tiny eyes asymmetrically placed) — explicit visual contrast against the single-eyed Pax cyclops anatomy. Repeat: many small eyes, NEVER one big central eye.
- Branching limbs: a mix of jointed legs and tendril-like ramified tentacles (four to six total appendages).
- Hunched, low-slung quadruped/multiped posture, body roughly the size of a Pax or slightly larger but never titan-scale, never insect-tiny.
- Surface details: fine cracks glowing dim red-violet from within, like dying embers under stone.

PALETTE — ANTI-PALETTE vs canonical Pax jade-magenta:
- Dominant: deep basalt black, charcoal-grey coral textures, fractured obsidian.
- Glow accents: muted, low-intensity red-violet (NOT vibrant magenta, NOT jade, NOT amber). The glow looks sickly, suppressed, almost extinguished.

COMPOSITION:
- Character sheet turn-around: front view on the left, three-quarter view on the right, both standing on the same neutral basalt ground line.
- Subtle vertical guideline marks behind the figures (light grey grid).
- Background: flat neutral basalt-grey backdrop, no scenery, slight vignette.

MOOD: unsettling, ominous, predatory — but NOT horror gore, NO blood, NO viscera, NO fanged maw close-up. Family-show maintainable. Think "stylized antagonist creature for an animated series", not "horror film monster".

RENDER: stylized 3D animation with semi-realistic PBR shading and neon-magic lighting, matching the look of Image 1 (the Pax universe key art). NOT 2D, NOT painterly, NOT illustration, NOT anime, NOT photorealistic.

REFERENCE INTEGRATION:
- Image 1 (portada) provides the canonical Pax universe render base: 3D PBR neon-magic look. Match the rendering quality, lighting model and material treatment.
- Image 2 (concept-cave-wide-dark) provides atmosphere baseline: the kind of dark subterranean world this creature inhabits. Use it for tonal/material grounding only — do NOT place the creature inside that cave; the sheet stays on neutral basalt backdrop.

NEGATIVE PROMPT:
Do not draw a Pax-like creature. Do not give it a single central eye, turquoise skin, pointed elastic ears, 4-fingered humanoid hands, or 3.5-head humanoid proportions. Do not use vivid jade-green or vivid magenta as primary glow — keep the glow muted red-violet only. No 2D hand-drawn aesthetic, no painterly Studio Ghibli style, no anime stylization, no photorealistic skin, no horror gore, no blood, no fanged jaw close-up, no human anatomy, no insect/arthropod cliches like compound bug eyes or chitinous segmented exoskeleton, no generic dragon or demon tropes.
"""

PROMPT_MUSHROOMS = """Cinematic botanical illustration sheet of bioluminescent mushrooms native to the Pax subterranean caverns. Concept art style, NO characters in frame, only the flora.

CORE IDEA: 4 to 5 distinct mushroom species displayed as a natural organic grouping (not rigid grid panels). They should feel like a single coherent ecosystem study from the Pax universe.

SPECIES VARIATION:
1. A tall ceremonial "champignon" — large central specimen, broad cap with internal soft jade-green glow radiating from gills.
2. A cluster of tiny luminous mushrooms in groups of 8-12, warm amber internal glow.
3. A medium mushroom with a tall slender stem, cap patterned with concentric Pax sacred geometry (radial spirals, hexagonal tessellation), jade-green glow.
4. A short squat mushroom with a thick stem and shelf-like cap, amber glow underside.
5. A delicate translucent species with a bell-shaped cap, faint jade glow visible through the membrane.

DESIGN VOCABULARY:
- Caps carry subtle Pax sacred geometry patterns: radial spirals, hexagons, fine concentric line work — etched as natural pigment patterns, not painted graphics.
- Internal bioluminescence: light originates from inside the mushroom flesh, glowing softly through gills, stem, and translucent membranes. Jade-green dominant on some species, warm amber on others. Some species combine both.
- Material: organic, slightly damp, mineral-flecked — they feel grown out of basalt and crystal substrate, not generic forest fungi.

COMPOSITION:
- Organic natural grouping, varied scale, depth layering: foreground large specimen, mid-ground cluster, background smaller specimens fading into ambient haze.
- Rule of thirds anchoring the ceremonial champignon slightly off-center.
- Subtle environmental hints at base: small basalt pebbles, faint mineral crystals, but NO full cave scenery — this is a flora study sheet, not a landscape.
- Background: gradient from deep basalt-dark at edges to soft jade-tinted dim ambience near the specimens, low contrast vignette.

PALETTE — CANONICAL PAX:
- Jade-green and warm amber as the bioluminescent accents.
- Basalt-dark and charcoal as the substrate and background.
- Subtle neon-magenta hints permitted in micro-details (spore particles in air, edge fringes) but not dominant.

RENDER: stylized 3D animation with semi-realistic PBR shading and neon-magic lighting. NOT 2D, NOT painterly, NOT illustration, NOT anime, NOT photorealistic.

REFERENCE INTEGRATION:
- Image 1 (portada) provides the canonical Pax universe render base and palette anchor.
- Image 2 (concept-cave-stalagmites-reawakening) provides the cave + crystal material vocabulary and the way internal glow reads against basalt. Match that lighting language for the mushrooms.

NEGATIVE PROMPT:
No characters, no Pax beings, no humans, no creatures of any kind. No realistic photographic mushrooms. No 2D hand-drawn aesthetic, no painterly Studio Ghibli style, no anime, no flat illustration. No grid panels with hard borders — keep it as an organic study sheet. No bright daylight ambience — this is a subterranean dim-glow context. No psychedelic toxic-looking colors outside the canonical palette.
"""

PROMPT_SCENE = """A dynamic mid-shot composition: Jiggy, a Pax, in an agile defensive stance facing a hostile Pax-universe creature inside a bioluminescent mushroom cave.

IDENTITY LOCK — JIGGY (match Image 1 EXACTLY):
The protagonist is Jiggy, a Pax — a cyclops-type single-eyed humanoid. Repeat: ONE central eye, no second eye, no companion eye, no extra eye anywhere on the face. Cyclops-type anatomy. Turquoise/teal skin, elongated pointed elastic ears, FOUR fingers per hand (not five), 3.5-head proportions. He is a kin/peer of Image 1, NOT a different species, NOT human, NOT Andean indigenous, NOT a generic fantasy creature. Match Image 1 anatomy, costume design vocabulary and color treatment exactly. Do not add accessories, jewelry, bandanas, or props that are not present in Image 1.

IDENTITY LOCK — ENEMY (match Image 2 EXACTLY):
The antagonist creature is the Pax-universe anti-pulse entity defined in Image 2. Match its design language EXACTLY: organic body with black coral and cracked obsidian textures, MULTIPLE small clustered eyes (NOT one central eye, NOT human-style two eyes), branching jointed legs and tendril-like ramified tentacles, body roughly Jiggy-sized or slightly larger, dim red-violet internal glow through fine surface cracks. Do NOT redesign it, do NOT make it look like a Pax, do NOT give it a single central eye, do NOT give it turquoise skin.

ASSET LOCK — MUSHROOMS (match Image 3 EXACTLY):
The cavern is populated by the Pax bioluminescent mushroom species defined in Image 3. Match their species design EXACTLY: tall ceremonial champignon with broad cap, clusters of tiny amber-glow mushrooms, medium mushrooms with sacred-geometry patterned caps, short squat shelf-cap mushrooms, delicate translucent bell-shaped species. Maintain their internal jade-green and warm-amber bioluminescence. Do NOT invent different mushroom designs.

ACTION:
Jiggy is in an agile, low defensive-ready stance, slightly crouched. ONE hand holds aloft a glowing jade-green crystal shard, used as a weapon-shield combo, casting cool jade light onto his face and upper body. The OTHER hand extends outward to the side for balance. Body weight is shifted onto his lead foot. His single central eye is locked on the creature. Expression: focused, alert, brave but wary — Pax wonder-under-tension, not terror.

Facing him, the enemy creature crouches in a hostile predatory posture, tendrils raised and partially uncoiled, multiple small eyes glinting dim red-violet. Its dim glow contrasts visibly against Jiggy's clear jade glow.

ENVIRONMENT:
A subterranean cavern populated with the Pax mushroom species from Image 3. Foreground: a couple of medium mushrooms (slight blur, depth-of-field). Mid-ground: Jiggy left, enemy right, both in clear focus. Background: more mushrooms scattered through the cave interior, soft bokeh, basalt walls visible. Side-lighting comes from the mushrooms — jade-green from one side, warm amber from the other — wrapping the figures laterally.

COMPOSITION:
Medium shot, rule of thirds. Jiggy occupies the left third, the enemy occupies the right third, mushrooms anchor the foreground bottom-third and background. Slight low camera angle to add tension. Shallow depth of field with mushrooms in foreground softly blurred and background mushrooms in stronger bokeh, the two characters in sharp focus.

LIGHT + PALETTE:
Diegetic light sources: jade-green and warm-amber bioluminescence from the mushrooms (lateral wrap), plus the brighter jade glow from Jiggy's crystal as a key on his side, and the dim red-violet glow of the enemy as a low fill on the opposite side. Canonical Pax palette dominant: jade-green, warm-amber, basalt-dark, with neon-magenta micro-accents permitted (spore particles, distant fissure lines). The enemy keeps its anti-palette muted red-violet.

STYLE / RENDER:
Stylized 3D animation with semi-realistic PBR shading and neon-magic lighting. NOT 2D, NOT painterly, NOT illustration, NOT anime, NOT photorealistic. Match the look of Image 4 (portada) for render quality, lighting model, and material treatment.

REFERENCE INTEGRATION:
- Image 1: jiggy.png — IDENTITY LOCK for Jiggy. Match anatomy and costume EXACTLY.
- Image 2: concept-pax-enemy.png — IDENTITY LOCK for the antagonist creature. Match design EXACTLY.
- Image 3: concept-pax-mushrooms.png — ASSET LOCK for the mushroom flora populating the cave. Match species designs EXACTLY.
- Image 4: portada.png — render base + canonical palette anchor. Match style and palette.

MOOD: tension and Pax-wonder coexisting. Cinematic but not horror-gore, family-show maintainable, no blood, no graphic violence, no grotesque body horror.

NEGATIVE PROMPT:
Do not draw Jiggy with two eyes (he has ONE central eye, cyclops-type). Do not draw the enemy with a single central eye, do not give it turquoise skin or Pax silhouette. Do not redesign the mushrooms — match Image 3 exactly. Do not add accessories, jewelry, bandanas, or props on Jiggy that are not in Image 1. No 2D hand-drawn aesthetic, no painterly Studio Ghibli style, no anime stylization, no photorealistic skin. No five-fingered hands on Jiggy. No generic fantasy creature tropes for the enemy. No daylight ambience. No human characters in frame. No horror gore, no blood, no fanged jaw close-ups, no body horror.
"""


# ---------------------------------------------------------------------------
# Ejecucion
# ---------------------------------------------------------------------------
def gen_enemy():
    print("[ENEMY] generating concept-pax-enemy.png ...")
    t0 = time.time()
    out = edit_image(
        prompt=PROMPT_ENEMY,
        input_image_paths=[PORTADA, CAVE_WIDE],
        output_path=OUT_ENEMY,
        size=SIZE,
        quality=QUALITY,
    )
    dt = time.time() - t0
    print(f"[ENEMY] done in {dt:.1f}s -> {out}")
    return out


def gen_mushrooms():
    print("[MUSH] generating concept-pax-mushrooms.png ...")
    t0 = time.time()
    out = edit_image(
        prompt=PROMPT_MUSHROOMS,
        input_image_paths=[PORTADA, CAVE_STAL],
        output_path=OUT_MUSH,
        size=SIZE,
        quality=QUALITY,
    )
    dt = time.time() - t0
    print(f"[MUSH] done in {dt:.1f}s -> {out}")
    return out


def gen_scene():
    print("[SCENE] generating scene-jiggy-vs-enemy-mushroom-cave.png ...")
    t0 = time.time()
    out = edit_image(
        prompt=PROMPT_SCENE,
        input_image_paths=[JIGGY, OUT_ENEMY, OUT_MUSH, PORTADA],
        output_path=OUT_SCENE,
        size=SIZE,
        quality=QUALITY,
    )
    dt = time.time() - t0
    print(f"[SCENE] done in {dt:.1f}s -> {out}")
    return out


def main():
    overall_t0 = time.time()
    # Paso A: pre-gen en paralelo (enemigo + hongos)
    with ThreadPoolExecutor(max_workers=2) as ex:
        f_enemy = ex.submit(gen_enemy)
        f_mush = ex.submit(gen_mushrooms)
        enemy_path = f_enemy.result()
        mush_path = f_mush.result()

    # Paso B: escena final (consume los pre-gens)
    if not os.path.exists(enemy_path) or not os.path.exists(mush_path):
        raise RuntimeError("pre-gens missing, abort scene")
    scene_path = gen_scene()

    overall_dt = time.time() - overall_t0
    print("\n=== DONE ===")
    print(f"enemy:    {enemy_path}")
    print(f"mush:     {mush_path}")
    print(f"scene:    {scene_path}")
    print(f"total:    {overall_dt:.1f}s")


if __name__ == "__main__":
    main()
