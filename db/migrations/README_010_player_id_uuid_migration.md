# Migration 010: player_id UUID Migration

## Overview

This migration converts `player_id` from `VARCHAR(255)` to `UUID` type across all tables in the database. This is a
**clean cutover** with **no backward compatibility** - all code has been updated to use UUID types exclusively.

## Purpose

**Type Safety**: UUID type ensures all player IDs are valid UUIDs

**Consistency**: Matches `user_id` type (UUID) for consistency

**Performance**: UUID type is more efficient for indexing and joins

**Code Clarity**: Eliminates string conversion code throughout the codebase

## Affected Tables

### Primary Table

`players.player_id` - Primary key conversion

### Dependent Tables (Foreign Keys)

`player_inventories.player_id`

- `player_sanity.player_id`
- `sanity_adjustment_log.player_id`
- `sanity_exposure_state.player_id`
- `sanity_cooldowns.player_id`
- `player_channel_preferences.player_id`

## Migration Process

The migration script (`010_migrate_player_id_to_uuid.sql`) performs the following steps:

1. **Verification**: Checks current state of `players.player_id` column
2. **Drop Foreign Keys**: Temporarily removes foreign key constraints from dependent tables
3. **Convert Dependent Tables**: Converts all dependent table `player_id` columns to UUID
4. **Convert Primary Table**: Converts `players.player_id` to UUID
5. **Re-add Foreign Keys**: Restores foreign key constraints

## Prerequisites

All existing `player_id` values must be valid UUID strings (format: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`)

- Database must be PostgreSQL (UUID type is PostgreSQL-specific)
- All application code must already be updated to use UUID types (completed in code migration)

## Usage

### Apply Migration

```powershell
# Set PostgreSQL password

$env:PGPASSWORD = "your_password"

# Apply to specific database

Get-Content .\db\migrations\010_migrate_player_id_to_uuid.sql | psql -h localhost -U postgres -d mythos_dev

# Or apply to all databases

Get-Content .\db\migrations\010_migrate_player_id_to_uuid.sql | psql -h localhost -U postgres -d mythos_unit
Get-Content .\db\migrations\010_migrate_player_id_to_uuid.sql | psql -h localhost -U postgres -d mythos_e2e
```

### Verify Migration

```sql
-- Check players table
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'players' AND column_name = 'player_id';
-- Should return: player_id | uuid

-- Check dependent tables
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE column_name = 'player_id'
ORDER BY table_name;
-- All should return: uuid
```

## Rollback

**⚠️ WARNING**: This migration is designed as a clean cutover. Rollback is not recommended and would require:

1. Converting all UUID values back to VARCHAR
2. Reverting all code changes
3. Updating all dependent tables

If rollback is absolutely necessary, create a reverse migration that:

- Converts UUID back to VARCHAR(255)
- Updates all dependent tables
- Re-adds foreign key constraints

## Code Changes

All application code has been updated to use `uuid.UUID` type:

✅ `server/models/player.py` - Player model uses UUID

✅ `server/persistence.py` - All methods accept UUID

✅ `server/async_persistence.py` - All methods accept UUID

✅ `server/game/player_service.py` - All methods accept UUID

- ✅ `server/services/*` - All service methods accept UUID
- ✅ `server/api/players.py` - API endpoints parse UUID from path
- ✅ `server/api/real_time.py` - Real-time endpoints use UUID
- ✅ `server/realtime/connection_manager.py` - All methods use UUID
- ✅ `server/realtime/websocket_handler.py` - Uses UUID
- ✅ `server/realtime/sse_handler.py` - Uses UUID

## Testing

After applying the migration:

1. **Verify Schema**: Check that all `player_id` columns are UUID type
2. **Test Queries**: Ensure all player lookups work correctly
3. **Test Foreign Keys**: Verify foreign key relationships are intact
4. **Test API**: Test all player-related API endpoints
5. **Test WebSocket**: Verify WebSocket connections work with UUID player_id

## Notes

The migration validates that all existing `player_id` values are valid UUIDs before conversion

- Foreign key constraints are temporarily dropped and re-added to ensure type compatibility
- The migration is idempotent - it can be run multiple times safely (will skip if already UUID)
