# Tests for get profession service

> 10 nodes

## Key Concepts

- **test_get_rooms_with_exits_return_shape()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **async_sessionmaker** (5 connections)
- **AsyncSession** (5 connections)
- **test_get_rooms_with_exits_includes_arena_zone_rooms()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_player_by_id_return_shape_and_not_found()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_npc_system_statistics_return_shape()** (5 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call get_rooms_with_exits() and verify result columns match procedure definition** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Verify get_rooms_with_exits() (room cache data source) includes arena zone rooms** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call get_player_by_id() with non-existent UUID; verify return shape when empty.** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call get_npc_system_statistics() and verify result columns.** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`

## Relationships

- [. init ()](_init_%28%29.md) (6 shared connections)
- [.validate message()](validate_message%28%29.md) (4 shared connections)

## Source Files

- `server/tests/integration/test_procedures_return_shape.py`

## Audit Trail

- EXTRACTED: 30 (88%)
- INFERRED: 4 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*