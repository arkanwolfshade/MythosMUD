#!/usr/bin/env pwsh
# Run dbmate migrations against one MythosMUD database (#811).
#
# Single wrapper around dbmate so the mythos_dev guard and the env-file/search_path resolution
# live in exactly one place, instead of being copy-pasted across apply scripts (see #811
# investigation: six near-identical ~40-line blocks were removed in favor of this file).
#
# Only "up" and "status" are reachable -- dbmate's "drop" and "down" are never exposed, and
# mythos_dev additionally can never be the target of anything but "status" and "up".
#
# db/schema.sql and data/db/seed.sql (the schema-agnostic baseline) are NOT applied by this
# script -- they are loaded once, outside dbmate, when a database is first provisioned (see
# db/databases/databases.sql and scripts/load_world_seed.py). dbmate only tracks and applies
# db/migrations/*.sql from db/migrations/20260915000000_baseline.sql onward.
#
# Usage:
#   .\scripts\migrate.ps1 -Environment unit
#   .\scripts\migrate.ps1 -Environment e2e -Verb status
#   .\scripts\migrate.ps1 -Environment dev -Verb status

[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status messages use Write-Host for clarity')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingConvertToSecureStringWithPlainText', '', Justification = 'Password from env-file DATABASE_URL requires plaintext conversion to build the dbmate URL')]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("dev", "unit", "e2e")]
    [string]$Environment,

    [ValidateSet("up", "status")]
    [string]$Verb = "up"
)

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path $PSScriptRoot -Parent
$DbName = "mythos_$Environment"

$EnvFileByEnvironment = @{
    dev  = ".env.local"
    unit = ".env.unit_test"
    e2e  = ".env.e2e_test"
}
$EnvFile = Join-Path $ProjectRoot $EnvFileByEnvironment[$Environment]

if (-not (Test-Path $EnvFile)) {
    Write-Host "[ERROR] Env file not found: $EnvFile" -ForegroundColor Red
    exit 1
}

$envContent = Get-Content $EnvFile -Raw
$databaseUrl = $null
$searchPath = $DbName
foreach ($line in ($envContent -split "`n")) {
    if ($line -match '^\s*DATABASE_URL=(.+)') { $databaseUrl = $matches[1].Trim() }
    if ($line -match '^\s*POSTGRES_SEARCH_PATH=(.+)') { $searchPath = $matches[1].Trim() }
}

if (-not $databaseUrl) {
    Write-Host "[ERROR] DATABASE_URL not found in $EnvFile" -ForegroundColor Red
    exit 1
}

if ($databaseUrl -notmatch 'postgresql\+?asyncpg?://([^:]+):([^@]+)@([^:/]+):([0-9]+)/(.+)') {
    Write-Host "[ERROR] Invalid PostgreSQL URL format in $EnvFile" -ForegroundColor Red
    exit 1
}
$dbUser = $matches[1]
$dbPassword = $matches[2]
$dbHost = $matches[3]
$dbPort = $matches[4]
$urlDbName = $matches[5] -replace '\?.*$', ''

if ($urlDbName -ne $DbName) {
    Write-Host "[ERROR] $EnvFile's DATABASE_URL points at '$urlDbName', expected '$DbName'." -ForegroundColor Red
    exit 1
}

$dbmateUrl = "postgres://${dbUser}:${dbPassword}@${dbHost}:${dbPort}/${DbName}?sslmode=disable&search_path=$searchPath"
$migrationsDir = Join-Path $ProjectRoot "db\migrations"

Write-Host "Running dbmate $Verb against $DbName (search_path=$searchPath)..." -ForegroundColor Green
Push-Location $ProjectRoot
try {
    & npx dbmate --url $dbmateUrl --migrations-dir $migrationsDir --no-dump-schema $Verb
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] dbmate $Verb failed for $DbName (exit $LASTEXITCODE)" -ForegroundColor Red
        exit $LASTEXITCODE
    }
}
finally {
    Pop-Location
}
