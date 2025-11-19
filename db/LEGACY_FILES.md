# Legacy Files Status

This document summarizes the status of legacy database files and directories.

## Active Infrastructure Files

These files are **actively used** and should **not** be removed:

### ✅ `db/roles/roles.sql`
- **Status**: Active
- **Purpose**: Creates PostgreSQL roles (users) for different environments
- **Used by**: Dockerfile, CI workflows
- **Location**: `db/roles/`
- **See**: `db/roles/README.md`

### ✅ `db/databases/databases.sql`
- **Status**: Active
- **Purpose**: Creates PostgreSQL databases (mythos_dev, mythos_unit, mythos_e2e)
- **Used by**: Dockerfile, CI workflows
- **Location**: `db/databases/`
- **See**: `db/databases/README.md`

## Deprecated/Legacy Files

These files are **kept for historical reference** but should **not** be used for new work:

### ⚠️ `db/schema/*.sql` (4 files)
- **Status**: Deprecated - Replaced by `db/authoritative_schema.sql`
- **Files**:
  - `01_world_and_calendar.sql`
  - `02_items_and_npcs.sql`
  - `03_identity_and_moderation.sql`
  - `04_runtime_tables.sql`
- **Replacement**: `db/authoritative_schema.sql`
- **Location**: `db/schema/`
- **See**: `db/schema/README.md`
- **Action**: Do not use - kept for historical reference only

### ⚠️ `data/static/generated_sql/static_seed.sql`
- **Status**: Deprecated - Replaced by `data/db/00_world_and_emotes.sql`
- **Replacement**: `data/db/00_world_and_emotes.sql`
- **Location**: `data/static/generated_sql/`
- **See**: `data/static/generated_sql/README.md`
- **Action**: Do not use - kept for historical reference only

## Removed Directories

These directories have been **removed** after migration:

### ❌ `db/migration/` (removed)
- **Status**: Removed
- **Reason**: All files moved to `db/migrations/` (note: plural)
- **Migration**:
  - SQL files → `db/migrations/`
  - Utility scripts → `scripts/`
  - Documentation → `db/migrations/`

### ❌ `data/seed/` (removed)
- **Status**: Removed
- **Reason**: All files moved to `data/db/`
- **Migration**: All `.sql` files and README moved to `data/db/`

### ❌ `data/migration/` (removed)
- **Status**: Removed
- **Reason**: CSV files moved to `data/db/migrations/`
- **Migration**: CSV files moved to `data/db/migrations/`

## Current Directory Structure

```
db/
├── authoritative_schema.sql    ✅ Active - Single source of truth
├── databases/                  ✅ Active - Database provisioning
│   ├── databases.sql
│   └── README.md
├── migrations/                 ✅ Active - DDL migrations
│   ├── *.sql (22 files)
│   └── README.md
├── roles/                      ✅ Active - Role creation
│   ├── roles.sql
│   └── README.md
└── schema/                     ⚠️ Legacy - Historical reference only
    ├── 01_world_and_calendar.sql
    ├── 02_items_and_npcs.sql
    ├── 03_identity_and_moderation.sql
    ├── 04_runtime_tables.sql
    └── README.md

data/
├── db/                         ✅ Active - DML baseline
│   ├── 00_world_and_emotes.sql
│   ├── 01_professions.sql
│   ├── 02_item_prototypes.sql
│   ├── 03_npc_definitions.sql
│   ├── migrations/             ✅ Active - DML migrations
│   │   ├── *.csv (historical)
│   │   └── README.md
│   └── README.md
└── static/
    └── generated_sql/          ⚠️ Legacy - Historical reference only
        ├── static_seed.sql
        └── README.md
```

## Migration Checklist

When updating code that references legacy files:

- [ ] Replace `db/schema/*.sql` → `db/authoritative_schema.sql`
- [ ] Replace `data/seed/*.sql` → `data/db/*.sql`
- [ ] Replace `data/static/generated_sql/static_seed.sql` → `data/db/00_world_and_emotes.sql`
- [ ] Replace `db/migration/*.sql` → `db/migrations/*.sql` (note: plural)
- [ ] Update any hardcoded paths in scripts
- [ ] Update comments and documentation

## Questions?

If you're unsure whether a file is still needed:
1. Check if it's referenced in Dockerfile or CI workflows
2. Check if it's imported/used by any Python/Node scripts
3. Check the file's README.md (if it exists)
4. When in doubt, ask before removing
