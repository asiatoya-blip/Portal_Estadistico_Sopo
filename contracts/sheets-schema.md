# Esquema de la Google Sheet — Propuesta v0

La hoja es la fuente única (ADR-002). La fila 1 de cada pestaña es el encabezado, **protegido**. Fechas ISO
`AAAA-MM-DD`. Números sin separador de miles; decimal con punto. Validación de datos de Sheets en columnas con lista.

## Pestaña `KPIs` (una fila por indicador y periodo)

| Columna | Tipo | Obligatoria | Ejemplo |
|---|---|---|---|
| `id` | slug | sí | `poblacion-total` |
| `titulo` | texto ≤ 40 | sí | Población total |
| `valor` | número | sí | 34015 |
| `unidad` | texto | sí | habitantes |
| `decimales` | entero 0–2 | sí | 0 |
| `periodo` | AAAA o AAAA-MM | sí | 2026 |
| `fecha_corte` | fecha | sí | 2026-09-30 |
| `comparacion_valor` | número | no | 24.8 |
| `comparacion_tipo` | `porcentaje` \| `puntos` \| `absoluto` \| `referencia` | si hay comparación | porcentaje |
| `comparacion_texto` | texto | si hay comparación | frente a 2018 |
| `sentido_positivo` | `sube` \| `baja` \| `neutro` | sí | sube |
| `fuente` | texto | sí | DANE — Proyecciones de población |
| `fuente_url` | URL | no | https://… |
| `responsable` | texto | sí | Secretaría de Planeación |
| `icono` | nombre del sprite nxgov | sí | users |
| `orden` | entero | sí | 1 |
| `destacado` | `si` \| `no` | sí | si |
| `estado` | `publicado` \| `borrador` \| `preliminar` | sí | publicado |

## Pestañas `Series_<tema>` (formato largo, una fila por punto)

`serie_id` · `categoria` · `subcategoria` (opcional) · `periodo` · `valor` · `unidad` · `fecha_corte` · `fuente` · `nota`

Una `serie_id` alimenta una gráfica nativa (ver `chart-config.schema.json`) y su CSV.

## Pestaña `Fichas` (metadatos por indicador; ver skill `metadatos-estadisticos`)

`id` · `nombre` · `definicion` · `formula` · `unidad` · `periodicidad` · `cobertura` · `desagregacion` · `fuente` ·
`responsable` · `limitaciones` · `regla_supresion` · `ultima_revision`

## Pestaña `Metricas_portal` (la escribe el workflow de exportación, no el editor)

`mes` · `ruta` · `visitas` · `vistas` · `eventos_csv` · `eventos_ver_datos` · `consultas_asistente`

## Reglas de validación (las aplica `scripts/data/`)
- Obligatorias presentes; tipos correctos; `fecha_corte` ≤ hoy.
- Variación frente al periodo anterior del mismo `id` > 50 % → bloquea y pide confirmación (fila `confirmado=si`).
- Conteos de personas < 5 en una desagregación → bloquea (regla de supresión).
- `id` único por `periodo`.
