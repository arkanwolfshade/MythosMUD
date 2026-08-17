# server commands communication commands flows

> 63 nodes

## Key Concepts

- **communication_commands_flows.py** (33 connections) — `server/commands/communication_commands_flows.py`
- **test_communication_commands_support.py** (22 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **ChatCommandsProtocol** (19 connections) — `server/commands/communication_commands_support.py`
- **communication_commands_support.py** (16 connections) — `server/commands/communication_commands_support.py`
- **PlayerResolutionProtocol** (15 connections) — `server/commands/communication_commands_support.py`
- **app_from_request()** (13 connections) — `server/commands/communication_commands_support.py`
- **get_services_from_container()** (13 connections) — `server/commands/communication_commands_support.py`
- **primary_id()** (13 connections) — `server/commands/communication_commands_support.py`
- **chat_result_map()** (11 connections) — `server/commands/communication_commands_support.py`
- **get_pose_persistence()** (11 connections) — `server/commands/communication_commands_support.py`
- **message_id_from_result()** (11 connections) — `server/commands/communication_commands_support.py`
- **flow_reply_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- **_require_chat_pair()** (10 connections) — `server/commands/communication_commands_flows.py`
- **_system_send_if_admin()** (10 connections) — `server/commands/communication_commands_flows.py`
- **flow_system_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- **flow_whisper_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- **UserManagerProtocol** (8 connections) — `server/commands/communication_commands_support.py`
- **_deliver_reply_to_last_whisper()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_deliver_whisper_message()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_system_services_triple()** (8 connections) — `server/commands/communication_commands_flows.py`
- **AsyncPersistenceForPose** (6 connections) — `server/commands/communication_commands_support.py`
- **_player_id_bundle()** (6 connections) — `server/commands/communication_commands_flows.py`
- **Protocol** (5 connections)
- **test_app_from_request_with_app()** (3 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_message_id_from_result_no_id()** (3 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- *... and 38 more nodes in this community*

## Relationships

- [server commands communication commands flows](server_commands_communication_commands_flows.md) (43 shared connections)
- [server commands communication commands](server_commands_communication_commands.md) (11 shared connections)
- [server commands quest commands npc](server_commands_quest_commands_npc.md) (7 shared connections)
- [server commands communication commands handle](server_commands_communication_commands_handle.md) (3 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server commands admin shutdown command](server_commands_admin_shutdown_command.md) (1 shared connections)
- [aliasrecord](aliasrecord.md) (1 shared connections)
- [object](object.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands_flows.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_support.py`

## Audit Trail

- EXTRACTED: 178 (88%)
- INFERRED: 24 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*