# test async persistence room cache

> 8 nodes

## Key Concepts

- **test_async_persistence_room_cache.py** (32 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_load_room_cache_async_table_not_found()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_exit_rows_missing_stable_id()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_warmup_room_cache()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Unit tests for async persistence layer: load_room_cache_async, query_rooms, warm** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _load_room_cache_async handles table not found error.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _process_exit_rows handles missing stable_id.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test warmup_room_cache calls _ensure_room_cache_loaded.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`

## Relationships

- [Any](Any.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [EventDict](EventDict.md) (1 shared connections)
- [Test get spawn rules() successfully](Test_get_spawn_rules%28%29_successfully.md) (1 shared connections)
- [Tests for get container dependency](Tests_for_get_container_dependency.md) (1 shared connections)
- [middleware()](middleware%28%29.md) (1 shared connections)
- [test utility commands whoami](test_utility_commands_whoami.md) (1 shared connections)
- [Test broadcast combat ended broadcasts](Test_broadcast_combat_ended_broadcasts.md) (1 shared connections)
- [rename invites columns](rename_invites_columns.md) (1 shared connections)
- [Test handle player movement handles](Test_handle_player_movement_handles.md) (1 shared connections)
- [Test subscribe to subject returns](Test_subscribe_to_subject_returns.md) (1 shared connections)
- [add hashed password column](add_hashed_password_column.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*