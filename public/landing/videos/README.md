# Videos del landing scroll-video

Drop aquí los archivos mp4 que aldot genere:

- pax-scene-1-h.mp4 — escena 1, horizontal (desktop)
- pax-scene-1-v.mp4 — escena 1, vertical (mobile)
- pax-scene-2-h.mp4 — escena 2, horizontal (RESERVA, opcional)
- pax-scene-2-v.mp4 — escena 2, vertical (RESERVA, opcional)

## Especificaciones tecnicas recomendadas

- Codec: H.264 (NO H.265/HEVC — algunos navegadores no scrubean bien)
- Keyframes cada 1-2 segundos (clave para que el scroll-scrub sea fluido y no se sienta saltón)
- Duración: 8-15 segundos por video
- Sin audio (el script lo silencia igual)
- Bitrate: ~5-8 Mbps para horizontal 1080p

Si los videos vienen con keyframes muy espaciados, se puede re-encodear con ffmpeg:
ffmpeg -i input.mp4 -c:v libx264 -g 30 -keyint_min 30 -an output.mp4
