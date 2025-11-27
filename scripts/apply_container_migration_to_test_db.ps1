#!/usr/bin/env pwsh
# Apply container_item_instance_id migration to test database
# This script applies the migration to an existing test database

$ErrorActionPreference = "Stop"

Write-Host "MythosMUD Container Migration for Test Database" -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Green
Write-Host ""

# Load database URL from .env.unit_test
$TestEnvPath = Join-Path -Path $PSScriptRoot -ChildPath ".." | Join-Path -ChildPath "server" | Join-Path -ChildPath "tests" | Join-Path -ChildPath ".env.unit_test"

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
} else {
    Write-Host "[ERROR] DATABASE_URL not found in .env.unit_test" -ForegroundColor Red
    exit 1
}

# Parse PostgreSQL URL
if ($databaseUrl -notmatch 'postgresql\+?asyncpg?://([^:]+):([^@]+)@([^:]+):(\d+)/(.+)') {
    Write-Host "[ERROR] Invalid PostgreSQL URL format: $databaseUrl" -ForegroundColor Red
    exit 1
}

$dbUser = $matches[1]
$dbPassword = $matches[2]
$dbHost = $matches[3]
$dbPort = $matches[4]
$dbName = $matches[5]

Write-Host "Database Configuration:" -ForegroundColor Yellow
Write-Host "  Host:     $dbHost" -ForegroundColor Gray
Write-Host "  Port:     $dbPort" -ForegroundColor Gray
Write-Host "  User:     $dbUser" -ForegroundColor Gray
Write-Host "  Database: $dbName" -ForegroundColor Gray
Write-Host ""

# Check if psql is available
$psqlPath = Get-Command psql -ErrorAction SilentlyContinue
if (-not $psqlPath) {
    # Try common PostgreSQL installation paths on Windows
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
} else {
    $psqlPath = $psqlPath.Path
}

Write-Host "[INFO] Using psql: $psqlPath" -ForegroundColor Cyan
Write-Host ""

# Set password for psql
$env:PGPASSWORD = $dbPassword

try {
    # Check if database exists
    Write-Host "Checking if database '$dbName' exists..." -ForegroundColor Yellow
    $dbCheck = & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d postgres -t -c "SELECT 1 FROM pg_database WHERE datname = '$dbName';" 2>&1

    if ($LASTEXITCODE -ne 0 -or -not ($dbCheck -match '1')) {
        Write-Host "[ERROR] Database '$dbName' does not exist" -ForegroundColor Red
        Write-Host "[SOLUTION] Run: scripts/setup_postgresql_test_db.ps1" -ForegroundColor Yellow
        exit 1
    }

    Write-Host "[OK] Database '$dbName' exists" -ForegroundColor Green
    Write-Host ""

    # Apply migration
    $migrationFile = Join-Path -Path $PSScriptRoot -ChildPath ".." | Join-Path -ChildPath "db" | Join-Path -ChildPath "migrations" | Join-Path -ChildPath "011_add_container_item_instance_id.sql"

    if (-not (Test-Path $migrationFile)) {
        Write-Host "[ERROR] Migration file not found: $migrationFile" -ForegroundColor Red
        exit 1
    }

    Write-Host "Applying container migration..." -ForegroundColor Yellow
    $migrationResult = & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d $dbName -f $migrationFile 2>&1

    if ($LASTEXITCODE -eq 0) {
        Write-Host "[OK] Container migration applied successfully" -ForegroundColor Green
    } else {
        # Check if error is because column already exists (migration already applied)
        if ($migrationResult -match 'already exists|duplicate') {
            Write-Host "[OK] Migration already applied (column/table already exists)" -ForegroundColor Green
        } else {
            Write-Host "[ERROR] Failed to apply migration: $migrationResult" -ForegroundColor Red
            exit 1
        }
    }

    Write-Host ""
    Write-Host "Migration completed successfully! ✓" -ForegroundColor Green

} catch {
    $errorMessage = $_.Exception.Message
    Write-Host "[ERROR] Migration failed: $errorMessage" -ForegroundColor Red
    exit 1
} finally {
    Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue
}
