# commands skills rationale

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

- [startup npc service](startup_npc_service.md) (11 shared connections)
- [caching lru cache](caching_lru_cache.md) (9 shared connections)
- [uuid services npc](uuid_services_npc.md) (7 shared connections)
- [services lucidity repository](services_lucidity_repository.md) (6 shared connections)
- [config rationale config()](config_rationale_config%28%29.md) (5 shared connections)
- [command combat models](command_combat_models.md) (5 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [cache caching service](cache_caching_service.md) (3 shared connections)
- [room game service](room_game_service.md) (1 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [cache lru caching](cache_lru_caching.md) (1 shared connections)

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