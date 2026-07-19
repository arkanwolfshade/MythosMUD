# WebSocket Helper Utilities

> 55 nodes · cohesion 0.05

## Key Concepts

- **test_websocket_helpers.py** (33 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **validate_occupant_name()** (13 connections) — `server/realtime/websocket_helpers.py`
- **get_npc_name_from_instance()** (12 connections) — `server/realtime/websocket_helpers.py`
- **load_player_mute_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **Test validate_occupant_name() returns False for UUID string.** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_npc_name_from_instance_runtime_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **_accumulate_valid_occupant_name()** (4 connections) — `server/realtime/websocket_helpers.py`
- **test_check_shutdown_and_reject_not_shutting_down()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_check_shutdown_and_reject_shutting_down()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_check_shutdown_and_reject_websocket_disconnect()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_schema_to_dict_with_dict()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_schema_to_dict_with_model_dump()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_uuids_to_strings_dict()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_uuids_to_strings_list()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_uuids_to_strings_nested()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_uuids_to_strings_no_uuid()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_npc_name_from_instance_import_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_npc_name_from_instance_no_name_attribute()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_npc_name_from_instance_not_found()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_npc_name_from_instance_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_empty()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_filters_uuid()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_none()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_load_player_mute_data_import_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- *... and 30 more nodes in this community*

## Relationships

- [[WebSocket Initial State]] (14 shared connections)
- [[WebSocket Player Helpers]] (11 shared connections)
- [[Look Command Helpers]] (3 shared connections)
- [[Realtime Connection Impl]] (1 shared connections)
- [[Database Manager Tests]] (1 shared connections)
- [[NPC Occupant Verification]] (1 shared connections)
- [[WebSocket Message Validation]] (1 shared connections)
- [[Realtime WebSocket Auth]] (1 shared connections)
- [[Player Respawn Events]] (1 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`

## Audit Trail

- EXTRACTED: 173 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
