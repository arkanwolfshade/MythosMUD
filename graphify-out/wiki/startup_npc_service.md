# startup npc service

> 22 nodes

## Key Concepts

- **RoomCacheService** (38 connections) — `server/caching/cache_service.py`
- **TestRoomCacheService** (17 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_RoomObj** (9 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_uses_existing_rooms_cache()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_lazy_creates_rooms_cache()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_concurrent_create_uses_existing()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_sync_miss_with_to_dict()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_rooms()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.invalidate_room()** (2 connections) — `server/caching/cache_service.py`
- **.preload_rooms()** (2 connections) — `server/caching/cache_service.py`
- **.to_dict()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_cache_hit()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_miss_with_to_dict()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_miss_returns_none()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_sync_cache_hit()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_sync_miss_caches_dict()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_room()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Service for caching room data.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate cached room data.          Args:             room_id: The room ID to** (1 connections) — `server/caching/cache_service.py`
- **Preload multiple rooms into cache.          Args:             room_ids: List of** (1 connections) — `server/caching/cache_service.py`
- **Any** (1 connections)

## Relationships

- [services lucidity repository](services_lucidity_repository.md) (5 shared connections)
- [uuid services npc](uuid_services_npc.md) (5 shared connections)
- [config rationale config()](config_rationale_config%28%29.md) (4 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (4 shared connections)
- [room build realtime](room_build_realtime.md) (3 shared connections)
- [cache caching service](cache_caching_service.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [caching lru cache](caching_lru_cache.md) (1 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (1 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 83 (81%)
- INFERRED: 20 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*