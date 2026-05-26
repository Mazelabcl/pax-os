# Sistema Escalable: Video Educativo Paxeado

Pipeline de 6 pasos para transformar cualquier video educativo de YouTube en un video "paxeado" — misma ensenanza, narrada por un personaje Pax, con visuales del Uray Pacha.

---

## Pipeline

### Paso 1 — Ingesta
- **Input:** URL de YouTube
- **Output:** Transcripcion completa + metadata (titulo, duracion, idioma)
- **Agente:** `transcriptor` — usa YouTube Data API + whisper fallback
- **Fallback:** si no hay transcripcion disponible, WebSearch del tema + brief manual

### Paso 2 — Analisis de contenido
- **Input:** Transcripcion
- **Output:** Estructura del metodo (N pasos), puntos clave, tono, publico objetivo
- **Agente:** `analizador-educativo` — LLM que extrae la estructura pedagogica
- **Reglas:** identificar pasos concretos, eliminar relleno, detectar el "metodo" central

### Paso 3 — Seleccion de personaje
- **Input:** Tema + tono del video original
- **Output:** Personaje Pax asignado como "maestro" + personaje "alumno"
- **Agente:** `casting-pax` — mapea temas a personajes segun su rol en el lore
- **Tabla base:**
  - Sabiduria/filosofia → Wiz (maestro) + Jiggy (alumno)
  - Tecnologia/sistemas → Byte (maestro) + KZ (alumno)
  - Emociones/relaciones → Luxa o Agatha (maestra) + Jiggy (alumno)
  - Creatividad/arte → Ludus (maestro) + Luz (alumna)
  - Disciplina/fuerza → Onyx o Fortis (maestro) + Jiggy (alumno)

### Paso 4 — Script paxeado
- **Input:** Estructura del metodo + personaje maestro + personaje alumno
- **Output:** Script de 60-90 seg con 4-6 escenas, dialogos, indicaciones visuales
- **Agente:** `guionista-pax` — LLM con contexto de lore + style-guide + canon completo
- **Reglas:**
  - Integrar cada paso del metodo en la mecanica Pax (cristales, anuraK, Ayni)
  - El "maestro" ensena, el "alumno" aprende con humor
  - Cerrar con un Ayni concreto y accionable para el espectador
  - Idioma: espanol neutro, sin voseo

### Paso 5 — Generacion de frames
- **Input:** Script con descripciones de escena + char sheets de personajes
- **Output:** 2 imagenes por escena (start frame + end frame), ~8-12 PNGs
- **Agente:** `frame-gen` — usa `scripts/openai_images.py` (gpt-image-2) con refs de personaje
- **Reglas:**
  - Estilo: 3D PBR neon-magic, paleta Pax canonica
  - Formato: 1536x1024 (16:9 landscape)
  - Cada par start/end debe mostrar cambio claro (para interpolar con video-gen)

### Paso 6 — Generacion de video
- **Input:** Pares start/end frame + script con timing
- **Output:** Clips de 3-5 seg por escena, ensamblados en video final de 60-90 seg
- **Herramienta:** Kling / Seedance 2 (manual por ahora, automatizable con API)
- **Post-produccion:** voice-over IA + musica ambient + textos en pantalla

---

## Escalamiento

### Fase 1 (actual) — Manual asistido
- Aldot pega URL, Claude analiza, genera script + frames
- Aldot genera video manualmente con Kling/Seedance
- Feedback via landing HTML con botones por escena

### Fase 2 — Semi-automatico
- Script Python orquesta pasos 1-5 en secuencia
- Solo paso 6 (video) requiere intervencion manual
- Queue de videos pendientes en un JSON local

### Fase 3 — Full pipeline
- API de Kling/Seedance integrada para paso 6
- Interfaz web: pegar URL → preview storyboard → generar video
- Batch processing: N videos por noche

---

## Metricas de exito
- Tiempo total por video paxeado (target: < 30 min con pipeline completo)
- Consistencia visual entre videos (mismo personaje = mismo look)
- Engagement: views, retention, shares del video publicado
- Ayni generado: cuantas personas reportan haber hecho el CTA del final
