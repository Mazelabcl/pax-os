# Personajes Pax — cast canónico

Fichas + portraits del cast. El archivo `_canon.md` consolida toda la información canónica; los `.md` individuales son fichas por personaje.

## Tabla del cast

### Clan core (7 protagonistas de la webserie 12×3 min)

| Personaje | Status   | Ficha (.md)         | Portrait (.png) | Rol                              |
|-----------|----------|---------------------|-----------------|----------------------------------|
| Jiggy     | canon    | `jiggy.md`          | `jiggy.png`     | Chasqui irreverente, detonante   |
| Wiz       | canon    | `wiz.md`            | `wiz.png`       | Sabio custodio, mentor           |
| Byte      | canon    | `byte.md`           | `byte.png`      | Sabio tecnológico, descifrador   |
| KZ        | canon    | `kz.md`             | `kz.png`        | Torpe-genio, corazón del grupo   |
| Onyx      | canon    | `onyx.md`           | `onyx.png`      | Motor físico, lealtad pura       |
| Agatha    | canon    | `agatha.md`         | `agatha.png`    | Ancla emocional, brújula         |
| Luxa      | canon    | `luxa.md`           | _falta_         | Exploradora cómica, alegría      |

### Secundarios recurrentes

| Personaje | Status   | Ficha (.md)         | Portrait (.png) | Rol                              |
|-----------|----------|---------------------|-----------------|----------------------------------|
| Zek       | canon    | `zek.md`            | _falta_         | Ritmo del clan, boombox          |
| Mariela   | canon    | `mariela.md`        | _falta_         | Humana, protagonista piloto      |

### Clan extendido (nuevos — fichas creadas 2026-05-22)

| Personaje | Status   | Ficha (.md)         | Portrait (.png) | Rol                                          |
|-----------|----------|---------------------|-----------------|----------------------------------------------|
| Fortis    | canon    | `fortis.md`         | `fortis.png`    | Protector del clan, fuerza moral             |
| Kif       | canon    | `kif.md`            | `kif.png`       | Sabio del umbral, segundo sabio              |
| Luz       | canon    | `luz.md`            | `luz.png`       | Mejor amiga de Jiggy, portadora violeta      |
| Alma      | canon    | `alma.md`           | `alma.png`      | Tejedora de cristales, memoria del anuraK    |
| Aura      | canon    | `aura.md`           | `aura.png`      | Vidente del clan, lectora de energías        |
| Baba      | canon    | `baba.md`           | `baba.png`      | Cría del clan, anuraK puro                   |
| Brizk     | canon    | `brizk.md`          | `brizk.png`     | Explorador-investigador, coleccionista campo |
| Cyfer     | canon    | `cyfer.md`          | `cyfer.png`     | Descifrador histórico, lector cristales      |
| Iris      | canon    | `iris.md`           | `iris.png`      | Curandera del clan, lectora de lo roto       |
| Ludus     | canon    | `ludus.md`          | `ludus.png`     | Narrador del clan, memoria oral              |

**Nota sobre PNGs del clan extendido:** los 10 PNGs correspondientes aún están en `_nuevos-pendientes-md/`. Mover con el comando de la sección "Pendientes operativos" abajo.

## Diferenciaciones clave (anti-duplicación)

- **Wiz vs Kif:** Wiz custodia los cristales y lee la energía. Kif custodia las preguntas que el lore oficial no respondió. Wiz tiene el mapa; Kif tiene el territorio sin mapear.
- **Onyx vs Fortis:** Onyx empuja hacia adelante (motor físico, impulso). Fortis absorbe lo que viene de frente (escudo moral). Uno abre; el otro aguanta.
- **Byte vs Cyfer:** Byte descifra sistemas y mecanismos actuales. Cyfer descifra registros históricos en cristales con memoria. Byte trabaja el presente; Cyfer trabaja el pasado.
- **Byte vs Brizk:** Byte trabaja patrones desde el interior del Uray Pacha. Brizk trabaja datos de campo en la superficie. Brizk provee; Byte procesa.
- **Luxa vs Luz:** Luxa es exploradora cómica, cristal dorado, paleta cálida. Luz es mejor amiga de Jiggy, cristal violeta, vínculo afectivo central con el protagonista.
- **Agatha vs Alma:** Agatha ancla el propósito colectivo del clan. Alma ancla la resonancia con los cristales. Agatha cuida el porqué; Alma cuida la conexión energética.
- **Agatha vs Iris:** Agatha sostiene el propósito colectivo. Iris cuida el estado individual de cada miembro. Agatha es el para qué; Iris es el cómo estás.
- **KZ vs Baba:** KZ es torpe-genio adolescente, mejor amigo de Jiggy. Baba es cría del clan, torpeza genuina de infancia. KZ tropezar esconde genialidad; Baba tropezar es simplemente aprender.
- **Luxa vs Ludus:** los dos generan anuraK indirecto (risas, historias). Luxa lo hace en tiempo real con humor de timing. Ludus lo hace convirtiendo los Aynis pasados en memoria activa del clan.

## Pendientes operativos

### Mover PNGs del clan extendido

Ejecutar en PowerShell desde la raíz del repo:

```powershell
$src = "_lore\personajes\_nuevos-pendientes-md"
$dst = "_lore\personajes"
foreach ($f in Get-ChildItem "$src\*.png") {
    Move-Item $f.FullName "$dst\$($f.Name)"
}
Remove-Item "$src\README.md"
Remove-Item $src
```

### Portraits faltantes en cast existente

- `luxa.png` — pendiente de generar
- `zek.png` — _falta_ (según estado anterior del índice)
- `mariela.png` — pendiente de generar

## Auxiliares

- `_canon.md` — Canon visual consolidado del cast completo (char sheets detallados).
- `mariela-prompt.md` — Prompt auxiliar para generación visual de Mariela.
