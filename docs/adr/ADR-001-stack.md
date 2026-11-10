# ADR-001 — Sitio estático con Eleventy + nxgov + CDN GOV.CO v5

- Fecha: 2026-10-20 · Estado: Aprobado

## Contexto
Costo recurrente $0, ~5.000 visitas/mes, convivencia sin conflictos con el CDN v5 y la librería `nxgov` (HTML + CSS BEM + JS vanilla, sin dependencias). El mockup v4 usa Tailwind por CDN, paleta v4, Font Awesome y `filter: invert`, incompatibles con la norma.

## Decisión
Generador estático **Eleventy** (plantillas Nunjucks, HTML-first, sin framework cliente). Los bloques `nxgov-` se exponen como macros/includes. Bootstrap 5 CSS solo para layout. El mockup v4 queda como referencia de contenido y distribución, no de código.

## Alternativas descartadas
| Opción | Por qué no |
|---|---|
| Astro | Viable, pero añade capa de componentes que duplica el modelo `nxgov` |
| WordPress/Drupal | Requiere hosting PHP+BD con costo y parches; choques con el CDN |
| Tailwind | Reset global que rompe el sandbox `nxgov` y el CDN v5 |

## Consecuencias
KPIs, tablas y textos llegan escritos en el HTML (funcionan sin JS). La librería se consume desde `vendor/nxgov/` con hash de origen; mejoras a la librería se proponen al repo Sogas.
