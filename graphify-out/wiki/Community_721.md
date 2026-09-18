# Community 721

> 23 nodes

## Key Concepts

- **session_factory()** (70 connections) — `server/tests/fixtures/integration/__init__.py`
- **db_cleanup()** (11 connections) — `server/tests/fixtures/integration/__init__.py`
- **_assert_allowed_integration_test_db()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_engine()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **db.py** (6 connections) — `server/tests/fixtures/integration/db.py`
- **_delete_mutable_integration_test_rows()** (5 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_db_url()** (5 connections) — `server/tests/fixtures/integration/__init__.py`
- **_get_db_name_from_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **_is_allowed_integration_test_db()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **fixture** (4 connections)
- **FixtureRequest** (3 connections)
- **AsyncSession** (3 connections)
- **async_sessionmaker** (2 connections)
- **AsyncEngine** (1 connections)
- **Database fixtures for integration tests. This module provides database…** (1 connections) — `server/tests/fixtures/integration/db.py`
- **Provide an async session factory for integration tests. CRITICAL: This fixture…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Remove test-created rows; preserve reference seed (world topology, professions).** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Clean up database after each test. Deletes test-created rows from mutable…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Extract database name from a PostgreSQL URL. Returns empty string on parse…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Return True only if the URL points to an allowed test-only database…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Raise ValueError if URL is not an allowed test DB. Never truncate mythos_dev.** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Provide an isolated PostgreSQL database URL for integration tests. Reads from…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Provide a SQLAlchemy async engine bound to the integration DB URL. CRITICAL:…** (1 connections) — `server/tests/fixtures/integration/__init__.py`

## Relationships

- [Community 549](Community_549.md) (12 shared connections)
- [Community 732](Community_732.md) (11 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (10 shared connections)
- [Community 763](Community_763.md) (9 shared connections)
- [Community 1195](Community_1195.md) (4 shared connections)
- [Community 970](Community_970.md) (4 shared connections)
- [Community 1086](Community_1086.md) (4 shared connections)
- [Community 1142](Community_1142.md) (4 shared connections)
- [Community 1197](Community_1197.md) (3 shared connections)
- [Community 1198](Community_1198.md) (3 shared connections)
- [Community 1196](Community_1196.md) (2 shared connections)
- [Community 1245](Community_1245.md) (2 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/fixtures/integration/db.py`

## Audit Trail

- EXTRACTED: 44 (42%)
- INFERRED: 62 (58%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*