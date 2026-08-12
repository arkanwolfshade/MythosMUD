# LRUCache

> 59 nodes

## Key Concepts

- **LRUCache** (27 connections) — `server/caching/lru_cache.py`
- **get_cache_manager()** (16 connections) — `server/caching/lru_cache.py`
- **test_lru_cache.py** (16 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **cache_service.py** (13 connections) — `server/caching/cache_service.py`
- **server/caching/__init__.py** (12 connections) — `server/caching/__init__.py`
- **lru_cache.py** (12 connections) — `server/caching/lru_cache.py`
- **CacheService** (8 connections) — `server/caching/cache_service.py`
- **.__init__()** (7 connections) — `server/caching/cache_service.py`
- **cached()** (5 connections) — `server/caching/cache_service.py`
- **.__len__()** (3 connections) — `server/caching/lru_cache.py`
- **.size()** (3 connections) — `server/caching/lru_cache.py`
- **reset_cache_manager()** (3 connections) — `server/caching/lru_cache.py`
- **cache_with_ttl()** (3 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **cache_without_ttl()** (3 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_expiration_performance_impact()** (3 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **.preload_frequently_accessed_data()** (2 connections) — `server/caching/cache_service.py`
- **.clear()** (2 connections) — `server/caching/lru_cache.py`
- **.__init__()** (2 connections) — `server/caching/lru_cache.py`
- **.is_full()** (2 connections) — `server/caching/lru_cache.py`
- **test_cache_expiration_check_only_when_ttl_enabled()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_expiration_rate_calculated()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_expired_count_tracked_in_stats()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_expired_entries_not_counted_in_evictions()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_expired_entries_removed_efficiently()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_mixed_expired_and_valid_entries()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- *... and 34 more nodes in this community*

## Relationships

- [NPCCacheService](NPCCacheService.md) (10 shared connections)
- [K](K.md) (8 shared connections)
- [CacheManager](CacheManager.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (4 shared connections)
- [RoomCacheService](RoomCacheService.md) (4 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [time.py](time.py.md) (2 shared connections)
- [LucidityRepository](LucidityRepository.md) (1 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (1 shared connections)
- [RoomService](RoomService.md) (1 shared connections)

## Source Files

- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_lru_cache.py`

## Audit Trail

- EXTRACTED: 187 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*