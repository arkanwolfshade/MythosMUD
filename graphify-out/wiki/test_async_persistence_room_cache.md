# test async persistence room cache

> 8 nodes

## Key Concepts

- **test_async_persistence_room_cache.py** (32 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_get_players_batch_with_players()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_exits_for_room_no_direction()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_combined_rows_no_exits()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Unit tests for async persistence layer: load_room_cache_async, query_rooms, warm** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test get_players_batch with actual players (UUID conversion).** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _process_exits_for_room skips exits without direction.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _process_combined_rows processes rows without exits.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`

## Relationships

- [Test load room cache async](Test_load_room_cache_async.md) (5 shared connections)
- [Test parse exits json with](Test_parse_exits_json_with.md) (4 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [Test generate room id from](Test_generate_room_id_from.md) (3 shared connections)
- [Test process exit rows handles](Test_process_exit_rows_handles.md) (3 shared connections)
- [Test process exits for room](Test_process_exits_for_room.md) (2 shared connections)
- [Test process room rows handles](Test_process_room_rows_handles.md) (2 shared connections)
- [Test query rooms with exits](Test_query_rooms_with_exits.md) (2 shared connections)
- [Test get players batch with](Test_get_players_batch_with.md) (1 shared connections)
- [Test get professions when no](Test_get_professions_when_no.md) (1 shared connections)
- [Test get user by username](Test_get_user_by_username.md) (1 shared connections)
- [Test process combined rows processes](Test_process_combined_rows_processes.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`

## Audit Trail

- EXTRACTED: 42 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*