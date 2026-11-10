# Contrato del asistente IA — Propuesta v0

`POST /api/asistente` (Worker) · cuerpo `{ "pregunta": string ≤ 300, "idioma": "es" | "en" }`

Respuesta 200:
```json
{ "respuesta": "texto plano, ≤ 120 palabras",
  "citas": [ { "indicador": "poblacion-total", "fuente": "DANE — …", "fecha_corte": "2026-09-30", "url": "/indicadores/poblacion-total/" } ],
  "sin_datos": false }
```
Si no hay datos: `sin_datos: true`, respuesta que lo dice y enlace al tablero más cercano. Errores: 429 (límite por
visitante, con `Retry-After`), 503 (cupo diario agotado o interruptor apagado). Nunca devuelve cifras que no estén en
`citas`. No registra texto de preguntas que contengan datos personales (regex de documento, teléfono, correo).
