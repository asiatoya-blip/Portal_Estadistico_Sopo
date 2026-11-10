---
name: sheets-data-pipeline
description: Lectura de la Google Sheet fuente única, validación contra los contratos, generación de data/*.json y CSV, instantánea en Git con historial y alertas. Úsala al construir o mantener scripts/data/, el workflow de datos, los datos de prueba o la página de historial.
---

# Pipeline Sheets → datos del portal

Contratos: `contracts/sheets-schema.md`, `contracts/kpi.schema.json`, `contracts/chart-config.schema.json`.

## Flujo
```
Google Sheet ──(cuenta de servicio, API Sheets v4, solo lectura)──▶ scripts/data/leer.mjs
   ▶ normalizar (tipos, si/no → boolean, comparación → objeto)
   ▶ validar (ajv + reglas de negocio)  ──FALLA──▶ alerta + salir sin escribir (el sitio queda como estaba)
   ▶ escribir data/kpis.json, data/series/<serie_id>.json, data/fichas.json, data/csv/<serie_id>.csv
   ▶ diff contra el commit anterior ▶ data/historial.json (fecha, id, periodo, anterior → nuevo)
   ▶ commit "datos: <n> cambios (<ids>)" por el bot ▶ build y despliegue
```
Disparadores: cron diario (06:00 hora Colombia = 11:00 UTC) + `workflow_dispatch` ("publicar ahora").

## Reglas de validación (además del JSON Schema)
- `fecha_corte` ≤ hoy; `periodo` coherente con `fecha_corte`.
- Variación > 50 % frente al periodo anterior del mismo `id` → bloquea salvo `confirmado=si` en la fila.
- Conteos de personas < 5 en cualquier desagregación → bloquea (supresión; ver `metadatos-estadisticos`).
- `id` único por `periodo`; `orden` sin duplicados entre destacados.
- Encabezados exactamente iguales al contrato; columna desconocida = error (protege contra cambios accidentales).

## CSV abiertos
UTF-8 con BOM (Excel), separador coma, decimal punto, encabezados en español sin tildes, primera fila de metadatos en
un archivo hermano `<serie_id>.metadata.json` (fuente, fecha de corte, licencia, responsable). Listos para datos.gov.co.

## Secretos
`GOOGLE_SERVICE_ACCOUNT_JSON` y `SHEET_ID` como secretos de GitHub; nunca en el repo ni en logs.

## Datos de prueba
`data/fixtures/` con valores realistas (no los del mockup sin fuente) para que las pistas A, B, D y E trabajen antes
de tener acceso a la hoja real. Marcados `"estado": "borrador"`.

## Criterios de salida
Pruebas unitarias de normalización y cada regla · ejecución en seco contra la hoja real · alerta de fallo probada ·
historial generado correctamente con dos periodos.
