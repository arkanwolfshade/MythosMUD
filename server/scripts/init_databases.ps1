# MythosMUD Database Initialization Script
# PowerShell script to create and initialize both production and test databases

Write-Host "Initializing MythosMUD databases..." -ForegroundColor Green

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

sqlite3 $prodDb < ./sql/schema.sql
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

sqlite3 $testDb < ./sql/schema.sql
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
