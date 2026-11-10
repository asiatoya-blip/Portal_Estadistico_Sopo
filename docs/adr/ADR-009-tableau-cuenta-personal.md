# ADR-009 — Tableau Public con cuenta personal; extracción completa desde la publicación pública

- Fecha: 2026-10-20 · Estado: Aprobado (decisión del usuario: no es posible una cuenta institucional)

## Contexto
Los 2 libros ("Indicadores Territorial TerriData" y "Acceso a Programas Sociales y Oferta Institucional") están en
una cuenta personal de Tableau Public. No habrá cuenta institucional.

## Decisión
1. El portal sigue embebiendo las vistas públicas de esa cuenta (Embedding API v3).
2. Se **extrae todo lo reutilizable de la publicación pública** y se versiona en el repo:
   - libro `.twbx` (si la descarga está habilitada en el perfil) → `tableau/libros/`;
   - datos de cada hoja ("Descargar → Datos / Tabla cruzada") → `tableau/extraccion/<libro>/<hoja>.csv`;
   - capturas PNG de cada vista y la lista de hojas con URL → `tableau/inventario-libros.md`.
3. Toda vista que se pueda reproducir con `nxgov-chart` a partir de la Google Sheet se reproduce como nativa
   (reduce la dependencia de la cuenta personal); Tableau queda para los exploradores complejos.
4. Acta de custodia: quién es titular, quién tiene acceso de respaldo y qué pasa si la persona deja la entidad.

## Consecuencias
La pérdida de la cuenta deja de ser crítica: los datos están en la hoja y en el repo, y las vistas complejas se pueden
republicar desde los `.twbx` en otra cuenta cambiando solo las URLs en Decap. Riesgo residual: cambios en el perfil
personal (renombrar, ocultar, desactivar descarga) → chequeo nocturno de URLs + avisos.
