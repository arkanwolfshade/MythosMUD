# caching lru cache

> 16 nodes

## Key Concepts

- **.items()** (8 connections) — `server/caching/lru_cache.py`
- **K** (7 connections)
- **.get_or_set()** (7 connections) — `server/caching/lru_cache.py`
- **.get()** (6 connections) — `server/caching/lru_cache.py`
- **.put()** (6 connections) — `server/caching/lru_cache.py`
- **V** (5 connections)
- **._evict_expired_entries()** (4 connections) — `server/caching/lru_cache.py`
- **.values()** (4 connections) — `server/caching/lru_cache.py`
- **.__contains__()** (3 connections) — `server/caching/lru_cache.py`
- **Get an item from the cache.          Args:             key: The key to look up** (1 connections) — `server/caching/lru_cache.py`
- **Remove expired entries from cache.          Returns:             Count of expire** (1 connections) — `server/caching/lru_cache.py`
- **Put an item into the cache.          Args:             key: The key to store** (1 connections) — `server/caching/lru_cache.py`
- **Get an item from the cache, or set it using a factory function if not found.** (1 connections) — `server/caching/lru_cache.py`
- **Get all values in the cache.** (1 connections) — `server/caching/lru_cache.py`
- **Get all key-value pairs in the cache.** (1 connections) — `server/caching/lru_cache.py`
- **Check if a key exists in the cache.** (1 connections) — `server/caching/lru_cache.py`

## Relationships

- [combat messaging service](combat_messaging_service.md) (9 shared connections)
- [time service rationale](time_service_rationale.md) (2 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (1 shared connections)
- [rescue service services](rescue_service_services.md) (1 shared connections)
- [container inventory display](container_inventory_display.md) (1 shared connections)
- [alias storage commands](alias_storage_commands.md) (1 shared connections)

## Source Files

- `server/caching/lru_cache.py`

## Audit Trail

- EXTRACTED: 54 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*