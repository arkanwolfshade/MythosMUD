# WebSocket Initial State

> 152 nodes · cohesion 0.02

## Key Concepts

- **websocket_initial_state.py** (45 connections) — `server/realtime/websocket_initial_state.py`
- **test_websocket_initial_state.py** (45 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **get_event_handler_for_initial_state()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **get_npc_lifecycle_manager_from_connection_manager()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **._prepare_room_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_AppWithState** (7 connections) — `server/realtime/websocket_initial_state.py`
- **Protocol** (7 connections)
- **_AppStateForEventHandler** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateWithNpcLifecycle** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcLifecycleManagerForOccupants** (6 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (6 connections)
- **_ContainerWithNpcLifecycle** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_get_event_handler_from_app_host()** (5 connections) — `server/realtime/websocket_initial_state.py`
- *... and 127 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (31 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (18 shared connections)
- [WebSocket Helper Utilities](WebSocket_Helper_Utilities.md) (16 shared connections)
- [WebSocket Player Helpers](WebSocket_Player_Helpers.md) (11 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (8 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (6 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (5 shared connections)
- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (4 shared connections)
- [Realtime WebSocket Auth](Realtime_WebSocket_Auth.md) (3 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (3 shared connections)
- [Calendar NPC Schedule](Calendar_NPC_Schedule.md) (3 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 544 (92%)
- INFERRED: 45 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*