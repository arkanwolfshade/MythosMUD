# Migration 019 Testing Guide

**Date:** 2025-01-14
**Migration:** `019_postgresql_anti_patterns_fixes.sql`

## Overview

This guide provides step-by-step instructions for testing Migration 019 before applying it to production databases.

## Prerequisites

1. **PostgreSQL 10+** (required for `generated always as identity`)
2. **Database backup** (always backup before migrations)
3. **Test database** (use `mythos_dev` or `mythos_unit` for testing)
4. **psql** command-line tool installed

## Testing Steps

### Step 1: Backup Database

**CRITICAL:** Always backup before running migrations.

```powershell
# Backup using pg_dump

pg_dump -h localhost -U postgres -d mythos_dev -F c -f backup_before_019_$(Get-Date -Format 'yyyyMMdd_HHmmss').dump
```

### Step 2: Verify Current State

Check current column types before migration:

```sql
-- Connect to database
psql -h localhost -U postgres -d mythos_dev

-- Check current types
SELECT
    table_name,
    column_name,
    data_type,
    is_identity
FROM information_schema.columns
WHERE table_schema = 'public'
AND table_name IN (
    'professions',
    'sanity_adjustment_log',
    'sanity_exposure_state',
    'sanity_cooldowns',
    'item_component_states',
    'npc_definitions',
    'npc_spawn_rules',
    'npc_relationships',
    'player_spells'
)
AND column_name = 'id'
ORDER BY table_name;
```

**Expected before migration:**

- `data_type` = `integer`
- `is_identity` = `NO` (or NULL)

### Step 3: Apply Migration

#### Option A: Using PowerShell Script (Recommended)

```powershell
# Apply to development database

.\scripts\apply_019_postgresql_anti_patterns_fixes.ps1 -Database "mythos_dev"

# Apply to unit test database

.\scripts\apply_019_postgresql_anti_patterns_fixes.ps1 -Database "mythos_unit"

# Dry run (no changes)

.\scripts\apply_019_postgresql_anti_patterns_fixes.ps1 -Database "mythos_dev" -DryRun
```

#### Option B: Using psql Directly

```powershell
# Set password

$env:PGPASSWORD = "Cthulhu1"

# Apply migration

psql -h localhost -U postgres -d mythos_dev -f db\migrations\019_postgresql_anti_patterns_fixes.sql
```

### Step 4: Verify Migration Results

After migration, verify the changes:

```sql
-- Check that all id columns are now bigint identity
SELECT
    table_name,
    column_name,
    data_type,
    is_identity,
    identity_generation
FROM information_schema.columns
WHERE table_schema = 'public'
AND table_name IN (
    'professions',
    'sanity_adjustment_log',
    'sanity_exposure_state',
    'sanity_cooldowns',
    'item_component_states',
    'npc_definitions',
    'npc_spawn_rules',
    'npc_relationships',
    'player_spells'
)
AND column_name = 'id'
ORDER BY table_name;
```

**Expected after migration:**

- `data_type` = `bigint`
- `is_identity` = `YES`
- `identity_generation` = `ALWAYS`

### Step 5: Verify Foreign Key Types

Check that foreign keys match their referenced primary keys:

```sql
-- Check foreign key types
SELECT
    tc.table_name,
    kcu.column_name,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name,
    c.data_type
FROM information_schema.table_constraints AS tc
JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage AS ccu
    ON ccu.constraint_name = tc.constraint_name
JOIN information_schema.columns AS c
    ON c.table_name = tc.table_name
    AND c.column_name = kcu.column_name
WHERE tc.constraint_type = 'FOREIGN KEY'
AND tc.table_schema = 'public'
AND (
    kcu.column_name IN ('npc_definition_id', 'npc_id_1', 'npc_id_2', 'profession_id')
    OR ccu.table_name IN ('npc_definitions', 'professions')
)
ORDER BY tc.table_name, kcu.column_name;
```

**Expected:**

- All foreign keys should be `bigint` to match their referenced `bigint` primary keys

### Step 6: Verify Text Column Conversions

Check that varchar columns were converted to text:

```sql
-- Check text column conversions
SELECT
    table_name,
    column_name,
    data_type
FROM information_schema.columns
WHERE table_schema = 'public'
AND (
    (table_name = 'users' AND column_name IN ('display_name', 'password_hash'))
    OR (table_name = 'sanity_adjustment_log' AND column_name = 'reason_code')
    OR (table_name = 'sanity_exposure_state' AND column_name = 'entity_archetype')
    OR (table_name = 'sanity_cooldowns' AND column_name = 'action_code')
)
ORDER BY table_name, column_name;
```

**Expected:**

- `data_type` = `text` (not `character varying`)

### Step 7: Verify Comments

Check that table and column comments were added:

```sql
-- Check table comments
SELECT
    schemaname,
    tablename,
    obj_description(c.oid, 'pg_class') AS table_comment
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'public'
AND c.relkind = 'r'
AND tablename IN (
    'users', 'players', 'professions', 'player_lucidity',
    'sanity_adjustment_log', 'sanity_exposure_state', 'sanity_cooldowns'
)
ORDER BY tablename;

-- Check column comments
SELECT
    table_name,
    column_name,
    col_description(c.oid, a.attnum) AS column_comment
FROM pg_attribute a
JOIN pg_class c ON c.oid = a.attrelid
JOIN pg_namespace n ON n.oid = c.relnamespace
JOIN information_schema.columns ic
    ON ic.table_name = c.relname
    AND ic.column_name = a.attname
WHERE n.nspname = 'public'
AND c.relkind = 'r'
AND a.attnum > 0
AND NOT a.attisdropped
AND (
    (table_name = 'users' AND column_name IN ('id', 'email', 'username'))
    OR (table_name = 'players' AND column_name IN ('player_id', 'user_id', 'name'))
    OR (table_name = 'professions' AND column_name IN ('id', 'name'))
)
ORDER BY table_name, column_name;
```

