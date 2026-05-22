# Research — Oracle Pax: Sistemas Ancestrales + APIs

_Fecha: 2026-05-20 | Agente: pax-mystic-researcher | Queries: 9 (Perplexity search/reason)_

---

## Bloque 1 — Astrologia occidental: sistema natal completo

### Datos minimos para calcular una carta

Tres datos son obligatorios: **fecha de nacimiento** (dia/mes/ano), **hora exacta de nacimiento**, y **lugar de nacimiento** (ciudad/pais, para derivar coordenadas y zona horaria). La hora es critica porque determina el Ascendente y la Luna — ambos cambian de signo en horas.

### Los cuatro puntos angulares

- **Sol (Sun sign)**: posicion zodiacal del Sol en la fecha de nacimiento. Identidad consciente central.
- **Luna (Moon sign)**: signo donde estaba la Luna en el momento exacto. Patrones emocionales; muy sensible a la hora.
- **Ascendente (Rising / ASC)**: signo que estaba saliendo por el horizonte este en el momento del nacimiento. Define el cusp de la Casa 1. Representa la "mascara" publica y el punto de partida del sistema de casas.
- **Medio Cielo (Midheaven / MC)**: punto donde la ecliptica cruza el meridiano local. Cusp de la Casa 10. Asociado a vocacion, carrera y rol publico.

### Las 12 casas

| Casa | Dominio |
|------|---------|
| 1 | Identidad, cuerpo, primera impresion |
| 2 | Recursos, dinero, valores propios |
| 3 | Comunicacion, hermanos, pensamiento cotidiano |
| 4 | Hogar, familia, raices, vida privada |
| 5 | Creatividad, placer, hijos, romance |
| 6 | Salud, servicio, trabajo rutinario |
| 7 | Relaciones uno a uno, asociaciones, enemigos |
| 8 | Transformacion, muerte/renacimiento, recursos compartidos |
| 9 | Filosofia, viajes largos, religion, educacion superior |
| 10 | Carrera, reputacion, vocacion publica |
| 11 | Comunidad, amigos, ideales colectivos |
| 12 | Inconsciente, retiro, sacrificio, instituciones |

Sistemas de casas mas usados: **Placidus** (default en la mayoria de sitios), **Whole Sign** (mas simple; todo el signo = una casa).

### Los 10 planetas y su rol estructural

Sol, Luna, Mercurio, Venus, Marte, Jupiter, Saturno, Urano, Neptuno, Pluton. Cada planeta = "actor". Cada signo donde cae = "estilo de actuacion". Cada casa = "escenario".

### Los 5 aspectos principales

| Aspecto | Angulo | Orbe tipico | Naturaleza |
|---------|--------|-------------|-----------|
| Conjuncion | 0° | 8-10° | Fusion, intensidad |
| Sextil | 60° | 4-6° | Fluidez, oportunidad |
| Cuadratura | 90° | 6-8° | Tension, friccion, crecimiento |
| Trigono | 120° | 6-8° | Facilidad, flujo natural |
| Oposicion | 180° | 6-8° | Tension polarizada, conciencia |

### Como se calcula en la practica moderna

1. Input: fecha + hora + lugar
2. Herramienta (Astro.com, API) calcula Local Sidereal Time
3. Deriva MC y Ascendente con formulas trigonometricas (oblicuidad, latitud, RAMC)
4. Tablas de casas dan los 12 cusps
5. Efemerides ubican planetas en grados zodiacales
6. Calculo de aspectos = diferencia absoluta entre longitudes, filtrado por orbe

**Como Pax podria usar esto:** El sistema de casas es el andamiaje ideal para el Oraculo — "la Casa 12 de Jiggy esta activa" tiene peso narrativo sin requerir que el usuario entienda astrologia. Cada casa mapea a un dominio de vida que se puede reinterpretar en lenguaje Pax (ej. Casa 6 = "el arte del servicio cotidiano en el clan").

**Fuente:** Perplexity sonar-pro-search, citas [1][2][4][5][6][7][8][9][10] — metodologia Astro.com y libros clasicos de calculo manual.

---

