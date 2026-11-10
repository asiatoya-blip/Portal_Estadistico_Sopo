---
name: nxgov-component-builder
description: Procedimiento para construir un bloque nxgov- nuevo (tabs, stat-card, viz, chart, data-table, fact-card, assistant, etc.) siguiendo las reglas de la librería Sogas. Úsala cada vez que se cree o modifique un componente en src/components/.
---

# Construir un bloque `nxgov-`

Base obligatoria: `vendor/nxgov/CLAUDE.md` (naming, sandbox, riesgos de colisión) y `contracts/componentes.md`.

## Estructura
```
src/components/<bloque>/        ← nombre SIN prefijo
├── <bloque>.css                ← todo bajo .nxgov-<bloque>
├── <bloque>.njk                ← macro Nunjucks para Eleventy (markup de referencia)
├── <bloque>.js                 ← solo si tiene lógica; ES module, sin dependencias (salvo ECharts en nxgov-chart)
└── README.md                   ← API: markup, modificadores, eventos, JS público, accesibilidad
```
Y una entrada en el catálogo `src/catalogo/` con todos los estados.

## Reglas (no negociables)
1. Prefijo `nxgov-` + BEM; estados `.nxgov-is-*` + atributos ARIA; `data-nxgov-*`.
2. Solo tokens `--nxgov-*` (añadir tokens nuevos en `src/styles/tokens-portal.json` y regenerar; nunca hex sueltos).
3. Reset de lo heredado solo dentro del bloque (`box-sizing`, márgenes de `h*`/`p`, `font` de `button`).
4. Tipografía en `rem`; sin alturas fijas en texto; probar con +5/−5 de la barra de accesibilidad.
5. Funciona igual con y sin Bootstrap; layout de página fuera del bloque.
6. JS: inicializa sobre `[data-nxgov-component="<bloque>"]`; emite `nxgov:action:<acción>` (cancelable, con
   `detail.component`) y `nxgov:<bloque>:<evento>`; usa `vendor/nxgov/utils/js/emit.js` (`emit`, `announce`, `setBusy`).
7. CSP: sin `style` en línea (variables vía CSSOM), sin `on*`, sin `eval`, sin `innerHTML` con datos.
8. Movimiento con `--nxgov-motion-*`, propiedades explícitas, respeta `prefers-reduced-motion`.
9. Sin JS el contenido sigue siendo usable (enlaces reales, tabla visible, `details` nativo).

## Accesibilidad por patrón
- Tabs: WAI-ARIA Tabs, activación manual, flechas/Inicio/Fin, `aria-selected`, panel enfocable, URL sincronizada.
- Tarjeta KPI: `article` con `h3`; variación con ícono + texto ("sube 24,8 % frente a 2018"), nunca solo color.
- Marco de gráfica: `figure`/`figcaption`; `iframe` con `title`; estado de carga con `aria-busy`; error con `nxgov-alert`.
- Asistente: `label` visible, región `role=log` + `aria-live=polite`, foco gestionado tras responder.

## Proceso (roles Sogas)
ARCHITECT ya fijó la API en `contracts/componentes.md` → ENGINEER construye → pide revisión a `auditor-a11y`.

## Criterios de salida
- Catálogo muestra todos los estados; 320/375/768/1024/1440 px sin desbordes.
- axe sin violaciones; teclado completo; foco visible 2px + offset 3px.
- Contrastes calculados (texto ≥ 4,5:1; no-texto ≥ 3:1) anotados en el README del bloque.
- Probado con y sin Bootstrap, y con CDN v5 cargado.
