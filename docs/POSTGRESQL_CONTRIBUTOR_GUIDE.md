# PostgreSQL Standards for Contributors

This guide summarizes the key PostgreSQL rules for MythosMUD. For the full style guide and
rationale, see [.cursor/rules/postgresql.mdc](../.cursor/rules/postgresql.mdc).

## Naming

- Use **snake_case** for all identifiers (tables, columns, functions).
- Use **lowercase** SQL keywords (`select`, `from`, `where`, `join`, etc.).
- Use explicit `as` for aliases.

## Data Types

- Prefer **`text`** over `varchar(n)` unless a strict length is required.
- Use **`uuid`** for primary and foreign keys that reference UUIDs (e.g. `player_id`, `user_id`).
- Use **`timestamptz`** with `default now()` for timestamp columns.
- Use **`bigint generated always as identity`** for surrogate keys (not `serial`/`bigserial`).

## Queries

- **Avoid `select *`** in production and maintenance code. Use explicit column lists so schema
  changes do not cause subtle bugs.
- Use **explicit joins** (`inner join`, `left join`) instead of comma-separated `from a, b where`.
- Prefer **`not exists`** or **`left join ... where ... is null`** over `not in` with subqueries
  (because of NULL semantics).

## Security

- Use **parameterized queries** only. Never interpolate user input into SQL strings.
- Pass values as bound parameters (e.g. `%s` with psycopg2, `:name` with SQLAlchemy `text()`).

## Verification

- Run **`make sqlfluff`** (and optionally **`make lint-sql-guardrails`**) before committing SQL
  changes.
- Hand-maintained SQL lives in `db/schema/`, `db/verification/`, `db/migrations/`, and
  `server/scripts/`. The authoritative schema is generated: `db/authoritative_schema.sql`.

## References

- Full rules: [.cursor/rules/postgresql.mdc](../.cursor/rules/postgresql.mdc)
- Audit report: [docs/POSTGRESQL_AUDIT_REPORT_2026.md](POSTGRESQL_AUDIT_REPORT_2026.md)
