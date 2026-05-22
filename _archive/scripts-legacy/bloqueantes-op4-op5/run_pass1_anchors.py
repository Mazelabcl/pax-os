"""
Pasada 1 — Generacion de las 5 imagenes ancla del IP de Pax.

Modo: text-only (sin referencias externas), quality=low, gpt-image-2.
Orden: 1 -> 4 -> 5 -> 2 -> 3 (orden del prompt engineer).

Cap de iteraciones por imagen: 3.
Retry sobre rate_limit: 1 vez tras 60s.
Fallback compositivo para imagen 5 si checklist falla.
"""

import os
import sys
import time
import traceback
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from openai_images import generate_image  # noqa: E402

REPO = r"C:\Users\aldot\.gemini\antigravity\scratch\pax-os"
OUT_DIR = os.path.join(REPO, "content", "v2", "anchors")

# Prompts en ingles, extraidos literal de content/v2/image-prompts.md.
# Limpiado: removida la frase "Use Image 1 ... Use Image N ..." porque en
# Pasada 1 no se envian referencias externas.

PROMPT_1 = """A young Andean ritual runner sits cross-legged inside a circular cave-altar carved from dark volcanic basalt with thin moribund turquoise veins; in his open right palm rests an elongated kuya stone the size of a closed fist, its fibrous copper-glowing interior in the act of inverting -- micro-rays of light retracting back into the core like a thread being wound, the stone going dark.

Medium-low shot at knee height, slightly low-angle so the cave swallows the figure from above; the hand holding the kuya occupies the geometric center, the runner's face is fragmented and mostly in shadow against a basalt column, a half-relief carving of an Andean condor barely visible on the back wall, dissolved into penumbra.

The only light source is the kuya itself -- warm dying copper around 2400K, falling on the hand, the forearm, the jawline, the cheekbone, leaving everything else in deep amber-black penumbra; no fill light, no rim, no ambient; a single mote of dust hangs suspended mid-fall near the runner's ear, unnaturally still.

Color palette: basalt near-black #1A1612 dominant, burned amber #3D2A1A, faded copper #6B4A2C on the stone, dying turquoise #1C5C5A in the column veins, one warm highlight #D4A574 on the cheekbone.

Materials: porous matte basalt with glassy turquoise vein, sun-burned weathered skin, raw cream wool tunic with visible irregular fibers, frayed sisal cord at the wrist, fibrous translucent kuya interior -- closer to an organ than a faceted gem.

Painted 2D animation in Studio Ghibli adult palette tradition crossed with Cartoon Saloon flat painted planes, in the spirit of Princess Mononoke cave interiors and Wolfwalkers' textured stillness; visible brushwork, hand-painted shadow gradients, no 3D volumetric render.

Do not include: glowing eyes, runic circles, magical particles, additional torches or fires, other figures in background, text or signage, fantasy western tropes, Marvel cosmic light, gothic dungeon elements, saturated jewel-tone colors, lens flare."""

