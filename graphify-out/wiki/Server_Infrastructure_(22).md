# Server Infrastructure (22)

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

- [Server Services](Server_Services.md) (3 shared connections)
- [Server Infrastructure (29)](Server_Infrastructure_%2829%29.md) (3 shared connections)
- [Server Infrastructure (32)](Server_Infrastructure_%2832%29.md) (2 shared connections)
- [Server Infrastructure (38)](Server_Infrastructure_%2838%29.md) (1 shared connections)
- [Server Infrastructure (39)](Server_Infrastructure_%2839%29.md) (1 shared connections)
- [Server Infrastructure (37)](Server_Infrastructure_%2837%29.md) (1 shared connections)
- [Server Infrastructure (36)](Server_Infrastructure_%2836%29.md) (1 shared connections)
- [Server Infrastructure (35)](Server_Infrastructure_%2835%29.md) (1 shared connections)
- [Server Infrastructure (34)](Server_Infrastructure_%2834%29.md) (1 shared connections)
- [Server Infrastructure (52)](Server_Infrastructure_%2852%29.md) (1 shared connections)
- [Server Infrastructure (43)](Server_Infrastructure_%2843%29.md) (1 shared connections)
- [Server Infrastructure (50)](Server_Infrastructure_%2850%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`

## Audit Trail

- EXTRACTED: 42 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*