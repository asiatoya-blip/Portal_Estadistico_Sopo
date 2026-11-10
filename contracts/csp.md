# Encabezados y CSP — Propuesta v0 (los aplica devops en `_headers`)

```
Content-Security-Policy: default-src 'self'; script-src 'self' https://cdn.www.gov.co https://public.tableau.com https://static.cloudflareinsights.com; style-src 'self' https://cdn.www.gov.co https://cdn.jsdelivr.net; font-src 'self' https://cdn.www.gov.co; img-src 'self' data: https://cdn.www.gov.co https://public.tableau.com; frame-src https://public.tableau.com; connect-src 'self' https://public.tableau.com https://cloudflareinsights.com https://<worker-asistente> https://<worker-metricas>; frame-ancestors 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```
`/admin/*` amplía `script-src`/`connect-src` solo para Decap y la API de GitHub. Verificar en la Etapa 0 los dominios
reales que pide el CDN v5 (`research-normativa`) y Bootstrap (servir local para evitar otro origen).
