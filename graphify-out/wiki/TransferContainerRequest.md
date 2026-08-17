# TransferContainerRequest

> 121 nodes

## Key Concepts

- **TransferContainerRequest** (39 connections) — `server/api/container_models.py`
- **test_container_events.py** (26 connections) — `server/tests/unit/api/test_container_events.py`
- **asyncio** (21 connections)
- **ConnectionManager** (19 connections)
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **emit_close_container_event()** (15 connections) — `server/api/container_events.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitCloseContainerEvent** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **TestTransferItems** (11 connections) — `server/tests/unit/api/test_containers.py`
- **CloseContainerRequest** (10 connections) — `server/api/container_models.py`
- **_assert_warning_once()** (10 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (9 connections) — `server/tests/unit/api/test_container_events.py`
- **TestCloseContainer** (8 connections) — `server/tests/unit/api/test_containers.py`
- **.test_emit_transfer_event_emission_error()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_container_direction()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_player_direction()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitTransferEventDirections** (7 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_success()** (7 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_validation_error()** (7 connections) — `server/tests/unit/api/test_container_events.py`
- **TestExecuteTransfer** (6 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_emit_close_container_event_emission_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_close_container_event_persistence_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_emission_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_validation_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 96 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (42 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (21 shared connections)
- [ContainerComponent](ContainerComponent.md) (9 shared connections)
- [ConnectionManager](ConnectionManager.md) (7 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [ContainerService](ContainerService.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [emit_loot_all_event](emit_loot_all_event.md) (2 shared connections)
- [LootAllRequest](LootAllRequest.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/api/container_models.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 288 (90%)
- INFERRED: 33 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*