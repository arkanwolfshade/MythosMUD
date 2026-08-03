# combat messaging service

> 15 nodes

## Key Concepts

- **LRUCache** (27 connections) — `server/caching/lru_cache.py`
- **.delete()** (3 connections) — `server/caching/lru_cache.py`
- **.clear()** (3 connections) — `server/caching/lru_cache.py`
- **.size()** (3 connections) — `server/caching/lru_cache.py`
- **.__len__()** (3 connections) — `server/caching/lru_cache.py`
- **.clear_all_caches()** (3 connections) — `server/caching/lru_cache.py`
- **.__init__()** (2 connections) — `server/caching/lru_cache.py`
- **.is_full()** (2 connections) — `server/caching/lru_cache.py`
- **Thread-safe LRU (Least Recently Used) cache implementation.      This cache auto** (1 connections) — `server/caching/lru_cache.py`
- **Initialize the LRU cache.          Args:             max_size: Maximum number of** (1 connections) — `server/caching/lru_cache.py`
- **Delete an item from the cache.          Args:             key: The key to delete** (1 connections) — `server/caching/lru_cache.py`
- **Clear all items from the cache.** (1 connections) — `server/caching/lru_cache.py`
- **Get the current number of items in the cache.** (1 connections) — `server/caching/lru_cache.py`
- **Check if the cache is at maximum capacity.** (1 connections) — `server/caching/lru_cache.py`
- **Get the number of items in the cache.** (1 connections) — `server/caching/lru_cache.py`

## Relationships

- [caching lru cache](caching_lru_cache.md) (9 shared connections)
- [command inventory factories](command_inventory_factories.md) (4 shared connections)
- [time service rationale](time_service_rationale.md) (4 shared connections)
- [services lucidity repository](services_lucidity_repository.md) (2 shared connections)
- [cache caching service](cache_caching_service.md) (2 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (1 shared connections)
- [cache lru caching](cache_lru_caching.md) (1 shared connections)

## Source Files

- `server/caching/lru_cache.py`

## Audit Trail

- EXTRACTED: 49 (92%)
- INFERRED: 4 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*