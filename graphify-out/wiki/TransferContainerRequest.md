# TransferContainerRequest

> 137 nodes

## Key Concepts

- **TransferContainerRequest** (39 connections) — `server/api/container_models.py`
- **container_events.py** (26 connections) — `server/api/container_events.py`
- **test_container_events.py** (26 connections) — `server/tests/unit/api/test_container_events.py`
- **asyncio** (21 connections)
- **ConnectionManager** (19 connections)
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **test_container_events_loot.py** (17 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **emit_close_container_event()** (15 connections) — `server/api/container_events.py`
- **container_models.py** (14 connections) — `server/api/container_models.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitCloseContainerEvent** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **TestTransferItems** (11 connections) — `server/tests/unit/api/test_containers.py`
- **_assert_warning_once()** (10 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (9 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_emission_error()** (8 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_transfer_event_emission_error()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_container_direction()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_player_direction()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitTransferEventDirections** (7 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_all_items_removed()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_calculates_items_removed()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_success()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- *... and 112 more nodes in this community*

## Relationships

- [container_endpoints_basic.py](container_endpoints_basic.py.md) (26 shared connections)
- [ContainerComponent](ContainerComponent.md) (25 shared connections)
- [LootAllRequest](LootAllRequest.md) (16 shared connections)
- [test_containers.py](test_containers.py.md) (12 shared connections)
- [ConnectionManager](ConnectionManager.md) (11 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (10 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (6 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (5 shared connections)
- [ContainerService](ContainerService.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/api/container_models.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_events_loot.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 353 (91%)
- INFERRED: 36 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*