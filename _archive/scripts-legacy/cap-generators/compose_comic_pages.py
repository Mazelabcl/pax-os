"""
Compositor de paginas estilo comic / storyboard pro para Pax.

Toma N storyboards individuales (PNG ya generados) de un capitulo y los
compone en una sola pagina con layout asimetrico, header, captions tecnicas
debajo de cada vineta, y footer de creditos.

Salida: content/storyboards/cap-N-comic-page.png

Layout vertical 1280x1920 (proporcion comic page).
- Header: ~140px (titulo capitulo)
- Cuerpo comic: 5 filas
    Fila 1 (Hook): 1 vineta wide
    Fila 2 (Setup + Catalizador): 2 vinetas medias
    Fila 3 (Decision + Accion): 2 vinetas medias
    Fila 4 (Climax): 1 vineta wide
    Fila 5 (Cliffhanger): 1 vineta wide
- Footer: ~70px (creditos + numero pagina)

Idioma de captions: espanol neutro.
"""

from __future__ import annotations

import os
from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Configuracion global
# ---------------------------------------------------------------------------

REPO_ROOT = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..")
)
STORYBOARDS_DIR = os.path.join(REPO_ROOT, "content", "storyboards")

# Paleta canon Pax
COLOR_BG = (15, 15, 26)         # basalt-deep
COLOR_PANEL_BORDER = (255, 255, 255)
COLOR_GUTTER = (240, 240, 240)  # blanco gutter ancho => elipsis
COLOR_TEXT_PRIMARY = (245, 245, 250)
COLOR_TEXT_SECONDARY = (200, 195, 210)
COLOR_ACCENT = (216, 70, 158)   # magenta canon Pax
COLOR_CAPTION_BG = (28, 22, 40)
COLOR_HEADER_BG = (8, 8, 14)

# Dimensiones de pagina (portrait, comic page)
PAGE_W = 1280
PAGE_H = 1920

HEADER_H = 140
FOOTER_H = 80
GUTTER = 14         # gutter ancho => elipsis temporal larga, segun research
GUTTER_TIGHT = 6    # gutter angosto => continuidad
PADDING_X = 28      # margen lateral

# Caption banda inferior por vineta
CAPTION_H = 64

# Fuentes
def load_fonts():
    try:
        f_title = ImageFont.truetype("arialbd.ttf", 38)
        f_subtitle = ImageFont.truetype("arial.ttf", 20)
        f_panel_num = ImageFont.truetype("arialbd.ttf", 22)
        f_panel_beat = ImageFont.truetype("arialbd.ttf", 16)
        f_caption_tech = ImageFont.truetype("arial.ttf", 14)
        f_caption_mood = ImageFont.truetype("arial.ttf", 13)
        f_footer = ImageFont.truetype("arial.ttf", 14)
    except OSError:
        # fallback default
        f_title = ImageFont.load_default()
        f_subtitle = ImageFont.load_default()
        f_panel_num = ImageFont.load_default()
        f_panel_beat = ImageFont.load_default()
        f_caption_tech = ImageFont.load_default()
        f_caption_mood = ImageFont.load_default()
        f_footer = ImageFont.load_default()
    return {
        "title": f_title,
        "subtitle": f_subtitle,
        "panel_num": f_panel_num,
        "panel_beat": f_panel_beat,
        "caption_tech": f_caption_tech,
        "caption_mood": f_caption_mood,
        "footer": f_footer,
    }


# ---------------------------------------------------------------------------
# Datos de panels — seleccion narrativa por capitulo
# ---------------------------------------------------------------------------

# Cada panel: file_slug, beat_label, plano, angulo, lente, movimiento, mood
# Captions traducidas/curadas a partir de los .md companions.

CAP_1_PANELS = [
    {
        "file": "cap-1-shot-01-crystal-dimming.png",
        "shot": "01",
        "beat": "HOOK 0:00",
        "plano": "Extreme close-up",
        "angulo": "Eye-level",
        "lente": "Macro 100mm",
        "movimiento": "Push-in lento",
        "mood": "Cristal magenta latiendo: tercer pulso baja un escalon. Algo no anda bien.",
    },
    {
        "file": "cap-1-shot-03-wiz-gathers-clan.png",
        "shot": "03",
        "beat": "SETUP",
        "plano": "Medium-wide",
        "angulo": "Eye-level",
        "lente": "35mm",
        "movimiento": "Locked-off",
        "mood": "Wiz convoca al clan ante el mapa de cristales. La red se oxida.",
    },
    {
        "file": "cap-1-shot-06-kz-approaches-crystal.png",
        "shot": "06",
        "beat": "CATALIZADOR",
        "plano": "Medium close",
        "angulo": "Slight low",
        "lente": "50mm",
        "movimiento": "Locked-off",
        "mood": "KZ se acerca sin pedir permiso. Curiosidad infantil concentrada.",
    },
    {
        "file": "cap-1-shot-09-byte-calculates.png",
        "shot": "09",
        "beat": "DECISION",
        "plano": "Medium close-up",
        "angulo": "Tres-cuartos",
        "lente": "50mm",
        "movimiento": "Locked-off",
        "mood": "Byte calcula tuneles. Resolucion silenciosa.",
    },
    {
        "file": "cap-1-shot-11-wiz-gives-crystal.png",
        "shot": "11",
        "beat": "CLIMAX",
        "plano": "Close two-shot",
        "angulo": "3/4 perfil",
        "lente": "85mm",
        "movimiento": "Locked-off",
        "mood": "Wiz entrega el cristal vacio a Jiggy. Bisagra del capitulo.",
    },
    {
        "file": "cap-1-shot-12-jiggy-runs.png",
        "shot": "12",
        "beat": "ACCION",
        "plano": "Medium-wide",
        "angulo": "Slight low",
        "lente": "35mm",
        "movimiento": "Push-in dinamico",
        "mood": "Jiggy sale corriendo como chasqui. Energia desatada.",
    },
    {
        "file": "cap-1-shot-15-jiggy-emerges-street.png",
        "shot": "15",
        "beat": "CLIFFHANGER",
        "plano": "Medium-wide",
        "angulo": "Low desde manhole",
        "lente": "24mm",
        "movimiento": "Locked-off",
        "mood": "Jiggy asoma a la calle latinoamericana nocturna. Bueno. Y ahora que.",
    },
]

