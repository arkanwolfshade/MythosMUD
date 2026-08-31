# test_room_sync_service.py

> 79 nodes

## Key Concepts

- **test_room_sync_service.py** (41 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **RoomSyncService** (21 connections) — `server/services/room_sync_service.py`
- **asyncio** (14 connections)
- **.__init__()** (10 connections) — `server/realtime/player_event_handlers.py`
- **room_sync_service()** (5 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **room_sync_service_with_room_service()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **sample_event()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_handles_error()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_update_with_validation_handles_error()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **fixture** (4 connections)
- **.process_event_with_ordering()** (3 connections) — `server/services/room_sync_service.py`
- **mock_room_service()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_no_room_service()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_not_found()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_success()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_get_room_sync_service_returns_singleton()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_handle_stale_room_data_invalid_room_id()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_handle_stale_room_data_no_room_service()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_handle_stale_room_data_success()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_transition_handles_error()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_transition_missing_data()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_transition_success()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_update_with_validation_invalid_data()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_update_with_validation_stale_data()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_update_with_validation_valid_data()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- *... and 54 more nodes in this community*

## Relationships

- [Any](Any.md) (8 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (7 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [RoomDataCache](RoomDataCache.md) (1 shared connections)
- [RoomDataValidator](RoomDataValidator.md) (1 shared connections)
- [TestRoomDataFixer](TestRoomDataFixer.md) (1 shared connections)
- [realtime/conftest.py](realtime-conftest.py.md) (1 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (1 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers.py`
- `server/services/room_sync_service.py`
- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 119 (93%)
- INFERRED: 9 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*