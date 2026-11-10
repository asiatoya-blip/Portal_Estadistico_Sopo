# Inventario de libros de Tableau Public (borrador E0-D-02)

Actualizado: 2026-10-30. Fuente: códigos de inserción entregados por el usuario y prueba local con iframe + Embedding
API v3 (solo para inventariar). Decisión vigente: ADR-011 (gráficas solo por iframe).

URL de inserción para todas las hojas (ADR-011):
`https://public.tableau.com/views/<libro>/<hoja>?:showVizHome=no&:embed=y&:tabs=<y|n>&:toolbar=y&:language=es-ES`

## Libros

| Libro (ruta) | Hojas | Pestañas | Datos por API | Estado |
|---|---|---|---|---|
| `TerriData2026_sopo` | 10 | sí | 403 bloqueado | Recibido 2026-10-29 |
| `SopoDatosCuriosos2026` | 6 | sí | 403 bloqueado | Recibido 2026-10-29 |
| `EscenariosDeportivosyRecreativosdeSop2026` | 1 | no | 403 bloqueado | Recibido 2026-10-29 |
| "Acceso a Programas Sociales y Oferta Institucional" | ? | ? | ? | **Pendiente: URL** |

### TerriData2026_sopo

| Hoja | Ruta | Capítulo de la landing |
|---|---|---|
| Demografía | `TerriData2026_sopo/Demografa` | 01 Población |
| Demografía Densidad | `TerriData2026_sopo/DemografaDensidad` | 01 Población (detalle) |
| Economía Valor Agregado | `TerriData2026_sopo/EconomaValorAgregado` | 03 Economía |
| Finanzas | `TerriData2026_sopo/Finanzas` | 04 Finanzas |
| Finanzas IDF | `TerriData2026_sopo/FinanzasIDF` | 04 Finanzas |
| Educación | `TerriData2026_sopo/Educacin` | 05 Educación y salud |
| Convivencia y Seguridad Ciudadana | `TerriData2026_sopo/ConvivenciaySeguridadCiudadana` | 07 Seguridad |
| Convivencia Medidas Correctivas | `TerriData2026_sopo/ConvivenciaMedidasCorrectivas` | 07 Seguridad (detalle) |
| Ambiente | `TerriData2026_sopo/Ambiente` | Sin capítulo → propuesta "Territorio y ambiente" |
| Catastro | `TerriData2026_sopo/Catastro` | Sin capítulo → propuesta "Territorio y ambiente" |

Sin hoja en Tableau (solo tarjetas desde el Excel de TerriData): 02 Ciudad moderna (ICM) y Salud.

### SopoDatosCuriosos2026

Hojas: Generación (`Generacin`), signo (`signo`), día (`da`), día cumpleaños (`diacumpleaos`), mes cumpleaños
(`mescumpleaos`), Altitud (`Altitud`). Va en la sección "¿Sabías que…? · Datos curiosos" y en `/datos-curiosos/`.

### EscenariosDeportivosyRecreativosdeSop2026

Hoja única `Hoja1` (mapa Mapbox/OSM de escenarios). Va en 08 Programas › Deporte. Renombrar "Hoja1" antes de publicar.

## Resultados de la prueba (2026-10-29/30)

| Verificación | Resultado |
|---|---|
| Iframe con CSP estricta (`frame-src https://public.tableau.com`, sin scripts de Tableau) | Funciona en los 3 libros; `load` en 0,1–0,3 s |
| Escritorio (≈ 760 px de ancho) | Correcto en los 3 |
| Móvil (319 px de ancho útil) | **Datos curiosos ilegible**: la leyenda ocupa la mitad y el treemap queda diminuto. El mapa de escenarios y los demás no se verificaron aún con iframe a ese ancho |
| `:device=phone` en la URL | No cambia nada si el libro no tiene diseño para teléfono |
| Lectura de datos por API | 403 en los 3 libros: no hay tabla ni CSV automáticos desde Tableau |
| Imagen estática (`/static/images/…`) | PNG de 1×1 px: no sirve de respaldo ni de vista previa |
| Código de inserción entregado (`viz_v1.js`) | No se usa: `<script>` en línea, incumple la CSP |

## Pedidos al autor de los libros
1. **Diseño para teléfono** (Dashboard → Device layouts → Phone) en cada hoja o tablero, empezando por Datos curiosos.
2. Revisar en Tableau Public "Permitir acceso a los datos / descarga" si se quiere ofrecer CSV desde Tableau.
3. Nombres de hoja descriptivos (sin "Hoja1"); las URL por tablero dependen de ellos (ADR-007).
4. Fijar zoom inicial del mapa de escenarios.
5. Entregar la URL del libro "Acceso a Programas Sociales y Oferta Institucional".
6. Por cada hoja: resumen de 1 a 3 frases de lo que muestra, para la alternativa en texto (WCAG 1.1.1).
