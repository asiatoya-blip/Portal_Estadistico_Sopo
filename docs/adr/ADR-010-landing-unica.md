# ADR-010 — Landing única con storytelling y normativa aplicada de forma transversal

- Fecha: 2026-10-20 · Estado: **Reemplazado por ADR-012** (2026-10-30), sin llegar a aprobarse
- Reemplaza en parte: estructura de páginas de `docs/ux/decision-modelo.md` (el modelo martini glass se mantiene)

## Contexto
El prototipo v1 cumplía la norma pero se veía demasiado institucional. El portal es un micrositio externo: la norma
GOV.CO se aplica de forma transversal (chrome oficial, accesibilidad, contraste, datos abiertos), no como plantilla
visual de cada sección. Referente: página de equidad de Spotify (tipografía grande, bloques de color, pestañas y años).

## Decisión
1. **Una sola landing** sin navegación interna entre páginas: capítulos por tema en la misma página, con barra de
   capítulos fija (anclas). Cada capítulo tiene ancla y URL propia (`/#poblacion`) para compartir y medir.
2. **Martini glass dentro de cada capítulo:** titular-hallazgo + cifra grande + gráfica de vista previa; el detalle
   (tabla, más series, desagregaciones) se despliega en el lugar ("Ver los 17 grupos", "Ver valor agregado y
   cosechas"); los exploradores de Tableau se abren en un panel de pantalla completa.
3. **Normativa transversal, sin negociar:** barra superior y pie del CDN GOV.CO v5 sin modificar; WCAG 2.1 AA
   (contrastes verificados, foco, teclado, alternativa en tabla y CSV, `aria-expanded`, `aria-live`); Cobalt `#0943B5`
   como color institucional dominante.
4. **Expresión visual ampliada (tokens nuevos `custom` en `src/styles/tokens-portal.json`):**
   | Token | Valor | Uso | Contraste verificado |
   |---|---|---|---|
   | azul-crema | `#E5ECF8` (Kit Solitude) | fondos de capítulo | texto `#0A1A3F` 14,4:1 |
   | azul-noche | `#0A1A3F` | titulares, bloques oscuros | blanco 17,0:1 |
   | amarillo-acento | `#FDBF2D` | acentos sobre azul | sobre `#0A1A3F` 10,3:1 · sobre Cobalt 5,1:1 |
   | crema-calida | `#FFF5D6` | capítulo Economía | texto `#6B4E00` 7,1:1 |
   | coral | `#EB6834` | segunda serie | texto `#0A1A3F` encima 5,3:1 |
   Tipografía: Nunito Sans (Kit) para titulares hasta 96 px y para el cuerpo; Work Sans para etiquetas y botones.
   Desviación del Kit: cuerpo en Nunito Sans en vez de Verdana (registrar en la matriz de requisitos).
5. Asistente IA como burbuja flotante.

## Consecuencias
- `contracts/urls.md`: una página principal con anclas; se conservan URLs propias para ficha de indicador y datos
  abiertos (necesarias para citar y descargar).
- Componentes nuevos o cambiados: `nxgov-chapter`, `nxgov-big-stat`, `nxgov-chapter-nav`, `nxgov-expand-panel`,
  `nxgov-carousel`, `nxgov-viz-overlay`, `nxgov-assistant-bubble` (además de los de `prototipo-v1.md`).
- `auditor-a11y` debe validar: barra de capítulos fija con teclado, panel de pantalla completa como diálogo modal,
  carrusel operable con teclado, `prefers-reduced-motion`.
