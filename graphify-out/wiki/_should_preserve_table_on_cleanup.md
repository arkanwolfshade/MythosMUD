# _should_preserve_table_on_cleanup

> 13 nodes

## Key Concepts

- **_should_preserve_table_on_cleanup()** (8 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_integration_cleanup_helpers.py** (6 connections) — `server/tests/unit/fixtures/test_integration_cleanup_helpers.py`
- **test_does_not_preserve_mutable_player_tables()** (4 connections) — `server/tests/unit/fixtures/test_integration_cleanup_helpers.py`
- **test_preserves_every_reference_seed_table()** (4 connections) — `server/tests/unit/fixtures/test_integration_cleanup_helpers.py`
- **test_no_longer_special_cases_the_unused_alembic_table_name()** (3 connections) — `server/tests/unit/fixtures/test_integration_cleanup_helpers.py`
- **test_preserves_the_dbmate_migration_ledger()** (3 connections) — `server/tests/unit/fixtures/test_integration_cleanup_helpers.py`
- **parametrize** (2 connections)
- **Return True for the migration ledger and reference/world seed tables.…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Regression tests for `_should_preserve_table_on_cleanup` (#811). The migration…** (1 connections) — `server/tests/unit/fixtures/test_integration_cleanup_helpers.py`
- **schema_migrations (dbmate, #811) must survive db_cleanup.** (1 connections) — `server/tests/unit/fixtures/test_integration_cleanup_helpers.py`
- **Alembic was scaffolded but never wired up (no alembic.ini/env.py, not a…** (1 connections) — `server/tests/unit/fixtures/test_integration_cleanup_helpers.py`
- **World topology and professions must survive cleanup so procedure/E2E tests keep…** (1 connections) — `server/tests/unit/fixtures/test_integration_cleanup_helpers.py`
- **Player-generated rows are exactly what db_cleanup exists to truncate.** (1 connections) — `server/tests/unit/fixtures/test_integration_cleanup_helpers.py`

## Relationships

- [session_factory](session_factory.md) (2 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/unit/fixtures/test_integration_cleanup_helpers.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*