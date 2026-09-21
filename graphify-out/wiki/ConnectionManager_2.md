# ConnectionManager

> 200 nodes

## Key Concepts

- **ConnectionManager** (180 connections) — `server/realtime/connection_manager.py`
- **UUID** (42 connections)
- **test_connection_manager_class.py** (15 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_connection_error_methods.py** (14 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **delegate_error_handler()** (12 connections) — `server/realtime/connection_delegates.py`
- **connection_error_methods.py** (11 connections) — `server/realtime/connection_error_methods.py`
- **ConnectionManager** (11 connections)
- **detect_and_handle_error_state_impl()** (10 connections) — `server/realtime/connection_error_methods.py`
- **handle_authentication_error_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **handle_security_violation_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **handle_websocket_error_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **recover_from_error_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **._track_player_disconnected()** (7 connections) — `server/realtime/connection_manager.py`
- **UUID** (6 connections)
- **asyncio** (6 connections)
- **.broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (5 connections) — `server/realtime/connection_manager.py`
- **.track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **Any** (5 connections)
- **Player** (5 connections)
- **._check_and_process_disconnect()** (4 connections) — `server/realtime/connection_manager.py`
- **.check_connection_health()** (4 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (4 connections) — `server/realtime/connection_manager.py`
- *... and 175 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (14 shared connections)
- [container_events.py](container_events.py.md) (11 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (8 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (7 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (6 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (6 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (5 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (4 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)
- [canonical_room_id_impl](canonical_room_id_impl.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_error_methods.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_error_methods.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 379 (88%)
- INFERRED: 51 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*