# Etapas, pistas paralelas y puertas de calidad

Un solo lanzamiento completo. Cada etapa termina en una **puerta** con criterios verificables; nadie empieza la
etapa siguiente sin que el `orquestador` marque la puerta como cumplida en `CLAUDE.md`.

Convención de IDs de tarea: `E<etapa>-<pista>-<n>` (ej. `E2-A-03`). Cada tarea cerrada deja entrada en
`docs/bitacora.md`.

---

## Etapa 0 — Adecuación (paralelo: research · data · devops · orquestador)

| ID | Tarea | Agente | Entregable |
|---|---|---|---|
| E0-R-01 | Matriz de requisitos trazable: Kit 9.2, CDN v5, WCAG 2.1 AA, Res. 1519 anexos 1–4, Ley 1712, Ley 1581 | research-normativa | `docs/normativa/matriz-requisitos.md` (requisito → criterio → cómo se prueba → dueño) |
| E0-R-02 | Snippets oficiales CDN v5 de barra superior, cabecera, pie, accesibilidad, volver arriba (desde los módulos fuente, ver protocolo en `vendor/nxgov/CLAUDE.md`) | research-normativa | `docs/normativa/cdn-v5-transversales.md` |
| E0-R-03 | Contenido obligatorio del pie (Anexo 2) con los datos reales de Sopó | research-normativa | sección en el mismo archivo |
| E0-D-01 | Inventario de la Google Sheet: pestañas, columnas, tipos, rangos, quién edita; cruce con `data_base/TerriData25758f.xlsx` (indicadores, fuentes, años) | data-analyst | `tableau/inventario-sheets.md` |
| E0-D-02 | Inventario de los 2 libros: hojas, tipo (vista simple / explorador), URL, filtros, layout móvil, fuente | data-analyst | `tableau/inventario-libros.md` con la columna "camino: nativa | tableau" |
| E0-D-03 | Extracción de la publicación pública (ADR-009): `.twbx`, CSV por hoja, capturas | data-analyst | `tableau/libros/`, `tableau/extraccion/` |
| E0-U-01 | Estudio UX: benchmark de portales de datos, decisión de modelo de experiencia, arquitectura de información y wireframes | ux-ui-designer | `docs/ux/` (puerta previa a E1-A-05, E1-A-06 y E1-A-10) |
| E0-O-01 | `git init`, commit inicial, `vendor/nxgov` desde Sogas con hash de origen | devops | `vendor/nxgov/VERSION` |
| E0-O-02 | Organización GitHub de la entidad, cuenta del editor (2FA), cuenta de servicio de Google con lectura a la hoja | devops | `docs/runbooks/cuentas.md` (sin secretos) |
| E0-O-03 | Proyecto Cloudflare Pages en `*.pages.dev`; solicitud formal de CNAME a TI | devops | URL de preproducción |
| E0-X-01 | Seguimiento de pendientes externos | orquestador | `CLAUDE.md` § Pendientes |

**Puerta 0:** matriz completa · ambos inventarios con el camino decidido por vista · repo con commit inicial ·
lectura de la hoja probada desde la cuenta de servicio.

---

## Etapa 1 — Contratos y arquitectura (architect lidera; data-analyst y compliance-security revisan)

Los contratos son lo que permite el trabajo en paralelo de la etapa 2. Una vez aprobados, solo cambian con ADR.

| ID | Contrato / decisión | Archivo |
|---|---|---|
| E1-A-01 | Esquema de la hoja (pestañas `KPIs`, `Series_*`, `Fichas`, `Metricas_portal`) | `contracts/sheets-schema.md` |
| E1-A-02 | JSON Schema de KPIs (con periodo para comparativos) | `contracts/kpi.schema.json` |
| E1-A-03 | JSON Schema de configuración de gráfica nativa | `contracts/chart-config.schema.json` |
| E1-A-04 | JSON Schema de vistas de Tableau | `contracts/tableau-view.schema.json` |
| E1-A-05 | API de bloques nuevos: markup, modificadores, eventos, JS público | `contracts/componentes.md` |
| E1-A-06 | Mapa de URLs (es/en), una URL por tablero, slugs | `contracts/urls.md` |
| E1-A-07 | Política CSP y encabezados | `contracts/csp.md` |
| E1-A-08 | Contrato del asistente IA (entrada, salida, citas, errores) | `contracts/asistente-api.md` |
| E1-A-09 | Contrato de eventos de métricas | `contracts/metricas.md` |
| E1-A-10 | Wireframes de las páginas (ASCII o Figma) y jerarquía de encabezados | `docs/adr/ADR-009-paginas.md` |
| E1-C-01 | Revisión de cumplimiento de todos los contratos | compliance-security → nota en bitácora |

**Puerta 1:** todos los contratos en estado "Aprobado v1" · **aprobación explícita del usuario** · paleta de
gráficas validada (`graficas-nativas`).

---

## Etapa 2 — Construcción en paralelo (6 pistas, un worktree cada una)

