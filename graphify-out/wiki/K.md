# K

> 20 nodes

## Key Concepts

- **K** (7 connections)
- **.get_or_set()** (6 connections) — `server/caching/lru_cache.py`
- **.put()** (6 connections) — `server/caching/lru_cache.py`
- **.get()** (5 connections) — `server/caching/lru_cache.py`
- **.items()** (5 connections) — `server/caching/lru_cache.py`
- **V** (5 connections)
- **.__contains__()** (3 connections) — `server/caching/lru_cache.py`
- **.delete()** (3 connections) — `server/caching/lru_cache.py`
- **._evict_expired_entries()** (3 connections) — `server/caching/lru_cache.py`
- **.keys()** (3 connections) — `server/caching/lru_cache.py`
- **.values()** (3 connections) — `server/caching/lru_cache.py`
- **Put an item into the cache. Args: key: The key to store value: The value to…** (1 connections) — `server/caching/lru_cache.py`
- **Delete an item from the cache. Args: key: The key to delete Returns: True if…** (1 connections) — `server/caching/lru_cache.py`
- **Get an item from the cache, or set it using a factory function if not found.…** (1 connections) — `server/caching/lru_cache.py`
- **Get all keys in the cache.** (1 connections) — `server/caching/lru_cache.py`
- **Get all values in the cache.** (1 connections) — `server/caching/lru_cache.py`
- **Get all key-value pairs in the cache.** (1 connections) — `server/caching/lru_cache.py`
- **Check if a key exists in the cache.** (1 connections) — `server/caching/lru_cache.py`
- **Get an item from the cache. Args: key: The key to look up Returns: The cached…** (1 connections) — `server/caching/lru_cache.py`
- **Remove expired entries from cache. Returns: Count of expired entries removed** (1 connections) — `server/caching/lru_cache.py`

## Relationships

- [RoomCacheService](RoomCacheService.md) (9 shared connections)
- [test_container_helpers_inventory_display.py](test_container_helpers_inventory_display.py.md) (1 shared connections)

## Source Files

- `server/caching/lru_cache.py`

## Audit Trail

- EXTRACTED: 33 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*