---
name: auditoria-wcag
description: Auditoría independiente de accesibilidad WCAG 2.1 AA y Anexo 1 de la Resolución 1519 para el portal, automática y manual, con informe y evidencias. Úsala para auditar un componente, una página o el sitio completo, o para preparar la certificación de accesibilidad.
---

# Auditoría WCAG 2.1 AA

Independencia: no audites lo que construiste. Reporta; no corrijas código ajeno.

## Automática (cada PR de componentes y sitio)
- axe-core (Playwright) y Pa11y CI sobre el catálogo y todas las páginas generadas, en 320 y 1440 px.
- Lighthouse accesibilidad ≥ 95.
- Validador HTML (nu) sin errores.
- Contraste: calcular pares de tokens con la fórmula de luminancia relativa (como en Sogas) y registrar ratios.

## Manual (Etapa 4, y por componente nuevo)
| Prueba | Criterios WCAG |
|---|---|
| Solo teclado: orden, foco visible, sin trampas (incluido el iframe de Tableau), atajos de pestañas | 2.1.1, 2.1.2, 2.4.3, 2.4.7 |
| NVDA + Firefox y NVDA + Chrome (y VoiceOver iOS en móvil): encabezados, regiones, nombres, estados, anuncios | 1.3.1, 4.1.2, 4.1.3 |
| Zoom 200 % y reflujo a 320 px CSS (400 %) | 1.4.4, 1.4.10 |
| Barra de accesibilidad GOV.CO: +5/−5 de texto y contraste | 1.4.4, 1.4.12 |
| Gráficas: alternativa textual, tabla, sin color como único medio | 1.1.1, 1.4.1, 1.4.11 |
| `prefers-reduced-motion`, `forced-colors` | 2.3.3 (buena práctica), 1.4.11 |
| Idioma de página y de partes (`lang="es"` en tableros dentro de `/en/`) | 3.1.1, 3.1.2 |
| Formularios (buscador, asistente): etiquetas, errores, instrucciones | 1.3.1, 3.3.1, 3.3.2 |
| Enlaces y títulos de página únicos y descriptivos | 2.4.2, 2.4.4 |
| Contenido de terceros (Tableau): documentar lo que no controlamos y la alternativa ofrecida | 1.1.1 |

## Informe (`audits/a11y/AAAA-MM-DD-<alcance>.md`)
| ID | Criterio | Página/componente | Severidad (bloqueante/alta/media/baja) | Evidencia | Dueño | Estado |
Severidad bloqueante = impide completar una tarea con teclado o lector, o falla un criterio A/AA sin alternativa.

## Criterios de salida (puerta 4)
Cero bloqueantes y cero altas abiertas · lista de chequeo del Anexo 1 completa con evidencia · informe firmado.
