# Database Schema Management

This directory contains environment-specific DDL and supporting scripts for MythosMUD.

## Environment DDL Files

Schema is maintained per environment using these DDL files (generated from the corresponding
PostgreSQL database via `pg_dump`):

- **`mythos_dev_ddl.sql`** - Development database schema (source of truth for structure)
- **`mythos_unit_ddl.sql`** - Unit test database schema
- **`mythos_e2e_ddl.sql`** - E2E test database schema

Each file creates a PostgreSQL schema with the same name as the database (e.g. `mythos_dev`)
and defines all tables in that schema (not `public`).

### Regenerating DDL

When you make schema changes to a database, regenerate the corresponding DDL file.

**Windows (from project root):**

```powershell
.\scripts\generate_schema_from_dev.ps1
```

The script connects to the configured database (e.g. `mythos_dev`), runs `pg_dump`, and writes
the DDL to the appropriate `db/mythos_<env>_ddl.sql` file.

### Verification

To verify that a DDL file matches the current database:

```bash
make verify-schema
```

This uses `scripts/verify_schema_match.ps1`, which reads `DATABASE_URL` from `.env.local` (or
`.env`) and compares `db/mythos_<dbname>_ddl.sql` with the live database.

### Directory Structure

**`mythos_dev_ddl.sql`**, **`mythos_unit_ddl.sql`**, **`mythos_e2e_ddl.sql`** - Authoritative
environment DDL (committed to git).

**`databases/`** - Database provisioning scripts (see `databases/README.md`).

**`roles/`** - PostgreSQL role creation scripts (see `roles/README.md`).

**Seed data (DML)** - Authoritative per-environment DML lives in **`data/db/`**:
`mythos_dev_dml.sql`, `mythos_unit_dml.sql`, `mythos_e2e_dml.sql`. Load with
`search_path` set to the schema name (e.g. `mythos_unit`).

See `LEGACY_FILES.md` for historical file status.

### Usage in CI/CD

Environment DDL is used as follows:

- **GitHub Actions CI** - Applies `db/mythos_unit_ddl.sql` to the `mythos_unit` database, then
  loads `data/db/mythos_unit_dml.sql` with `search_path` set to `mythos_unit`.
- **Dockerfile.github-runner** - Applies `db/mythos_unit_ddl.sql` then
  `data/db/mythos_unit_dml.sql` with `search_path` set to `mythos_unit`.

For local or other environments, use the DDL that matches your database name (e.g. `mythos_dev`
-> `db/mythos_dev_ddl.sql`).

### Notes

- DDL files are committed to git (not generated on-demand in CI).
- Each DDL creates a named schema (e.g. `mythos_unit`) and sets `search_path`; applications
  use `POSTGRES_SEARCH_PATH` in `.env` to target that schema.
