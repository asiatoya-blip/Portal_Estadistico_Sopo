---
name: ux-portales-datos
description: Método de investigación y diseño UX/UI para portales de datos públicos y estadísticos (benchmark global, evaluación heurística, modelo dashboard vs. storytelling, arquitectura de información, patrones de visualización accesibles bajo GOV.CO). Úsala para estudios de mercado de portales de datos, decidir el modelo de experiencia, definir recorridos y wireframes, o revisar una propuesta de interfaz del portal.
---

# UX/UI de portales de datos públicos

## 1. Antes de diseñar: a quién sirve el portal
Define 3–5 perfiles con su tarea principal y nivel de alfabetización de datos. Para un portal municipal típico:
| Perfil | Tarea | Alfabetización de datos | Dispositivo |
|---|---|---|---|
| Ciudadanía | "¿Cómo va mi municipio en X?" | baja | móvil |
| Periodista / veeduría / concejal | Verificar y citar una cifra | media | escritorio y móvil |
| Funcionario / secretaría | Seguir indicadores de su programa | media-alta | escritorio |
| Investigador / academia | Descargar datos y metadatos | alta | escritorio |
Cada decisión de interfaz se justifica contra estas tareas.

## 2. Benchmark (estudio de mercado)
**Muestra mínima:** 15 portales, en 3 grupos: (a) oficinas estadísticas y organismos internacionales, (b) ciudades y
gobiernos locales, (c) referentes de storytelling de datos (prensa, ONG, corporativos). Incluir al menos 4 de
Colombia/Latinoamérica.

**Ficha por portal** (`references/ficha-benchmark.md`): URL · tipo · público · modelo de experiencia
(dashboard / narrativa / híbrido / catálogo) · página de inicio (qué se ve primero) · navegación (por tema, territorio,
indicador, pregunta) · cómo muestra un indicador (cifra, tendencia, comparación, contexto) · gráficas y alternativa
accesible · descarga y metadatos · móvil · lenguaje · qué tomar · qué evitar.

**Puntuación** 1–5 en 8 criterios (`references/criterios.md`) y ranking. Fuente primaria: visitar el portal; citar URL
y fecha. No puntuar lo que no se pudo ver.

## 3. Evidencia a revisar
- Modelos narrativos de visualización: Segel & Heer (2010) "Narrative Visualization" (estructura *martini glass*:
  guía del autor → exploración del lector); "explorable explanations".
- Guías de gobiernos para gráficas y estadísticas: GOV.UK / Analysis Function (UK), ONS, Statistics Canada,
  ABS, Eurostat "Statistics Explained", guías de accesibilidad de datos.
- Investigación de usabilidad sobre dashboards, cifras clave y alfabetización de datos (NN/g, Datawrapper, etc.).
- Contexto Colombia: DANE, TerriData (DNP), datos.gov.co, Kit UI 9.2, Res. 1519.

## 4. Decisión de modelo de experiencia
Evalúa al menos: **dashboard SaaS** (todo a la vista, filtros), **storytelling** (secciones guiadas con cifra +
explicación), **híbrido martini glass** (relato arriba, exploración abajo), **catálogo** (lista de conjuntos). Matriz
modelo × perfil (¿resuelve su tarea?) + riesgos (carga cognitiva, móvil, accesibilidad, mantenimiento por un solo
editor). La recomendación cita evidencia del benchmark, no gusto.

## 5. Patrones obligatorios en el portal (GOV.CO + WCAG)
- Cada cifra: título que dice el hallazgo, valor, unidad, comparación con texto, fuente y fecha de corte.
- Cada gráfica: resumen textual, tabla y CSV; nunca color como único medio; etiquetas directas antes que leyendas.
- Navegación por pregunta o tema con URL propia; nada importante solo dentro de un iframe.
- Móvil primero: una columna, cifras antes que gráficas, gráficas simples; exploradores complejos detrás de un botón.
- Animación solo para mostrar cambios causados por el usuario; respeta `prefers-reduced-motion`.
- El aspecto lo dicta el Kit UI 9.2 y la librería `nxgov`; la "personalidad" sale del contenido (Sopó), no de
  romper el Kit.

## 6. Entregables
`docs/ux/benchmark.md` (fichas + ranking) · `docs/ux/decision-modelo.md` (matriz y recomendación, como ADR) ·
`docs/ux/arquitectura-informacion.md` (mapa del sitio, recorridos por perfil) · `docs/ux/wireframes/` (ASCII o
Figma por página, móvil y escritorio) · lista de componentes nuevos o cambiados para el `architect`.

## Criterios de salida
≥ 15 portales fichados con URL y fecha · recomendación trazable a evidencia · wireframes de inicio, tema, indicador y
datos abiertos en 375 px y 1440 px · revisión de `auditor-a11y` sobre los wireframes.
