# MythosMUD Database Initialization Script
# PowerShell script to create and initialize both production and test databases

Write-Host "Initializing MythosMUD databases..." -ForegroundColor Green

# Check if server is running and stop it if necessary
Write-Host "Checking if MythosMUD server is running..." -ForegroundColor Yellow
$serverProcesses = Get-Process | Where-Object { $_.ProcessName -like "*python*" -or $_.ProcessName -like "*uvicorn*" } -ErrorAction SilentlyContinue

if ($serverProcesses) {
    Write-Host "⚠️  MythosMUD server is running. Stopping server to unlock database..." -ForegroundColor Yellow
    try {
        # Try to stop server gracefully first
        .\scripts\stop_server.ps1
        Start-Sleep -Seconds 3
    } catch {
        Write-Host "⚠️  Could not stop server gracefully. Force stopping processes..." -ForegroundColor Yellow
        Get-Process | Where-Object { $_.ProcessName -like "*python*" -or $_.ProcessName -like "*uvicorn*" } | Stop-Process -Force
        Start-Sleep -Seconds 2
    }
    Write-Host "✓ Server stopped" -ForegroundColor Green
} else {
    Write-Host "✓ Server is not running" -ForegroundColor Green
}

# Create directories if they don't exist
$prodDir = "../../data/players"
$testDir = "./tests/data/players"

if (!(Test-Path $prodDir)) {
    New-Item -ItemType Directory -Path $prodDir -Force
    Write-Host "✓ Created production database directory" -ForegroundColor Green
}

if (!(Test-Path $testDir)) {
    New-Item -ItemType Directory -Path $testDir -Force
    Write-Host "✓ Created test database directory" -ForegroundColor Green
}

# Check if sqlite3 is available
try {
    $sqliteVersion = sqlite3 --version 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ SQLite3 found: $sqliteVersion" -ForegroundColor Green
    } else {
        throw "SQLite3 not found"
    }
} catch {
    Write-Host "❌ SQLite3 not found. Please install SQLite3 and add it to your PATH." -ForegroundColor Red
    Write-Host "You can download it from: https://www.sqlite.org/download.html" -ForegroundColor Yellow
    exit 1
}

# Initialize production database
$prodDb = "$prodDir/players.db"
Write-Host "Initializing production database: $prodDb" -ForegroundColor Yellow

if (Test-Path $prodDb) {
    Write-Host "⚠️  Production database already exists. Backing up..." -ForegroundColor Yellow
    $backupPath = "$prodDb.backup.$(Get-Date -Format 'yyyyMMdd_HHmmss')"
    Copy-Item $prodDb $backupPath
    Write-Host "✓ Backup created: $backupPath" -ForegroundColor Green
}

# Drop all existing objects and recreate schema
Write-Host "Dropping all existing database objects..." -ForegroundColor Yellow

# First, try to drop tables if they exist
$dropCommands = @"
DROP TABLE IF EXISTS invites;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS users;
"@

$dropCommands | sqlite3 $prodDb

# If database is corrupted or locked, recreate it completely
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  Database may be locked or corrupted. Recreating database file..." -ForegroundColor Yellow
    if (Test-Path $prodDb) {
        Remove-Item $prodDb -Force
    }
}

# Create fresh schema
Get-Content ./sql/schema.sql | sqlite3 $prodDb
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Production database initialized successfully" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to initialize production database" -ForegroundColor Red
    exit 1
}

# Initialize test database
$testDb = "$testDir/test_players.db"
Write-Host "Initializing test database: $testDb" -ForegroundColor Yellow

if (Test-Path $testDb) {
    Write-Host "⚠️  Test database already exists. Removing..." -ForegroundColor Yellow
    Remove-Item $testDb -Force
}

# Create test database with clean schema
Write-Host "Creating test database with clean schema..." -ForegroundColor Yellow
Get-Content ./sql/schema.sql | sqlite3 $testDb
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Test database initialized successfully" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to initialize test database" -ForegroundColor Red
    exit 1
}

# Verify both databases
Write-Host "`nVerifying database schemas..." -ForegroundColor Green

Write-Host "Production database tables:" -ForegroundColor Yellow
sqlite3 $prodDb ".tables"

Write-Host "`nTest database tables:" -ForegroundColor Yellow
sqlite3 $testDb ".tables"

Write-Host "`n🎉 Database initialization completed successfully!" -ForegroundColor Green
Write-Host "Both databases now contain: users, players, invites tables" -ForegroundColor Green
