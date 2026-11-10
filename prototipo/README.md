# Propuesta: Portal Estadístico de Sopó (página única por temas)

Prototipo estático de la "ventana sencilla" aprobada el 2026-11-10: barra de 8 temas con su cifra, y por tema la
cifra con fuente y su tablero de Tableau Public. Se publica en GitHub Pages con `.github/workflows/pages.yml`.

- Contenido: `temas.json` (cifras verificadas contra `data/fixtures/terridata-sopo.json`; resúmenes por hoja).
- Generar: `python prototipo/build.py` → `index.html`. Sin dependencias.
- Tableau: iframe directo, creado solo al pulsar "Cargar el tablero" (aviso de tercero). Sin `viz_v1.js`.
- CSP por `<meta>` (GitHub Pages no aplica `_headers`). Producción: Cloudflare Pages con `_headers`.
- Las barras GOV.CO están simuladas; en producción las pone el CDN GOV.CO v5 sin modificar.
- Pendiente de la entidad: 13 resúmenes de hoja, URL de Programas Sociales, confirmar qué cambios son
  favorables/desfavorables por indicador.
