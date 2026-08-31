# TransferContainerRequest

> 92 nodes

## Key Concepts

- **TransferContainerRequest** (39 connections) — `server/api/container_models.py`
- **container_events.py** (26 connections) — `server/api/container_events.py`
- **test_container_events.py** (26 connections) — `server/tests/unit/api/test_container_events.py`
- **asyncio** (21 connections)
- **ConnectionManager** (19 connections)
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **emit_close_container_event()** (15 connections) — `server/api/container_events.py`
- **container_models.py** (14 connections) — `server/api/container_models.py`
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
- *... and 67 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (30 shared connections)
- [ContainerComponent](ContainerComponent.md) (15 shared connections)
- [LootAllRequest](LootAllRequest.md) (12 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (9 shared connections)
- [ConnectionManager](ConnectionManager.md) (8 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [ContainerService](ContainerService.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/api/container_models.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 252 (91%)
- INFERRED: 24 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*