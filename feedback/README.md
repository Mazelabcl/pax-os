---
title: "Feedback / inputs visuales"
description: "Carpeta para screenshots y archivos que aldot deja para mostrarme algo."
---

# Feedback inputs

## Cómo usar

Cuando necesites mostrarme algo visual (error de Vercel, screenshot Obsidian, foto de referencia, etc.):

1. **Guarda el archivo en esta carpeta** con nombre descriptivo: `error-vercel-1.png`, `obsidian-graph.png`, `reference-jiggy-pose.jpeg`, etc.
2. **Mencionalo en el chat** ("dejé `error-vercel-3.png` en feedback").
3. Yo lo leo (multimodal) y respondo.

## Por qué no paste-image directo

Claude Code **NO recibe imágenes pegadas** en el chat — solo recibe paths a archivos. Por eso necesitas guardarlas primero.

**Workaround para tu OS:**
- **Windows:** `Win+Shift+S` para captura → automáticamente clipboard → pegar en cualquier app que acepte (Paint, mspaint) → guardar como PNG en `feedback/`. O usar [ShareX](https://getsharex.com) para guardar directo a una carpeta predefinida.
- **Alternativa rápida:** abrir esta carpeta en Explorer + arrastrar la captura ahí.

## Mantenimiento

- Esta carpeta **NO está en `.gitignore`** — los archivos quedan en el repo histórico (útil para debugging futuro).
- Si querés limpiar inputs viejos, los muevo yo a `archive/feedback-historico/` cuando me lo pidas.
- Los screenshots de errores resueltos pueden quedar acá como evidencia del proceso.

## Convención de naming sugerida

| Tipo | Ejemplo |
|---|---|
| Errores de plataforma | `error-{plataforma}-{N}.png` |
| Screenshots informativos | `{tema}-{descripcion}.png` |
| Refs visuales | `ref-{personaje-o-cosa}.{ext}` |
| Comparativas | `compare-{a}-vs-{b}.png` |
