# Cache and NPC Cache

> 53 nodes

## Key Concepts

- **LRUCache** (27 connections) — `server/caching/lru_cache.py`
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
- **.size()** (3 connections) — `server/caching/lru_cache.py`
- **.__len__()** (3 connections) — `server/caching/lru_cache.py`
- **.__contains__()** (3 connections) — `server/caching/lru_cache.py`
- **.__repr__()** (3 connections) — `server/caching/lru_cache.py`
- **.__init__()** (3 connections) — `server/caching/lru_cache.py`
- **.clear_all_caches()** (3 connections) — `server/caching/lru_cache.py`
- *... and 28 more nodes in this community*

## Relationships

- [Grace Period Blocking Tests](Grace_Period_Blocking_Tests.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Alias Command Models](Alias_Command_Models.md) (1 shared connections)
- [Lucidity Flux Performance Bug](Lucidity_Flux_Performance_Bug.md) (1 shared connections)
- [Test Refactoring Status](Test_Refactoring_Status.md) (1 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (1 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (1 shared connections)
- [Player Effects API](Player_Effects_API.md) (1 shared connections)

## Source Files

- `server/caching/lru_cache.py`

## Audit Trail

- EXTRACTED: 167 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*