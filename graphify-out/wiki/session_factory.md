# session_factory

> 26 nodes

## Key Concepts

- **session_factory()** (71 connections) — `server/tests/fixtures/integration/__init__.py`
- **fixtures/integration/__init__.py** (18 connections) — `server/tests/fixtures/integration/__init__.py`
- **db_cleanup()** (11 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_engine()** (7 connections) — `server/tests/fixtures/integration/__init__.py`
- **_assert_allowed_integration_test_db()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **_delete_mutable_integration_test_rows()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **db.py** (6 connections) — `server/tests/fixtures/integration/db.py`
- **integration_db_url()** (5 connections) — `server/tests/fixtures/integration/__init__.py`
- **_get_db_name_from_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **_is_allowed_integration_test_db()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **fixture** (4 connections)
- **FixtureRequest** (3 connections)
- **AsyncSession** (3 connections)
- **async_sessionmaker** (2 connections)
- **_IntegrationState** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **AsyncEngine** (1 connections)
- **Database fixtures for integration tests. This module provides database…** (1 connections) — `server/tests/fixtures/integration/db.py`
- **Integration-tier fixtures with real database connections.** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Provide an async session factory for integration tests. CRITICAL: This fixture…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Remove test-created rows; preserve reference seed (world topology, professions).** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Clean up database after each test. Deletes test-created rows from mutable…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Extract database name from a PostgreSQL URL. Returns empty string on parse…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Return True only if the URL points to an allowed test-only database…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Raise ValueError if URL is not an allowed test DB. Never truncate mythos_dev.** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Provide an isolated PostgreSQL database URL for integration tests. Reads from…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- *... and 1 more nodes in this community*

## Relationships

- [test_room_write_procedures.py](test_room_write_procedures.py.md) (12 shared connections)
- [test_exploration_procedures.py](test_exploration_procedures.py.md) (11 shared connections)
- [test_players_procedures.py](test_players_procedures.py.md) (9 shared connections)
- [User](User.md) (5 shared connections)
- [models/player.py](models-player.py.md) (4 shared connections)
- [test_calendar_procedures.py](test_calendar_procedures.py.md) (4 shared connections)
- [test_update_container_found_returns_the_id](test_update_container_found_returns_the_id.md) (4 shared connections)
- [subzone_with_override](subzone_with_override.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [emote_row](emote_row.md) (3 shared connections)
- [zone_and_subzone](zone_and_subzone.md) (3 shared connections)
- [_should_preserve_table_on_cleanup](_should_preserve_table_on_cleanup.md) (2 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/fixtures/integration/db.py`

## Audit Trail

- EXTRACTED: 54 (46%)
- INFERRED: 64 (54%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*