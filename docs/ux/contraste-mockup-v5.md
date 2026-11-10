# Contraste: mockup v5 (Gemini) vs. prototipo v2 (2026-10-29)

Insumo revisado: `mockup_gemini_alpha/Mockup portal_estadistico_de_sopo v5.html` (entregado por el usuario, generado
con Gemini). Referencia vigente: `docs/ux/prototipo-v2.md` y ADR-010 (propuesto).

**Conclusión:** el v5 se usa como **inventario de contenido**, no como código ni como modelo de experiencia. Se mantiene
el v2 (landing única con capítulos, martini glass) y se incorporan del v5 las áreas de programas, el Observatorio de
Familia, los datos curiosos (con fuente) y los datos del pie, según la propuesta de la sección 4.

---

## 1. Qué aporta el v5

| Aporte | Uso propuesto | Dueño / tarea |
|---|---|---|
| 9 áreas de oferta institucional con su secretaría o instituto (tabla en § 4.1) | Estructura del libro "Acceso a Programas Sociales" y del capítulo 07 | data-analyst E0-D-01/02 · ux |
| Hojas del libro TerriData: Ambiente, Convivencia y Seguridad Ciudadana, Convivencia Medidas Correctivas, Demografía, Demografía Densidad, Economía Valor Agregado, Educación, Finanzas, Finanzas IDF | Borrador del inventario de libros; **confirmar contra el libro publicado** | data-analyst E0-D-02 |
| Desglose del IDF 2020–2024: balance fiscal primario, capacidad de ejecución de ingresos e inversión, gestión financiera, holgura | Detalle desplegable del capítulo 04 Finanzas | data-analyst (verificar en el xlsx) |
| Datos del pie de la sede: dirección, código postal, horario, NIT, DANE, líneas, correos, certificaciones ICONTEC, redes | Contenido del pie (Anexo 2) | research-normativa E0-R-03 (validar contra la sede real) |
| 6 datos curiosos | Colección "Datos curiosos" de Decap | cms-content (solo con fuente, § 4.3) |
| Desagregación por vereda (cultura, familias) | Detalle territorial en capítulos 07 y "Familias" | data-analyst (columna `vereda` en la hoja) |
| Comparativo por vigencia (selector de año) | Confirma el requisito del alcance; en v2 ya existe vía barras por año clicables | — |

### Verificación de cifras

| Cifra del v5 | Estado |
|---|---|
| Población 34.015 (2026), +24,8 % vs 2018 | Coincide con el fixture (27.249 → 34.015) |
| ICM 67,7 | Coincide (67,67 en 2024) |
| IDF 71,5 · 78,5 · 61,9 · 75,9 · 61,4 (2020–2024) | Coincide con el fixture |
| Componentes del IDF (balance, holgura, etc.) | No están en el fixture; pendiente de verificar en el xlsx |
| "Cundinamarca: 57,1" (ICM) | No está en el fixture; sin verificar |
| Todas las cifras de programas (4.850 inscritos IMRD, 1.280 FOES, 9.850 hogares, 44,2 % jefatura femenina, etc.) | **De prueba / inventadas**. No usar como reales hasta tener la Google Sheet |
| Datos curiosos (150.000 L de leche/día, 28 % de aprovechamiento, 3.250 m s. n. m., 680 ha, fundación 1653) | **Sin fuente**; varios parecen generados por el modelo |

---

## 2. Conflictos con lo decidido

### Stack y reglas de `CLAUDE.md`
- Tailwind (CDN) y Font Awesome: **prohibidos**. Chart.js en lugar de ECharts (ADR-003), cargado sin versión fija.
- Colores del mockup v4 `#004884` y `#3366CC`: **prohibidos** → Cobalt `#0943B5` y tokens.
- Chrome GOV.CO hecho a mano (barra superior, pie, barra de accesibilidad). Debe ser el CDN v5 sin modificar.
  El "alto contraste" es un `filter: invert()`; no equivale al de la barra oficial.
- CSP: `onclick`, `onerror`, `onkeyup` en línea; `<style>` y `<script>` en línea; `innerHTML` con texto de la IA
  (riesgo de XSS).
- Fuera de alcance: "Iniciar sesión / Registrarse", botones "Formularios" y "Usuario". Contacto por WhatsApp no
  previsto (los canales oficiales salen del pie y la PQRSD de la sede).

