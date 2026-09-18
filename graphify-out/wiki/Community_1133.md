# Community 1133

> 11 nodes

## Key Concepts

- **cached()** (10 connections) — `server/caching/cache_service.py`
- **TestCachedDecorator** (6 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.fetch()** (6 connections) — `server/tests/unit/test_support_helpers.py`
- **_seed_players_cache()** (5 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_async_cache_hit_and_miss()** (5 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_async_cached_missing_cache_calls_function()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_cached_custom_key_func()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_sync_cache_hit_and_miss()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_cached_missing_cache_calls_function()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Decorator to cache function results. Args: cache_name: Name of the cache to use…** (1 connections) — `server/caching/cache_service.py`
- **Keep players cache truthy; empty LRUCache is bool-false via __len__.** (1 connections) — `server/tests/unit/caching/test_cache_service.py`

## Relationships

- [Community 750](Community_750.md) (5 shared connections)
- [Community 886](Community_886.md) (2 shared connections)
- [Community 751](Community_751.md) (1 shared connections)
- [Community 786](Community_786.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`
- `server/tests/unit/test_support_helpers.py`

## Audit Trail

- EXTRACTED: 24 (83%)
- INFERRED: 5 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*