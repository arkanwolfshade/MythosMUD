# Init

> 28 nodes

## Key Concepts

- **session_factory()** (59 connections) — `server/tests/fixtures/integration/__init__.py`
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
- **async_sessionmaker** (2 connections)
- **_IntegrationState** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **AsyncEngine** (1 connections)
- **Database fixtures for integration tests. This module provides database…** (1 connections) — `server/tests/fixtures/integration/db.py`
- **Integration-tier fixtures with real database connections.** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Provide an async session factory for integration tests. CRITICAL: This fixture…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Return True for alembic_version and reference/world seed tables.** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Remove test-created rows; preserve reference seed (world topology, professions).** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Clean up database after each test. Deletes test-created rows from mutable…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Extract database name from a PostgreSQL URL. Returns empty string on parse…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Return True only if the URL points to an allowed test-only database…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- *... and 3 more nodes in this community*

## Relationships

- [Test Room Write Procedures](Test_Room_Write_Procedures.md) (12 shared connections)
- [Test Exploration Procedures](Test_Exploration_Procedures.md) (10 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (5 shared connections)
- [Test Procedures Return Shape](Test_Procedures_Return_Shape.md) (5 shared connections)
- [Test Calendar Procedures](Test_Calendar_Procedures.md) (4 shared connections)
- [Test Containers Procedures](Test_Containers_Procedures.md) (4 shared connections)
- [Test Lucidity Procedures](Test_Lucidity_Procedures.md) (4 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (3 shared connections)
- [Test Emotes Procedures](Test_Emotes_Procedures.md) (3 shared connections)
- [Test Npcs Zone Config Procedures](Test_Npcs_Zone_Config_Procedures.md) (3 shared connections)
- [Test Npc Database](Test_Npc_Database.md) (2 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/fixtures/integration/db.py`

## Audit Trail

- EXTRACTED: 56 (52%)
- INFERRED: 52 (48%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*