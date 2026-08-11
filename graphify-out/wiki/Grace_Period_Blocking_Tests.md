# Grace Period Blocking Tests

> 45 nodes

## Key Concepts

- **LRUCache** (27 connections) — `server/caching/lru_cache.py`
- **.items()** (8 connections) — `server/caching/lru_cache.py`
- **K** (7 connections)
- **.get_or_set()** (7 connections) — `server/caching/lru_cache.py`
- **.get()** (6 connections) — `server/caching/lru_cache.py`
- **.put()** (6 connections) — `server/caching/lru_cache.py`
- **V** (5 connections)
- **.get_stats()** (5 connections) — `server/caching/lru_cache.py`
- **.keys()** (5 connections) — `server/caching/lru_cache.py`
- **.get_cache()** (5 connections) — `server/caching/lru_cache.py`
- **.get_all_stats()** (5 connections) — `server/caching/lru_cache.py`
- **._evict_expired_entries()** (4 connections) — `server/caching/lru_cache.py`
- **.delete()** (4 connections) — `server/caching/lru_cache.py`
- **Any** (4 connections)
- **.values()** (4 connections) — `server/caching/lru_cache.py`
- **.create_cache()** (4 connections) — `server/caching/lru_cache.py`
- **.clear()** (3 connections) — `server/caching/lru_cache.py`
- **.size()** (3 connections) — `server/caching/lru_cache.py`
- **.__len__()** (3 connections) — `server/caching/lru_cache.py`
- **.__contains__()** (3 connections) — `server/caching/lru_cache.py`
- **.__repr__()** (3 connections) — `server/caching/lru_cache.py`
- **.clear_all_caches()** (3 connections) — `server/caching/lru_cache.py`
- **.__init__()** (2 connections) — `server/caching/lru_cache.py`
- **.is_full()** (2 connections) — `server/caching/lru_cache.py`
- **.get_cache_names()** (2 connections) — `server/caching/lru_cache.py`
- *... and 20 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (8 shared connections)
- [Alias Command Models](Alias_Command_Models.md) (2 shared connections)
- [E 2 E Testing Guide](E_2_E_Testing_Guide.md) (1 shared connections)
- [Structured Concurrency Patterns](Structured_Concurrency_Patterns.md) (1 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (1 shared connections)
- [Connection Room Presence Utils](Connection_Room_Presence_Utils.md) (1 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (1 shared connections)
- [Realtime Errors Error](Realtime_Errors_Error.md) (1 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (1 shared connections)
- [Player Effects API](Player_Effects_API.md) (1 shared connections)

## Source Files

- `server/caching/lru_cache.py`

## Audit Trail

- EXTRACTED: 142 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*