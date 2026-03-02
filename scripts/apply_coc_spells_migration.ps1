#!/usr/bin/env pwsh
# Apply CoC/Grand Grimoire spell batch migration to test databases.
#
# This script:
# - Reuses the PostgreSQL connection details from .env.unit_test (same as setup_postgresql_test_db.ps1)
# - Applies per-environment CoC spell migrations to mythos_unit and mythos_e2e.

[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status messages use Write-Host for clarity')]
param(
    [string[]]$TargetDbs = @("mythos_unit", "mythos_e2e")
)

$ErrorActionPreference = "Stop"

Write-Host "Applying CoC spell batch migration to test databases" -ForegroundColor Green
Write-Host "====================================================" -ForegroundColor Green
Write-Host ""

$ProjectRoot = Split-Path $PSScriptRoot -Parent
$TestEnvPath = Join-Path -Path $ProjectRoot -ChildPath ".env.unit_test"

if (-not (Test-Path $TestEnvPath)) {
    Write-Host "[ERROR] .env.unit_test file not found at: $TestEnvPath" -ForegroundColor Red
    Write-Host "[SOLUTION] Run: make setup-test-env" -ForegroundColor Yellow
    exit 1
}

Write-Host "[INFO] Loading configuration from $TestEnvPath" -ForegroundColor Cyan
$envContent = Get-Content $TestEnvPath -Raw

$databaseUrl = ""
if ($envContent -match 'DATABASE_URL=(.+)') {
    $databaseUrl = $matches[1].Trim()
}
else {
    Write-Host "[ERROR] DATABASE_URL not found in .env.unit_test" -ForegroundColor Red
    exit 1
}

if ($databaseUrl -notmatch 'postgresql\+?asyncpg?://([^:]+):([^@]+)@([^:]+):(\d+)/(.+)') {
    Write-Host "[ERROR] Invalid PostgreSQL URL format in .env.unit_test: $databaseUrl" -ForegroundColor Red
    exit 1
}

$dbUser = $matches[1]
$dbPassword = $matches[2]
$dbHost = $matches[3]
$dbPort = $matches[4]

Write-Host "Database Configuration (from .env.unit_test):" -ForegroundColor Yellow
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
                $migrationFile = Join-Path -Path $ProjectRoot -ChildPath "data\db\migrations\20260227_add_coc_spells_batch1_unit.sql"
            }
            "mythos_e2e" {
                $migrationFile = Join-Path -Path $ProjectRoot -ChildPath "data\db\migrations\20260227_add_coc_spells_batch1_e2e.sql"
            }
            default {
                Write-Host "[WARNING] No CoC migration configured for database '$targetDb'; skipping." -ForegroundColor Yellow
                continue
            }
        }

        if (-not (Test-Path $migrationFile)) {
            Write-Host "[ERROR] Migration file not found for '$targetDb': $migrationFile" -ForegroundColor Red
            exit 1
        }

        Write-Host "Applying CoC spells migration to database '$targetDb' using $migrationFile ..." -ForegroundColor Yellow

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

    Write-Host "CoC spell batch migration applied to all test databases." -ForegroundColor Green
}
finally {
    Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue
}
