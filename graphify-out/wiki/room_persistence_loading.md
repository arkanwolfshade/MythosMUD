# room persistence loading

> 8 nodes

## Key Concepts

- **test_async_persistence_room_loading.py** (28 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_exit_rows_with_partial_room_ids()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_build_room_objects_success()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_load_room_cache_with_rooms_logs_sample_ids()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Unit tests for async persistence layer: process_room_rows, process_exit_rows, bu** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _process_exit_rows with stable_ids that need room ID generation.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _build_room_objects successfully builds room objects.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _load_room_cache logs sample room IDs when rooms are loaded.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`

## Relationships

- [room game service](room_game_service.md) (13 shared connections)
- [game room service](game_room_service.md) (7 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (2 shared connections)
- [test_get_combat_result_message_success_no_damage](test_get_combat_result_message_success_no_damage.md) (1 shared connections)
- [room service game](room_service_game.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*