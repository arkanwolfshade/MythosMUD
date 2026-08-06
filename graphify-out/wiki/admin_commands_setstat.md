# admin commands setstat

> 31 nodes

## Key Concepts

- **get_cache_manager()** (21 connections) — `server/caching/lru_cache.py`
- **test_cache_service.py** (21 connections) — `server/tests/unit/caching/test_cache_service.py`
- **cache_service.py** (14 connections) — `server/caching/cache_service.py`
- **lru_cache.py** (13 connections) — `server/caching/lru_cache.py`
- **__init__.py** (12 connections) — `server/caching/__init__.py`
- **CacheManager** (12 connections) — `server/caching/lru_cache.py`
- **cached()** (11 connections) — `server/caching/cache_service.py`
- **TestCachedDecorator** (10 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_seed_players_cache()** (6 connections) — `server/tests/unit/caching/test_cache_service.py`
- **reset_cache_manager()** (5 connections) — `server/caching/lru_cache.py`
- **._initialize_default_caches()** (4 connections) — `server/caching/lru_cache.py`
- **.__init__()** (3 connections) — `server/caching/lru_cache.py`
- **.test_sync_cache_hit_and_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_async_cache_hit_and_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_cached_custom_key_func()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.delete_cache()** (2 connections) — `server/caching/lru_cache.py`
- **_reset_cache_manager()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_cached_missing_cache_calls_function()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_async_cached_missing_cache_calls_function()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Caching module for MythosMUD server.  This module provides comprehensive caching** (1 connections) — `server/caching/__init__.py`
- **Cache service for MythosMUD server.  This module provides caching services that** (1 connections) — `server/caching/cache_service.py`
- **Decorator to cache function results.      Args:         cache_name: Name of the** (1 connections) — `server/caching/cache_service.py`
- **LRU Cache implementation for MythosMUD server.  This module provides thread-safe** (1 connections) — `server/caching/lru_cache.py`
- **Centralized cache manager for MythosMUD server.      Manages multiple LRU caches** (1 connections) — `server/caching/lru_cache.py`
- **Initialize the cache manager.** (1 connections) — `server/caching/lru_cache.py`
- *... and 6 more nodes in this community*

## Relationships

- [player left room](player_left_room.md) (11 shared connections)
- [caching lru cache](caching_lru_cache.md) (9 shared connections)
- [player requests schemas](player_requests_schemas.md) (7 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (7 shared connections)
- [services lucidity repository](services_lucidity_repository.md) (6 shared connections)
- [message realtime messaging](message_realtime_messaging.md) (5 shared connections)
- [persistence container helpers](persistence_container_helpers.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [services chat logger](services_chat_logger.md) (2 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (1 shared connections)
- [map layout useMapLayout](map_layout_useMapLayout.md) (1 shared connections)
- [metrics memory leak](metrics_memory_leak.md) (1 shared connections)

## Source Files

- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 157 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*