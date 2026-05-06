---
title: "Escena — Jiggy enfrenta al enemigo en cueva de hongos"
slug: scene-jiggy-vs-enemy-mushroom-cave
date: 2026-05-04
generated_by: pax-image-gen v0 (sub-pipeline pre-gen, escena final, prueba de fuego)
model: gpt-image-2
quality: medium
size: 1536x1024
iteraciones: 1
references_used:
  - C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\personajes\jiggy.png
  - C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-pax-enemy.png
  - C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\concepts\concept-pax-mushrooms.png
  - C:\Users\aldot\.gemini\antigravity\scratch\pax-os\public\images\portadas\portada.png
file: content/test-images/scene-jiggy-vs-enemy-mushroom-cave.png
estado: PASS
sub_pipeline_funciono: si
tags: [escena, jiggy, enemigo, hongos, accion, test-subpipeline, prueba-de-fuego]
---

# Escena — Jiggy enfrenta al enemigo en cueva de hongos

## Descripcion visual completa
Plano medio dinamico en cueva subterranea poblada de hongos Pax bioluminiscentes. Jiggy a la izquierda en pose defensiva-agil agachada: una mano sostiene en alto un fragmento de cristal jade que irradia luz fria sobre su rostro y torso, la otra mano extendida lateral para equilibrio. Su unico ojo central esta fijo en el antagonista. A la derecha-centro, la entidad anti-pulso en postura predatoria: corona de espinas oscuras desplegada, miembros tentaculares parcialmente abiertos, multiples ojillos pequenos brillando rojo-violeta apagado, texturas de coral negro y obsidiana resquebrajada. Hongos bioluminiscentes en primer plano (especimenes ambar y jade con leve blur), agrupacion mas amplia al fondo en bokeh suave. Iluminacion lateral wrap: jade-verde por el lado izquierdo, ambar calido por el derecho, ambos emanando de los hongos diegeticos. Angulo de camara levemente bajo para anadir tension. Esporas magenta neon flotando en aire.

## Sujeto principal
Jiggy (Pax cyclops, IDENTITY LOCK estricta de jiggy.png) frente a la criatura Sombra Pulsora del universo Pax (IDENTITY LOCK estricta de concept-pax-enemy.png), en biome de hongos canonicos (ASSET LOCK de concept-pax-mushrooms.png).

## Composicion
Plano medio. Regla de tercios: Jiggy en tercio izquierdo, enemigo en tercio derecho-centro, hongos anclando el tercio inferior y el fondo. Depth-of-field marcado: foreground hongos en blur ligero, mid-ground personajes en foco nitido, background hongos en bokeh fuerte. Camara levemente baja.

## Paleta dominante
- Jade-verde (cristal de Jiggy + bioluminiscencia del lado izquierdo)
- Ambar calido (bioluminiscencia del lado derecho)
- Basalto-oscuro (paredes y suelo de cueva)
- Rojo-violeta apagado (anti-paleta del enemigo, fill bajo en su lado)
- Magenta neon en micro-detalles (esporas en aire, micro-cristales)

## Cuando usar esta imagen
- Como prueba de coherencia del sub-pipeline pre-gen — escena final (esta es la prueba explicita y paso 5 de 5)
- Como hero shot para promo de un episodio de accion / encuentro antagonico
- Como reference visual para storyboard de secuencias de combate Pax-enemigo

## Cuando NO usar
- Como portrait limpio de Jiggy — el cristal y la pose contaminan el frame
- En contextos cooperativos o pacificos — la escena grita conflicto
- Como reference de design del enemigo o de los hongos aislados — usar los concept arts canonicos directamente

## Validacion post-generacion (checklist 5 items)
1. Jiggy mantiene anatomia cyclops Pax (1 ojo central, 4 dedos, turquesa, orejas puntiagudas) — PASS
2. El enemigo se parece al concept-pax-enemy.png (silueta Sombra Pulsora, corona de espinas, multiples ojillos rojo-violeta apagado, texturas coral-obsidiana) — PASS
3. Los hongos se parecen al concept-pax-mushrooms.png (champignon jade, luminas ambar, bioluminiscencia mixta, micro-detalles magenta) — PASS
4. Composicion coherente (Jiggy izq, enemigo der, hongos primer plano y fondo, regla de tercios, DOF) — PASS
5. Render 3D PBR neon-magic con materiales correctos (subsurface piel, refraccion cristal, emisivo hongos, roughness coral en enemigo) — PASS

Resultado: 5/5 PASS en iteracion 1.

## Sub-pipeline pre-gen — funciono?
Si. Los assets pre-generados en el mismo sub-pipeline (concept-pax-enemy.png y concept-pax-mushrooms.png) fueron honrados por el modelo en la composicion final con fidelidad alta:
- El enemigo conserva silueta, texturas y anti-palette del concept canonico, sin drift hacia "Pax friendly".
- Los hongos conservan tipologia (champignon ceremonial jade + luminas ambar) y micro-detalles del concept botanico.
- Jiggy conserva anatomia cyclops del char sheet.
- La paleta canonica (jade, ambar, basalto) coexiste con la anti-paleta del enemigo (rojo-violeta apagado) sin contaminarse.

Conclusion: el patron "pre-gen concept arts del universo + IDENTITY LOCK estricto sobre cada uno + edit_image con N references" funciona como pipeline reutilizable para escenas que mezclan elementos canonicos con elementos nuevos.

## Notas tecnicas
- Iteraciones: 1 (no requirio regeneracion)
- Cap definido: 3 iteraciones
- Modelo: gpt-image-2
- Costo estimado: ~$0.06-0.08 USD (medium quality, 1536x1024, 4 references)
- Refs entrada (en orden):
  - Image 1: jiggy.png (IDENTITY LOCK Jiggy cyclops, 1 ojo, turquesa, 4 dedos)
  - Image 2: concept-pax-enemy.png (IDENTITY LOCK enemigo Sombra Pulsora)
  - Image 3: concept-pax-mushrooms.png (ASSET LOCK flora Pax)
  - Image 4: portada.png (paleta canonica + render base)
