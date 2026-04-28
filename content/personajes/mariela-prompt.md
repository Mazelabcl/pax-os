---
name: Mariela — Prompt de generación
slug: mariela-prompt
---

# Mariela — Prompt de generación visual

> Prompt completo y copiable para generar/regenerar el render de Mariela en cualquier modelo de imagen (Seedance, Midjourney, ChatGPT/DALL·E, etc.).

## Contexto

Mariela Salcedo, 36 años, ingeniera de procesos en Santiago de Chile. Protagonista humana del episodio 1. NO es del universo Pax subterráneo: vive en el plano cotidiano (Providencia/Ñuñoa) y la paleta de su mundo es deliberadamente más apagada y realista que la del universo Pax. El contraste visual entre ella y los Pax es parte del lenguaje de la serie.

## Prompt principal (copiar tal cual)

```
Stylized 3D character render, semi-realistic shading, subsurface scattering on skin, cinematic soft lighting with warm fill, NO magical neon (saved for Pax universe). Subject: Mariela Salcedo, Chilean woman, 36 years old, process engineer in Santiago, Chile.

Appearance: average height, average build, everyday Latin American Chilean features without glamourization or Hollywood polish. Dark brown shoulder-length hair, loose or in a casual ponytail. Tired-but-competent face — not sad, vacant. No noticeable makeup. Eyes that do not seek to be seen. Slight under-eye shadow from screen fatigue.

Wardrobe (office hour, Providencia): muted neutral blouse (gray, beige, soft blue) or simple cardigan over a plain shirt. Dark slacks or dark jeans. Plain flats or quiet sneakers, no visible logos. Worn leather crossbody bag.

Canonical accessory: small worn brown leather notebook with a visible crack along the spine — when she presses the pencil to write a sincere question, the spine crack emits a faint cyan glow, single brief flicker, almost subliminal. Simple wooden pencil.

Locations to support the character:
- Small office in a Providencia building, Excel spreadsheet on screen, fluorescent overhead light, paper coffee cup.
- Santiago metro carriage on the way home, dim reflection of her face on the window, sodium lights blurring past outside.
- Small Ñuñoa apartment kitchen at night, kettle on the stove starting to whistle, view of Santiago skyline through the window, single warm pendant light overhead.

Mood: latinoamerican cotidiano filmado como cotidiano, NO exótico. Pattern-interrupt: real Chilean office and apartment, not Hollywood Latin America. Medium close-up, medium depth of field, color grading muted neutral with greens and grays — deliberate contrast with the saturated magenta/turquoise palette of the Pax subterranean universe.

Render style consistent with the rest of the Pax series character sheets so she lives in the same animated film, but lit and graded for the human/surface plane.
```

## Variaciones útiles

- **Plano oficina:** añadir "wide shot, fluorescent office, multiple monitors, colleague walking past in background, end of day energy".
- **Plano metro:** añadir "tight medium shot, metro window reflection, notebook just pulled from bag, hesitation reading the last page dated 6 months ago".
- **Plano cocina (cliffhanger del episodio):** añadir "kitchen counter, open notebook with handwritten line 'Why did I stop writing here?', pencil resting, faint cyan flicker on spine crack, kettle steam catching the light, her right hand closing around an invisible warmth in her left palm".

## Notas para continuidad con la imagen actual

La imagen base ya entregada está en `public/images/personajes/mariela.png`. Si la regenerás:

1. Mantené paleta apagada (no entres en magenta/turquesa Pax).
2. Mantené la libreta de cuero gastado como accesorio invariante.
3. Tono emocional: vacante, no triste. Si el render sale "deprimido" es overshoot.
4. Aldot todavía no fijó seed canónica para Mariela. Cuando lo haga, agregá `seed: <numero>` al frontmatter de `mariela.md`.

## TODO

- [ ] Aldot: confirmar si la imagen actual se queda como canónica o se regenera con este prompt.
- [ ] Aldot: asignar seed canónica una vez fijada la generación final.
