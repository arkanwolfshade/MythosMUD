# Load seed data into PostgreSQL database with FK validation
# This script checks for FK violations, loads seed data, and verifies integrity

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

Write-Host "=== MythosMUD Seed Data Loader ===" -ForegroundColor Cyan
Write-Host "Database: $DB_NAME" -ForegroundColor Yellow

# Set password environment variable
$env:PGPASSWORD = $PGPASSWORD

# Check for FK violations before loading
Write-Host "`nChecking for foreign key violations..." -ForegroundColor Cyan

$violations = & $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -t -A -c @"
SELECT
    CASE
        WHEN EXISTS (SELECT 1 FROM players WHERE profession_id IS NOT NULL AND profession_id NOT IN (SELECT id FROM professions))
        THEN 'VIOLATION: Players with invalid profession_id'
        ELSE 'OK: No invalid profession_id in players'
    END
UNION ALL
SELECT
    CASE
        WHEN EXISTS (SELECT 1 FROM item_instances WHERE prototype_id NOT IN (SELECT prototype_id FROM item_prototypes))
        THEN 'VIOLATION: Item instances with invalid prototype_id'
        ELSE 'OK: No invalid prototype_id in item_instances'
    END;
"@

Write-Host $violations

# Check if seed tables are empty
Write-Host "`nChecking seed table status..." -ForegroundColor Cyan
$profCount = & $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -t -A -c "SELECT COUNT(*) FROM professions;"
$itemCount = & $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -t -A -c "SELECT COUNT(*) FROM item_prototypes;"
$npcCount = & $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -t -A -c "SELECT COUNT(*) FROM npc_definitions;"

Write-Host "  Professions: $($profCount.Trim())" -ForegroundColor $(if ([int]$profCount.Trim() -eq 0) { "Red" } else { "Green" })
Write-Host "  Item Prototypes: $($itemCount.Trim())" -ForegroundColor $(if ([int]$itemCount.Trim() -eq 0) { "Red" } else { "Green" })
Write-Host "  NPC Definitions: $($npcCount.Trim())" -ForegroundColor $(if ([int]$npcCount.Trim() -eq 0) { "Red" } else { "Green" })

# Load professions
Write-Host "`nLoading professions..." -ForegroundColor Yellow
$result = & $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -f "data\seed\01_professions.sql" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to load professions" -ForegroundColor Red
    Write-Host $result
    exit 1
}
Write-Host "  Professions loaded successfully" -ForegroundColor Green

# Load item prototypes
Write-Host "`nLoading item prototypes..." -ForegroundColor Yellow
$result = & $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -f "data\seed\02_item_prototypes.sql" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to load item prototypes" -ForegroundColor Red
    Write-Host $result
    exit 1
}
Write-Host "  Item prototypes loaded successfully" -ForegroundColor Green

# Load NPC definitions
Write-Host "`nLoading NPC definitions..." -ForegroundColor Yellow
$result = & $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -f "data\seed\03_npc_definitions.sql" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to load NPC definitions" -ForegroundColor Red
    Write-Host $result
    exit 1
}
Write-Host "  NPC definitions loaded successfully" -ForegroundColor Green

# Verify data was loaded
Write-Host "`n=== Final Verification ===" -ForegroundColor Cyan
$profCount = & $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -t -A -c "SELECT COUNT(*) FROM professions;"
$itemCount = & $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -t -A -c "SELECT COUNT(*) FROM item_prototypes;"
$npcCount = & $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -t -A -c "SELECT COUNT(*) FROM npc_definitions;"

Write-Host "`nResults:" -ForegroundColor Green
Write-Host "  Professions: $($profCount.Trim())" -ForegroundColor White
Write-Host "  Item Prototypes: $($itemCount.Trim())" -ForegroundColor White
Write-Host "  NPC Definitions: $($npcCount.Trim())" -ForegroundColor White

# Verify FK integrity
Write-Host "`nVerifying foreign key integrity..." -ForegroundColor Cyan
$fkCheck = & $PSQL_PATH -h $DB_HOST -U $DB_USER -d $DB_NAME -t -A -c @"
SELECT
    CASE
        WHEN EXISTS (SELECT 1 FROM players WHERE profession_id IS NOT NULL AND profession_id NOT IN (SELECT id FROM professions))
        THEN 'FAIL: Players with invalid profession_id'
        ELSE 'PASS: All profession_id values valid'
    END
UNION ALL
SELECT
    CASE
        WHEN EXISTS (SELECT 1 FROM item_instances WHERE prototype_id NOT IN (SELECT prototype_id FROM item_prototypes))
        THEN 'FAIL: Item instances with invalid prototype_id'
        ELSE 'PASS: All prototype_id values valid'
    END;
"@

Write-Host $fkCheck

Write-Host "`n=== Seed data loading complete! ===" -ForegroundColor Green
