# Restart Invalidating JWT

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

- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (56 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (44 shared connections)
- [Realtime Payload Optimizer](Realtime_Payload_Optimizer.md) (4 shared connections)
- [Container Loot Helpers](Container_Loot_Helpers.md) (3 shared connections)
- [NATS Message Handler Tests](NATS_Message_Handler_Tests.md) (2 shared connections)
- [Realtime Errors Error](Realtime_Errors_Error.md) (1 shared connections)
- [Realtime Event Delegation](Realtime_Event_Delegation.md) (1 shared connections)
- [Game Session Lifecycle](Game_Session_Lifecycle.md) (1 shared connections)
- [NPC Combat Handler Tests](NPC_Combat_Handler_Tests.md) (1 shared connections)
- [Whisper Reply Command Tests](Whisper_Reply_Command_Tests.md) (1 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 384 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*