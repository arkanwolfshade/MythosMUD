# Community 752

> 22 nodes

## Key Concepts

- **RoomCacheService** (28 connections) — `server/caching/cache_service.py`
- **TestRoomCacheService** (14 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_RoomObj** (5 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_cache_hit()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_miss_returns_none()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_miss_with_to_dict()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_sync_miss_with_to_dict()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_rooms()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.invalidate_room()** (2 connections) — `server/caching/cache_service.py`
- **.preload_rooms()** (2 connections) — `server/caching/cache_service.py`
- **.to_dict()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_sync_cache_hit()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_sync_miss_caches_dict()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_concurrent_create_uses_existing()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_lazy_creates_rooms_cache()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_uses_existing_rooms_cache()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_room()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Any** (1 connections)
- **Service for caching room data.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate cached room data. Args: room_id: The room ID to invalidate** (1 connections) — `server/caching/cache_service.py`
- **Preload multiple rooms into cache. Args: room_ids: List of room IDs to preload** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [Community 750](Community_750.md) (6 shared connections)
- [Community 751](Community_751.md) (4 shared connections)
- [Community 886](Community_886.md) (3 shared connections)
- [Community 1229](Community_1229.md) (2 shared connections)
- [Community 80](Community_80.md) (2 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (2 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 51 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*