# commands communication flows

> 108 nodes

## Key Concepts

- **test_communication_commands_flows.py** (41 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **communication_commands_flows.py** (33 connections) — `server/commands/communication_commands_flows.py`
- **communication_commands.py** (31 connections) — `server/commands/communication_commands.py`
- **test_communication_commands_support.py** (21 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **ChatCommandsProtocol** (18 connections) — `server/commands/communication_commands_support.py`
- **communication_commands_support.py** (16 connections) — `server/commands/communication_commands_support.py`
- **PlayerResolutionProtocol** (16 connections) — `server/commands/communication_commands_support.py`
- **get_services_from_container()** (15 connections) — `server/commands/communication_commands_support.py`
- **_chat_send_with_room_bundle()** (14 connections) — `server/commands/communication_commands_flows.py`
- **primary_id()** (13 connections) — `server/commands/communication_commands_support.py`
- **flow_global_command()** (12 connections) — `server/commands/communication_commands_flows.py`
- **app_from_request()** (12 connections) — `server/commands/communication_commands_support.py`
- **_message_from_command()** (11 connections) — `server/commands/communication_commands_flows.py`
- **_RoomChannelOutcomeConfig** (11 connections) — `server/commands/communication_commands_flows.py`
- **chat_result_map()** (11 connections) — `server/commands/communication_commands_support.py`
- **message_id_from_result()** (11 connections) — `server/commands/communication_commands_support.py`
- **_require_chat_pair()** (10 connections) — `server/commands/communication_commands_flows.py`
- **flow_say_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- **flow_reply_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- **_str_error_from_chat_result()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_room_player_bundle()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_system_send_if_admin()** (9 connections) — `server/commands/communication_commands_flows.py`
- **flow_system_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- **flow_whisper_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_global_player_bundle()** (8 connections) — `server/commands/communication_commands_flows.py`
- *... and 83 more nodes in this community*

## Relationships

- [character creation service](character_creation_service.md) (8 shared connections)
- [message broadcast realtime](message_broadcast_realtime.md) (7 shared connections)
- [npc combat service](npc_combat_service.md) (7 shared connections)
- [commands whisper command](commands_whisper_command.md) (6 shared connections)
- [occupants npc commands](occupants_npc_commands.md) (5 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (4 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (1 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/commands/communication_commands_flows.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_flows.py`
- `server/tests/unit/commands/test_communication_commands_support.py`

## Audit Trail

- EXTRACTED: 545 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*