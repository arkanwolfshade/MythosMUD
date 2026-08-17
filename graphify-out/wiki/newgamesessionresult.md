# newgamesessionresult

> 84 nodes

## Key Concepts

- **UUID** (41 connections)
- **._track_player_disconnected()** (6 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **.broadcast_connection_message()** (4 connections) — `server/realtime/connection_manager.py`
- **._check_and_process_disconnect()** (4 connections) — `server/realtime/connection_manager.py`
- **.check_connection_health()** (4 connections) — `server/realtime/connection_manager.py`
- **.force_disconnect_player()** (4 connections) — `server/realtime/connection_manager.py`
- **._get_players_batch()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_new_game_session()** (4 connections) — `server/realtime/connection_manager.py`
- **._send_initial_game_state()** (4 connections) — `server/realtime/connection_manager.py`
- **.track_player_connected()** (4 connections) — `server/realtime/connection_manager.py`
- **.broadcast_to_room()** (3 connections) — `server/realtime/connection_manager.py`
- **.check_rate_limit()** (3 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (3 connections) — `server/realtime/connection_manager.py`
- **._cleanup_dead_websocket()** (3 connections) — `server/realtime/connection_manager.py`
- **.detect_and_handle_error_state()** (3 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket_connection()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_connection_count()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_message_delivery_stats()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_pending_messages()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_player_presence_info()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_player_session()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_player_websocket_connection_id()** (3 connections) — `server/realtime/connection_manager.py`
- *... and 59 more nodes in this community*

## Relationships

- [playercombatservice](playercombatservice.md) (39 shared connections)
- [server realtime connection disconnection](server_realtime_connection_disconnection.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)
- [server realtime connection manager connectionmanager](server_realtime_connection_manager_connectionmanager.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 132 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*