# UUID

> 115 nodes · cohesion 0.02

## Key Concepts

- **UUID** (41 connections)
- **Any** (40 connections)
- **.check_connection_health()** (6 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (6 connections) — `server/realtime/connection_manager.py`
- **._track_player_disconnected()** (6 connections) — `server/realtime/connection_manager.py`
- **._broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.broadcast_to_room()** (5 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (5 connections) — `server/realtime/connection_manager.py`
- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.detect_and_handle_error_state()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_message_delivery_stats()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_pending_messages()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_player_presence_info()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_players_batch()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_rate_limit_info()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_authentication_error()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_new_game_session()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_security_violation()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_websocket_error()** (5 connections) — `server/realtime/connection_manager.py`
- **.recover_from_error()** (5 connections) — `server/realtime/connection_manager.py`
- **._send_initial_game_state()** (5 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message()** (5 connections) — `server/realtime/connection_manager.py`
- **._track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **.validate_player_presence()** (5 connections) — `server/realtime/connection_manager.py`
- *... and 90 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (56 shared connections)
- [connection_manager.py](connection_manager.py.md) (44 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (4 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (3 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (2 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (1 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (1 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (1 shared connections)
- [send_game_event](send_game_event.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [test_connection_statistics.py](test_connection_statistics.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 384 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*