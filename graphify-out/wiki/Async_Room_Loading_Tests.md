# Async Room Loading Tests

> 32 nodes · cohesion 0.07

## Key Concepts

- **test_async_persistence_room_loading.py** (28 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _ensure_room_cache_loaded handles DatabaseError gracefully.** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_ensure_room_cache_loaded_database_error()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_ensure_room_cache_loaded_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_build_room_objects_debug_logging()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_build_room_objects_success()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_build_room_objects_with_dict_attributes()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_ensure_room_cache_loaded_already_loaded()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_ensure_room_cache_loaded_concurrent_load()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_ensure_room_cache_loaded_os_error()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_load_room_cache_success()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_load_room_cache_with_rooms_logs_sample_ids()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_exit_rows_multiple_exits_same_room()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_exit_rows_with_full_room_ids()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_exit_rows_with_partial_room_ids()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_exit_rows_zone_single_part()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_room_rows_empty_list()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_room_rows_with_partial_room_id()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Unit tests for async persistence layer: process_room_rows, process_exit_rows, bu** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _process_exit_rows with stable_ids that already contain full hierarchical p** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _process_exit_rows with stable_ids that need room ID generation.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _build_room_objects successfully builds room objects.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _build_room_objects logs debug info for specific room.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _load_room_cache successfully loads rooms.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _load_room_cache logs sample room IDs when rooms are loaded.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- *... and 7 more nodes in this community*

## Relationships

- [[Infrastructure Async Persistence]] (9 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Database Manager Tests]] (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`

## Audit Trail

- EXTRACTED: 78 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
