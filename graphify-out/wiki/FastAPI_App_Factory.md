# FastAPI App Factory

> 80 nodes

## Key Concepts

- **test_communication_commands_flows.py** (41 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **SimpleNamespace** (38 connections)
- **communication_commands_flows.py** (33 connections) — `server/commands/communication_commands_flows.py`
- **ChatCommandsProtocol** (18 connections) — `server/commands/communication_commands_support.py`
- **PlayerResolutionProtocol** (16 connections) — `server/commands/communication_commands_support.py`
- **_chat_send_with_room_bundle()** (14 connections) — `server/commands/communication_commands_flows.py`
- **flow_global_command()** (12 connections) — `server/commands/communication_commands_flows.py`
- **_message_from_command()** (11 connections) — `server/commands/communication_commands_flows.py`
- **_RoomChannelOutcomeConfig** (11 connections) — `server/commands/communication_commands_flows.py`
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
- **_deliver_reply_to_last_whisper()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_system_services_triple()** (7 connections) — `server/commands/communication_commands_flows.py`
- **_player_id_bundle()** (6 connections) — `server/commands/communication_commands_flows.py`
- *... and 55 more nodes in this community*

## Relationships

- [Quest Journal Commands](Quest_Journal_Commands.md) (36 shared connections)
- [Client Event Store](Client_Event_Store.md) (12 shared connections)
- [Container Inventory Finders](Container_Inventory_Finders.md) (6 shared connections)
- [Grace Period Blocking Tests](Grace_Period_Blocking_Tests.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)
- [Container Inventory Ops](Container_Inventory_Ops.md) (2 shared connections)
- [Deprecated Logging Patterns](Deprecated_Logging_Patterns.md) (1 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (1 shared connections)
- [Message Broker Errors](Message_Broker_Errors.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands_flows.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_flows.py`
- `server/tests/unit/commands/test_container_helpers_inventory_find.py`

## Audit Trail

- EXTRACTED: 386 (86%)
- INFERRED: 62 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*