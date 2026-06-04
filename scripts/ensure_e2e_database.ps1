#!/usr/bin/env pwsh
# Ensure mythos_e2e exists and has reference seed (professions from mythos_e2e_dml.sql).
# Used by make test-playwright before Playwright runs against the E2E server (.env.e2e_test).
# Full recreate via bootstrap_e2e_database.ps1 when the DB is missing or professions count is 0.

# Suppress PSAvoidUsingWriteHost: status output for operators
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
param()

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

$databaseUrl = ""
$searchPath = "mythos_e2e"
foreach ($line in Get-Content $envFile) {
    if ($line -match "^([^#][^=]+)=(.*)$") {
        $name = $matches[1].Trim()
        $value = $matches[2].Trim()
        if ($name -eq "DATABASE_URL") { $databaseUrl = $value }
        if ($name -eq "POSTGRES_SEARCH_PATH") { $searchPath = $value }
    }
}

if (-not $databaseUrl) {
    Write-Host "[ERROR] DATABASE_URL not found in $envFile" -ForegroundColor Red
    exit 1
}

if ($databaseUrl -notmatch 'postgresql\+?asyncpg?://([^:]+):([^@]+)@([^:]+):(\d+)/([^?]+)') {
    Write-Host "[ERROR] Invalid PostgreSQL URL in .env.e2e_test" -ForegroundColor Red
    exit 1
}

$dbUser = $matches[1]
$dbPassword = $matches[2]
$dbHost = $matches[3]
$dbPort = $matches[4]
$dbName = $matches[5]

if ($dbName -ne "mythos_e2e") {
    Write-Host "[ERROR] .env.e2e_test must use database mythos_e2e (got '$dbName')" -ForegroundColor Red
    exit 1
}

function Get-ProfessionCount {
    param([string]$PsqlPath, [string]$DbHost, [string]$DbPort, [string]$DbUser, [string]$DbName, [string]$Schema)
    $countSql = "SELECT COUNT(*) FROM ${Schema}.professions;"
    $profRaw = & $PsqlPath -h $DbHost -p $DbPort -U $DbUser -d $DbName -t -A -c $countSql 2>&1
    if ($LASTEXITCODE -ne 0) {
        return -1
    }
    return [int]($profRaw.Trim())
}

function Invoke-ProfessionSeedFile {
    param([string]$PsqlPath, [string]$DbHost, [string]$DbPort, [string]$DbUser, [string]$DbName)
    $seedFile = Join-Path $ProjectRoot "data\db\e2e_professions_seed.sql"
    if (-not (Test-Path $seedFile)) {
        Write-Host "[ERROR] Profession seed file not found: $seedFile" -ForegroundColor Red
        return $false
    }
    Write-Host "[INFO] Loading profession seed (no DB drop): $seedFile" -ForegroundColor Yellow
    $result = & $PsqlPath -h $DbHost -p $DbPort -U $DbUser -d $DbName -v ON_ERROR_STOP=1 -f $seedFile 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] Failed to load profession seed: $result" -ForegroundColor Red
        return $false
    }
    return $true
}

function Resolve-PsqlPath {
    $cmd = Get-Command psql -ErrorAction SilentlyContinue
    if ($cmd) {
        return $cmd.Path
    }
    $commonPaths = @(
        "C:\Program Files\PostgreSQL\*\bin\psql.exe",
        "C:\Program Files (x86)\PostgreSQL\*\bin\psql.exe"
    )
    foreach ($pattern in $commonPaths) {
        $psqlFiles = Get-ChildItem -Path $pattern -ErrorAction SilentlyContinue
        if ($psqlFiles) {
            return $psqlFiles[0].FullName
        }
    }
    Write-Host "[ERROR] PostgreSQL client (psql) not found" -ForegroundColor Red
    exit 1
}

$psqlPath = Resolve-PsqlPath
$env:PGPASSWORD = $dbPassword

Write-Host "MythosMUD ensure E2E database (mythos_e2e)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

try {
    $dbExistsRaw = & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d postgres -t -A -c `
        "SELECT 1 FROM pg_database WHERE datname = '$dbName';" 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] Failed to query PostgreSQL: $dbExistsRaw" -ForegroundColor Red
        exit 1
    }

    $dbExists = ($dbExistsRaw -match '1')
    $profCount = 0

    if ($dbExists) {
        $profCount = Get-ProfessionCount -PsqlPath $psqlPath -DbHost $dbHost -DbPort $dbPort -DbUser $dbUser -DbName $dbName -Schema $searchPath
        if ($profCount -lt 0) {
            Write-Host "[INFO] professions table missing or unreadable; will bootstrap" -ForegroundColor Yellow
            $profCount = 0
        }
    }

    if ($dbExists -and $profCount -eq 0) {
        if (-not (Invoke-ProfessionSeedFile -PsqlPath $psqlPath -DbHost $dbHost -DbPort $dbPort -DbUser $dbUser -DbName $dbName)) {
            Write-Host "[WARNING] Profession seed file failed; will try full bootstrap" -ForegroundColor Yellow
        }
        $profCount = Get-ProfessionCount -PsqlPath $psqlPath -DbHost $dbHost -DbPort $dbPort -DbUser $dbUser -DbName $dbName -Schema $searchPath
        if ($profCount -lt 0) {
            $profCount = 0
        }
    }

    if (-not $dbExists -or $profCount -eq 0) {
        if (-not $dbExists) {
            Write-Host "[INFO] Database '$dbName' does not exist; running full E2E bootstrap" -ForegroundColor Yellow
        }
        else {
            Write-Host "[INFO] '$dbName' still has no professions after seed file; running full E2E bootstrap" -ForegroundColor Yellow
        }
        & (Join-Path $PSScriptRoot "bootstrap_e2e_database.ps1")
        if ($LASTEXITCODE -ne 0) {
            exit 1
        }
        $profCount = Get-ProfessionCount -PsqlPath $psqlPath -DbHost $dbHost -DbPort $dbPort -DbUser $dbUser -DbName $dbName -Schema $searchPath
        if ($profCount -le 0) {
            Write-Host "[ERROR] mythos_e2e.professions is still empty after bootstrap." -ForegroundColor Red
            Write-Host "[SOLUTION] Run: make bootstrap-e2e-database" -ForegroundColor Yellow
            Write-Host "[SOLUTION] Then restart the E2E server (e2e.bat or scripts/start_e2e_test.ps1)" -ForegroundColor Yellow
            exit 1
        }
    }
    else {
        Write-Host "[OK] mythos_e2e has $profCount profession(s); skipping full recreate" -ForegroundColor Green
    }
    Write-Host "[INFO] Idempotent E2E user seed (seed_e2e_users.py)" -ForegroundColor Yellow
    Get-Content $envFile | ForEach-Object {
        if ($_ -match "^([^#][^=]+)=(.*)$") {
            Set-Item -Path "env:$($matches[1].Trim())" -Value $matches[2].Trim() -Force
        }
    }
    $seedResult = & uv run python scripts/seed_e2e_users.py 2>&1
    $seedResult | Write-Host
    if (-not $?) {
        Write-Host "[ERROR] seed_e2e_users.py failed" -ForegroundColor Red
        exit 1
    }
}
finally {
    Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue
}