## Bloque 2 — Carta maya / Tzolkin

### Que es el Tzolkin

El Tzolkin (Chol Q'ij en quiche) es el calendario sagrado maya de 260 dias. Es el cruce de dos ciclos: 20 signos del dia (nahuales / Sellos Solares) y 13 tonos. Porque 20 y 13 son coprimos, las 260 combinaciones unicas no se repiten hasta completar el ciclo completo.

### Los 20 sellos / nahuales

Cada nahual tiene nombre, elemento y arquetipo de conciencia (ej. Imix = dragon/comienzo, Ik' = viento/espiritu, Lamat = estrella/armonia, Ahau = sol/iluminacion). No son constelaciones — son "energias de dia sagradas".

### Los 13 tonos

Cada tono describe *como se expresa* la energia del sello: tono 1 (magnetico, iniciar), tono 2 (lunar, polarizar), tono 7 (resonante, punto medio), tono 13 (cosmico, trascender). Es una capa de modulacion sobre el arquetipo del sello.

### Como se calcula el kin personal

1. Fecha de nacimiento → numero de dias Juliano (JDN)
2. Constante de correlacion GMT (584283) alinea Long Count maya con JDN
3. Diferencia modulo 260 = numero de kin (1-260)
4. Del kin: tono = kin mod 13; sello = kin mod 20 (mapeado a secuencia de 20 glifos)

**Resultado:** "Kin 71 — Mono Electrico Azul" o "5 Ben / 5 Cana". El mismo kin se repite cada 260 dias, no cada ano.

### Diferencias clave con astrologia occidental

| Aspecto | Occidental | Tzolkin |
|---------|-----------|---------|
| Base temporal | Ano solar 365 dias | Ciclo sagrado 260 dias |
| Referencia | Cielo / constelaciones | Calendario sagrado |
| Personalidad | Multivariable (sol+luna+ASC+...) | Binario limpio: sello + tono |
| Uso tradicional | Prediccion psicologica | Ceremonia, nombres, timing ritual |
| Requiere hora de nacimiento | Si (para luna/ASC) | No (solo fecha) |

### Por que potencia el Oraculo Pax

El Tzolkin es el **sistema mas simple de implementar** (solo fecha de nacimiento, no hora ni lugar) y devuelve un arquetipo limpio y binario (sello + tono = 260 combinaciones). Es mas "mistico" y menos conocido que el horoscopo occidental, lo que lo hace ideal como "capa Pax" que siente original. El Smithsonian tiene conversor publico (Living Maya Time).

**Como Pax podria usar esto:** El nahual = identidad profunda del personaje/visitante en el universo Pax. El tono = como esa identidad "se mueve" o "sirve". Es la columna vertebral mas clara del oraculo — ver insight principal al final.

**Fuente:** Perplexity sonar-pro-search, citas [1][5][6][7][8][10] — Smithsonian Living Maya Time, literatura academica Tzolkin.

---

## Bloque 3 — Tarot Rider-Waite

### Estructura del maso

78 cartas totales:
- **22 Arcanos Mayores** (0 El Loco — 21 El Mundo): temas arquetipicos grandes, momentos de umbral psicologico.
- **56 Arcanos Menores**: 4 palos de 14 cartas c/u (As-10 + 4 figuras: Paje, Caballero, Reina, Rey).

Los 4 palos y sus dominios:
| Palo | Elemento | Dominio |
|------|---------|---------|
| Bastos (Wands) | Fuego | Voluntad, proyectos, creatividad |
| Copas (Cups) | Agua | Emociones, relaciones, intuicion |
| Espadas (Swords) | Aire | Intelecto, conflicto, decisiones |
| Oros/Pentaculos | Tierra | Materia, trabajo, seguridad |

### Tiraje de 3 cartas

**Layout clasico:** Pasado — Presente — Futuro. Variante Jungiana: Actitud consciente — Contenido en sombra — Integracion/individuacion.

Regla de lectura: Arcano Mayor en cualquier posicion = fuerza arquetipica profunda activa. Arcano Menor = como se manifiesta en lo cotidiano.

### Conexion con arquetipos jungianos

Mapeos establecidos: El Emperador = arquetipo del Padre; La Emperatriz = Madre; El Diablo = Sombra; El Mundo = Self/Totalidad; El Loco = Puer Aeternus (nino eterno). Los Arcanos Mayores forman una especie de "viaje de individuacion" de 0 a 21.

**Como Pax podria usar esto:** Tiraje de 3 cartas como "lectura rapida" en el Oraculo — situacion actual del visitante segun su arquetipo Pax. Las cartas se re-ilustrarian con iconografia Pax (ej. La Sacerdotisa = el Cristal Memoria; El Loco = el corredor-mensajero; El Mundo = el anuraK completo).

**Fuente:** Perplexity sonar-pro-search, citas [1][2][4][6][7][8][9][10].

---

## Bloque 4 — I Ching, Numerologia, Runas

### I Ching

Sistema oraculo chino de 64 hexagramas. Cada hexagrama = 6 lineas (yin quebrada / yang solida), dando 2^6 = 64 patrones que mapean "todos los estados posibles del cambio".

**Metodo clasico moderno (3 monedas):** 6 tiradas de 3 monedas. Cara=3, Cruz=2. Suma 6/7/8/9:
- 7 = yang estable
- 8 = yin estable
- 9 = yang cambiante (pasa a yin en hexagrama resultado)
- 6 = yin cambiante (pasa a yang)

Las lineas cambiantes generan un segundo hexagrama = "hacia donde se mueve la situacion".

Lectura: Hexagrama primario (juicio + imagen) + lineas cambiantes especificas + hexagrama resultado.

**Como Pax podria usar esto:** El modelo "estado presente + linea de cambio + estado futuro" es perfecto para lecturas de coyuntura ("Pax dice: estas en Hexagrama 29 — El Abismo. Aqui esta tu linea de cambio.").

**Fuente:** Perplexity sonar-pro-search, citas [3][4][5][7][8][9][10].

---

### Numerologia

Sistema **pitagorico** (mas comun en occidente): letras A-Z = valores 1-9 ciclicamente.

**Calculo del Numero de Vida (Life Path):**
- Suma todos los digitos de la fecha de nacimiento (DD+MM+AAAA)
- Reduce a un digito (si suma >9, suma sus digitos de nuevo)
- Excepcion: 11, 22, 33 son "Numeros Maestros", no se reducen

**Calculo de numeros del nombre:**
- Expresion: todos los valores de letras del nombre completo → reduce
- Impulso del Alma: solo vocales
- Numero de Personalidad: solo consonantes

**Arquetipos por numero de vida (1-9):**
1=Lider/iniciador, 2=Diplomático/mediador, 3=Creativo/expresivo, 4=Constructor/practico, 5=Explorador/libre, 6=Cuidador/responsable, 7=Buscador/analitico-espiritual, 8=Ambicioso/manifestador, 9=Humanitario/idealista.

**Como Pax podria usar esto:** Numero de Vida como capa adicional de perfil (especialmente el 6 y el 9 resuenan con el universo de servicio de Pax). Facil de calcular solo con fecha.

---

### Runas Elder Futhark

24 simbolos germanicos arcaicos, organizados en 3 grupos de 8 (aettir). Cada runa = sonido + nombre + campo semantico. Uso divinatorio moderno: se extraen runas de una bolsa y se interpretan por posicion + significado.

Las 24 y sus temas centrales (seleccion relevante para universo Pax):

| Runa | Tema central |
|------|-------------|
| Ansuz (A) | Comunicacion, mensaje divino, inspiracion |
| Raidho (R) | Viaje, movimiento, alinearse con el camino |
| Kenaz (K) | Luz/antorcha, aprendizaje, iluminacion |
| Gebo (G) | Don, reciprocidad, Ayni |
| Wunjo (W) | Alegria, armonia, pertenencia al clan |
| Eihwaz | Eje entre mundos, resistencia, yew |
| Algiz | Proteccion, guardia espiritual |
| Tiwaz (T) | Justicia, sacrificio por causa mayor |
| Berkana (B) | Crecimiento, sanacion, hogar |
| Laguz (L) | Intuicion, emociones, fluir |
| Dagaz (D) | Amanecer, cambio irreversible, avance |
| Othala (O) | Herencia ancestral, pertenencia, legado |

**Nota cultural:** Las runas son protocolo germanico-nordico, no andino. Para Pax, su uso debe ser metaforico y filtrado — no copiar literalmente. El patron estructural (simbolo + sombra) si es util como framework.

**Como Pax podria usar esto:** Gebo (reciprocidad/Ayni) y Wunjo (alegria colectiva) son las runas que mas resuenan con el lore Pax. Podrian inspirar simbolos visuales propios del universo sin apropiacion directa.

---

## Bloque 5 — Arquetipos jungianos del servicio (CRITICO)

Ocho arquetipos centrados en ayudar/servir. Para cada uno: caracteristicas, sombra, manifestacion concreta, correlacion astrologica.

### 1. Cuidador (Caregiver)
- **Esencia:** Nutre, protege, sostiene. Motivado por cuidar y apoyar.
- **Sombra:** Martirio, codependencia, control via culpa ("despues de todo lo que hice por ti").
- **Accion concreta:** Cuidado de enfermos, recordar cumpleanos, cocinar para otros, quedarse en relaciones por "ellos me necesitan".
- **Astrologico:** Cancer (casa 4), Virgo (casa 6), Piscis (casa 12); planetas Luna, Ceres, Neptuno.

### 2. Sanador (Healer)
- **Esencia:** Restaura la integridad — fisica, emocional o espiritual. Percibe "donde duele".
- **Sombra:** Complejo del Sanador Herido (overidentificacion con ser necesitado por trauma propio), complejo mesias, burnout, sanacion no solicitada.
- **Accion concreta:** Terapia, medicina, espacios de retiro, mediacion de conflictos, "siempre arreglando situaciones".
- **Astrologico:** Virgo/Piscis (eje salud-sacrificio), Escorpion (transformacion profunda); Chiron (clave), Neptuno, Pluton; casas 6, 8, 12.

### 3. Sabio (Sage)
- **Esencia:** Busca verdad para beneficiar a otros. Ilumina el camino intelectual o espiritualmente.
- **Sombra:** Intelectualismo frio, arrogancia epistemica, parálisis analitica, usar el conocimiento como escudo emocional.
- **Accion concreta:** Ensenanza, investigacion, escritura, cuestionamiento de supuestos, "voz de razon" en crisis.
- **Astrologico:** Sagitario (casa 9), Acuario (casa 11), Virgo; Jupiter, Mercurio, Urano; casas 3, 9, 11.

### 4. Heroe altruista (Hero)
- **Esencia:** Actua con coraje *en nombre de otros*. Protector, defensor, primero en responder.
- **Sombra:** Complejo de salvador (necesita enemigos para sentir valor), soberbia ("solo yo puedo"), burnout heroico, convertir a otros en victimas pasivas.
- **Accion concreta:** Servicios de emergencia, activismo, proteger vulnerables, ser "el fuerte" de la familia.
- **Astrologico:** Aries (casa 1), Leo, Sagitario; Marte, Sol, Jupiter; casas 1, 9, 10.

### 5. Santo / Mistico (Saint / Mystic)
- **Esencia:** Orientado a lo trascendente. Compasion, devocion, rendicion al servicio del alma colectiva.
- **Sombra:** Escapismo espiritual (spiritual bypassing), auto-negligencia, superioridad espiritual, falta de limites ("el amor exige sacrificio").
- **Accion concreta:** Vida contemplatia, caridad silenciosa, trabajo con olvidados (prisiones, hospicios), crear rituales o arte que conecta con lo sagrado.
- **Astrologico:** Piscis (casa 12), Escorpion (casa 8), Cancer; Neptuno, Luna, Jupiter; casas 8, 9, 12.

### 6. Mentor / Maestro (Mentor / Teacher)
- **Esencia:** Guia el desarrollo de otros. Paciente, ve el potencial, invierte en la autonomia ajena.
- **Sombra:** Paternalismo, crear dependencia, proyectar potencial no vivido en el alumno, burnout por sobreinvolucramiento.
- **Accion concreta:** Ensenanza, coaching, supervision, retroalimentacion estructurada, mentoria informal.
- **Astrologico:** Sagitario (casa 9), Geminis (casa 3), Virgo; Jupiter ("el guru"), Mercurio; casas 3, 9, 11.

### 7. Lider Servidor (Servant Leader)
- **Esencia:** Lidera sirviendo. Prioriza el crecimiento de quienes guia sobre su propio ego.
- **Sombra:** Hiper-responsabilidad, dificultad para delegar, resentimiento callado cuando el servicio se da por sentado.
- **Accion concreta:** Liderazgo colaborativo, abogar por el equipo, dar credito, tomar responsabilidad por errores colectivos.
- **Astrologico:** Virgo (casa 6), Cancer (casa 4), Capricornio (casa 10), Acuario; Sol, Saturno, Luna; casas 6, 10, 11.

### 8. Ayudante / Companero (Helper / Companion)
- **Esencia:** Acompana con presencia y solidaridad — no "arregla", camina al lado.
- **Sombra:** Auto-borramiento, miedo al abandono, ayudar para evitar conflicto o ganar aprobacion, evitar los propios problemas enfocandose en los de otros.
- **Accion concreta:** El amigo que aparece en las crisis, apoyo entre pares, acompanamiento en duelo o transicion, rol armonizador en equipos.
- **Astrologico:** Libra (casa 7), Cancer, Tauro; Venus, Luna; casas 4, 7, 11.

**Como Pax podria usar esto:** Cada visitante del Oraculo recibe un "arquetipo de servicio" como parte central de su lectura. El arquitecto de lore puede mapear los 8 arquetipos a roles del universe Pax (ej. Sanador = los que custodian cristales memoria; Corredor-Mensajero = Heroe altruista; Cuidador = las tribus que guardan el Ayni). La sombra de cada arquetipo es el vector de conflicto narrativo mas rico.

**Fuente:** Perplexity sonar-reasoning-pro — literatura jungiana, astrologia psicologica.

---

## Bloque 6 — APIs publicas para carta natal

### Ranking recomendado para MVP

#### 1. Free Astrology API — freeastrologyapi.com
- **URL:** https://freeastrologyapi.com
- **Free tier:** 50 requests/dia, 1 req/seg — el mas generoso para MVP
- **Input:** fecha, hora, lat, lon, zona horaria
- **Output JSON:** posiciones planetarias, cusps de casas (12), aspectos; opcion de SVG del mapa
- **Western + Vedic:** si (Vedic puede ser bonus para lecturas adicionales)
- **Tiers pagos:** Mercury $15/mes (50k req), Venus $40/mes (200k req)
- **Recomendacion:** Primera opcion para prototipo. 50 req/dia es suficiente para beta privado.

#### 2. AstrologyAPI.com (Vedicrishi) — json.astrologyapi.com
- **URL:** https://json.astrologyapi.com
- **Endpoints clave:**
  - `POST /v1/western_chart_data` → planetas + casas + aspectos
  - `POST /v1/natal_chart_interpretation` → datos + texto de interpretacion en JSON
- **Input:** `day, month, year, hour, min, lat, lon, tzone, house_type`
- **Output:** array de planetas (nombre, grado, signo, casa, retrogrado), array de casas (cusp de cada una), lista de aspectos
- **Free tier:** trial limitado + bundles pagos — menos generoso que el anterior pero mas documentado
- **Ventaja:** devuelve texto de interpretacion listo, util si el oraculo necesita fallback de texto

#### 3. AstroAPI / astrology-api.io
- **URL:** https://astrology-api.io (o astroapi.com segun branding actual)
- **Diseno:** especificamente para integraciones AI/programaticas
- **Input:** fecha, hora, lat/lon, tz, sistema de casas, zodiaco (tropical/sideral)
- **Output:** JSON limpio con planetas, casas, aspectos — disenado para bajo overhead
- **Free tier:** entrada dev-friendly con facturacion por request
- **Recomendacion:** segunda opcion si freeastrologyapi.com no cubre las necesidades de formato

#### APIs descartadas para MVP
- **Prokerala:** orientado a Vedico. Util si se quiere dimension adicional, no prioritario.
- **AstroAPI Bloom.be:** mas B2B, documentacion limitada para libre acceso.
- **Astro-Seek:** solo UI web, no tiene endpoint JSON publico estable.
- **Vedicrishi directo:** es la misma infraestructura que AstrologyAPI.com.

### Ejemplo minimo de request (freeastrologyapi.com)

```json
POST https://api.freeastrologyapi.com/v1/western/natal
Headers: { "x-api-key": "TU_KEY" }
Body: {
  "year": 1990,
  "month": 3,
  "date": 15,
  "hours": 14,
  "minutes": 30,
  "latitude": -33.4,
  "longitude": -70.6,
  "timezone": -4,
  "config": { "house_system": "placidus" }
}
```

**Como Pax podria usar esto:** El MVP del Oraculo llama a la API con los datos del visitante, recibe el JSON de planetas/casas/aspectos, y los mapea a arquetipos Pax. El modelo LLM (o tabla de reglas) hace la reinterpretacion. Costo inicial: $0 (50 req/dia gratuitos).

**Fuente:** Perplexity sonar-pro-search, citas [1][3][4][5][6][8][9][10].

---

## Bloque 7 — Best practices: contenido espiritual/oraculo 2026

### Que diferencia un oraculo profundo de uno superficial

**Profundo:**
- Especifico y contextual: "Puedes sentirte impulsado a retirarte cuando las conversaciones se intensifican emocionalmente" > "Puedes sentirte emocional hoy"
- Descriptivo, no prescriptivo: describe estados internos y posibles reacciones, pregunta que resuena
- Transparente: explica *por que* dice lo que dice (que patron, arquetipo o carta lo genero)
- Orientado a la agencia: cada insight termina con un experimento o pregunta, no con un mandato

**Superficial (evitar):**
- Afirmaciones genericas que aplican a cualquiera ("Grandes cambios vienen pronto")
- Predicciones absolutistas que eliminan la agencia ("Perderás esta relacion")
- Contenido reciclado que no construye sobre lo que el usuario ya vio
- Urgencia falsa, miedo o monetizacion agresiva interrumpiendo el espacio de lectura

### Los tres casos de referencia

**Co-Star:** voz afilada, minimal, provocadora. Datos "NASA" dan credibilidad. Riesgo: puede sentirse fatidico o desempoderador.

**The Pattern:** tono terapeutico-intimo, perfil profundo de "patrones de vida", continuidad narrativa a traves del tiempo. Punto debil: modelo freemium agresivo que fractura la experiencia.

**Sanctuary:** conversacional, equilibra mistico con pedagogico, chats con astrologos humanos. Lo que lo hace profundo: *hay una persona real detras*.

### Principios de tono para Oraculo Pax

1. **Calido pero no vago:** solemne sin ser opresivo. Voz de guia-companion, no de oraculo que dictamina.
2. **Normalizar la ambivalencia:** reconocer que el visitante puede dudar, que la lectura puede no resonar del todo.
3. **Formato por capas:** titular del insight → parrafo corto → opcional: profundizacion / pregunta de reflexion.
4. **Agencia activa:** cada lectura termina con 1-3 experimentos posibles que el visitante puede *elegir* hacer.
5. **Sin prediccion de outcomes negativos:** el Oraculo Pax no dice "tus relaciones estaran mal". Dice "este es un momento para revisar como das y recibes".

### Mecanicas que crean profundidad (UX)

- Permitir que el visitante marque "resuena / no resuena" → retroalimentacion para mejorar el perfil
- Preguntas de reflexion adjuntas a cada insight
- "Vista de patrones": mostrar como lecturas anteriores conectan
- Jornadas tematicas de varias semanas ("Trabajar con el Cuidador en ti")

**Ejemplo de reescritura:**

- Superficial: "Ten cuidado con las relaciones esta semana"
- Profundo Pax: "Estas en un momento donde tus formas habituales de relacionarte pueden sentirse ajustadas. Nota donde sientes inquietud con alguien cercano — y experimenta hoy diciendole una verdad pequena pero honesta"

**Como Pax podria usar esto:** El tono del Oraculo es de "companion del clan Pax" — conoce al visitante, camina con el, no le dictamina. La metafora del cristal-memoria de Pax encaja perfectamente: "tu cristal muestra este patron" en lugar de "el universo dice".

**Fuente:** Perplexity sonar-pro-search, citas [1][3][5][6][8][9][10] — Co-Star, The Pattern, Sanctuary.

---

## Conexiones cruzadas

- **Gebo (runa) = Ayni (quechua) = reciprocidad sagrada:** tres sistemas independientes convergen en el mismo principio. El Oraculo Pax puede hacer de este patron su eje — "tu lectura revela como das y recibes en el Ayni de tu vida".
- **Casa 12 occidental + Piscis + Santo/Mistico + Eihwaz (runa):** cuatro tradiciones apuntan al mismo arquetipo — el servicio invisible, el sacrificio, el trabajo detras de escena. Muy relevante para el universo Pax donde los personajes pequeños sostienen el mundo en silencio.
- **Luna (astrologia) + Tono 1 Magnetico (Tzolkin) + Caregiver archetype:** los tres senalan el mismo perfil — quien atrae, sostiene y nutre sin reclamar poder.
- **Heroe altruista (Jung) + Tiwaz (runa) + Casa 1/10 (astrologia) + Kin Serpiente (Tzolkin):** cuatro capas que definen al corredor-mensajero de Pax.
- **The Pattern (app) + I Ching:** ambos usan el mismo principio de "dos hexagramas" — estado presente + vector de cambio. El Oraculo Pax podria tener una "lectura de movimiento" con esa estructura sin mencionar el I Ching.

---

## Lo que NO encontre

- Documentacion publica estable de un endpoint JSON para **Astro-Seek** — solo UI web.
- Precios actualizados 2026 de **AstroAPI.com (Bloom.be)** — sus terminos de free tier no estan claros publicamente.
- Calculo del kin Tzolkin via API REST publica y documentada — los conversores existentes son web UI (Living Maya Time de Smithsonian). El calculo es matematicamente simple y puede implementarse en JS directamente (modulo 260 sobre JDN menos constante GMT 584283).
- Literatura jungiana especifica sobre el arquetipo "Mensajero" como categoria separada del Heroe — en Jung el mensajero cae bajo Hermes/Mercurio como arquetipo del Trickster o del Psicopompo, no exactamente "servicio altruista".

---

## Queries ejecutadas (audit trail)

1. `search` — "western astrology natal chart complete system: sun sign moon sign ascendant rising midheaven 12 houses planets aspects conjunction square trine how to calculate"
2. `search` — "Tzolkin Maya calendar 260 days 20 seals nahuales 13 tones how to calculate personal kin from birth date differences from western astrology"
3. `search` — "Tarot Rider-Waite structure 22 major arcana 56 minor arcana four suits cups wands swords pentacles 3-card spread Jungian archetypes"
4. `search` — "I Ching 64 hexagrams divination Chinese oracle system how it works three coin method meaning"
5. `search` — "numerology life path number calculation name number pythagorean numerology personality profile"
6. `search` — "Elder Futhark runes 24 symbols divination meanings Nordic Germanic origins"
7. `reason` — "Jungian archetypes of service and altruism: Caregiver, Healer, Sage, Hero, Saint/Mystic, Mentor/Teacher, Servant Leader, Helper/Companion. For each: core characteristics, shadow/weakness, how it manifests in concrete action, which astrological signs/planets/houses are associated with it."
8. `search` — "public API astrology natal chart calculation JSON endpoint: AstroAPI, Prokerala, free-astrology-api, astro-seek API, vedicrishi API, astrologyAPI.com - free tier input output JSON planets houses aspects 2024 2025"
9. `search` — "best practices digital oracle spiritual app 2024 2025: Co-Star The Pattern Sanctuary tone voice what makes oracle app feel deep not shallow avoid vague predictions user agency empowerment"

_Total: 9 queries. Modelos: 8x sonar-pro-search, 1x sonar-reasoning-pro._
