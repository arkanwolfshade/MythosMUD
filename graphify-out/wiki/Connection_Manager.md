# Connection Manager

> 159 nodes

## Key Concepts

- **ConnectionManager** (149 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **test_connection_manager_class.py** (16 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **ConnectionManager** (11 connections)
- **NewGameSessionResult** (7 connections) — `server/realtime/connection_session_management.py`
- **._track_player_disconnected()** (7 connections) — `server/realtime/connection_manager.py`
- **.broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_new_game_session()** (5 connections) — `server/realtime/connection_manager.py`
- **.track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **._check_and_process_disconnect()** (4 connections) — `server/realtime/connection_manager.py`
- **.check_connection_health()** (4 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (4 connections) — `server/realtime/connection_manager.py`
- **._cleanup_dead_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **.force_disconnect_player()** (4 connections) — `server/realtime/connection_manager.py`
- **._get_players_batch()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_new_login()** (4 connections) — `server/realtime/connection_manager.py`
- **.mark_player_seen()** (4 connections) — `server/realtime/connection_manager.py`
- **._send_initial_game_state()** (4 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message_old()** (4 connections) — `server/realtime/connection_manager.py`
- **._validate_token()** (4 connections) — `server/realtime/connection_manager.py`
- **manager()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_broadcast_and_health_delegates()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- *... and 134 more nodes in this community*

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (15 shared connections)
- [Connection Error Methods](Connection_Error_Methods.md) (10 shared connections)
- [Test Container Events](Test_Container_Events.md) (8 shared connections)
- [Connection Cleanup Methods](Connection_Cleanup_Methods.md) (6 shared connections)
- [Connection Manager](Connection_Manager.md) (5 shared connections)
- [Event Handlers](Event_Handlers.md) (5 shared connections)
- [Test Connection Room Utils](Test_Connection_Room_Utils.md) (4 shared connections)
- [Container/Loot Events](Container-Loot_Events.md) (3 shared connections)
- [Test Envelope](Test_Envelope.md) (3 shared connections)
- [Test Player Presence Tracker](Test_Player_Presence_Tracker.md) (3 shared connections)
- [Test Connection Disconnection](Test_Connection_Disconnection.md) (3 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (2 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_session_management.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 283 (89%)
- INFERRED: 36 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*