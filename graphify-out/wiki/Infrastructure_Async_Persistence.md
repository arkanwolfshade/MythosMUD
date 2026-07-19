# Infrastructure Async Persistence

> 4 nodes · cohesion 0.50

## Key Concepts

- **Test _process_room_rows handles None zone_stable_id.** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_room_rows_with_none_stable_id()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_room_rows_with_none_zone_stable_id()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_room_rows_with_none_attributes()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`

## Relationships

- [[Async Room Cache Tests]] (2 shared connections)
- [[Async Room Loading Tests]] (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
