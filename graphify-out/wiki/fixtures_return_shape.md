# fixtures return shape

> 45 nodes

## Key Concepts

- **__init__.py** (18 connections) — `server/tests/fixtures/integration/__init__.py`
- **session_factory()** (17 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_procedures_return_shape.py** (11 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **db_cleanup()** (10 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_add_player_effect_generates_id()** (7 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **_assert_allowed_integration_test_db()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_engine()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **db.py** (6 connections) — `server/tests/fixtures/integration/db.py`
- **_delete_mutable_integration_test_rows()** (5 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_get_rooms_with_exits_return_shape()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **async_sessionmaker** (5 connections)
- **AsyncSession** (5 connections)
- **test_get_rooms_with_exits_includes_arena_zone_rooms()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_player_by_id_return_shape_and_not_found()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_npc_system_statistics_return_shape()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **_get_db_name_from_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **_is_allowed_integration_test_db()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_db_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_db_connectivity.py** (4 connections) — `server/tests/integration/test_db_connectivity.py`
- **test_db_connectivity_create_and_read_user()** (4 connections) — `server/tests/integration/test_db_connectivity.py`
- **FixtureRequest** (3 connections)
- **AsyncSession** (3 connections)
- **_should_preserve_table_on_cleanup()** (3 connections) — `server/tests/fixtures/integration/__init__.py`
- **_IntegrationState** (2 connections) — `server/tests/fixtures/integration/__init__.py`
- **async_sessionmaker** (2 connections)
- *... and 20 more nodes in this community*

## Relationships

- [world models rationale](world_models_rationale.md) (8 shared connections)
- [models npc rationale](models_npc_rationale.md) (4 shared connections)
- [Exception Containers](Exception_Containers.md) (4 shared connections)
- [commands lucidity recovery](commands_lucidity_recovery.md) (3 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [admin auth service](admin_auth_service.md) (2 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/fixtures/integration/db.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/integration/test_procedures_return_shape.py`

## Audit Trail

- EXTRACTED: 151 (89%)
- INFERRED: 18 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*