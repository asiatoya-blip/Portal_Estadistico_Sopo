# ADR-011 — Gráficas solo en Tableau (iframe) y tarjetas desde el Excel de TerriData

- Fecha: 2026-10-29 · Estado: Aprobado (decisión del usuario)
- Reemplaza: ADR-003 (gráficas híbridas). Modifica: ADR-002 (fuente de las tarjetas) y ADR-004 (colecciones de Decap).

## Contexto
El usuario decide no construir gráficas nativas por ahora. Las visualizaciones las aporta la entidad como libros de
Tableau Public (p. ej. "Escenarios Deportivos y Recreativos de Sopó 2026"). Las tarjetas y los campos que no están en
Tableau salen de la exportación de TerriData (DNP) en Excel; al cargar un Excel nuevo, el sitio se debe actualizar solo.

La exportación (`data_base/TerriData25758f.xlsx`) es una tabla larga de una hoja con 13 columnas fijas:
`Código Departamento · Departamento · Código Entidad · Entidad · Dimensión · Subcategoría · Indicador · Dato Numérico ·
Dato Cualitativo · Año · Mes · Fuente · Unidad de Medida` (5.961 filas, 932 indicadores, 18 dimensiones). Los números
vienen como texto con formato colombiano (`13.883,00`) y un mismo indicador-año puede repetirse con dos fuentes.

## Decisión
1. **Gráficas:** solo libros de Tableau Public insertados con `<iframe>` (sin `viz_v1.js` ni la Embedding API), dentro
   del bloque `nxgov-viz`: título, resumen en texto, fuente, fecha de corte, "Abrir en Tableau Public" y, cuando la
   entidad lo entregue, enlace a los datos en CSV. URL: `https://public.tableau.com/views/<libro>/<hoja>?:showVizHome=no&:embed=y&:language=es-ES`.
   Las URLs, títulos y resúmenes se administran en Decap (colección "Tableros").
2. **Tarjetas y campos fuera de Tableau:** salen del Excel de TerriData. Flujo:
   - El editor sube el Excel nuevo en Decap (colección "Datos TerriData", campo archivo) o en GitHub, a
     `data_base/terridata/`.
   - Un workflow de GitHub Actions se dispara con ese cambio, lee el Excel, valida (13 columnas exactas, código de
     entidad 25758, números legibles, año y fuente presentes), normaliza números y resuelve duplicados (última fila por
     indicador-año, como en el fixture), y escribe `data/terridata.json`, `data/csv/terridata.csv` y
     `data/tarjetas.json`.
   - **Qué tarjeta muestra qué** lo define un archivo de configuración editable en Decap (`content/tarjetas.yml`):
     indicador exacto, etiqueta en lenguaje claro, unidad, capítulo, y comparación (año anterior o año base). El año
     mostrado es siempre el último disponible.
   - El workflow genera un resumen de cambios (indicadores nuevos, valores cambiados, años nuevos, indicadores que
     desaparecieron) que queda en el commit y en la página "Historial de actualizaciones".
   - Si la validación falla, o una tarjeta apunta a un indicador que ya no existe, no se publica: el sitio conserva la
     última versión buena y se alerta.
3. **Lenguaje:** el lector del Excel y el workflow en JavaScript (Node), igual que el resto del sitio (ADR-001).

4. **Programas, Familias y Datos curiosos** (2026-10-30, decisión del usuario): se muestran **solo desde Tableau**,
   sin tarjetas propias ni datos fuera del libro. Sus capítulos llevan titular, resumen en texto e iframe.
   Inventario de libros y hojas: `tableau/inventario-libros.md`.

## Alternativas descartadas
| Opción | Por qué no |
|---|---|
| Gráficas nativas con ECharts (ADR-003) | Decisión del usuario: por ahora toda gráfica viene de Tableau |
| Código de inserción de Tableau (`viz_v1.js`) | `<script>` en línea y estilos por JS: incumple la CSP; el respaldo de imagen estática sale vacío (1×1 px) |
| Embedding API v3 (`<tableau-viz>`) | Útil para eventos y datos, pero la lectura de datos devuelve 403 en los libros probados; el iframe es más simple y suficiente |
| Copiar las cifras del Excel a mano en Google Sheets | Doble trabajo y riesgo de error; TerriData ya es la fuente oficial |
| Leer el Excel en el navegador | Sin validación, sin historial, sin HTML para buscadores ni lectores de pantalla |

## Consecuencias
- Se retiran del alcance: `nxgov-chart`, Apache ECharts, `contracts/chart-config.schema.json` y la skill
  `graficas-nativas` (queda solo como referencia de paleta para tarjetas).
- `contracts/kpi.schema.json` y `contracts/sheets-schema.md` pasan a describir el Excel de TerriData y
  `content/tarjetas.yml` (architect + data-analyst).
- Google Sheets ya no alimenta el portal; solo la usa la entidad, si quiere, para sus libros de Tableau.
- **Accesibilidad (WCAG 1.1.1):** un iframe de Tableau no es accesible por sí solo. Cada tablero necesita un resumen en
  texto escrito por el editor (obligatorio en Decap) y, cuando sea posible, los datos en CSV. Sin eso, la auditoría de
  la etapa 4 lo marcará como hallazgo.
- CSP: `frame-src https://public.tableau.com`; sin `script-src` para Tableau.
- El prototipo v2.1 usa gráficas dibujadas en población, ciudad moderna, economía, finanzas y seguridad; en la
  construcción se reemplazan por tarjetas TerriData + iframe del libro correspondiente (prototipo v2.2).
- El Excel de TerriData tiene nombres de indicador largos y a veces cambian entre exportaciones; la validación de
  `content/tarjetas.yml` lo detecta antes de publicar.
