# app-disabled-routes — rutas legacy de la webapp

8 rutas legacy de la webapp Pax que fueron deshabilitadas renombrandolas con prefijo `_` (convencion de Next.js App Router para ignorar carpetas).

## Contenido

| Carpeta archivada                | Ruta original que servia       |
|---------------------------------- |--------------------------------|
| `_cambios/`                       | `/cambios`                     |
| `_episodio-1/`                    | `/episodio-1`                  |
| `_episodios/`                     | `/episodios/[id]`              |
| `_estilo/`                        | `/estilo`                      |
| `_lore/`                          | `/lore`                        |
| `_personajes/`                    | `/personajes` y `/personajes/[slug]` |
| `_principles/`                    | `/principles`                  |
| `_roadmap/`                       | `/roadmap`                     |

## Razon del archivado

La webapp actual sirve solo `/oraculo`, `/docs` y home (`/`). Estas rutas pertenecian a la fase v2 antigua del sitio (catalogo de personajes, lore navegable, roadmap publico, etc.) y se descartaron al pivotear el scope hacia el Oraculo + docs internas.

Los archivos quedan aqui por si conviene rescatar codigo (componentes, estilos, patrones de fetch de markdown).

## Como reactivar una ruta

```bash
# Ejemplo: reactivar /lore
git mv _archive/app-disabled-routes/_lore app/lore
# (ojo: el directorio destino debe NO empezar con `_` para que Next lo sirva)
```

Luego verificar que las rutas internas y los `<Link>` apunten al path correcto.
