# LRUCache

> 36 nodes

## Key Concepts

- **LRUCache** (27 connections) — `server/caching/lru_cache.py`
- **K** (7 connections)
- **.get_or_set()** (6 connections) — `server/caching/lru_cache.py`
- **.put()** (6 connections) — `server/caching/lru_cache.py`
- **.get()** (5 connections) — `server/caching/lru_cache.py`
- **.items()** (5 connections) — `server/caching/lru_cache.py`
- **V** (5 connections)
- **.get_stats()** (4 connections) — `server/caching/lru_cache.py`
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
- **Put an item into the cache. Args: key: The key to store value: The value to…** (1 connections) — `server/caching/lru_cache.py`
- **Delete an item from the cache. Args: key: The key to delete Returns: True if…** (1 connections) — `server/caching/lru_cache.py`
- **Clear all items from the cache.** (1 connections) — `server/caching/lru_cache.py`
- **Get the current number of items in the cache.** (1 connections) — `server/caching/lru_cache.py`
- **Check if the cache is at maximum capacity.** (1 connections) — `server/caching/lru_cache.py`
- **Get cache statistics. Returns: Dictionary containing cache statistics** (1 connections) — `server/caching/lru_cache.py`
- *... and 11 more nodes in this community*

## Relationships

- [get_cache_manager](get_cache_manager.md) (3 shared connections)
- [CacheManager](CacheManager.md) (3 shared connections)
- [test_lru_cache.py](test_lru_cache.py.md) (1 shared connections)
- [CacheService](CacheService.md) (1 shared connections)
- [NPCCacheService](NPCCacheService.md) (1 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (1 shared connections)
- [RoomCacheService](RoomCacheService.md) (1 shared connections)
- [container_helpers_inventory_display.py](container_helpers_inventory_display.py.md) (1 shared connections)

## Source Files

- `server/caching/lru_cache.py`

## Audit Trail

- EXTRACTED: 57 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*