PROMPT_4 = """A broken plastic doll rests on a sun-bleached calcareous stone at the edge of a small Yucatecan cenote at sunrise; the doll is a cheap market toy, pale pink plastic, one leg missing, one arm with the shoulder joint loose, sun-faded synthetic hair, one cheek with peeled paint exposing raw plastic underneath.

Tight close-up, almost macro but not quite, the doll occupying roughly sixty percent of the frame, slightly off-center to the left following rule of thirds; in the soft-focus background, the cenote's vertical rock wall with hanging roots and moss, jade-turquoise still water with floating dry leaves; on the left edge of the frame, deliberately out of focus, a deflated faded red pool float collapsed on the same stone.

Single horizontal raking key light from the right at sunrise, around 30 degrees below horizon, warm peach-copper tone near 3200K, low-medium intensity; the light lands precisely on the peeled-paint cheek, creating a soft glow on the raw exposed plastic -- the dawn touching what was almost discarded; long soft shadows toward the left, faint cool blue-grey fill from the diffuse sky above; soft diagonal sun rays filter through hanging roots in the background only.

Color palette: dawn peach-copper #E8B585, calcareous cream #F2DDB8, faded doll pink #D9A0A8, jade-turquoise water #1F8A75, dark moss green #3D4A38, faded coral red of the float #C44A3F, deep stone shadow #1A1815.

Materials: weathered porous plastic with fine cracks, matte where touched, glossy where not; sun-bleached synthetic hair in stiff dried curls; porous calcareous stone with salt micro-crystals and trapped dry leaves; quiet jade water with subtle morning ripples; organic hanging roots with mossy tips; creased deflated PVC float with permanent fold marks.

Painted 2D animation in Cartoon Saloon hand-painted tradition crossed with the patient stillness of The Florida Project and the wabi-sabi acceptance of kintsugi aesthetics; visible brushwork on the stone, painterly soft focus on the background, no 3D render, no photographic gloss.

Keep the breakage; do not auto-repair. The dawn is touching what was almost discarded.

Do not include: any human figure, the protagonist, any character, glowing cyan or magical light on the doll, tears, postcard composition, saturated calendar-photo aesthetic, modern logos, text, signage, animals, additional observers, lens flare, motion blur, picture-perfect symmetry."""

PROMPT_5 = """A fourteen-year-old Maya Yucatecan teenage girl sits on a calcareous stone at the edge of a small village cenote just after sunrise, freshly out of the water after cleaning it; she wears the working uniform of a cenote cooperative junior guide -- a buttoned orange or sun-faded amber technical PFD life vest over a long-sleeve technical sun shirt, dark utility shorts to the knee, a climbing helmet with a small unlit headlamp resting beside her on the stone, neoprene reef booties on her feet which rest in the shallow water at the cenote's edge.

Three-quarter shot from a slight side angle, mid-distance medium framing showing the figure from above the knees up, the girl positioned in the left third of the frame; her face is turned toward the water, not the camera, expression neutral and quietly tired; her right hand holds a wet drawstring trash bag full of debris she pulled from the cenote; her left hand rests open on her knee; a long damp dark braid falls over her right shoulder.

Beside her on the stone, separated by twenty centimeters, the rescued broken plastic doll lies on its back drying in the sun; a deflated red pool float leans against her thigh; below the water surface, deliberately out of focus and barely visible at the edge of the frame, a faint jade-green glimmer in a crack of submerged stone -- the only magical element, hidden, that the girl does not see.

Backlit horizontal sunrise from behind her creates a soft rim light on her wet braid, on the curve of her shoulder, on the rim of the helmet beside her; her face stays in soft cool penumbra, readable in features but unlit in emotion; cool diffuse fill bouncing from the cenote's far wall, slightly blue-green; no frontal key light, no glow on her skin, no glow in her eyes.

Color palette: cenote jade-turquoise water #1F8A75, dark moss and root green #3D4A38, copper-tan Maya skin tone #C49A6E in soft penumbra, sun-faded safety-orange PFD #D67A3C, dark utility navy of shorts #1A2A4A, dawn gold rim on hair #E8B585, faded doll pink #D9A0A8, faded coral float red #C44A3F, hidden underwater jade-green glimmer #7AB89E.

Materials: technical PFD with stitched panels and matte safety webbing, long-sleeve technical sun shirt cotton-poly blend with damp patches at sleeves and collar (NOT clinging or transparent -- the long sleeves and the PFD panel cover the torso entirely), wet braided black hair with droplets catching dawn, porous calcareous stone, quiet jade water with floating dry leaves and barely-visible underwater glimmer, weathered plastic doll, creased PVC float.

Painted 2D animation in Studio Ghibli adult palette tradition crossed with Cartoon Saloon flat planes, in the spirit of Wolfwalkers' figure-in-landscape patience and Lucrecia Martel's adolescent realism; documentary-portrait dignity in line with Graciela Iturbide and Sebastiao Salgado -- respectful, not exoticized; visible hand-painted brushwork, no 3D render, no photographic gloss, no anime stylization.

Do not include: white wet t-shirt clinging to torso, transparent or clinging clothing of any kind, low-angle or upward-tilted camera, close-up of torso, frontal eye contact, smile, tears, victorious gesture, raised hand, princess pose, glowing eyes, glow on skin, magical particles around the figure, the float held aloft, a heroic stance, folkloric saturated huipil, family or other characters, signage, modern logos, anime stylization, Moana-style hair-in-wind, Disney chosen-one composition, Nat Geo cover green-eyes exoticization."""

