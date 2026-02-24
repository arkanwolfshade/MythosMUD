# DDL Migrations (Removed)

DDL migration scripts that previously lived in this directory have been **removed**.

Schema is now maintained only via **authoritative DDL** files:

- `db/mythos_dev_ddl.sql`
- `db/mythos_unit_ddl.sql`
- `db/mythos_e2e_ddl.sql`

For new databases, apply the DDL that matches your environment. Regenerate DDL from a live
database using `scripts/generate_schema_from_dev.ps1` when the schema changes.

See `db/README.md` and `db/LEGACY_FILES.md` for the current layout.
