---
version: 1
slug: "prototipo-index-html"
primary_target: "prototipo/index.html"
related_targets: []
---

# Surface brief — Portal Estadístico de Sopó (página única)

Scope: `prototipo/index.html` (propuesta publicable en GitHub Pages; luego se porta a Eleventy). Mode: Operate.
Audiencia: ciudadanía y funcionarios por igual. Tarea: encontrar la cifra de un tema y explorar su tablero de Tableau.
Restricciones: chrome GOV.CO intacto; CSP estricta (sin inline); iframes de Tableau solo tras clic, con aviso de tercero;
Programas Sociales oculto; cada hoja con resumen en texto fuera del iframe.

## Direction contract

THESIS: La barra de temas es el resumen de Sopó: cada tema trae su cifra, y al abrirlo la cifra y su tablero quedan lado a lado. Rechaza la franja de 6 tarjetas sueltas + secciones con mundos de color distintos.
OWN-WORLD: Kit GOV.CO 9.2 en modo restringido: fondo #F4F6FB, superficies blancas con borde #C3CFE5, Cobalt #0943B5 para acción y selección, Marino oscuro #0A1A3F para texto y la pestaña activa, amarillo #FDBF2D solo en la fecha de corte; rojo #A5361A solo para "desfavorable". Work Sans en títulos y cifras, Nunito Sans en texto.
STORY: El visitante ve en la barra las 8 cifras de Sopó, toca un tema, lee la cifra con su fuente y su resumen, y si quiere carga el tablero.
FIRST VIEWPORT: Chrome GOV.CO arriba; título "Portal Estadístico de Sopó" con fecha de corte a la derecha; debajo la barra de 8 temas, cada uno con nombre + cifra; panel del tema activo: columna izquierda (≈1/3) con cifra grande, variación con valoración, fuente y resumen; columna derecha con selector de hojas y el marco del tablero con botón "Cargar el tablero" como acción principal.
FORM: Temas que juntan cifra y tablero, posición 2 de mi lista ordenada; seed:93046ec3089052a6. Señal propia: la pestaña-cifra (cada tema muestra su número en la barra).
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Desviaciones citadas (revisión final 2026-11-10)

- Población sin valoración: el crecimiento de la población no es favorable ni desfavorable; solo se muestra la dirección.
- Verde #1B6B3A para "Favorable": verde de éxito del Kit; siempre va con texto e ícono, nunca solo color.
- Asistente IA: no hay enlace porque aún no existe (PRODUCT.md, principio 4). Datos abiertos enlaza a TerriData (DNP).
- Tipografía: Work Sans (OFL) alojada en `assets/fonts/` desde 2026-11-10; Nunito Sans en texto corrido.
