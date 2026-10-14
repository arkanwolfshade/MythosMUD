# session_factory

> 21 nodes

## Key Concepts

- **session_factory()** (91 connections) — `server/tests/fixtures/integration/__init__.py`
- **db_cleanup()** (13 connections) — `server/tests/fixtures/integration/__init__.py`
- **_assert_allowed_integration_test_db()** (7 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_engine()** (7 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_db_url()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **db.py** (6 connections) — `server/tests/fixtures/integration/db.py`
- **fixture** (5 connections)
- **_get_db_name_from_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **_is_allowed_integration_test_db()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **FixtureRequest** (4 connections)
- **AsyncSession** (3 connections)
- **async_sessionmaker** (2 connections)
- **AsyncEngine** (1 connections)
- **Database fixtures for integration tests. This module provides database…** (1 connections) — `server/tests/fixtures/integration/db.py`
- **Provide a SQLAlchemy async engine bound to the integration DB URL. CRITICAL:…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Provide an async session factory for integration tests. CRITICAL: This fixture…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Clean up database after each test. Deletes test-created rows from mutable…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Extract database name from a PostgreSQL URL. Returns empty string on parse…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Return True only if the URL points to an allowed test-only database…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Raise ValueError if URL is not an allowed test DB. Never truncate mythos_dev.** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Provide an isolated PostgreSQL database URL for integration tests. Reads from…** (1 connections) — `server/tests/fixtures/integration/__init__.py`

## Relationships

- [get_logger](get_logger.md) (12 shared connections)
- [test_room_write_procedures.py](test_room_write_procedures.py.md) (12 shared connections)
- [test_exploration_procedures.py](test_exploration_procedures.py.md) (11 shared connections)
- [test_players_procedures.py](test_players_procedures.py.md) (9 shared connections)
- [test_experience_procedures.py](test_experience_procedures.py.md) (7 shared connections)
- [PlayerInventory](PlayerInventory.md) (6 shared connections)
- [test_room_environment_cascade.py](test_room_environment_cascade.py.md) (5 shared connections)
- [session](session.md) (4 shared connections)
- [test_calendar_procedures.py](test_calendar_procedures.py.md) (4 shared connections)
- [test_update_container_found_returns_the_id](test_update_container_found_returns_the_id.md) (4 shared connections)
- [subzone_with_override](subzone_with_override.md) (4 shared connections)
- [ContainerCreateParams](ContainerCreateParams.md) (3 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/fixtures/integration/db.py`

## Audit Trail

- EXTRACTED: 45 (34%)
- INFERRED: 86 (66%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*