CAP_2_PANELS = [
    {
        "file": "cap-2-shot-01-jiggy-running-tunnel.png",
        "shot": "01",
        "beat": "HOOK 0:00",
        "plano": "Wide tracking",
        "angulo": "Lateral",
        "lente": "28mm",
        "movimiento": "Truck lateral",
        "mood": "Jiggy corre por tunel angosto. Polvo volumetrico, magenta en vetas.",
    },
    {
        "file": "cap-2-shot-03-wall-collapse-reveal.png",
        "shot": "03",
        "beat": "REVEAL",
        "plano": "Wide reveal",
        "angulo": "Slight low",
        "lente": "24mm",
        "movimiento": "Locked-off",
        "mood": "La pared de raices cae. Aparece un templo Pax olvidado.",
    },
    {
        "file": "cap-2-shot-06-byte-cleaning-inscriptions.png",
        "shot": "06",
        "beat": "EXPLORACION",
        "plano": "Medium close-up",
        "angulo": "3/4",
        "lente": "50mm",
        "movimiento": "Locked-off",
        "mood": "Byte limpia inscripciones con scan cyan. Asombro arqueologico.",
    },
    {
        "file": "cap-2-shot-07-fresco-humans-pax-together.png",
        "shot": "07",
        "beat": "DESCUBRIMIENTO",
        "plano": "Medium",
        "angulo": "3/4 sobre muro",
        "lente": "50mm",
        "movimiento": "Locked-off",
        "mood": "Fresco: humanos y Pax cargando juntos un cristal. Esto ya paso antes.",
    },
    {
        "file": "cap-2-shot-09-wiz-recognition.png",
        "shot": "09",
        "beat": "BISAGRA",
        "plano": "Close-up",
        "angulo": "Slight low",
        "lente": "85mm",
        "movimiento": "Locked-off",
        "mood": "Wiz reconoce el lugar. Memoria ancestral en el ojo unico.",
    },
    {
        "file": "cap-2-shot-13-kz-touches-old-crystal.png",
        "shot": "13",
        "beat": "CHISPA",
        "plano": "Close-up",
        "angulo": "Lateral",
        "lente": "85mm",
        "movimiento": "Locked-off",
        "mood": "KZ apoya la mano. Una chispa magenta sube por el brazo. No esta muerto, dormido.",
    },
    {
        "file": "cap-2-shot-15-cliffhanger-graffiti-symbol.png",
        "shot": "15",
        "beat": "CLIFFHANGER",
        "plano": "Medium-wide",
        "angulo": "Slight low",
        "lente": "35mm",
        "movimiento": "Locked-off",
        "mood": "El simbolo del templo coincide con un grafiti urbano. Alguien arriba lo dibuja.",
    },
]


# ---------------------------------------------------------------------------
# CAPS 3-12 — Comic page panels
# Cada cap tiene exactamente 7 panels que cuentan el arc:
# [hook, setup, catalizador, desarrollo, climax, accion, cliffhanger]
# Filenames vienen del script gen_caps_3_to_12_async.py
# ---------------------------------------------------------------------------

