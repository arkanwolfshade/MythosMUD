# Holiday Persistence Models

> 64 nodes

## Key Concepts

- **test_room_sync_service.py** (40 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **sample_event()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_update_with_validation_handles_error()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_invalidate_stale_cache_error()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_handles_error()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_get_room_sync_service_returns_singleton()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
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
- **test_fetch_fresh_room_data_no_room_service()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_not_found()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_handle_stale_room_data_success()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_handle_stale_room_data_invalid_room_id()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_handle_stale_room_data_no_room_service()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- *... and 39 more nodes in this community*

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (7 shared connections)
- [Room Data Fixer](Room_Data_Fixer.md) (3 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (3 shared connections)

## Source Files

- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 135 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*