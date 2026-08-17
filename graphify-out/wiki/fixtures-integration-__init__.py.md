# fixtures/integration/__init__.py

> 54 nodes

## Key Concepts

- **session_factory()** (19 connections) — `server/tests/fixtures/integration/__init__.py`
- **fixtures/integration/__init__.py** (19 connections) — `server/tests/fixtures/integration/__init__.py`
- **db_cleanup()** (11 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_quest_start_by_trigger_then_abandon()** (10 connections) — `server/tests/integration/test_quest_flow.py`
- **test_quest_start_log_abandon_flow()** (10 connections) — `server/tests/integration/test_quest_flow.py`
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
- **_make_shared_session_factory()** (4 connections) — `server/tests/integration/test_quest_flow.py`
- **fixture** (4 connections)
- **_should_preserve_table_on_cleanup()** (3 connections) — `server/tests/fixtures/integration/__init__.py`
- **FixtureRequest** (3 connections)
- *... and 29 more nodes in this community*

## Relationships

- [get_session_maker](get_session_maker.md) (8 shared connections)
- [User](User.md) (8 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [npc_database.py](npc_database.py.md) (2 shared connections)
- [QuestService](QuestService.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [QuestInstance](QuestInstance.md) (2 shared connections)
- [LucidityService](LucidityService.md) (1 shared connections)
- [database_config_helpers.py](database_config_helpers.py.md) (1 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/fixtures/integration/db.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/integration/test_quest_flow.py`

## Audit Trail

- EXTRACTED: 103 (85%)
- INFERRED: 18 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*