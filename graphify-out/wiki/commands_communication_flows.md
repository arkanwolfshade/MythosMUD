# commands communication flows

> 130 nodes

## Key Concepts

- **test_communication_commands_flows.py** (41 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **communication_commands_flows.py** (33 connections) — `server/commands/communication_commands_flows.py`
- **talk_command.py** (27 connections) — `server/commands/talk_command.py`
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
- **get_pose_persistence()** (11 connections) — `server/commands/communication_commands_support.py`
- **chat_result_map()** (11 connections) — `server/commands/communication_commands_support.py`
- **message_id_from_result()** (11 connections) — `server/commands/communication_commands_support.py`
- **handle_talk_command()** (11 connections) — `server/commands/talk_command.py`
- **_require_chat_pair()** (10 connections) — `server/commands/communication_commands_flows.py`
- **flow_say_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- **flow_reply_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- **_str_error_from_chat_result()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_room_player_bundle()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_system_send_if_admin()** (9 connections) — `server/commands/communication_commands_flows.py`
- **flow_system_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- *... and 105 more nodes in this community*

## Relationships

- [commands whisper command](commands_whisper_command.md) (17 shared connections)
- [dialogue service game](dialogue_service_game.md) (8 shared connections)
- [commands position system](commands_position_system.md) (5 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (5 shared connections)
- [models npc rationale](models_npc_rationale.md) (4 shared connections)
- [quest chat game](quest_chat_game.md) (3 shared connections)
- [inventory commands command](inventory_commands_command.md) (2 shared connections)
- [command utility models](command_utility_models.md) (2 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)
- [services service hallucination](services_service_hallucination.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands_flows.py`
- `server/commands/communication_commands_support.py`
- `server/commands/talk_command.py`
- `server/tests/unit/commands/test_communication_commands_flows.py`
- `server/tests/unit/commands/test_communication_commands_support.py`

## Audit Trail

- EXTRACTED: 617 (97%)
- INFERRED: 16 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*