# Player

> 152 nodes

## Key Concepts

- **ConnectionManager** (166 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **._track_player_disconnected()** (6 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **._track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **._broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.check_connection_health()** (4 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (4 connections) — `server/realtime/connection_manager.py`
- **._cleanup_dead_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (4 connections) — `server/realtime/connection_manager.py`
- **._get_players_batch()** (4 connections) — `server/realtime/connection_manager.py`
- **.detect_and_handle_error_state()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_websocket_error()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_authentication_error()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_security_violation()** (4 connections) — `server/realtime/connection_manager.py`
- **.recover_from_error()** (4 connections) — `server/realtime/connection_manager.py`
- **._check_and_process_disconnect()** (4 connections) — `server/realtime/connection_manager.py`
- **._send_initial_game_state()** (4 connections) — `server/realtime/connection_manager.py`
- **.get_player_websocket_connection_id()** (3 connections) — `server/realtime/connection_manager.py`
- **.has_websocket_connection()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_connection_count()** (3 connections) — `server/realtime/connection_manager.py`
- **.subscribe_to_room()** (3 connections) — `server/realtime/connection_manager.py`
- **.unsubscribe_from_room()** (3 connections) — `server/realtime/connection_manager.py`
- *... and 127 more nodes in this community*

## Relationships

- [Any](Any.md) (16 shared connections)
- [UUID](UUID.md) (11 shared connections)
- [Room](Room.md) (10 shared connections)
- [Player Position Service](Player_Position_Service.md) (7 shared connections)
- [APIRouter](APIRouter.md) (6 shared connections)
- [as event data dict()](as_event_data_dict%28%29.md) (6 shared connections)
- [Periodically check for cleanup conditions](Periodically_check_for_cleanup_conditions.md) (6 shared connections)
- [.connect websocket()](connect_websocket%28%29.md) (5 shared connections)
- [. init ()](_init_%28%29.md) (5 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (3 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (3 shared connections)
- [websocket handler connection](websocket_handler_connection.md) (3 shared connections)

## Source Files

- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 476 (93%)
- INFERRED: 36 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*