# room persistence loading

> 52 nodes

## Key Concepts

- **test_async_persistence_room_loading.py** (28 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_ensure_room_cache_loaded_database_error()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_room_rows_with_full_room_id()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_room_rows_with_partial_room_id()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_room_rows_with_none_attributes()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_room_rows_zone_without_slash()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_exit_rows_with_full_room_ids()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_exit_rows_with_partial_room_ids()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_exit_rows_debug_logging()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_build_room_objects_success()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_build_room_objects_with_non_dict_attributes()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_build_room_objects_debug_logging()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_load_room_cache_success()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_load_room_cache_with_rooms_logs_sample_ids()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_room_rows_empty_list()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_exit_rows_empty_list()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_exit_rows_multiple_exits_same_room()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_room_rows_zone_single_part()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_process_exit_rows_zone_single_part()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_build_room_objects_with_exits()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_build_room_objects_with_dict_attributes()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_build_room_objects_without_environment_in_attributes()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_ensure_room_cache_loaded_already_loaded()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_ensure_room_cache_loaded_concurrent_load()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_ensure_room_cache_loaded_os_error()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- *... and 27 more nodes in this community*

## Relationships

- [endpoints auth rationale](endpoints_auth_rationale.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`

## Audit Trail

- EXTRACTED: 105 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*