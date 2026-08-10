# WebSocket Initial State

> 72 nodes

## Key Concepts

- **websocket_initial_state.py** (45 connections) — `server/realtime/websocket_initial_state.py`
- **test_websocket_initial_state.py** (45 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **get_event_handler_for_initial_state()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **_AppWithState** (7 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateForEventHandler** (6 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (6 connections)
- **WebSocket** (5 connections)
- **_get_player_for_death_check()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_initial_room_data()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_get_event_handler_from_app_host()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **test_send_initial_game_state_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_dead()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_alive()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_in_limbo()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_game_state_event_safely_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_game_state_event_safely_disconnected()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_game_state_event_safely_close_message_sent()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_game_state_player_not_found()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_game_state_handles_exception()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- *... and 47 more nodes in this community*

## Relationships

- [Dual Connection Troubleshooting](Dual_Connection_Troubleshooting.md) (15 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (9 shared connections)
- [Plan Modernization Archive](Plan_Modernization_Archive.md) (7 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (7 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (6 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (4 shared connections)
- [Container Data Models](Container_Data_Models.md) (4 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (4 shared connections)
- [Combat Command Helpers](Combat_Command_Helpers.md) (4 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (4 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 311 (96%)
- INFERRED: 14 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*