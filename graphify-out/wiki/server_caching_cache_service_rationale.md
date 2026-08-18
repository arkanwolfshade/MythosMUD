# server caching cache service rationale

> 24 nodes

## Key Concepts

- **RoomCacheService** (29 connections) — `server/caching/cache_service.py`
- **get_cache_manager()** (21 connections) — `server/caching/lru_cache.py`
- **TestRoomCacheService** (14 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_RoomObj** (5 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_cache_hit()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_miss_returns_none()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_miss_with_to_dict()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_sync_miss_with_to_dict()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_concurrent_create_uses_existing()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_lazy_creates_rooms_cache()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_uses_existing_rooms_cache()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_rooms()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.invalidate_room()** (2 connections) — `server/caching/cache_service.py`
- **.preload_rooms()** (2 connections) — `server/caching/cache_service.py`
- **.to_dict()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_sync_cache_hit()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_sync_miss_caches_dict()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_room()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Any** (1 connections)
- **Service for caching room data.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate cached room data. Args: room_id: The room ID to invalidate** (1 connections) — `server/caching/cache_service.py`
- **Preload multiple rooms into cache. Args: room_ids: List of room IDs to preload** (1 connections) — `server/caching/cache_service.py`
- **Get the global cache manager instance. Returns: The global cache manager…** (1 connections) — `server/caching/lru_cache.py`

## Relationships

- [server caching cache service cacheservice](server_caching_cache_service_cacheservice.md) (8 shared connections)
- [server caching cache service professioncacheservice](server_caching_cache_service_professioncacheservice.md) (7 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server caching cache service npccacheservice](server_caching_cache_service_npccacheservice.md) (3 shared connections)
- [scripts bench cache](scripts_bench_cache.md) (2 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [server api monitoring](server_api_monitoring.md) (2 shared connections)
- [server api system monitoring get](server_api_system_monitoring_get.md) (2 shared connections)
- [server caching cache service cached](server_caching_cache_service_cached.md) (2 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (1 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (1 shared connections)
- [k](k.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 72 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*