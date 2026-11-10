# Contrato de métricas — Propuesta v0

Páginas: Cloudflare Web Analytics (beacon). Eventos propios: `POST /api/evento` → `{ "tipo": "csv" | "ver-datos" | "asistente" | "tableau-error", "ruta": "/tableros/…", "id": "serie o vista" }`. Sin cookies, sin IP ni user-agent almacenados; agregación diaria por `tipo`+`ruta`. Exportación mensual a la pestaña `Metricas_portal`.
