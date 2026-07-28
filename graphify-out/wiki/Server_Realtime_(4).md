# Server Realtime (4)

> 169 nodes

## Key Concepts

- **ConnectionManager** (166 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **Any** (40 connections)
- **.check_connection_health()** (6 connections) — `server/realtime/connection_manager.py`
- **._track_player_disconnected()** (6 connections) — `server/realtime/connection_manager.py`
- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_rate_limit_info()** (5 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message_old()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_message_delivery_stats()** (5 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (5 connections) — `server/realtime/connection_manager.py`
- **.broadcast_to_room()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_pending_messages()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **._get_players_batch()** (5 connections) — `server/realtime/connection_manager.py`
- **._track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **._broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.detect_and_handle_error_state()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_websocket_error()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_authentication_error()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_security_violation()** (5 connections) — `server/realtime/connection_manager.py`
- **.recover_from_error()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_player_presence_info()** (5 connections) — `server/realtime/connection_manager.py`
- *... and 144 more nodes in this community*

## Relationships

- [Server Realtime (7)](Server_Realtime_%287%29.md) (62 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (14 shared connections)
- [Server Realtime (6)](Server_Realtime_%286%29.md) (11 shared connections)
- [Server Api (2)](Server_Api_%282%29.md) (6 shared connections)
- [Server Commands (8)](Server_Commands_%288%29.md) (4 shared connections)
- [Server Game (3)](Server_Game_%283%29.md) (4 shared connections)
- [Server Realtime](Server_Realtime.md) (4 shared connections)
- [Server Realtime (3)](Server_Realtime_%283%29.md) (4 shared connections)
- [Server Realtime (24)](Server_Realtime_%2824%29.md) (4 shared connections)
- [Server Realtime (16)](Server_Realtime_%2816%29.md) (3 shared connections)
- [Server Events](Server_Events.md) (3 shared connections)
- [Server Realtime (56)](Server_Realtime_%2856%29.md) (3 shared connections)

## Source Files

- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 637 (95%)
- INFERRED: 32 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*