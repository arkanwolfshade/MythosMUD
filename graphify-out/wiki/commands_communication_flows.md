# commands communication flows

> 152 nodes

## Key Concepts

- **test_communication_commands_flows.py** (41 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **communication_commands_flows.py** (33 connections) — `server/commands/communication_commands_flows.py`
- **communication_commands.py** (31 connections) — `server/commands/communication_commands.py`
- **test_communication_commands_support.py** (21 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_communication_commands_channels.py** (20 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **ChatCommandsProtocol** (18 connections) — `server/commands/communication_commands_support.py`
- **communication_commands_support.py** (16 connections) — `server/commands/communication_commands_support.py`
- **PlayerResolutionProtocol** (16 connections) — `server/commands/communication_commands_support.py`
- **get_services_from_container()** (15 connections) — `server/commands/communication_commands_support.py`
- **_chat_send_with_room_bundle()** (14 connections) — `server/commands/communication_commands_flows.py`
- **handle_pose_command()** (13 connections) — `server/commands/communication_commands.py`
- **primary_id()** (13 connections) — `server/commands/communication_commands_support.py`
- **flow_global_command()** (12 connections) — `server/commands/communication_commands_flows.py`
- **app_from_request()** (12 connections) — `server/commands/communication_commands_support.py`
- **handle_global_command()** (11 connections) — `server/commands/communication_commands.py`
- **_message_from_command()** (11 connections) — `server/commands/communication_commands_flows.py`
- **_RoomChannelOutcomeConfig** (11 connections) — `server/commands/communication_commands_flows.py`
- **get_pose_persistence()** (11 connections) — `server/commands/communication_commands_support.py`
- **chat_result_map()** (11 connections) — `server/commands/communication_commands_support.py`
- **message_id_from_result()** (11 connections) — `server/commands/communication_commands_support.py`
- **handle_local_command()** (10 connections) — `server/commands/communication_commands.py`
- **handle_system_command()** (10 connections) — `server/commands/communication_commands.py`
- **_require_chat_pair()** (10 connections) — `server/commands/communication_commands_flows.py`
- **flow_say_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- **flow_reply_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- *... and 127 more nodes in this community*

## Relationships

- [commands whisper command](commands_whisper_command.md) (32 shared connections)
- [dialogue service game](dialogue_service_game.md) (7 shared connections)
- [commands npc admin](commands_npc_admin.md) (5 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [commands inventory command](commands_inventory_command.md) (2 shared connections)
- [commands emote rationale](commands_emote_rationale.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)
- [models player related](models_player_related.md) (1 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/commands/communication_commands_flows.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_channels.py`
- `server/tests/unit/commands/test_communication_commands_flows.py`
- `server/tests/unit/commands/test_communication_commands_support.py`

## Audit Trail

- EXTRACTED: 696 (98%)
- INFERRED: 13 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*