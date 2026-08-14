# test_room_sync_service.py

> 66 nodes

## Key Concepts

- **test_room_sync_service.py** (40 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **asyncio** (14 connections)
- **room_sync_service_with_room_service()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_handles_error()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_update_with_validation_handles_error()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **fixture** (4 connections)
- **mock_room_service()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **sample_event()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
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
- **test_clear_cache_all()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_clear_cache_specific_room()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_get_room_data_cache_stats()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_get_room_data_cache_stats_with_events()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- *... and 41 more nodes in this community*

## Relationships

- [RoomSyncService](RoomSyncService.md) (6 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 91 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*