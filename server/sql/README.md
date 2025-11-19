# Legacy SQL Files

⚠️ **DEPRECATED** - These files are kept for historical reference only.

## Status

This directory contains **legacy SQLite-specific SQL files** that have been replaced by the PostgreSQL authoritative schema approach.

## Files

### Schema Files (SQLite - Deprecated)

- **`items_schema.sql`** - SQLite schema for items system
- **`npc_schema.sql`** - SQLite schema for NPC system

**Status**: ⚠️ **DEPRECATED** - Replaced by `db/authoritative_schema.sql`

### Seed Data Files (SQLite - Deprecated)

- **`items_seed_data.sql`** - SQLite seed data for items
- **`npc_sample_data.sql` - ⚠️ **STILL REFERENCED** - Used by `scripts/populate_npc_sample_data.py`

**Status**:
- `items_seed_data.sql` - ⚠️ **DEPRECATED** - Replaced by `data/db/02_item_prototypes.sql`
- `npc_sample_data.sql` - ⚠️ **LEGACY** - Still referenced but should be migrated to PostgreSQL format

### Migration Files (Mixed - Deprecated)

- **`migrations/001_add_player_channel_preferences.sql`** - SQLite migration (legacy, kept for reference)
- **`migrations/002_add_hashed_password_column.sql`** - PostgreSQL migration (moved to `db/migrations/`, deprecated)
- **`migrations/003_add_used_by_user_id_column.sql`** - PostgreSQL migration (moved to `db/migrations/`, deprecated)
- **`migrations/004_rename_invites_columns.sql`** - PostgreSQL migration (moved to `db/migrations/`, deprecated)
- **`migrations/005_add_fastapi_users_columns.sql`** - PostgreSQL migration (moved to `db/migrations/`, deprecated)
- **`migrations/006_migrate_stats_to_jsonb.sql`** - PostgreSQL migration (moved to `db/migrations/`, deprecated)
- **`migrations/007_fix_professions_table_schema.sql`** - PostgreSQL migration (moved to `db/migrations/`, deprecated)
- **`migrations/008_increase_current_room_id_length.sql`** - PostgreSQL migration (moved to `db/migrations/`, deprecated)
- **`migrations/009_add_password_hash_column.sql`** - PostgreSQL migration (moved to `db/migrations/`, deprecated)

**Status**: ⚠️ **DEPRECATED** - All PostgreSQL migrations (002-009) have been moved to `db/migrations/` and marked as deprecated. SQLite migration 001 is kept for historical reference only.

## Migration Path

### For New Database Setups

**DO NOT** use these files. Instead:
1. Use `db/authoritative_schema.sql` for schema
2. Use `data/db/*.sql` for seed data
3. Use `db/migrations/*.sql` for existing database migrations

### For Existing Databases

If you have an existing SQLite database that needs migration:
1. Review `db/migrations/` for applicable PostgreSQL migrations
2. Use the migration scripts in `db/migrations/` (not `server/sql/migrations/`)

## Why These Files Are Kept

These files are retained for:
- **Historical reference** - Understanding schema evolution from SQLite to PostgreSQL
- **Migration context** - Some scripts may still reference them during transition
- **Documentation** - Showing the migration path from SQLite to PostgreSQL

## ⚠️ Do Not Use

**DO NOT** use these files for:
- New database setups (use `db/authoritative_schema.sql`)
- Production deployments (use PostgreSQL schema)
- CI/CD workflows (use `db/authoritative_schema.sql`)
- New migrations (use `db/migrations/`)

## Known References

These files are still referenced in:
- `scripts/populate_npc_sample_data.py` - References `npc_sample_data.sql` (should be updated)
- `scripts/init_npc_database.py` - References schema files (should be updated to use authoritative schema)

## Action Items

1. ✅ **COMPLETED**: Migrate PostgreSQL migrations to `db/migrations/` (migrations 002-009 moved and marked as deprecated)
2. ⚠️ **PENDING**: Update `scripts/populate_npc_sample_data.py` to use PostgreSQL seed data
3. ⚠️ **PENDING**: Update `scripts/init_npc_database.py` to use `db/authoritative_schema.sql`
4. ⚠️ **PENDING**: Convert `npc_sample_data.sql` to PostgreSQL format if still needed

## Migration Status

### PostgreSQL Migrations (Moved to `db/migrations/`)

The following PostgreSQL migrations have been moved to `db/migrations/` and marked as deprecated:
- `002_add_hashed_password_column.sql` → `db/migrations/002_add_hashed_password_column.sql`
- `003_add_used_by_user_id_column.sql` → `db/migrations/003_add_used_by_user_id_column.sql`
- `004_rename_invites_columns.sql` → `db/migrations/004_rename_invites_columns.sql`
- `005_add_fastapi_users_columns.sql` → `db/migrations/005_add_fastapi_users_columns.sql`
- `006_migrate_stats_to_jsonb.sql` → `db/migrations/006_migrate_stats_to_jsonb.sql`
- `007_fix_professions_table_schema.sql` → `db/migrations/007_fix_professions_table_schema.sql`
- `008_increase_current_room_id_length.sql` → `db/migrations/008_increase_current_room_id_length.sql`
- `009_add_password_hash_column.sql` → `db/migrations/009_add_password_hash_column.sql`

All of these migrations are **deprecated** because their changes are already incorporated into `db/authoritative_schema.sql`.

### SQLite Migration (Legacy)

- `001_add_player_channel_preferences.sql` - SQLite-specific, kept in `server/sql/migrations/` for historical reference only
