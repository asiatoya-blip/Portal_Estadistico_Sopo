---
name: Portal Estadístico de Sopó
description: Tablero claro y liviano con las cifras oficiales de Sopó y sus libros de Tableau, dentro del chrome GOV.CO v5.
colors:
  accent: "#0943B5"
  accent-hover: "#07368F"
  accent-soft: "#EEF3FD"
  text: "#101828"
  muted: "#5B6478"
  ground: "#F6F7F9"
  surface: "#FFFFFF"
  line: "#E6E9EF"
  line-strong: "#CDD3DE"
  neutral-soft: "#F1F3F6"
  cut: "#FDBF2D"
  good: "#0F7A55"
  good-soft: "#E8F6EF"
  bad: "#B42318"
  bad-soft: "#FDECEA"
typography:
  display:
    fontFamily: "Work Sans, Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(1.75rem, 1.4rem + 1.2vw, 2.25rem)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Work Sans, Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(1.625rem, 1.3rem + 1vw, 2rem)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  figure:
    fontFamily: "Work Sans, Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "2rem"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-0.02em"
    fontFeature: "tnum"
  title:
    fontFamily: "Work Sans, Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 600
    lineHeight: 1.3
  title-sm:
    fontFamily: "Work Sans, Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 600
    lineHeight: 1.3
  label:
    fontFamily: "Work Sans, Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 600
    lineHeight: 1.3
  body:
    fontFamily: "Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: "Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.6
  caption:
    fontFamily: "Nunito Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 400
    lineHeight: 1.6
rounded:
  sm: "0.5rem"
  md: "0.875rem"
  pill: "999px"
spacing:
  xxs: "0.25rem"
  xs: "0.5rem"
  sm: "0.75rem"
  md: "1rem"
  lg: "1.25rem"
  xl: "1.5rem"
  2xl: "2rem"
  3xl: "2.5rem"
  4xl: "3rem"
  gutter: "clamp(1rem, 3vw, 2.5rem)"
  container: "90rem"
  nav-width: "15rem"
components:
  kpi-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    padding: "0.875rem 1.125rem 0.75rem"
  kpi-chip-mejora:
    backgroundColor: "{colors.good-soft}"
    textColor: "{colors.good}"
    rounded: "{rounded.pill}"
    padding: "0.125rem 0.5rem"
  kpi-chip-empeora:
    backgroundColor: "{colors.bad-soft}"
    textColor: "{colors.bad}"
    rounded: "{rounded.pill}"
    padding: "0.125rem 0.5rem"
  kpi-chip-neutral:
    backgroundColor: "{colors.neutral-soft}"
    textColor: "{colors.muted}"
    rounded: "{rounded.pill}"
    padding: "0.125rem 0.5rem"
  button:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "0.5rem 1rem"
    height: "2.5rem"
  button-hover:
    textColor: "{colors.accent}"
  nav-item:
    textColor: "{colors.text}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "0.5rem 0.75rem"
    height: "2.5rem"
  nav-item-active:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.accent}"
  nav-sub-active:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.accent}"
    rounded: "{rounded.sm}"
    padding: "0.375rem 0.625rem"
  tab:
    textColor: "{colors.muted}"
    typography: "{typography.label}"
    padding: "0.625rem 0.875rem"
  tab-active:
    textColor: "{colors.accent}"
  board:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
  collection-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    padding: "1.25rem"
  pager-link:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "0.75rem 1rem"
  status-pill:
    backgroundColor: "{colors.neutral-soft}"
    textColor: "{colors.muted}"
    rounded: "{rounded.pill}"
    padding: "0.25rem 0.75rem"
---

# Design System: Portal Estadístico de Sopó

## Overview

**Creative North Star: "La mesa de trabajo despejada"**

El portal es un tablero de producto claro y liviano, en la familia de Mercury, Wise o Monarch: un menú lateral sereno a la izquierda, cifras con su tendencia arriba y los libros de Tableau Public como protagonistas del área principal. Todo vive sobre un suelo gris muy pálido (`ground`), con superficies blancas recortadas por un borde fino y esquinas de 14px. El color casi no habla: Cobalt aparece solo donde hay selección o acción, y verde y rojo solo donde una cifra mejora o empeora.

La densidad es media: seis tarjetas en tres columnas, un tablero de proporción 16:11 y pestañas por hoja, sin decoración que compita con los datos. Work Sans da cuerpo a títulos, cifras y navegación; Nunito Sans lleva el texto corrido, las fuentes y los metadatos. El chrome GOV.CO v5 (barra superior, pie, barra de accesibilidad, volver arriba) se carga del CDN sin modificar y no forma parte de este sistema; lo único propio es su alineación al contenedor de 1440px.

