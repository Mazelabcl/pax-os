"""
Regeneracion quirurgica de la imagen ancla 1 ("piedra apagandose") R3.

Diagnostico R2: el prompt anterior describio al chasqui como humano andino y
el modelo entrego un humano de superficie (dos ojos, vestimenta indigena).
Pero segun el lore v4 (`content/v2/lore.md`) y el char sheet canonico
(`content/personajes/_canon.md`), los Pax son la civilizacion subterranea
ciclope (un solo ojo central, piel turquesa #21D8B6, proporcion 3-3.5
cabezas). El chasqui Apu del cold open es un Pax (no un humano andino).

R3 fuerza la identidad visual con:
- Image 1 = jiggy.png (char sheet del corredor canonico) — el primer slot va
  al char sheet especifico para que el modelo aplique anatomia Pax (ojo
  unico, piel turquesa, proporcion 3-3.5 cabezas, orejas elasticas).
- Image 2 = wiz.png (Apu anciano) — segundo char-lock que refuerza
  "ciclope Pax" y el oficio Apu (ambos viven en cuevas con cristales).
- Image 3 = concept-cave-wide-dark.png — geometria + paleta + iluminacion
  canonicas de la caverna Apu fading.
- Image 4 = portada.png — paleta neon-magic Pax y bloom emisivo.
- Bloque de identidad EXPLICITO al inicio del prompt.
- Negative prompt explicito anti-humano-de-superficie.
"""

import os
import sys

# Permite importar openai_images cuando el script se corre con cwd = repo root
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from openai_images import edit_image  # noqa: E402

REPO = os.path.dirname(HERE)


def abs_path(*parts: str) -> str:
    return os.path.join(REPO, *parts)


