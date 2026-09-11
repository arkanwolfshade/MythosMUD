# session_factory

> 14 nodes

## Key Concepts

- **session_factory()** (70 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_get_npc_system_statistics_return_shape()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_player_by_id_return_shape_and_not_found()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_rooms_with_exits_includes_arena_zone_rooms()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_rooms_with_exits_return_shape()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **async_sessionmaker** (5 connections)
- **asyncio** (5 connections)
- **AsyncSession** (5 connections)
- **async_sessionmaker** (2 connections)
- **Provide an async session factory for integration tests. CRITICAL: This fixture…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Verify get_rooms_with_exits() (room cache data source) includes arena zone…** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call get_player_by_id() with non-existent UUID; verify return shape when empty.** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call get_npc_system_statistics() and verify result columns.** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call get_rooms_with_exits() and verify result columns match procedure…** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`

## Relationships

- [test_room_write_procedures.py](test_room_write_procedures.py.md) (12 shared connections)
- [Player](Player.md) (11 shared connections)
- [test_exploration_procedures.py](test_exploration_procedures.py.md) (10 shared connections)
- [test_players_procedures.py](test_players_procedures.py.md) (9 shared connections)
- [fixtures/integration/__init__.py](fixtures-integration-__init__.py.md) (7 shared connections)
- [test_calendar_procedures.py](test_calendar_procedures.py.md) (4 shared connections)
- [test_update_container_found_returns_the_id](test_update_container_found_returns_the_id.md) (4 shared connections)
- [subzone_with_override](subzone_with_override.md) (4 shared connections)
- [emote_row](emote_row.md) (3 shared connections)
- [zone_and_subzone](zone_and_subzone.md) (3 shared connections)
- [test_db_connectivity_create_and_read_user](test_db_connectivity_create_and_read_user.md) (2 shared connections)
- [test_quest_start_by_trigger_then_abandon](test_quest_start_by_trigger_then_abandon.md) (2 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/integration/test_procedures_return_shape.py`

## Audit Trail

- EXTRACTED: 32 (34%)
- INFERRED: 62 (66%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*