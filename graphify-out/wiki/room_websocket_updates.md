# room websocket updates

> 70 nodes

## Key Concepts

- **test_websocket_helpers.py** (41 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **check_shutdown_and_reject()** (12 connections) — `server/realtime/websocket_helpers.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **is_client_disconnected_exception()** (9 connections) — `server/realtime/websocket_helpers.py`
- **load_player_mute_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **_accumulate_valid_occupant_name()** (4 connections) — `server/realtime/websocket_helpers.py`
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
- *... and 45 more nodes in this community*

## Relationships

- [websocket helpers realtime](websocket_helpers_realtime.md) (11 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (11 shared connections)
- [room look commands](room_look_commands.md) (9 shared connections)
- [look helpers commands](look_helpers_commands.md) (8 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [realtime player connection](realtime_player_connection.md) (1 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)
- [models profession rationale](models_profession_rationale.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`

## Audit Trail

- EXTRACTED: 214 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*