### Asistente IA (ADR-006)
- Llama a la API de Gemini desde el navegador, con la clave del lado del cliente y un prompt con cifras fijas, sin
  grounding, sin citas ni interruptor. Se mantiene el diseño del ADR-006 (Worker + Workers AI, respuesta con cita).
- En v5 es una pestaña más; en v2 es una burbuja flotante disponible en todo el recorrido. Se conservan del v5 las
  **preguntas sugeridas** como chips dentro del panel.

### Tableau (ADR-003 / ADR-009)
- El ciudadano puede escribir la URL del iframe ("Configurar enlace iframe"). Las URLs se administran en Decap y se
  embeben con la Embedding API v3; nunca editables por el visitante.
- La "vista Tableau" es HTML que imita el tablero; no hay alternativa accesible (tabla + CSV).

### Experiencia (ADR-010)
- Dashboard de 10 pestañas y 17 gráficas sin titulares que digan qué significan los números: es el patrón
  "demasiado institucional" descartado en v1.
- Tortas, donas y `polarArea` (antipatrones de `graficas-nativas`); sin etiquetas directas.
- Ninguna gráfica trae resumen, tabla, CSV, fuente ni fecha de corte (obligatorios).
- El selector de vigencia no hace nada.

### Accesibilidad (WCAG 2.1 AA)
- Pestañas sin `role="tablist"/"tab"`, `aria-selected` ni flechas de teclado.
- `<canvas>` sin alternativa textual. Botones solo con ícono y `title`. Buscador sin `<label>`.
- Contrastes que fallan:

  | Par | Contraste | Mínimo |
  |---|---|---|
  | Título del pie `#689f2c` sobre blanco | 3,19:1 | 4,5:1 |
  | Banner datos curiosos, blanco sobre amber-500 | 2,15:1 | 3:1 (texto grande) |
  | Botón WhatsApp, blanco sobre `#22c55e` | 2,28:1 | 3:1 |
  | Verde "éxito" `#008A3B` sobre blanco | 4,47:1 | 4,5:1 |

### Defectos del propio archivo
- La pestaña *Desarrollo Económico* no cierra su `<div>`: *Observatorio de Familia* queda anidada y nunca se muestra.
- `economicoFondoChart` no tiene `<canvas>`. `handleSearch`, `updateDashboardYear` y `changeFontSize` no existen.
- El logo `logo_sopo_2024_2027_1x.png` no está en el repo.

---

## 3. Qué se conserva de cada uno

| Aspecto | Se queda con | Motivo |
|---|---|---|
| Modelo de experiencia (landing con capítulos, hallazgo + cifra + detalle) | v2 | ADR-010 |
| Chrome, tokens, tipografía, componentes | v2 / `nxgov` + CDN v5 | Normativa y reglas Sogas |
| Inventario de programas y secretarías | **v5** | No existía en v2 |
| Observatorio de Familia | **v5** | Tema nuevo con peso estadístico |
| Datos curiosos | **v5** (contenido) + v2 (forma) | Solo con fuente |
| Preguntas sugeridas del asistente | **v5** | Mejoran el arranque de la conversación |
| Datos del pie | **v5** como borrador | A validar en E0-R-03 |

---

## 4. Propuesta de integración en el prototipo v2

### 4.1 Capítulo 07 "Programas" → pestañas por área (reemplaza el carrusel)

Titular: "Lo que hace la Alcaldía, en personas atendidas". Debajo, `nxgov-tabs` con un panel por área. Cada panel sigue
el martini glass: **titular-hallazgo + cifra grande + una gráfica de barras** → "Ver detalle" desplegable (tabla por
programa y por vereda, CSV, fuente y fecha) → enlace "Explorar en Tableau" a la hoja correspondiente del libro
"Acceso a Programas Sociales".

| Pestaña | Responsable | Programas (del v5) | Gráfica de vista previa |
|---|---|---|---|
| Deporte | IMRD | Escuelas de formación deportiva (por disciplina) | Línea de inscritos por año |
| Cultura | Secretaría de Cultura | Escuela Recrearte (música, danza, teatro, artes plásticas, literatura) | Barras por área artística |
| Educación | Secretaría de Educación | Estímulos FOES, transporte escolar, EducaTIC | Barras por modalidad FOES |
| Ciencia y tecnología | Secretaría de CTI | Semilleros de robótica, energía solar fotovoltaica, acompañamiento a proyectos | Barras por programa |
| Salud | Secretaría de Salud | Manipulación de alimentos, bioseguridad, Sopó Escucha | Barras agrupadas por trimestre |
| Desarrollo social | Secretaría de Desarrollo Social | Adulto mayor, discapacidad, mujer y género, juventud | Barras por población |
| Desarrollo económico | Secretaría de Desarrollo Económico | Sopó Emprende, asistencia técnica agropecuaria | Línea de inversión por año |

