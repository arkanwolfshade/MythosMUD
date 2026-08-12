# UUID

> 115 nodes

## Key Concepts

- **UUID** (41 connections)
- **Any** (40 connections)
- **.check_connection_health()** (6 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (6 connections) — `server/realtime/connection_manager.py`
- **._track_player_disconnected()** (6 connections) — `server/realtime/connection_manager.py`
- **._broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.broadcast_to_room()** (5 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (5 connections) — `server/realtime/connection_manager.py`
- **.detect_and_handle_error_state()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_message_delivery_stats()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_players_batch()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_authentication_error()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_new_game_session()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_security_violation()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_websocket_error()** (5 connections) — `server/realtime/connection_manager.py`
- **.recover_from_error()** (5 connections) — `server/realtime/connection_manager.py`
- **._send_initial_game_state()** (5 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message_old()** (5 connections) — `server/realtime/connection_manager.py`
- **._track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **__getattr__()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **.broadcast_global()** (4 connections) — `server/realtime/connection_manager.py`
- **.broadcast_global_event()** (4 connections) — `server/realtime/connection_manager.py`
- *... and 90 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (54 shared connections)
- [connection_manager.py](connection_manager.py.md) (25 shared connections)
- [connection_manager_health_cleanup.py](connection_manager_health_cleanup.py.md) (7 shared connections)
- [test_connection_statistics.py](test_connection_statistics.py.md) (7 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (3 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (2 shared connections)
- [time.py](time.py.md) (1 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (1 shared connections)
- [send_game_event](send_game_event.md) (1 shared connections)
- [test_connection_initialization.py](test_connection_initialization.py.md) (1 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 241 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*