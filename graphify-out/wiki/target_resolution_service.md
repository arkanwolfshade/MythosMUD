# target resolution service

> 62 nodes

## Key Concepts

- **UUID** (41 connections)
- **handle_new_login_impl()** (9 connections) — `server/realtime/connection_helpers.py`
- **.check_connection_health()** (6 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (6 connections) — `server/realtime/connection_manager.py`
- **._track_player_disconnected()** (6 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **._get_players_batch()** (5 connections) — `server/realtime/connection_manager.py`
- **._track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **._broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **._send_initial_game_state()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_player_websocket_connection_id()** (4 connections) — `server/realtime/connection_manager.py`
- **.get_connection_count()** (4 connections) — `server/realtime/connection_manager.py`
- **.unsubscribe_from_room()** (4 connections) — `server/realtime/connection_manager.py`
- **.force_disconnect_player()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_new_game_session()** (4 connections) — `server/realtime/connection_manager.py`
- **.get_player_session()** (4 connections) — `server/realtime/connection_manager.py`
- **.validate_session()** (4 connections) — `server/realtime/connection_manager.py`
- **.mark_player_seen()** (4 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message_old()** (4 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (4 connections) — `server/realtime/connection_manager.py`
- **._cleanup_dead_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **._validate_token()** (4 connections) — `server/realtime/connection_manager.py`
- **.detect_and_handle_error_state()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_websocket_error()** (4 connections) — `server/realtime/connection_manager.py`
- *... and 37 more nodes in this community*

## Relationships

- [Room Broadcast](Room_Broadcast.md) (49 shared connections)
- [realtime connection helpers](realtime_connection_helpers.md) (5 shared connections)
- [connection realtime error](connection_realtime_error.md) (5 shared connections)
- [movement monitor game](movement_monitor_game.md) (3 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (2 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (2 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (1 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (1 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)
- [commands channel rationale](commands_channel_rationale.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [session connection management](session_connection_management.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 206 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*