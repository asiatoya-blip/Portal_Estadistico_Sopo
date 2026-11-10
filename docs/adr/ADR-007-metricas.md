# ADR-007 — Métricas del portal sin cookies

- Fecha: 2026-10-20 · Estado: Aprobado

## Decisión
Cloudflare Web Analytics (visitas, páginas, origen, dispositivo; registra cambios de URL vía History API). Cada pestaña/tablero tiene URL propia. Eventos (descarga CSV, "ver datos", consultas al asistente) con un contador propio en `workers/metrics/` sin cookies ni IP almacenada. Exportación mensual a la pestaña `Metricas_portal` de la hoja (Web Analytics solo conserva 6 meses consultables). Página "Uso del portal" generada desde esa pestaña. Google Search Console para búsquedas.
