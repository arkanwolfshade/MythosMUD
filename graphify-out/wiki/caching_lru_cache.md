# caching lru cache

> 79 nodes

## Key Concepts

- **LRUCache** (27 connections) — `server/caching/lru_cache.py`
- **test_lru_cache.py** (16 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **CacheManager** (12 connections) — `server/caching/lru_cache.py`
- **K** (7 connections)
- **.items()** (7 connections) — `server/caching/lru_cache.py`
- **.get()** (6 connections) — `server/caching/lru_cache.py`
- **.put()** (6 connections) — `server/caching/lru_cache.py`
- **.get_or_set()** (6 connections) — `server/caching/lru_cache.py`
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
- *... and 54 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (7 shared connections)
- [startup npc service](startup_npc_service.md) (1 shared connections)
- [uuid services npc](uuid_services_npc.md) (1 shared connections)
- [services lucidity repository](services_lucidity_repository.md) (1 shared connections)
- [config rationale config()](config_rationale_config%28%29.md) (1 shared connections)
- [task registry app](task_registry_app.md) (1 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)

## Source Files

- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_lru_cache.py`

## Audit Trail

- EXTRACTED: 220 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*