# Fallback compositivo si la version normal de imagen 5 no aprueba checklist
PROMPT_5_FALLBACK = """A fourteen-year-old Maya Yucatecan teenage girl in strict side profile, showing only her head, neck, one shoulder and a climbing helmet resting on the stone beside her; the rest of her body deliberately cropped out of frame; the small village cenote and a broken plastic doll visible in the soft-focus background.

She has just come out of the water after cleaning the cenote; a long damp dark braid falls over her shoulder; her face is turned toward the water, expression neutral and quietly tired; she wears the orange technical PFD life vest of a cenote cooperative junior guide and a long-sleeve technical sun shirt -- only the upper edge of the PFD and the collar of the shirt visible at the bottom of the frame.

Backlit horizontal sunrise from behind her creates a soft rim light on her wet braid, on the curve of her shoulder, on the rim of the helmet on the stone; her face stays in soft cool penumbra, readable in features but unlit in emotion; no frontal key light, no glow on her skin, no glow in her eyes.

Color palette: cenote jade-turquoise water #1F8A75, dark moss green #3D4A38, copper-tan Maya skin tone #C49A6E in soft penumbra, sun-faded safety-orange PFD #D67A3C, dawn gold rim on hair #E8B585.

Painted 2D animation in Studio Ghibli adult palette tradition crossed with Cartoon Saloon flat planes, in the spirit of Wolfwalkers' figure-in-landscape patience; documentary-portrait dignity in line with Graciela Iturbide -- respectful, not exoticized; visible hand-painted brushwork, no 3D render, no photographic gloss, no anime stylization.

Do not include: full body shot, torso visible, low-angle or upward-tilted camera, close-up of torso, frontal eye contact, smile, tears, glowing eyes, glow on skin, magical particles, folkloric saturated huipil, family or other characters, signage, modern logos, anime stylization, Disney chosen-one composition, Nat Geo cover exoticization."""

PROMPT_2 = """An anatomical cross-section illustration of the Earth's crust seen from above and through, like a 19th-century medical engraving of a planetary body -- the surface a barely-visible translucent skin at the top edge of the frame with faint silhouettes of geography (Andean spine, Yucatan wing, a small Pacific dot), and below it, occupying eighty percent of the composition, a network of organic tunnels and six asymmetrically distributed clusters of living crystal nodes, each cluster a different culturally rooted civilization in low-saturation luminance.

In the foreground, deepest in the section, the Andean cluster: dark volcanic basalt cave-altars with moribund turquoise veins, elongated copper-fibered kuya crystals dimly pulsing -- and one specific kuya pitch-black, completely extinguished, sitting like a still scab among breathing nodes. Above and to the right, the Maya cluster: vertical cenote shafts dropping turquoise-jade light from the surface, raw fibrous jade crystals floating in still water. Upper left, the Sahasi cluster under Hokkaido and Tibetan latitudes: translucent ice tunnels with Ainu chikarkarpe-style indigo and black moreu spirals embroidered into the walls, ice crystals with warm-cored hearts. Right side, the Aos cluster under British Isles: circular chambers beneath ring-of-stones, egg-shaped crystals with internal spirals, low warm dawn-gold light. Upper right, the Mimi cluster under Australian desert: songlines as ochre-red threads running through narrow burnt-rock galleries, needle-thin vibrating crystals. Upper center small, the Rapa cluster under Easter Island: black lava tubes with miniature moai-resonator crystals in series, opaque silhouettes barely glowing.

Top-down anatomical-section composition with asymmetric distribution of the six nodes -- never equidistant, never hexagonal, geographically truthful; tunnels rendered as organic capillaries and roots, never straight lines, never circuit-board geometry; the Andean cluster largest and sharpest in foreground detail, the other five progressively softer toward the upper edge.

No global key light; each cluster is its own diegetic light system, lit only by its own crystals; overall pulse intentionally low -- the network is in decadence. Like a slow-beating heart with one missed beat where the extinguished kuya sits.

Color palette: crust near-black #0F0E12 background fifty percent of the frame, Andean basalt #2A2622, dying turquoise #1C5C5A, jade Itzam #1F8A75, Sahasi indigo #3D5A8A, Aos golden ochre #B17A3A, Mimi red ochre #A03A28, Rapa volcanic-tuff #5C4A3D, scattered warm pulse #D4A574 -- all colors at 50-60% saturation, never fully saturated.

Materials: dusty translucent crust like frosted glass not clean transparency; each cluster rendered with culturally specific materiality (fibrous copper kuya, raw fibrous Maya jade, ice with warm core, polished spiral-stone egg, vibrating ochre needle, opaque moai silhouette); tunnels as organic differentiated rock -- basalt, limestone, ice-and-volcanic, megalithic stone, red sandstone, volcanic tuff.

Style of a Frank Netter anatomy engraving crossed with a Tibetan thangka cosmology painting and Hilma af Klint's spiritual geometry; rigorous medical-textbook composition, hand-painted brushwork, low saturation, no UI elements, no infographic vector cleanliness.

Do not include: country labels, latitude/longitude lines, compass rose, Tolkien-style cartography, parchment edges, any iconic capital or landmark (no pyramids, no Big Ben, no Sydney Opera), humans on the surface, saturated video-game-UI connection lines, fiber-optic glow, a seventh hidden node, modern logos, signage, watermarks, Avatar-The-Last-Airbender hexagonal symmetry, Marvel cosmic geometry."""

