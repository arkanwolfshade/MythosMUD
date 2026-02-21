# Apply all database migrations to mythos_e2e.
# Safe to run multiple times (migrations are idempotent: IF NOT EXISTS / ON CONFLICT DO NOTHING).
# Requires: psql on PATH, PostgreSQL running, mythos_e2e database exists.
# Usage: .\scripts\apply_migrations_to_e2e.ps1

param(
    [string]$DbHost = "localhost",
    [int]$Port = 5432,
    [string]$User = "postgres",
    [string]$Database = "mythos_e2e"
)

$ErrorActionPreference = "Stop"
$projectRoot = if ($PSScriptRoot) { (Get-Item $PSScriptRoot).Parent.FullName } else { Get-Location }
Set-Location $projectRoot

$env:PGPASSWORD = "Cthulhu1"
$psql = "psql"
$uv = "uv"

# DATABASE_URL for Python scripts (sync URL for psycopg2)
$env:DATABASE_URL = "postgresql://${User}:$env:PGPASSWORD@${DbHost}:${Port}/${Database}"

function Invoke-Psql {
    param([string]$FilePath)
    $abs = (Resolve-Path $FilePath).Path
    Write-Host "[APPLY] $FilePath" -ForegroundColor Cyan
    & $psql -h $DbHost -p $Port -U $User -d $Database -f $abs
    if ($LASTEXITCODE -ne 0) { throw "psql failed: $FilePath" }
}

# --- data/db/migrations (04-14; 15 after quest DDL) ---
$dataMigrations = @(
    "data\db\migrations\04_add_backpack_item.sql",
    "data\db\migrations\05_normalize_wear_slots_to_lowercase.sql",
    "data\db\migrations\06_normalize_schedule_effects_to_lowercase.sql",
    "data\db\migrations\07_add_switchblade_weapon.sql",
    "data\db\migrations\08_add_tutorial_instance_id.sql",
    "data\db\migrations\09_update_tutorial_bedroom_no_combat_no_death.sql",
    "data\db\migrations\10_heal_self_heal_other_rename.sql",
    "data\db\migrations\11_migrate_weekday_names.sql",
    "data\db\migrations\12_add_tutorial_bedroom_room.sql",
    "data\db\migrations\13_update_tutorial_bedroom_exit_direction.sql",
    "data\db\migrations\14_add_healing_spells.sql"
)
foreach ($m in $dataMigrations) {
    $p = Join-Path $projectRoot $m
    if (Test-Path $p) { Invoke-Psql -FilePath $p } else { Write-Host "[SKIP] $m (not found)" -ForegroundColor Yellow }
}

# --- Quest DDL + seed (creates quest_definitions, quest_instances, quest_offers) ---
Write-Host "[APPLY] scripts/apply_quest_migrations_to_dev.py" -ForegroundColor Cyan
& $uv run python scripts/apply_quest_migrations_to_dev.py
if ($LASTEXITCODE -ne 0) { throw "apply_quest_migrations_to_dev.py failed" }

# --- data/db/migrations 15 (quest leave_the_tutorial seed) ---
$p15 = Join-Path $projectRoot "data\db\migrations\15_add_quest_leave_the_tutorial.sql"
if (Test-Path $p15) { Invoke-Psql -FilePath $p15 } else { Write-Host "[SKIP] 15_add_quest_leave_the_tutorial.sql (not found)" -ForegroundColor Yellow }

# --- Ensure player_lucidity exists (019 adds comments to it; table comes from base schema) ---
$luciditySql = @"
CREATE TABLE IF NOT EXISTS player_lucidity (
    player_id uuid PRIMARY KEY REFERENCES players (player_id) ON DELETE CASCADE,
    current_lcd integer NOT NULL DEFAULT 100 CHECK (current_lcd >= -100 AND current_lcd <= 100),
    current_tier varchar(32) NOT NULL DEFAULT 'lucid' CHECK (current_tier IN ('lucid','uneasy','fractured','deranged','catatonic')),
    liabilities text NOT NULL DEFAULT '[]',
    last_updated_at timestamptz NOT NULL DEFAULT now(),
    catatonia_entered_at timestamptz
);
CREATE INDEX IF NOT EXISTS idx_player_sanity_tier ON player_lucidity (current_tier);
"@
$luciditySql | & $psql -h $DbHost -p $Port -U $User -d $Database -v ON_ERROR_STOP=1
if ($LASTEXITCODE -ne 0) { Write-Host "[WARN] player_lucidity create skipped or failed (may already exist)" -ForegroundColor Yellow }

# --- db/migrations (015-027) ---
$dbMigrations = @(
    "db\migrations\015_add_magic_system_tables.sql",
    "db\migrations\016_multi_character_support.sql",
    "db\migrations\017_add_ascii_map_fields.sql",
    "db\migrations\018_fix_players_name_constraint.sql",
    "db\migrations\019_postgresql_anti_patterns_fixes.sql",
    "db\migrations\021_add_partial_indexes_for_active_players.sql",
    "db\migrations\023_add_player_effects_table.sql",
    "db\migrations\024_add_skills_table.sql",
    "db\migrations\025_add_player_skills_table.sql",
    "db\migrations\026_add_profession_modifiers.sql",
    "db\migrations\027_add_skill_use_log_table.sql"
)
foreach ($m in $dbMigrations) {
    $p = Join-Path $projectRoot $m
    if (Test-Path $p) { Invoke-Psql -FilePath $p } else { Write-Host "[SKIP] $m (not found)" -ForegroundColor Yellow }
}

Write-Host "`n[OK] All migrations applied to $Database" -ForegroundColor Green
