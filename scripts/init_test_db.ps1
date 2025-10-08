#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Initialize the test database for MythosMUD

.DESCRIPTION
    This script initializes the test database using the unified database
    initialization script. It creates the database at data/unit_test/players/unit_test_players.db
    with the current schema including case-insensitive unique constraints.

.EXAMPLE
    .\init_test_db.ps1
#>

param()

# Get the script directory
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent $ScriptDir

# Set the test database path
$TestDbPath = Join-Path $ProjectRoot "server\tests\data\players\unit_test_players.db"

Write-Host "Initializing MythosMUD Test Database..." -ForegroundColor Green
Write-Host "Database path: $TestDbPath" -ForegroundColor Yellow

# Change to project root directory
Set-Location $ProjectRoot

# Run the unified database initialization script
try {
    python scripts\init_database.py $TestDbPath
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n✅ Test database initialized successfully!" -ForegroundColor Green
    }
    else {
        Write-Host "`n❌ Test database initialization failed!" -ForegroundColor Red
        exit 1
    }
}
catch {
    Write-Host "`n❌ Error initializing test database: $_" -ForegroundColor Red
    exit 1
}
