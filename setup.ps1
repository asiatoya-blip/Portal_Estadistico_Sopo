# Instala la configuración de agentes (.claude) y workflows (.github) e inicializa git.
# Uso (PowerShell, en la carpeta del repo):  powershell -ExecutionPolicy Bypass -File .\setup.ps1
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

foreach ($par in @(@('_setup\claude', '.claude'), @('_setup\github', '.github'))) {
    $origen = $par[0]; $destino = $par[1]
    if (-not (Test-Path $origen)) { Write-Host "No existe $origen (¿ya instalado?)"; continue }
    New-Item -ItemType Directory -Force -Path $destino | Out-Null
    Copy-Item -Path "$origen\*" -Destination $destino -Recurse -Force
    Write-Host "Instalado $destino"
}
Remove-Item -Recurse -Force '_setup'

if (-not (Test-Path '.git')) {
    git init -b main
    git add -A
    git commit -m "E0: configuración inicial del repositorio (agentes, skills, contratos v0)"
    Write-Host 'Repositorio git inicializado con commit inicial.'
}
Write-Host 'Listo. Abre Claude Code en esta carpeta: claude'
Remove-Item -Force $MyInvocation.MyCommand.Path
