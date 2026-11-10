# Diagnóstico de diseño y funcionalidad — 2026-11-10

Objeto: prototipo v3 "Tablero" (lienzo, 2026-11-03), maqueta alpha v5 del cliente, contratos y ADR vigentes, y los
códigos de inserción de Tableau entregados hoy. Aún no hay código del sitio.

Revisores (independientes, sin editar archivos): `ecc:a11y-architect` (WCAG 2.1 AA / Res. 1519 anexo 1),
`ecc:security-reviewer` (inserción de Tableau, CSP, privacidad), `ecc:architect` (coherencia y alcance) y crítica de
diseño con Impeccable (modo Operate). No se probó con NVDA ni se midieron las cookies de Tableau.

Decisiones del usuario tomadas en esta revisión: **cifras + tableros** como única ventana (asistente y datos abiertos
pasan a enlaces); **Programas Sociales oculto** hasta tener URL; visitante = ciudadanía y funcionarios por igual;
entrega = repositorio en GitHub publicado con GitHub Pages.

## 1. Bloqueantes (se corrigen antes de construir)

| # | Hallazgo | Fuente | Corrección |
|---|---|---|---|
| B1 | Los códigos de Tableau entregados usan `viz_v1.js`, `<script>` y `style` en línea: incompatibles con la CSP y con ADR-011 | seguridad, a11y | Iframe directo `public.tableau.com/views/<libro>/<hoja>?:showVizHome=no&:embed=y&:tabs=…&:language=es-ES`, `title` por hoja, `sandbox="allow-scripts allow-same-origin allow-popups"` (a verificar), `referrerpolicy="strict-origin"` |
| B2 | Tableau es un tercero que puede poner cookies; ADR-007 promete "sin cookies" | seguridad | El iframe se crea solo tras clic en "Cargar tablero", con aviso de tercero; ajustar texto de ADR-007 y política de tratamiento |
| B3 | 16 de 17 hojas sin resumen en texto (`[Resumen de la hoja…]`); el iframe no es accesible por dentro | a11y, architect | Resumen de 1–3 frases por hoja, obligatorio en Decap. Bloquea el lanzamiento (WCAG 1.1.1) |
| B4 | Textos de Programas Sociales son datos de prueba de la maqueta | architect | Sección oculta hasta tener libro y textos reales (decidido) |
| B5 | Pestañas no seleccionadas con borde `#B5C7E9` (1,7:1) | a11y | Borde ≥3:1 (`#7E8BA6` o más oscuro) — WCAG 1.4.11 |
| B6 | Tablists sin flechas, Inicio/Fin ni `tabindex` itinerante; 10 pestañas que se envuelven en 2 filas | a11y | Lista de enlaces con anclas (funciona sin JS) en vez de pestañas ARIA para 10+ opciones |
| B7 | "Hurto sube" usa la misma flecha azul que una mejora | a11y, architect | Dirección en texto + valoración aparte (favorable/desfavorable); campo `sentido_positivo` en `tarjetas.yml` |
| B8 | Espejo en GitHub Pages no aplica `_headers` (sin CSP/HSTS por cabecera) | seguridad, architect | En Pages: CSP por `<meta http-equiv>` (sin `frame-ancestors`). Producción sigue en Cloudflare Pages |

## 2. Diseño (crítica Impeccable, modo Operate)

| Problema en v3 | Por qué importa | Propuesta |
|---|---|---|
| 4 franjas de navegación antes del contenido (barra GOV.CO, cabecera, barra del portal oscura, nav de secciones) | El primer dato aparece a ~300 px; compite con el chrome oficial | Una sola cabecera propia bajo el chrome GOV.CO; la fecha de corte va junto al título |
| Cada sección con su propio mundo (navy, amarillo, cobalto lleno, blanco) | Se lee como 5 sitios distintos; nada es jerarquía | Un fondo, un tipo de superficie, color solo para estado y acción |
| Pastillas para todo (chips, pestañas, botones, etiquetas) | No se distingue qué es control y qué es etiqueta | Botones = acción; enlaces subrayados = navegación; etiquetas sin forma de botón |
| Etiquetas en MAYÚSCULAS 12 px, fuente 12 px | Lectura difícil; lectores deletrean | 14 px mínimo en caja normal |
| h1 "Sopó en cifras" | La página no tiene título propio | h1 "Portal Estadístico de Sopó" |
| Asistente como bloque azul de página completa | Compite con los tableros, que son el producto | Enlace en la cabecera (decidido) |
| Iframes de altura fija (460 px) | Datos curiosos ilegible a 319 px | `aspect-ratio` por hoja + "Abrir en Tableau Public" como salida en móvil |

## 3. Coherencia documental (architect)

Desactualizados frente a ADR-011/012: `contracts/chart-config.schema.json` (borrar), `kpi.schema.json`,
`sheets-schema.md` (→ esquema del Excel TerriData), `tableau-view.schema.json` (3 libros, `tabs`, CSV opcional),
`componentes.md` (`nxgov-viz` = iframe), `urls.md` (una página con anclas), `csp.md` (quitar Tableau de
`script-src`/`connect-src`/`img-src`, quitar jsDelivr, añadir `object-src 'none'`), ADR-002 (marcar reemplazado),
ADR-004, ADR-009 ("2 libros", API v3), `etapas.md` (Sheet, gráficas nativas) y `CLAUDE.md` (alcance, pendientes,
skill `graficas-nativas`). Inconsistencia: ADR-011 §4 habla de "Familias" sin libro.

Recorte de alcance propuesto (requiere ADR-013 y aprobación): salen asistente IA (ADR-006), contador propio +
exportación a Sheets (ADR-007 queda en Cloudflare Web Analytics), i18n en/es, búsqueda Pagefind (una sola página).
Se mantienen: pipeline del Excel, Decap con 4 colecciones, historial de actualizaciones.

## 4. Pendientes de la entidad

Resúmenes de las 17 hojas · renombrar `Hoja1` del libro de escenarios · diseño para teléfono en Tableau (Datos
curiosos) · URL de Programas Sociales · dominio `.gov.co` · organización GitHub · acta de custodia de Tableau.
Ya no aplica: compartir la Google Sheet.

## 5. CSP recomendada (página pública)

```
default-src 'self'; script-src 'self' https://cdn.www.gov.co https://static.cloudflareinsights.com;
style-src 'self' https://cdn.www.gov.co; font-src 'self' https://cdn.www.gov.co; img-src 'self' data: https://cdn.www.gov.co;
frame-src https://public.tableau.com; connect-src 'self' https://cloudflareinsights.com; object-src 'none';
frame-ancestors 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests
```
