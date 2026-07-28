# Integration DB Fixtures

> 37 nodes · cohesion 0.09

## Key Concepts

- **__init__.py** (18 connections) — `server/tests/fixtures/integration/__init__.py`
- **session_factory()** (17 connections) — `server/tests/fixtures/integration/__init__.py`
- **db_cleanup()** (10 connections) — `server/tests/fixtures/integration/__init__.py`
- **db.py** (6 connections) — `server/tests/fixtures/integration/db.py`
- **_assert_allowed_integration_test_db()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_engine()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **_delete_mutable_integration_test_rows()** (5 connections) — `server/tests/fixtures/integration/__init__.py`
- **async_sessionmaker** (5 connections)
- **AsyncSession** (5 connections)
- **test_get_npc_system_statistics_return_shape()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_player_by_id_return_shape_and_not_found()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_rooms_with_exits_includes_arena_zone_rooms()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_rooms_with_exits_return_shape()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **_get_db_name_from_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_db_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **_is_allowed_integration_test_db()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **FixtureRequest** (3 connections)
- **AsyncSession** (3 connections)
- **_should_preserve_table_on_cleanup()** (3 connections) — `server/tests/fixtures/integration/__init__.py`
- **_IntegrationState** (2 connections) — `server/tests/fixtures/integration/__init__.py`
- **async_sessionmaker** (2 connections)
- **Database fixtures for integration tests.  This module provides database connecti** (1 connections) — `server/tests/fixtures/integration/db.py`
- **AsyncEngine** (1 connections)
- **Integration-tier fixtures with real database connections.** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Provide an async session factory for integration tests.      CRITICAL: This fixt** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- *... and 12 more nodes in this community*

## Relationships

- [Event Bus Serialization](Event_Bus_Serialization.md) (8 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (3 shared connections)
- [Metadata Npc](Metadata_Npc.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (2 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (1 shared connections)
- [Player Death Service Tests](Player_Death_Service_Tests.md) (1 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/fixtures/integration/db.py`
- `server/tests/integration/test_procedures_return_shape.py`

## Audit Trail

- EXTRACTED: 124 (89%)
- INFERRED: 15 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*