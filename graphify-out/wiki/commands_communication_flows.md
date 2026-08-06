# commands communication flows

> 116 nodes

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
- **get_pose_persistence()** (11 connections) — `server/commands/communication_commands_support.py`
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
- *... and 91 more nodes in this community*

## Relationships

- [commands whisper command](commands_whisper_command.md) (17 shared connections)
- [dialogue service game](dialogue_service_game.md) (7 shared connections)
- [realtime real time](realtime_real_time.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (3 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (2 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)
- [models player related](models_player_related.md) (1 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/commands/communication_commands_flows.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_flows.py`
- `server/tests/unit/commands/test_communication_commands_support.py`

## Audit Trail

- EXTRACTED: 569 (98%)
- INFERRED: 12 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*