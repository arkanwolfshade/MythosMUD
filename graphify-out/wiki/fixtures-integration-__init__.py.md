# fixtures/integration/__init__.py

> 25 nodes

## Key Concepts

- **fixtures/integration/__init__.py** (19 connections) — `server/tests/fixtures/integration/__init__.py`
- **db_cleanup()** (11 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_engine()** (7 connections) — `server/tests/fixtures/integration/__init__.py`
- **_assert_allowed_integration_test_db()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **_delete_mutable_integration_test_rows()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **db.py** (6 connections) — `server/tests/fixtures/integration/db.py`
- **integration_db_url()** (5 connections) — `server/tests/fixtures/integration/__init__.py`
- **_get_db_name_from_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **_is_allowed_integration_test_db()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **fixture** (4 connections)
- **_should_preserve_table_on_cleanup()** (3 connections) — `server/tests/fixtures/integration/__init__.py`
- **FixtureRequest** (3 connections)
- **AsyncSession** (3 connections)
- **_IntegrationState** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **AsyncEngine** (1 connections)
- **Database fixtures for integration tests. This module provides database…** (1 connections) — `server/tests/fixtures/integration/db.py`
- **Integration-tier fixtures with real database connections.** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Return True for alembic_version and reference/world seed tables.** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Remove test-created rows; preserve reference seed (world topology, professions).** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Clean up database after each test. Deletes test-created rows from mutable…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Extract database name from a PostgreSQL URL. Returns empty string on parse…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Return True only if the URL points to an allowed test-only database…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Raise ValueError if URL is not an allowed test DB. Never truncate mythos_dev.** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Provide an isolated PostgreSQL database URL for integration tests. Reads from…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Provide a SQLAlchemy async engine bound to the integration DB URL. CRITICAL:…** (1 connections) — `server/tests/fixtures/integration/__init__.py`

## Relationships

- [session_factory](session_factory.md) (7 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (3 shared connections)
- [npc_database.py](npc_database.py.md) (2 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/fixtures/integration/db.py`

## Audit Trail

- EXTRACTED: 54 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*