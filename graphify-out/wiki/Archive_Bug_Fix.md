# Archive Bug Fix

> 160 nodes

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
- **.send_personal_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_message_delivery_stats()** (5 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (5 connections) — `server/realtime/connection_manager.py`
- **.broadcast_to_room()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **._get_players_batch()** (5 connections) — `server/realtime/connection_manager.py`
- **._track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **._broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.detect_and_handle_error_state()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_websocket_error()** (5 connections) — `server/realtime/connection_manager.py`
- *... and 135 more nodes in this community*

## Relationships

- [Container Exception Handlers](Container_Exception_Handlers.md) (32 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (15 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (10 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (10 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (9 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (7 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (6 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (5 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (5 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (5 shared connections)
- [Follow Service Tests](Follow_Service_Tests.md) (5 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (4 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/event_handlers.py`
- `server/realtime/websocket_handler_connection.py`

## Audit Trail

- EXTRACTED: 633 (95%)
- INFERRED: 35 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*