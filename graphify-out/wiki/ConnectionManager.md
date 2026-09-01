# ConnectionManager

> 169 nodes

## Key Concepts

- **ConnectionManager** (174 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **test_connection_manager_class.py** (16 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **ConnectionManager** (11 connections)
- **._track_player_disconnected()** (7 connections) — `server/realtime/connection_manager.py`
- **.broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (5 connections) — `server/realtime/connection_manager.py`
- **.track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **._check_and_process_disconnect()** (4 connections) — `server/realtime/connection_manager.py`
- **.check_connection_health()** (4 connections) — `server/realtime/connection_manager.py`
- **._cleanup_dead_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **.detect_and_handle_error_state()** (4 connections) — `server/realtime/connection_manager.py`
- **.force_disconnect_player()** (4 connections) — `server/realtime/connection_manager.py`
- **._get_players_batch()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_authentication_error()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_new_login()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_security_violation()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_websocket_error()** (4 connections) — `server/realtime/connection_manager.py`
- **._is_websocket_open()** (4 connections) — `server/realtime/connection_manager.py`
- **._prune_player_from_all_rooms()** (4 connections) — `server/realtime/connection_manager.py`
- **.recover_from_error()** (4 connections) — `server/realtime/connection_manager.py`
- **._safe_close_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- *... and 144 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (12 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (11 shared connections)
- [build_event](build_event.md) (10 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (7 shared connections)
- [EventHandler](EventHandler.md) (6 shared connections)
- [test_connection_error_methods.py](test_connection_error_methods.py.md) (5 shared connections)
- [FollowService](FollowService.md) (4 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (4 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (3 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (3 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 305 (86%)
- INFERRED: 48 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*