# ADR-002 — Google Sheets como fuente única de datos; instantánea en Git como control de cambios

- Fecha: 2026-10-20 · Estado: Aprobado, **modificado por ADR-011** (2026-10-29): la fuente de tarjetas es el Excel de
  TerriData en lugar de Google Sheets; se mantienen validación, instantánea en Git e historial

## Contexto
Los tableros de Tableau ya cargan desde una Google Sheet que el editor designado actualiza. Se pide un control de cambios mensual fácil, rápido y con mínima curva de aprendizaje.

## Decisión
Tarjetas KPI, gráficas nativas y CSV salen de la misma hoja. Un workflow de GitHub Actions (diario + botón "publicar ahora") la lee con una cuenta de servicio, valida contra `contracts/*.schema.json` y reglas de negocio (fuente, fecha de corte, umbral de variación), escribe `data/*.json` + `data/csv/*.csv`, hace commit (autor bot, mensaje con el resumen de cambios) y dispara el build. Si falla, el sitio conserva la última versión buena y se envía alerta.

## Alternativas descartadas
| Opción | Por qué no |
|---|---|
| KPIs en Decap | Segunda herramienta para el editor; doble fuente frente a Tableau |
| Leer la hoja en el navegador | Expone la hoja, sin validación ni historial, falla si Google cae |

## Consecuencias
El historial de `data/` es el registro de cambios; el sitio publica una página "Historial de actualizaciones" generada desde él. La hoja necesita encabezados protegidos y validación de datos.
