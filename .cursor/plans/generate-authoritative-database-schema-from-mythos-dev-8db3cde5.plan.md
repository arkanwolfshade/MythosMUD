<!-- 8db3cde5-f05e-4107-b16d-ec6d942ab0a9 401231c6-12bd-4986-b852-ab51ac3cf420 -->
# Generate Authoritative Database Schema from mythos_dev

## Objective

Replace the current multi-file schema approach (4 separate SQL files) with a single authoritative schema script extracted directly from the `mythos_dev` database, ensuring Docker container databases match the development database structure. Establish directory conventions: DDL in `/db/` with migrations in `/db/migrations/`, DML in `/data/db/` with migrations in `/data/db/migrations/`.

## Current State

Dockerfile applies 4 schema files sequentially: `01_world_and_calendar.sql`, `02_items_and_npcs.sql`, `03_identity_and_moderation.sql`, `04_runtime_tables.sql`

- CI workflow applies the same 4 files
- Schema files are manually maintained and can drift from actual database structure
- Migration scripts exist but may not reflect current state

## Directory Structure Convention

**DDL (Data Definition Language)**:

- `db/authoritative_schema.sql` - Baseline authoritative schema (committed to git)
- `db/migrations/*.sql` - DDL migration scripts for new database setups
- **DML (Data Manipulation Language)**:
  - `data/db/*.sql` - DML baseline scripts (seed data, initial data loads)
  - `data/db/migrations/*.sql` - DML migration scripts (INSERT, UPDATE, DELETE operations for existing databases)

## Resolved Decisions

1. **`authoritative_schema.sql`**: Committed to git (not generated on-demand)
2. **Schema verification**: No pre-commit hook, but add `make verify-schema` target to check if schema is up-to-date
3. **Schema changes for existing databases**: Backwards compatible, idempotent SQL migration scripts in `/db/migrations/` (DDL) and `/data/db/migrations/` (DML)

## Implementation Plan

### Phase 1: Extract DDL from mythos_dev

1. Create script `scripts/generate_schema_from_dev.sh` (and `.ps1` for Windows)

   - Use `pg_dump` with `--schema-only` flag to extract DDL
   - Connect to `mythos_dev` database
   - Output to `db/authoritative_schema.sql`
   - Include: tables, indexes, constraints, sequences, types, functions
   - Exclude: data (use `--no-data` or `--schema-only`)
   - Format: Clean, ordered output suitable for version control

### Phase 2: Create Authoritative Schema File

1. Generate `db/authoritative_schema.sql` from `mythos_dev`

   - Use `pg_dump --schema-only --no-owner --no-privileges` for clean output
   - Order: types/enums first, then tables in dependency order, then indexes/constraints
   - Add header comment explaining source and generation process
   - Include `SET client_min_messages = WARNING;` and `SET search_path = public;` at top
   - **Location**: `/db/` directory (baseline DDL)
   - **Git**: Commit to repository (not git-ignored)

### Phase 3: Update Dockerfile

1. Modify `Dockerfile.github-runner` (lines 106-113)

   - Replace 4 separate `psql -f` commands with single command:

`su postgres -c "psql -d mythos_unit -f /workspace/db/authoritative_schema.sql"`

- Apply same change for `mythos_e2e` database
- Update verification commands to check for expected tables

### Phase 4: Update CI Workflow

1. Modify `.github/workflows/ci.yml` (lines 72-75)

   - Replace 4 separate schema file applications with single authoritative script
   - Update to: `sudo -u postgres psql -d mythos_unit -f db/authoritative_schema.sql`

### Phase 5: Documentation

1. Create `db/README.md`

   - Document the authoritative schema approach
   - Instructions for regenerating from `mythos_dev`
   - Process for updating schema: make changes in `mythos_dev`, regenerate script, commit
   - **Directory convention**:
     - Baseline DDL: `/db/authoritative_schema.sql`
     - DDL migrations: `/db/migrations/*.sql`
   - Note that old schema files in `db/schema/` are kept for historical reference only

2. Create `db/migrations/README.md`

   - Document DDL migration process for existing databases
   - **Directory convention**: All backwards-compatible, idempotent DDL migration scripts belong in `/db/migrations/`
   - Guidelines for writing idempotent migration scripts
   - Examples of safe schema changes (ALTER TABLE with IF NOT EXISTS, etc.)

