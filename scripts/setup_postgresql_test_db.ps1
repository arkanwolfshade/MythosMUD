#!/usr/bin/env pwsh
# MythosMUD PostgreSQL Test Database Setup Script
# Creates and initializes the PostgreSQL test database

# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
param(
    [switch]$Force,
    # Env file under project root (e.g. .env.unit_test, .env.e2e_test) or absolute path
    [string]$EnvFile = ".env.unit_test"
)

$ErrorActionPreference = "Stop"

Write-Host "MythosMUD PostgreSQL Test Database Setup" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Green
Write-Host ""

# Load database URL from env file (default: .env.unit_test at project root)
$ProjectRoot = Split-Path $PSScriptRoot -Parent
$TestEnvPath = if ([System.IO.Path]::IsPathRooted($EnvFile)) {
    $EnvFile
}
else {
    Join-Path -Path $ProjectRoot -ChildPath $EnvFile
}

if (-not (Test-Path $TestEnvPath)) {
    Write-Host "[ERROR] Env file not found at: $TestEnvPath" -ForegroundColor Red
    Write-Host "[SOLUTION] Run: make setup-test-env  (or copy env.e2e_test.example to .env.e2e_test)" -ForegroundColor Yellow
    exit 1
}

Write-Host "[INFO] Loading configuration from $TestEnvPath" -ForegroundColor Cyan
$envContent = Get-Content $TestEnvPath -Raw

$databaseUrl = ""
if ($envContent -match 'DATABASE_URL=(.+)') {
    $databaseUrl = $matches[1].Trim()
}
else {
    Write-Host "[ERROR] DATABASE_URL not found in env file: $TestEnvPath" -ForegroundColor Red
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

$allowedDbs = @("mythos_unit", "mythos_e2e", "mythos_dev")
if ($dbName -notin $allowedDbs) {
    Write-Host "[ERROR] DATABASE_URL database name '$dbName' is not allowed; refusing to create or drop." -ForegroundColor Red
    Write-Host "[INFO] Allowed names: $($allowedDbs -join ', ')" -ForegroundColor Yellow
    exit 1
}

$envLeaf = Split-Path -Leaf $TestEnvPath
if ($Force -and ($envLeaf -eq '.env.e2e_test') -and ($dbName -ne 'mythos_e2e')) {
    Write-Host "[ERROR] With -Force and .env.e2e_test, DATABASE_URL must use database mythos_e2e (got '$dbName')." -ForegroundColor Red
    exit 1
}

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
}
else {
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
            if ($dbName -in @("mythos_unit", "mythos_e2e")) {
                Write-Host "[INFO] Terminating other sessions on '$dbName' before drop..." -ForegroundColor Yellow
                $terminateSql = @"
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = '$dbName' AND pid <> pg_backend_pid();
"@
                $null = & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d postgres -c $terminateSql 2>&1
                Start-Sleep -Seconds 1
            }
            $dropResult = & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d postgres -c "DROP DATABASE $dbName;" 2>&1
            if ($LASTEXITCODE -ne 0) {
                Write-Host "[ERROR] Failed to drop database: $dropResult" -ForegroundColor Red
                exit 1
            }
            Write-Host "[OK] Database dropped" -ForegroundColor Green
        }
        else {
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
    }
    else {
        if ($createResult -match 'already exists') {
            Write-Host "[WARNING] Database already exists (may have been created concurrently)" -ForegroundColor Yellow
        }
        else {
            Write-Host "[ERROR] Failed to create database: $createResult" -ForegroundColor Red
            exit 1
        }
    }

    # Apply environment-specific DDL (db/mythos_<dbname>_ddl.sql)
    if ($dbName -in $allowedDbs) {
        $schemaFile = Join-Path -Path (Join-Path -Path $ProjectRoot -ChildPath "db") -ChildPath "${dbName}_ddl.sql"
        if (Test-Path $schemaFile) {
            Write-Host "Applying environment DDL ($dbName)..." -ForegroundColor Yellow
            $schemaResult = & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d $dbName -f $schemaFile 2>&1
            if ($LASTEXITCODE -eq 0) {
                Write-Host "[OK] DDL applied ($schemaFile)" -ForegroundColor Green
            }
            else {
                Write-Host "[WARNING] Failed to apply DDL: $schemaResult" -ForegroundColor Yellow
                Write-Host "[INFO] Schema may be initialized by test fixtures instead" -ForegroundColor Cyan
            }
        }
        else {
            Write-Host "[INFO] DDL file not found: $schemaFile" -ForegroundColor Cyan
        }
    }
    else {
        Write-Host "[INFO] Database $dbName not in (mythos_unit, mythos_e2e, mythos_dev); skipping DDL" -ForegroundColor Cyan
    }

    # Apply container table creation migration (must run before 011)
    $migration012File = Join-Path -Path $PSScriptRoot -ChildPath ".." | Join-Path -ChildPath "db" | Join-Path -ChildPath "migrations" | Join-Path -ChildPath "012_create_containers_table.sql"
    if (Test-Path $migration012File) {
        Write-Host "Applying container table creation migration (012)..." -ForegroundColor Yellow
        $migrationResult = & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d $dbName -v ON_ERROR_STOP=1 -f $migration012File 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "[OK] Container table creation migration applied" -ForegroundColor Green
        }
        else {
            Write-Host "[ERROR] Failed to apply container table creation migration: $migrationResult" -ForegroundColor Red
            exit 1
        }
    }
    else {
        Write-Host "[WARNING] Container table creation migration file not found: $migration012File" -ForegroundColor Yellow
    }

    # Apply container schema normalization migration (adds container_item_instance_id column)
    $migrationFile = Join-Path -Path $PSScriptRoot -ChildPath ".." | Join-Path -ChildPath "db" | Join-Path -ChildPath "migrations" | Join-Path -ChildPath "011_add_container_item_instance_id.sql"
    if (Test-Path $migrationFile) {
        Write-Host "Applying container schema normalization migration (011)..." -ForegroundColor Yellow
        $migrationResult = & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d $dbName -v ON_ERROR_STOP=1 -f $migrationFile 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "[OK] Container schema normalization migration applied" -ForegroundColor Green
        }
        else {
            Write-Host "[ERROR] Failed to apply container schema normalization migration: $migrationResult" -ForegroundColor Red
            exit 1
        }
    }
    else {
        Write-Host "[WARNING] Container schema normalization migration file not found: $migrationFile" -ForegroundColor Yellow
    }

    # Authoritative seed (world, NPC definitions, items, etc.) lives in data/db/<dbname>_dml.sql
    $dmlFile = Join-Path -Path $ProjectRoot -ChildPath "data\db\${dbName}_dml.sql"
    if (Test-Path $dmlFile) {
        Write-Host "Loading environment DML ($dbName)..." -ForegroundColor Yellow
        $dmlResult = & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d $dbName -v ON_ERROR_STOP=1 -f $dmlFile 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "[OK] DML applied ($dmlFile)" -ForegroundColor Green
        }
        else {
            Write-Host "[ERROR] Failed to apply DML: $dmlResult" -ForegroundColor Red
            exit 1
        }
    }
    else {
        Write-Host "[INFO] DML file not found (skipping): $dmlFile" -ForegroundColor Cyan
    }

    Write-Host ""
    Write-Host "Setup completed successfully!" -ForegroundColor Green
    Write-Host "You can now run: scripts/check_postgresql.ps1 to verify the connection" -ForegroundColor Cyan

}
catch {
    Write-Host "[ERROR] Setup failed: $_" -ForegroundColor Red
    exit 1
}
finally {
    Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue
}
