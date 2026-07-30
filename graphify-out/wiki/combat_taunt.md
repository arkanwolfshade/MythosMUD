# combat taunt

> 75 nodes

## Key Concepts

- **test_room_sync_service.py** (40 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **RoomSyncService** (19 connections) — `server/services/room_sync_service.py`
- **room_sync_service()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **.process_event_with_ordering()** (3 connections) — `server/services/room_sync_service.py`
- **room_sync_service_with_room_service()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **sample_event()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_update_with_validation_handles_error()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_invalidate_stale_cache_error()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_handles_error()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_get_room_sync_service_returns_singleton()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **.clear_cache()** (2 connections) — `server/services/room_sync_service.py`
- **mock_room_service()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_room_sync_service_init()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_room_sync_service_init_with_room_service()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_set_room_service()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_event_with_ordering()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_event_with_ordering_increments_counter()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_event_with_ordering_tracks_last_processed()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_event_with_ordering_handles_error()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_update_with_validation_valid_data()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_update_with_validation_invalid_data()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_update_with_validation_stale_data()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_invalidate_stale_cache_success()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_invalidate_stale_cache_no_room_service()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_success()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- *... and 50 more nodes in this community*

## Relationships

- [Any](Any.md) (10 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (10 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [Manages room data caching and](Manages_room_data_caching_and.md) (1 shared connections)

## Source Files

- `server/services/room_sync_service.py`
- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 168 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*