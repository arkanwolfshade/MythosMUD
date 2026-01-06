#!/usr/bin/env pwsh
# MythosMUD PostgreSQL Connection Diagnostic Script
# Checks PostgreSQL connectivity and configuration for tests
# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and diagnostic messages require Write-Host for proper display')]

param(
    [string]$DatabaseUrl = "",
    [switch]$Verbose
)

$ErrorActionPreference = "Stop"

Write-Host "MythosMUD PostgreSQL Diagnostic" -ForegroundColor Green
Write-Host "===============================" -ForegroundColor Green
Write-Host ""

# Load database URL from .env.unit_test if not provided
if (-not $DatabaseUrl) {
    $TestEnvPath = Join-Path -Path $PSScriptRoot -ChildPath ".." | Join-Path -ChildPath "server" | Join-Path -ChildPath "tests" | Join-Path -ChildPath ".env.unit_test"

    if (Test-Path $TestEnvPath) {
        Write-Host "[INFO] Loading DATABASE_URL from $TestEnvPath" -ForegroundColor Cyan
        $envContent = Get-Content $TestEnvPath -Raw
        if ($envContent -match 'DATABASE_URL=(.+)') {
            $DatabaseUrl = $matches[1].Trim()
        }
        else {
            Write-Host "[ERROR] DATABASE_URL not found in .env.unit_test" -ForegroundColor Red
            exit 1
        }
    }
    else {
        Write-Host "[ERROR] .env.unit_test file not found at: $TestEnvPath" -ForegroundColor Red
        Write-Host "[SOLUTION] Run: make setup-test-env" -ForegroundColor Yellow
        exit 1
    }
}

