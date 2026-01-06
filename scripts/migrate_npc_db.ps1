# MythosMUD NPC Database Migration Script
# Applies the rename_players_to_population migration to NPC databases
# This renames min_players/max_players to min_population/max_population in npc_spawn_rules

# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
param(
    [string]$Environment = "local"
)

Write-Host "=== MythosMUD NPC Database Migration ===" -ForegroundColor Cyan
Write-Host "Applying rename_players_to_population migration" -ForegroundColor Cyan
Write-Host ""

# Determine database path based on environment
$dbPath = switch ($Environment) {
    "local" { "data\local\npcs\local_npcs.db" }
    "e2e_test" { "data\e2e_test\npcs\e2e_test_npcs.db" }
    "unit_test" { "data\unit_test\npcs\unit_test_npcs.db" }
    default {
        Write-Host "❌ Invalid environment: $Environment" -ForegroundColor Red
        Write-Host "Valid options: local, e2e_test, unit_test" -ForegroundColor Yellow
        exit 1
    }
}

# Check if database exists
if (-not (Test-Path $dbPath)) {
    Write-Host "❌ Database not found: $dbPath" -ForegroundColor Red
    exit 1
}

Write-Host "✓ Found database: $dbPath" -ForegroundColor Green

# Create backup
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$backupPath = "$dbPath.backup.$timestamp"
Copy-Item $dbPath $backupPath
Write-Host "✓ Backup created: $backupPath" -ForegroundColor Green

# Check current schema
Write-Host ""
Write-Host "Checking current schema..." -ForegroundColor Yellow
$currentSchema = sqlite3 $dbPath "PRAGMA table_info(npc_spawn_rules);"
if ($currentSchema -match "min_players") {
    Write-Host "✓ Found old schema with min_players/max_players columns" -ForegroundColor Yellow
}
elseif ($currentSchema -match "min_population") {
    Write-Host "⚠️  Database already has min_population/max_population columns" -ForegroundColor Yellow
    Write-Host "Migration may have already been applied" -ForegroundColor Yellow
    $response = Read-Host "Continue anyway? (y/n)"
    if ($response -ne "y") {
        Write-Host "Migration cancelled" -ForegroundColor Yellow
        exit 0
    }
}
else {
    Write-Host "❌ npc_spawn_rules table not found or has unexpected schema" -ForegroundColor Red
    exit 1
}

# Apply migration
Write-Host ""
Write-Host "Applying migration..." -ForegroundColor Yellow

# Create temporary SQL file
$tempSqlFile = [System.IO.Path]::GetTempFileName() + ".sql"
$migrationSQL = @'
-- Create temporary table with new column names
CREATE TABLE npc_spawn_rules_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    npc_definition_id INTEGER NOT NULL,
    sub_zone_id TEXT NOT NULL,
    min_population INTEGER DEFAULT 0 NOT NULL,
    max_population INTEGER DEFAULT 999 NOT NULL,
    spawn_conditions TEXT NOT NULL DEFAULT '{}',
    FOREIGN KEY (npc_definition_id) REFERENCES npc_definitions(id) ON DELETE CASCADE
);

-- Copy data from old table to new table
INSERT INTO npc_spawn_rules_new (id, npc_definition_id, sub_zone_id, min_population, max_population, spawn_conditions)
SELECT id, npc_definition_id, sub_zone_id, min_players, max_players, spawn_conditions
FROM npc_spawn_rules;

-- Drop old table
DROP TABLE npc_spawn_rules;

-- Rename new table to old table name
ALTER TABLE npc_spawn_rules_new RENAME TO npc_spawn_rules;

-- Recreate indexes
CREATE INDEX IF NOT EXISTS idx_npc_spawn_rules_sub_zone ON npc_spawn_rules(sub_zone_id);
CREATE INDEX IF NOT EXISTS idx_npc_spawn_rules_npc_def ON npc_spawn_rules(npc_definition_id);
'@

# Write SQL to temp file
Set-Content -Path $tempSqlFile -Value $migrationSQL -Encoding UTF8

# Execute migration
sqlite3 $dbPath ".read $tempSqlFile"

# Clean up temp file
Remove-Item $tempSqlFile -Force

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Migration applied successfully" -ForegroundColor Green
}
else {
    Write-Host "❌ Migration failed" -ForegroundColor Red
    Write-Host "Restoring from backup..." -ForegroundColor Yellow
    Copy-Item $backupPath $dbPath -Force
    Write-Host "✓ Database restored from backup" -ForegroundColor Green
    exit 1
}

# Verify new schema
Write-Host ""
Write-Host "Verifying new schema..." -ForegroundColor Yellow
$newSchema = sqlite3 $dbPath "PRAGMA table_info(npc_spawn_rules);"
if ($newSchema -match "min_population") {
    Write-Host "✓ Schema verified: min_population/max_population columns present" -ForegroundColor Green
}
else {
    Write-Host "❌ Schema verification failed" -ForegroundColor Red
    Write-Host "Restoring from backup..." -ForegroundColor Yellow
    Copy-Item $backupPath $dbPath -Force
    Write-Host "✓ Database restored from backup" -ForegroundColor Green
    exit 1
}

Write-Host ""
Write-Host "=== Migration Complete ===" -ForegroundColor Green
Write-Host "Backup retained at: $backupPath" -ForegroundColor Cyan
