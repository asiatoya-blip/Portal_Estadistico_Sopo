# Portal Estadístico de Sopó — Memoria operativa

Micrositio estadístico de la Alcaldía de Sopó (Cundinamarca), enlazado desde la sede electrónica, publicado bajo un
dominio `.gov.co` suministrado por la entidad. Cumple **Kit UI GOV.CO 9.2**, convive sin conflictos con el
**CDN GOV.CO v5** y debe pasar **WCAG 2.1 AA** y la **Resolución 1519 de 2020** (anexos 1 a 4).

> Este archivo es la fuente de contexto de TODOS los agentes. Se actualiza cuando cambia una decisión, un contrato o
> el estado de una etapa. Las decisiones largas viven en `docs/adr/`; aquí solo su resumen de una línea.

## Alcance (un solo lanzamiento, completo — sin "fase 2")

| Pieza | Definición cerrada |
|---|---|
| Chrome GOV.CO | Barra superior, cabecera, pie, barra de accesibilidad y volver arriba del CDN v5 **sin modificar**; mejoras de UX del pie en contenedores propios |
| KPIs | Tarjetas con valor, unidad, variación (texto + ícono, no solo color), fuente, fecha de corte; **comparativo por vigencia** |
| Gráficas | **Solo Tableau Public por `<iframe>`** (ADR-011), dentro de `nxgov-viz` con título, resumen en texto, fuente, fecha y enlace al libro. Sin gráficas nativas |
| Libros Tableau | "Indicadores Territorial TerriData", "Acceso a Programas Sociales y Oferta Institucional", "Escenarios Deportivos y Recreativos de Sopó 2026" y los que la entidad agregue en Decap |
| Datos | **Excel de TerriData = fuente de tarjetas y campos fuera de Tableau** (ADR-011). Subir un Excel nuevo dispara GitHub Actions: lee, valida, guarda instantánea en Git y publica |
| CMS | **Decap CMS** (GitHub, flujo editorial) para textos, fichas técnicas, tableros (URL, orden, resumen), carga del Excel TerriData, qué indicador va en cada tarjeta, datos curiosos |
| Asistente IA | Cloudflare Worker + Workers AI (cupo gratuito), respuestas solo desde datos oficiales con cita; interruptor en Decap |
| Métricas | Cloudflare Web Analytics (sin cookies), una URL por tablero, contador propio de eventos, exportación mensual a Sheets, página "Uso del portal" |
| Idiomas | Interfaz es/en; tableros y datos en español marcados con `lang="es"` |
| Datos abiertos | CSV por conjunto, listos para datos.gov.co |
| Hosting | Cloudflare Pages (`_headers` con CSP/HSTS) + espejo en GitHub Pages |
| Costo recurrente | $0 (solo dominio) |

Fuera de alcance: login/registro de ciudadanos, formularios con datos personales (se enlaza la PQRSD de la sede).

## Stack (ver `docs/adr/`)

Eleventy (HTML-first) · librería `nxgov` (repo Sogas, en `vendor/nxgov/`, solo lectura) · Bootstrap 5 CSS solo para
layout · CDN GOV.CO v5 · Tableau Public por iframe · lector de Excel en Node · Pagefind (búsqueda) ·
Decap CMS · GitHub Actions · Cloudflare Pages + Workers + Web Analytics.

Orden de carga CSS: `bootstrap.min.css` → CDN v5 `all.css` → `vendor/nxgov/styles/nxgov.css` → `src/styles/portal.css`.
**Nunca** cargar el CDN v4, Tailwind ni Font Awesome.

## Reglas heredadas de Sogas (obligatorias)

La bitácora completa está en `vendor/nxgov/CLAUDE.md`. Resumen que no se discute:
- Prefijo `nxgov-` + BEM estricto en todo bloque propio; estados `.nxgov-is-*`; eventos `nxgov:action:<acción>`
  (cancelable) y `nxgov:<bloque>:<evento>` (informativo); `data-nxgov-*`.
- Sandbox: tokens en `:root` (`--nxgov-*`), estilos solo bajo `.nxgov-<bloque>`; sin selectores de etiqueta globales,
  sin `!important` (salvo `.nxgov-sr-only`/`.nxgov-is-hidden`), sin tocar clases `.govco-*`, `.btn`, `.d-*`.
- Cero valores mágicos: todo sale de tokens. Prioridad de fuentes: Figma > Kit 9.2 > CDN v5; si incumple AA gana el Kit.
- Tipografía en `rem`, sin alturas fijas en texto (la barra de accesibilidad escribe `font-size` en línea).
- CSP estricta: sin `eval`, sin `style` en línea, sin `on*`. Movimiento con `--nxgov-motion-*` y `prefers-reduced-motion`.
- Colores del mockup v4 (`#004884`, `#3366CC`) prohibidos → Cobalt `#0943B5` y tokens del Kit.

## Agentes (`.claude/agents/`)

