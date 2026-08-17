# server services room sync service

> 77 nodes

## Key Concepts

- **test_room_sync_service.py** (41 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **RoomSyncService** (19 connections) — `server/services/room_sync_service.py`
- **asyncio** (14 connections)
- **get_room_sync_service()** (8 connections) — `server/services/room_sync_service.py`
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
- *... and 52 more nodes in this community*

## Relationships

- [server services room sync service](server_services_room_sync_service.md) (8 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [attributeerror](attributeerror.md) (3 shared connections)
- [moduletype](moduletype.md) (2 shared connections)
- [server services room data cache](server_services_room_data_cache.md) (1 shared connections)
- [server services room data validator](server_services_room_data_validator.md) (1 shared connections)
- [server services room data fixer](server_services_room_data_fixer.md) (1 shared connections)
- [server realtime event handler py](server_realtime_event_handler_py.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [server events event bus](server_events_event_bus.md) (1 shared connections)

## Source Files

- `server/services/room_sync_service.py`
- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 112 (93%)
- INFERRED: 9 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*