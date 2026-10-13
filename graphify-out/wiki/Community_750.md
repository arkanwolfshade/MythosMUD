# Community 750

> 22 nodes

## Key Concepts

- **test_cache_service.py** (21 connections) — `server/tests/unit/caching/test_cache_service.py`
- **lru_cache.py** (13 connections) — `server/caching/lru_cache.py`
- **cache_service.py** (12 connections) — `server/caching/cache_service.py`
- **server/caching/__init__.py** (12 connections) — `server/caching/__init__.py`
- **cached()** (10 connections) — `server/caching/cache_service.py`
- **TestCachedDecorator** (6 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_seed_players_cache()** (6 connections) — `server/tests/unit/caching/test_cache_service.py`
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
- **Reset the global cache manager (for testing).** (1 connections) — `server/caching/lru_cache.py`
- **Unit tests for server.caching.cache_service.** (1 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Keep players cache truthy; empty LRUCache is bool-false via __len__.** (1 connections) — `server/tests/unit/caching/test_cache_service.py`

## Relationships

- [Community 695](Community_695.md) (9 shared connections)
- [Community 896](Community_896.md) (8 shared connections)
- [Community 869](Community_869.md) (6 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (6 shared connections)
- [Community 522](Community_522.md) (5 shared connections)
- [Community 897](Community_897.md) (2 shared connections)
- [Community 489](Community_489.md) (2 shared connections)
- [Community 78](Community_78.md) (1 shared connections)
- [Community 793](Community_793.md) (1 shared connections)
- [Map & Admin Responses](Map_&_Admin_Responses.md) (1 shared connections)
- [Community 616](Community_616.md) (1 shared connections)

## Source Files

- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_cache_service.py`
- `server/tests/unit/test_support_helpers.py`

## Audit Trail

- EXTRACTED: 76 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*