# Server Caching

> 88 nodes

## Key Concepts

- **LRUCache** (27 connections) — `server/caching/lru_cache.py`
- **test_lru_cache.py** (16 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **__init__.py** (12 connections) — `server/caching/__init__.py`
- **CacheManager** (12 connections) — `server/caching/lru_cache.py`
- **CacheService** (8 connections) — `server/caching/cache_service.py`
- **.items()** (8 connections) — `server/caching/lru_cache.py`
- **K** (7 connections)
- **.get_or_set()** (7 connections) — `server/caching/lru_cache.py`
- **.get()** (6 connections) — `server/caching/lru_cache.py`
- **.put()** (6 connections) — `server/caching/lru_cache.py`
- **cached()** (5 connections) — `server/caching/cache_service.py`
- **V** (5 connections)
- **.get_stats()** (5 connections) — `server/caching/lru_cache.py`
- **.keys()** (5 connections) — `server/caching/lru_cache.py`
- **.get_cache()** (5 connections) — `server/caching/lru_cache.py`
- **.get_all_stats()** (5 connections) — `server/caching/lru_cache.py`
- **._evict_expired_entries()** (4 connections) — `server/caching/lru_cache.py`
- **.delete()** (4 connections) — `server/caching/lru_cache.py`
- **Any** (4 connections)
- **.values()** (4 connections) — `server/caching/lru_cache.py`
- **._initialize_default_caches()** (4 connections) — `server/caching/lru_cache.py`
- **.create_cache()** (4 connections) — `server/caching/lru_cache.py`
- **.clear()** (3 connections) — `server/caching/lru_cache.py`
- **.size()** (3 connections) — `server/caching/lru_cache.py`
- **.__len__()** (3 connections) — `server/caching/lru_cache.py`
- *... and 63 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (10 shared connections)
- [Server Caching (2)](Server_Caching_%282%29.md) (8 shared connections)
- [Server Monitoring](Server_Monitoring.md) (3 shared connections)
- [Server Caching (3)](Server_Caching_%283%29.md) (2 shared connections)
- [Server Services](Server_Services.md) (1 shared connections)
- [Server Services (114)](Server_Services_%28114%29.md) (1 shared connections)
- [Server Commands (61)](Server_Commands_%2861%29.md) (1 shared connections)
- [Server Api](Server_Api.md) (1 shared connections)

## Source Files

- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_lru_cache.py`

## Audit Trail

- EXTRACTED: 252 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*