Por qué pestañas y no carrusel: siete áreas con cifras comparables se leen mejor como pestañas operables con teclado
(patrón ARIA conocido) que como carrusel; además se elimina `nxgov-carousel` de la lista de componentes de ADR-010
(un componente menos que construir y auditar). La pestaña activa queda en la URL (`/#programas-cultura`) para
compartir y medir (ADR-007).

### 4.2 Capítulo nuevo "Familias de Sopó" (Observatorio de Familia)

Ubicación: después de 05 Educación y salud (es contexto social, antes de Seguridad).
- Titular-hallazgo según el dato real (p. ej. "Casi la mitad de los hogares tiene a una mujer al frente", si la cifra
  se confirma).
- Cifra grande: hogares caracterizados. Vista previa: tipologías de hogar en **barras horizontales** (no dona).
- Detalle desplegable: familias por vereda y participación por programa (Crianza Amorosa, seguridad alimentaria,
  apoyo psicosocial, vínculos, vivienda rural), con tabla y CSV.
- Requiere confirmar con la entidad que el Observatorio publica estos datos y bajo qué fuente oficial.

### 4.3 Datos curiosos

- Forma: tarjetas "¿Sabías que?" (`nxgov-fact-card`, ya previsto) intercaladas **una por capítulo** cuando el dato
  tenga relación temática (lácteos → Economía; Pionono → Ambiente; reciclaje → Ambiente; Arcángeles → Cultura), más
  la página `/datos-curiosos/` de `contracts/urls.md` con todas.
- Regla: cada tarjeta lleva fuente y fecha (ADR-004). Ninguno de los 6 textos del v5 se publica sin verificar; se
  cargan en Decap como borrador con el campo fuente vacío para que la entidad lo complete.
- Contraste: nada de blanco sobre amarillo; usar `crema-calida` con texto `#6B4E00` (7,1:1, ADR-010).

### 4.4 Orden resultante de la landing

Hero · Sopó hoy · 01 Población · 02 Ciudad moderna · 03 Economía · 04 Finanzas (con desglose IDF) · 05 Educación y
salud · **06 Familias de Sopó** · 07 Seguridad · **08 Programas (pestañas por área)** · 09 Explorar a fondo · Datos
abiertos · Asistente (burbuja, con preguntas sugeridas).

### 4.5 Impacto en otros documentos (requiere aviso a sus dueños)

| Documento | Cambio propuesto | Dueño |
|---|---|---|
| ADR-010 | Capítulos 06 y 08 nuevos o cambiados; quitar `nxgov-carousel`; `nxgov-tabs` dentro de capítulo | architect |
| `contracts/sheets-schema.md` | Pestaña `Series_programas` con columnas `area`, `responsable`, `programa`, `indicador`, `vereda`, `periodo`, `valor`, `unidad`, `fuente`, `fecha_corte`; pestaña `Series_familia` | architect + data-analyst |
| `contracts/urls.md` | Anclas `#familias` y `#programas-<area>` | architect |
| `tableau/inventario-libros.md` | Hojas del libro TerriData listadas en § 1 como borrador | data-analyst |
| `docs/normativa/cdn-v5-transversales.md` | Datos del pie del v5 como borrador a validar | research-normativa |
| `docs/ux/prototipo-v2.md` | Actualizar el prototipo (v2.1) si el usuario aprueba esta propuesta | ux-ui-designer |

## Decisiones del usuario
1. ✅ 2026-10-29 — Aprobado: pestañas por área en lugar del carrusel (§ 4.1). Aplicado en el prototipo v2.1.
2. ✅ 2026-10-29 — Aprobado: Observatorio de Familia como capítulo propio "Familias de Sopó" (§ 4.2). Aplicado en v2.1.
3. ⏳ Pendiente: quién en la entidad entrega las fuentes de los datos curiosos y confirma los datos del pie.
4. ➕ 2026-10-29 — El usuario agregó el tablero "Escenarios Deportivos y Recreativos de Sopó 2026" a la pestaña
   Deporte. Resultado de la prueba en `docs/ux/prototipo-v2.md` § v2.1.