# Parse PostgreSQL URL
# Format: postgresql+asyncpg://user:password@host:port/database
if ($DatabaseUrl -notmatch 'postgresql\+?asyncpg?://([^:]+):([^@]+)@([^:]+):(\d+)/(.+)') {
    Write-Host "[ERROR] Invalid PostgreSQL URL format: $DatabaseUrl" -ForegroundColor Red
    Write-Host "[EXPECTED] postgresql+asyncpg://user:password@host:port/database" -ForegroundColor Yellow
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
Write-Host "  Password: [REDACTED]" -ForegroundColor Gray
Write-Host ""

# Check if psql is available
$psqlPath = Get-Command psql -ErrorAction SilentlyContinue
if (-not $psqlPath) {
    Write-Host "[WARNING] psql command not found in PATH" -ForegroundColor Yellow
    Write-Host "[INFO] Attempting to find PostgreSQL installation..." -ForegroundColor Cyan

    # Common PostgreSQL installation paths on Windows
    $commonPaths = @(
        "C:\Program Files\PostgreSQL\*\bin\psql.exe",
        "C:\Program Files (x86)\PostgreSQL\*\bin\psql.exe"
    )

    $found = $false
    foreach ($path in $commonPaths) {
        $psqlFiles = Get-ChildItem -Path $path -ErrorAction SilentlyContinue
        if ($psqlFiles) {
            $psqlPath = $psqlFiles[0].FullName
            Write-Host "[INFO] Found psql at: $psqlPath" -ForegroundColor Green
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

# Test 1: Check if PostgreSQL service is running
Write-Host "Test 1: Checking PostgreSQL service status..." -ForegroundColor Yellow
$pgService = Get-Service -Name "*postgresql*" -ErrorAction SilentlyContinue
if ($pgService) {
    $running = $pgService | Where-Object { $_.Status -eq 'Running' }
    if ($running) {
        Write-Host "  [OK] PostgreSQL service is running" -ForegroundColor Green
    }
    else {
        Write-Host "  [ERROR] PostgreSQL service is not running" -ForegroundColor Red
        Write-Host "  [SOLUTION] Start PostgreSQL service:" -ForegroundColor Yellow
        Write-Host "    Start-Service -Name '$($pgService[0].Name)'" -ForegroundColor Cyan
        exit 1
    }
}
else {
    Write-Host "  [WARNING] Could not detect PostgreSQL service (may be running as different user)" -ForegroundColor Yellow
}

# Test 2: Check network connectivity
Write-Host "Test 2: Checking network connectivity to $dbHost`:$dbPort..." -ForegroundColor Yellow
try {
    $tcpClient = New-Object System.Net.Sockets.TcpClient
    $connect = $tcpClient.BeginConnect($dbHost, $dbPort, $null, $null)
    $wait = $connect.AsyncWaitHandle.WaitOne(3000, $false)
    if ($wait) {
        $tcpClient.EndConnect($connect)
        Write-Host "  [OK] Can connect to PostgreSQL server" -ForegroundColor Green
        $tcpClient.Close()
    }
    else {
        Write-Host "  [ERROR] Cannot connect to PostgreSQL server (timeout)" -ForegroundColor Red
        Write-Host "  [SOLUTION] Ensure PostgreSQL is running and listening on $dbHost`:$dbPort" -ForegroundColor Yellow
        exit 1
    }
}
catch {
    Write-Host "  [ERROR] Cannot connect to PostgreSQL server: $_" -ForegroundColor Red
    Write-Host "  [SOLUTION] Ensure PostgreSQL is running and accessible" -ForegroundColor Yellow
    exit 1
}

# Test 3: Check authentication
Write-Host "Test 3: Checking authentication..." -ForegroundColor Yellow
$env:PGPASSWORD = $dbPassword
try {
    $authTest = & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d postgres -c "SELECT version();" 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  [OK] Authentication successful" -ForegroundColor Green
        if ($Verbose) {
            Write-Host "  PostgreSQL version: $($authTest -join ' ')" -ForegroundColor Gray
        }
    }
    else {
        Write-Host "  [ERROR] Authentication failed" -ForegroundColor Red
        Write-Host "  Error output: $authTest" -ForegroundColor Red
        Write-Host "  [SOLUTION] Check PostgreSQL password for user '$dbUser'" -ForegroundColor Yellow
        Write-Host "    You may need to reset the password:" -ForegroundColor Yellow
        Write-Host "    psql -U postgres -c `"ALTER USER $dbUser WITH PASSWORD '$dbPassword';`"" -ForegroundColor Cyan
        exit 1
    }
}
catch {
    Write-Host "  [ERROR] Authentication test failed: $_" -ForegroundColor Red
    exit 1
}
finally {
    Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue
}

# Test 4: Check if database exists
Write-Host "Test 4: Checking if database '$dbName' exists..." -ForegroundColor Yellow
$env:PGPASSWORD = $dbPassword
try {
    $dbCheck = & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d postgres -t -c "SELECT 1 FROM pg_database WHERE datname = '$dbName';" 2>&1
    if ($LASTEXITCODE -eq 0 -and ($dbCheck -match '1')) {
        Write-Host "  [OK] Database '$dbName' exists" -ForegroundColor Green
    }
    else {
        Write-Host "  [WARNING] Database '$dbName' does not exist" -ForegroundColor Yellow
        Write-Host "  [SOLUTION] Create the database:" -ForegroundColor Yellow
        Write-Host "    psql -h $dbHost -p $dbPort -U $dbUser -d postgres -c `"CREATE DATABASE $dbName;`"" -ForegroundColor Cyan
        Write-Host "  Or run: scripts/setup_postgresql_test_db.ps1" -ForegroundColor Cyan
    }
}
catch {
    Write-Host "  [ERROR] Could not check database: $_" -ForegroundColor Red
}
finally {
    Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue
}

# Test 5: Check database connection
Write-Host "Test 5: Testing connection to database '$dbName'..." -ForegroundColor Yellow
$env:PGPASSWORD = $dbPassword
try {
    $connTest = & $psqlPath -h $dbHost -p $dbPort -U $dbUser -d $dbName -c "SELECT 1;" 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  [OK] Can connect to database '$dbName'" -ForegroundColor Green
    }
    else {
        Write-Host "  [ERROR] Cannot connect to database '$dbName'" -ForegroundColor Red
        Write-Host "  Error output: $connTest" -ForegroundColor Red
        Write-Host "  [SOLUTION] Ensure database exists and user has permissions" -ForegroundColor Yellow
        exit 1
    }
}
catch {
    Write-Host "  [ERROR] Connection test failed: $_" -ForegroundColor Red
    exit 1
}
finally {
    Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue
}

Write-Host ""
Write-Host "All diagnostic tests passed! ✓" -ForegroundColor Green
Write-Host "PostgreSQL is properly configured for tests." -ForegroundColor Green
