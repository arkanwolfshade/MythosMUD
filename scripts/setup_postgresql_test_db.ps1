#!/usr/bin/env pwsh
# MythosMUD PostgreSQL Test Database Setup Script
# Creates and initializes the PostgreSQL test database

param(
    [switch]$Force,
    [switch]$Verbose
)

$ErrorActionPreference = "Stop"

Write-Host "MythosMUD PostgreSQL Test Database Setup" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Green
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

    if ($LASTEXITCODE -eq 0 -and ($dbCheck -match '1')) {
        if ($Force) {
            Write-Host "[INFO] Database exists. Dropping (Force mode)..." -ForegroundColor Yellow
            $dropResult = & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d postgres -c "DROP DATABASE $dbName;" 2>&1
            if ($LASTEXITCODE -ne 0) {
                Write-Host "[ERROR] Failed to drop database: $dropResult" -ForegroundColor Red
                exit 1
            }
            Write-Host "[OK] Database dropped" -ForegroundColor Green
        } else {
            Write-Host "[OK] Database '$dbName' already exists" -ForegroundColor Green
            Write-Host "[INFO] Use -Force to recreate the database" -ForegroundColor Cyan
            exit 0
        }
    }

    # Create database
    Write-Host "Creating database '$dbName'..." -ForegroundColor Yellow
    $createResult = & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d postgres -c "CREATE DATABASE $dbName;" 2>&1

    if ($LASTEXITCODE -eq 0) {
        Write-Host "[OK] Database '$dbName' created successfully" -ForegroundColor Green
    } else {
        if ($createResult -match 'already exists') {
            Write-Host "[WARNING] Database already exists (may have been created concurrently)" -ForegroundColor Yellow
        } else {
            Write-Host "[ERROR] Failed to create database: $createResult" -ForegroundColor Red
            exit 1
        }
    }

    # Note: Schema initialization is handled by DDL scripts, not this script
    # The database will be initialized when tests run or when DDL scripts are executed
    Write-Host ""
    Write-Host "[INFO] Database created. Schema will be initialized by DDL scripts or test fixtures." -ForegroundColor Cyan
    Write-Host "[INFO] You may need to run database initialization scripts separately." -ForegroundColor Cyan

    Write-Host ""
    Write-Host "Setup completed successfully! ✓" -ForegroundColor Green
    Write-Host "You can now run: scripts/check_postgresql.ps1 to verify the connection" -ForegroundColor Cyan

} catch {
    Write-Host "[ERROR] Setup failed: $_" -ForegroundColor Red
    exit 1
} finally {
    Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue
}
