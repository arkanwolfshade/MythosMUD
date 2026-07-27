# Async Room Cache Tests

> 30 nodes · cohesion 0.07

## Key Concepts

- **test_async_persistence_room_cache.py** (31 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _process_exit_rows handles missing direction.** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_generate_room_id_from_zone_data_with_prefix()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_get_players_batch_empty_list()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_get_user_by_username_case_insensitive_no_session()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_load_room_cache_async_other_error_raises()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_load_room_cache_async_rooms_none()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_load_room_cache_async_success_with_rooms_logs_sample_ids()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_load_room_cache_async_warning_logging()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_parse_exits_json_list()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_parse_exits_json_other_type()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_parse_exits_json_string_valid()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_combined_rows_no_exits()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_exit_rows_missing_direction()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_exit_rows_missing_stable_id()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_exit_rows_missing_zone()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_exits_for_room_no_direction()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Unit tests for async persistence layer: load_room_cache_async, query_rooms, warm** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test get_user_by_username_case_insensitive when no session is yielded.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test get_players_batch with empty list.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _generate_room_id_from_zone_data when stable_id already has full path.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _parse_exits_json with valid JSON string.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _parse_exits_json with list.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _load_room_cache_async handles case when rooms is None.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _parse_exits_json with non-string, non-list value.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- *... and 5 more nodes in this community*

## Relationships

- [[Infrastructure Async Persistence]] (14 shared connections)
- [[Player Domain Model]] (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`

## Audit Trail

- EXTRACTED: 77 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
