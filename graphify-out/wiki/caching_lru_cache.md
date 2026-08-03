# caching lru cache

> 53 nodes

## Key Concepts

- **LRUCache** (27 connections) — `server/caching/lru_cache.py`
- **CacheManager** (12 connections) — `server/caching/lru_cache.py`
- **.items()** (8 connections) — `server/caching/lru_cache.py`
- **K** (7 connections)
- **.get_or_set()** (7 connections) — `server/caching/lru_cache.py`
- **.get()** (6 connections) — `server/caching/lru_cache.py`
- **.put()** (6 connections) — `server/caching/lru_cache.py`
- **V** (5 connections)
- **.get_stats()** (5 connections) — `server/caching/lru_cache.py`
- **.keys()** (5 connections) — `server/caching/lru_cache.py`
- **.get_cache()** (5 connections) — `server/caching/lru_cache.py`
- **.get_all_stats()** (5 connections) — `server/caching/lru_cache.py`
- **._evict_expired_entries()** (4 connections) — `server/caching/lru_cache.py`
- **Any** (4 connections)
- **.values()** (4 connections) — `server/caching/lru_cache.py`
- **._initialize_default_caches()** (4 connections) — `server/caching/lru_cache.py`
- **.create_cache()** (4 connections) — `server/caching/lru_cache.py`
- **.delete()** (3 connections) — `server/caching/lru_cache.py`
- **.clear()** (3 connections) — `server/caching/lru_cache.py`
- **.size()** (3 connections) — `server/caching/lru_cache.py`
- **.__len__()** (3 connections) — `server/caching/lru_cache.py`
- **.__contains__()** (3 connections) — `server/caching/lru_cache.py`
- **.__repr__()** (3 connections) — `server/caching/lru_cache.py`
- **.__init__()** (3 connections) — `server/caching/lru_cache.py`
- **.clear_all_caches()** (3 connections) — `server/caching/lru_cache.py`
- *... and 28 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (5 shared connections)
- [cache caching service](cache_caching_service.md) (3 shared connections)
- [bench cache professions](bench_cache_professions.md) (1 shared connections)
- [cache lru caching](cache_lru_caching.md) (1 shared connections)
- [rescue service services](rescue_service_services.md) (1 shared connections)
- [container inventory display](container_inventory_display.md) (1 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)
- [health models rationale](health_models_rationale.md) (1 shared connections)

## Source Files

- `server/caching/lru_cache.py`

## Audit Trail

- EXTRACTED: 167 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*