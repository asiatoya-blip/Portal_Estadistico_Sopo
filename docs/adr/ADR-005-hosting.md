# ADR-005 — Cloudflare Pages con espejo en GitHub Pages

- Fecha: 2026-10-20 · Estado: Aprobado

## Decisión
Cloudflare Pages (gratuito) con `_headers` para CSP, HSTS, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`, `frame-ancestors`. Vista previa por PR. El mismo artefacto se publica en GitHub Pages como espejo de contingencia; DNS con TTL 300 s. Subdominio `.gov.co` por CNAME (lo crea TI de la entidad).

## Alternativas descartadas
| Opción | Por qué no |
|---|---|
| Solo GitHub Pages | Sin encabezados propios (Anexo 3) ni vistas previas |
| Netlify | Viable; Cloudflare además aporta Workers y Web Analytics en la misma cuenta |
