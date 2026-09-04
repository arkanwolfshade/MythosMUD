# Test Procedures Return Shape

> 14 nodes

## Key Concepts

- **test_add_player_effect_generates_id()** (9 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_npc_system_statistics_return_shape()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_player_by_id_return_shape_and_not_found()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_rooms_with_exits_includes_arena_zone_rooms()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_rooms_with_exits_return_shape()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **async_sessionmaker** (5 connections)
- **asyncio** (5 connections)
- **AsyncSession** (5 connections)
- **serial** (1 connections)
- **Verify get_rooms_with_exits() (room cache data source) includes arena zone…** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call get_player_by_id() with non-existent UUID; verify return shape when empty.** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call get_npc_system_statistics() and verify result columns.** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call add_player_effect() and verify it returns a non-null UUID. This guards…** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call get_rooms_with_exits() and verify result columns match procedure…** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`

## Relationships

- [Player Model & Migrations](Player_Model_&_Migrations.md) (6 shared connections)
- [Init](Init.md) (5 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/tests/integration/test_procedures_return_shape.py`

## Audit Trail

- EXTRACTED: 26 (79%)
- INFERRED: 7 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*