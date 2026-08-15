# ConnectionManager

> 237 nodes

## Key Concepts

- **ConnectionManager** (254 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **container_events.py** (26 connections) — `server/api/container_events.py`
- **test_container_events.py** (25 connections) — `server/tests/unit/api/test_container_events.py`
- **asyncio** (21 connections)
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **test_container_events_loot.py** (16 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **emit_close_container_event()** (15 connections) — `server/api/container_events.py`
- **test_connection_manager_class.py** (15 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitCloseContainerEvent** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **_assert_warning_once()** (10 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (9 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_emission_error()** (8 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_transfer_event_emission_error()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_container_direction()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_player_direction()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **NewGameSessionResult** (7 connections) — `server/realtime/connection_session_management.py`
- **TestEmitTransferEventDirections** (7 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_all_items_removed()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_calculates_items_removed()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_success()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- *... and 212 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (93 shared connections)
- [get_logger](get_logger.md) (30 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (27 shared connections)
- [ContainerComponent](ContainerComponent.md) (19 shared connections)
- [LootAllRequest](LootAllRequest.md) (14 shared connections)
- [test_connection_error_methods.py](test_connection_error_methods.py.md) (10 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (10 shared connections)
- [RateLimiter](RateLimiter.md) (7 shared connections)
- [test_connection_cleanup_methods.py](test_connection_cleanup_methods.py.md) (7 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_session_management.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_events_loot.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 647 (92%)
- INFERRED: 58 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*