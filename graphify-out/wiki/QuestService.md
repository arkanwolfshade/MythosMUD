# QuestService

> 72 nodes

## Key Concepts

- **UUID** (41 connections)
- **._track_player_disconnected()** (6 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._check_and_process_disconnect()** (4 connections) — `server/realtime/connection_manager.py`
- **.check_connection_health()** (4 connections) — `server/realtime/connection_manager.py`
- **.force_disconnect_player()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_new_game_session()** (4 connections) — `server/realtime/connection_manager.py`
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
- **.get_rate_limit_info()** (3 connections) — `server/realtime/connection_manager.py`
- **.handle_authentication_error()** (3 connections) — `server/realtime/connection_manager.py`
- **.handle_new_login()** (3 connections) — `server/realtime/connection_manager.py`
- **.handle_security_violation()** (3 connections) — `server/realtime/connection_manager.py`
- **.handle_websocket_error()** (3 connections) — `server/realtime/connection_manager.py`
- **.has_websocket_connection()** (3 connections) — `server/realtime/connection_manager.py`
- *... and 47 more nodes in this community*

## Relationships

- [PopulationStats](PopulationStats.md) (34 shared connections)
- [AnyIO vs Asyncio: High-Level Comparison and Decision Guide](AnyIO_vs_Asyncio-_High-Level_Comparison_and_Decision_Guide.md) (5 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [📞 Next Steps](📞_Next_Steps.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 116 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*