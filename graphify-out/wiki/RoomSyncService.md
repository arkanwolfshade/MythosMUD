# RoomSyncService

> 28 nodes · cohesion 0.10

## Key Concepts

- **RoomSyncService** (19 connections) — `server/services/room_sync_service.py`
- **Any** (7 connections)
- **._handle_stale_room_data()** (6 connections) — `server/services/room_sync_service.py`
- **.__init__()** (6 connections) — `server/services/room_sync_service.py`
- **._fetch_fresh_room_data()** (4 connections) — `server/services/room_sync_service.py`
- **._process_room_update_with_validation()** (4 connections) — `server/services/room_sync_service.py`
- **room_sync_service()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **.get_room_data_cache_stats()** (3 connections) — `server/services/room_sync_service.py`
- **._invalidate_stale_cache()** (3 connections) — `server/services/room_sync_service.py`
- **.process_event_with_ordering()** (3 connections) — `server/services/room_sync_service.py`
- **._process_room_transition()** (3 connections) — `server/services/room_sync_service.py`
- **.set_room_service()** (3 connections) — `server/services/room_sync_service.py`
- **room_sync_service_with_room_service()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **.clear_cache()** (2 connections) — `server/services/room_sync_service.py`
- **T** (1 connections)
- **Process room update with comprehensive validation.          Args:             ro** (1 connections) — `server/services/room_sync_service.py`
- **Invalidate stale room cache entry.          Args:             room_id: Room ID t** (1 connections) — `server/services/room_sync_service.py`
- **Fetch fresh room data from room service.          Args:             room_id: Roo** (1 connections) — `server/services/room_sync_service.py`
- **Handle stale room data by requesting fresh data.          Args:             room** (1 connections) — `server/services/room_sync_service.py`
- **Process room transition with proper ordering and validation.          Args:** (1 connections) — `server/services/room_sync_service.py`
- **Get statistics about the room data cache.          Returns:             Dict[str** (1 connections) — `server/services/room_sync_service.py`
- **Clear room data cache.          Args:             room_id: Specific room ID to c** (1 connections) — `server/services/room_sync_service.py`
- **Enhanced room synchronization service.      Provides improved event processing o** (1 connections) — `server/services/room_sync_service.py`
- **Initialize the room synchronization service.          Args:             room_ser** (1 connections) — `server/services/room_sync_service.py`
- **Set the room service for fetching fresh room data.          Args:             ro** (1 connections) — `server/services/room_sync_service.py`
- *... and 3 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (3 shared connections)
- [RoomDataCache](RoomDataCache.md) (2 shared connections)
- [TestRoomDataFixer](TestRoomDataFixer.md) (2 shared connections)
- [RoomDataValidator](RoomDataValidator.md) (2 shared connections)

## Source Files

- `server/services/room_sync_service.py`
- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 80 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*