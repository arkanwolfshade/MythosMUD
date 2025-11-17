# Load seed data into PostgreSQL database
# This script loads all seed data files in the correct order

$ErrorActionPreference = "Stop"

# Load environment variables from .env file
if (Test-Path ".env") {
    Get-Content ".env" | ForEach-Object {
        if ($_ -match '^\s*([^#][^=]+)=(.*)$') {
            $name = $matches[1].Trim()
            $value = $matches[2].Trim()
            [Environment]::SetEnvironmentVariable($name, $value, "Process")
        }
    }
}

# Get database URL from environment
$DATABASE_URL = $env:DATABASE_URL
if (-not $DATABASE_URL) {
    Write-Host "ERROR: DATABASE_URL environment variable not set" -ForegroundColor Red
    exit 1
}

# Parse database URL (postgresql+asyncpg://user:password@host:port/database)
$url = $DATABASE_URL -replace "postgresql\+asyncpg://", "postgresql://" -replace "postgresql\+psycopg2://", "postgresql://"
if ($url -match "postgresql://([^:]+):([^@]+)@([^:]+):(\d+)/(.+)") {
    $DB_USER = $matches[1]
    $PGPASSWORD = $matches[2]
    $DB_HOST = $matches[3]
    $DB_PORT = $matches[4]
    $DB_NAME = $matches[5]
} else {
    Write-Host "ERROR: Could not parse DATABASE_URL" -ForegroundColor Red
    exit 1
}

$PSQL_PATH = "E:\Program Files\PostgreSQL\18\bin\psql.exe"

Write-Host "Loading seed data into $DB_NAME..." -ForegroundColor Cyan

# Set password environment variable
$env:PGPASSWORD = $PGPASSWORD

# Load professions
Write-Host "`nLoading professions..." -ForegroundColor Yellow
& $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -f "data\seed\01_professions.sql"
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to load professions" -ForegroundColor Red
    exit 1
}

# Load item prototypes
Write-Host "`nLoading item prototypes..." -ForegroundColor Yellow
& $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -f "data\seed\02_item_prototypes.sql"
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to load item prototypes" -ForegroundColor Red
    exit 1
}

# Load NPC definitions
Write-Host "`nLoading NPC definitions..." -ForegroundColor Yellow
& $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -f "data\seed\03_npc_definitions.sql"
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to load NPC definitions" -ForegroundColor Red
    exit 1
}

# Verify data was loaded
Write-Host "`nVerifying data..." -ForegroundColor Cyan
$professions = & $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -t -c "SELECT COUNT(*) FROM professions;"
$items = & $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -t -c "SELECT COUNT(*) FROM item_prototypes;"
$npcs = & $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -t -c "SELECT COUNT(*) FROM npc_definitions;"

Write-Host "`nResults:" -ForegroundColor Green
Write-Host "  Professions: $($professions.Trim())" -ForegroundColor White
Write-Host "  Item Prototypes: $($items.Trim())" -ForegroundColor White
Write-Host "  NPC Definitions: $($npcs.Trim())" -ForegroundColor White

Write-Host "`nSeed data loading complete!" -ForegroundColor Green
