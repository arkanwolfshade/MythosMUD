# Lru Cache

> 39 nodes

## Key Concepts

- **LRUCache** (29 connections) — `server/caching/lru_cache.py`
- **K** (7 connections)
- **.get_or_set()** (6 connections) — `server/caching/lru_cache.py`
- **.put()** (6 connections) — `server/caching/lru_cache.py`
- **.get()** (5 connections) — `server/caching/lru_cache.py`
- **.items()** (5 connections) — `server/caching/lru_cache.py`
- **V** (5 connections)
- **.get_stats()** (4 connections) — `server/caching/lru_cache.py`
- **test_cache_expiration_performance_impact()** (4 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **.__contains__()** (3 connections) — `server/caching/lru_cache.py`
- **.delete()** (3 connections) — `server/caching/lru_cache.py`
- **._evict_expired_entries()** (3 connections) — `server/caching/lru_cache.py`
- **.keys()** (3 connections) — `server/caching/lru_cache.py`
- **.__len__()** (3 connections) — `server/caching/lru_cache.py`
- **.__repr__()** (3 connections) — `server/caching/lru_cache.py`
- **.size()** (3 connections) — `server/caching/lru_cache.py`
- **.values()** (3 connections) — `server/caching/lru_cache.py`
- **.clear()** (2 connections) — `server/caching/lru_cache.py`
- **.__init__()** (2 connections) — `server/caching/lru_cache.py`
- **.is_full()** (2 connections) — `server/caching/lru_cache.py`
- **asyncio** (1 connections)
- **Put an item into the cache. Args: key: The key to store value: The value to…** (1 connections) — `server/caching/lru_cache.py`
- **Delete an item from the cache. Args: key: The key to delete Returns: True if…** (1 connections) — `server/caching/lru_cache.py`
- **Clear all items from the cache.** (1 connections) — `server/caching/lru_cache.py`
- **Get the current number of items in the cache.** (1 connections) — `server/caching/lru_cache.py`
- *... and 14 more nodes in this community*

## Relationships

- [Test Lru Cache](Test_Lru_Cache.md) (4 shared connections)
- [Lru Cache](Lru_Cache.md) (3 shared connections)
- [Cache Service](Cache_Service.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Test Cache Service](Test_Cache_Service.md) (1 shared connections)
- [Container Helpers Inventory Display](Container_Helpers_Inventory_Display.md) (1 shared connections)

## Source Files

- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_lru_cache.py`

## Audit Trail

- EXTRACTED: 60 (90%)
- INFERRED: 7 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*