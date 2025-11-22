# DDL Migration Scripts

This directory contains **DDL (Data Definition Language) migration scripts** for existing databases.

## Purpose

DDL migrations are used to modify the database schema for databases that already exist. These scripts are:
- **Backwards compatible**: Can be safely applied to existing databases
- **Idempotent**: Can be run multiple times without causing errors
- **Safe**: Use `IF NOT EXISTS`, `IF EXISTS`, and other safety checks

## When to Use DDL Migrations

Use DDL migrations when you need to:
- Add new tables, columns, indexes, or constraints to existing databases
- Modify existing table structures
- Add or modify database functions, types, or sequences
- Make schema changes that need to be applied to production databases

## When NOT to Use DDL Migrations

- **New database setups**: Use `db/authoritative_schema.sql` instead
- **Data changes**: Use DML migrations in `data/db/migrations/` instead
- **Seed data**: Use DML baseline scripts in `data/db/` instead

## Writing Idempotent Migration Scripts

All migration scripts must be idempotent. Use PostgreSQL's conditional statements:

### Adding Columns

```sql
-- Safe: Only adds column if it doesn't exist
ALTER TABLE players
ADD COLUMN IF NOT EXISTS new_field TEXT;
```

### Creating Indexes

```sql
-- Safe: Only creates index if it doesn't exist
CREATE INDEX IF NOT EXISTS idx_players_new_field
ON players(new_field);
```

### Adding Constraints

```sql
-- Safe: Check if constraint exists before adding
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'check_new_field'
    ) THEN
        ALTER TABLE players
        ADD CONSTRAINT check_new_field
        CHECK (new_field IS NOT NULL);
    END IF;
END $$;
```

### Creating Tables

```sql
-- Safe: Only creates table if it doesn't exist
CREATE TABLE IF NOT EXISTS new_table (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);
```

### Dropping Objects

```sql
-- Safe: Only drops if exists
DROP INDEX IF EXISTS idx_old_index;
DROP TABLE IF EXISTS old_table;
```

## Migration Naming Convention

Use descriptive names that indicate the change:

- `add_profession_id_to_players.sql`
- `create_combat_log_table.sql`
- `add_index_to_players_username.sql`
- `migrate_timestamp_columns.sql`

## Migration Execution Order

Migrations should be designed to be independent and order-independent when possible. If a migration depends on another, document the dependency clearly in comments.

## Testing Migrations

Before committing a migration:

1. Test on a copy of the development database
2. Verify the migration is idempotent (run it twice)
3. Verify the migration doesn't break existing functionality
4. Test rollback procedures if applicable

## Example Migration

```sql
-- Migration: Add flavor_text column to professions table
-- Date: 2024-01-15
-- Author: Development Team
--
-- This migration adds a flavor_text column to the professions table
-- for enhanced profession descriptions.

-- Add column if it doesn't exist
ALTER TABLE professions
ADD COLUMN IF NOT EXISTS flavor_text TEXT;

-- Add comment to document the column
COMMENT ON COLUMN professions.flavor_text IS
    'Flavor text describing the profession in-game';
```

## Directory Convention

- **Baseline DDL**: `/db/authoritative_schema.sql` - Complete schema for new databases
- **DDL Migrations**: `/db/migrations/*.sql` - Schema changes for existing databases (this directory)
- **DML Baseline**: `/data/db/*.sql` - Seed data for new databases
- **DML Migrations**: `/data/db/migrations/*.sql` - Data changes for existing databases
