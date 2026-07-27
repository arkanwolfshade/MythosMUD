# Room Sync Service

> 57 nodes · cohesion 0.04

## Key Concepts

- **test_room_sync_service.py** (37 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_get_room_sync_service_returns_singleton()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **Test clear_cache clears all rooms when room_id is None.** (2 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **mock_room_service()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **Test _process_room_update_with_validation() processes valid room data.** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **sample_event()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_clear_cache_all()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_clear_cache_specific_room()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_no_room_service()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_not_found()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_success()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_get_room_data_cache_stats()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_get_room_data_cache_stats_with_events()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_handle_stale_room_data_invalid_room_id()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_handle_stale_room_data_no_room_service()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_handle_stale_room_data_success()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_invalidate_stale_cache_no_room_service()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_invalidate_stale_cache_success()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_event_with_ordering()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_event_with_ordering_handles_error()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_event_with_ordering_increments_counter()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_event_with_ordering_tracks_last_processed()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_transition_handles_error()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_transition_missing_data()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_transition_success()** (2 connections) — `server/tests/unit/services/test_room_sync_service.py`
- *... and 32 more nodes in this community*

## Relationships

- [[Room Data Fixer]] (3 shared connections)
- [[Services Service Room]] (3 shared connections)
- [[Player Respawn Events]] (2 shared connections)
- [[Room Data Cache]] (1 shared connections)
- [[Distributed Event Bus]] (1 shared connections)

## Source Files

- `server/tests/unit/services/test_room_data_cache.py`
- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 124 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