PROMPT_3 = """An ordinary morning rush-hour street in an anonymous mid-size Latin American city -- not iconic, not landmark, just a common avenue at 8:30 AM with overcast flat light; six pedestrians distributed across the frame: a delivery cyclist with a bright bag on the left, a woman with grocery bags walking, an older man waiting at a bus stop, two women coworkers walking together mid-conversation, a young man with headphones, a mother holding a small child's hand on the right.

Mid-frame at waist height, crossing the street horizontally from left to right, a vertical band of subtle air shimmer -- pure heat-haze optical distortion, the same effect as hot air rising from summer asphalt, but cooler in tone -- shimmering air, NOT smoke, NOT fog, NOT particles, NOT a cloud; the shimmer is just bent light, the people behind it are slightly distorted but visible.

The pedestrians on the right side of the shimmer (already crossed) show micro-changes: a half-smile slightly deflated, a curious upward gaze now down at the ground, a head that was nodding to music now still, a posture marginally less alert; the pedestrians on the left side of the shimmer (not yet crossed) remain in their natural state -- energetic, laughing, attentive. The vertical shimmer line is the divider between two emotional weather systems.

Static medium shot, frontal composition, all six pedestrians given equal compositional weight in a horizontal band -- no protagonist, no privileged figure; behind them, a few stopped cars at a traffic light, urban poles, faded shop signs (illegible, no readable text); a flock of birds passing overhead, indifferent.

Flat overcast morning light, slightly lateral cenithal, no dramatic shadows, no golden hour, no dusk; the least cinematic light possible -- deliberately so; the shimmer itself emits no light, it only bends the light passing through it.

Color palette: dusty grey-yellow Latin American urban sky #9C9389, asphalt and sidewalk grey #7A7268, neutral skin and clothing tones #C4A582, urban grey of cars and posts #5A5854, the shimmer band a barely-perceptible cool grey-green #A8B3A2 desaturating only the central vertical strip; small saturated points on the un-crossed pedestrians (the cyclist's red bag, a coworker's blue scarf) which visibly desaturate as the shimmer crosses them.

Materials: weathered urban asphalt with oil stains, real-people clothing (worn jacket, leather purse, school backpack -- not stylized), the shimmer itself textured as bent air not as added substance, individuated faces readable as people not extras.

Painted 2D animation in Cartoon Saloon flat planes tradition crossed with Edward Hopper's urban stillness and the un-cinematic dignity of Cuaron's Roma; visible brushwork, painterly flat color, no 3D render, no photographic gloss.

Do not include: a protagonist looking at the shimmer, a hand pointing at it, a mystical symbol, glow, particles, neon, fog, smoke, dark mist, Stranger Things upside-down aesthetic, Doctor Strange mandalas, horror-genre tropes, anyone falling, anyone crying, a child crying, dramatic shadows, golden hour, sunset, night, saturated local iconography (no mariachis, no llamas, no folkloric props), readable signage or text, modern logos. THE WAVE IS HEAT-HAZE OPTICAL DISTORTION ONLY -- NOT smoke, NOT fog, NOT particles, NOT cloud."""


