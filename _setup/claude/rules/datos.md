---
paths:
  - "scripts/data/**"
  - "data/**"
  - "tableau/**"
---

# Reglas al tocar datos
- Usa `sheets-data-pipeline` y `metadatos-estadisticos`. `data/` lo escribe solo el workflow; no se edita a mano
  (excepto `data/fixtures/`).
- Ninguna cifra sin fuente ni fecha de corte; conteos < 5 se suprimen.
- No renombrar libros ni hojas de Tableau publicados.
