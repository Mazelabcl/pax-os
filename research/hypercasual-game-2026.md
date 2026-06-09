# Best practices 2025-2026 — Juego hyper-casual web (estilo flappy) con rewarded ads

Research para el gesto game de Pax: atención del jugador → donaciones reales. Fecha: 2026-06-09.

## 1. Game feel / juice

- **Feedback inmediato al input**: el flap debe ejecutar al instante. Truco probado: escalar el pájaro ~1.1x y cambiar su color por unos milisegundos en cada tap ([GameDev Academy](https://gamedevacademy.org/game-feel-tutorial/), [foro LÖVE "Flappy juice"](https://love2d.org/forums/viewtopic.php?t=82165)).
- **Screen shake al morir**: 0.1–0.3 seg, dirección levemente aleatoria, magnitud que decae a cero con easing. No exagerar: rompe legibilidad y marea ([Medium — camera shake](https://gt3000.medium.com/juice-it-adding-camera-shake-to-your-game-e63e1a16f0a6)).
- **Partículas en todo evento**: puff al flap, chispas al pasar un obstáculo, explosión al chocar. Son el "mejor amigo" del juice ([GameAnalytics](https://www.gameanalytics.com/blog/squeezing-more-juice-out-of-your-game-design)).
- **El juice debe hacer eco del core gameplay** — premiar visualmente pasar obstáculos (el punto del juego), no decorar al azar. Sonido distinto para near-miss vs paso limpio refuerza la precisión.
- Polish audiovisual = retención: animación agradable en cada interacción + recompensa visual potente en acciones clave ([Slavna Studio](https://www.slavnastudio.com/blog/profitable-casual-game-development-best-design-practices-monetization-rates-and-2025-trends/)).

## 2. Curva de dificultad y primeros 10 segundos

- **Física consistente = dificultad justa**: mismo impulso de flap, misma gravedad siempre. El jugador predice dónde caerá y al morir sabe qué hizo mal → "una partida más" ([Medium — análisis Flappy Bird](https://medium.com/@thomaspalef/game-design-analysis-of-flappy-bird-and-swing-copters-5c6df9fc10f0)).
- **Cero tutorial**: jugable en segundos, un solo input. Tutoriales bajo 30 seg y acción significativa inmediata → D1 retention >50% en los top hyper-casual ([game-developers.org](https://www.game-developers.org/22-tips-to-increase-player-retention-in-games-the-definitive-guide)).
- **Arranque suave**: primeros 2-3 obstáculos con gap amplio y velocidad baja; escalar gap/velocidad gradualmente. Reto genuino pero alcanzable temprano para que el jugador se sienta competente ([Supersonic](https://supersonic.com/learn/blog/is-your-hyper-casual-game-fun-best-practices-for-boosting-retention)).
- **Muerte en 3 seg con feedback claro está OK** — el flow viene de tarea clara + feedback inmediato + restart instantáneo (sin pantallas intermedias) ([Scientific American — flow](https://www.scientificamerican.com/article/be-one-with-flappy-bird-the-science-of-flow-in-game-design/)).

## 3. Progresión y misiones (sesiones 30-90 seg)

- **Daily missions como "appointment mechanic"**: 3 misiones diarias simples ("pasa 10 obstáculos", "juega 3 partidas", "logra 1 near-miss") crean hábito de retorno ([Deconstructor of Fun](https://www.deconstructoroffun.com/blog/2024/9/23/daily-missions-in-puzzles-why-should-we-see-them-more-often)).
- **Loop diario completable en <15 min**; el jugador se queda si siente progreso aun en sesiones cortas ([Melior Games](https://meliorgames.com/game-development/game-mechanics-that-drive-player-retention/)).
- **Metas acumulativas + unlockeables cosméticos** (skins del personaje, fondos) — capa de metas en niveles que funciona en sesiones frecuentes y breves ([vgames](https://www.vgames.vc/post/hooked-on-your-game-how-to-use-retention-mechanics-to-keep-players-coming-back)). Para Pax: la meta acumulativa natural es la donación colectiva (puntos de todos → $).

## 4. Rewarded ads en web

- **Opciones**: [Google AdSense H5 Games Ads](https://support.google.com/adsense/answer/9959170?hl=en) (rewarded + interstitial, requiere aprobación AdSense), [AppLixir](https://www.applixir.com/) (web-first, CPM $8-15, GDPR built-in, integración ~3 líneas JS, callback `onComplete` para otorgar reward) ([guía AppLixir](https://www.applixir.com/blog/a-guide-to-monetizing-html5-games-with-rewarded-video-ads/)).
- **UX correcta (reglas CrazyGames, el estándar de facto)**: opt-in siempre; no encadenar 2+ ads por un reward; no ofrecerlo demasiado seguido (timer u ocultar botón); nunca diseñar niveles que requieran ad; el rewarded debe ser oportunidad especial, no expectativa ([CrazyGames docs](https://docs.crazygames.com/requirements/ads/)).
- **Placement**: en pausas naturales — pantalla de game over ("revive" o "x2 donación") es el punto clásico ([Bidlogic](https://bidlogic.io/2025/02/28/how-to-monetize-the-html5-games-with-advertising/)).
- **Por qué funciona**: completion rate >90%, +20% retención vs interstitials forzados, >70% de usuarios prefiere ver ad por beneficio ([AppSamurai](https://appsamurai.com/blog/rewarded-ads-in-mobile-games-strategy-data-and-best-practices/), [Genieee](https://genieee.com/blogs/how-to-monetize-html5-games-in-2025-your-complete-guide/)).
- **Placeholder pre-ads**: simular el flujo completo — botón opt-in → video corto propio (15-30 seg, ej. clip Pax/lore) → callback que otorga el reward. Así la UX y el contrato "atención = donación" quedan validados antes de integrar la red real.
- **Encaje Pax**: rewarded = intercambio justo de atención (modelo de dos lados). Reencuadre: "tu atención se convierte en donación" hace explícito el value exchange que la literatura identifica como la clave del formato.

## 5. Retención sin app store

- **localStorage**: high score, racha diaria, misiones, cosméticos desbloqueados — progreso que persiste entre sesiones es lo que sostiene retorno ([Featureupvote](https://featureupvote.com/blog/game-retention/)).
- **Leaderboard segmentado** (global / amigos) + share de score (Web Share API con imagen del resultado) crean competencia y pertenencia ([Melior Games](https://meliorgames.com/game-development/game-mechanics-that-drive-player-retention/)).
- **Streaks con daily reward** (login rewards escalonados) son el mecanismo más simple de hábito ([MAF](https://maf.ad/en/blog/daily-login-rewards-engagement-retention/)).

## 6. Performance Three.js mobile

- **Pixel ratio cap**: `renderer.setPixelRatio(Math.min(devicePixelRatio, 1.5))` — target 1–1.5 en móvil evita throttling de GPU y drenaje de batería ([three.js forum](https://discourse.threejs.org/t/changing-pixelratio-based-on-fps-good-or-bad-idea/34563), [MoldStud](https://moldstud.com/articles/p-optimizing-three-js-for-mobile-platforms-tips-and-tricks)).
- **Draw calls = el killer silencioso**: merge de geometrías con mismo material (BufferGeometry), `InstancedMesh` para obstáculos repetidos, texture atlas ([Three.js Roadmap](https://threejsroadmap.com/blog/draw-calls-the-silent-killer)).
- **Low-poly + materiales baratos**: `MeshLambertMaterial`/`MeshBasicMaterial` sobre Standard donde se pueda; sombras off o baked; pool de objetos (reciclar obstáculos, no crear/destruir) ([Codrops](https://tympanus.net/codrops/2025/02/11/building-efficient-three-js-scenes-optimize-performance-while-maintaining-quality/)).
