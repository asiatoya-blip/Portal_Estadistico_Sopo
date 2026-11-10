# API de bloques nuevos — Propuesta v0

Todos siguen `nxgov-component-builder`. Se inicializan sobre `[data-nxgov-component="<bloque>"]`.

| Bloque | Base | Markup núcleo | Eventos | JS público |
|---|---|---|---|---|
| `nxgov-tabs` | Patrón WAI-ARIA Tabs (activación manual) | `div[role=tablist]` > `button[role=tab][aria-selected][aria-controls]`; `div[role=tabpanel][tabindex=0]` | `nxgov:action:tab` (cancelable, `detail.id`) · `nxgov:tabs:changed` | `nxgov.tabs.select(el, id)`; sincroniza URL con `history.pushState` |
| `nxgov-stat-card` | Custom | `article` > `h3` título · `p.__value` (`data` con valor) · `p.__delta` (ícono + texto, no solo color) · `p.__meta` (fuente, `time` fecha de corte) | — | — (sin JS) |
| `nxgov-viz` | Custom | `figure` > `figcaption` (título + resumen) · `div.__frame` (`tableau-viz`) · `nxgov-data-table` en `details` · enlaces CSV/Tableau | `nxgov:viz:loaded` · `nxgov:viz:error` · `nxgov:action:view-data` · `nxgov:action:download` | `nxgov.viz.load(el)` (diferida con IntersectionObserver) |
| `nxgov-chart` | ECharts | Igual a `nxgov-viz` pero `div.__canvas` con `role=img` + `aria-label` generado; tabla siempre presente | `nxgov:chart:rendered` · `nxgov:action:view-data` · `nxgov:action:download` | `nxgov.chart.render(el, config, rows)` |
| `nxgov-data-table` | `nxgov-table` | `table` con `caption`, `th[scope]`, números `tabular-nums` a la derecha | — | — |
| `nxgov-fact-card` | Custom | `article` > `h3` · `p` · `p.__source` | — | — |
| `nxgov-lang-switch` | Custom | `nav[aria-label]` > enlaces con `hreflang` y `lang` | — | — |
| `nxgov-assistant` | Custom | `section` > `form` (label visible) · `div[role=log][aria-live=polite]` · citas como enlaces | `nxgov:action:ask` · `nxgov:assistant:answered` · `nxgov:assistant:error` | `nxgov.assistant.ask(texto)` |
| `nxgov-update-log` | Custom | `ol` de cambios (`time`, indicador, valor anterior → nuevo) | — | — |
| `nxgov-period-select` | `nxgov-select` | `select` con `label`; cambia la vigencia mostrada de KPIs y series | `nxgov:action:period` | — |
