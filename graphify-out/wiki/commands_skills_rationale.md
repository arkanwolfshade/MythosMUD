# commands skills rationale

> 7 nodes

## Key Concepts

- **.keys()** (5 connections) — `server/caching/lru_cache.py`
- **._initialize_default_caches()** (4 connections) — `server/caching/lru_cache.py`
- **.__init__()** (3 connections) — `server/caching/lru_cache.py`
- **.get_cache_names()** (2 connections) — `server/caching/lru_cache.py`
- **Get all keys in the cache.** (1 connections) — `server/caching/lru_cache.py`
- **Initialize the cache manager.** (1 connections) — `server/caching/lru_cache.py`
- **Initialize default caches with appropriate configurations.** (1 connections) — `server/caching/lru_cache.py`

## Relationships

- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [combat messaging service](combat_messaging_service.md) (1 shared connections)
- [caching lru cache](caching_lru_cache.md) (1 shared connections)

## Source Files

- `server/caching/lru_cache.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*