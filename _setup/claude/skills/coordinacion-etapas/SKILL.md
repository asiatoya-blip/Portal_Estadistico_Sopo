---
name: coordinacion-etapas
description: Protocolo común de trabajo por etapas del Portal Estadístico de Sopó. Úsala al iniciar o cerrar cualquier tarea, al pasar trabajo a otro agente, al cambiar un contrato o al pedir una puerta de etapa.
---

# Coordinación por etapas

Todos los agentes siguen este protocolo. El plan vive en `docs/etapas.md`; el estado, en `CLAUDE.md`.

## Al iniciar una tarea
1. Ubica el ID (`E<etapa>-<pista>-<n>`) en `docs/etapas.md`. Sin ID, no se trabaja: pide uno al `orquestador`.
2. Verifica que la puerta de la etapa anterior esté marcada como cumplida en `CLAUDE.md`.
3. Lee los contratos que tocas (`contracts/`). Si un contrato no alcanza, **no improvises**: nota al `architect`.
4. Confirma que solo escribirás en carpetas que te pertenecen (mapa de propiedad en `docs/etapas.md`).
5. Trabaja en tu worktree/rama: `etapa<N>/<pista>` (ej. `claude --worktree etapa2-componentes`).

## Al cerrar una tarea
1. Corre las verificaciones de tu skill de especialidad (cada una tiene "Criterios de salida").
2. Entrada en `docs/bitacora.md`, arriba del todo:
   `AAAA-MM-DD · agente · ID · qué se hizo · archivos · siguiente paso / bloqueo`
3. Commit con mensaje `E2-A-03: nxgov-tabs con navegación por flechas` (ID primero).
4. Si cambió una decisión, avisa al `orquestador` para actualizar `CLAUDE.md`.

## Traspaso a otro agente (nota de handoff)
```
Para: <agente> · Desde: <agente> · Tarea: <ID>
Qué te entrego: <archivos / rama>
Qué falta: <lista corta>
Contratos involucrados: <archivos>
Riesgos conocidos: <si hay>
```

## Cambios de contrato
Un contrato "Aprobado v1" solo cambia con un ADR (`docs/adr/ADR-000-plantilla.md`) y aviso a cada agente que lo usa.
El `architect` redacta; el usuario aprueba si afecta alcance.

## Bloqueos
Bloqueo externo (accesos, DNS, cuentas) → `CLAUDE.md` § Pendientes externos. Bloqueo técnico → bitácora + dueño.
Nunca se resuelve un bloqueo escribiendo en carpetas ajenas.

## Independencia de la auditoría
Quien construye no audita su trabajo. `auditor-a11y` y `compliance-security` revisan sin haber participado.
