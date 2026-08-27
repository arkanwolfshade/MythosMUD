# test_nats_service.py

> 77 nodes

## Key Concepts

- **TransferContainerRequest** (39 connections) — `server/api/container_models.py`
- **test_container_events.py** (26 connections) — `server/tests/unit/api/test_container_events.py`
- **asyncio** (21 connections)
- **ConnectionManager** (19 connections)
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **emit_close_container_event()** (15 connections) — `server/api/container_events.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitCloseContainerEvent** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **_assert_warning_once()** (10 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (9 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_emission_error()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_container_direction()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_player_direction()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitTransferEventDirections** (7 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_success()** (7 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_validation_error()** (7 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_close_container_event_emission_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_close_container_event_persistence_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_emission_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_validation_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_missing_mutation_token()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_room_emission_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_connection_manager()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_container_in_result()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_room_id()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 52 more nodes in this community*

## Relationships

- [ChatService](ChatService.md) (19 shared connections)
- [ValidationError](ValidationError.md) (19 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (11 shared connections)
- [PopulationStats](PopulationStats.md) (7 shared connections)
- [P7 · Rulings — complete](P7_·_Rulings_—_complete.md) (3 shared connections)
- [.disconnect](disconnect.md) (3 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (3 shared connections)
- [asyncio](asyncio.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/api/container_models.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 207 (90%)
- INFERRED: 22 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*