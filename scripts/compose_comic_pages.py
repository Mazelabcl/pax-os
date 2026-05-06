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


def main():
    if not os.path.isdir(STORYBOARDS_DIR):
        raise SystemExit(f"No encontre {STORYBOARDS_DIR}")

    out_cap_1 = os.path.join(STORYBOARDS_DIR, "cap-1-comic-page.png")
    out_cap_2 = os.path.join(STORYBOARDS_DIR, "cap-2-comic-page.png")

    build_page(
        CAP_1_PANELS,
        cap_num=1,
        cap_title="La red oxidada",
        output_path=out_cap_1,
    )
    build_page(
        CAP_2_PANELS,
        cap_num=2,
        cap_title="El templo que nadie cuido",
        output_path=out_cap_2,
    )


if __name__ == "__main__":
    main()
