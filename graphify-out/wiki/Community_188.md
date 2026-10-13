# Community 188

> 76 nodes

## Key Concepts

- **UUID** (42 connections)
- **.broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.check_connection_health()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (5 connections) — `server/realtime/connection_manager.py`
- **.track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **._cleanup_dead_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **._get_players_batch()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_new_login()** (4 connections) — `server/realtime/connection_manager.py`
- **.mark_player_seen()** (4 connections) — `server/realtime/connection_manager.py`
- **._send_initial_game_state()** (4 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message_old()** (4 connections) — `server/realtime/connection_manager.py`
- **._validate_token()** (4 connections) — `server/realtime/connection_manager.py`
- **.broadcast_to_room()** (3 connections) — `server/realtime/connection_manager.py`
- **.check_rate_limit()** (3 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (3 connections) — `server/realtime/connection_manager.py`
- **.detect_and_handle_error_state()** (3 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket_connection()** (3 connections) — `server/realtime/connection_manager.py`
- **.force_disconnect_player()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_connection_count()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_message_delivery_stats()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_pending_messages()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_player_presence_info()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_player_session()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_player_websocket_connection_id()** (3 connections) — `server/realtime/connection_manager.py`
- *... and 51 more nodes in this community*

## Relationships

- [Community 106](Community_106.md) (36 shared connections)
- [Community 1392](Community_1392.md) (3 shared connections)
- [Community 43](Community_43.md) (2 shared connections)
- [Community 90](Community_90.md) (2 shared connections)
- [Community 634](Community_634.md) (2 shared connections)
- [Community 207](Community_207.md) (1 shared connections)
- [Community 1443](Community_1443.md) (1 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)
- [Community 1273](Community_1273.md) (1 shared connections)
- [Community 119](Community_119.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 128 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*