# commands communication flows

> 90 nodes

## Key Concepts

- **test_communication_commands_flows.py** (41 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **SimpleNamespace** (38 connections)
- **communication_commands_flows.py** (33 connections) — `server/commands/communication_commands_flows.py`
- **ChatCommandsProtocol** (18 connections) — `server/commands/communication_commands_support.py`
- **PlayerResolutionProtocol** (16 connections) — `server/commands/communication_commands_support.py`
- **get_services_from_container()** (15 connections) — `server/commands/communication_commands_support.py`
- **_chat_send_with_room_bundle()** (14 connections) — `server/commands/communication_commands_flows.py`
- **primary_id()** (13 connections) — `server/commands/communication_commands_support.py`
- **flow_global_command()** (12 connections) — `server/commands/communication_commands_flows.py`
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
- **flow_local_command()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_whisper_id_pair_or_error()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_deliver_whisper_message()** (8 connections) — `server/commands/communication_commands_flows.py`
- *... and 65 more nodes in this community*

## Relationships

- [commands communication say](commands_communication_say.md) (38 shared connections)
- [commands communication channels](commands_communication_channels.md) (3 shared connections)
- [cache caching service](cache_caching_service.md) (3 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (3 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [commands whisper command](commands_whisper_command.md) (2 shared connections)
- [dialogue service game](dialogue_service_game.md) (2 shared connections)
- [command validation commands](command_validation_commands.md) (2 shared connections)
- [combat npc services](combat_npc_services.md) (2 shared connections)
- [container inventory helpers](container_inventory_helpers.md) (2 shared connections)
- [admin shutdown commands](admin_shutdown_commands.md) (1 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands_flows.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_flows.py`
- `server/tests/unit/commands/test_communication_commands_support.py`

## Audit Trail

- EXTRACTED: 436 (87%)
- INFERRED: 67 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*