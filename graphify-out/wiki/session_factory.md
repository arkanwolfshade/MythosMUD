# session_factory

> 19 nodes

## Key Concepts

- **session_factory()** (68 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_add_player_effect_generates_id()** (9 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_npc_system_statistics_return_shape()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_player_by_id_return_shape_and_not_found()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_rooms_with_exits_includes_arena_zone_rooms()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_rooms_with_exits_return_shape()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **quest_seed_data()** (6 connections) — `server/tests/integration/test_quest_flow.py`
- **async_sessionmaker** (5 connections)
- **asyncio** (5 connections)
- **AsyncSession** (5 connections)
- **serial** (1 connections)
- **fixture** (1 connections)
- **Provide an async session factory for integration tests. CRITICAL: This fixture…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Verify get_rooms_with_exits() (room cache data source) includes arena zone…** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call get_player_by_id() with non-existent UUID; verify return shape when empty.** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call get_npc_system_statistics() and verify result columns.** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call add_player_effect() and verify it returns a non-null UUID. This guards…** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call get_rooms_with_exits() and verify result columns match procedure…** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Create User, Player, leave_the_tutorial QuestDefinition and QuestOffer. Quest…** (1 connections) — `server/tests/integration/test_quest_flow.py`

## Relationships

- [test_room_write_procedures.py](test_room_write_procedures.py.md) (12 shared connections)
- [test_exploration_procedures.py](test_exploration_procedures.py.md) (10 shared connections)
- [test_players_procedures.py](test_players_procedures.py.md) (9 shared connections)
- [Player](Player.md) (8 shared connections)
- [fixtures/integration/__init__.py](fixtures-integration-__init__.py.md) (7 shared connections)
- [test_calendar_procedures.py](test_calendar_procedures.py.md) (4 shared connections)
- [test_containers_procedures.py](test_containers_procedures.py.md) (4 shared connections)
- [test_lucidity_procedures.py](test_lucidity_procedures.py.md) (4 shared connections)
- [User](User.md) (3 shared connections)
- [test_emotes_procedures.py](test_emotes_procedures.py.md) (3 shared connections)
- [test_npcs_zone_config_procedures.py](test_npcs_zone_config_procedures.py.md) (3 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (2 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/integration/test_quest_flow.py`

## Audit Trail

- EXTRACTED: 39 (39%)
- INFERRED: 62 (61%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*