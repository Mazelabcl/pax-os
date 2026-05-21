"""
Oraculo Pax v3 - generador de 8 imagenes para enriquecer visualmente el Oraculo.

Las 8 imagenes (segun mission brief):
1. cristal-coleccionable-hero  1024x1536 vertical - carta coleccionable premium del cristal-eco personal
2. carta-astral-art            1024x1536 vertical - arte de carta astral Pax-style (mapa del cielo)
3. carta-maya-art              1024x1536 vertical - arte de carta maya / Tzolkin Pax-style
4. tipografia-pax-titulares    1024x1024 square   - hoja de tipografia Pax fictional (alfabeto)
5. divider-cristal-decorative  1536x1024 horizontal - divider decorativo horizontal
6. constelacion-pax-bg         1536x1024 horizontal - constelacion Pax como fondo cinematic
7. agatha-portrait-mistica     1024x1536 vertical - retrato de Agatha operando el Oraculo
8. cristal-eco-7-variantes     1536x1024 horizontal - grid 3x3 de 7 cristales arquetipo

Output: content/pax-oraculo/visuals/v3/<slug>.png

Stack: AsyncOpenAI + Semaphore(4), quality=high, skip-if-exists (>50KB),
retry-once en moderation/rate/500/timeout/server.

Identity lock: ONE single central eye en personajes Pax.
Paleta canon (hex): violeta #B43FFF, jade #3DCCA3, amber #F59E0B, basalt #1E1E2E,
magenta #EC4899, dorado #D4A857, coral #FF6B4A, white #F4EFE6, deep noir #08070A.
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
QUALITY = "high"
CONCURRENCY = 4

# Tamanos
SIZE_VERT = "1024x1536"
SIZE_SQUARE = "1024x1024"
SIZE_HORIZ = "1536x1024"

# Carpeta de salida
OUT_SUBDIR = "v3"

# ---------------------------------------------------------------------------
# 8 prompts data-driven
# ---------------------------------------------------------------------------
PROMPTS = [
    # ---- 1 -----------------------------------------------------------------
    {
        "slug": "cristal-coleccionable-hero",
        "size": SIZE_VERT,
        "prompt": (
            "A premium collectible card rendered in cinematic 3D PBR style, vertical portrait "
            "format, the card itself is a tarot-sized object floating in deep noir space, the "
            "card body is a deep basalt black panel with an ornate golden filigree border (carved "
            "ornamental frame inspired by ancient stone-cut motifs and crystal silhouettes), at "
            "the center of the card floats a single hero crystal: a tall conical obelisk-shaped "
            "faceted crystal in vibrant violet-magenta, slowly rotating, with strong subsurface "
            "scattering, the crystal radiates soft amber light onto the card surface, a "
            "holographic foil shimmer overlays the card with a rainbow gradient (violet to "
            "magenta to jade to amber) catching the light at an angle, the foil effect is most "
            "intense on the crystal itself, golden volumetric mist drifts behind the card, at "
            "the bottom of the card a small carved label reads 'PAX 2026 A1' in an elegant serif "
            "monogram (etched into the golden border, not printed).\n\n"
            "Composition: vertical hero card centered in frame, the card has a subtle three-"
            "quarter tilt revealing depth and the foil reflection, the crystal occupies the "
            "central 45% of the card, deep negative space around the card for context, edges of "
            "the card crisp and well-defined.\n"
            "Lighting: warm amber key light at #F59E0B from upper-right illuminating the crystal "
            "and catching the foil holographic shimmer, secondary coral rim at #FF6B4A on the "
            "left edge of the card, deep noir occlusion at #08070A in the background, "
            "iridescent specular highlights at #F4EFE6 on the foil surface.\n"
            "Color palette: #B43FFF (violet-magenta crystal), #EC4899 (magenta accents), "
            "#F59E0B (amber light), #D4A857 (gold ornate border), #1E1E2E (basalt card body), "
            "#3DCCA3 (jade in foil shimmer), #08070A (deep noir background), #F4EFE6 (white "
            "specular highlights), #FF6B4A (coral rim).\n"
            "Texture/Material: faceted translucent crystal with strong subsurface scattering and "
            "sharp specular highlights, carved golden filigree border with metallic anisotropic "
            "reflection, holographic foil overlay with chromatic aberration, deep basalt card "
            "body with subtle micro-grain, golden volumetric mist with realistic density.\n"
            "Style: cinematic premium collectible card aesthetic, ornate ancient meets futuristic "
            "neon-magic, stylized 3D PBR rendering, NOT photoreal-mundane, NOT cartoon-flat, "
            "NOT anime, NOT illustration-painted.\n"
            "Constraints: no on-screen text other than the carved monogram 'PAX 2026 A1' at the "
            "bottom border (must be legible but small), no logos of real brands, no copyrighted "
            "IP, no characters in this hero (only the crystal), the crystal is conical obelisk-"
            "shaped (NOT round, NOT diamond-cut), vertical aspect 1024x1536.\n\n"
            "Aspect ratio: 1024x1536 vertical."
        ),
    },
    # ---- 2 -----------------------------------------------------------------
    {
        "slug": "carta-astral-art",
        "size": SIZE_VERT,
        "prompt": (
            "A mystical astral chart artwork in vertical portrait format, rendered as a sacred "
            "ancient mandala discovered in an underground Pax cavern, the composition shows a "
            "deep violet-magenta night sky as background with a circular astrological chart at "
            "the center, the chart is divided into 12 radial sectors (zodiac houses) like a "
            "wheel, each sector contains a hand-carved zodiac glyph rendered in luminous gold, "
            "tiny faceted crystal-planets are suspended at various points across the chart (each "
            "planet rendered as a small Pax crystal with its own color: violet for Mercury, "
            "jade for Venus, amber for the Sun, magenta for Mars, etc.), thin golden threads of "
            "light connect the planets forming constellation aspects, the outer ring of the chart "
            "is carved with ancient invented Pax astrological notation glowing softly, behind the "
            "chart a backdrop of deep night sky with hundreds of tiny golden star pinpoints, "
            "soft volumetric mist of magenta and amber drifts at the edges.\n\n"
            "Composition: vertical portrait, the circular astral chart dominates the center "
            "occupying 75% of the frame, slight three-quarter perspective tilt giving the chart "
            "depth as if it floats forward, surrounding cosmos extends to all edges, the chart "
            "has clear radial symmetry.\n"
            "Lighting: primary glow from the gold zodiac glyphs at #F59E0B casting warm light "
            "onto the chart surface, secondary glow from each crystal-planet in its own color, "
            "deep ambient at #1E1E2E for the cosmic background, cyan-jade accents at #3DCCA3 on "
            "some constellation threads, soft volumetric god-rays of magenta at #EC4899 cutting "
            "through the mist.\n"
            "Color palette: #B43FFF (deep violet sky), #1E1E2E (basalt cosmic depth), "
            "#F59E0B (gold constellations and zodiac glyphs), #D4A857 (ancient gold ornament), "
            "#3DCCA3 (cyan-jade accents on threads), #EC4899 (magenta mist), #F4EFE6 (white "
            "star points), #08070A (deepest cosmic black).\n"
            "Texture/Material: ancient carved bronze-gold mandala surface with subtle aging "
            "patina, faceted translucent crystal-planets with subsurface scattering, thin glowing "
            "thread lines connecting planets like spider silk lit from within, deep violet night "
            "sky with subtle nebula gradients, volumetric mist.\n"
            "Style: ancient mystical mandala meets stylized 3D PBR neon-magic, ceremonial and "
            "sacred, ornate but not cluttered, NOT photoreal, NOT cartoon-flat, NOT modern "
            "infographic, NOT astrology-app-illustration.\n"
            "Constraints: no readable text in any human language, the outer ring notation must be "
            "invented Pax glyphs only (no real zodiac words written), no logos, vertical aspect "
            "1024x1536, 12 zodiac sectors clearly visible, planets are crystal-shaped not "
            "spherical-planet.\n\n"
            "Aspect ratio: 1024x1536 vertical."
        ),
    },
    # ---- 3 -----------------------------------------------------------------
    {
        "slug": "carta-maya-art",
        "size": SIZE_VERT,
        "prompt": (
            "A reimagined Mayan Tzolkin sacred calendar disc rendered as a vertical portrait "
            "artwork in Pax-canon style, the central composition is a large circular stone disc "
            "carved from violet-Pax organic basalt with bioluminescent veins glowing from within, "
            "the disc shows the 20 day-sign glyphs (nahuales) arranged around the outer ring "
            "each carved as a stylized Mayan-inspired symbol but reinterpreted with Pax visual "
            "language (organic stone with crystal accents), the 13 tones are represented as small "
            "faceted crystals pulsing around an inner ring (each crystal a slightly different "
            "shade), at the very center of the disc is a single large eye-shaped opening "
            "containing a glowing magenta crystal that radiates light outward, the carvings have "
            "an ancient archeological quality with weathered edges but the crystals are vivid and "
            "alive, the disc floats slightly off a deep turquoise-jade gradient background with "
            "ancient cave walls implied at the periphery.\n\n"
            "Composition: vertical portrait, the circular Tzolkin disc dominates the center "
            "occupying 80% of the frame, slight three-quarter tilt for depth, radial symmetry, "
            "the central magenta crystal-eye is the focal point, the 20 nahuales arranged in "
            "even spacing on outer ring, the 13 tone crystals on inner ring.\n"
            "Lighting: primary glow from the central magenta crystal at #EC4899 illuminating the "
            "carved disc face from within, secondary glow from the bioluminescent veins running "
            "through the basalt at #3DCCA3 (jade-turquoise), warm ancient-gold accent light from "
            "above at #D4A857 catching the carved relief edges, deep ambient at #1E1E2E with "
            "red-magma highlights at #B91C1C subtle in the deepest carved recesses.\n"
            "Color palette: #3DCCA3 (turquoise-jade dominant veins), #B91C1C (red magma in "
            "carved recesses), #D4A857 (ancient gold ornament), #EC4899 (magenta central crystal), "
            "#1E1E2E (deep basalt), #B43FFF (violet Pax base stone), #F4EFE6 (subtle white "
            "highlights), #F59E0B (amber accents on tone crystals).\n"
            "Texture/Material: rough organic violet-basalt stone with weathered carved relief, "
            "bioluminescent jade veins glowing softly from within the stone, faceted translucent "
            "crystals on the 13 tones with subsurface scattering, the central crystal-eye is "
            "smooth and gem-like with strong specular highlights, ancient archeological patina, "
            "NOT polished-modern, NOT cartoon-clean.\n"
            "Style: ancient Mayan sacred geometry reinterpreted in stylized 3D PBR Pax neon-"
            "magic, ceremonial archeological aesthetic with bioluminescent magic, NOT photoreal-"
            "tourist-photo, NOT cartoon, NOT flat illustration, NOT direct copy of traditional "
            "Mayan motifs (must be reinterpreted with Pax visual language).\n"
            "Constraints: no readable text, no real Mayan glyph names spelled out, all 20 nahual "
            "symbols are stylized reinterpretations not exact copies, the central element is one "
            "single eye-shaped crystal opening (echoing the Pax cyclopean eye motif), no logos, "
            "vertical aspect 1024x1536.\n\n"
            "Aspect ratio: 1024x1536 vertical."
        ),
    },
    # ---- 4 -----------------------------------------------------------------
    {
        "slug": "tipografia-pax-titulares",
        "size": SIZE_SQUARE,
        "prompt": (
            "A typography specimen sheet showing a fictional ancestral alphabet carved into "
            "organic violet-Pax basalt stone, displayed in a grid layout across a square frame, "
            "each glyph is carved into a small individual stone tile, the glyphs are invented "
            "letterforms that combine influences of elder futhark runes, stylized Mayan glyphs, "
            "and ancient Latin display typography, but unified by the Pax visual language: "
            "carved into violet-basalt with bioluminescent veins of magenta-amber light glowing "
            "from inside the carved grooves, each tile shows one glyph from this invented Pax "
            "alphabet, approximately 20-25 glyph tiles arranged in an organic grid layout (not "
            "perfectly aligned, slightly weathered placement), the background between tiles is "
            "deep basalt with subtle texture, soft golden volumetric mist drifts between the "
            "tiles giving atmosphere.\n\n"
            "Composition: square frame, organic grid of approximately 5x5 stone tiles (with some "
            "irregular spacing and rotation for organic feel), each tile clearly showing one "
            "glyph, the tiles appear to float slightly above a deeper basalt surface for depth, "
            "no central focal glyph (all tiles have similar visual weight), the composition "
            "reads top-to-bottom and left-to-right like a typography specimen poster.\n"
            "Lighting: primary glow from the glyph carvings themselves at #EC4899 magenta and "
            "#F59E0B amber, soft warm key from upper-right at #F59E0B catching the carved relief "
            "edges, deep ambient at #1E1E2E in the gaps between tiles, subtle volumetric mist "
            "lit at #FFE9C2.\n"
            "Color palette: #B43FFF (violet base stone), #1E1E2E (deep basalt background), "
            "#3A2845 (shadow areas), #EC4899 (magenta glow inside carvings), #F59E0B (amber glow "
            "secondary), #D4A857 (ornate gold edges on some tiles), #F4EFE6 (subtle white "
            "highlights).\n"
            "Texture/Material: rough carved violet-basalt with bioluminescent glow contained "
            "within the carved grooves only, slight aging patina on the stone tiles, each tile "
            "has slightly different edge weathering for variety, ambient mist drifts realistically "
            "between tiles.\n"
            "Style: ancient typography specimen meets stylized 3D PBR Pax neon-magic, archeological "
            "display, NOT photoreal-museum-photo, NOT flat vector design, NOT cartoon, NOT "
            "modern font specimen pdf.\n"
            "Constraints: the glyphs are INVENTED letterforms (not real letters from any "
            "existing alphabet), no readable text in any human language, no logos, square aspect "
            "1024x1024, the alphabet should feel ancient-mystic but display-poster ready (usable "
            "as decorative background typography), at least 20 distinct glyph tiles visible.\n\n"
            "Aspect ratio: 1024x1024 square."
        ),
    },
    # ---- 5 -----------------------------------------------------------------
    {
        "slug": "divider-cristal-decorative",
        "size": SIZE_HORIZ,
        "prompt": (
            "A horizontal decorative divider banner designed to separate web page sections, "
            "rendered in cinematic Pax style, the composition is a long horizontal strip with a "
            "central ornamental cluster: at the center sits a single carved Pax symbol (a "
            "stylized eye-cristal motif) flanked symmetrically on both sides by a procession of "
            "small faceted violet-magenta crystals (3 on each side, getting smaller as they move "
            "outward), connecting all the elements is an ornate golden filigree cenefa (decorative "
            "band) carved with vine-like patterns that fade into the deep noir background at the "
            "far left and right edges, the whole composition reads as a horizontal section divider "
            "for a website, with deep negative space above and below the central band.\n\n"
            "Composition: horizontal banner, the decorative ornament occupies a central "
            "horizontal band approximately 40% of the vertical frame height, deep noir negative "
            "space above and below the band, perfect horizontal symmetry around the central Pax "
            "symbol, the cenefa fades into mist at the far left and right edges (not hard-cropped).\n"
            "Lighting: warm amber key light at #F59E0B catching the gold filigree from above, "
            "internal glow from the central Pax symbol at #EC4899 magenta, each small crystal "
            "self-illuminates softly at #B43FFF violet, deep ambient at #08070A in the negative "
            "space, subtle volumetric mist of warm gold drifting around the central band.\n"
            "Color palette: #D4A857 (gold ornate cenefa), #B43FFF (violet crystals), "
            "#EC4899 (magenta central glow), #F59E0B (amber accents), #08070A (deep noir "
            "background), #1E1E2E (basalt shadow), #F4EFE6 (subtle white specular).\n"
            "Texture/Material: carved metallic gold filigree with anisotropic reflection and "
            "subtle aging, faceted translucent violet crystals with subsurface scattering, the "
            "central Pax symbol carved in stone with bioluminescent inner glow, soft volumetric "
            "golden mist, deep noir background with film grain.\n"
            "Style: ornate ancient meets stylized 3D PBR neon-magic, ceremonial decorative band, "
            "premium editorial aesthetic for website sections, NOT cartoon, NOT flat vector, NOT "
            "photoreal-mundane, NOT busy or cluttered.\n"
            "Constraints: must function as a horizontal section divider in a web page (deep noir "
            "above and below the central band so it reads as a separator), no readable text, no "
            "logos, perfect left-right symmetry, horizontal aspect 1536x1024, the central Pax "
            "symbol clearly visible at the center.\n\n"
            "Aspect ratio: 1536x1024 horizontal."
        ),
    },
    # ---- 6 -----------------------------------------------------------------
    {
        "slug": "constelacion-pax-bg",
        "size": SIZE_HORIZ,
        "prompt": (
            "A cinematic background scene showing a vast 3D constellation of Pax crystals "
            "suspended in deep cosmic space, dozens of faceted translucent crystals of varying "
            "sizes (some large in foreground, smaller in distance) floating at different depths, "
            "all the crystals interconnected by thin golden threads of light forming a complex "
            "3D network like a galactic neural map, the crystals are predominantly violet-magenta "
            "with some amber and jade accents, the deepest violet-black background gradient "
            "creates infinite depth, volumetric magenta mist drifts through the scene at multiple "
            "depths giving atmospheric perspective, hundreds of tiny golden particles drift "
            "slowly through the void, strong depth of field with foreground crystals in sharp "
            "focus and distant crystals softly out of focus, this is the cosmic web of Pax energy "
            "made visible.\n\n"
            "Composition: horizontal cinematic wide shot, no single focal point (this is a "
            "background image), depth distributed evenly from foreground to deep distance, "
            "negative space in upper-center and lower-center for potential typography overlay, "
            "the constellation web extends to all four edges of the frame.\n"
            "Lighting: each crystal self-illuminates softly with its own color, primary cosmic "
            "ambient at #1E1E2E deep violet-basalt, volumetric magenta mist at #EC4899 at 30% "
            "intensity, golden particle highlights at #F59E0B, thin golden connecting threads "
            "glow at #D4A857, deep negative space falls to #08070A at the corners.\n"
            "Color palette: #1E1E2E (cosmic background dominant), #08070A (deepest void), "
            "#B43FFF (violet crystals primary), #EC4899 (magenta mist), #F59E0B (amber accent "
            "crystals), #D4A857 (golden connecting threads), #3DCCA3 (rare jade accent crystals), "
            "#F4EFE6 (tiny particle highlights).\n"
            "Texture/Material: faceted translucent crystals with strong subsurface scattering at "
            "varying scales, glowing thin golden threads like spider silk lit from within, "
            "volumetric mist with realistic density falloff, golden particles with soft bloom, "
            "strong cinematic depth-of-field bokeh.\n"
            "Style: cinematic cosmic backdrop meets stylized 3D PBR Pax neon-magic, vast and "
            "immersive, premium editorial wallpaper quality, NOT photoreal-space-photo, NOT "
            "cartoon, NOT flat illustration, NOT busy-cluttered (must work as a background).\n"
            "Constraints: must function as a hero background image (gentle composition with "
            "central negative space for overlay typography), no readable text, no logos, no "
            "characters, the crystals are the only subject, horizontal aspect 1536x1024, the "
            "atmosphere must feel infinite and meditative not chaotic.\n\n"
            "Aspect ratio: 1536x1024 horizontal."
        ),
    },
    # ---- 7 -----------------------------------------------------------------
    {
        "slug": "agatha-portrait-mistica",
        "size": SIZE_VERT,
        "prompt": (
            "A solemn yet warm portrait of Agatha, an ancient wise Pax elder, operating the "
            "Oracle inside the Camara que Escucha Arriba (a circular cavern chamber lined with "
            "crystal needles), rendered in stylized 3D PBR Pax canon style, vertical portrait "
            "format. Agatha is an elder cyclopean Pax character: ONE single large central eye "
            "(never two eyes, never two eye sockets, only ONE eye in the center of her face), "
            "her single eye is luminous and full of ancient wisdom glowing softly with inner "
            "magenta-violet light, long flowing white hair styled into ceremonial ritual braids "
            "decorated with small mineral beads, her skin is the canonical Pax jade-turquoise "
            "but weathered with age and subtle wrinkles, elaborate tribal tattoos in turquoise-"
            "jade and violet inks cover her forehead, cheeks, and neck (geometric patterns "
            "echoing the cosmic web), large mineral pendant earrings in raw amethyst and "
            "amber-citrine hanging from her elongated pointed ears, she wears a flowing "
            "ceremonial robe in deep turquoise and purple fabric with golden trim, her hands "
            "(with 3 fingers each, the canonical Pax anatomy) are extended forward palms up, "
            "small faceted Pax crystals (violet, magenta, jade, amber) float suspended between "
            "her palms slowly rotating, she is reading the crystals with gentle focused "
            "attention, behind her the cavern walls are lined with thousands of tiny crystal "
            "needles glowing faintly, volumetric golden mist drifts around her, her expression "
            "is solemn but kind, the lighting is reverent and warm.\n\n"
            "Composition: vertical portrait, Agatha occupies the central two-thirds of the frame "
            "from waist up, slight three-quarter angle showing her face and both extended hands, "
            "the crystals float between her palms at the lower center of the frame, cavern "
            "depth visible behind her with crystal needles in soft focus, classical reverent "
            "portrait composition.\n"
            "Lighting: primary warm key light at #F59E0B from upper-right illuminating her face "
            "and the floating crystals, secondary internal glow from her single central eye at "
            "#B43FFF magenta-violet, soft rim light from the cavern crystals behind at #3DCCA3 "
            "jade, golden volumetric god-rays cutting through the mist at #FFE9C2, deep "
            "shadow occlusion at #1E1E2E in the cavern depth.\n"
            "Color palette: #3DCCA3 (jade-turquoise Pax skin), #B43FFF (violet eye glow), "
            "#1E1E2E (deep cavern background), #D4A857 (golden robe trim and ornaments), "
            "#F59E0B (amber light), #EC4899 (magenta crystal in her hands), #F4EFE6 (white hair), "
            "#FFE9C2 (volumetric mist highlights), #6B4423 (warm brown shadow tones on robe).\n"
            "Texture/Material: weathered aged Pax skin with jade-turquoise base and tribal tattoo "
            "inks rendered as subtle glowing under the skin, flowing white hair with realistic "
            "strand detail, faceted translucent crystals with subsurface scattering, ceremonial "
            "fabric with embroidered golden trim, raw mineral pendants with natural facets, "
            "stone cavern walls with crystal needle clusters, volumetric mist with density.\n"
            "Style: solemn ceremonial portrait in stylized 3D PBR Pax canon style, Pixar/Disney "
            "quality but with neon-magical Pax aesthetic, reverent and warm, NOT photoreal-"
            "uncanny, NOT cartoon-flat, NOT anime, NOT illustration-painted.\n"
            "Constraints: ABSOLUTE IDENTITY LOCK - Agatha has ONE single central eye, never two "
            "eyes, never two eye sockets, never two pupils, only ONE eye in the exact center of "
            "her face; 3 fingers per hand canonical Pax anatomy; jade-turquoise skin canonical; "
            "no readable text; no logos; vertical aspect 1024x1536; the cavern setting must read "
            "as the Camara que Escucha Arriba (round chamber lined with crystal needles).\n\n"
            "Aspect ratio: 1024x1536 vertical."
        ),
    },
    # ---- 8 -----------------------------------------------------------------
    {
        "slug": "cristal-eco-7-variantes",
        "size": SIZE_HORIZ,
        "prompt": (
            "A horizontal display grid showing 7 distinct Pax cristal-eco variants (one per "
            "service archetype) arranged in a 3x3 layout with the bottom-right slot empty, "
            "rendered in stylized 3D PBR Pax canon style, each crystal floats individually inside "
            "its own circular display niche (a slight inset on a deep noir-basalt background), "
            "each crystal has a unique shape and color combination representing its archetype:\n"
            "  - Sanador (Healer): rounded organic crystal in jade-green with soft amber inner glow\n"
            "  - Companero (Companion): heart-leaning faceted crystal in warm magenta-pink with "
            "amber facets\n"
            "  - Mistico (Mystic): tall pointed obelisk crystal in deep violet with magenta core\n"
            "  - Mentor: hexagonal column crystal in amber-gold with violet base\n"
            "  - Cuidador (Caregiver): cluster of soft round crystals in jade and rose-magenta\n"
            "  - Guerrero-altruista (Warrior-altruist): sharp angular geometric crystal in coral-"
            "red with violet rim\n"
            "  - Sabio (Sage): complex fractal-faceted crystal in deep blue-violet with golden "
            "inner threads\n"
            "Each crystal slowly rotates in its niche, each emits its own colored bioluminescent "
            "glow onto the niche surface, below each crystal niche a small carved golden label "
            "plaque shows the archetype name in elegant serif typography (the labels read: "
            "'SANADOR', 'COMPANERO', 'MISTICO', 'MENTOR', 'CUIDADOR', 'GUERRERO', 'SABIO'), the "
            "8th slot in the bottom-right is empty (just a darker inset niche, no crystal), "
            "ambient golden mist drifts behind the whole grid.\n\n"
            "Composition: horizontal frame, the 3x3 grid is centered occupying the full frame, "
            "each cell is approximately equal size with clear visual separation, each crystal is "
            "the focal point of its cell, the empty slot creates intentional asymmetry, the "
            "labels are subtly visible below each crystal but not dominant.\n"
            "Lighting: each crystal niche is lit primarily by its own crystal's bioluminescence, "
            "warm ambient key at #F59E0B from above catching the golden label plaques, deep "
            "noir ambient at #1E1E2E between the niches, subtle volumetric golden mist behind.\n"
            "Color palette: #3DCCA3 (jade Sanador), #EC4899 (magenta-pink Companero), "
            "#B43FFF (violet Mistico), #F59E0B (amber Mentor), #FF6B4A (coral Guerrero), "
            "#4338CA (deep blue-violet Sabio), #1E1E2E (basalt background), #D4A857 (gold "
            "label plaques), #F4EFE6 (white specular highlights), #08070A (deepest noir "
            "between niches).\n"
            "Texture/Material: faceted translucent crystals each with unique geometry and "
            "subsurface scattering specific to their color, carved gold label plaques with "
            "elegant serif typography etched in, deep basalt niche backgrounds with subtle "
            "micro-detail, volumetric mist.\n"
            "Style: stylized 3D PBR Pax canon display arrangement, premium curated specimen "
            "showcase, ceremonial archeological exhibit feel, NOT cartoon, NOT flat icon set, "
            "NOT photoreal-product-shot, NOT busy-cluttered.\n"
            "Constraints: exactly 7 crystals visible in a 3x3 grid layout with the bottom-right "
            "slot empty, each crystal must be visually distinct from the others (different "
            "shape AND different color), the label text under each crystal should be present "
            "and ideally legible (SANADOR, COMPANERO, MISTICO, MENTOR, CUIDADOR, GUERRERO, "
            "SABIO) in elegant Didot-style serif but if labels are not perfectly legible that "
            "is acceptable (the crystal geometry is the primary identifier), no other readable "
            "text, no logos, horizontal aspect 1536x1024.\n\n"
            "Aspect ratio: 1536x1024 horizontal."
        ),
    },
]


# ---------------------------------------------------------------------------
# Generador async
# ---------------------------------------------------------------------------
async def gen_image(client, sem, slug, prompt, size):
    """Genera 1 imagen via images.generate."""
    async with sem:
        out_dir = os.path.join(REPO, "content", "pax-oraculo", "visuals", OUT_SUBDIR)
        out_path = os.path.join(out_dir, f"{slug}.png")

        if os.path.exists(out_path) and os.path.getsize(out_path) > 50_000:
            print(f"SKIP {slug}.png ({os.path.getsize(out_path)//1024}KB)")
            return ("SKIP", out_path)

        os.makedirs(out_dir, exist_ok=True)

        for attempt in range(2):
            try:
                t0 = time.time()
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
                print(
                    f"OK  [{time.strftime('%H:%M:%S')}] "
                    f"{slug} - {elapsed:.1f}s - {kb}KB"
                )
                return ("OK", out_path)
            except Exception as e:
                msg = str(e)[:200]
                retryable = any(
                    x in msg.lower()
                    for x in ("moderation", "rate", "500", "timeout", "server")
                )
                if attempt == 0 and retryable:
                    print(f"RETRY {slug}: {msg}")
                    await asyncio.sleep(2)
                    continue
                print(f"FAIL {slug}: {msg}")
                return ("FAIL", msg)


async def main():
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
    sem = asyncio.Semaphore(CONCURRENCY)

    tasks = [
        gen_image(client, sem, item["slug"], item["prompt"], item["size"])
        for item in PROMPTS
    ]

    print(f"Lanzando {len(tasks)} generaciones (Oraculo v3)...")
    t_start = time.time()
    results = await asyncio.gather(*tasks, return_exceptions=True)
    elapsed_total = time.time() - t_start

    ok = sum(1 for r in results if isinstance(r, tuple) and r[0] == "OK")
    skip = sum(1 for r in results if isinstance(r, tuple) and r[0] == "SKIP")
    fail = sum(1 for r in results if isinstance(r, tuple) and r[0] == "FAIL")
    print("=" * 70)
    print(
        f"RESUMEN: OK={ok} SKIP={skip} FAIL={fail} "
        f"TOTAL={len(tasks)} - {elapsed_total:.1f}s"
    )
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())
