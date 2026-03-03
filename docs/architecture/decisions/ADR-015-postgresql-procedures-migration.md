# ADR-015: PostgreSQL Procedures and Functions for Data Access

**Status:** Accepted
**Date:** 2026-02-26

## Context

MythosMUD uses PostgreSQL as the primary datastore (ADR-006) with repository-style data access (ADR-005). The codebase had evolved with a mix of SQLAlchemy ORM (select, merge, delete), raw SQL via `text()`, and sync psycopg2 in a few places. This led to:

- Inline SQL scattered across repositories and API layers
- N+1 patterns and duplicated query logic
- Difficulty changing schema or query shape without touching many Python files
- No single place to enforce query contracts or optimize at the database

A migration to centralize all DML/DQL in PostgreSQL stored procedures and functions was undertaken so that Python manages transactions and maps procedure results to domain objects, while the database owns query shape and logic.

## Decision

Migrate all Python–PostgreSQL data access to **stored procedures and functions**:

- **Procedure storage**: One `.sql` file per domain under `db/procedures/` (e.g. `players.sql`, `rooms.sql`, `quests.sql`). Each file uses `CREATE OR REPLACE FUNCTION` (and PROCEDURE where needed) with schema applied via `psql -v schema_name=<schema>`.
- **Apply script**: `scripts/apply_procedures.ps1` applies all procedure files to target databases (mythos_dev, mythos_unit, mythos_e2e). `make build` runs `apply-procedures` before the client build; test targets run it for mythos_unit and mythos_e2e before pytest.
- **Python usage**: Repositories and services call procedures via `session.execute(text("SELECT * FROM get_entity_by_id(:id)"), params)`. Results are consumed with `result.mappings().all()` or `.scalar()` and mapped to domain objects in Python. Transactions (commit/rollback) remain in Python.
- **Schema resolution**: Connections use `search_path` set from the database name (mythos_dev, mythos_unit, mythos_e2e) so procedure names are unqualified in SQL; `database.py` normalizes `search_path` for these databases.
- **Naming**: `verb_entity` (e.g. `get_player_by_id`, `upsert_player`, `get_rooms_with_exits`). Functions return rows (SETOF or single row); procedures used where multi-statement mutations with OUT parameters are needed.

## Alternatives Considered

1. **Keep ORM + raw SQL** – Rejected: did not address scattered SQL or give a single contract at the DB boundary.
2. **Schema-qualified names in Python** – Rejected in favour of search_path: unqualified names keep Python agnostic of schema; one connection per environment.
3. **Alembic for procedure versioning** – Deferred: procedures are applied as part of build/test; versioned migrations for procedure changes can be added later if needed.

## Consequences

- **Positive**: Single place for query logic; procedure return shape is a clear contract; fewer round-trips where procedures aggregate data (e.g. get_rooms_with_exits); test and dev DBs get procedures via the same script; integration tests can assert procedure return shape.
- **Negative**: Procedure definitions must be kept in sync with table schema; DB type mismatches (e.g. json vs jsonb) surface at call sites until fixed in the procedure.
- **Neutral**: SQLAlchemy ORM mappings remain for now where used by Alembic or other tooling; `postgres_adapter.py` can be deprecated or removed once unused.

## Related ADRs

- ADR-005: Repository Pattern for Data Access
- ADR-006: PostgreSQL as Primary Datastore

## References

- `db/procedures/README.md` – Apply order and usage
- `scripts/apply_procedures.ps1` – Application script
- `server/tests/integration/test_procedures_return_shape.py` – Return-shape tests
