# test_cache_service.py

> 23 nodes

## Key Concepts

- **test_cache_service.py** (22 connections) — `server/tests/unit/caching/test_cache_service.py`
- **get_cache_manager()** (21 connections) — `server/caching/lru_cache.py`
- **cache_service.py** (15 connections) — `server/caching/cache_service.py`
- **lru_cache.py** (13 connections) — `server/caching/lru_cache.py`
- **server/caching/__init__.py** (12 connections) — `server/caching/__init__.py`
- **cached()** (11 connections) — `server/caching/cache_service.py`
- **TestCachedDecorator** (6 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_seed_players_cache()** (6 connections) — `server/tests/unit/caching/test_cache_service.py`
- **reset_cache_manager()** (5 connections) — `server/caching/lru_cache.py`
- **.test_async_cache_hit_and_miss()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_cached_custom_key_func()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_reset_cache_manager()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_async_cached_missing_cache_calls_function()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_sync_cache_hit_and_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_cached_missing_cache_calls_function()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Cache service for MythosMUD server. This module provides caching services that…** (1 connections) — `server/caching/cache_service.py`
- **Decorator to cache function results. Args: cache_name: Name of the cache to use…** (1 connections) — `server/caching/cache_service.py`
- **Caching module for MythosMUD server. This module provides comprehensive caching…** (1 connections) — `server/caching/__init__.py`
- **LRU Cache implementation for MythosMUD server. This module provides thread-safe…** (1 connections) — `server/caching/lru_cache.py`
- **Get the global cache manager instance. Returns: The global cache manager…** (1 connections) — `server/caching/lru_cache.py`
- **Reset the global cache manager (for testing).** (1 connections) — `server/caching/lru_cache.py`
- **Unit tests for server.caching.cache_service.** (1 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Keep players cache truthy; empty LRUCache is bool-false via __len__.** (1 connections) — `server/tests/unit/caching/test_cache_service.py`

## Relationships

- [RoomCacheService](RoomCacheService.md) (8 shared connections)
- [NPCCacheService](NPCCacheService.md) (8 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (7 shared connections)
- [CacheService](CacheService.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [Any](Any.md) (3 shared connections)
- [CacheManager](CacheManager.md) (3 shared connections)
- [LRUCache](LRUCache.md) (3 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)

## Source Files

- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 95 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*