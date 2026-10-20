# dbmate migrations (#811)

This directory is one of the **dbmate** migrations directories, run via
`scripts/migrate.ps1 -Environment <dev|unit|e2e>`. It replaces the hand-copied per-environment
migration triplets and per-feature apply scripts this project used previously.

## DDL here, DML in the data repo

dbmate is given two directories and merges them into **one ledger, ordered by version**:

| Directory | Holds | Why |
| --- | --- | --- |
| `db/migrations/` (this one) | **DDL only**: `CREATE` / `ALTER` / `DROP` / `COMMENT` / `GRANT` | The schema is code. |
| `data/db/migrations/` | **DML only**: `INSERT` / `UPDATE` / `DELETE` (rooms, items, NPCs, quests, dialogue) | World content lives in the data repo, beside the seed it extends. |

`scripts/lint_sql_guardrails.py` (part of `make lint`) fails a migration that sits in the wrong directory, or whose
version is used twice across the two. A change that needs both (a new column *and* a backfill) is two migrations: the
DDL one gets the earlier version, so it runs first on a fresh database. Keep DDL idempotent (`IF NOT EXISTS`,
`DROP ... IF EXISTS`) and DML replay-safe, since dbmate runs any migration the ledger has not seen.

## What lives here

Plain `.sql` files, `-- migrate:up` / `-- migrate:down` blocks, applied in filename order and
tracked in a `schema_migrations` table (per database). Object names are **unqualified** —
`scripts/migrate.ps1` sets `search_path` to the target schema before dbmate runs, the same
convention `db/schema.sql`, `data/db/seed.sql`, and `db/procedures/*.sql` all use.

`20260915000000_baseline.sql` is a required no-op: dbmate refuses to run against zero migration
files, so this file exists purely to give it a first ledger entry. Everything before it is
captured in `db/schema.sql` (DDL) and `data/db/seed.sql` (static world seed) — loaded once,
outside dbmate, when a database is first provisioned (see `db/databases/databases.sql` and
`scripts/load_world_seed.py`). Real migrations start after the baseline.

## What does NOT live here

- **Stored procedures/functions** (`db/procedures/*.sql`) — reapplied wholesale via
  `scripts/apply_procedures.ps1` on every build/test run. They're idempotent
  `CREATE OR REPLACE` bodies, not incremental history, so a versioned ledger buys nothing.
- **The base schema/seed** — see `db/schema.sql` / `data/db/seed.sql` above.

## Adding a migration

```powershell
npx dbmate new <description> --migrations-dir db/migrations
```

For a content change use the data directory instead (`npx dbmate new <description> --migrations-dir
data/db/migrations`); it is committed in the data repo, and the parent repo bumps its pointer. Then edit the
generated file and run `scripts/migrate.ps1 -Environment <env>` to apply it. Only
`up` and `status` are reachable through that wrapper — `drop`/`down` are never exposed, and
`mythos_dev` (PROTECTED, see `.claude/rules/database.md`) can only ever be targeted by those two.

`mythos_dev` also migrates automatically on the next `scripts/start_local.ps1` run (local
environment only) — running `migrate.ps1` by hand is only needed to apply a new migration
immediately, without restarting the server.
