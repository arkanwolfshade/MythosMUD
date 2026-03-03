#!/usr/bin/env pwsh
# Apply PostgreSQL procedures and functions from db/procedures/ to target databases.
#
# This script:
# - Reads PostgreSQL connection details from .env.unit_test (tests) or .env.local/.env (dev)
# - Applies all .sql files in db/procedures/ to each target database
# - Uses schema name matching the database name (mythos_unit, mythos_e2e, mythos_dev)
#
# Usage:
#   .\scripts\apply_procedures.ps1 -TargetDbs mythos_dev
#   .\scripts\apply_procedures.ps1 -TargetDbs mythos_unit, mythos_e2e
#   .\scripts\apply_procedures.ps1 -EnvFile .env.local -TargetDbs mythos_dev

[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status messages use Write-Host for clarity')]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$TargetDbs = @("mythos_dev"),
    [string]$EnvFile = ""
)

# Flatten in case TargetDbs was passed as "mythos_unit,mythos_e2e" (single string)
$TargetDbs = $TargetDbs | ForEach-Object { $_ -split "," } | ForEach-Object { $_.Trim() } | Where-Object { $_ }
if ($TargetDbs.Count -eq 0) {
    $TargetDbs = @("mythos_dev")
}

$ErrorActionPreference = "Stop"

Write-Host "Applying PostgreSQL procedures to databases" -ForegroundColor Green
Write-Host "===========================================" -ForegroundColor Green
Write-Host ""

$ProjectRoot = Split-Path $PSScriptRoot -Parent
$ProceduresDir = Join-Path -Path $ProjectRoot -ChildPath "db\procedures"

if (-not (Test-Path $ProceduresDir)) {
    Write-Host "[ERROR] Procedures directory not found: $ProceduresDir" -ForegroundColor Red
    exit 1
}

# Resolve env file: explicit > .env.unit_test (when targeting test dbs) > .env.local > .env
$envPath = $null
if ($EnvFile -and (Test-Path (Join-Path $ProjectRoot $EnvFile))) {
    $envPath = Join-Path $ProjectRoot $EnvFile
}
elseif (($TargetDbs | Where-Object { $_ -match "mythos_unit|mythos_e2e" }) -and (Test-Path (Join-Path $ProjectRoot ".env.unit_test"))) {
    $envPath = Join-Path $ProjectRoot ".env.unit_test"
}
elseif (Test-Path (Join-Path $ProjectRoot ".env.local")) {
    $envPath = Join-Path $ProjectRoot ".env.local"
}
elseif (Test-Path (Join-Path $ProjectRoot ".env")) {
    $envPath = Join-Path $ProjectRoot ".env"
}

if (-not $envPath) {
    Write-Host "[ERROR] No env file found. Tried: .env.local, .env.unit_test, .env" -ForegroundColor Red
    Write-Host "[SOLUTION] Run: make setup-test-env (for tests) or create .env.local (for dev)" -ForegroundColor Yellow
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

Write-Host "Database Configuration:" -ForegroundColor Yellow
Write-Host "  Host: $dbHost" -ForegroundColor Gray
Write-Host "  Port: $dbPort" -ForegroundColor Gray
Write-Host "  User: $dbUser" -ForegroundColor Gray
Write-Host "  Target DBs: $($TargetDbs -join ', ')" -ForegroundColor Gray
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

# Get procedure files in order (alphabetical; see db/procedures/README.md for dependency order)
$procedureFiles = Get-ChildItem -Path $ProceduresDir -Filter "*.sql" | Sort-Object Name
if ($procedureFiles.Count -eq 0) {
    Write-Host "[WARNING] No .sql files found in $ProceduresDir - nothing to apply" -ForegroundColor Yellow
    exit 0
}

$env:PGPASSWORD = $dbPassword

try {
    foreach ($targetDb in $TargetDbs) {
        Write-Host "Applying procedures to database '$targetDb' (schema: $targetDb) ..." -ForegroundColor Yellow

        foreach ($file in $procedureFiles) {
            Write-Host "  - $($file.Name)" -ForegroundColor Gray
            $result = & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d $targetDb `
                -v "ON_ERROR_STOP=1" `
                -v "schema_name=$targetDb" `
                -f $file.FullName 2>&1

            if ($LASTEXITCODE -ne 0) {
                Write-Host "[ERROR] Failed to apply $($file.Name) to '$targetDb':" -ForegroundColor Red
                Write-Host $result -ForegroundColor Red
                exit 1
            }
        }

        Write-Host "[OK] All procedures applied successfully to '$targetDb'" -ForegroundColor Green
        Write-Host ""
    }

    Write-Host "Procedure application complete." -ForegroundColor Green
}
finally {
    Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue
}
