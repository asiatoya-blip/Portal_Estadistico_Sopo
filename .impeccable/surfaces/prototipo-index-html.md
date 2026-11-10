---
version: 1
slug: "prototipo-index-html"
primary_target: "prototipo/index.html"
related_targets: []
---

# Surface brief — Portal Estadístico de Sopó (v2, tablero de producto)

Scope: `prototipo/index.html`. Mode: Operate. Reemplaza la v1 "Temas que juntan cifra y tablero" (rechazada por el
usuario el 2026-11-10: tableros ocultos tras botón, chrome GOV.CO simulado, diseño soso).
Audiencia: ciudadanía y funcionarios. Preguntas que responde: ¿cómo va Sopó?, ¿qué cambió?, ¿dónde exploro el detalle?
Restricciones: barra superior y pie GOV.CO reales del CDN; tableros de Tableau visibles sin clic (iframe directo);
Programas Sociales oculto; resumen en texto junto a cada tablero; WCAG 2.1 AA.

## Direction contract

THESIS: Un tablero de producto, como la banca y la salud digitales: shell con navegación lateral de temas, un resumen que responde "¿cómo va Sopó?" con estados (mejora / empeora / estable) y los libros de Tableau visibles y grandes. Rechaza la página-documento con tableros escondidos.
OWN-WORLD: Fondo gris azulado #EEF2F8; riel lateral marino #0A1A3F con texto claro y el tema activo en Cobalt #0943B5; tarjetas blancas con radio 16px y sombra suave; estados con chip (verde #1B6B3A mejora, rojo #A5361A empeora, gris estable); amarillo #FDBF2D solo para la fecha de corte y el foco; Work Sans en cifras y títulos, Nunito Sans en texto; mini tendencias SVG de TerriData en cada tarjeta.
STORY: Llega y ve en una línea cuántos indicadores mejoraron y cuántos empeoraron; lee las 6 cifras con su tendencia; ve el tablero destacado ya cargado; elige un tema en el riel y el tablero de ese tema ocupa el área principal.
FIRST VIEWPORT: Barra GOV.CO real; riel lateral izquierdo (≈260px) con marca del portal y temas agrupados por libro; área principal: título "¿Cómo va Sopó?" + fecha de corte + franja de estado; fila de 6 tarjetas con valor, chip de estado y mini tendencia; debajo, tablero destacado (Demografía) cargado a la izquierda y columna derecha "¿Sabías que…?".
FORM: Tablero con shell lateral inspirado en Mercury, Monarch, Copilot Money, Perplexity Health y Mixpanel (referentes Mobbin 2026-11-10). seed: none (pinned) — "dashboard … banking, medical care … que muestren gráficas y tengan una excelente arquitectura de contenido" (usuario, 2026-11-10).
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
