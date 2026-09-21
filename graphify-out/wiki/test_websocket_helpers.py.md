# test_websocket_helpers.py

> 78 nodes

## Key Concepts

- **test_websocket_helpers.py** (41 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **check_shutdown_and_reject()** (12 connections) — `server/realtime/websocket_helpers.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **is_websocket_disconnect_message()** (11 connections) — `server/realtime/websocket_helpers.py`
- **asyncio** (9 connections)
- **handle_websocket_runtime_error()** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **convert_schema_to_dict()** (7 connections) — `server/realtime/websocket_helpers.py`
- **.model_dump()** (4 connections) — `server/models/alias.py`
- **_accumulate_valid_occupant_name()** (4 connections) — `server/realtime/websocket_helpers.py`
- **test_check_shutdown_and_reject_not_shutting_down()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_check_shutdown_and_reject_shutting_down()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_check_shutdown_and_reject_websocket_disconnect()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_empty()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_filters_uuid()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_none()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_load_player_mute_data_import_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_load_player_mute_data_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_schema_to_dict_with_dict()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_schema_to_dict_with_model_dump()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_uuids_to_strings_dict()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_uuids_to_strings_list()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_uuids_to_strings_nested()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- *... and 53 more nodes in this community*

## Relationships

- [websocket_handler.py](websocket_handler.py.md) (15 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (10 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (8 shared connections)
- [websocket_room_updates.py](websocket_room_updates.py.md) (7 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (2 shared connections)
- [player_event_handlers_respawn_room.py](player_event_handlers_respawn_room.py.md) (2 shared connections)
- [Alias](Alias.md) (1 shared connections)
- [is_shutdown_pending](is_shutdown_pending.md) (1 shared connections)
- [get_shutdown_blocking_message](get_shutdown_blocking_message.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/models/alias.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`

## Audit Trail

- EXTRACTED: 151 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*