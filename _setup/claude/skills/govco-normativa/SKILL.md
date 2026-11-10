---
name: govco-normativa
description: Requisitos GOV.CO aplicables al portal (Kit UI 9.2, CDN GOV.CO v5, Resolución 1519 de 2020 anexos 1-4, Ley 1712, Ley 1581, WCAG 2.1 AA). Úsala para construir o revisar la matriz de requisitos, decidir si algo cumple, integrar componentes transversales o redactar el pie de página.
---

# Normativa GOV.CO para el portal

## Fuentes y prioridad
- Kit UI GOV.CO 9.2: `../Sogas/design_specs/kit-ui-9-2.pdf` (repo Sogas, hermano de este). Páginas ya leídas en Sogas:
  color p.8, tipografía p.12, botones p.19, etiquetas p.24.
- CDN GOV.CO v5 (`https://cdn.www.gov.co/layout-govco-v5/all.css` + `script.js`). Protocolo de extracción de snippets en
  `vendor/nxgov/CLAUDE.md` § Fuentes de verdad (los módulos lazy de la documentación, no la SPA).
- Resolución 1519 de 2020 MinTIC y sus anexos: 1 Accesibilidad (WCAG), 2 Estándares de publicación y sede electrónica,
  3 Seguridad digital, 4 Datos abiertos.
- Prioridad ante conflicto: Figma > Kit 9.2 > CDN v5; si un valor incumple WCAG AA gana el Kit y se documenta.

## Transversales del CDN v5 (se usan sin modificar)
| Componente | Regla del portal |
|---|---|
| Barra superior | Obligatoria, enlace a www.gov.co, sin estilos propios encima |
| Cabecera | Logo de la Alcaldía alojado localmente; sin login/registro |
| Barra de accesibilidad | Obligatoria; contraste vía tema `.contrast-govco` sobre tokens `nxgov`; tolerar `font-size` en línea |
| Pie de página | Estructura CDN v5; contenido del Anexo 2; mejoras de UX en contenedores `nxgov-` propios |
| Volver arriba | CDN v5; reservar espacio para no tapar contenido a 320 px |

## Contenido mínimo del pie (verificar redacción vigente en la Etapa 0)
Nombre de la entidad y del portal · dirección y código postal · horario de atención · teléfonos (conmutador, línea
gratuita / servicio a la ciudadanía, anticorrupción) · correo institucional y de notificaciones judiciales · redes
oficiales con nombre accesible · enlaces a políticas (privacidad, términos, accesibilidad), mapa del sitio, PQRSD y
sede electrónica · logos GOV.CO / Colombia según el CDN.

## Matriz de requisitos (formato del entregable E0-R-01)
| ID | Norma y numeral | Requisito | Aplica a | Cómo se prueba | Dueño | Estado |
|---|---|---|---|---|---|---|

## Errores frecuentes a vigilar
Tailwind/Font Awesome/CDN v4 cargados · clases `.govco-*` sobrescritas · pie sin datos obligatorios · iframe sin
`title` · CSV sin metadatos · enlaces externos sin aviso · cookies de terceros sin política.

## Criterios de salida
Cada requisito con prueba concreta y dueño; nada marcado "cumple" sin evidencia enlazada.
