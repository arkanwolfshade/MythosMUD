# TransferContainerRequest

> 143 nodes

## Key Concepts

- **TransferContainerRequest** (39 connections) — `server/api/container_models.py`
- **models/container.py** (34 connections) — `server/models/container.py`
- **container_events.py** (26 connections) — `server/api/container_events.py`
- **test_container_events.py** (26 connections) — `server/tests/unit/api/test_container_events.py`
- **test_container_websocket_events.py** (24 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **asyncio** (21 connections)
- **ConnectionManager** (19 connections)
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **test_container_events_loot.py** (17 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **container_websocket_events.py** (16 connections) — `server/services/container_websocket_events.py`
- **emit_close_container_event()** (15 connections) — `server/api/container_events.py`
- **emit_container_opened()** (14 connections) — `server/services/container_websocket_events.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **emit_container_opened_to_room()** (12 connections) — `server/services/container_websocket_events.py`
- **asyncio** (12 connections)
- **TestEmitCloseContainerEvent** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **emit_container_updated()** (10 connections) — `server/services/container_websocket_events.py`
- **_assert_warning_once()** (10 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (9 connections) — `server/tests/unit/api/test_container_events.py`
- **emit_container_closed()** (9 connections) — `server/services/container_websocket_events.py`
- **emit_container_decayed()** (8 connections) — `server/services/container_websocket_events.py`
- **.test_emit_transfer_event_emission_error()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_container_direction()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 118 more nodes in this community*

## Relationships

- [pytest.md](pytest.md.md) (33 shared connections)
- [ContainerComponent](ContainerComponent.md) (26 shared connections)
- [TestEmitLootAllEvent](TestEmitLootAllEvent.md) (13 shared connections)
- [ConnectionManager](ConnectionManager.md) (9 shared connections)
- [LootAllRequest](LootAllRequest.md) (9 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (8 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [ContainerService](ContainerService.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [ContainerFactoryOptions](ContainerFactoryOptions.md) (3 shared connections)
- [ContainerLockState](ContainerLockState.md) (3 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/api/container_models.py`
- `server/models/container.py`
- `server/services/container_websocket_events.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_events_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/services/test_container_websocket_events.py`

## Audit Trail

- EXTRACTED: 398 (94%)
- INFERRED: 26 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*