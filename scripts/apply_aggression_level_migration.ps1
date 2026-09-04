#!/usr/bin/env pwsh
# Apply aggression_level to npc_definitions behavior_config for existing DBs.
#
# This script:
# - Uses .env.local (or .env) when targeting mythos_dev; .env.unit_test for mythos_unit/mythos_e2e.
# - Applies per-environment migration: 20260310_add_aggression_level_npc_definitions_*.sql
# - Idempotent: safe to run multiple times.

[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status messages use Write-Host for clarity')]
param(
    [string[]]$TargetDbs = @("mythos_unit", "mythos_e2e")
)

$ErrorActionPreference = "Stop"

Write-Host "Applying aggression_level npc_definitions migration to target databases" -ForegroundColor Green
Write-Host "=========================================================================" -ForegroundColor Green
Write-Host ""

$ProjectRoot = Split-Path $PSScriptRoot -Parent

# Resolve env file: mythos_dev -> .env.local or .env; test dbs -> .env.unit_test
$envPath = $null
$targetsDev = $TargetDbs | Where-Object { $_ -eq "mythos_dev" }
$targetsTest = $TargetDbs | Where-Object { $_ -match "mythos_unit|mythos_e2e" }
if ($targetsDev.Count -gt 0 -and (Test-Path (Join-Path $ProjectRoot ".env.local"))) {
    $envPath = Join-Path $ProjectRoot ".env.local"
}
elseif ($targetsDev.Count -gt 0 -and (Test-Path (Join-Path $ProjectRoot ".env"))) {
    $envPath = Join-Path $ProjectRoot ".env"
}
elseif ($targetsTest.Count -gt 0 -and (Test-Path (Join-Path $ProjectRoot ".env.unit_test"))) {
    $envPath = Join-Path $ProjectRoot ".env.unit_test"
}
elseif (Test-Path (Join-Path $ProjectRoot ".env.local")) {
    $envPath = Join-Path $ProjectRoot ".env.local"
}
elseif (Test-Path (Join-Path $ProjectRoot ".env.unit_test")) {
    $envPath = Join-Path $ProjectRoot ".env.unit_test"
}
elseif (Test-Path (Join-Path $ProjectRoot ".env")) {
    $envPath = Join-Path $ProjectRoot ".env"
}

if (-not $envPath) {
    Write-Host "[ERROR] No env file found. For mythos_dev use .env.local or .env; for test dbs use .env.unit_test." -ForegroundColor Red
    exit 1
}

Write-Host "[INFO] Loading configuration from $envPath" -ForegroundColor Cyan
$envContent = Get-Content $envPath -Raw

$databaseUrl = ""
if ($envContent -match 'DATABASE_URL=(.+)') {
    $databaseUrl = $matches[1].Trim()
}
else {
    Write-Host "[ERROR] DATABASE_URL not found in $envPath" -ForegroundColor Red
    exit 1
}

if ($databaseUrl -notmatch 'postgresql\+?asyncpg?://([^:]+):([^@]+)@([^:]+):(\d+)/(.+)') {
    Write-Host "[ERROR] Invalid PostgreSQL URL format: $databaseUrl" -ForegroundColor Red
    exit 1
}

$dbUser = $matches[1]
$dbPassword = $matches[2]
$dbHost = $matches[3]
$dbPort = $matches[4]

Write-Host "Database Configuration (from $envPath):" -ForegroundColor Yellow
Write-Host "  Host: $dbHost" -ForegroundColor Gray
Write-Host "  Port: $dbPort" -ForegroundColor Gray
Write-Host "  User: $dbUser" -ForegroundColor Gray
Write-Host ""

$psqlPath = Get-Command psql -ErrorAction SilentlyContinue
if (-not $psqlPath) {
    $commonPaths = @(
        "C:\Program Files\PostgreSQL\*\bin\psql.exe",
        "C:\Program Files (x86)\PostgreSQL\*\bin\psql.exe"
    )

    $found = $false
    foreach ($path in $commonPaths) {
        $psqlFiles = Get-ChildItem -Path $path -ErrorAction SilentlyContinue
        if ($psqlFiles) {
            $psqlPath = $psqlFiles[0].FullName
            $found = $true
            break
        }
    }

    if (-not $found) {
        Write-Host "[ERROR] PostgreSQL client (psql) not found" -ForegroundColor Red
        Write-Host "[SOLUTION] Install PostgreSQL from: https://www.postgresql.org/download/windows/" -ForegroundColor Yellow
        exit 1
    }
}
else {
    $psqlPath = $psqlPath.Path
}

Write-Host "[INFO] Using psql: $psqlPath" -ForegroundColor Cyan
Write-Host ""

$env:PGPASSWORD = $dbPassword

try {
    foreach ($targetDb in $TargetDbs) {
        $migrationFile = $null

        switch ($targetDb) {
            "mythos_unit" {
                $migrationFile = Join-Path -Path $ProjectRoot -ChildPath "data\db\migrations\20260310_add_aggression_level_npc_definitions_unit.sql"
            }
            "mythos_e2e" {
                $migrationFile = Join-Path -Path $ProjectRoot -ChildPath "data\db\migrations\20260310_add_aggression_level_npc_definitions_e2e.sql"
            }
            "mythos_dev" {
                $migrationFile = Join-Path -Path $ProjectRoot -ChildPath "data\db\migrations\20260310_add_aggression_level_npc_definitions_dev.sql"
            }
            default {
                Write-Host "[WARNING] No aggression_level migration configured for database '$targetDb'; skipping." -ForegroundColor Yellow
                continue
            }
        }

        if (-not (Test-Path $migrationFile)) {
            Write-Host "[ERROR] Migration file not found for '$targetDb': $migrationFile" -ForegroundColor Red
            exit 1
        }

        Write-Host "Applying aggression_level migration to database '$targetDb' using $migrationFile ..." -ForegroundColor Yellow

        $result = & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d $targetDb -v ON_ERROR_STOP=1 -f $migrationFile 2>&1

        if ($LASTEXITCODE -eq 0) {
            Write-Host "[OK] Migration applied successfully to '$targetDb'" -ForegroundColor Green
        }
        else {
            Write-Host "[ERROR] Failed to apply migration to '$targetDb':" -ForegroundColor Red
            Write-Host $result -ForegroundColor Red
            exit 1
        }

        Write-Host ""
    }

    Write-Host "Aggression_level npc_definitions migration applied to all target databases." -ForegroundColor Green
}
finally {
    Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue
}
