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

THESIS: Un tablero moderno y liviano, como Mercury, Wise o Monarch: navegación lateral clara, cifras con tendencia y los libros de Tableau como protagonistas, con pestañas para moverse entre hojas. Rechaza tanto la página-documento como el tablero oscuro y pesado.
OWN-WORLD: Fondo #F6F7F9, superficies blancas con borde fino #E6E9EF y radio 14px, sin sombras pesadas; texto #101828 y gris #5B6478; Cobalt #0943B5 solo para selección y acción, con su tinte #EEF3FD; estados suaves (verde #0F7A55, rojo #B42318); Work Sans en títulos y cifras, Nunito Sans en texto. Chrome GOV.CO real y barra de accesibilidad del CDN, todo centrado a 1440px.
STORY: Llega, ve "¿Cómo va Sopó?" con 6 cifras y su tendencia, ve el tablero destacado ya cargado, y navega por libro y hoja desde el menú lateral o las pestañas del tablero.
FIRST VIEWPORT: Barra GOV.CO; cabecera blanca con logo, nombre y fecha de corte; menú lateral claro (≈15rem) con Resumen y tres libros plegables; área principal con título, franja de estado, 6 tarjetas en 3 columnas y el inicio del tablero destacado.
FORM: Tablero moderno con shell lateral claro (referentes Mobbin: Mercury, Wise, Monarch, Copilot Money, Seline). seed: none (pinned) — "más simple, estético, minimalista … usa algo más modernista como un tablero moderno" (usuario, 2026-11-10).
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
