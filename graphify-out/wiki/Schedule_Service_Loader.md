# Schedule Service Loader

> 51 nodes

## Key Concepts

- **test_communication_commands_flows.py** (41 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **SimpleNamespace** (38 connections)
- **_chat_send_with_room_bundle()** (14 connections) — `server/commands/communication_commands_flows.py`
- **flow_global_command()** (12 connections) — `server/commands/communication_commands_flows.py`
- **_message_from_command()** (11 connections) — `server/commands/communication_commands_flows.py`
- **_RoomChannelOutcomeConfig** (11 connections) — `server/commands/communication_commands_flows.py`
- **flow_say_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- **_str_error_from_chat_result()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_room_player_bundle()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_global_player_bundle()** (8 connections) — `server/commands/communication_commands_flows.py`
- **flow_local_command()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_whisper_id_pair_or_error()** (8 connections) — `server/commands/communication_commands_flows.py`
- **test_chat_send_with_room_bundle_exception_returns_generic_message()** (5 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_chat_send_with_room_bundle_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_chat_send_with_room_bundle_chat_failure()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_say_command_success_broadcasts_room_message()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_whisper_command_exception_returns_generic_message()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_whisper_command_success_sends_private_message()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_reply_command_success_uses_container_services()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_reply_command_no_last_sender_returns_user_message()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_global_command_blocks_low_level_user()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_system_command_blocks_non_admin_user()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_whisper_id_pair_self_whisper()** (3 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_whisper_id_pair_missing_id()** (3 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_whisper_id_pair_ok()** (3 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- *... and 26 more nodes in this community*

## Relationships

- [Quest Journal Commands](Quest_Journal_Commands.md) (49 shared connections)
- [Container Inventory Finders](Container_Inventory_Finders.md) (5 shared connections)
- [Container Open Events](Container_Open_Events.md) (4 shared connections)
- [Alias Command Models](Alias_Command_Models.md) (3 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (2 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (2 shared connections)
- [Container Inventory Ops](Container_Inventory_Ops.md) (2 shared connections)
- [Structured Concurrency Patterns](Structured_Concurrency_Patterns.md) (1 shared connections)
- [Message Broker Errors](Message_Broker_Errors.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands_flows.py`
- `server/tests/unit/commands/test_communication_commands_flows.py`

## Audit Trail

- EXTRACTED: 216 (79%)
- INFERRED: 59 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*