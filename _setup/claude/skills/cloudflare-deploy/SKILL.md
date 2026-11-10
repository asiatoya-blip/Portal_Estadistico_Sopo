---
name: cloudflare-deploy
description: Infraestructura del portal en Cloudflare (Pages, Workers de OAuth/métricas/asistente, Web Analytics), GitHub Actions, encabezados de seguridad, espejo en GitHub Pages, DNS, monitoreo y reversión. Úsala para CI/CD, despliegue, dominios, secretos, monitoreo o incidentes.
---

# Despliegue y operación

Decisiones: ADR-005 (hosting), ADR-007 (métricas). Encabezados: `contracts/csp.md`.

## Workflows (`.github/workflows/`)
| Workflow | Disparo | Hace |
|---|---|---|
| `build.yml` | push/PR | instala, `eleventy`, Pagefind, axe/Pa11y sobre el sitio generado, publica en Pages (preview por PR) |
| `datos.yml` | cron 11:00 UTC + manual | pipeline Sheets (`sheets-data-pipeline`) y commit de `data/` |
| `tableau-urls.yml` | diario | verifica que cada URL de `content/tableau/` responda; abre issue si falla |
| `cdn-regresion.yml` | semanal | captura Playwright del chrome GOV.CO y compara; abre issue si cambia |
| `metricas-export.yml` | mensual | exporta Web Analytics + contador propio a `Metricas_portal` |
| `espejo.yml` | tras deploy en main | publica el mismo artefacto en GitHub Pages |
| `dependencias.yml` | mensual | auditoría de dependencias y versiones fijadas |

Acciones fijadas por SHA; permisos mínimos por job; secretos solo en GitHub/Cloudflare.

## Cloudflare
- Pages: proyecto conectado al repo; `_headers` en la salida del build; dominio personalizado por CNAME.
- Workers: `workers/oauth` (proxy OAuth de Decap), `workers/metrics` (eventos sin cookies), `workers/assistant`.
- Web Analytics: beacon en el layout; CSP lo permite.

## DNS y dominio (Etapa 5)
Pedir a TI: `CNAME <subdominio> → <proyecto>.pages.dev`, TTL 300. Verificar HTTPS, HSTS y el dominio en Search Console.

## Monitoreo y reversión
- Chequeo de disponibilidad cada 5 min con alerta por correo (servicio gratuito; documentar cuál en el runbook).
- Reversión: "Rollback" al despliegue anterior en Pages o `git revert` del commit; ensayar antes del go-live.
- Contingencia: cambiar CNAME al espejo de GitHub Pages (≤ 10 min).

## Runbooks (`docs/runbooks/`)
cuentas.md · despliegue.md · reversion.md · incidente-tableau.md · incidente-datos.md · rotacion-secretos.md.

## Criterios de salida
Preview por PR funcionando · encabezados verificados (securityheaders o curl) · reversión y espejo ensayados ·
monitoreo con alerta probada.