### Step 8: Test Application Functionality

After migration, test that the application still works:

1. **Start the server:**

   ```powershell
   .\scripts\start_local.ps1
   ```

2. **Test key functionality:**

   - Create a new profession
   - Create NPC definitions
   - Record lucidity adjustments
   - Learn player spells
   - Query professions by ID

3. **Run tests:**

   ```powershell
   make test-server
   ```

### Step 9: Test Idempotency

The migration should be idempotent (safe to run multiple times):

```powershell
# Run migration again

.\scripts\apply_019_postgresql_anti_patterns_fixes.ps1 -Database "mythos_dev"

# Should complete without errors
# All checks should show migration already applied

```

### Step 10: Verify Data Integrity

Ensure no data was lost during migration:

```sql
-- Count records in affected tables
SELECT
    'professions' AS table_name,
    COUNT(*) AS record_count
FROM professions
UNION ALL
SELECT 'sanity_adjustment_log', COUNT(*) FROM sanity_adjustment_log
UNION ALL
SELECT 'sanity_exposure_state', COUNT(*) FROM sanity_exposure_state
UNION ALL
SELECT 'sanity_cooldowns', COUNT(*) FROM sanity_cooldowns
UNION ALL
SELECT 'item_component_states', COUNT(*) FROM item_component_states
UNION ALL
SELECT 'npc_definitions', COUNT(*) FROM npc_definitions
UNION ALL
SELECT 'npc_spawn_rules', COUNT(*) FROM npc_spawn_rules
UNION ALL
SELECT 'npc_relationships', COUNT(*) FROM npc_relationships
UNION ALL
SELECT 'player_spells', COUNT(*) FROM player_spells;

-- Verify ID sequences are correct
SELECT
    'professions' AS table_name,
    MAX(id) AS max_id
FROM professions
UNION ALL
SELECT 'sanity_adjustment_log', MAX(id) FROM sanity_adjustment_log
UNION ALL
SELECT 'sanity_exposure_state', MAX(id) FROM sanity_exposure_state
UNION ALL
SELECT 'sanity_cooldowns', MAX(id) FROM sanity_cooldowns
UNION ALL
SELECT 'item_component_states', MAX(id) FROM item_component_states
UNION ALL
SELECT 'npc_definitions', MAX(id) FROM npc_definitions
UNION ALL
SELECT 'npc_spawn_rules', MAX(id) FROM npc_spawn_rules
UNION ALL
SELECT 'npc_relationships', MAX(id) FROM npc_relationships
UNION ALL
SELECT 'player_spells', MAX(id) FROM player_spells;
```

## Rollback Plan

If migration fails or causes issues:

### Option 1: Restore from Backup

```powershell
# Drop and recreate database

dropdb -h localhost -U postgres mythos_dev
createdb -h localhost -U postgres mythos_dev

# Restore from backup

pg_restore -h localhost -U postgres -d mythos_dev backup_before_019_*.dump
```

### Option 2: Manual Rollback (if needed)

The migration converts columns to identity, which cannot be easily reversed. If rollback is needed:

1. Restore from backup (recommended)
2. Or manually convert identity columns back to serial (complex, not recommended)

## Troubleshooting

### Issue: "function convert_serial_to_identity does not exist"

**Solution:** The function is created at the start of the migration. Ensure you're running the complete migration file.

### Issue: "column already has identity"

**Solution:** Migration already applied. This is safe - the migration is idempotent.

### Issue: "cannot alter type of column because there is a default"

**Solution:** The migration handles this by dropping the default first. If this error occurs, check that the migration
function ran correctly.

### Issue: Foreign key constraint violations

**Solution:** The migration updates foreign key types automatically. If errors occur, verify that all referenced tables
were migrated.

## Success Criteria

✅ All `id` columns are `bigint` with `is_identity = YES`
✅ All foreign keys match their referenced primary key types
✅ Text columns converted from `varchar(n)` to `text`
✅ Table and column comments added
✅ No data loss (record counts match)
✅ Application tests pass
✅ Migration is idempotent (can run multiple times)

## Production Deployment Checklist

Before applying to production:

- [ ] Tested on development database
- [ ] Tested on unit test database
- [ ] Verified all application tests pass
- [ ] Created production database backup
- [ ] Scheduled maintenance window (if needed)
- [ ] Notified team of migration
- [ ] Prepared rollback plan
- [ ] Documented any issues found during testing

## Related Documentation

[Migration 019 README](../db/migrations/019_POSTGRESQL_ANTI_PATTERNS_FIXES_README.md)

- [PostgreSQL Anti-Patterns Review](../docs/POSTGRESQL_ANTI_PATTERNS_REVIEW.md)
- [Python Model Updates](../docs/PYTHON_MODEL_UPDATES_REQUIRED.md)
- [Migration Verification](../docs/MIGRATION_019_VERIFICATION.md)
