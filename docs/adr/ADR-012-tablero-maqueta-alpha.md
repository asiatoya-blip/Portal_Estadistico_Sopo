# ADR-012 — Estructura tipo tablero (maqueta alpha) con chrome GOV.CO y iframes de Tableau

- Fecha: 2026-10-30 · Estado: Aprobado (decisión del usuario, a pedido del cliente)
- Reemplaza: ADR-010 (landing única con storytelling), que no llegó a aprobarse. Se apoya en ADR-011.

## Contexto
El cliente quiere un portal parecido a la maqueta alpha (`mockup_gemini_alpha/…v5.html`): tarjetas de cifras arriba
y secciones con pestañas por tema. La norma GOV.CO obliga en el chrome (barra superior, cabecera, pie, barra de
accesibilidad) y en accesibilidad; en el cuerpo hay libertad de diseño. Las gráficas son iframes de Tableau (ADR-011).

## Decisión
Estructura de una página con estas secciones, en este orden (prototipo v3, artboard "v3 · Tablero tipo maqueta alpha"):

| Sección | Contenido | Fuente |
|---|---|---|
| Chrome GOV.CO | Barra superior, cabecera con logo oficial, buscador y cambio de idioma; pie con datos de la sede | CDN v5 sin modificar |
| Barra del portal | Nombre del portal, fecha de corte de los datos y enlaces a las secciones | — |
| Sopó en cifras | 6 tarjetas: valor, unidad, variación frente al año anterior (ícono + texto), fuente | Excel TerriData |
| Indicadores territoriales | Pestañas con las 10 hojas del libro TerriData; cada una con título, iframe, "Qué muestra", CSV y ficha | Tableau + Decap |
| Programas sociales | Pestañas por área (8, incluido Observatorio de Familia): responsable, descripción, programas, iframe; Deporte suma el mapa de escenarios | Tableau + Decap |
| Datos curiosos | Pestañas con las 6 hojas del libro de datos curiosos y un resumen en texto | Tableau + Decap |
| Pregúntale a los datos | Preguntas sugeridas + campo de pregunta + respuesta con fuente | Asistente (ADR-006) |
| Datos abiertos | Descarga CSV e historial | Pipeline |

Se toma de la maqueta alpha: la estructura, las pestañas por área, las tarjetas, el asistente con preguntas sugeridas
y los datos del pie. **No** se toma: Tailwind, Font Awesome, Chart.js, colores `#004884`/`#3366CC`, chrome hecho a
mano, iframe con URL editable por el visitante, login, WhatsApp ni la llamada a la IA desde el navegador.

## Consecuencias
- Componentes: `nxgov-stat-card`, `nxgov-tabs` (patrón ARIA con flechas e Inicio/Fin), `nxgov-viz` (iframe + resumen +
  CSV + ficha), `nxgov-assistant` (panel en sección, no burbuja). Se retiran `nxgov-chapter`, `nxgov-big-stat`,
  `nxgov-chapter-nav`, `nxgov-carousel` y `nxgov-expand-panel` de ADR-010.
- URLs (ADR-007): cada pestaña con ancla propia (`#territorio-catastro`, `#programas-deporte`, `#curiosos-altitud`).
- Los iframes no se cargan hasta que su pestaña se abre (`loading="lazy"` + creación al activar la pestaña).
- Prototipos v1, v2 y v2.1 quedan en el lienzo como historial.
- Pendiente de la entidad: URL del libro de Programas Sociales, diseños para teléfono en Tableau y resumen por hoja.
