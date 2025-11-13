Param(
    [string]$Path = "data/prototypes/items"
)

$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $PSScriptRoot

Set-Location $projectRoot

if (-not (Test-Path $Path)) {
    Write-Error "Prototype directory not found: $Path"
    exit 1
}

uv run python -m server.scripts.validate_prototypes --path $Path

exit $LASTEXITCODE
