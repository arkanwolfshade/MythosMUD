# Player Event Handlers Respawn Room

> 51 nodes

## Key Concepts

- **player_event_handlers_respawn_room.py** (22 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **test_player_event_handlers_respawn_room.py** (14 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **prepare_room_data_for_respawn()** (11 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **extract_occupant_names()** (10 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **.app()** (9 connections) — `server/commands/admin_setstat_support.py`
- **_host()** (9 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **player_event_handlers_respawn_types.py** (9 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **_RespawnRoomHost** (8 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **enrich_room_data_with_occupant_names()** (8 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **get_npc_name_from_lifecycle_manager()** (7 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **room_data_from_persistence_room()** (7 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **get_npc_lifecycle_manager_from_connection_manager()** (7 connections) — `server/realtime/websocket_initial_state.py`
- **convert_npc_ids_to_names()** (6 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **append_unique_valid_occupant()** (5 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **ensure_respawned_player_in_lists()** (5 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **.validate_name()** (5 connections) — `server/schemas/players/player_requests.py`
- **asyncio** (5 connections)
- **merge_player_lists()** (4 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **is_npc_occupant_row()** (4 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **occupant_str_field()** (4 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **test_convert_npc_ids_to_names_resolves_lifecycle_and_short_ids()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **test_enrich_room_data_with_occupant_names()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **test_prepare_room_data_for_respawn_logs_on_error()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **test_prepare_room_data_for_respawn_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **test_prepare_room_data_for_respawn_with_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- *... and 26 more nodes in this community*

## Relationships

- [Test Websocket Initial State](Test_Websocket_Initial_State.md) (8 shared connections)
- [Test Websocket Helpers](Test_Websocket_Helpers.md) (3 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (3 shared connections)
- [Admin Setstat Support](Admin_Setstat_Support.md) (2 shared connections)
- [Test Player Event Handlers Respawn](Test_Player_Event_Handlers_Respawn.md) (2 shared connections)
- [Real Time](Real_Time.md) (1 shared connections)
- [Test Logout Commands](Test_Logout_Commands.md) (1 shared connections)
- [Test Player Presence Tracker](Test_Player_Presence_Tracker.md) (1 shared connections)
- [Test Websocket Helpers Player](Test_Websocket_Helpers_Player.md) (1 shared connections)
- [Character Creation API](Character_Creation_API.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_support.py`
- `server/realtime/player_event_handlers_respawn_room.py`
- `server/realtime/player_event_handlers_respawn_types.py`
- `server/realtime/websocket_initial_state.py`
- `server/schemas/players/player_requests.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`

## Audit Trail

- EXTRACTED: 108 (91%)
- INFERRED: 11 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*