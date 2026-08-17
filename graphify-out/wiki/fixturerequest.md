# fixturerequest

> 45 nodes

## Key Concepts

- **session_factory()** (19 connections) — `server/tests/fixtures/integration/__init__.py`
- **fixtures/integration/__init__.py** (19 connections) — `server/tests/fixtures/integration/__init__.py`
- **db_cleanup()** (11 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_add_player_effect_generates_id()** (9 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **integration_engine()** (7 connections) — `server/tests/fixtures/integration/__init__.py`
- **_assert_allowed_integration_test_db()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **_delete_mutable_integration_test_rows()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_get_npc_system_statistics_return_shape()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_player_by_id_return_shape_and_not_found()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_rooms_with_exits_includes_arena_zone_rooms()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_rooms_with_exits_return_shape()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **quest_seed_data()** (6 connections) — `server/tests/integration/test_quest_flow.py`
- **db.py** (6 connections) — `server/tests/fixtures/integration/db.py`
- **integration_db_url()** (5 connections) — `server/tests/fixtures/integration/__init__.py`
- **async_sessionmaker** (5 connections)
- **asyncio** (5 connections)
- **AsyncSession** (5 connections)
- **_get_db_name_from_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **_is_allowed_integration_test_db()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **fixture** (4 connections)
- **_should_preserve_table_on_cleanup()** (3 connections) — `server/tests/fixtures/integration/__init__.py`
- **FixtureRequest** (3 connections)
- **AsyncSession** (3 connections)
- **async_sessionmaker** (2 connections)
- **_IntegrationState** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- *... and 20 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (11 shared connections)
- [server game skill service](server_game_skill_service.md) (4 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (3 shared connections)
- [e2e tests load tests get](e2e_tests_load_tests_get.md) (3 shared connections)
- [server database config helpers get](server_database_config_helpers_get.md) (2 shared connections)
- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/fixtures/integration/db.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/integration/test_quest_flow.py`

## Audit Trail

- EXTRACTED: 87 (86%)
- INFERRED: 14 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*