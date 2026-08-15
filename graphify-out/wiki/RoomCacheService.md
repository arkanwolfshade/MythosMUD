# RoomCacheService

> 28 nodes

## Key Concepts

- **RoomCacheService** (29 connections) — `server/caching/cache_service.py`
- **get_cache_manager()** (21 connections) — `server/caching/lru_cache.py`
- **TestRoomCacheService** (14 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.__init__()** (7 connections) — `server/caching/cache_service.py`
- **_RoomObj** (5 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
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
- **Initialize the room cache service. Args: persistence: Persistence layer instance** (1 connections) — `server/caching/cache_service.py`
- **Invalidate cached room data. Args: room_id: The room ID to invalidate** (1 connections) — `server/caching/cache_service.py`
- *... and 3 more nodes in this community*

## Relationships

- [test_cache_service.py](test_cache_service.py.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [Any](Any.md) (6 shared connections)
- [NPCCacheService](NPCCacheService.md) (4 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (3 shared connections)
- [bench_cache.py](bench_cache.py.md) (2 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [cached](cached.md) (2 shared connections)
- [HolidayService](HolidayService.md) (1 shared connections)
- [RoomService](RoomService.md) (1 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 78 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*