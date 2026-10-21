# BaseCommand

> 130 nodes · cohesion 0.04

## Key Concepts

- **test_communication_commands_flows.py** (49 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **communication_commands_flows.py** (39 connections) — `server/commands/communication_commands_flows.py`
- **communication_commands.py** (35 connections) — `server/commands/communication_commands.py`
- **SimpleNamespace** (24 connections)
- **asyncio** (22 connections)
- **test_communication_commands_support.py** (21 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **ChatCommandsProtocol** (19 connections) — `server/commands/communication_commands_support.py`
- **communication_commands_support.py** (16 connections) — `server/commands/communication_commands_support.py`
- **_chat_send_with_room_bundle()** (15 connections) — `server/commands/communication_commands_flows.py`
- **flow_global_command()** (15 connections) — `server/commands/communication_commands_flows.py`
- **PlayerResolutionProtocol** (15 connections) — `server/commands/communication_commands_support.py`
- **get_services_from_container()** (13 connections) — `server/commands/communication_commands_support.py`
- **primary_id()** (13 connections) — `server/commands/communication_commands_support.py`
- **flow_say_command()** (12 connections) — `server/commands/communication_commands_flows.py`
- **_message_from_command()** (12 connections) — `server/commands/communication_commands_flows.py`
- **_system_send_if_admin()** (12 connections) — `server/commands/communication_commands_flows.py`
- **app_from_request()** (12 connections) — `server/commands/communication_commands_support.py`
- **get_pose_persistence()** (12 connections) — `server/commands/communication_commands_support.py`
- **flow_local_command()** (11 connections) — `server/commands/communication_commands_flows.py`
- **flow_reply_command()** (11 connections) — `server/commands/communication_commands_flows.py`
- **flow_system_command()** (11 connections) — `server/commands/communication_commands_flows.py`
- **chat_result_map()** (11 connections) — `server/commands/communication_commands_support.py`
- **message_id_from_result()** (11 connections) — `server/commands/communication_commands_support.py`
- **_deliver_reply_to_last_whisper()** (10 connections) — `server/commands/communication_commands_flows.py`
- **_deliver_whisper_message()** (10 connections) — `server/commands/communication_commands_flows.py`
- *... and 105 more nodes in this community*

## Relationships

- [PlayerStateCommandFactory](PlayerStateCommandFactory.md) (21 shared connections)
- [look_container.py](look_container.py.md) (20 shared connections)
- [command_parser.py](command_parser.py.md) (17 shared connections)
- [Persistence Layer Refactoring - COMPLETE ✅](Persistence_Layer_Refactoring_-_COMPLETE_✅.md) (7 shared connections)
- [Room](Room.md) (4 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (2 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)
- [test_lint_optional_auth_no_guard.py](test_lint_optional_auth_no_guard.py.md) (1 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (1 shared connections)
- [inventory_item_matching.py](inventory_item_matching.py.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/commands/communication_commands_flows.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_flows.py`
- `server/tests/unit/commands/test_communication_commands_support.py`

## Audit Trail

- EXTRACTED: 379 (91%)
- INFERRED: 38 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*