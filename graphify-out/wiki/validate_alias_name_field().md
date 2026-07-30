# .validate alias name field()

> 31 nodes

## Key Concepts

- **communication_commands_flows.py** (33 connections) — `server/commands/communication_commands_flows.py`
- **ChatCommandsProtocol** (18 connections) — `server/commands/communication_commands_support.py`
- **PlayerResolutionProtocol** (16 connections) — `server/commands/communication_commands_support.py`
- **flow_global_command()** (12 connections) — `server/commands/communication_commands_flows.py`
- **chat_result_map()** (11 connections) — `server/commands/communication_commands_support.py`
- **message_id_from_result()** (11 connections) — `server/commands/communication_commands_support.py`
- **_require_chat_pair()** (10 connections) — `server/commands/communication_commands_flows.py`
- **flow_reply_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- **_str_error_from_chat_result()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_system_send_if_admin()** (9 connections) — `server/commands/communication_commands_flows.py`
- **flow_whisper_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_deliver_whisper_message()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_deliver_reply_to_last_whisper()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_system_services_triple()** (7 connections) — `server/commands/communication_commands_flows.py`
- **_player_id_bundle()** (6 connections) — `server/commands/communication_commands_flows.py`
- **UserManagerProtocol** (2 connections)
- **Room/global/system/whisper/reply flows for communication command handlers.  Ex** (1 connections) — `server/commands/communication_commands_flows.py`
- **Handle the `global` command: server-wide chat when permitted.** (1 connections) — `server/commands/communication_commands_flows.py`
- **Handle `whisper`: send a private message to a named online player.** (1 connections) — `server/commands/communication_commands_flows.py`
- **Handle `reply`: whisper back to the last player who whispered to you.** (1 connections) — `server/commands/communication_commands_flows.py`
- **.resolve_player_name()** (1 connections) — `server/commands/communication_commands_support.py`
- **.send_say_message()** (1 connections) — `server/commands/communication_commands_support.py`
- **.send_local_message()** (1 connections) — `server/commands/communication_commands_support.py`
- **.send_global_message()** (1 connections) — `server/commands/communication_commands_support.py`
- **.send_system_message()** (1 connections) — `server/commands/communication_commands_support.py`
- *... and 6 more nodes in this community*

## Relationships

- [chat send with room bundle()](chat_send_with_room_bundle%28%29.md) (40 shared connections)
- [ConnectionsComponent](ConnectionsComponent.md) (25 shared connections)
- [.get instance()](get_instance%28%29.md) (4 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [handle global command()](handle_global_command%28%29.md) (2 shared connections)
- [test quest service collect](test_quest_service_collect.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands_flows.py`
- `server/commands/communication_commands_support.py`

## Audit Trail

- EXTRACTED: 192 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*