# Communication Command Flows

> 241 nodes · cohesion 0.02

## Key Concepts

- **test_communication_commands_flows.py** (41 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **SimpleNamespace** (38 connections)
- **communication_commands_flows.py** (33 connections) — `server/commands/communication_commands_flows.py`
- **communication_commands.py** (31 connections) — `server/commands/communication_commands.py`
- **request_with_app_container()** (28 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_communication_commands_say_me_pose.py** (22 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **handle_whisper_command()** (21 connections) — `server/commands/communication_commands.py`
- **test_communication_commands_support.py** (21 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_communication_commands_channels.py** (20 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **ChatCommandsProtocol** (18 connections) — `server/commands/communication_commands_support.py`
- **handle_say_command()** (17 connections) — `server/commands/communication_commands.py`
- **test_communication_commands_whisper_reply.py** (17 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **PlayerResolutionProtocol** (16 connections) — `server/commands/communication_commands_support.py`
- **communication_commands_support.py** (15 connections) — `server/commands/communication_commands_support.py`
- **get_services_from_container()** (15 connections) — `server/commands/communication_commands_support.py`
- **_chat_send_with_room_bundle()** (14 connections) — `server/commands/communication_commands_flows.py`
- **handle_pose_command()** (14 connections) — `server/commands/communication_commands.py`
- **test_whisper_command.py** (13 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **flow_global_command()** (12 connections) — `server/commands/communication_commands_flows.py`
- **handle_global_command()** (12 connections) — `server/commands/communication_commands.py`
- **_message_from_command()** (11 connections) — `server/commands/communication_commands_flows.py`
- **_RoomChannelOutcomeConfig** (11 connections) — `server/commands/communication_commands_flows.py`
- **handle_local_command()** (11 connections) — `server/commands/communication_commands.py`
- **handle_reply_command()** (11 connections) — `server/commands/communication_commands.py`
- **handle_system_command()** (11 connections) — `server/commands/communication_commands.py`
- *... and 216 more nodes in this community*

## Relationships

- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (32 shared connections)
- [Container Inventory Finders](Container_Inventory_Finders.md) (5 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (4 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (2 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (2 shared connections)
- [WebSocket Request Context](WebSocket_Request_Context.md) (2 shared connections)
- [Container Inventory Ops](Container_Inventory_Ops.md) (2 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (1 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (1 shared connections)
- [Room Planning Archive](Room_Planning_Archive.md) (1 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/commands/communication_commands_flows.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/communication_commands_mocks.py`
- `server/tests/unit/commands/test_communication_commands_channels.py`
- `server/tests/unit/commands/test_communication_commands_flows.py`
- `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- `server/tests/unit/commands/test_communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- `server/tests/unit/commands/test_whisper_command.py`

## Audit Trail

- EXTRACTED: 986 (92%)
- INFERRED: 84 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*