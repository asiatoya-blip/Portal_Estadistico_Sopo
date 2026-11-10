# ADR-004 — Decap CMS para contenido; datos numéricos fuera del CMS

- Fecha: 2026-10-20 · Estado: Aprobado

## Decisión
Decap CMS 3.x en `/admin` con backend GitHub, flujo editorial (borrador → revisión → listo) y proxy OAuth en un Worker de Cloudflare. Colecciones: páginas, fichas técnicas por indicador, vistas de Tableau (URL, hoja, orden, resumen), configuración de gráficas nativas, datos curiosos (fuente obligatoria), ajustes globales (interruptor del asistente, avisos). La configuración es compatible con Sveltia CMS como plan B.

## Consecuencias
El editor usa una cuenta GitHub de la entidad con 2FA. Cada publicación es un PR con vista previa de Cloudflare Pages.
