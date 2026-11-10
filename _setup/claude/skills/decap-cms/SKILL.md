---
name: decap-cms
description: Configuración de Decap CMS (admin/config.yml) para el portal, colecciones, flujo editorial, OAuth con GitHub vía Cloudflare Worker, vista previa y guía del editor. Úsala al crear o cambiar colecciones, campos, validaciones o la documentación para el editor.
---

# Decap CMS del portal

Decisión: ADR-004. Los datos numéricos NO están en el CMS (viven en Sheets, ADR-002).

## Configuración base (`admin/config.yml`)
```yaml
backend:
  name: github
  repo: <org>/Portal_Estadistico_sopo
  branch: main
  base_url: https://<worker-oauth>.workers.dev   # workers/oauth (devops)
publish_mode: editorial_workflow                 # borrador → en revisión → listo
locale: es
media_folder: src/site/assets/uploads
public_folder: /assets/uploads
```
Cargar Decap desde el propio dominio (copia fijada por versión y hash) para cumplir la CSP; `/admin/` con CSP ampliada
solo para la API de GitHub (`contracts/csp.md`).

## Colecciones (cada una valida contra su contrato)
| Colección | Archivo(s) | Contrato | Campos clave |
|---|---|---|---|
| Páginas | `content/paginas/*.md` (es/en) | — | título, resumen, cuerpo, idioma |
| Vistas Tableau | `content/tableau/*.json` | `tableau-view.schema.json` | libro, hoja exacta, URL, resumen, serie CSV, orden, visible |
| Gráficas nativas | `content/graficas/*.json` | `chart-config.schema.json` | tipo, serie, eje, título-hallazgo, resumen |
| Fichas técnicas (textos) | `content/fichas/*.md` | `metadatos-estadisticos` | definición ampliada, notas |
| Datos curiosos | `content/curiosos/*.md` | — | título, texto, **fuente obligatoria**, fecha |
| Ajustes | `content/ajustes.json` | — | interruptor asistente, aviso global, enlaces de la sede |

Usa `pattern`, `required`, `hint` y widgets `select` para que el editor no pueda guardar valores inválidos. Los
nombres de campos y ayudas en español claro (`lenguaje-claro`).

## Vista previa
Plantillas de previsualización que cargan `nxgov.css` para que el editor vea el resultado real; además, cada PR
del flujo editorial genera vista previa en Cloudflare Pages.

## Guía del editor (`docs/manuales/guia-editor.md`)
Tareas con capturas: actualizar datos del mes (en Sheets) · publicar ahora · cambiar un texto · agregar una vista de
Tableau · ocultar una gráfica · apagar el asistente · revertir un cambio. Máximo 1 página por tarea.

## Criterios de salida
Un editor sin experiencia en Git completa cada tarea de la guía sin ayuda · validaciones impiden guardar campos
obligatorios vacíos · la configuración también abre en Sveltia CMS (plan B).
