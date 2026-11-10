---
name: asistente-ia-grounded
description: Construcción y evaluación del asistente IA del portal sobre Cloudflare Workers AI, restringido a datos oficiales con citas, límites de uso, privacidad e interruptor. Úsala al trabajar en workers/assistant/, el componente nxgov-assistant o el set de evaluación.
---

# Asistente IA con respuestas solo desde datos oficiales

Decisión: ADR-006. Contrato: `contracts/asistente-api.md`.

## Arquitectura
```
nxgov-assistant ──POST /api/asistente──▶ Worker
   ├─ límite por visitante (KV/Durable Object, ventana deslizante; sin guardar IP en claro: hash con sal diaria)
   ├─ caché de preguntas frecuentes (normalizadas)
   ├─ recuperación: índice de data/kpis.json, data/series/*.json, data/fichas.json (embebido en el build del Worker)
   ├─ prompt de sistema: responde SOLO con el contexto; si no está, dilo; cita id, fuente y fecha de corte
   ├─ Workers AI (modelo de texto del catálogo con buen español; elegir y fijar versión en la Etapa 1)
   └─ verificación posterior: toda cifra de la respuesta debe existir en las citas → si no, respuesta "sin_datos"
```
Cupo gratuito: 10.000 neuronas/día; al agotarse responde 503 con mensaje útil y enlaces a tableros.

## Reglas
- Nunca inventa cifras; la verificación posterior es obligatoria (no basta con el prompt).
- No da opiniones políticas ni evalúa la gestión; redirige a los datos.
- Privacidad: no registra preguntas con patrones de datos personales; aviso visible antes de preguntar.
- Interruptor en `content/ajustes.json` (Decap) leído por el Worker en cada solicitud.
- Accesibilidad del componente: ver `nxgov-component-builder`.

## Evaluación (puerta de la Etapa 3)
`workers/assistant/eval/preguntas.json`: 30 preguntas con respuesta esperada y citas (20 con dato, 5 sin dato, 5
fuera de tema/adversariales). Aprobado: ≥ 28/30 correctas y **0 cifras inventadas**. Re-evaluar cuando cambien los datos
o el modelo.

## Criterios de salida
Evaluación aprobada · límites y 503 probados · interruptor probado · sin secretos en el repo.
