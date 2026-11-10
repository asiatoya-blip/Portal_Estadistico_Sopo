# Prototipo visual v2 — landing única (2026-10-20)

Lienzo: "Prototipo Portal Estadístico de Sopó" (claude.ai/artifact/9xAnrmEV6cQAuwtRALB7oB), fila "v2".
Decisión: ADR-010 (propuesto). Datos: TerriData (DNP) de `data_base/TerriData25758f.xlsx`, extraídos en
`data/fixtures/terridata-sopo.json`; programas municipales = datos de prueba del mockup v4 (marcados).

| Capítulo | Titular-hallazgo | Interacción |
|---|---|---|
| Hero (azul crema) | "Sopó, contado con datos." · 34.015 habitantes 2026 | CTA al recorrido y a descargas |
| Sopó hoy (Cobalt) | 34.015 · 66 % urbano · ICM 67,7 · $1,28 bill. valor agregado | — |
| 01 Población | "Sopó crece: 6.766 personas más desde 2018" | Barras por año clicables (2018–2030, proyección punteada) que reescriben cifra y frase; grupos de edad desplegables |
| 02 Ciudad moderna | "Fuerte en equidad y gobernanza; la productividad es el reto" | Barras 0–100 estilo Spotify |
| 03 Economía (crema) | "La industria mueve 63 de cada 100 pesos…" | Años 2012/2018/2023 en barra apilada; detalle desplegable (valor agregado y cosechas) |
| 04 Finanzas | "El desempeño fiscal bajó a 61,4 en 2024" | Línea con etiquetas directas sobre azul noche |
| 05 Educación y salud | Cambia con la pestaña | Pestañas Educación / Salud |
| 06 Seguridad (azul noche) | "El hurto a personas bajó 65 % desde su pico de 2022" | Barras con pico y último año resaltados |
| 07 Programas | "Lo que hace la Alcaldía, en personas atendidas" | Carrusel horizontal de tarjetas |
| 08 Explorar a fondo | "¿Quieres cruzar los datos tú mismo?" | Tarjetas que abren Tableau en panel de pantalla completa |
| Datos abiertos (Cobalt) | "Los datos son tuyos" | Descarga CSV, historial |
| Asistente | Burbuja flotante | Abre panel con pregunta y respuesta citada |

---

## v2.1 (2026-10-29) — aprobada por el usuario

Origen: `docs/ux/contraste-mockup-v5.md` (§ 4). Mismo lienzo, artboards "v2.1 · Landing única" (escritorio y móvil).

| Cambio | Detalle |
|---|---|
| Logo oficial | `design_specs/logo_sopo_2024_2027_1x - copia.png` (recortado sin el marco) en cabecera y pie; reemplaza el marcador "Escudo". Texto "Portal Estadístico" al lado, separado por filete Cobalt |
| **06 Familias de Sopó** (nuevo, fondo blanco) | "Casi la mitad de los hogares tiene a una mujer al frente" · 44,2 % jefatura femenina · 9.850 hogares · 4.120 familias en programas · tipos de hogar en barras horizontales (monoparental con jefa en coral) · desplegable "Ver las 7 zonas y los programas" (hogares por vereda + familias por programa) |
| 07 Seguridad | Solo cambia de número |
| **08 Programas** (cambiado) | Carrusel reemplazado por 7 pestañas (`role="tablist"`): Deporte, Cultura, Educación, Ciencia y tecnología, Salud, Desarrollo social, Desarrollo económico. Cada panel: responsable · titular-hallazgo · cifra grande · barras horizontales con valor · fuente · "Ver detalle" (tabla) · "Explorar en Tableau" · "Descargar CSV" |
| Deporte: mapa de escenarios | Bloque "¿Dónde puedes hacer deporte en Sopó?" con vista previa del tablero de Tableau "Escenarios Deportivos y Recreativos de Sopó 2026", botón "Abrir el mapa" (panel de pantalla completa) y "Ver la lista de escenarios" (alternativa accesible) |
| 09 Explorar a fondo | Solo cambia de número |

Todas las cifras de 06 y 08 son **datos de prueba del mockup v5** y están marcadas así en el lienzo.

Pendiente para la construcción (no se puede mostrar en el lienzo): flechas izquierda/derecha e Inicio/Fin entre pestañas
con `tabindex` itinerante, pestaña activa en la URL (`#programas-deporte`) y tabla real con `nxgov-data-table`.

### Prueba del tablero "Escenarios Deportivos y Recreativos de Sopó 2026" (2026-10-29)

Página de prueba local con Embedding API v3 (`<tableau-viz>`), servida en `localhost`.

| Verificación | Resultado |
|---|---|
| Carga | Funciona. `firstinteractive` en 3,0 s (en caché) y 11,6 s (en frío) |
| Estructura | 1 libro · 1 hoja (`Hoja 1`, worksheet, tamaño automático) · sin filtros · tipo mapa (Mapbox/OSM) con un ícono por escenario |
| Lectura de datos por API (`getSummaryDataReaderAsync`, `getSummaryDataAsync`, `getUnderlyingTablesAsync`) | **403 PermissionDenied**. No se puede generar la tabla alternativa ni el CSV desde Tableau |
| Imagen estática (`/static/images/…/1.png` y `1_rss.png`) | Devuelve un PNG de 1×1 px: el respaldo `noscript` del código de inserción no muestra nada |
| Móvil (375 px) | Se ve el municipio completo y los íconos son legibles |
| Escritorio | En una carga abrió con el zoom sobre un sector (Centro Alto); en otra, el casco urbano completo. Conviene fijar el zoom inicial al publicar |
| Código de inserción entregado | Usa `viz_v1.js` (API antigua) y `<script>` en línea con `style` por JS: incumple la CSP y ADR-003. Se reemplaza por `<tableau-viz>` de la API v3 dentro de `nxgov-viz` |

Consecuencias:
1. La lista de escenarios (nombre, tipo, vereda, dirección, coordenadas) debe venir de la **Google Sheet** (`Series_escenarios`), no de Tableau. Es obligatoria como alternativa al mapa (WCAG 1.1.1) y como CSV abierto.
2. La vista previa del mapa (imagen) la genera el pipeline o se carga en Decap; no se puede depender de la imagen estática de Tableau Public.
3. Revisar en Tableau Public si el libro tiene desactivada la descarga o el acceso a datos (pendiente de ADR-009: "descarga habilitada en el perfil").
4. Nombre de la hoja: renombrar "Hoja 1" a algo descriptivo antes de publicar (aparece en la URL por tablero de ADR-007).
