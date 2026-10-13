# Community 379

> 46 nodes

## Key Concepts

- **asyncio** (20 connections)
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **emit_close_container_event()** (15 connections) — `server/api/container_events.py`
- **TestEmitCloseContainerEvent** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **_assert_warning_once()** (10 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (9 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_emission_error()** (7 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_passes_updated_container()** (7 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_close_container_event_emission_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_close_container_event_persistence_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_emission_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_validation_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_missing_mutation_token()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_room_emission_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_validation_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEventsEdgeCases** (5 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitTransferEventDirections** (5 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_close_container_event_no_container_data()** (5 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_close_container_event_no_room_id()** (5 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_close_container_event_success()** (5 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_no_room_id()** (5 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_success()** (5 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_close_container_event_no_connection_manager()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_no_connection_manager()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **Test emit_container_opened_events handles validation errors gracefully.** (3 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 21 more nodes in this community*

## Relationships

- [Community 194](Community_194.md) (20 shared connections)
- [Community 106](Community_106.md) (20 shared connections)
- [Community 94](Community_94.md) (6 shared connections)
- [Container API Models](Container_API_Models.md) (4 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Community 80](Community_80.md) (2 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/tests/unit/api/test_container_events.py`

## Audit Trail

- EXTRACTED: 121 (94%)
- INFERRED: 8 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*