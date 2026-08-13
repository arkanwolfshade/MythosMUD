# CacheManager

> 17 nodes

## Key Concepts

- **CacheManager** (12 connections) — `server/caching/lru_cache.py`
- **.create_cache()** (4 connections) — `server/caching/lru_cache.py`
- **.get_cache()** (4 connections) — `server/caching/lru_cache.py`
- **Any** (4 connections)
- **.get_all_stats()** (3 connections) — `server/caching/lru_cache.py`
- **.__init__()** (3 connections) — `server/caching/lru_cache.py`
- **._initialize_default_caches()** (3 connections) — `server/caching/lru_cache.py`
- **.delete_cache()** (2 connections) — `server/caching/lru_cache.py`
- **.clear_all_caches()** (1 connections) — `server/caching/lru_cache.py`
- **.get_cache_names()** (1 connections) — `server/caching/lru_cache.py`
- **Centralized cache manager for MythosMUD server. Manages multiple LRU caches for…** (1 connections) — `server/caching/lru_cache.py`
- **Initialize the cache manager.** (1 connections) — `server/caching/lru_cache.py`
- **Initialize default caches with appropriate configurations.** (1 connections) — `server/caching/lru_cache.py`
- **Get a cache by name. Args: name: The name of the cache Returns: The cache…** (1 connections) — `server/caching/lru_cache.py`
- **Create a new cache. Args: name: The name of the cache max_size: Maximum number…** (1 connections) — `server/caching/lru_cache.py`
- **Delete a cache. Args: name: The name of the cache to delete Returns: True if…** (1 connections) — `server/caching/lru_cache.py`
- **Get statistics for all caches. Returns: Dictionary mapping cache names to their…** (1 connections) — `server/caching/lru_cache.py`

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [LRUCache](LRUCache.md) (3 shared connections)

## Source Files

- `server/caching/lru_cache.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*