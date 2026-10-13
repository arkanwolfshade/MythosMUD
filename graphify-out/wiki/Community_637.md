# Community 637

> 27 nodes

## Key Concepts

- **db_cleanup()** (13 connections) — `server/tests/fixtures/integration/__init__.py`
- **_assert_allowed_integration_test_db()** (7 connections) — `server/tests/fixtures/integration/__init__.py`
- **_delete_mutable_integration_test_rows()** (7 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_engine()** (7 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_cleanup_deletes_rows_from_mutable_tables()** (7 connections) — `server/tests/integration/test_integration_cleanup.py`
- **integration_db_url()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **db.py** (6 connections) — `server/tests/fixtures/integration/db.py`
- **fixture** (5 connections)
- **_get_db_name_from_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **_is_allowed_integration_test_db()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **FixtureRequest** (4 connections)
- **test_integration_cleanup.py** (4 connections) — `server/tests/integration/test_integration_cleanup.py`
- **AsyncSession** (3 connections)
- **async_sessionmaker** (2 connections)
- **AsyncEngine** (1 connections)
- **async_sessionmaker** (1 connections)
- **asyncio** (1 connections)
- **AsyncSession** (1 connections)
- **Database fixtures for integration tests. This module provides database…** (1 connections) — `server/tests/fixtures/integration/db.py`
- **Provide a SQLAlchemy async engine bound to the integration DB URL. CRITICAL:…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Remove test-created rows; preserve reference seed (world topology, professions).** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Clean up database after each test. Deletes test-created rows from mutable…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Extract database name from a PostgreSQL URL. Returns empty string on parse…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Return True only if the URL points to an allowed test-only database…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Raise ValueError if URL is not an allowed test DB. Never truncate mythos_dev.** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- *... and 2 more nodes in this community*

## Relationships

- [Core Bundle & DB Init](Core_Bundle_&_DB_Init.md) (10 shared connections)
- [Community 674](Community_674.md) (7 shared connections)
- [Community 226](Community_226.md) (2 shared connections)
- [Community 1028](Community_1028.md) (2 shared connections)
- [Community 384](Community_384.md) (2 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)
- [Community 1076](Community_1076.md) (1 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (1 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/fixtures/integration/db.py`
- `server/tests/integration/test_integration_cleanup.py`

## Audit Trail

- EXTRACTED: 54 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*