CAP_3_PANELS = [
    {"file": "cap-3-shot-01-manhole-eye-peek.png", "shot": "01", "beat": "HOOK 0:00",
     "plano": "Extreme close-up", "angulo": "Slight low", "lente": "Macro 100mm",
     "movimiento": "Locked-off",
     "mood": "Ojo turquesa de Jiggy mira por la rendija de una alcantarilla. Adrenalina del primer contacto."},
    {"file": "cap-3-shot-02-jiggy-tiny-vs-city.png", "shot": "02", "beat": "SETUP",
     "plano": "Wide-low", "angulo": "Muy bajo", "lente": "24mm",
     "movimiento": "Locked-off",
     "mood": "Jiggy pequeno bajo torres y cables. Asombro y miedo justo."},
    {"file": "cap-3-shot-03-symbol-trail-collage.png", "shot": "03", "beat": "CATALIZADOR",
     "plano": "Medium", "angulo": "Eye-level", "lente": "35mm",
     "movimiento": "Locked-off",
     "mood": "El simbolo Pax repetido en stickers, servilletas, tiza. Suelto en la ciudad."},
    {"file": "cap-3-shot-04-sami-painting-fresh.png", "shot": "04", "beat": "DESARROLLO",
     "plano": "Medium", "angulo": "3/4", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Sami termina de pintar el simbolo. No sabe que lo es."},
    {"file": "cap-3-shot-05-jiggy-hides-behind-dumpster.png", "shot": "05", "beat": "CLIMAX",
     "plano": "Medium", "angulo": "Lateral", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Jiggy observa a Sami dejar un sandwich a un desconocido sin testigos."},
    {"file": "cap-3-shot-06-crystal-first-spark.png", "shot": "06", "beat": "ACCION",
     "plano": "Extreme close-up", "angulo": "Eye-level", "lente": "Macro 100mm",
     "movimiento": "Locked-off",
     "mood": "Primera chispa magenta dentro del cristal. El sistema funciona."},
    {"file": "cap-3-shot-07-cliffhanger-wiz-pockets-spark.png", "shot": "07", "beat": "CLIFFHANGER",
     "plano": "Medium", "angulo": "Slight low", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Wiz guarda en secreto la chispa-ancla dorada. Semilla del arc final."},
]

CAP_4_PANELS = [
    {"file": "cap-4-shot-01-balcony-class-pov.png", "shot": "01", "beat": "HOOK 0:00",
     "plano": "Wide", "angulo": "POV rama", "lente": "35mm",
     "movimiento": "Locked-off",
     "mood": "Balcon humilde con pizarra y tres ninos. Sagrado en lo ordinario."},
    {"file": "cap-4-shot-02-byte-luxa-upside-down.png", "shot": "02", "beat": "SETUP",
     "plano": "Medium close-up", "angulo": "Canted", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Byte y Luxa colgados de cabeza espian la clase. Comica curiosidad."},
    {"file": "cap-4-shot-03-byte-detects-frequency.png", "shot": "03", "beat": "CATALIZADOR",
     "plano": "Close-up", "angulo": "Lateral", "lente": "85mm",
     "movimiento": "Locked-off",
     "mood": "Byte detecta una frecuencia de energia ordenada. Algo aqui carga."},
    {"file": "cap-4-shot-04-heriberto-doubt.png", "shot": "04", "beat": "DESARROLLO",
     "plano": "Medium close-up", "angulo": "Slight low", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Don Heriberto al borde de cancelar. Cansado, sin confirmacion."},
    {"file": "cap-4-shot-05-girl-gives-drawing.png", "shot": "05", "beat": "CLIMAX",
     "plano": "Medium", "angulo": "Slight low", "lente": "35mm",
     "movimiento": "Locked-off",
     "mood": "Una nina le entrega un dibujo. El profesor se queda mirandolo."},
    {"file": "cap-4-shot-06-byte-crystal-charges.png", "shot": "06", "beat": "ACCION",
     "plano": "Close-up", "angulo": "Lateral", "lente": "85mm",
     "movimiento": "Locked-off",
     "mood": "Cristal de Byte pulsa. Ruca-clase activa, doble carga."},
    {"file": "cap-4-shot-07-cliffhanger-ant-on-symbol.png", "shot": "07", "beat": "CLIFFHANGER",
     "plano": "Extreme macro", "angulo": "Eye-level", "lente": "Macro 100mm",
     "movimiento": "Locked-off",
     "mood": "Una hormiga camina sobre el simbolo Pax dibujado en un cuaderno."},
]

CAP_5_PANELS = [
    {"file": "cap-5-shot-01-onyx-pokes-head.png", "shot": "01", "beat": "HOOK 0:00",
     "plano": "Medium close-up", "angulo": "Bajo", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Onyx asoma la cabeza por la alcantarilla. Pasa una bici. Comica vacilacion."},
    {"file": "cap-5-shot-02-jiggy-onyx-walking-rich-zone.png", "shot": "02", "beat": "SETUP",
     "plano": "Wide", "angulo": "Bajo", "lente": "24mm",
     "movimiento": "Tracking",
     "mood": "Jiggy y Onyx caminan en zona de oficinas. Fuera de lugar, modo recon."},
    {"file": "cap-5-shot-03-woman-falls-bags.png", "shot": "03", "beat": "CATALIZADOR",
     "plano": "Medium-wide", "angulo": "Slight high", "lente": "35mm",
     "movimiento": "Locked-off",
     "mood": "Una senora cae con las bolsas. Hombre de corbata pasa indiferente."},
    {"file": "cap-5-shot-04-onyx-stops-jiggy.png", "shot": "04", "beat": "DESARROLLO",
     "plano": "Medium close-up", "angulo": "Slight low", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Onyx detiene a Jiggy con la mano. Espera, mira."},
    {"file": "cap-5-shot-05-young-helper-helps.png", "shot": "05", "beat": "CLIMAX",
     "plano": "Medium", "angulo": "Slight low", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Un joven con poca pinta levanta las bolsas. Bondad sin espectaculo."},
    {"file": "cap-5-shot-06-onyx-processing-silent.png", "shot": "06", "beat": "ACCION",
     "plano": "Close-up", "angulo": "3/4 frontal", "lente": "85mm",
     "movimiento": "Locked-off",
     "mood": "Onyx procesa en silencio. La red no carga proporcional a recursos."},
    {"file": "cap-5-shot-07-cliffhanger-vuelve-graffiti.png", "shot": "07", "beat": "CLIFFHANGER",
     "plano": "Medium", "angulo": "Lateral", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Grafiti nuevo: simbolo Pax + 'vuelve' en marcador. Alguien arriba ve."},
]

CAP_6_PANELS = [
    {"file": "cap-6-shot-01-new-crystal-born.png", "shot": "01", "beat": "HOOK 0:00",
     "plano": "Medium close-up", "angulo": "Eye-level", "lente": "85mm",
     "movimiento": "Locked-off",
     "mood": "Un cristal magenta nuevo brota entre dos viejos. Tibio, latiendo."},
    {"file": "cap-6-shot-02-wiz-discovers-new-crystal.png", "shot": "02", "beat": "SETUP",
     "plano": "Medium close-up", "angulo": "Slight low", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Wiz descubre el cristal recien nacido. Asombro reverente."},
    {"file": "cap-6-shot-03-mariela-laptop-night.png", "shot": "03", "beat": "CATALIZADOR",
     "plano": "Medium", "angulo": "3/4", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Mariela sola con su laptop de noche. La pregunta que no se va."},
    {"file": "cap-6-shot-04-mariela-types-deletes.png", "shot": "04", "beat": "DESARROLLO",
     "plano": "Close-up", "angulo": "Slight high", "lente": "85mm",
     "movimiento": "Locked-off",
     "mood": "Manos sobre el teclado. Tercera version, casi lista."},
    {"file": "cap-6-shot-05-jiggy-bilbao-ushnu.png", "shot": "05", "beat": "CLIMAX",
     "plano": "Wide-medium", "angulo": "Bajo", "lente": "35mm",
     "movimiento": "Locked-off",
     "mood": "Jiggy cruza una placita con ushnu antiguo en avenida Bilbao."},
    {"file": "cap-6-shot-06-jiggy-leaves-crystal-mariela.png", "shot": "06", "beat": "ACCION",
     "plano": "Close-up", "angulo": "Slight high", "lente": "85mm",
     "movimiento": "Locked-off",
     "mood": "Jiggy deposita el cristal magenta en la palma dormida de Mariela."},
    {"file": "cap-6-shot-07-cliffhanger-te-vimos.png", "shot": "07", "beat": "CLIFFHANGER",
     "plano": "Medium", "angulo": "Slight low", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "El grafiti ahora dice 'te vimos'. La frontera se vuelve fragil."},
]

CAP_7_PANELS = [
    {"file": "cap-7-shot-01-hand-marker-symbol.png", "shot": "01", "beat": "HOOK 0:00",
     "plano": "Extreme close-up", "angulo": "Eye-level", "lente": "Macro 100mm",
     "movimiento": "Locked-off",
     "mood": "Mano humana dibuja el simbolo en una pared del metro. 'los veo'."},
    {"file": "cap-7-shot-02-byte-triangulates-map.png", "shot": "02", "beat": "SETUP",
     "plano": "Medium close-up", "angulo": "3/4", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Byte triangula los grafitis en su holo-tablet. Forman un patron."},
    {"file": "cap-7-shot-03-bakery-exterior.png", "shot": "03", "beat": "CATALIZADOR",
     "plano": "Wide", "angulo": "Slight low", "lente": "28mm",
     "movimiento": "Locked-off",
     "mood": "Panaderia de barrio. El simbolo Pax discreto en la puerta."},
    {"file": "cap-7-shot-04-sami-grandma-bread.png", "shot": "04", "beat": "DESARROLLO",
     "plano": "Medium", "angulo": "Eye-level", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Sami y abuela envuelven pan. El simbolo viene de antes — herencia."},
    {"file": "cap-7-shot-05-sami-bread-homeless.png", "shot": "05", "beat": "CLIMAX",
     "plano": "Medium", "angulo": "3/4", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Sami deja pan al senor durmiendo. Sin firma, sin testigo."},
    {"file": "cap-7-shot-06-byte-agatha-realize.png", "shot": "06", "beat": "ACCION",
     "plano": "Medium", "angulo": "Slight low", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Byte y Agatha leen 'gracias por venir'. No los caza, los agradece."},
    {"file": "cap-7-shot-07-cliffhanger-sami-draws-jiggy.png", "shot": "07", "beat": "CLIFFHANGER",
     "plano": "Medium", "angulo": "3/4 espalda", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Sami pinta a Jiggy en un grafiti. Lo vio en cap 3. No olvido."},
]

CAP_8_PANELS = [
    {"file": "cap-8-shot-01-temple-crystal-cracks.png", "shot": "01", "beat": "HOOK 0:00",
     "plano": "Extreme close-up", "angulo": "Eye-level", "lente": "Macro 100mm",
     "movimiento": "Locked-off",
     "mood": "Una grieta nueva en el cristal templario. Magenta sangrando hacia afuera."},
    {"file": "cap-8-shot-02-cavern-crystals-dim.png", "shot": "02", "beat": "SETUP",
     "plano": "Wide", "angulo": "Crane descendente", "lente": "24mm",
     "movimiento": "Slow descent",
     "mood": "Media docena de cristales se apagan a la vez. Cascada."},
    {"file": "cap-8-shot-03-clan-panic-contained.png", "shot": "03", "beat": "CATALIZADOR",
     "plano": "Medium-wide", "angulo": "Slight low", "lente": "35mm",
     "movimiento": "Locked-off",
     "mood": "Clan en panico contenido. Onyx quiere subir, Agatha lo frena."},
    {"file": "cap-8-shot-04-byte-studies-fracture.png", "shot": "04", "beat": "DESARROLLO",
     "plano": "Close-up", "angulo": "3/4", "lente": "85mm",
     "movimiento": "Locked-off",
     "mood": "Byte escanea la fractura. Sobrecarga sin distribucion."},
    {"file": "cap-8-shot-05-kz-cries-without-knowing.png", "shot": "05", "beat": "CLIMAX",
     "plano": "Close-up", "angulo": "Slight low", "lente": "85mm",
     "movimiento": "Locked-off",
     "mood": "KZ llora sin saber por que. Esta cansado, no roto. Cansado."},
    {"file": "cap-8-shot-06-wiz-recognizes-spark-mark.png", "shot": "06", "beat": "ACCION",
     "plano": "Close-up", "angulo": "Slight low", "lente": "85mm",
     "movimiento": "Locked-off",
     "mood": "Wiz reconoce la marca. La grieta es el reverso de su chispa-ancla."},
    {"file": "cap-8-shot-07-cliffhanger-wiz-confesses.png", "shot": "07", "beat": "CLIFFHANGER",
     "plano": "Medium-wide", "angulo": "Slight low", "lente": "35mm",
     "movimiento": "Locked-off",
     "mood": "Wiz por primera vez vulnerable. 'Hay algo que tengo que contarles.'"},
]

CAP_9_PANELS = [
    {"file": "cap-9-shot-01-wiz-opens-hand-spark.png", "shot": "01", "beat": "HOOK 0:00",
     "plano": "Extreme close-up", "angulo": "Eye-level", "lente": "Macro 100mm",
     "movimiento": "Locked-off",
     "mood": "Wiz abre la mano. La chispa-ancla dorada pulsa. Confesion empieza."},
    {"file": "cap-9-shot-02-flashback-pax-humans-hands-united.png", "shot": "02", "beat": "SETUP",
     "plano": "Medium-wide", "angulo": "Slight low", "lente": "35mm",
     "movimiento": "Locked-off",
     "mood": "Flashback sepia: Pax y humanos con las manos juntas sobre un cristal."},
    {"file": "cap-9-shot-03-young-wiz-pockets-spark.png", "shot": "03", "beat": "CATALIZADOR",
     "plano": "Medium close-up", "angulo": "3/4", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Wiz joven guarda la chispa-ancla. La eleccion equivocada por miedo."},
    {"file": "cap-9-shot-04-sami-rain-symbol-fading.png", "shot": "04", "beat": "DESARROLLO",
     "plano": "Medium close-up", "angulo": "Slight low", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Micro-corte: Sami pasa la mano sobre un grafiti que la lluvia borra."},
    {"file": "cap-9-shot-05-mariela-looks-at-hand.png", "shot": "05", "beat": "CLIMAX",
     "plano": "Close-up", "angulo": "Slight high", "lente": "85mm",
     "movimiento": "Locked-off",
     "mood": "Micro-corte: Mariela mira su mano. La chispa del cap 6 sigue pesando."},
    {"file": "cap-9-shot-06-clan-hands-on-wiz.png", "shot": "06", "beat": "ACCION",
     "plano": "Medium-wide", "angulo": "Eye-level", "lente": "35mm",
     "movimiento": "Locked-off",
     "mood": "El clan posa las manos sobre Wiz. Lo que cargo solo lo cargan juntos."},
    {"file": "cap-9-shot-07-cliffhanger-wiz-passes-spark-jiggy.png", "shot": "07", "beat": "CLIFFHANGER",
     "plano": "Close two-shot", "angulo": "Lateral", "lente": "85mm",
     "movimiento": "Locked-off",
     "mood": "Wiz le pasa la chispa-ancla a Jiggy. Esta vez no vas solo."},
]

CAP_10_PANELS = [
    {"file": "cap-10-shot-01-clan-emerges-row.png", "shot": "01", "beat": "HOOK 0:00",
     "plano": "Wide ensemble", "angulo": "Slight low", "lente": "24mm",
     "movimiento": "Locked-off",
     "mood": "Los siete Pax salen en fila por la alcantarilla. Primera vez juntos arriba."},
    {"file": "cap-10-shot-02-clan-coral-crossing-city.png", "shot": "02", "beat": "SETUP",
     "plano": "Wide tracking", "angulo": "Lateral", "lente": "28mm",
     "movimiento": "Truck lateral",
     "mood": "El clan cruza la ciudad como coral. Cada uno con su rol."},
    {"file": "cap-10-shot-03-arrive-plaza.png", "shot": "03", "beat": "CATALIZADOR",
     "plano": "Wide", "angulo": "Slight low", "lente": "24mm",
     "movimiento": "Locked-off",
     "mood": "Llegan a la placita con ushnu. Pequenos en el espacio abierto."},
    {"file": "cap-10-shot-04-sami-painting-wall-mural.png", "shot": "04", "beat": "DESARROLLO",
     "plano": "Medium", "angulo": "3/4 espalda", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Sami pinta un mural Pax-humano cargando juntos. Los esperaba."},
    {"file": "cap-10-shot-05-sami-turns-sees-clan.png", "shot": "05", "beat": "CLIMAX",
     "plano": "Close-up", "angulo": "Frontal", "lente": "85mm",
     "movimiento": "Locked-off",
     "mood": "Sami se da vuelta. Suelta el spray. 'Sabia que eran de verdad.'"},
    {"file": "cap-10-shot-06-clan-faces-sami-frontal.png", "shot": "06", "beat": "ACCION",
     "plano": "Wide-medium", "angulo": "Slight low POV Sami", "lente": "28mm",
     "movimiento": "Locked-off",
     "mood": "Los siete frente a Sami. Visibles sin verguenza. Doctrina rota."},
    {"file": "cap-10-shot-07-cliffhanger-spark-fully-lit.png", "shot": "07", "beat": "CLIFFHANGER",
     "plano": "Extreme close-up", "angulo": "Eye-level", "lente": "Macro 100mm",
     "movimiento": "Locked-off",
     "mood": "La chispa-ancla se enciende entera. La visibilidad era la carga."},
]

CAP_11_PANELS = [
    {"file": "cap-11-shot-01-sami-paints-new-stroke.png", "shot": "01", "beat": "HOOK 0:00",
     "plano": "Close-up", "angulo": "3/4", "lente": "85mm",
     "movimiento": "Locked-off",
     "mood": "Sami inventa un trazo nuevo al lado del simbolo. 'Tu tambien'."},
    {"file": "cap-11-shot-02-onyx-discovers-icecream.png", "shot": "02", "beat": "SETUP",
     "plano": "Medium close-up", "angulo": "Slight low", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Onyx descubre el helado. Asombro mas grande que el cuerpo."},
    {"file": "cap-11-shot-03-byte-sami-design-sign.png", "shot": "03", "beat": "CATALIZADOR",
     "plano": "Medium", "angulo": "Slight high", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Byte y Sami disenan la senal en una mesa. No marca, gesto."},
    {"file": "cap-11-shot-04-heriberto-draws-on-board.png", "shot": "04", "beat": "DESARROLLO",
     "plano": "Medium", "angulo": "Eye-level", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Heriberto dibuja el trazo en su pizarra. Tres ninos lo copian."},
    {"file": "cap-11-shot-05-mariela-draws-note-monitor.png", "shot": "05", "beat": "CLIMAX",
     "plano": "Close-up", "angulo": "Slight high", "lente": "85mm",
     "movimiento": "Locked-off",
     "mood": "Mariela dibuja el trazo en una nota junto al monitor. La senal viaja."},
    {"file": "cap-11-shot-06-cavern-crystals-cascade.png", "shot": "06", "beat": "ACCION",
     "plano": "Wide", "angulo": "Crane ascendente", "lente": "24mm",
     "movimiento": "Slow rise",
     "mood": "Cristales encendiendose en cadena. La red se alimenta sola."},
    {"file": "cap-11-shot-07-cliffhanger-wiz-jiggy-smile.png", "shot": "07", "beat": "CLIFFHANGER",
     "plano": "Medium two-shot", "angulo": "Lateral", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Wiz y Jiggy sonrien sin hablar. El gran cristal vibra. Manana se activa."},
]

CAP_12_PANELS = [
    {"file": "cap-12-shot-01-wiz-hands-on-big-crystal.png", "shot": "01", "beat": "HOOK 0:00",
     "plano": "Medium", "angulo": "Slight low", "lente": "50mm",
     "movimiento": "Locked-off",
     "mood": "Wiz coloca las manos sobre el gran cristal. Ritual final."},
    {"file": "cap-12-shot-02-clan-channels-energy.png", "shot": "02", "beat": "SETUP",
     "plano": "Wide ensemble", "angulo": "Slight low", "lente": "28mm",
     "movimiento": "Locked-off",
     "mood": "Los siete canalizan la energia en circulo. Sin protagonista unico."},
    {"file": "cap-12-shot-03-water-truck-village.png", "shot": "03", "beat": "CATALIZADOR",
     "plano": "Wide", "angulo": "Slight low", "lente": "35mm",
     "movimiento": "Locked-off",
     "mood": "Camion de agua llega a un pueblo. Pequeno milagro concreto."},
    {"file": "cap-12-shot-04-mariela-email-accepted.png", "shot": "04", "beat": "DESARROLLO",
     "plano": "Close-up", "angulo": "Slight high", "lente": "85mm",
     "movimiento": "Locked-off",
     "mood": "Mariela ve su correo aceptado. Alegria privada."},
    {"file": "cap-12-shot-05-sami-paints-with-strangers.png", "shot": "05", "beat": "CLIMAX",
     "plano": "Wide", "angulo": "Slight low", "lente": "35mm",
     "movimiento": "Locked-off",
     "mood": "Sami pinta con tres desconocidos. La senal se descentraliza."},
    {"file": "cap-12-shot-06-coral-vignette-grid.png", "shot": "06", "beat": "ACCION",
     "plano": "Composite split", "angulo": "Varios", "lente": "35mm eq",
     "movimiento": "Locked-off",
     "mood": "Cuatro vinetas simultaneas. Pequenos milagros en muchos lugares."},
    {"file": "cap-12-shot-07-cliffhanger-sami-fourth-wall.png", "shot": "07", "beat": "INVITACION",
     "plano": "Close-up", "angulo": "Frontal", "lente": "85mm",
     "movimiento": "Locked-off",
     "mood": "Sami mira a camara y dibuja el trazo en el aire. Tu tambien."},
]


# Registry para acceso por numero de cap
CAP_REGISTRY = {
    1:  ("La red oxidada",            CAP_1_PANELS),
    2:  ("El templo que nadie cuido", CAP_2_PANELS),
    3:  ("El grafiti",                CAP_3_PANELS),
    4:  ("La clase del lunes",        CAP_4_PANELS),
    5:  ("El que no quiso",           CAP_5_PANELS),
    6:  ("La pregunta de Mariela",    CAP_6_PANELS),
    7:  ("El observador",             CAP_7_PANELS),
    8:  ("Se rompe algo",             CAP_8_PANELS),
    9:  ("Lo que Wiz guardo",         CAP_9_PANELS),
    10: ("Subir todos",               CAP_10_PANELS),
    11: ("La ruca de las rucas",      CAP_11_PANELS),
    12: ("Lo que aparece arriba",     CAP_12_PANELS),
}


# ---------------------------------------------------------------------------
# Utilidades de composicion
# ---------------------------------------------------------------------------

def fit_image_into_panel(src_path: str, panel_w: int, panel_h: int) -> Image.Image:
    """Carga PNG y la encaja en panel_w x panel_h con cover crop centrado.

    Mantiene aspect del original (1536x1024 = 1.5) y crop cubre todo el panel.
    """
    img = Image.open(src_path).convert("RGB")
    src_w, src_h = img.size
    src_ratio = src_w / src_h
    dst_ratio = panel_w / panel_h

    if src_ratio > dst_ratio:
        # source mas ancha => escalar por alto, recortar lados
        new_h = panel_h
        new_w = int(round(new_h * src_ratio))
    else:
        # source mas alta o igual => escalar por ancho, recortar arriba/abajo
        new_w = panel_w
        new_h = int(round(new_w / src_ratio))

    img = img.resize((new_w, new_h), Image.LANCZOS)
    # crop centrado
    left = (new_w - panel_w) // 2
    top = (new_h - panel_h) // 2
    img = img.crop((left, top, left + panel_w, top + panel_h))
    return img


def draw_panel(
    canvas: Image.Image,
    draw: ImageDraw.ImageDraw,
    panel: dict,
    x: int,
    y: int,
    w: int,
    h: int,
    fonts: dict,
) -> None:
    """Dibuja una vineta en (x,y) con tamano (w,h).

    h incluye CAPTION_H — la imagen ocupa h - CAPTION_H, debajo va caption.
    """
    img_h = h - CAPTION_H
    src_path = os.path.join(STORYBOARDS_DIR, panel["file"])

    if not os.path.exists(src_path):
        # placeholder oscuro con texto
        draw.rectangle([x, y, x + w, y + img_h], fill=(40, 30, 50))
        draw.text(
            (x + 12, y + 12),
            f"FALTA {panel['file']}",
            fill=(255, 100, 100),
            font=fonts["panel_num"],
        )
    else:
        panel_img = fit_image_into_panel(src_path, w, img_h)
        canvas.paste(panel_img, (x, y))

    # Borde negro fino del panel
    draw.rectangle(
        [x, y, x + w - 1, y + h - 1],
        outline=(0, 0, 0),
        width=2,
    )

    # Tag esquina superior izq: SHOT NUMBER + BEAT
    tag_text = f"#{panel['shot']}  {panel['beat']}"
    tag_w = draw.textlength(tag_text, font=fonts["panel_beat"]) + 16
    tag_h = 28
    draw.rectangle(
        [x, y, x + tag_w, y + tag_h],
        fill=COLOR_ACCENT,
    )
    draw.text(
        (x + 8, y + 5),
        tag_text,
        fill=(255, 255, 255),
        font=fonts["panel_beat"],
    )

    # Caption inferior: tech specs + mood
    cap_y = y + img_h
    draw.rectangle(
        [x, cap_y, x + w, cap_y + CAPTION_H],
        fill=COLOR_CAPTION_BG,
    )

    tech_line = (
        f"{panel['plano']}  /  {panel['angulo']}  /  "
        f"{panel['lente']}  /  {panel['movimiento']}"
    )
    draw.text(
        (x + 10, cap_y + 7),
        tech_line,
        fill=COLOR_TEXT_PRIMARY,
        font=fonts["caption_tech"],
    )

    mood = panel["mood"]
    # truncar mood si pasa del ancho
    max_mood_w = w - 20
    if draw.textlength(mood, font=fonts["caption_mood"]) > max_mood_w:
        # truncar progresivamente
        while (
            mood
            and draw.textlength(mood + "...", font=fonts["caption_mood"]) > max_mood_w
        ):
            mood = mood[:-1]
        mood = mood.rstrip() + "..."
    draw.text(
        (x + 10, cap_y + 28),
        mood,
        fill=COLOR_TEXT_SECONDARY,
        font=fonts["caption_mood"],
    )

    # Linea acento inferior magenta
    draw.line(
        [(x, cap_y + CAPTION_H - 1), (x + w, cap_y + CAPTION_H - 1)],
        fill=COLOR_ACCENT,
        width=2,
    )


# ---------------------------------------------------------------------------
# Layout principal
# ---------------------------------------------------------------------------

def build_page(
    panels: list[dict],
    cap_num: int,
    cap_title: str,
    output_path: str,
) -> None:
    assert len(panels) == 7, f"Esperaba 7 panels, llegaron {len(panels)}"

    canvas = Image.new("RGB", (PAGE_W, PAGE_H), COLOR_BG)
    draw = ImageDraw.Draw(canvas)
    fonts = load_fonts()

    # ---- Header ----
    draw.rectangle([0, 0, PAGE_W, HEADER_H], fill=COLOR_HEADER_BG)
    draw.line([(0, HEADER_H), (PAGE_W, HEADER_H)], fill=COLOR_ACCENT, width=3)
    title_text = f"PAX  /  CAPITULO {cap_num}  /  {cap_title.upper()}"
    draw.text(
        (PADDING_X, 30),
        title_text,
        fill=COLOR_TEXT_PRIMARY,
        font=fonts["title"],
    )
    subtitle = "Storyboard estilo comic-pagina  -  7 vinetas  -  arc completo del capitulo"
    draw.text(
        (PADDING_X, 80),
        subtitle,
        fill=COLOR_TEXT_SECONDARY,
        font=fonts["subtitle"],
    )

    # ---- Cuerpo comic ----
    body_top = HEADER_H + 16
    body_bottom = PAGE_H - FOOTER_H - 8
    body_h = body_bottom - body_top
    body_w = PAGE_W - 2 * PADDING_X

    # Layout asimetrico — 5 filas:
    # row 1 wide (1 panel)        peso 1.15 (hook grande)
    # row 2 doble (2 panels)      peso 0.95
    # row 3 doble (2 panels)      peso 0.95
    # row 4 wide (1 panel)        peso 1.15 (climax)
    # row 5 wide (1 panel)        peso 1.10 (cliffhanger panoramico)
    # gutters entre filas: ancho (GUTTER) salvo entre row 4 y row 5 que es elipsis
    weights = [1.15, 0.95, 0.95, 1.15, 1.10]
    # gutter total: 4 entre filas
    total_gutter = 4 * GUTTER
    avail_h = body_h - total_gutter
    weight_sum = sum(weights)
    row_heights = [int(round(avail_h * w / weight_sum)) for w in weights]

    cur_y = body_top

    # --- Row 1: panel 0 (Hook) wide ---
    panel0 = panels[0]
    draw_panel(
        canvas,
        draw,
        panel0,
        x=PADDING_X,
        y=cur_y,
        w=body_w,
        h=row_heights[0],
        fonts=fonts,
    )
    cur_y += row_heights[0] + GUTTER

    # --- Row 2: panel 1 + panel 2 ---
    half_w = (body_w - GUTTER_TIGHT) // 2
    draw_panel(
        canvas,
        draw,
        panels[1],
        x=PADDING_X,
        y=cur_y,
        w=half_w,
        h=row_heights[1],
        fonts=fonts,
    )
    draw_panel(
        canvas,
        draw,
        panels[2],
        x=PADDING_X + half_w + GUTTER_TIGHT,
        y=cur_y,
        w=body_w - half_w - GUTTER_TIGHT,
        h=row_heights[1],
        fonts=fonts,
    )
    cur_y += row_heights[1] + GUTTER

    # --- Row 3: panel 3 + panel 4 ---
    draw_panel(
        canvas,
        draw,
        panels[3],
        x=PADDING_X,
        y=cur_y,
        w=half_w,
        h=row_heights[2],
        fonts=fonts,
    )
    draw_panel(
        canvas,
        draw,
        panels[4],
        x=PADDING_X + half_w + GUTTER_TIGHT,
        y=cur_y,
        w=body_w - half_w - GUTTER_TIGHT,
        h=row_heights[2],
        fonts=fonts,
    )
    cur_y += row_heights[2] + GUTTER

    # --- Row 4: panel 5 wide (accion central) ---
    draw_panel(
        canvas,
        draw,
        panels[5],
        x=PADDING_X,
        y=cur_y,
        w=body_w,
        h=row_heights[3],
        fonts=fonts,
    )
    cur_y += row_heights[3] + GUTTER

    # --- Row 5: panel 6 wide (cliffhanger) ---
    # gutter ancho antes => elipsis. Ya esta en GUTTER.
    draw_panel(
        canvas,
        draw,
        panels[6],
        x=PADDING_X,
        y=cur_y,
        w=body_w,
        h=row_heights[4],
        fonts=fonts,
    )

    # ---- Footer ----
    foot_y = PAGE_H - FOOTER_H
    draw.rectangle([0, foot_y, PAGE_W, PAGE_H], fill=COLOR_HEADER_BG)
    draw.line([(0, foot_y), (PAGE_W, foot_y)], fill=COLOR_ACCENT, width=2)
    foot_left = "PAX webserie  -  storyboard composicion  -  espanol neutro"
    foot_right = f"PAGINA {cap_num} / 12"
    draw.text(
        (PADDING_X, foot_y + 30),
        foot_left,
        fill=COLOR_TEXT_SECONDARY,
        font=fonts["footer"],
    )
    rw = draw.textlength(foot_right, font=fonts["footer"])
    draw.text(
        (PAGE_W - PADDING_X - rw, foot_y + 30),
        foot_right,
        fill=COLOR_TEXT_PRIMARY,
        font=fonts["footer"],
    )

    canvas.save(output_path, "PNG", optimize=True)
    print(f"OK -> {output_path}  ({PAGE_W}x{PAGE_H})")


def build_for_cap(cap_num: int) -> str:
    """Construye la comic page para un cap dado y devuelve el output path."""
    if cap_num not in CAP_REGISTRY:
        raise SystemExit(f"Cap {cap_num} no esta registrado")
    title, panels = CAP_REGISTRY[cap_num]
    out_path = os.path.join(STORYBOARDS_DIR, f"cap-{cap_num}-comic-page.png")
    build_page(panels, cap_num=cap_num, cap_title=title, output_path=out_path)
    return out_path


def main():
    """
    CLI:
        python compose_comic_pages.py                  -> compone caps 1 y 2 (default original)
        python compose_comic_pages.py --cap 3          -> solo cap 3
        python compose_comic_pages.py --caps 3,4,5     -> caps 3, 4, 5
        python compose_comic_pages.py --range 3 12     -> caps 3..12
        python compose_comic_pages.py --all            -> caps 1..12
    """
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--cap", type=int, help="Compone solo este cap")
    parser.add_argument("--caps", type=str, help="Lista CSV de caps (ej: 3,4,5)")
    parser.add_argument("--range", nargs=2, type=int, metavar=("START", "END"),
                        help="Rango inclusivo (ej: --range 3 12)")
    parser.add_argument("--all", action="store_true", help="Caps 1..12")
    args = parser.parse_args()

    if not os.path.isdir(STORYBOARDS_DIR):
        raise SystemExit(f"No encontre {STORYBOARDS_DIR}")

    if args.all:
        targets = list(range(1, 13))
    elif args.range:
        targets = list(range(args.range[0], args.range[1] + 1))
    elif args.caps:
        targets = [int(x.strip()) for x in args.caps.split(",")]
    elif args.cap:
        targets = [args.cap]
    else:
        # Comportamiento original — caps 1 y 2
        targets = [1, 2]

    outputs = []
    for cap_num in targets:
        out = build_for_cap(cap_num)
        outputs.append(out)

    print(f"\n[OK] {len(outputs)} comic pages generadas:")
    for o in outputs:
        print(f"  - {o}")


if __name__ == "__main__":
    main()
