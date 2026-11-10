# Paleta del portal (instancia nxgov del método dataviz)

Sustituye a la paleta de referencia del método. Superficie de gráficas: blanco `#FFFFFF` (GOV.CO no usa modo oscuro;
el alto contraste lo da `.contrast-govco`).

## Categórica (orden fijo; validada 2026-10-20)
| Slot | Hex | Origen |
|---|---|---|
| 1 | `#0943B5` | Cobalt (primario Kit 9.2) |
| 2 | `#EB6834` | naranja de referencia |
| 3 | `#1BAF7A` | aguamarina de referencia |
| 4 | `#EDA100` | amarillo de referencia |
| 5 | `#E87BA4` | magenta de referencia |
| 6 | `#008300` | verde de referencia |
| 7 | `#6250D6` | violeta de referencia |
| 8 | `#A80521` | rojo error Kit/CDN |

Resultado del validador (`--mode light --surface #ffffff`): banda de luminosidad PASS · croma PASS · separación CVD
adyacente PASS (peor ΔE 9,1) · piso visión normal PASS (peor ΔE 19,6) · **contraste WARN** en slots 3, 4 y 5
(2,82 / 2,17 / 2,69 : 1) → regla de alivio: etiquetas visibles o tabla (en el portal la tabla siempre existe).
Para gráficas de dispersión/small multiples (todos los pares) limitar a 3 series. El `data-analyst` re-valida si
cambia algún valor.

## Secuencial (un tono: Cobalt, claro → oscuro)
`#E5ECF8` (Solitude) · `#B5C7E9` (Tropical Blue) · `#4672C8` (Havelock) · `#0943B5` (Cobalt) · pasos intermedios y
más oscuros: los calcula y valida el `data-analyst` en la Etapa 1 (monotonía de luminosidad).

## Divergente
Cobalt `#0943B5` ↔ rojo `#A80521`, punto medio gris `#F4F4F4`. Mismo número de pasos por brazo.

## Estado (reservado; siempre con ícono + texto)
| Rol | Relleno/borde | Texto sobre blanco |
|---|---|---|
| Bueno | `#158361` | `#0D684B` |
| Advertencia | `#FDAA29` | `#806000` |
| Crítico | `#A80521` | `#A80521` |

## Tinta y ejes
| Rol | Hex |
|---|---|
| Texto primario | `#000000` |
| Texto secundario | `#4C4C4C` |
| Ejes / línea base | `#7E7E7E` (3,7:1) |
| Rejilla | `#E2E8F0` |
| Borde de tarjeta | `#B9B9B9` |

## Alto contraste (`.contrast-govco`) y `forced-colors`
Series con `decal` obligatorio y bordes 2px; colores del sistema en `forced-colors`. Lo define el `data-analyst`
con el `engineer-components` en la Etapa 2 y lo valida `auditor-a11y`.