El sistema rechaza explícitamente dos extremos: la página-documento (texto largo con tableros escondidos tras un botón) y el tablero oscuro y pesado.

**Key Characteristics:**
- Suelo gris pálido, superficies blancas, borde fino de 1px, sombra casi imperceptible.
- Cobalt reservado para selección, enlaces y acción; nunca como relleno decorativo.
- Estado de cada cifra con texto + ícono SVG + color suave (nunca solo color).
- Tableros de Tableau visibles sin clic, dentro de un marco con resumen, fuente y fecha.
- Todo alineado a un contenedor de 90rem (1440px), incluido el chrome GOV.CO.
- Tipografía en `rem`, tokens `--nxgov-*` en `:root`, BEM con prefijo `nxgov-`, sin estilos en línea.

## Colors

Una paleta casi neutra, fría y luminosa, con un solo acento institucional y dos tonos de estado apagados.

### Primary
- **Cobalt Institucional** (`accent`): enlaces, pestaña y entrada de menú activas, botón al pasar el cursor, contorno de foco (3px) y la línea de tendencia de cada tarjeta. Es el Cobalt del Kit GOV.CO 9.2.
- **Cobalt Profundo** (`accent-hover`): variante oscura reservada para estado de presión/hover en acciones rellenas.
- **Bruma Cobalt** (`accent-soft`): fondo de la sub-entrada activa del menú, del contador de un grupo abierto, del ícono de colección y de la selección de texto.

### Secondary
- **Ámbar de Corte** (`cut`): solo el punto que acompaña la fecha de corte en la cabecera ("Datos a octubre de 2026"). Señal de vigencia, nunca texto ni fondo amplio.

### Tertiary
- **Verde Mejora** (`good`) sobre **Verde Bruma** (`good-soft`): chip, variación y franja de estado de una cifra que mejoró.
- **Rojo Alerta** (`bad`) sobre **Rojo Bruma** (`bad-soft`): chip, variación y franja de estado de una cifra que empeoró.

### Neutral
- **Tinta Pizarra** (`text`): texto principal, cifras y títulos.
- **Gris Pizarra** (`muted`): texto secundario, etiquetas, fuentes, metadatos, pestañas inactivas, íconos del menú.
- **Suelo Niebla** (`ground`): fondo de la página bajo todo el cuerpo.
- **Blanco Superficie** (`surface`): tarjetas, tablero, botones, cabecera y entrada de menú activa.
- **Línea Fina** (`line`): bordes de tarjetas y tablero, divisores internos, raíl de pestañas, borde de la cabecera.
- **Línea Firme** (`line-strong`): borde de botones, separador del nombre en la cabecera, borde de tarjeta al pasar el cursor.
- **Gris Lavado** (`neutral-soft`): chips sin valoración, contadores, fondo del escenario del tablero mientras carga.

### Named Rules
**La Regla del Acento Escaso.** Cobalt marca solo lo seleccionado o accionable. Si un elemento no se puede tocar ni está activo, no es Cobalt.

**La Regla del Estado Triple.** Una mejora o un empeoramiento se dice siempre con palabra ("Mejora", "Empeora"), ícono SVG de flecha y color; ninguna de las tres señales va sola.

**La Regla del Contraste Alto.** En modo `contrast-govco` del CDN solo se redefinen los tokens `--nxgov-color-*` (fondo negro, texto blanco, acento amarillo `#FFE14D`, estados `#7CF2C2` / `#FF9B90`); ningún componente lleva reglas propias de contraste.

## Typography

**Display Font:** Work Sans variable (con Nunito Sans, Segoe UI, system-ui)
**Body Font:** Nunito Sans (con Segoe UI, system-ui)

**Character:** Work Sans aporta un trazo geométrico y técnico a títulos, cifras y navegación; Nunito Sans, redondeada y abierta, hace legible el texto institucional. Ambas se sirven localmente con `font-display: swap`.

### Hierarchy
- **Display** (700, clamp 1.75–2.25rem, 1.15, -0.02em): el título "¿Cómo va Sopó?" del resumen; uno por página.
- **Headline** (700, clamp 1.625–2rem, 1.2, -0.02em): título de cada vista de tablero.
- **Figure** (600, 2rem, 1.1, -0.02em, cifras tabulares): el valor de cada tarjeta; nunca se parte (`nowrap`).
- **Title** (600, 1.25rem, 1.3): encabezados de sección del resumen.
- **Title-sm** (600, 1.0625rem, 1.3): título de cada colección/libro.
- **Label** (600, 0.9375rem, 1.3, Work Sans): entradas del menú, pestañas, botones y paginador.
- **Body** (400, 1rem, 1.6): texto corrido; el resumen de cada tablero se limita a 75ch con `text-wrap: pretty`.
- **Body-sm** (400, 0.875rem): unidades, variación, migas, fecha de corte, franja de estado.
- **Caption** (400, 0.8125rem): fuente de la cifra, metadatos del tablero, nota del menú, aviso de desplazamiento.

