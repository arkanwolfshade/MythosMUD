# Archive Bug Fix

> 175 nodes

## Key Concepts

- **ConnectionManager** (166 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **Any** (40 connections)
- **websocket_handler_connection.py** (17 connections) — `server/realtime/websocket_handler_connection.py`
- **cleanup_websocket_connection()** (7 connections) — `server/realtime/websocket_handler_connection.py`
- **setup_initial_connection_state()** (7 connections) — `server/realtime/websocket_handler_connection.py`
- **.check_connection_health()** (6 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (6 connections) — `server/realtime/connection_manager.py`
- **._track_player_disconnected()** (6 connections) — `server/realtime/connection_manager.py`
- **PlayerDisconnectService** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **AsyncPersistenceRoomLookup** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **send_welcome_event()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_new_game_session()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_rate_limit_info()** (5 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message_old()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_message_delivery_stats()** (5 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (5 connections) — `server/realtime/connection_manager.py`
- **.broadcast_to_room()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_pending_messages()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **._get_players_batch()** (5 connections) — `server/realtime/connection_manager.py`
- **._track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- *... and 150 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (50 shared connections)
- [Client Event Store](Client_Event_Store.md) (18 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (17 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (10 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (10 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (7 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (6 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (6 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (5 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (4 shared connections)
- [NATS Subject Patterns](NATS_Subject_Patterns.md) (3 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (3 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_helpers.py`

## Audit Trail

- EXTRACTED: 676 (95%)
- INFERRED: 37 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*