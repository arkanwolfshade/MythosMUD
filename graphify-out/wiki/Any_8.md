# Any

> 17 nodes

## Key Concepts

- **Any** (7 connections)
- **._handle_stale_room_data()** (6 connections) — `server/services/room_sync_service.py`
- **.__init__()** (6 connections) — `server/services/room_sync_service.py`
- **._fetch_fresh_room_data()** (4 connections) — `server/services/room_sync_service.py`
- **._process_room_update_with_validation()** (4 connections) — `server/services/room_sync_service.py`
- **.get_room_data_cache_stats()** (3 connections) — `server/services/room_sync_service.py`
- **._invalidate_stale_cache()** (3 connections) — `server/services/room_sync_service.py`
- **._process_room_transition()** (3 connections) — `server/services/room_sync_service.py`
- **.set_room_service()** (3 connections) — `server/services/room_sync_service.py`
- **Process room update with comprehensive validation. Args: room_data: Room data…** (1 connections) — `server/services/room_sync_service.py`
- **Invalidate stale room cache entry. Args: room_id: Room ID to invalidate…** (1 connections) — `server/services/room_sync_service.py`
- **Fetch fresh room data from room service. Args: room_id: Room ID to fetch…** (1 connections) — `server/services/room_sync_service.py`
- **Handle stale room data by requesting fresh data. Args: room_data: Stale room…** (1 connections) — `server/services/room_sync_service.py`
- **Process room transition with proper ordering and validation. Args:…** (1 connections) — `server/services/room_sync_service.py`
- **Get statistics about the room data cache. Returns: Dict[str, Any]: Cache…** (1 connections) — `server/services/room_sync_service.py`
- **Initialize the room synchronization service. Args: room_service: Optional…** (1 connections) — `server/services/room_sync_service.py`
- **Set the room service for fetching fresh room data. Args: room_service:…** (1 connections) — `server/services/room_sync_service.py`

## Relationships

- [player_event_handlers.py](player_event_handlers.py.md) (8 shared connections)
- [RoomDataCache](RoomDataCache.md) (1 shared connections)
- [RoomDataValidator](RoomDataValidator.md) (1 shared connections)
- [TestRoomDataFixer](TestRoomDataFixer.md) (1 shared connections)

## Source Files

- `server/services/room_sync_service.py`

## Audit Trail

- EXTRACTED: 29 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*