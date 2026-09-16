# Database Schema Management

This directory contains the schema baseline, migrations, and supporting scripts for MythosMUD.

## The schema baseline

**`db/schema.sql`** is the single, schema-agnostic DDL source for all three environments
(`mythos_dev` / `mythos_unit` / `mythos_e2e`, #811). Before #811 this was three separate,
per-environment `pg_dump` files that had quietly drifted from each other despite being intended
to be identical — see the #811 investigation for what that drift looked like in practice.

Object names in `db/schema.sql` are **unqualified**. The loader must `SET search_path TO
<target_schema>;` (or connect with that search_path already set) before running it — the target
schema itself, and the `pgcrypto` extension, are created once by `db/databases/databases.sql` and
are not part of this file.

### Regenerating the baseline

When you make schema changes to `mythos_dev`, regenerate `db/schema.sql` from it:

```powershell
.\scripts\generate_schema_from_dev.ps1
```

The script connects to `mythos_dev`, runs `pg_dump`, and strips the schema qualification pg_dump
always emits so the checked-in file stays schema-agnostic.

### Verification

To verify that `db/schema.sql` matches the current database:

```bash
make verify-schema
```

This uses `scripts/verify_schema_match.ps1`, which reads `DATABASE_URL` from `.env.local` (or
`.env`) and compares `db/schema.sql` against the live database (schema-qualification stripped
from both sides before comparing).

### Directory structure

**`schema.sql`** - The single authoritative baseline DDL (committed to git).

**`migrations/`** - dbmate migrations directory (`scripts/migrate.ps1`), for schema/seed changes
made *after* the baseline. See `migrations/README.md`.

**`procedures/`** - Stored procedures/functions, applied separately via
`scripts/apply_procedures.ps1` (idempotent `CREATE OR REPLACE`, not part of the versioned
ledger — see `procedures/README.md`).

**`databases/`** - Database provisioning scripts (see `databases/README.md`).

**`roles/`** - PostgreSQL role creation scripts (see `roles/README.md`).

**Seed data** - The matching static-world seed lives in **`data/db/seed.sql`**. Load with
`search_path` set to the schema name (e.g. `mythos_unit`). See `data/db/README.md`.

See `LEGACY_FILES.md` for historical file status.

### Usage in CI/CD

- **GitHub Actions CI** - Applies `db/schema.sql` to the `mythos_unit` database (search_path set
  to `mythos_unit`), then `data/db/seed.sql`, then `db/procedures/*.sql`, then dbmate migrations.
- **Dockerfile.github-runner** - Same sequence, self-contained in the image.

For local or other environments, the same `db/schema.sql` and `data/db/seed.sql` apply — only the
target database name and `search_path` change.

### Notes

- `db/schema.sql` is committed to git (not generated on-demand in CI).
- Each environment has its own named schema (e.g. `mythos_unit`); applications use
  `POSTGRES_SEARCH_PATH` in `.env` to target it.
