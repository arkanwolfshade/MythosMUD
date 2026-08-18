# server caching cache service professioncacheservice

> 20 nodes

## Key Concepts

- **test_cache_service.py** (22 connections) — `server/tests/unit/caching/test_cache_service.py`
- **ProfessionCacheService** (20 connections) — `server/caching/cache_service.py`
- **server/caching/__init__.py** (12 connections) — `server/caching/__init__.py`
- **TestProfessionCacheService** (7 connections) — `server/tests/unit/caching/test_cache_service.py`
- **reset_cache_manager()** (5 connections) — `server/caching/lru_cache.py`
- **fixture** (5 connections)
- **_Profession** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_reset_cache_manager()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_profession_by_id_hit_and_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.invalidate_professions()** (2 connections) — `server/caching/cache_service.py`
- **.test_get_all_professions_hit_and_miss()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_profession_by_id_not_found()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_professions()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Service for caching profession data.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all profession caches.** (1 connections) — `server/caching/cache_service.py`
- **Caching module for MythosMUD server. This module provides comprehensive caching…** (1 connections) — `server/caching/__init__.py`
- **Reset the global cache manager (for testing).** (1 connections) — `server/caching/lru_cache.py`
- **Unit tests for server.caching.cache_service.** (1 connections) — `server/tests/unit/caching/test_cache_service.py`

## Relationships

- [server caching cache service cacheservice](server_caching_cache_service_cacheservice.md) (8 shared connections)
- [server caching cache service rationale](server_caching_cache_service_rationale.md) (7 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server caching cache service npccacheservice](server_caching_cache_service_npccacheservice.md) (6 shared connections)
- [server caching cache service cached](server_caching_cache_service_cached.md) (4 shared connections)
- [scripts bench cache professions](scripts_bench_cache_professions.md) (2 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [k](k.md) (2 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (1 shared connections)
- [server caching lru cache cachemanager](server_caching_lru_cache_cachemanager.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 67 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*