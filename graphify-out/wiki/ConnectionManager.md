# ConnectionManager

> 202 nodes

## Key Concepts

- **ConnectionManager** (167 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **test_connection_manager_class.py** (16 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_connection_error_methods.py** (15 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **delegate_error_handler()** (12 connections) — `server/realtime/connection_delegates.py`
- **connection_error_methods.py** (11 connections) — `server/realtime/connection_error_methods.py`
- **ConnectionManager** (11 connections)
- **detect_and_handle_error_state_impl()** (10 connections) — `server/realtime/connection_error_methods.py`
- **handle_authentication_error_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **handle_security_violation_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **handle_websocket_error_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **recover_from_error_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **NewGameSessionResult** (7 connections) — `server/realtime/connection_session_management.py`
- **._track_player_disconnected()** (7 connections) — `server/realtime/connection_manager.py`
- **UUID** (6 connections)
- **asyncio** (6 connections)
- **.broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_new_game_session()** (5 connections) — `server/realtime/connection_manager.py`
- **.track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **Any** (5 connections)
- **Player** (5 connections)
- *... and 177 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (19 shared connections)
- [container_events.py](container_events.py.md) (11 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (9 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (8 shared connections)
- [EventHandler](EventHandler.md) (6 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (6 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (6 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (3 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (3 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (3 shared connections)

## Source Files

- `server/container/bundles/realtime.py`
- `server/realtime/connection_delegates.py`
- `server/realtime/connection_error_methods.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_session_management.py`
- `server/tests/unit/realtime/test_connection_error_methods.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 386 (90%)
- INFERRED: 43 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*