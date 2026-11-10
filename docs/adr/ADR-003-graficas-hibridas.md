# ADR-003 — Gráficas híbridas: nativas (ECharts) + Tableau Public (Embedding API v3)

- Fecha: 2026-10-20 · Estado: **Reemplazado por ADR-011** (2026-10-29)

## Contexto
Tableau Public no exporta HTML autónomo: código de inserción, iframe y Embedding API v3 cargan desde public.tableau.com. En teléfono el comportamiento es errático. WCAG 1.1.1 exige alternativa a cada gráfica.

## Decisión
Cada vista del inventario se clasifica: **simple** (barras, líneas, donas, comparativos) → `nxgov-chart` con Apache ECharts (módulo `aria`, patrones `decal`) desde los JSON de la hoja; **explorador** (filtros múltiples, mapas, drill-down) → `nxgov-viz` con `<tableau-viz hide-tabs>` y `activateSheetAsync()`, carga diferida. **Toda** vista lleva resumen textual, `nxgov-data-table`, CSV, fuente y fecha de corte. Sin hojas tipo Story.

## Alternativas descartadas
| Opción | Por qué no |
|---|---|
| Solo iframe | Sin control de pestañas, errores ni carga diferida |
| Todo nativo | Re-implementar exploradores complejos de TerriData sin beneficio |
| Imágenes exportadas | Pierden interactividad; exportación manual mensual |

## Consecuencias
Regla dura: no renombrar libros ni hojas publicados. `.twbx` versionados en `tableau/libros/`. Chequeo nocturno de URLs.