### Named Rules
**La Regla de la Cifra Tabular.** Todo número que se compara (valores de tarjeta, contadores del menú) usa `font-variant-numeric: tabular-nums`.

**La Regla del Rem.** Todo tamaño de texto va en `rem` y ninguna caja de texto tiene altura fija: la barra de accesibilidad del CDN escribe `font-size` en línea y el diseño debe crecer con ella.

## Layout

Contenedor centrado de **90rem** (1440px) con margen lateral fluido `clamp(1rem, 3vw, 2.5rem)`. La barra superior GOV.CO conserva su fondo a todo el ancho pero alinea su contenido al mismo contenedor; el pie GOV.CO se limita a 90rem.

El cuerpo es un **shell de dos columnas**: menú lateral de 15rem, pegajoso (`sticky`, top 1.5rem, alto máximo `100vh - 3rem` con desplazamiento propio), y área principal flexible, con 2.5rem de separación. Las tarjetas y las colecciones usan una rejilla de 3 columnas con 1rem de separación.

Ritmo de espaciado observado (en rem): 0.25 · 0.5 · 0.75 · 1 · 1.25 · 1.5 · 2 · 2.5 · 3. Las vistas consecutivas sin JS se separan 3rem; con JS solo se muestra una a la vez.

Puntos de quiebre:
- **≤75rem:** tarjetas y colecciones pasan a 2 columnas.
- **≤64rem:** el shell se vuelve una columna; el menú lateral se convierte en un desplegable (`<details>`) con superficie blanca, que se cierra al elegir un tablero.
- **≤40rem:** tarjetas y colecciones a 1 columna; las pestañas se vuelven una tira desplazable con desvanecido en los bordes; el paginador se apila; el escenario del tablero pasa a 34rem de alto con el iframe a ancho nativo de 60rem y desplazamiento horizontal, precedido por un aviso visible ("Desliza para ver el tablero completo o ábrelo en Tableau Public"). La barra de accesibilidad baja a 5rem del borde inferior.

### Named Rules
**La Regla de los 1440.** Cabecera, cuerpo, barra superior y pie comparten el mismo eje de 90rem; nada propio se sale de ese contenedor.

**La Regla del Tablero Nativo.** En teléfono el libro de Tableau se muestra a su ancho de escritorio con desplazamiento horizontal y aviso; nunca con `:device=phone`, que Tableau Public entrega en blanco.

## Elevation & Depth

Sistema plano con capas tonales: la profundidad la dan el contraste suelo gris / superficie blanca y el borde fino, no las sombras. Existe una sombra de reposo apenas perceptible y una sombra difusa que solo aparece como respuesta al cursor.

### Shadow Vocabulary
- **Reposo** (`box-shadow: 0 1px 2px rgba(16, 24, 40, 0.04)`): tarjetas, colecciones, tablero y entrada activa del menú.
- **Elevación al cursor** (`box-shadow: 0 4px 16px rgba(16, 24, 40, 0.08)`): solo tarjetas de cifra al pasar el cursor, junto con el borde `line-strong`.

### Named Rules
**La Regla de lo Plano por Defecto.** En reposo, las superficies son planas; la sombra visible es respuesta a un estado, nunca adorno.

## Shapes

Esquinas suavemente redondeadas en dos tamaños y una píldora. Las superficies grandes (tarjetas, tablero, colecciones, menú desplegable) usan **0.875rem** (14px); los controles y elementos internos (botones, entradas del menú, paginador, ícono de colección, contorno de foco) usan **0.5rem**; chips, contadores, franja de estado y la fecha de corte son píldoras. El tablero recorta su contenido (`overflow: hidden`) para que el iframe respete la esquina. Bordes siempre de 1px; la única línea de 2px es el subrayado de la pestaña activa.

Los íconos son SVG de trazo (1.125rem, trazo 1.8, extremos redondeados, `currentColor`), nunca fuentes de íconos ni glifos de texto.

## Components

### Buttons
Discretos y de contorno: el botón nunca es un bloque de color.
- **Shape:** esquina suave (0.5rem), alto mínimo 2.5rem.
- **Default:** fondo blanco, borde `line-strong`, texto `text` en Label (Work Sans 600, 0.875rem).
- **Hover / Focus:** el borde y el texto pasan a Cobalt (transición de 150ms); el foco es un contorno Cobalt de 3px separado 2px.
- **Uso:** "Abrir en Tableau Public" junto al título de cada tablero.

