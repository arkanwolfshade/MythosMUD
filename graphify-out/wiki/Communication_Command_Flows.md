# Communication Command Flows

> 116 nodes · cohesion 0.04

## Key Concepts

- **test_communication_commands_flows.py** (40 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **SimpleNamespace** (38 connections) — `server/tests/fixtures/unit/__init__.py`
- **communication_commands_flows.py** (32 connections) — `server/commands/communication_commands_flows.py`
- **communication_commands.py** (27 connections) — `server/commands/communication_commands.py`
- **test_communication_commands_support.py** (20 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **ChatCommandsProtocol** (15 connections) — `server/commands/communication_commands_support.py`
- **_chat_send_with_room_bundle()** (14 connections) — `server/commands/communication_commands_flows.py`
- **communication_commands_support.py** (14 connections) — `server/commands/communication_commands_support.py`
- **flow_global_command()** (12 connections) — `server/commands/communication_commands_flows.py`
- **get_services_from_container()** (12 connections) — `server/commands/communication_commands_support.py`
- **PlayerResolutionProtocol** (12 connections) — `server/commands/communication_commands_flows.py`
- **_message_from_command()** (11 connections) — `server/commands/communication_commands_flows.py`
- **_RoomChannelOutcomeConfig** (11 connections) — `server/commands/communication_commands_flows.py`
- **chat_result_map()** (11 connections) — `server/commands/communication_commands_support.py`
- **message_id_from_result()** (11 connections) — `server/commands/communication_commands_support.py`
- **primary_id()** (11 connections) — `server/commands/communication_commands_support.py`
- **flow_reply_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- **flow_say_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- **_require_chat_pair()** (10 connections) — `server/commands/communication_commands_flows.py`
- **app_from_request()** (10 connections) — `server/commands/communication_commands_support.py`
- **PlayerResolutionProtocol** (10 connections) — `server/commands/communication_commands_support.py`
- **UserManagerProtocol** (10 connections) — `server/commands/communication_commands_support.py`
- **ChatCommandsProtocol** (9 connections) — `server/commands/communication_commands_flows.py`
- **flow_system_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- **flow_whisper_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- *... and 91 more nodes in this community*

## Relationships

- [[Communication Command Handlers]] (15 shared connections)
- [[Alias Expansion Logic]] (5 shared connections)
- [[Container Inventory Finders]] (5 shared connections)
- [[NPC Admin API]] (4 shared connections)
- [[Player Combat XP]] (4 shared connections)
- [[Container Inventory Ops]] (3 shared connections)
- [[Bench Cache Npc]] (3 shared connections)
- [[Whisper Reply Command Tests]] (2 shared connections)
- [[Commands Communication Support]] (2 shared connections)
- [[Command Request App State]] (2 shared connections)
- [[Database Manager Tests]] (1 shared connections)
- [[Cache and NPC Cache]] (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/commands/communication_commands_flows.py`
- `server/commands/communication_commands_support.py`
- `server/tests/fixtures/unit/__init__.py`
- `server/tests/unit/commands/test_communication_commands_flows.py`
- `server/tests/unit/commands/test_communication_commands_support.py`
- `server/tests/unit/commands/test_container_helpers_inventory_ops.py`

## Audit Trail

- EXTRACTED: 544 (86%)
- INFERRED: 88 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
