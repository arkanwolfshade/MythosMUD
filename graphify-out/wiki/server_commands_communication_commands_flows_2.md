# server commands communication commands flows

> 51 nodes

## Key Concepts

- **test_communication_commands_flows.py** (42 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **asyncio** (18 connections)
- **_chat_send_with_room_bundle()** (14 connections) — `server/commands/communication_commands_flows.py`
- **flow_global_command()** (12 connections) — `server/commands/communication_commands_flows.py`
- **flow_say_command()** (11 connections) — `server/commands/communication_commands_flows.py`
- **_message_from_command()** (11 connections) — `server/commands/communication_commands_flows.py`
- **flow_local_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_room_player_bundle()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_str_error_from_chat_result()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_RoomChannelOutcomeConfig** (8 connections) — `server/commands/communication_commands_flows.py`
- **_global_player_bundle()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_whisper_id_pair_or_error()** (8 connections) — `server/commands/communication_commands_flows.py`
- **test_chat_send_with_room_bundle_exception_returns_generic_message()** (5 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_chat_send_with_room_bundle_chat_failure()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_chat_send_with_room_bundle_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_global_command_blocks_low_level_user()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_reply_command_no_last_sender_returns_user_message()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_reply_command_success_uses_container_services()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_say_command_success_broadcasts_room_message()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_system_command_blocks_non_admin_user()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_whisper_command_exception_returns_generic_message()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_whisper_command_success_sends_private_message()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_global_player_bundle_level_too_low()** (3 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_global_player_bundle_non_int_level_coerced()** (3 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_global_player_bundle_success()** (3 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- *... and 26 more nodes in this community*

## Relationships

- [server commands communication commands flows](server_commands_communication_commands_flows.md) (43 shared connections)
- [server commands communication commands](server_commands_communication_commands.md) (4 shared connections)
- [server commands communication commands handle](server_commands_communication_commands_handle.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands_flows.py`
- `server/tests/unit/commands/test_communication_commands_flows.py`

## Audit Trail

- EXTRACTED: 146 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*