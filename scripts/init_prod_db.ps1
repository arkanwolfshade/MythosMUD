#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Initialize the production database for MythosMUD

.DESCRIPTION
    This script initializes the production database using the unified database
    initialization script. It creates the database at data/local/players/local_players.db
    with the current schema including case-insensitive unique constraints.

.EXAMPLE
    .\init_prod_db.ps1
#>

param()

# Get the script directory
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent $ScriptDir

# Set the production database path
$ProdDbPath = Join-Path $ProjectRoot "data\players\players.db"

Write-Host "Initializing MythosMUD Production Database..." -ForegroundColor Green
Write-Host "Database path: $ProdDbPath" -ForegroundColor Yellow

# Change to project root directory
Set-Location $ProjectRoot

# Run the unified database initialization script
try {
    python scripts\init_database.py $ProdDbPath
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n✅ Production database initialized successfully!" -ForegroundColor Green
    }
    else {
        Write-Host "`n❌ Production database initialization failed!" -ForegroundColor Red
        exit 1
    }
}
catch {
    Write-Host "`n❌ Error initializing production database: $_" -ForegroundColor Red
    exit 1
}
