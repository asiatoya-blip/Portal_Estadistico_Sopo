---
name: Portal Estadístico de Sopó
description: Las cifras oficiales de Sopó, cada una junto a su tablero, dentro del Kit GOV.CO 9.2.
colors:
  cobalt: "#0943B5"
  cobalt-hover: "#07368F"
  ink: "#0A1A3F"
  ink-soft: "#33415C"
  ground: "#F4F6FB"
  surface: "#FFFFFF"
  tint: "#EAF0FB"
  line: "#C3CFE5"
  control: "#6F7D99"
  cut: "#FDBF2D"
  bad: "#A5361A"
  bad-tint: "#FBEAE5"
  good: "#1B6B3A"
  good-tint: "#E4F2E9"
typography:
  display:
    fontFamily: "Work Sans, Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(1.875rem, 1.4rem + 1.6vw, 2.75rem)"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  figure:
    fontFamily: "Work Sans, Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(2.5rem, 2rem + 1.6vw, 3.5rem)"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.02em"
    fontFeature: "tnum"
  headline:
    fontFamily: "Work Sans, Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "1.75rem"
    fontWeight: 800
    lineHeight: 1.15
  title:
    fontFamily: "Work Sans, Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "1.375rem"
    fontWeight: 700
    lineHeight: 1.3
  tab-figure:
    fontFamily: "Work Sans, Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "1.375rem"
    fontWeight: 700
    lineHeight: 1.15
    fontFeature: "tnum"
  button:
    fontFamily: "Work Sans, Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 600
    lineHeight: 1.3
  body:
    fontFamily: "Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  lead:
    fontFamily: "Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 700
    lineHeight: 1.6
  meta:
    fontFamily: "Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.6
rounded:
  md: "0.75rem"
  lg: "1rem"
  pill: "999px"
spacing:
  "1": "0.5rem"
  "2": "1rem"
  "3": "1.5rem"
  "4": "2rem"
  "5": "3rem"
  wrap: "80rem"
components:
  theme-tab:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "0.75rem 0.875rem"
  theme-tab-hover:
    backgroundColor: "{colors.tint}"
    textColor: "{colors.ink}"
  theme-tab-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface}"
  theme-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.4}"
  button-load:
    backgroundColor: "{colors.cobalt}"
    textColor: "{colors.surface}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "0.75rem 1.75rem"
    height: "3rem"
  button-load-hover:
    backgroundColor: "{colors.cobalt-hover}"
    textColor: "{colors.surface}"
  sheet-chip:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.cobalt}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "0.5rem 1rem"
    height: "2.75rem"
  sheet-chip-hover:
    backgroundColor: "{colors.tint}"
    textColor: "{colors.cobalt}"
  sheet-chip-selected:
    backgroundColor: "{colors.cobalt}"
    textColor: "{colors.surface}"
  cut-badge:
    backgroundColor: "{colors.cut}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "0.375rem 0.875rem"
  verdict-favorable:
    backgroundColor: "{colors.good-tint}"
    textColor: "{colors.good}"
    rounded: "{rounded.pill}"
    padding: "0.125rem 0.625rem"
  verdict-desfavorable:
    backgroundColor: "{colors.bad-tint}"
    textColor: "{colors.bad}"
    rounded: "{rounded.pill}"
    padding: "0.125rem 0.625rem"
  viz-stage:
    backgroundColor: "{colors.tint}"
    rounded: "{rounded.md}"
    height: "15rem"
---

# Design System: Portal Estadístico de Sopó

<!-- Registrado el 2026-11-10 desde el código publicado: prototipo/assets/portal.css, prototipo/index.html, prototipo/assets/portal.js. -->

## Overview

**Creative North Star: "La Ventana Sencilla"**

El portal es una ventana oficial y tranquila a las cifras del municipio, dentro del Kit UI GOV.CO 9.2 en modo restringido. Su firma es la **pestaña-cifra**: cada tema de la barra trae su número, de modo que la barra misma es el resumen de Sopó; al abrir un tema, la cifra y su tablero de Tableau quedan lado a lado en un solo panel pegado a la pestaña.

