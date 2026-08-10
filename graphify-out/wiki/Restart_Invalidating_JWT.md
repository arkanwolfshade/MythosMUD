# Restart Invalidating JWT

> 93 nodes

## Key Concepts

- **coerce_int()** (37 connections) — `server/utils/int_coercion.py`
- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerRespawnedEvent** (19 connections) — `server/events/event_types.py`
- **PlayerDeliriumRespawnedEvent** (15 connections) — `server/events/event_types.py`
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn.py`
- **int_coercion.py** (13 connections) — `server/utils/int_coercion.py`
- **test_inventory_command_coercion.py** (12 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **UUID** (11 connections)
- **.get_player_data_for_respawn()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_fallback_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._send_room_occupants_after_respawn()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._enrich_room_data_with_occupant_names()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_current_lucidity()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **RespawnPlayerStatsPayload** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.update_connection_manager_position()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 68 more nodes in this community*

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (15 shared connections)
- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (11 shared connections)
- [Panel Layout Libraries Spec](Panel_Layout_Libraries_Spec.md) (8 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (8 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (8 shared connections)
- [Plan Modernization Archive](Plan_Modernization_Archive.md) (5 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (4 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (4 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (4 shared connections)
- [Container Sync Remediation](Container_Sync_Remediation.md) (4 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (3 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (3 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 392 (94%)
- INFERRED: 23 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*