### Chips
- **Estado de cifra:** píldora de 0.75rem en negrita: Verde Bruma/Verde Mejora para "Mejora", Rojo Bruma/Rojo Alerta para "Empeora", Gris Lavado/Gris Pizarra para "Sin valoración".
- **Franja de estado:** píldoras de 0.875rem en el encabezado del resumen ("3 mejoraron", "2 empeoraron", "1 sin valoración") con el número en negrita.
- **Contador del menú:** píldora tabular gris que pasa a Bruma Cobalt cuando su grupo está abierto.

### Cards / Containers
- **Tarjeta de cifra (firma del sistema):** superficie blanca, borde `line`, radio 0.875rem, sombra de reposo, relleno `0.875rem 1.125rem 0.75rem`. De arriba abajo: etiqueta + chip de estado, valor (Figure), unidad, línea de tendencia SVG (Cobalt con relleno al 8% y punto final), variación con ícono de flecha, y pie con fuente separado por una línea fina y el enlace "Ver tablero". Si tiene tablero, toda la tarjeta es un enlace; al cursor gana borde `line-strong`, sombra difusa y sube 2px. La tendencia lleva `aria-label` con el rango y el máximo.
- **Colección:** superficie blanca, radio 0.875rem, relleno 1.25rem, ícono SVG sobre Bruma Cobalt, título del libro, metadato y lista de hojas como enlaces Cobalt.

### Navigation
- **Menú lateral:** fondo transparente sobre el suelo. Entradas en Label con ícono gris; al cursor, fondo blanco; la activa (`aria-current="page"`) es blanca con texto e ícono Cobalt y sombra de reposo. Cada libro es un `<details>` plegable con contador; sus hojas cuelgan de una guía vertical de 1px y la activa usa Bruma Cobalt con texto Cobalt en negrita.
- **Pestañas:** tira sobre un raíl `line` de 1px; pestaña inactiva en Gris Pizarra, activa en Cobalt con subrayado de 2px. Se conectan sin espacio con el tablero que controlan.
- **Paginador:** dos tarjetas pequeñas (radio 0.5rem) "anterior / siguiente" con dirección en Caption; al cursor, borde y texto Cobalt.
- **Móvil:** el menú se pliega en un desplegable con chevron que gira 180°.

### Visor de tablero (firma)
Marco blanco de radio 0.875rem que contiene: franja de información (resumen en texto de hasta 75ch + metadatos de fuente y fecha, enlace Cobalt), escenario 16:11 (alto máximo 85vh) con fondo Gris Lavado mientras carga, e iframe de Tableau Public a sangre. El resumen pendiente se marca en cursiva gris.

### Motion
Un solo momento: al llegar al resumen, las tarjetas suben 0.5rem y se asientan (320ms, `cubic-bezier(0.16, 1, 0.3, 1)`), sin ocultar contenido. Las transiciones de estado duran 150ms. Con `prefers-reduced-motion` se eliminan animación y transiciones.

## Do's and Don'ts

### Do:
- **Do** tomar todo color, radio, sombra y duración de los tokens `--nxgov-*` declarados en `:root`.
- **Do** usar el prefijo `nxgov-`, BEM estricto y estados `.nxgov-is-*`; atributos `data-nxgov-*` y eventos `nxgov:<bloque>:<evento>`.
- **Do** mostrar cada tablero de Tableau sin clic, con resumen en texto, fuente, fecha y enlace al libro.
- **Do** acompañar cada estado de cifra con palabra, ícono SVG y color suave.
- **Do** escribir tipografía en `rem` y dejar que el texto crezca sin alturas fijas.
- **Do** alinear todo contenido propio y el chrome GOV.CO al contenedor de 90rem.
- **Do** dar foco visible con contorno Cobalt de 3px y 2px de separación.

### Don't:
- **Don't** modificar el chrome GOV.CO del CDN v5 ni las clases `.govco-*`; solo se ajusta su alineación desde contenedores propios.
- **Don't** usar los colores del mockup v4 (`#004884`, `#3366CC`); el acento es Cobalt.
- **Don't** usar estilos o scripts en línea ni manejadores `on*`; la CSP es estricta.
- **Don't** esconder un tablero tras un botón ni convertir la página en un documento de texto largo.
- **Don't** pasar a un tablero oscuro o pesado, ni usar sombras fuertes en reposo.
- **Don't** usar Cobalt como relleno decorativo ni en elementos que no se pueden tocar.
- **Don't** usar fuentes de íconos ni glifos de texto como íconos; solo SVG de trazo.
- **Don't** cargar Tableau con `:device=phone`.
