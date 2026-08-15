# LRUCache

> 60 nodes

## Key Concepts

- **LRUCache** (29 connections) — `server/caching/lru_cache.py`
- **test_lru_cache.py** (16 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **K** (7 connections)
- **.get_or_set()** (6 connections) — `server/caching/lru_cache.py`
- **.put()** (6 connections) — `server/caching/lru_cache.py`
- **.get()** (5 connections) — `server/caching/lru_cache.py`
- **.items()** (5 connections) — `server/caching/lru_cache.py`
- **V** (5 connections)
- **cache_with_ttl()** (4 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **cache_without_ttl()** (4 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_expiration_performance_impact()** (4 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **.__contains__()** (3 connections) — `server/caching/lru_cache.py`
- **.delete()** (3 connections) — `server/caching/lru_cache.py`
- **._evict_expired_entries()** (3 connections) — `server/caching/lru_cache.py`
- **.keys()** (3 connections) — `server/caching/lru_cache.py`
- **.__len__()** (3 connections) — `server/caching/lru_cache.py`
- **.size()** (3 connections) — `server/caching/lru_cache.py`
- **.values()** (3 connections) — `server/caching/lru_cache.py`
- **.clear()** (2 connections) — `server/caching/lru_cache.py`
- **.__init__()** (2 connections) — `server/caching/lru_cache.py`
- **.is_full()** (2 connections) — `server/caching/lru_cache.py`
- **test_cache_expiration_check_only_when_ttl_enabled()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_expiration_rate_calculated()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_expired_count_tracked_in_stats()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_expired_entries_not_counted_in_evictions()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- *... and 35 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [CacheManager](CacheManager.md) (4 shared connections)
- [NPCCacheService](NPCCacheService.md) (1 shared connections)
- [test_cache_service.py](test_cache_service.py.md) (1 shared connections)
- [RoomCacheService](RoomCacheService.md) (1 shared connections)
- [container_helpers_inventory_display.py](container_helpers_inventory_display.py.md) (1 shared connections)

## Source Files

- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_lru_cache.py`

## Audit Trail

- EXTRACTED: 83 (92%)
- INFERRED: 7 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*