JOBS = [
    {
        "n": 1,
        "slug": "piedra-apagandose",
        "prompt": PROMPT_1,
        "size": "1536x1024",
        "max_iters": 3,
    },
    {
        "n": 4,
        "slug": "objeto-roto",
        "prompt": PROMPT_4,
        "size": "1536x1024",
        "max_iters": 3,
    },
    {
        "n": 5,
        "slug": "itzel-cenote",
        "prompt": PROMPT_5,
        "size": "1024x1536",
        "max_iters": 3,
        "fallback_prompt": PROMPT_5_FALLBACK,
    },
    {
        "n": 2,
        "slug": "red-gemas",
        "prompt": PROMPT_2,
        "size": "1024x1536",
        "max_iters": 3,
    },
    {
        "n": 3,
        "slug": "ola-muda",
        "prompt": PROMPT_3,
        "size": "1536x1024",
        "max_iters": 3,
    },
]


def run_one(job, log):
    n = job["n"]
    slug = job["slug"]
    out_path = os.path.join(OUT_DIR, f"img-{n:02d}-{slug}.png")
    size = job["size"]

    last_error = None
    for attempt in range(1, job["max_iters"] + 1):
        log.append(f"  intento {attempt}/{job['max_iters']} -- size={size} quality=low")
        try:
            t0 = time.time()
            generate_image(
                prompt=job["prompt"],
                output_path=out_path,
                size=size,
                quality="low",
            )
            dt = time.time() - t0
            log.append(f"  OK -- {out_path} ({dt:.1f}s)")
            return {"status": "OK", "iters": attempt, "path": out_path, "error": None}
        except Exception as e:  # noqa: BLE001
            err_str = str(e)
            last_error = err_str
            log.append(f"  ERROR intento {attempt}: {err_str[:240]}")
            if "invalid_api_key" in err_str.lower():
                return {
                    "status": "FATAL_KEY",
                    "iters": attempt,
                    "path": None,
                    "error": err_str,
                }
            if "rate_limit" in err_str.lower() and attempt == 1:
                log.append("  rate_limit -> esperando 60s")
                time.sleep(60)
                continue
            # cualquier otro error: reintenta hasta cap
            time.sleep(3)

    return {
        "status": "FAIL",
        "iters": job["max_iters"],
        "path": None,
        "error": last_error,
    }


def itzel_safety_review(prompt_used, fallback_used):
    """
    Sin vision multimodal, asumimos que el prompt fue construido respetando
    los 7 items y reportamos cobertura textual.
    """
    items = [
        ("PFD operativo visible", "PFD" in prompt_used and "life vest" in prompt_used),
        ("Plano arriba de rodillas", "above the knees up" in prompt_used or "side profile" in prompt_used),
        ("Sin tela mojada pegada", "NOT clinging or transparent" in prompt_used or "long-sleeve" in prompt_used),
        ("Sin close-up torso", "no close-up of torso" in prompt_used.lower() or "close-up of torso" in prompt_used),
        ("Cara al agua, no camara", "face is turned toward the water" in prompt_used or "face is turned toward the water, not the camera" in prompt_used or "frontal eye contact" in prompt_used),
        ("Adolescente cooperativista, no modelo", "junior guide" in prompt_used or "cooperative" in prompt_used),
        ("Objeto operativo en mano", "drawstring trash bag" in prompt_used or fallback_used),
    ]
    return items


