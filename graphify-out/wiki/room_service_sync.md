# room service sync

> 62 nodes

## Key Concepts

- **test_room_sync_service.py** (40 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **room_sync_service()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **room_sync_service_with_room_service()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **sample_event()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
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
- **test_process_room_transition_success()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- *... and 37 more nodes in this community*

## Relationships

- [room fixer services](room_fixer_services.md) (4 shared connections)
- [item models rationale](item_models_rationale.md) (3 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (3 shared connections)
- [room websocket updates](room_websocket_updates.md) (3 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 134 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*