# Party Service Management

> 63 nodes

## Key Concepts

- **test_websocket_helpers.py** (36 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
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
- **test_get_occupant_names_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_filters_uuid()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_empty()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_none()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_uuids_to_strings_dict()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- *... and 38 more nodes in this community*

## Relationships

- [Combat Domain Events](Combat_Domain_Events.md) (13 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (9 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (5 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (4 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (2 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`

## Audit Trail

- EXTRACTED: 188 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*