3. Create `data/db/README.md`

   - Document DML baseline scripts
   - **Directory convention**: DML baseline scripts (seed data, initial data loads) belong in `/data/db/`
   - Examples of baseline DML scripts

4. Create `data/db/migrations/README.md`

   - Document DML migration process
   - **Directory convention**: All DML migration scripts (INSERT, UPDATE, DELETE) belong in `/data/db/migrations/`
   - Examples of when to use DML migrations vs DDL migrations

### Phase 6: Verification

1. Add verification script `scripts/verify_schema_match.sh`

   - Compare `db/authoritative_schema.sql` structure with `mythos_dev` database
   - Check for drift between source and generated file
   - Can be run in CI to ensure schema stays in sync

2. Add `make verify-schema` target to Makefile

   - Run verification script to check if `authoritative_schema.sql` matches `mythos_dev`
   - Provide clear output indicating if schema is up-to-date or needs regeneration
   - Exit with non-zero code if schema drift detected

## Files to Create/Modify

**New Files:**

- `scripts/generate_schema_from_dev.sh` - Linux/Mac script to extract DDL
- `scripts/generate_schema_from_dev.ps1` - Windows PowerShell version
- `db/authoritative_schema.sql` - Generated authoritative schema (committed to git)
- `db/README.md` - Documentation for DDL baseline
- `db/migrations/README.md` - Documentation for DDL migrations
- `data/db/README.md` - Documentation for DML baseline
- `data/db/migrations/README.md` - Documentation for DML migrations
- `scripts/verify_schema_match.sh` - Verification script

**Modified Files:**

- `Dockerfile.github-runner` - Replace multi-file schema application with single file
- `.github/workflows/ci.yml` - Update CI to use authoritative schema
- `Makefile` - Add `verify-schema` target to check schema is up-to-date

**Files to Keep (for reference):**

- `db/schema/01_world_and_calendar.sql` - Keep for historical reference
- `db/schema/02_items_and_npcs.sql` - Keep for historical reference
- `db/schema/03_identity_and_moderation.sql` - Keep for historical reference
- `db/schema/04_runtime_tables.sql` - Keep for historical reference
- `server/sql/migrations/*.sql` - Keep for historical reference

## Technical Details

### pg_dump Command

```bash
pg_dump -h localhost -U postgres -d mythos_dev \
  --schema-only \
  --no-owner \
  --no-privileges \
  --file=db/authoritative_schema.sql
```

### Schema Ordering

Custom types/enums first

- Tables in dependency order (users before players, etc.)
- Indexes after tables
- Foreign key constraints after all tables exist
- Sequences last

### Dockerfile Changes

Replace:

```dockerfile
su postgres -c "psql -d mythos_unit -f /workspace/db/schema/01_world_and_calendar.sql" && \
su postgres -c "psql -d mythos_unit -f /workspace/db/schema/02_items_and_npcs.sql" && \
su postgres -c "psql -d mythos_unit -f /workspace/db/schema/03_identity_and_moderation.sql" && \
su postgres -c "psql -d mythos_unit -f /workspace/db/schema/04_runtime_tables.sql"
```

With:

```dockerfile
su postgres -c "psql -d mythos_unit -f /workspace/db/authoritative_schema.sql"
```

### Makefile Target

Add to Makefile:

```makefile
verify-schema:
 @echo "Verifying authoritative_schema.sql matches mythos_dev..."
 @./scripts/verify_schema_match.sh
```

## Success Criteria

Single authoritative schema file generated from `mythos_dev` in `/db/` directory

- Schema file committed to git repository
- Docker container creates databases matching `mythos_dev` structure
- CI workflow uses authoritative schema
- `make verify-schema` target available to check schema is up-to-date
- Documentation explains regeneration process and directory conventions
- Verification script can detect schema drift
- Directory structure established:
  - DDL baseline: `/db/authoritative_schema.sql`
  - DDL migrations: `/db/migrations/*.sql`
  - DML baseline: `/data/db/*.sql`
  - DML migrations: `/data/db/migrations/*.sql`
