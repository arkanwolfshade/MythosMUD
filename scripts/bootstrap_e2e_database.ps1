#!/usr/bin/env pwsh
# Force-recreate mythos_e2e, apply DDL/migrations, procedures, and seed E2E users.
# Loads .env.e2e_test from project root (same as E2E server). Run from repo root.

# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
param()

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path $PSScriptRoot -Parent
Set-Location -LiteralPath $ProjectRoot

Write-Host "MythosMUD E2E database bootstrap (mythos_e2e)" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""

$envFile = Join-Path $ProjectRoot ".env.e2e_test"
if (-not (Test-Path $envFile)) {
    Write-Host "[ERROR] .env.e2e_test not found at: $envFile" -ForegroundColor Red
    Write-Host "[SOLUTION] Copy env.e2e_test.example to .env.e2e_test" -ForegroundColor Yellow
    exit 1
}

Write-Host "[INFO] Loading $envFile into process environment" -ForegroundColor Cyan
Get-Content $envFile | ForEach-Object {
    if ($_ -match "^([^#][^=]+)=(.*)$") {
        $name = $matches[1].Trim()
        $value = $matches[2].Trim()
        Set-Item -Path "env:$name" -Value $value -Force
    }
}

function Invoke-Step {
    param([string]$Label, [scriptblock]$Action)
    Write-Host "[INFO] $Label" -ForegroundColor Yellow
    & $Action
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] Step failed: $Label (exit $LASTEXITCODE)" -ForegroundColor Red
        exit 1
    }
}

Write-Host "[INFO] Recreating database from .env.e2e_test (Force)" -ForegroundColor Yellow
Invoke-Step "setup_postgresql_test_db.ps1" { & (Join-Path $PSScriptRoot "setup_postgresql_test_db.ps1") -Force -EnvFile ".env.e2e_test" }

Write-Host ""
Write-Host "[INFO] Applying procedures and migrations to mythos_e2e" -ForegroundColor Yellow
Invoke-Step "apply_procedures.ps1" { & (Join-Path $PSScriptRoot "apply_procedures.ps1") -TargetDbs mythos_e2e }
Invoke-Step "apply_coc_spells_migration.ps1" { & (Join-Path $PSScriptRoot "apply_coc_spells_migration.ps1") -TargetDbs mythos_e2e }
Invoke-Step "apply_arena_migration.ps1" { & (Join-Path $PSScriptRoot "apply_arena_migration.ps1") -TargetDbs mythos_e2e }
Invoke-Step "apply_aggression_level_migration.ps1" { & (Join-Path $PSScriptRoot "apply_aggression_level_migration.ps1") -TargetDbs mythos_e2e }

Write-Host ""
Write-Host "[INFO] Seeding E2E users (uv run python scripts/seed_e2e_users.py)" -ForegroundColor Yellow
$seedResult = & uv run python scripts/seed_e2e_users.py 2>&1
$seedResult | Write-Host
if (-not $?) {
    Write-Host "[ERROR] seed_e2e_users.py failed" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "[OK] E2E database bootstrap complete." -ForegroundColor Green
