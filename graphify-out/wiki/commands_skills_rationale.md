# commands skills rationale

> 15 nodes

## Key Concepts

- **test_cache_service.py** (21 connections) — `server/tests/unit/caching/test_cache_service.py`
- **cached()** (11 connections) — `server/caching/cache_service.py`
- **TestCachedDecorator** (10 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_seed_players_cache()** (6 connections) — `server/tests/unit/caching/test_cache_service.py`
- **reset_cache_manager()** (5 connections) — `server/caching/lru_cache.py`
- **.test_sync_cache_hit_and_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_async_cache_hit_and_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_cached_custom_key_func()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_reset_cache_manager()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_cached_missing_cache_calls_function()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_async_cached_missing_cache_calls_function()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Decorator to cache function results.      Args:         cache_name: Name of the** (1 connections) — `server/caching/cache_service.py`
- **Reset the global cache manager (for testing).** (1 connections) — `server/caching/lru_cache.py`
- **Unit tests for server.caching.cache_service.** (1 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Keep players cache truthy; empty LRUCache is bool-false via __len__.** (1 connections) — `server/tests/unit/caching/test_cache_service.py`

## Relationships

- [Error Conversion](Error_Conversion.md) (6 shared connections)
- [uuid services npc](uuid_services_npc.md) (5 shared connections)
- [startup npc service](startup_npc_service.md) (4 shared connections)
- [services lucidity repository](services_lucidity_repository.md) (4 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (3 shared connections)
- [config rationale config()](config_rationale_config%28%29.md) (3 shared connections)
- [cache caching service](cache_caching_service.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 68 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*