PROMPT_R3 = """\
IDENTITY LOCK — READ FIRST. The character in this scene is a young Pax of \
the Apu nation, a member of the subterranean cyclops civilization shown in \
Image 1 (Jiggy character sheet) and Image 2 (Wiz/Orin character sheet). The \
character is NOT a human surface dweller, NOT an Andean indigenous person, \
NOT a mestizo, NOT a generic poncho-wearing figure, NOT an ethnographic \
subject, NOT photorealistic, NOT a documentary photograph. The character \
must visually match the cast in Image 1 and Image 2 with the SAME visual \
grammar: ONE single large central eye (no second eye, no two eyes — a \
single cyclops eye occupying ~35 percent of the face), turquoise-cyan skin \
hex 21D8B6 with subsurface scattering, expressive single eyebrow above the \
single eye, elastic pointed elf-like ears curved backward, small elastic \
mouth, rounded cyclops cranium, proportions of 3 to 3.5 heads tall \
(juvenile-cartoon proportions like Jiggy in Image 1, NOT realistic adult \
human proportions), four-fingered cartoon hand with no marked knuckles. \
This character is a kin and peer of Image 1 — a young Apu chasqui (Pax \
runner of the Andean nation, a cyclops), not a different species or \
ethnicity.

SCENE. The young Pax Apu chasqui sits cross-legged inside a circular \
cave-altar carved from dark volcanic basalt with thin moribund turquoise \
mineral veins; in his open right four-fingered turquoise hand rests an \
elongated kuya crystal the size of a closed fist, its fibrous interior — \
organ-like, not faceted — in the act of inverting: micro-rays of dying \
copper-amber light retracting back into the core like a thread being wound, \
hairline cooling cracks barely visible on the worn surface, the stone going \
dark.

COMPOSITION. Medium-low shot at knee height, slightly low-angle so the cave \
swallows the figure from above; the turquoise four-fingered hand holding \
the kuya occupies the geometric center of the frame, the Pax runner's face \
is fragmented and mostly in shadow against a basalt column, his single \
cyclops eye partially closed in concentration (not glowing — just tired), \
a half-relief carving of an Andean condor and a faint chakana stepped-cross \
pattern dissolved into the back wall's penumbra. The runner wears a short \
raw-cream undyed wool unku-style tunic with visible irregular fibers, a \
frayed sisal cord at the wrist, simple sandals — no decorative pectoral, \
no amulets, no folkloric saturated patterns. He is operative, not \
ceremonial. Apu chasquis are austere working runners, not ornamental \
shamans.

LIGHTING. The only diegetic light source in the frame is the kuya itself — \
warm dying copper around 2400K, falling on the turquoise hand, the \
turquoise forearm, the jawline, the cheekbone, leaving everything else in \
deep amber-black penumbra; no fill light, no rim light from outside the \
kuya, no ambient global. Subsurface scattering visible on the runner's \
turquoise Pax skin catching the dying light (the turquoise reads cooler \
under the dying copper — a desaturated jade-amber blend). A single mote of \
dust hangs suspended mid-fall near the runner's pointed ear, unnaturally \
still — the impossible detail that signals something deeper than physics \
has just failed.

PALETTE. Basalt near-black hex 1A1612 dominant (~50%), burned amber hex \
3D2A1A (~22%), faded copper hex 6B4A2C on the kuya emission (~12%), dying \
turquoise hex 1C5C5A in the column veins (~6%), desaturated turquoise Pax \
skin hex 21D8B6 muted by dying copper light (~8%), one warm highlight hex \
D4A574 on the cheekbone (~2%). Saturation deliberately low across the \
frame except for the kuya emission (which is also dying).

MATERIALS. Porous matte volcanic basalt with glassy turquoise mineral \
veining, smooth turquoise Pax skin with subtle subsurface scattering \
(canonical Pax cyclops skin from Image 1 / Image 2 — NOT human skin), raw \
cream wool unku tunic with visible irregular fibers and slight specular \
highlights on weave, frayed sisal cord at wrist with worn fibers, fibrous \
translucent kuya interior with hairline cooling cracks and copper-amber \
internal subsurface emission inverting inward — the kuya is closer to a \
living organ in cooling than a faceted gem.

STYLE. Stylized 3D animation, semi-realistic PBR shading with subsurface \
scattering on Pax cyclops skin and on basalt stone, expressive cartoon \
proportions matching Jiggy in Image 1 (3 to 3.5 heads tall, juvenile Pax \
build), high-contrast cinematic lighting with the single dying emissive \
crystal as the primary light source, painterly volumetric background with \
dense suspended dust motes and faint god-rays from above the runner barely \
cutting through, slight film grain, color grading in the dark amber-basalt \
complementary, 16:9 reads as premium mobile-game cinematic / animated key \
art — same render base as the cast shown in Image 1 and Image 2.

REFERENCE INTEGRATION. Image 1 (Jiggy character sheet) is the PRIMARY \
identity lock: the runner's anatomy, ethnicity, species, proportions, \
single cyclops eye, turquoise skin, four-fingered hands and pointed elastic \
ears must match Jiggy exactly — this is a peer of Jiggy, a young Pax of \
the same species, only with Apu-chasqui cultural costume (raw wool unku, \
sisal cord) instead of Jiggy's leather harness. Image 2 (Wiz/Orin \
character sheet) reinforces the cyclops Pax identity and the Apu cultural \
context (cave-altar, crystals, ceremonial calm). Image 3 \
(concept-cave-wide-dark) establishes the cave-altar geometry, basalt-purple \
cavernous atmosphere, turquoise vein treatment, dust mote density and \
volumetric haze — match these. Image 4 (portada principal) establishes the \
Pax universe neon-magic palette signature and bloom intensity logic — apply \
the same complementary magenta/turquesa color grading philosophy, but tuned \
to dying-amber (the kuya is in death, not in carga full).

NEGATIVE — DO NOT depict the character as: a human surface dweller, an \
indigenous Andean person, a mestizo, an ethnographic photographic subject, \
a documentary portrait, a generic poncho-wearing figure, a person with two \
eyes, a person with normal human proportions, a sun-burned weathered \
Andean man, a ritual shaman, a Marvel-multicultural character. NOT \
photorealistic, NOT hyperrealistic, NOT a documentary photograph, NOT 2D \
hand-drawn, NOT painted Studio Ghibli, NOT Cartoon Saloon flat planes, NOT \
visible brushwork, NOT hand-painted shadow gradients, NOT anime, NOT moe, \
NOT cel-shaded flat, NOT Pixar/Disney/DreamWorks generic family-feature \
look, NOT glowing eyes on the runner, NOT a glowing single eye (the eye \
is just an eye, not magical), NOT runic circles on the floor or walls, NOT \
magical particles spiraling, NOT additional torches or fires, NOT other \
figures in the background, NOT readable text or signage, NOT fantasy \
western tropes, NOT Marvel cosmic light, NOT Doctor Strange mandalas, NOT \
gothic dungeon elements, NOT saturated jewel-tone colors, NOT lens flare, \
NOT Avatar-2009 glowing skin, NOT heroic upward contrapicado, NOT thriller \
vignette, NOT glamour beauty shot, NOT a second eye, NOT human ears, NOT \
five-fingered hands, NOT a beard, NOT facial hair, NOT a wizard, NOT Wiz \
(this character is young like Jiggy, not old like Wiz)."""


def main() -> None:
    out_dir = abs_path("content", "v2", "anchors")
    os.makedirs(out_dir, exist_ok=True)
    output_path = os.path.join(out_dir, "img-01-piedra-apagandose-r3.png")

    refs = [
        abs_path("public", "images", "personajes", "jiggy.png"),
        abs_path("public", "images", "personajes", "wiz.png"),
        abs_path("public", "images", "concepts", "concept-cave-wide-dark.png"),
        abs_path("public", "images", "portadas", "portada.png"),
    ]

    for r in refs:
        if not os.path.exists(r):
            raise SystemExit(f"Missing reference: {r}")

    print("=== R3 generation — img-01 piedra apagandose ===")
    print(f"Model: gpt-image-2 / size=1536x1024 / quality=medium")
    print(f"Output: {output_path}")
    print("References:")
    for i, r in enumerate(refs, start=1):
        print(f"  Image {i}: {r}")
    print()

    result_path = edit_image(
        prompt=PROMPT_R3,
        input_image_paths=refs,
        output_path=output_path,
        size="1536x1024",
        quality="medium",
    )
    print(f"OK -> {result_path}")


if __name__ == "__main__":
    main()
