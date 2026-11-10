---
name: graficas-nativas
description: Método para diseñar y construir las gráficas nativas del portal (nxgov-chart con Apache ECharts) y su alternativa accesible, con la paleta del Kit GOV.CO 9.2 validada. Úsala al clasificar vistas, elegir el tipo de gráfica, asignar colores, configurar ECharts o revisar una gráfica antes de publicarla.
---

# Gráficas nativas (`nxgov-chart`)

Adaptación del método *dataviz* (en `references/dataviz/`, agnóstico de sistema) a los parámetros del Kit 9.2.
**El método no cambia; solo los parámetros** (`references/paleta-nxgov.md`).

## Procedimiento (en orden; el color va al final)
1. **Elegir la forma** según el trabajo del dato → `references/dataviz/choosing-a-form.md`. A veces la respuesta es
   una tarjeta KPI, no una gráfica. Comparativo por vigencia = barras agrupadas o líneas, nunca doble eje.
2. **Asignar color por función** (categórico, secuencial, divergente, estado) → `references/dataviz/color-formula.md`
   con los valores de `references/paleta-nxgov.md`. Orden fijo de categorías; el color sigue a la entidad, no al rango.
3. **Validar la paleta corriendo el script, no a ojo:**
   `node .claude/skills/graficas-nativas/scripts/validate_palette.js "<hex,...>" --mode light --surface "#ffffff"`.
   Cualquier FAIL se corrige antes de seguir; un WARN de contraste obliga a etiquetas visibles o tabla.
4. **Marcas y anatomía** → `references/dataviz/marks-and-anatomy.md` (líneas 2px, extremos redondeados, separación de
   2px entre rellenos, etiquetas directas selectivas, ejes y rejilla recesivos).
5. **Interacción** → `references/dataviz/interaction.md` (tooltip por marca, cruz en líneas, objetivos táctiles amplios,
   filtros en una fila arriba). Debe funcionar con teclado.
6. **Accesibilidad (obligatoria en el portal):**
   - `figure` + `figcaption` con título que dice el hallazgo y resumen textual (WCAG 1.1.1).
   - ECharts `aria: { enabled: true }` con descripción generada en español + `role="img"` en el lienzo.
   - `decal` (patrones) activable y siempre activo bajo `.contrast-govco` y `forced-colors` (WCAG 1.4.1).
   - `nxgov-data-table` con los mismos datos y enlace al CSV, siempre en el DOM (no generado al vuelo).
   - Leyenda para ≥ 2 series; ≤ 4 series con etiqueta directa; texto en tinta de texto, nunca en el color de la serie.
   - Tamaño de texto ≥ 12px equivalente; respeta +5/−5 de la barra de accesibilidad (re-render en `resize`).
7. **Renderizar y mirar** (captura a 320 y 1440 px) y revisar contra `references/dataviz/anti-patterns.md`.

## ECharts en el portal
- Importación modular (solo `BarChart`, `LineChart`, `PieChart`, componentes `Grid`, `Tooltip`, `Legend`, `Aria`,
  renderer `SVGRenderer`) para un paquete pequeño; servido desde el propio dominio (CSP `'self'`).
- Configuración desde `contracts/chart-config.schema.json` (editable en Decap) + filas de `data/series/<serie_id>.json`.
- Formato numérico es-CO (`Intl.NumberFormat('es-CO')`): miles con punto, decimales con coma.
- Fuente: la del Kit (Nunito Sans / Verdana según rol), tamaños desde tokens.

## Criterios de salida
Paleta validada (salida del script pegada en el PR) · tabla y CSV presentes · resumen escrito por humano o revisado ·
axe sin violaciones · captura a 320 px sin solapes · ninguna entrada de anti-patterns aplica.
