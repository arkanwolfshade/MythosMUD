# LucidityTierCache

> 24 nodes · cohesion 0.17

## Key Concepts

- **get_cache_manager()** (21 connections) — `server/caching/lru_cache.py`
- **test_cache_service.py** (21 connections) — `server/tests/unit/caching/test_cache_service.py`
- **cache_service.py** (14 connections) — `server/caching/cache_service.py`
- **lru_cache.py** (13 connections) — `server/caching/lru_cache.py`
- **server/caching/__init__.py** (12 connections) — `server/caching/__init__.py`
- **cached()** (11 connections) — `server/caching/cache_service.py`
- **_seed_players_cache()** (6 connections) — `server/tests/unit/caching/test_cache_service.py`
- **TestCachedDecorator** (6 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.fetch()** (6 connections) — `server/tests/unit/test_support_helpers.py`
- **reset_cache_manager()** (5 connections) — `server/caching/lru_cache.py`
- **.test_async_cache_hit_and_miss()** (5 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_cached_custom_key_func()** (5 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_async_cached_missing_cache_calls_function()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_sync_cache_hit_and_miss()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_reset_cache_manager()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_cached_missing_cache_calls_function()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Cache service for MythosMUD server. This module provides caching services that…** (1 connections) — `server/caching/cache_service.py`
- **Decorator to cache function results. Args: cache_name: Name of the cache to use…** (1 connections) — `server/caching/cache_service.py`
- **Caching module for MythosMUD server. This module provides comprehensive caching…** (1 connections) — `server/caching/__init__.py`
- **LRU Cache implementation for MythosMUD server. This module provides thread-safe…** (1 connections) — `server/caching/lru_cache.py`
- **Get the global cache manager instance. Returns: The global cache manager…** (1 connections) — `server/caching/lru_cache.py`
- **Reset the global cache manager (for testing).** (1 connections) — `server/caching/lru_cache.py`
- **Unit tests for server.caching.cache_service.** (1 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Keep players cache truthy; empty LRUCache is bool-false via __len__.** (1 connections) — `server/tests/unit/caching/test_cache_service.py`

## Relationships

- [fixture](fixture.md) (8 shared connections)
- [Persistence Layer Extraction - COMPLETE ✅](Persistence_Layer_Extraction_-_COMPLETE_✅.md) (8 shared connections)
- [Test Coverage Summary: Disconnect Grace Period & Rest Command](Test_Coverage_Summary-_Disconnect_Grace_Period_&_Rest_Command.md) (7 shared connections)
- [Room](Room.md) (6 shared connections)
- [Skill: Create a New Worktree for a Task](Skill-_Create_a_New_Worktree_for_a_Task.md) (4 shared connections)
- [ConnectionManager Refactoring Summary](ConnectionManager_Refactoring_Summary.md) (4 shared connections)
- [.get_upcoming_holidays](get_upcoming_holidays.md) (3 shared connections)
- [channel_broadcasting_strategies.py](channel_broadcasting_strategies.py.md) (3 shared connections)
- [Player](Player.md) (2 shared connections)
- [ValueError](ValueError.md) (2 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (1 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (1 shared connections)

## Source Files

- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_cache_service.py`
- `server/tests/unit/test_support_helpers.py`

## Audit Trail

- EXTRACTED: 94 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*