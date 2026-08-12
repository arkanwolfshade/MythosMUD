# asyncio

> 132 nodes

## Key Concepts

- **asyncio** (28 connections)
- **test_container_websocket_events.py** (23 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_container_events.py** (22 connections) — `server/tests/unit/api/test_container_events.py`
- **container_events.py** (21 connections) — `server/api/container_events.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **container_websocket_events.py** (17 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **_emit_close_container_event()** (14 connections) — `server/api/container_events.py`
- **emit_container_opened()** (14 connections) — `server/services/container_websocket_events.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitCloseContainerEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **emit_container_opened_to_room()** (12 connections) — `server/services/container_websocket_events.py`
- **asyncio** (12 connections)
- **TestEmitContainerOpenedEvents** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **emit_container_updated()** (10 connections) — `server/services/container_websocket_events.py`
- **emit_container_closed()** (9 connections) — `server/services/container_websocket_events.py`
- **emit_container_decayed()** (8 connections) — `server/services/container_websocket_events.py`
- **UUID** (6 connections)
- **.test_emit_loot_all_event_all_items_removed()** (5 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_calculates_items_removed()** (5 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_emission_error()** (5 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_no_connection_manager()** (5 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_no_room_id()** (5 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 107 more nodes in this community*

## Relationships

- [LootAllRequest](LootAllRequest.md) (32 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (24 shared connections)
- [ContainerComponent](ContainerComponent.md) (8 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (2 shared connections)
- [mock_container](mock_container.md) (2 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/services/container_websocket_events.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/services/test_container_websocket_events.py`

## Audit Trail

- EXTRACTED: 550 (97%)
- INFERRED: 16 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*