#!/usr/bin/env pwsh
# Run server integration tests against mythos_e2e (same DB as Playwright / E2E server).
# Loads .env.e2e_test so DATABASE_URL and POSTGRES_SEARCH_PATH match the runtime stack.

[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status output for operators')]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$PytestArgs
)

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path $PSScriptRoot -Parent
Set-Location -LiteralPath $ProjectRoot

$envFile = Join-Path $ProjectRoot ".env.e2e_test"
$exampleEnv = Join-Path $ProjectRoot "env.e2e_test.example"

if (-not (Test-Path $envFile)) {
    if (-not (Test-Path $exampleEnv)) {
        Write-Host "[ERROR] .env.e2e_test not found and no env.e2e_test.example at: $exampleEnv" -ForegroundColor Red
        exit 1
    }
    Write-Host "[INFO] Creating .env.e2e_test from env.e2e_test.example" -ForegroundColor Yellow
    Copy-Item -LiteralPath $exampleEnv -Destination $envFile
}

Write-Host "[INFO] Loading $envFile for integration tests (mythos_e2e)" -ForegroundColor Cyan
Get-Content $envFile | ForEach-Object {
    if ($_ -match "^([^#][^=]+)=(.*)$") {
        Set-Item -Path "env:$($matches[1].Trim())" -Value $matches[2].Trim() -Force
    }
}

$defaultArgs = @(
    "server/tests/",
    "-m", "integration",
    "-n", "1"
)

if ($PytestArgs.Count -gt 0) {
    $allArgs = $defaultArgs + $PytestArgs
}
else {
    $allArgs = $defaultArgs
}

& uv run pytest @allArgs
exit $LASTEXITCODE
