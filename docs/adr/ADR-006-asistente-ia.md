# ADR-006 — Asistente IA con Cloudflare Workers AI, restringido a datos oficiales

- Fecha: 2026-10-20 · Estado: Aprobado

## Contexto
Solo se mantiene si hay solución gratuita para la demanda (~5.000 visitas/mes). Workers AI incluye 10.000 neuronas/día gratis; al superarlas falla en vez de cobrar.

## Decisión
Worker propio (`workers/assistant/`) que recibe la pregunta, recupera el contexto desde `data/*.json` y las fichas técnicas, y responde solo con esos datos, citando indicador, fuente y fecha de corte. Si no hay dato, lo dice y enlaza el tablero. Límite por visitante, caché de preguntas frecuentes, interruptor en Decap. No guarda preguntas con datos personales. Puerta de calidad: ≥ 28/30 en el set de evaluación y 0 cifras inventadas.

## Alternativas descartadas
| Opción | Por qué no |
|---|---|
| Gemini desde el navegador (mockup) | Clave expuesta |
| API de pago | Incumple la condición de gratuidad |
