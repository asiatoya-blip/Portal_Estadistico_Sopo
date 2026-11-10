---
name: metadatos-estadisticos
description: Ficha técnica por indicador, fuente, fecha de corte, periodicidad y reglas de confidencialidad estadística (supresión de conteos pequeños) para el portal. Úsala al definir o revisar un indicador, un KPI, un CSV o un dato curioso con cifras.
---

# Metadatos y calidad estadística

Toda cifra publicada responde: qué mide, cómo se calcula, de dónde sale, a qué fecha corresponde y quién responde.

## Ficha técnica (pestaña `Fichas` y página `/indicadores/<id>/`)
| Campo | Ejemplo |
|---|---|
| Nombre | Población total |
| Definición | Número de habitantes del municipio |
| Fórmula / método | Proyección DANE con base CNPV 2018 |
| Unidad | habitantes |
| Periodicidad | anual |
| Cobertura / desagregación | municipal; urbano/rural |
| Fuente | DANE — Proyecciones de población (enlace) |
| Responsable | Secretaría de Planeación |
| Limitaciones | Proyección, no conteo |
| Regla de supresión | Conteos < 5 se publican como "< 5" o se agregan |
| Última revisión | AAAA-MM-DD |

## Reglas
- **Sin fuente no se publica** (KPIs, series, datos curiosos). El mockup tiene cifras sin fuente: verificarlas o retirarlas.
- Fecha de corte visible junto a cada cifra; "preliminar" se etiqueta con `nxgov-tag`.
- Confidencialidad: ninguna celda con menos de 5 personas en desagregaciones (vereda, condición de discapacidad,
  salud mental, etc.). Ley 1581 de 2012.
- Comparaciones solo entre periodos con la misma metodología; si cambia, nota en la ficha.
- Redondeo y decimales fijados por indicador (`decimales`), formato es-CO.

## Criterios de salida
Cada indicador publicado tiene ficha completa, fuente enlazada cuando es pública y regla de supresión declarada.
