#!/usr/bin/env pwsh
# Reconverge mythos_e2e (schema, seed, procedures, migrations) and seed E2E users.
# Loads .env.e2e_test from project root (same as E2E server). Run from repo root.
#
# By default, also DROP DATABASE/CREATE DATABASE mythos_e2e first, via
# setup_postgresql_test_db.ps1 -Force. -SkipForce keeps the existing database instead --
# schema/seed/migrations are still fully reconverged either way (setup_postgresql_test_db.ps1
# no longer has an early-exit for "database already exists", #811 follow-up); -SkipForce just
# skips the database-object-level drop. `make ensure-e2e-database` passes -SkipForce as its
# fast, always-correct pre-test-run gate (replacing the old ensure_e2e_database.ps1 heuristic,
# which could and did guess wrong).

# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
param(
    [switch]$SkipForce
)
$Force = -not $SkipForce

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

Write-Host "[INFO] Reconverging database from .env.e2e_test (Force=$Force)" -ForegroundColor Yellow
Invoke-Step "setup_postgresql_test_db.ps1" { & (Join-Path $PSScriptRoot "setup_postgresql_test_db.ps1") -Force:$Force -EnvFile ".env.e2e_test" }

Write-Host ""
Write-Host "[INFO] Applying procedures and migrations to mythos_e2e" -ForegroundColor Yellow
Invoke-Step "apply_procedures.ps1" { & (Join-Path $PSScriptRoot "apply_procedures.ps1") -TargetDbs mythos_e2e }
Invoke-Step "migrate.ps1" { & (Join-Path $PSScriptRoot "migrate.ps1") -Environment e2e }

Write-Host ""
Write-Host "[INFO] Seeding E2E users (uv run --no-sync python scripts/seed_e2e_users.py)" -ForegroundColor Yellow
$seedResult = & uv run --no-sync python scripts/seed_e2e_users.py 2>&1
$seedResult | Write-Host
if (-not $?) {
    Write-Host "[ERROR] seed_e2e_users.py failed" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "[OK] E2E database bootstrap complete." -ForegroundColor Green
