# PostgreSQL Standards for Contributors

**Version 1.0.0** · MythosMUD · 2026-07-30

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
This guide summarizes the key PostgreSQL rules for MythosMUD. For the full style guide and
rationale, see [.cursor/rules/postgresql.mdc](../.cursor/rules/postgresql.mdc).

## 2. Naming

**[SPEC]**

- Use **snake_case** for all identifiers (tables, columns, functions).
- Use **lowercase** SQL keywords (`select`, `from`, `where`, `join`, etc.).
- Use explicit `as` for aliases.

## 3. Data Types

**[SPEC]**

- Prefer **`text`** over `varchar(n)` unless a strict length is required.
- Use **`uuid`** for primary and foreign keys that reference UUIDs (e.g. `player_id`, `user_id`).
- Use **`timestamptz`** with `default now()` for timestamp columns.
- Use **`bigint generated always as identity`** for surrogate keys (not `serial`/`bigserial`).

## 4. Queries

**[SPEC]**

- **Avoid `select *`** in production and maintenance code. Use explicit column lists so schema
  changes do not cause subtle bugs.
- Use **explicit joins** (`inner join`, `left join`) instead of comma-separated `from a, b where`.
- Prefer **`not exists`** or **`left join ... where ... is null`** over `not in` with subqueries
  (because of NULL semantics).

## 5. Security

**[SPEC]**

- Use **parameterized queries** only. Never interpolate user input into SQL strings.
- Pass values as bound parameters (e.g. `%s` with psycopg2, `:name` with SQLAlchemy `text()`).

## 6. Verification

**[NOTE]**

- Run **`make sqlfluff`** (and optionally **`make lint-sql-guardrails`**) before committing SQL
  changes.
- Hand-maintained SQL lives in `db/schema/`, `db/verification/`, `db/migrations/`, and
  `server/scripts/`. Environment DDL is in `db/mythos_dev_ddl.sql`, `db/mythos_unit_ddl.sql`,
  and `db/mythos_e2e_ddl.sql` (generated from the corresponding database).

## 7. References

**[SPEC]**

- Full rules: [.cursor/rules/postgresql.mdc](../.cursor/rules/postgresql.mdc)
- Audit report: [docs/POSTGRESQL_AUDIT_REPORT_2026.md](POSTGRESQL_AUDIT_REPORT_2026.md)

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
