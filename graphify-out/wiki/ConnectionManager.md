# ConnectionManager

> 171 nodes

## Key Concepts

- **ConnectionManager** (257 connections) — `server/realtime/connection_manager.py`
- **TransferContainerRequest** (39 connections) — `server/api/container_models.py`
- **container_events.py** (26 connections) — `server/api/container_events.py`
- **test_container_events.py** (26 connections) — `server/tests/unit/api/test_container_events.py`
- **test_container_websocket_events.py** (24 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **asyncio** (21 connections)
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **test_container_events_loot.py** (17 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **container_websocket_events.py** (16 connections) — `server/services/container_websocket_events.py`
- **test_connection_manager_class.py** (16 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **emit_close_container_event()** (15 connections) — `server/api/container_events.py`
- **emit_container_opened()** (14 connections) — `server/services/container_websocket_events.py`
- **container_models.py** (14 connections) — `server/api/container_models.py`
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
- *... and 146 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (84 shared connections)
- [UUID](UUID.md) (37 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (26 shared connections)
- [TestEmitLootAllEvent](TestEmitLootAllEvent.md) (21 shared connections)
- [ContainerComponent](ContainerComponent.md) (19 shared connections)
- [LootAllRequest](LootAllRequest.md) (17 shared connections)
- [build_event](build_event.md) (13 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (8 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (6 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/api/container_models.py`
- `server/realtime/connection_manager.py`
- `server/realtime/event_handlers.py`
- `server/services/container_websocket_events.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_events_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`
- `server/tests/unit/services/test_container_websocket_events.py`

## Audit Trail

- EXTRACTED: 595 (91%)
- INFERRED: 61 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*