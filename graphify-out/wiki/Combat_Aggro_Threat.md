# Combat Aggro Threat

> 55 nodes

## Key Concepts

- **test_websocket_helpers.py** (34 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **get_npc_name_from_instance()** (12 connections) — `server/realtime/websocket_helpers.py`
- **check_shutdown_and_reject()** (12 connections) — `server/realtime/websocket_helpers.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **load_player_mute_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **test_get_npc_name_from_instance_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_npc_name_from_instance_not_found()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_npc_name_from_instance_no_name_attribute()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_npc_name_from_instance_import_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_npc_name_from_instance_runtime_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_check_shutdown_and_reject_not_shutting_down()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_check_shutdown_and_reject_shutting_down()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_check_shutdown_and_reject_websocket_disconnect()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_load_player_mute_data_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_load_player_mute_data_import_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_validate_occupant_name_valid()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_validate_occupant_name_uuid()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_validate_occupant_name_empty()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_validate_occupant_name_none()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_validate_occupant_name_not_string()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_uuids_to_strings_dict()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_uuids_to_strings_list()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_uuids_to_strings_nested()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_uuids_to_strings_no_uuid()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- *... and 30 more nodes in this community*

## Relationships

- [Async Persistence Layer](Async_Persistence_Layer.md) (10 shared connections)
- [Plan Modernization Archive](Plan_Modernization_Archive.md) (7 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (5 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (4 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (2 shared connections)
- [Combat Command Helpers](Combat_Command_Helpers.md) (2 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (2 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (2 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`

## Audit Trail

- EXTRACTED: 180 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*