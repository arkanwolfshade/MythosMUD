# Legacy Schema Files

⚠️ **DEPRECATED** - These files are kept for historical reference only.

## Status

These schema files have been **replaced** by the authoritative schema approach:

- **Old approach**: 4 separate schema files applied sequentially
  - `01_world_and_calendar.sql`
  - `02_items_and_npcs.sql`
  - `03_identity_and_moderation.sql`
  - `04_runtime_tables.sql`

- **New approach**: Single authoritative schema file
  - `../authoritative_schema.sql` - Generated from `mythos_dev` database

## Current Usage

The authoritative schema (`../authoritative_schema.sql`) is used by:
- **Dockerfile.github-runner** - Database initialization in CI
- **GitHub Actions CI** - Test database setup
- **All new database setups**

## Why These Files Are Kept

These files are retained for:
- **Historical reference** - Understanding schema evolution
- **Migration context** - Some migration scripts may reference them
- **Documentation** - Showing how the schema was previously organized

## ⚠️ Do Not Use

**DO NOT** use these files for:
- New database setups (use `../authoritative_schema.sql`)
- CI/CD workflows (use `../authoritative_schema.sql`)
- Production deployments (use `../authoritative_schema.sql`)

## Migration Notes

If you find code referencing these files:
1. Update to use `db/authoritative_schema.sql` instead
2. Or use the appropriate migration script from `../migrations/` for existing databases
