# Legacy Files Status

This document summarizes the status of legacy database files and directories.

## Active Infrastructure Files

These files are **actively used** and should **not** be removed:

### ✅ `db/roles/roles.sql`

**Status**: Active

**Purpose**: Creates PostgreSQL roles (users) for different environments

**Used by**: Dockerfile, CI workflows

**Location**: `db/roles/`

- **See**: `db/roles/README.md`

### ✅ `db/databases/databases.sql`

**Status**: Active

**Purpose**: Creates PostgreSQL databases (mythos_dev, mythos_unit, mythos_e2e)

**Used by**: Dockerfile, CI workflows

**Location**: `db/databases/`

- **See**: `db/databases/README.md`

## Removed DDL/DML (Authoritative Files Only)

All non-authoritative DDL and DML migration files have been **removed**. Only these are used:

- **DDL**: `db/mythos_dev_ddl.sql`, `db/mythos_unit_ddl.sql`, `db/mythos_e2e_ddl.sql`
- **DML**: `data/db/mythos_dev_dml.sql`, `data/db/mythos_unit_dml.sql`, `data/db/mythos_e2e_dml.sql`

### ❌ `db/schema/*.sql` (removed)

**Status**: Removed

**Reason**: Replaced by environment DDL (`db/mythos_*_ddl.sql`). The four legacy schema files
were deleted.

### ❌ `db/migrations/*.sql` (removed)

**Status**: Removed

**Reason**: DDL migrations removed in favor of applying a single authoritative DDL file per
environment. New databases use `db/mythos_<env>_ddl.sql` only.

### ❌ `data/db/00_world_and_emotes.sql`, `01_professions.sql`, etc. (removed)

**Status**: Removed

**Reason**: Replaced by authoritative per-environment DML: `data/db/mythos_<env>_dml.sql`.

### ❌ `data/db/migrations/*.sql` (removed)

**Status**: Removed

**Reason**: DML migrations removed; seed data is in the authoritative `data/db/mythos_*_dml.sql`
files only.

### ⚠️ `data/static/generated_sql/static_seed.sql`

**Status**: Deprecated - Replaced by authoritative DML in `data/db/`

**Replacement**: Content is incorporated into `data/db/mythos_dev_dml.sql` (and other env DML).

**Location**: `data/static/generated_sql/`

- **Action**: Do not use - use `data/db/mythos_<env>_dml.sql` for seed data

## Active Scripts

These scripts are **actively used** for data generation:

### ✅ `scripts/static_data/generate_sql.mjs`

**Status**: Active

**Purpose**: Generates world/calendar/emotes SQL from JSON source data (for inclusion in
authoritative DML or dev workflows).

**Output**: World data, calendars, and emotes (incorporate into `data/db/mythos_*_dml.sql` as needed)

**Location**: `scripts/static_data/`

- **See**: `scripts/static_data/README.md`

## Removed Directories

These directories have been **removed** after migration:

### ❌ `db/migration/` (removed)

**Status**: Removed (consolidated into `db/migrations/`, then migrations removed in favor of
authoritative DDL).

### ❌ `scripts/migrations/` (removed)

**Status**: Removed

**Reason**: Migration files were moved to `db/migrations/`; DDL migrations have since been
removed in favor of `db/mythos_*_ddl.sql`.

### ⚠️ `server/sql/` (legacy - kept for reference)

**Status**: Deprecated - Legacy SQLite files kept for historical reference

**Files**:

- `items_schema.sql` - SQLite schema (replaced by environment DDL in `db/mythos_*_ddl.sql`)
- `npc_schema.sql` - SQLite schema (replaced by environment DDL in `db/mythos_*_ddl.sql`)
- `items_seed_data.sql` - SQLite seed data (replaced by authoritative `data/db/mythos_*_dml.sql`)
- `npc_sample_data.sql` - SQLite seed data (still referenced, should be migrated)
- `migrations/001_add_player_channel_preferences.sql` - SQLite migration (legacy)
- `migrations/002-009_*.sql` - PostgreSQL migrations (removed; use `db/mythos_*_ddl.sql`)
- **Location**: `server/sql/`
- **See**: `server/sql/README.md`
- **Action**: Do not use - all functionality replaced by PostgreSQL schema and migrations

### ❌ `data/seed/` (removed)

**Status**: Removed

**Reason**: All files moved to `data/db/`

**Migration**: All `.sql` files and README moved to `data/db/`

### ❌ `data/migration/` (removed)

**Status**: Removed

**Reason**: CSV files were in `data/db/migrations/`; DML migrations have been removed in favor
of authoritative `data/db/mythos_*_dml.sql`.

## Current Directory Structure

```
db/
├── mythos_dev_ddl.sql         ✅ Authoritative - Dev DDL
├── mythos_unit_ddl.sql        ✅ Authoritative - Unit test DDL
├── mythos_e2e_ddl.sql         ✅ Authoritative - E2E test DDL
├── databases/                  ✅ Active - Database provisioning
│   ├── databases.sql
│   └── README.md
├── migrations/                 ❌ DDL migration .sql files removed (README only)
│   └── README.md
├── roles/                      ✅ Active - Role creation
│   ├── roles.sql
│   └── README.md
└── schema/                     ❌ Schema .sql files removed (README only)
    └── README.md

data/
├── db/                         ✅ Authoritative DML only
│   ├── mythos_dev_dml.sql
│   ├── mythos_unit_dml.sql
│   └── mythos_e2e_dml.sql
└── static/
    └── generated_sql/          ⚠️ Legacy - Historical reference only
        ├── static_seed.sql
        └── README.md
```

## Migration Checklist

When updating code that references legacy files:

- [x] Replace `db/schema/*.sql` with environment DDL (`db/mythos_*_ddl.sql`) — done
- [x] Use only authoritative DML (`data/db/mythos_*_dml.sql`) — done
- [x] Remove DDL/DML migration files in favor of authoritative DDL/DML — done
- [ ] Update any remaining hardcoded paths in scripts
- [ ] Update comments and documentation

## Questions?

If you're unsure whether a file is still needed:

1. Check if it's referenced in Dockerfile or CI workflows
2. Check if it's imported/used by any Python/Node scripts
3. Check the file's README.md (if it exists)
4. When in doubt, ask before removing
