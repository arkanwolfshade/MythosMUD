# cached

> 11 nodes

## Key Concepts

- **cached()** (11 connections) — `server/caching/cache_service.py`
- **TestCachedDecorator** (6 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_seed_players_cache()** (6 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.fetch()** (6 connections) — `server/tests/unit/test_support_helpers.py`
- **.test_async_cache_hit_and_miss()** (5 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_cached_custom_key_func()** (5 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_async_cached_missing_cache_calls_function()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_sync_cache_hit_and_miss()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_cached_missing_cache_calls_function()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Decorator to cache function results. Args: cache_name: Name of the cache to use…** (1 connections) — `server/caching/cache_service.py`
- **Keep players cache truthy; empty LRUCache is bool-false via __len__.** (1 connections) — `server/tests/unit/caching/test_cache_service.py`

## Relationships

- [test_cache_service.py](test_cache_service.py.md) (3 shared connections)
- [RoomCacheService](RoomCacheService.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [NPCCacheService](NPCCacheService.md) (2 shared connections)
- [Any](Any.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [test_support_helpers.py](test_support_helpers.py.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`
- `server/tests/unit/test_support_helpers.py`

## Audit Trail

- EXTRACTED: 26 (81%)
- INFERRED: 6 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*