La densidad es media y ordenada: fondo gris azulado, superficies blancas con borde fino, un solo color de acción (Cobalt) y un marino oscuro que hace de tinta y de selección fuerte. El color no decora: marca acción, selección, fecha de corte y valoración, y cada valoración va con texto e ícono. Nada se mueve salvo la cifra cuando cambia de tema.

El chrome GOV.CO (barra superior, cabecera, pie, barra de accesibilidad, volver arriba) lo pone el CDN v5 sin modificar; en el prototipo se simula y no forma parte de este sistema.

**Key Characteristics:**
- La cifra manda: Work Sans en cifras y títulos, Nunito Sans en todo el texto.
- Un solo acento de acción (Cobalt); el marino marca la pestaña activa.
- Amarillo solo para la fecha de corte; verde y rojo solo para la valoración, siempre con texto.
- Plano: profundidad por borde y tono, sin sombras.
- Píldoras para acciones y etiquetas; esquinas suaves para superficies.
- Contenido de terceros (Tableau) detrás de una puerta con aviso, nunca cargado solo.

## Colors

Paleta restringida del Kit 9.2: un azul de acción, un marino de tinta, neutros fríos y tres colores de señal con trabajo fijo.

### Primary
- **Cobalt GOV.CO** (#0943B5): la única voz de acción. Enlaces, botón "Cargar el tablero", píldoras de hoja (borde, texto y relleno al seleccionar), cifras grandes y cifras de pestaña inactiva, anillo de foco. Su tono de presión **Cobalt profundo** (#07368F) solo aparece en hover.

### Secondary
- **Marino tinta** (#0A1A3F): texto principal y, como relleno, la pestaña activa y el filo superior de 4px del panel del tema. Es la selección fuerte: pestaña y panel se leen como una sola pieza.

### Tertiary
- **Amarillo corte** (#FDBF2D): la fecha de corte ("Datos a octubre de 2026"), la cifra de la pestaña activa sobre marino y el fondo de `::selection`. Nada más.
- **Verde favorable** (#1B6B3A) sobre **Verde velo** (#E4F2E9): variación valorada como favorable. Verde de éxito del Kit (desviación citada en el contrato).
- **Rojo desfavorable** (#A5361A) sobre **Rojo velo** (#FBEAE5): variación valorada como desfavorable.

### Neutral
- **Gris pizarra** (#33415C): texto secundario (entrada, etiqueta de la cifra, fuente, metadatos, aviso de tercero).
- **Fondo GOV** (#F4F6FB): fondo de página.
- **Superficie** (#FFFFFF): cabecera, panel del tema, pestañas inactivas, pie.
- **Velo Cobalt** (#EAF0FB): hover de pestañas y píldoras; fondo del escenario del tablero antes de cargar.
- **Línea** (#C3CFE5): bordes de superficies y divisores de la cifra.
- **Control** (#6F7D99): bordes de elementos interactivos (pestañas, resumen pendiente) y barra de desplazamiento; cumple 3:1 sin texto.

### Named Rules
**La Regla de la Voz Única.** Cobalt es el único color de acción. Si algo se puede tocar y no es la pestaña activa, es Cobalt o tiene borde Cobalt al pasar.

**La Regla del Amarillo con Oficio.** El amarillo solo marca el corte de los datos (y la cifra activa sobre marino). Nunca fondo de sección, nunca alerta.

**La Regla de la Valoración Dicha.** Verde y rojo solo acompañan una valoración escrita ("Favorable", "Desfavorable") y una flecha SVG. Si un indicador no tiene valoración (Población), solo se muestra la dirección en tinta.

**La Regla de los Colores Vetados.** #004884 y #3366CC (mockup v4) no existen en este sistema; su lugar lo ocupa Cobalt.

## Typography

**Display Font:** Work Sans variable (OFL, alojada en `assets/fonts/`), con Nunito Sans, Segoe UI y system-ui de respaldo
**Body Font:** Nunito Sans (400, 700, 900, alojada), con Segoe UI y system-ui de respaldo

**Character:** Work Sans da a títulos y cifras un peso firme y geométrico; Nunito Sans lleva el texto con calidez y buena lectura en celular. Toda medida en `rem`.

### Hierarchy
- **Display** (800, clamp(1.875rem → 2.75rem), 1.1, -0.02em, `text-wrap: balance`): título de la página, una vez.
- **Figure** (700, clamp(2.5rem → 3.5rem), 1, -0.02em, cifras tabulares, Cobalt): la cifra principal del tema. La unidad va debajo en cuerpo 1rem tinta.
- **Headline** (800, 1.75rem, 1.15): nombre del tema en su panel.
- **Title** (700, 1.375rem, 1.3): título de cada hoja de tablero.
- **Tab figure** (700, 1.375rem, 1.15, tabulares; 1.0625rem sin cortes de línea bajo 40rem): la cifra en la pestaña.
- **Button** (Work Sans 600, 0.9375rem en píldoras de hoja, 1.0625rem en "Cargar el tablero", 1.3).
- **Body** (Nunito 400, 1rem, 1.6): texto general. Notas y resúmenes a 1.0625rem; resúmenes hasta 70ch, notas 40ch.
- **Lead** (Nunito 400, 1.125rem, Gris pizarra, 60ch, `text-wrap: pretty`): entrada bajo el título.
- **Label** (Nunito 700, 0.9375rem): nombre del tema en la pestaña, enlaces de cabecera (700, 1rem), etiqueta de la cifra.
- **Meta** (Nunito 400, 0.875rem, Gris pizarra): fuente, fecha y aviso de tercero.

### Named Rules
**La Regla de la Cifra en Work Sans.** Todo número que sea dato (cifra grande, cifra de pestaña) va en Work Sans con cifras tabulares; el texto corrido nunca.

**La Regla del Tamaño Libre.** Sin alturas fijas en texto: la barra de accesibilidad del CDN escribe `font-size` en línea y todo debe crecer con ella.

## Layout

Contenedor centrado de 80rem con margen lateral de 2rem (1rem bajo 40rem). Ritmo de espacio en cinco pasos (0.5, 1, 1.5, 2, 3rem); las secciones respiran con 3rem, los paneles con 2rem de relleno.

Orden de la página: entrada (título y entrada a la izquierda, fecha de corte alineada abajo a la derecha) → barra de 8 pestañas-cifra en rejilla de columnas iguales con 0.5rem de separación → panel del tema activo. El panel es una rejilla de dos columnas (1 : 2.1): hechos a la izquierda (título, cifra, nota), tableros a la derecha (píldoras de hoja, título, resumen, metadatos, escenario).

Respuesta:
- **≤64rem:** la barra pasa a 4 columnas; las pestañas se vuelven tarjetas redondeadas por completo y el panel se separa (pierde el filo marino y gana esquinas en los cuatro lados).
- **≤48rem:** el panel pasa a una columna; la cifra queda encima del tablero.
- **≤40rem:** barra en 2 columnas, cifra de pestaña a 1.0625rem, enlaces de cabecera apilados, escenario cargado en 3:4.

El escenario del tablero mide al menos 15rem antes de cargar; cargado toma 4:3 (máximo 50rem de alto).

## Elevation & Depth

Sistema plano. No hay `box-shadow` en ninguna parte. La profundidad sale de tres capas tonales (Fondo GOV → Superficie → Velo Cobalt) y de bordes de 1px. La única señal de jerarquía fuerte es el filo superior marino de 4px del panel, que lo cose a la pestaña activa.

### Named Rules
**La Regla Plana.** Ninguna superficie lleva sombra. Si algo necesita separarse, gana borde Línea o cambia de capa tonal.

## Shapes

Dos familias de forma. **Superficies** con esquinas suaves: escenario y resumen pendiente a 0.75rem, panel del tema a 1rem. **Acciones y etiquetas** en píldora completa: botón de carga, píldoras de hoja, fecha de corte, valoración.

Las pestañas de escritorio tienen esquinas solo arriba (0.75rem) y el panel solo abajo (1rem): juntos forman una carpeta. Bajo 64rem cada pieza se redondea completa. El resumen pendiente usa borde discontinuo Control para decir "esto aún no está".

Íconos: SVG en línea de 24×24 con trazo `currentColor` de 2.6, extremos redondos, mostrados a 1.25rem. Sin fuentes de íconos.

## Components

### Pestaña-cifra (firma)
Cada tema es un enlace con nombre (Label) y cifra (Tab figure Cobalt). Superficie blanca, borde Control, esquinas superiores 0.75rem, relleno 0.75rem × 0.875rem.
- **Hover:** fondo Velo Cobalt, borde Cobalt.
- **Activa** (`aria-current="true"`): relleno y borde Marino tinta, nombre blanco, cifra amarilla. Foco Cobalt.
- **Transición:** fondo y borde en 180ms con `cubic-bezier(0.16, 1, 0.3, 1)`.

### Panel del tema
Superficie blanca, borde Línea, filo superior marino de 4px, esquinas inferiores 1rem, relleno 2rem. Al cambiar de tema, el título y la cifra suben 0.5rem y aparecen en 320ms (`.nxgov-is-entering`); nada más se anima, y `prefers-reduced-motion` lo apaga.

### Cifra (stat)
Bloque entre dos líneas Línea con 1.5rem de aire: etiqueta (Label, Gris pizarra), cifra (Figure), unidad, variación con flecha SVG y valoración en píldora, y fuente (Meta). La variación sin valoración va en tinta.

### Buttons
- **Shape:** píldora (999px).
- **Primario "Cargar el tablero":** relleno Cobalt, texto blanco, Work Sans 600 1.0625rem, alto mínimo 3rem, relleno 0.75rem × 1.75rem. Hover Cobalt profundo en 180ms. Es la acción principal del escenario.
- **Píldora de hoja** (`aria-pressed`): borde y texto Cobalt sobre blanco, alto mínimo 2.75rem; hover Velo Cobalt; seleccionada en relleno Cobalt y texto blanco.

### Chips
- **Fecha de corte:** píldora amarilla, texto tinta 700 0.9375rem.
- **Valoración:** píldora con velo verde o rojo y texto del color pleno, 0.875rem, siempre junto a la flecha.

### Escenario del tablero (`nxgov-viz`)
Encabezado (título de hoja + "Abrir en Tableau Public"), resumen en texto fuera del iframe, metadatos de fuente y corte, y el escenario: Velo Cobalt, borde Línea, esquinas 0.75rem, con una puerta centrada (botón de carga + aviso de tercero a 36ch). Al cargar (`.nxgov-is-loaded`) el escenario pasa a blanco y el iframe ocupa todo. La carga emite `nxgov:action:load-viz` (cancelable).

### Navigation
Enlaces de cabecera en Label 700 Cobalt subrayados (grosor 0.08em, 0.14em en hover, desfase 0.18em), apilados bajo 40rem. Salto al contenido en marino con texto blanco, visible al recibir foco.

## Do's and Don'ts

### Do:
- **Do** sacar todo valor de un token `--nxgov-*` en `:root`; tipografía y espacio en `rem`.
- **Do** nombrar todo bloque con prefijo `nxgov-` y BEM estricto; estados con `.nxgov-is-*` o atributos ARIA (`aria-current`, `aria-pressed`).
- **Do** acompañar cada valoración con texto y flecha SVG; el color nunca va solo.
- **Do** poner junto a cada cifra su fuente y fecha de corte, y junto a cada tablero su resumen en texto fuera del iframe.
- **Do** cargar Tableau solo tras clic, detrás de la puerta con aviso de tercero.
- **Do** usar anillo de foco Cobalt de 3px con 3px de separación (amarillo sobre la barra Cobalt).
- **Do** respetar `prefers-reduced-motion`: sin animación ni transición.

### Don't:
- **Don't** usar #004884 ni #3366CC, ni cargar el CDN v4, Tailwind o Font Awesome.
- **Don't** tocar ni reestilizar el chrome GOV.CO del CDN v5 ni clases `.govco-*`, `.btn`, `.d-*`.
- **Don't** usar `style` o `script` en línea ni manejadores `on*` (CSP estricta).
- **Don't** usar el amarillo fuera de la fecha de corte y la cifra activa, ni verde o rojo fuera de una valoración.
- **Don't** añadir sombras; la profundidad es tonal.
- **Don't** usar `!important` salvo en `.nxgov-sr-only` y `.nxgov-is-hidden`.
- **Don't** fijar alturas a cajas de texto.
