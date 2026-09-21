# ConnectionManager

> 202 nodes

## Key Concepts

- **ConnectionManager** (180 connections) — `server/realtime/connection_manager.py`
- **UUID** (42 connections)
- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **test_connection_manager_class.py** (15 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **ConnectionManager** (11 connections)
- **_npc_died_broadcast_and_bridge()** (8 connections) — `server/realtime/event_handlers.py`
- **._track_player_disconnected()** (7 connections) — `server/realtime/connection_manager.py`
- **_publish_npc_died_to_event_bus()** (6 connections) — `server/realtime/event_handlers.py`
- **_refresh_room_after_npc_death()** (6 connections) — `server/realtime/event_handlers.py`
- **.broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_new_game_session()** (5 connections) — `server/realtime/connection_manager.py`
- **.track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **ConnectionManager** (5 connections)
- **_EventBusPublishPort** (4 connections) — `server/realtime/event_handlers.py`
- **.canonical_room_id()** (4 connections) — `server/realtime/connection_manager.py`
- **._check_and_process_disconnect()** (4 connections) — `server/realtime/connection_manager.py`
- **.check_connection_health()** (4 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (4 connections) — `server/realtime/connection_manager.py`
- **._cleanup_dead_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **.detect_and_handle_error_state()** (4 connections) — `server/realtime/connection_manager.py`
- **.force_disconnect_player()** (4 connections) — `server/realtime/connection_manager.py`
- *... and 177 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (24 shared connections)
- [EventHandler](EventHandler.md) (12 shared connections)
- [container_events.py](container_events.py.md) (11 shared connections)
- [websocket_room_updates.py](websocket_room_updates.py.md) (8 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [test_connection_error_methods.py](test_connection_error_methods.py.md) (5 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (5 shared connections)
- [event_types.py](event_types.py.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [follow_service.py](follow_service.py.md) (3 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/event_handlers.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 368 (88%)
- INFERRED: 51 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*