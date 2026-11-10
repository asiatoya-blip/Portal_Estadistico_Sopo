# Decisión de modelo de experiencia — Propuesta (pendiente de aprobación del usuario)

- Fecha: 2026-10-20 · Autor: ux-ui-designer (E0-U-01) · Estudio completo: documento "Estudio UX/UI — Portal Estadístico
  de Sopó: dashboard vs. storytelling" (claude.ai/artifact/Sg3GZGCJShnsNU73uwRd5T)

## Decisión propuesta
Híbrido **martini glass con narrativa generada por plantilla**:
- **Relato guiado (arriba):** Inicio (4–6 cifras con frase, comparación, fuente, fecha) · Página de tema (3–5 hallazgos,
  selector de año, pestañas de vista) · Pregunta ciudadana (`/preguntas/<slug>/`, respuesta en la primera línea).
- **Exploración (abajo):** Indicador (tendencia, tabla, CSV, ficha técnica) · Explorador Tableau (TerriData) ·
  Datos abiertos · Seguimiento (metas del Plan de Desarrollo, filtros; el "dashboard" vive aquí).
- Frases generadas desde la hoja: `En {año}, {indicador} fue {valor}, {variación} frente a {año anterior}`.

## Evidencia (resumen)
- ONS Service Manual: no usar dashboards para hallazgos clave ni datos de actualización manual.
- NN/g: dashboards para quien ya actúa sobre las métricas; evitar donas, gauges, treemaps, 3D.
- Shao et al. 2024: historias de datos 0,889 vs 0,667 de acierto (n=103, mayoría sin formación en datos).
- Segel & Heer 2010: estructura martini glass. Peck et al. 2019: lo local primero.
- Benchmark de 25 portales: los mejor puntuados (Eurostat, ONS, OWID, Data USA, DANE, USAFacts) abren con cifras en frase
  y dejan exploración y descarga debajo; ninguno es dashboard puro.

## Patrones a evitar
Tortas > 3 porciones, donas al 100 %, anillos, treemaps, globo 3D, tema oscuro, carruseles, filtros como entrada,
periodo incompleto que cae a cero, cifras que dependen de JavaScript, Tableau/Power BI como única vía.

## Cambios que dispara (Etapa 1)
- `contracts/urls.md`: páginas de tema, pregunta y seguimiento.
- `contracts/componentes.md`: `nxgov-finding`, `nxgov-section-nav`, `nxgov-ranked-bars`, `nxgov-question-card`,
  `nxgov-freshness`, `nxgov-progress-track`; `nxgov-stat-card` con referencia y meta.
- `contracts/sheets-schema.md`: `referencia_cundinamarca`, `referencia_colombia`, `meta`, `proxima_actualizacion`,
  `periodo_parcial`.
- Decap: colección de plantillas de frases.

## Pendiente
Arquitectura de información detallada y wireframes 375/1440 px de las 7 páginas; verificación móvil de referentes con
navegador real.
