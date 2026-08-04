# room persistence cache

> 60 nodes

## Key Concepts

- **test_async_persistence_room_cache.py** (32 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_get_players_batch_with_players()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_load_room_cache_async_rooms_none()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_load_room_cache_async_table_not_found()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_load_room_cache_async_other_error_raises()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_query_rooms_with_exits_async_table_not_found()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_query_rooms_with_exits_async_other_error_raises()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_get_user_by_username_case_insensitive_no_session()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_get_professions_no_session()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_get_players_batch_empty_list()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_generate_room_id_from_zone_data_with_prefix()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_generate_room_id_from_zone_data_needs_generation()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_generate_room_id_from_zone_data_none_values()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_parse_exits_json_string_valid()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_parse_exits_json_string_invalid()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_parse_exits_json_list()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_parse_exits_json_other_type()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_exits_for_room_with_direction()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_exits_for_room_no_direction()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_exits_for_room_multiple_exits()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_combined_rows_with_exits()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_combined_rows_no_exits()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_room_rows_with_none_zone_stable_id()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_room_rows_with_none_stable_id()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_exit_rows_missing_direction()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- *... and 35 more nodes in this community*

## Relationships

- [combat models rationale](combat_models_rationale.md) (3 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`

## Audit Trail

- EXTRACTED: 120 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*