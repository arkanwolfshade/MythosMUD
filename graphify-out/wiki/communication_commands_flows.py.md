# communication_commands_flows.py

> 36 nodes

## Key Concepts

- **communication_commands_flows.py** (33 connections) — `server/commands/communication_commands_flows.py`
- **ChatCommandsProtocol** (18 connections) — `server/commands/communication_commands_support.py`
- **PlayerResolutionProtocol** (16 connections) — `server/commands/communication_commands_support.py`
- **_chat_send_with_room_bundle()** (14 connections) — `server/commands/communication_commands_flows.py`
- **_RoomChannelOutcomeConfig** (11 connections) — `server/commands/communication_commands_flows.py`
- **flow_say_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- **_require_chat_pair()** (10 connections) — `server/commands/communication_commands_flows.py`
- **flow_system_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- **flow_whisper_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_str_error_from_chat_result()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_system_send_if_admin()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_deliver_whisper_message()** (8 connections) — `server/commands/communication_commands_flows.py`
- **flow_local_command()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_system_services_triple()** (7 connections) — `server/commands/communication_commands_flows.py`
- **_player_id_bundle()** (6 connections) — `server/commands/communication_commands_flows.py`
- **test_chat_send_with_room_bundle_exception_returns_generic_message()** (6 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_chat_send_with_room_bundle_chat_failure()** (5 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_chat_send_with_room_bundle_success()** (5 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_str_error_from_chat_result_non_string_defaults()** (2 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_str_error_from_chat_result_string()** (2 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **UserManagerProtocol** (2 connections)
- **.get_last_whisper_sender()** (1 connections) — `server/commands/communication_commands_support.py`
- **.send_global_message()** (1 connections) — `server/commands/communication_commands_support.py`
- **.send_local_message()** (1 connections) — `server/commands/communication_commands_support.py`
- **.send_say_message()** (1 connections) — `server/commands/communication_commands_support.py`
- *... and 11 more nodes in this community*

## Relationships

- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (40 shared connections)
- [test_communication_commands_support.py](test_communication_commands_support.py.md) (29 shared connections)
- [AliasStorage](AliasStorage.md) (8 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [handle_whisper_command](handle_whisper_command.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands_flows.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_flows.py`

## Audit Trail

- EXTRACTED: 141 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*