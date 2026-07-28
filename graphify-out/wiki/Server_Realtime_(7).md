# Server Realtime (7)

> 132 nodes

## Key Concepts

- **connection_manager.py** (162 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (88 connections) — `server/realtime/connection_manager_methods.py`
- **Any** (60 connections)
- **UUID** (27 connections)
- **delegate_error_handler()** (12 connections) — `server/realtime/connection_delegates.py`
- **broadcast_to_room_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_room_event_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_event_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **check_connection_health_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **CleanupContext** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **get_message_delivery_stats_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_presence_info_method()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **validate_player_presence_method()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **force_disconnect_player_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **disconnect_websocket_connection_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **detect_and_handle_error_state_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **handle_websocket_error_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **handle_authentication_error_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **handle_security_violation_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **recover_from_error_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_players_batch_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **send_initial_game_state_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **cleanup_dead_connections_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- *... and 107 more nodes in this community*

## Relationships

- [Server Realtime (4)](Server_Realtime_%284%29.md) (62 shared connections)
- [Server Realtime (12)](Server_Realtime_%2812%29.md) (39 shared connections)
- [Server Commands](Server_Commands.md) (15 shared connections)
- [Server Realtime (40)](Server_Realtime_%2840%29.md) (10 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (9 shared connections)
- [Server Realtime (56)](Server_Realtime_%2856%29.md) (7 shared connections)
- [Server Realtime (3)](Server_Realtime_%283%29.md) (7 shared connections)
- [Server Realtime (43)](Server_Realtime_%2843%29.md) (6 shared connections)
- [Server Persistence](Server_Persistence.md) (6 shared connections)
- [Server Realtime (64)](Server_Realtime_%2864%29.md) (5 shared connections)
- [Server Realtime (48)](Server_Realtime_%2848%29.md) (4 shared connections)
- [Server Realtime (14)](Server_Realtime_%2814%29.md) (4 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 799 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*