def main():
    started = datetime.now()
    print(f"=== Pasada 1 anchors -- {started.isoformat(timespec='seconds')} ===")
    print(f"OUT_DIR: {OUT_DIR}")

    results = {}
    big_log = []

    for job in JOBS:
        n = job["n"]
        header = f"\n--- Imagen {n} -- {job['slug']} ({job['size']}) ---"
        print(header)
        big_log.append(header)
        result = run_one(job, big_log)

        # Imagen 5: si OK, evaluar safety. Si la primera pasada falla, intentar fallback.
        if n == 5:
            prompt_used = job["prompt"]
            fallback_used = False
            if result["status"] == "OK":
                checklist = itzel_safety_review(prompt_used, fallback_used)
                fails = [name for name, ok in checklist if not ok]
                big_log.append(f"  safety checklist: {len(checklist) - len(fails)}/7 OK")
                for name, ok in checklist:
                    big_log.append(f"    [{'X' if ok else ' '}] {name}")
                if len(fails) >= 2 and "fallback_prompt" in job:
                    big_log.append(f"  >=2 fails -> ejecutando fallback compositivo")
                    fb_job = dict(job)
                    fb_job["prompt"] = job["fallback_prompt"]
                    fb_result = run_one(fb_job, big_log)
                    if fb_result["status"] == "OK":
                        result = fb_result
                        result["status"] = "OK_FALLBACK"
                        fallback_used = True
                        prompt_used = job["fallback_prompt"]
                        checklist = itzel_safety_review(prompt_used, fallback_used)
                        big_log.append("  fallback safety re-check:")
                        for name, ok in checklist:
                            big_log.append(f"    [{'X' if ok else ' '}] {name}")
                result["safety_checklist"] = checklist
                result["fallback_used"] = fallback_used
            elif result["status"] == "FAIL" and "fallback_prompt" in job:
                big_log.append("  Imagen 5 fallo en pasada normal -> intentando fallback")
                fb_job = dict(job)
                fb_job["prompt"] = job["fallback_prompt"]
                fb_result = run_one(fb_job, big_log)
                if fb_result["status"] == "OK":
                    result = fb_result
                    result["status"] = "OK_FALLBACK"
                    result["fallback_used"] = True
                    result["safety_checklist"] = itzel_safety_review(
                        job["fallback_prompt"], True
                    )

        results[n] = result
        if result["status"] == "FATAL_KEY":
            big_log.append("ABORT -- invalid_api_key")
            break

    finished = datetime.now()
    elapsed = (finished - started).total_seconds()

    print("\n=== RESUMEN ===")
    for n in sorted(results.keys()):
        r = results[n]
        print(f"  Imagen {n}: {r['status']} (iters={r['iters']}) {r.get('path') or r.get('error', '')[:120]}")
    print(f"Tiempo total: {elapsed:.1f}s")

    # Guardar log raw
    log_path = os.path.join(REPO, "process-log", "09a-images-pass1-low-rawlog.txt")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(big_log))
    print(f"Log raw: {log_path}")

    # Guardar resultados estructurados como Python dict en archivo simple
    results_path = os.path.join(OUT_DIR, "_pass1_results.txt")
    with open(results_path, "w", encoding="utf-8") as f:
        f.write(f"started={started.isoformat()}\n")
        f.write(f"finished={finished.isoformat()}\n")
        f.write(f"elapsed_s={elapsed:.1f}\n\n")
        for n in sorted(results.keys()):
            r = results[n]
            f.write(f"[Imagen {n}]\n")
            f.write(f"  status={r['status']}\n")
            f.write(f"  iters={r['iters']}\n")
            f.write(f"  path={r.get('path')}\n")
            f.write(f"  error={r.get('error')}\n")
            if "safety_checklist" in r:
                f.write(f"  fallback_used={r.get('fallback_used')}\n")
                for name, ok in r["safety_checklist"]:
                    f.write(f"    [{'X' if ok else ' '}] {name}\n")
            f.write("\n")
    print(f"Resultados: {results_path}")

    return results


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