| Pista | Agente | Tareas principales | Depende de |
|---|---|---|---|
| **A Componentes** | engineer-components | `nxgov-tabs`, `nxgov-stat-card`, `nxgov-viz` (marco Tableau + estados), `nxgov-chart` (ECharts), `nxgov-data-table` (sobre `nxgov-table`), `nxgov-fact-card`, `nxgov-lang-switch`, `nxgov-assistant` (UI del chat), `nxgov-update-log`; catálogo `src/catalogo/` | Puerta 1 |
| **B Sitio** | engineer-site | Eleventy, layout con chrome CDN v5, páginas (inicio, tableros por libro, ficha de indicador, historial, datos abiertos, uso del portal, accesibilidad, privacidad), rutas es/en, Pagefind, sitemap, 404 | Puerta 1; usa A por markup de referencia |
| **C Datos** | data-analyst (+devops para el workflow) | Lector Sheets → JSON, validación, umbrales, instantánea, CSV, historial; datos de prueba realistas para las demás pistas | Puerta 1 |
| **D CMS** | cms-content | Decap `config.yml`, colecciones, vista previa, contenidos reales migrados del mockup con fuente, guía del editor | Puerta 1 |
| **E IA** | ai-assistant | Worker, índice de contexto desde `data/` y fichas, citas, límite de uso, caché, interruptor, 30 preguntas de evaluación | Puerta 1; usa C |
| **F Infra** | devops | Workflows (build, datos, export métricas, chequeo de URLs Tableau, regresión visual del CDN), `_headers`, OAuth Worker, Web Analytics, contador de eventos, monitoreo, espejo GitHub Pages | Puerta 1 |

Durante toda la etapa, `auditor-a11y` corre la auditoría automática sobre cada PR de A y B (no construye).

**Puerta 2 (por pista):** criterios de la skill de la pista cumplidos · auditoría automática sin errores ·
entrada en bitácora · PR listo para integrar.

---

## Etapa 3 — Integración (orquestador + engineer-site)

Orden de merge: C → A → B → D → F → E. Se integra con los datos reales de la hoja en `pages.dev`.

**Puerta 3:** recorrido de punta a punta: el editor cambia un KPI en Sheets → publica → aparece con historial;
cambia un texto en Decap → revisión → publicado; cada vista Tableau y nativa con tabla y CSV; asistente responde
las 30 preguntas de evaluación con cita correcta (≥ 28/30, 0 cifras inventadas).

---

## Etapa 4 — Auditoría independiente (auditor-a11y · compliance-security)

- WCAG 2.1 AA completa: automática en todas las páginas + manual (teclado, NVDA + Firefox/Chrome, zoom 200 %/400 %,
  reflujo 320 px, texto +5/−5 de la barra GOV.CO, contraste, alto contraste, `forced-colors`, `prefers-reduced-motion`).
- Res. 1519: anexo 1 (lista de chequeo), anexo 2 (pie, enlace con sede), anexo 3 (HTTPS, encabezados, dependencias,
  disponibilidad), anexo 4 (CSV abiertos y metadatos).
- Rendimiento: Lighthouse ≥ 90 en accesibilidad, buenas prácticas y SEO; LCP < 2,5 s en 4G simulado sin Tableau.

Ciclo: hallazgo → issue al dueño → corrección → re-auditoría. **Puerta 4:** cero hallazgos bloqueantes; informe
firmado en `audits/`.

---

## Etapa 5 — Despliegue (devops)

DNS (CNAME), HTTPS, HSTS, Search Console, Web Analytics, monitoreo, espejo, enlace desde la sede, prueba de reversión.
**Puerta 5:** sitio en el dominio final, monitoreo verde 72 h, reversión ensayada.

## Etapa 6 — Entrega y operación

Guía del editor, video corto, runbooks (actualización mensual, incidente Tableau, reversión, rotación de cuentas),
capacitación. Operación: ciclo mensual de datos; revisión trimestral de dependencias, accesibilidad y CDN.

---

## Mapa de propiedad de carpetas

| Ruta | Dueño | Otros |
|---|---|---|
| `CLAUDE.md`, `docs/etapas.md`, `docs/bitacora.md` | orquestador | todos agregan entradas a la bitácora |
| `contracts/`, `docs/adr/` | architect | lectura para todos |
| `docs/normativa/` | research-normativa | |
| `data_base/` | entidad (insumos, solo lectura) | data-analyst lee |
| `vendor/nxgov/` | nadie (solo lectura) | cambios a la librería → propuesta al repo Sogas |
| `src/components/`, `src/catalogo/` | engineer-components | |
| `src/site/`, `src/styles/`, `eleventy.config.*`, `tests/e2e/` | engineer-site | |
| `scripts/data/`, `tableau/`, `data/fixtures/` | data-analyst | |
| `data/` (generado) | solo el workflow de datos | nadie lo edita a mano |
| `admin/`, `content/`, `docs/manuales/` | cms-content | |
| `workers/assistant/` | ai-assistant | |
| `.github/`, `workers/oauth/`, `workers/metrics/`, `_headers`, `docs/runbooks/` | devops | |
| `tests/a11y/`, `audits/a11y/` | auditor-a11y | |
| `docs/ux/` | ux-ui-designer | |
| `audits/cumplimiento/` | compliance-security | |
