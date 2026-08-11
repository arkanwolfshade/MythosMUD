# Restart Invalidating JWT

> 75 nodes

## Key Concepts

- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerRespawnedEvent** (19 connections) — `server/events/event_types.py`
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn.py`
- **UUID** (11 connections)
- **.get_player_data_for_respawn()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._prepare_room_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_fallback_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._send_room_occupants_after_respawn()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._enrich_room_data_with_occupant_names()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_current_lucidity()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **RespawnPlayerStatsPayload** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.update_connection_manager_position()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._room_data_from_persistence_room()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_delirium_respawn()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 50 more nodes in this community*

## Relationships

- [Character Stats Generator](Character_Stats_Generator.md) (10 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (9 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (6 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (6 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (4 shared connections)
- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (4 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (2 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (2 shared connections)
- [Profession Get Mechanical Effects](Profession_Get_Mechanical_Effects.md) (2 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 305 (96%)
- INFERRED: 14 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*