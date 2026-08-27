# Implementation Phases

> 10 nodes

## Key Concepts

- **test_async_persistence_room_loading.py** (30 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_build_room_objects_debug_logging()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_load_room_cache_success()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_exit_rows_with_full_room_ids()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_room_rows_zone_single_part()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Unit tests for async persistence layer: process_room_rows, process_exit_rows,…** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _process_exit_rows with stable_ids that already contain full hierarchical…** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _build_room_objects logs debug info for specific room.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _load_room_cache successfully loads rooms.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _process_room_rows with zone_stable_id that has only one part (no slash).** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`

## Relationships

- [days](days.md) (6 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [test_unsubscribe_from_subzone_unsubscribe_failure](test_unsubscribe_from_subzone_unsubscribe_failure.md) (1 shared connections)
- [test_handle_combat_started_event](test_handle_combat_started_event.md) (1 shared connections)
- [test_handle_combat_ended_event](test_handle_combat_ended_event.md) (1 shared connections)
- [test_handle_npc_attacked_event](test_handle_npc_attacked_event.md) (1 shared connections)
- [test_handle_npc_took_damage_event](test_handle_npc_took_damage_event.md) (1 shared connections)
- [test_handle_npc_died_event](test_handle_npc_died_event.md) (1 shared connections)
- [test_handle_player_movement_different_subzone](test_handle_player_movement_different_subzone.md) (1 shared connections)
- [test_handle_player_movement_same_subzone](test_handle_player_movement_same_subzone.md) (1 shared connections)
- [test_create_unequip_command](test_create_unequip_command.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*