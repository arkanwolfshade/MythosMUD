# Database Schema Management

This directory contains the authoritative database schema definition for MythosMUD.

## Authoritative Schema

The `authoritative_schema.sql` file is the single source of truth for the database schema. It is generated directly from the `mythos_dev` PostgreSQL database using `pg_dump`.

### Regenerating the Schema

When you make schema changes to the `mythos_dev` database, regenerate the authoritative schema file:

**Linux/Mac:**
```bash
./scripts/generate_schema_from_dev.sh
```

**Windows:**
```powershell
.\scripts\generate_schema_from_dev.ps1
```

The script will:
1. Connect to the `mythos_dev` database
2. Extract the complete DDL (Data Definition Language) using `pg_dump`
3. Write the schema to `db/authoritative_schema.sql`
4. Add header comments explaining the generation process

### Verification

To verify that the schema file matches the current database:

```bash
make verify-schema
```

This will compare `db/authoritative_schema.sql` with the current `mythos_dev` database structure and report any drift.

### Schema Update Process

1. Make schema changes directly in the `mythos_dev` database (using `psql`, migrations, or your preferred tool)
2. Regenerate the schema file using the generation script
3. Review the generated file to ensure it captures your changes correctly
4. Commit the updated `authoritative_schema.sql` to git

### Directory Structure

- **`authoritative_schema.sql`** - Baseline DDL schema (committed to git)
- **`migrations/`** - DDL migration scripts for existing databases (see `migrations/README.md`)
- **`databases/`** - Database provisioning scripts (see `databases/README.md`)
- **`roles/`** - PostgreSQL role creation scripts (see `roles/README.md`)
- **`schema/`** - ⚠️ Legacy schema files kept for historical reference only (see `schema/README.md`)
  - `01_world_and_calendar.sql`
  - `02_items_and_npcs.sql`
  - `03_identity_and_moderation.sql`
  - `04_runtime_tables.sql`

See `LEGACY_FILES.md` for complete status of all database-related files.

### Usage in CI/CD

The authoritative schema is used by:
- **Dockerfile.github-runner** - Applies schema to test databases during image build
- **GitHub Actions CI** - Applies schema to test databases during workflow execution

Both use a single command:
```bash
psql -d mythos_unit -f db/authoritative_schema.sql
```

This replaces the previous approach of applying 4 separate schema files sequentially.

### Notes

- The schema file is **committed to git** (not generated on-demand)
- The schema file includes `SET` statements for clean execution
- Owner and privilege commands are excluded for portability
- The schema includes `--clean` and `--if-exists` flags for idempotent execution
