# Players Table Migration

This migration aligns the PostgreSQL `players` table with the SQLAlchemy model defined in `server/models/player.py` and the schema in `db/schema/04_runtime_tables.sql`.

## Problem

The current database has a schema mismatch:

- **Current**: `id uuid PRIMARY KEY`, `attributes jsonb`, `sanity_score integer`, `profession_id uuid`, `updated_at timestamptz`
- **Expected**: `player_id varchar(255) PRIMARY KEY`, `stats text`, `inventory text`, `status_effects text`, `current_room_id varchar`, `respawn_room_id varchar`, `experience_points integer`, `level integer`, `is_admin integer`, `profession_id integer`, `last_active timestamptz`

## Migration Steps

1. **Backup**: Creates `players_backup_migration` table with old data
2. **Create New Table**: Creates `players_new` with correct schema
3. **Migrate Data**: Transforms old schema data to new schema
4. **Drop Old Table**: Drops old `players` table (CASCADE handles dependent objects)
5. **Rename**: Renames `players_new` to `players`
6. **Verify**: Checks that migration completed successfully

## Usage

### Apply Migration

```powershell
# Apply to all databases (mythos_dev, mythos_unit, mythos_e2e)
.\db\migration\apply_players_migration.ps1

# Apply to specific database
.\db\migration\apply_players_migration.ps1 -Database mythos_dev
```

### Manual Application

```bash
# Set password
$env:PGPASSWORD = "Cthulhu1"

# Apply to specific database
Get-Content .\db\migration\migrate_players_to_correct_schema.sql | psql -h localhost -U postgres -d mythos_dev
```

### Rollback (if needed)

```bash
Get-Content .\db\migration\rollback_players_migration.sql | psql -h localhost -U postgres -d mythos_dev
```

## Important Notes

1. **Dependent Tables**: The migration uses `DROP TABLE ... CASCADE` which will drop dependent tables like:
   - `player_inventories`
   - `player_sanity`
   - `sanity_adjustment_log`
   - `sanity_exposure_state`
   - `sanity_cooldowns`

   **After migration, you must reapply the schema** to recreate these tables:

   ```bash
   Get-Content .\db\schema\04_runtime_tables.sql | psql -h localhost -U postgres -d mythos_dev
   ```

2. **Data Migration**:
   - `id uuid` → `player_id varchar(255)` (converted to text)
   - `attributes jsonb` + `sanity_score integer` → `stats text` (merged JSON)
   - `updated_at` → `last_active`
   - Missing fields get default values (inventory, status_effects, current_room_id, etc.)

3. **Profession ID**: The migration sets `profession_id` to NULL if it was a UUID, since the new schema expects an integer. You may need to manually map profession UUIDs to integer IDs after migration.

4. **Backup Table**: The `players_backup_migration` table is kept after migration. You can drop it after verifying everything works:

   ```sql
   DROP TABLE IF EXISTS players_backup_migration;
   ```

## Verification

After migration, verify the schema:

```sql
-- Check columns
\d players

-- Check row count
SELECT COUNT(*) FROM players;

-- Verify player_id exists
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'players' AND column_name = 'player_id';
```

## Testing

Test the migration on a non-production database first:

1. Apply to `mythos_unit` (test database)
2. Run tests: `make test`
3. If successful, apply to `mythos_dev` and `mythos_e2e`
