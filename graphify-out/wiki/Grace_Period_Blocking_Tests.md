# Grace Period Blocking Tests

> 43 nodes

## Key Concepts

- **CacheManager** (12 connections) — `server/caching/lru_cache.py`
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
- **._initialize_default_caches()** (4 connections) — `server/caching/lru_cache.py`
- **.create_cache()** (4 connections) — `server/caching/lru_cache.py`
- **.clear()** (3 connections) — `server/caching/lru_cache.py`
- **.__contains__()** (3 connections) — `server/caching/lru_cache.py`
- **.__repr__()** (3 connections) — `server/caching/lru_cache.py`
- **.__init__()** (3 connections) — `server/caching/lru_cache.py`
- **.clear_all_caches()** (3 connections) — `server/caching/lru_cache.py`
- **.delete_cache()** (2 connections) — `server/caching/lru_cache.py`
- **.get_cache_names()** (2 connections) — `server/caching/lru_cache.py`
- **Get an item from the cache.          Args:             key: The key to look up** (1 connections) — `server/caching/lru_cache.py`
- *... and 18 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (16 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (1 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (1 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (1 shared connections)
- [Player Effects API](Player_Effects_API.md) (1 shared connections)
- [Command Field Validators](Command_Field_Validators.md) (1 shared connections)

## Source Files

- `server/caching/lru_cache.py`

## Audit Trail

- EXTRACTED: 129 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*