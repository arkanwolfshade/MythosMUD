# overrides

> 17 nodes · cohesion 0.23

## Key Concepts

- **test_procedures_return_shape.py** (13 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_clear_player_inventory_empties_gear_and_leaves_stats_untouched()** (9 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_add_player_effect_generates_id()** (8 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **async_sessionmaker** (6 connections)
- **asyncio** (6 connections)
- **AsyncSession** (6 connections)
- **test_get_npc_system_statistics_return_shape()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_player_by_id_return_shape_and_not_found()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_rooms_with_exits_includes_arena_zone_rooms()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_get_rooms_with_exits_return_shape()** (6 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Integration tests that call PostgreSQL procedures/functions directly and verify…** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Verify get_rooms_with_exits() (room cache data source) includes arena zone…** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call get_player_by_id() with non-existent UUID; verify return shape when empty.** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call get_npc_system_statistics() and verify result columns.** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **clear_player_inventory() empties carried + equipped items and touches nothing…** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call add_player_effect() and verify it returns a non-null UUID. This guards…** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **Call get_rooms_with_exits() and verify result columns match procedure…** (1 connections) — `server/tests/integration/test_procedures_return_shape.py`

## Relationships

- [CombatBroadcastMixin](CombatBroadcastMixin.md) (6 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (3 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (3 shared connections)
- [test_room_write_procedures.py](test_room_write_procedures.py.md) (2 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (1 shared connections)
- [test_combat_persistence_handler_persistence.py](test_combat_persistence_handler_persistence.py.md) (1 shared connections)

## Source Files

- `server/tests/integration/test_procedures_return_shape.py`

## Audit Trail

- EXTRACTED: 37 (77%)
- INFERRED: 11 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*