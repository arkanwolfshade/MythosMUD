# room websocket updates

> 66 nodes

## Key Concepts

- **test_websocket_helpers.py** (41 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **check_shutdown_and_reject()** (12 connections) — `server/realtime/websocket_helpers.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **is_client_disconnected_exception()** (9 connections) — `server/realtime/websocket_helpers.py`
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
- *... and 41 more nodes in this community*

## Relationships

- [realtime websocket initial](realtime_websocket_initial.md) (13 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (9 shared connections)
- [command models moderation](command_models_moderation.md) (8 shared connections)
- [command commands aliases](command_commands_aliases.md) (7 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (6 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`

## Audit Trail

- EXTRACTED: 195 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*