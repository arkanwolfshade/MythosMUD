# Community 695

> 24 nodes

## Key Concepts

- **RoomCacheService** (28 connections) — `server/caching/cache_service.py`
- **get_cache_manager()** (15 connections) — `server/caching/lru_cache.py`
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

- [Community 750](Community_750.md) (9 shared connections)
- [Community 522](Community_522.md) (5 shared connections)
- [Community 896](Community_896.md) (3 shared connections)
- [Community 1264](Community_1264.md) (2 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (2 shared connections)
- [Map & Admin Responses](Map_&_Admin_Responses.md) (1 shared connections)
- [Community 88](Community_88.md) (1 shared connections)
- [Community 180](Community_180.md) (1 shared connections)
- [Community 897](Community_897.md) (1 shared connections)
- [Community 426](Community_426.md) (1 shared connections)
- [Community 467](Community_467.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 66 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*