| Agente | Rol | Dueño de |
|---|---|---|
| `ux-ui-designer` | Benchmark, modelo de experiencia, arquitectura de información, wireframes | `docs/ux/` |
| `orquestador` | Plan, etapas, integración, este archivo | `CLAUDE.md`, `docs/etapas.md`, `docs/bitacora.md` |
| `research-normativa` | Kit 9.2, CDN v5, Res. 1519, WCAG, Tableau | `docs/normativa/` |
| `architect` | Arquitectura, contratos, ADRs, API de bloques | `contracts/`, `docs/adr/` |
| `data-analyst` | Sheets, Tableau, fichas técnicas, paleta, CSV | `scripts/data/`, `tableau/`, `contracts/sheets-schema.md` (con architect) |
| `engineer-components` | Bloques `nxgov-` nuevos y gráfica nativa | `src/components/` |
| `engineer-site` | Eleventy, layouts, páginas, rutas, i18n, búsqueda | `src/site/`, `src/styles/`, `eleventy.config.*`, `tests/e2e/` |
| `cms-content` | Decap, colecciones, contenidos, manuales | `admin/`, `content/`, `docs/manuales/` |
| `ai-assistant` | Worker del asistente, grounding, evaluación | `workers/assistant/` |
| `devops` | Repo, CI, Cloudflare, OAuth, analítica, monitoreo | `.github/`, `workers/oauth/`, `workers/metrics/`, `_headers`, `docs/runbooks/` |
| `auditor-a11y` | WCAG 2.1 AA automático y manual (independiente) | `tests/a11y/`, `audits/a11y/` |
| `compliance-security` | Res. 1519 anexos 2–4, Ley 1581, CSP (independiente) | `audits/cumplimiento/` |

Un agente solo escribe en lo que le pertenece. Para cambiar algo ajeno: nota en `docs/bitacora.md` + aviso al dueño.
Ningún agente audita su propio trabajo.

## Skills del proyecto (`.claude/skills/`)

`coordinacion-etapas` (todos) · `govco-normativa` · `nxgov-component-builder` · `graficas-nativas` ·
`tableau-embed` · `sheets-data-pipeline` · `metadatos-estadisticos` · `decap-cms` · `lenguaje-claro` ·
`asistente-ia-grounded` · `cloudflare-deploy` · `auditoria-wcag` · `ux-portales-datos`.

## Etapas (detalle y puertas en `docs/etapas.md`)

| Etapa | Qué | Paralelo | Estado |
|---|---|---|---|
| 0 Adecuación | Accesos, inventarios, repo, matriz de requisitos | research · data · devops | ⏳ Pendiente |
| 1 Contratos y arquitectura | ADRs, esquemas, API de bloques, mapa de URLs, CSP | architect + data + compliance | ⏳ |
| 2 Construcción | Pistas A–F en paralelo (componentes, sitio, datos, CMS, IA, infra) | 6 pistas | ⏳ |
| 3 Integración | Datos reales de punta a punta en `pages.dev` | orquestador + site | ⏳ |
| 4 Auditoría | WCAG manual (NVDA), Res. 1519, seguridad, rendimiento | auditor + compliance | ⏳ |
| 5 Despliegue | DNS, HTTPS, go-live, enlace desde la sede | devops | ⏳ |
| 6 Entrega y operación | Manuales, runbooks, capacitación, ciclo mensual | cms + devops + data | ⏳ |

Puerta de etapa 1 = **aprobación del usuario** (regla Sogas: RESEARCH → ARCHITECT (aprobación) → ENGINEER → AUDITOR).

## Trabajo en paralelo

- Un worktree por pista: `claude --worktree <pista>` (ej. `etapa2-componentes`). Requiere repo git con un commit.
- Rama por pista: `etapa<N>/<pista>`; merge a `main` solo por el `orquestador`, en el orden de dependencias de `docs/etapas.md`.
- Cada cierre de tarea deja una entrada en `docs/bitacora.md` (fecha · agente · qué · archivos · siguiente).

## Insumos entregados por la entidad

- `data_base/TerriData25758f.xlsx` — exportación TerriData (DNP) de Sopó (código DANE 25758). Solo lectura;
  la usa `data-analyst` en E0-D-01 para mapear indicadores y fuentes del libro "Indicadores Territorial TerriData".

## Pendientes externos (bloquean etapas)

- [ ] Nombre exacto del dominio `.gov.co` y contacto de TI para el CNAME (etapa 5; pedir en etapa 0).
- [ ] Compartir la Google Sheet (lectura) con la cuenta de servicio del portal (etapa 0).
- [ ] URLs de los 2 libros de Tableau y lista de hojas (etapa 0).
- [ ] Acta de custodia de la cuenta personal de Tableau Public (ADR-009) y descarga habilitada en el perfil.
- [ ] Organización GitHub de la entidad; cuenta del editor con 2FA (etapa 0).

## Decisiones tomadas (resumen; detalle en `docs/adr/`)

- 2026-10-20 — ADR-001 Sitio estático Eleventy + nxgov + CDN v5; mockup v4 solo como referencia de contenido.
- 2026-10-20 — ADR-002 Google Sheets fuente única; instantánea en Git = control de cambios.
- 2026-10-20 — ADR-003 Gráficas híbridas (nativas + Tableau API v3). **Reemplazado por ADR-011.**
- 2026-10-20 — ADR-004 Decap CMS para contenido; datos numéricos fuera del CMS.
- 2026-10-20 — ADR-005 Cloudflare Pages + espejo GitHub Pages; CSP/HSTS en `_headers`.
- 2026-10-20 — ADR-006 Asistente IA con Workers AI, grounded y con interruptor.
- 2026-10-20 — ADR-007 Métricas sin cookies; una URL por tablero.
- 2026-10-20 — ADR-008 Un solo lanzamiento completo; sin entregas posteriores planificadas.
- 2026-10-20 — ADR-009 Tableau con cuenta personal; extracción completa de la publicación pública al repo.
- 2026-10-20 — ADR-010 Landing única con storytelling. **Reemplazado por ADR-012.**
- 2026-10-29 — ADR-011 Gráficas solo con iframe de Tableau Public; tarjetas desde el Excel de TerriData, que al
  subirse actualiza el sitio. Modifica ADR-002 y ADR-004. Programas, Familias y Datos curiosos solo desde Tableau.
- 2026-10-30 — ADR-012 Estructura tipo tablero (maqueta alpha): cifras arriba + secciones con pestañas e iframes;
  chrome GOV.CO intacto, cuerpo con diseño propio. Prototipo v3 en el lienzo.
