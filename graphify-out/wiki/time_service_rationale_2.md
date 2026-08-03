# time service rationale

> 11 nodes

## Key Concepts

- **.get_stats()** (5 connections) — `server/caching/lru_cache.py`
- **.get_cache()** (5 connections) — `server/caching/lru_cache.py`
- **.get_all_stats()** (5 connections) — `server/caching/lru_cache.py`
- **Any** (4 connections)
- **.create_cache()** (4 connections) — `server/caching/lru_cache.py`
- **.__repr__()** (3 connections) — `server/caching/lru_cache.py`
- **Get cache statistics.          Returns:             Dictionary containing cache** (1 connections) — `server/caching/lru_cache.py`
- **String representation of the cache.** (1 connections) — `server/caching/lru_cache.py`
- **Get a cache by name.          Args:             name: The name of the cache** (1 connections) — `server/caching/lru_cache.py`
- **Create a new cache.          Args:             name: The name of the cache** (1 connections) — `server/caching/lru_cache.py`
- **Get statistics for all caches.          Returns:             Dictionary mapping** (1 connections) — `server/caching/lru_cache.py`

## Relationships

- [combat messaging service](combat_messaging_service.md) (4 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [caching lru cache](caching_lru_cache.md) (2 shared connections)

## Source Files

- `server/caching/lru_cache.py`

## Audit Trail

- EXTRACTED: 31 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*