---
paths:
  - "src/components/**"
  - "src/catalogo/**"
  - "src/styles/**"
---

# Reglas al tocar componentes y estilos
- Usa la skill `nxgov-component-builder`. Prefijo `nxgov-`, BEM, solo tokens `--nxgov-*`, sin `!important`.
- Nada de selectores de etiqueta globales ni clases del CDN/Bootstrap dentro de un bloque.
- Sin `style` en línea, `on*`, `eval` ni `innerHTML` con datos (CSP).
- `vendor/nxgov/` es solo lectura.
