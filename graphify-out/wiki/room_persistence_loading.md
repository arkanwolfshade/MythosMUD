# room persistence loading

> 8 nodes

## Key Concepts

- **test_async_persistence_room_loading.py** (28 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_exit_rows_with_partial_room_ids()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_load_room_cache_with_rooms_logs_sample_ids()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_ensure_room_cache_loaded_already_loaded()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Unit tests for async persistence layer: process_room_rows, process_exit_rows, bu** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _process_exit_rows with stable_ids that need room ID generation.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _load_room_cache logs sample room IDs when rooms are loaded.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _ensure_room_cache_loaded returns early when cache is already loaded.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`

## Relationships

- [room infrastructure persistence](room_infrastructure_persistence.md) (14 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (4 shared connections)
- [infrastructure persistence room](infrastructure_persistence_room.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [npc populate databases](npc_populate_databases.md) (1 shared connections)
- [services ascii map](services_ascii_map.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*