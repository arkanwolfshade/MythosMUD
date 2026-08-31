# ConnectionManager

> 174 nodes

## Key Concepts

- **ConnectionManager** (174 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **test_connection_manager_class.py** (16 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **ConnectionManager** (11 connections)
- **._track_player_disconnected()** (7 connections) — `server/realtime/connection_manager.py`
- **.broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_new_game_session()** (5 connections) — `server/realtime/connection_manager.py`
- **.track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **._check_and_process_disconnect()** (4 connections) — `server/realtime/connection_manager.py`
- **.check_connection_health()** (4 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (4 connections) — `server/realtime/connection_manager.py`
- **._cleanup_dead_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **.detect_and_handle_error_state()** (4 connections) — `server/realtime/connection_manager.py`
- **.force_disconnect_player()** (4 connections) — `server/realtime/connection_manager.py`
- **._get_players_batch()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_authentication_error()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_new_login()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_security_violation()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_websocket_error()** (4 connections) — `server/realtime/connection_manager.py`
- **.mark_player_seen()** (4 connections) — `server/realtime/connection_manager.py`
- **._prune_player_from_all_rooms()** (4 connections) — `server/realtime/connection_manager.py`
- **.recover_from_error()** (4 connections) — `server/realtime/connection_manager.py`
- *... and 149 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (19 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (9 shared connections)
- [player_event_handlers_state.py](player_event_handlers_state.py.md) (6 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (6 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (5 shared connections)
- [.connect_websocket](connect_websocket.md) (5 shared connections)
- [EventHandler](EventHandler.md) (5 shared connections)
- [test_connection_error_methods.py](test_connection_error_methods.py.md) (5 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (4 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 309 (87%)
- INFERRED: 48 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*