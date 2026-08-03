# container events rationale

> 91 nodes

## Key Concepts

- **test_container_events.py** (22 connections) — `server/tests/unit/api/test_container_events.py`
- **container_events.py** (21 connections) — `server/api/container_events.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **_emit_close_container_event()** (14 connections) — `server/api/container_events.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitCloseContainerEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitTransferEventDirections** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEventsEdgeCases** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **UUID** (5 connections)
- **Any** (4 connections)
- **.test_emit_transfer_event_success()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_connection_manager()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_container_in_result()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_room_id()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_validation_error()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_emission_error()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_success()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_no_connection_manager()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_no_room_id()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_emission_error()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_calculates_items_removed()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 66 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (54 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (10 shared connections)
- [task registry app](task_registry_app.md) (8 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/tests/unit/api/test_container_events.py`

## Audit Trail

- EXTRACTED: 308 (93%)
- INFERRED: 24 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*