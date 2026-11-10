---
name: tableau-embed
description: Integración de Tableau Public en el portal con Embedding API v3 (nxgov-viz), reglas de publicación de libros, inventario de vistas, diseño móvil y alternativa accesible. Úsala al inventariar, publicar o republicar libros, configurar una vista embebida o diagnosticar un tablero que no carga.
---

# Tableau Public en el portal

## Hechos que condicionan todo
- Tableau Public no exporta HTML autónomo: iframe, código de inserción y API v3 cargan desde `public.tableau.com`.
- Embedding API v3 en Tableau Public desde 2021.4: `https://public.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js`
  como `type="module"`; componente `<tableau-viz src="…" hide-tabs toolbar="bottom">`.
- `activateSheetAsync()` falla al pasar a hojas tipo Story → **no usar Stories**.
- Fuente Google Sheets → Tableau Public sincroniza una vez al día (activar "mantener datos sincronizados").
- La URL de una vista es `https://public.tableau.com/views/<Libro>/<Hoja>`: **renombrar = romper el portal**.

## Inventario (E0-D-02) — `tableau/inventario-libros.md`
| Libro | Hoja (exacta) | URL | Tipo de contenido | Filtros | ¿Móvil OK? | Serie para CSV | Camino |
|---|---|---|---|---|---|---|---|
Camino = `nativa` (barras/líneas/donas/comparativos simples) o `tableau` (exploradores, mapas, filtros múltiples).

## Integración (`nxgov-viz`)
1. La lista de vistas sale de Decap (`contracts/tableau-view.schema.json`), no del código.
2. Un `<tableau-viz>` por libro; las pestañas `nxgov-tabs` llaman `viz.workbook.activateSheetAsync(hoja)`; si falla,
   se reemplaza `src` por la URL de la hoja (respaldo).
3. Carga diferida: el script de Tableau se inyecta cuando el panel entra en pantalla (IntersectionObserver).
4. Estados: cargando (`aria-busy`, texto visible) · cargado (`nxgov:viz:loaded`) · error a los 20 s o por evento
   (`nxgov-alert` + tabla + CSV + enlace "Abrir en Tableau Public").
5. Móvil (`movil: resumen-primero`): por debajo de 768 px se muestra resumen + tabla y un botón "Ver tablero
   interactivo" que carga la vista.
6. `iframe` con `title` = título de la vista; `lang="es"` en el contenedor también en las páginas `/en/`.

## Republicar un libro (checklist para el analista)
- [ ] Mismo nombre de libro y de cada hoja publicada (comparar con el inventario).
- [ ] Sin hojas Story; dashboards con tamaño "Automático" o rango, y diseño de dispositivo "Teléfono".
- [ ] Colores de la paleta `graficas-nativas/references/paleta-nxgov.md`; texto ≥ 12 pt; títulos que dicen el hallazgo.
- [ ] Descarga de datos permitida solo si no hay datos sensibles.
- [ ] Guardar `.twbx` en `tableau/libros/<libro>-AAAA-MM-DD.twbx` y anotar en la bitácora.
- [ ] Correr el chequeo de URLs (workflow `tableau-urls`) tras publicar.

## Criterios de salida
Toda vista del inventario con camino decidido, URL verificada, serie CSV asociada y resumen; chequeo de URLs verde.
