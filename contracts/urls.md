# Mapa de URLs — Propuesta v0

Español en la raíz, inglés bajo `/en/` (solo interfaz; tableros y datos en español con `lang="es"`).

| Página | es | en |
|---|---|---|
| Inicio (KPIs + accesos) | `/` | `/en/` |
| Tableros por libro | `/tableros/terridata/` · `/tableros/programas-sociales/` | `/en/dashboards/…` |
| Una vista (pestaña con URL propia) | `/tableros/<libro>/<slug-vista>/` | `/en/dashboards/<libro>/<slug>/` |
| Ficha de indicador | `/indicadores/<id>/` | `/en/indicators/<id>/` |
| Historial de actualizaciones | `/historial/` | `/en/history/` |
| Datos abiertos (CSV) | `/datos-abiertos/` | `/en/open-data/` |
| Datos curiosos | `/datos-curiosos/` | `/en/fun-facts/` |
| Asistente | `/asistente/` | `/en/assistant/` |
| Uso del portal | `/uso-del-portal/` | `/en/portal-usage/` |
| Accesibilidad · Privacidad · Mapa del sitio | `/accesibilidad/` · `/privacidad/` · `/mapa-del-sitio/` | `/en/…` |
| CSV | `/datos/csv/<serie_id>.csv` | (mismo archivo) |

Cada pestaña es un enlace real (funciona sin JS); con JS, `nxgov-tabs` cambia de panel y actualiza la URL.
