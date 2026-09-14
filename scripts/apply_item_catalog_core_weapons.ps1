#!/usr/bin/env pwsh
# Apply item catalog DML batches (ADR-026 Phase 2).
# Idempotent ON CONFLICT upserts. Targets: mythos_unit, mythos_e2e, mythos_dev.

[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status messages use Write-Host for clarity')]
param(
    [string[]]$TargetDbs = @("mythos_unit", "mythos_e2e"),
    [string[]]$Batches = @("core_weapons", "core_tomes", "core_equipment", "scenario_dark_turns"),
    [string]$Stamp = "20260914"
)

$ErrorActionPreference = "Stop"

Write-Host "Applying item catalog migrations ($($Batches -join ', '))" -ForegroundColor Green
Write-Host "=========================================================" -ForegroundColor Green
Write-Host ""

$ProjectRoot = Split-Path $PSScriptRoot -Parent

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
    Write-Host "[ERROR] No env file found." -ForegroundColor Red
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
        $suffix = switch ($targetDb) {
            "mythos_unit" { "unit" }
            "mythos_e2e" { "e2e" }
            "mythos_dev" { "dev" }
            default { $null }
        }
        if (-not $suffix) {
            Write-Host "[WARNING] No item catalog migration for '$targetDb'; skipping." -ForegroundColor Yellow
            continue
        }

        foreach ($batch in $Batches) {
            $migrationFile = Join-Path $ProjectRoot "data\db\migrations\${Stamp}_item_catalog_${batch}_${suffix}.sql"
            if (-not (Test-Path $migrationFile)) {
                Write-Host "[ERROR] Migration file not found: $migrationFile" -ForegroundColor Red
                exit 1
            }
            Write-Host "Applying $migrationFile to '$targetDb' ..." -ForegroundColor Yellow
            $result = & { $ErrorActionPreference = "Continue"; & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d $targetDb -v ON_ERROR_STOP=1 -f $migrationFile 2>&1 }
            if ($LASTEXITCODE -ne 0) {
                Write-Host "[ERROR] Failed to apply migration to '$targetDb':" -ForegroundColor Red
                Write-Host $result -ForegroundColor Red
                exit 1
            }
            Write-Host "[OK] Applied $batch to '$targetDb'" -ForegroundColor Green
        }
        Write-Host ""
    }
    Write-Host "Item catalog migrations applied." -ForegroundColor Green
}
finally {
    Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue
}
