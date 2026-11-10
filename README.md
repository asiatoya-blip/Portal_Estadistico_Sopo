# Portal Estadístico de Sopó

Micrositio estadístico de la Alcaldía de Sopó, bajo normativa GOV.CO (Kit UI 9.2, CDN v5, WCAG 2.1 AA, Res. 1519 de
2020). Lo construye un equipo de agentes de Claude Code en paralelo, por etapas.

- Contexto y reglas: [`CLAUDE.md`](CLAUDE.md)
- Plan, pistas y puertas: [`docs/etapas.md`](docs/etapas.md) · Bitácora: [`docs/bitacora.md`](docs/bitacora.md)
- Decisiones: [`docs/adr/`](docs/adr/) · Contratos: [`contracts/`](contracts/)
- Agentes: [`.claude/agents/`](.claude/agents/) · Skills: [`.claude/skills/`](.claude/skills/)

## Arranque (una vez)

En PowerShell, dentro de la carpeta del repo:

```powershell
powershell -ExecutionPolicy Bypass -File .\setup.ps1
```

El script mueve `_setup/claude` → `.claude/` (agentes, skills, reglas) y `_setup/github` → `.github/`, ejecuta
`git init -b main` con el commit inicial y se borra a sí mismo. Luego abre `claude` en la carpeta y acepta la confianza
del directorio.

## Trabajo en paralelo

Una sesión por pista, cada una en su worktree y rama:

```bash
claude --worktree etapa0-normativa     # dentro: "Actúa como research-normativa y haz E0-R-01"
claude --worktree etapa0-datos         # data-analyst: E0-D-01..03
claude --worktree etapa0-infra         # devops: E0-O-01..03
```

O una sola sesión con el agente `orquestador`, que delega en subagentes. Los merges a `main` los hace el orquestador
en el orden de `docs/etapas.md`.

## Estructura

| Ruta | Contenido | Dueño |
|---|---|---|
| `contracts/` | Esquemas y APIs acordadas | architect |
| `docs/` | Etapas, bitácora, ADR, normativa, runbooks, manuales | varios |
| `vendor/nxgov/` | Librería Sogas (solo lectura) | devops (actualiza) |
| `src/components/`, `src/catalogo/` | Bloques `nxgov-` nuevos | engineer-components |
| `src/site/`, `src/styles/` | Sitio Eleventy | engineer-site |
| `scripts/data/`, `tableau/` | Pipeline de datos y libros | data-analyst |
| `data/` | Datos generados por el workflow | — |
| `admin/`, `content/` | Decap CMS y contenidos | cms-content |
| `workers/` | assistant · oauth · metrics | ai-assistant · devops |
| `tests/`, `audits/` | e2e · a11y · informes | engineer-site · auditores |
