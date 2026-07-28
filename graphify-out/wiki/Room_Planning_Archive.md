# Room Planning Archive

> 37 nodes · cohesion 0.09

## Key Concepts

- **player_service()** (23 connections) — `docs/examples/logging/fastapi_integration.py`
- **party_commands.py** (19 connections) — `server/commands/party_commands.py`
- **teach_command.py** (14 connections) — `server/commands/teach_command.py`
- **handle_teach_command()** (13 connections) — `server/commands/teach_command.py`
- **handle_party_command()** (12 connections) — `server/commands/party_commands.py`
- **Any** (9 connections)
- **_get_party_command_context()** (6 connections) — `server/commands/party_commands.py`
- **_handle_party_invite()** (6 connections) — `server/commands/party_commands.py`
- **_handle_party_kick()** (6 connections) — `server/commands/party_commands.py`
- **test_teach_command.py** (6 connections) — `server/tests/unit/commands/test_teach_command.py`
- **_handle_party_chat()** (5 connections) — `server/commands/party_commands.py`
- **_handle_party_list()** (5 connections) — `server/commands/party_commands.py`
- **_get_container()** (4 connections) — `server/commands/party_commands.py`
- **_get_member_display()** (4 connections) — `server/commands/party_commands.py`
- **_handle_party_leave()** (3 connections) — `server/commands/party_commands.py`
- **test_handle_teach_command()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_target()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Any** (2 connections)
- **Simulate player service.** (1 connections) — `docs/examples/logging/fastapi_integration.py`
- **Party commands for MythosMUD.  Handlers for party, party invite <name>, party le** (1 connections) — `server/commands/party_commands.py`
- **Handle party [invite|leave|kick|list]. No subcommand = party status/list.** (1 connections) — `server/commands/party_commands.py`
- **Handle party invite <name> logic. Uses confirmation pattern: target must accept.** (1 connections) — `server/commands/party_commands.py`
- **Handle party kick <name> logic.** (1 connections) — `server/commands/party_commands.py`
- **Get application container from request.** (1 connections) — `server/commands/party_commands.py`
- *... and 12 more nodes in this community*

## Relationships

- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (15 shared connections)
- [Flee Command Tests](Flee_Command_Tests.md) (7 shared connections)
- [FastAPI Auth Integration](FastAPI_Auth_Integration.md) (5 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (3 shared connections)
- [Command Request App State](Command_Request_App_State.md) (2 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (2 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (2 shared connections)
- [Development Setup Guide](Development_Setup_Guide.md) (1 shared connections)
- [Combat Monitoring Service](Combat_Monitoring_Service.md) (1 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/commands/party_commands.py`
- `server/commands/teach_command.py`
- `server/tests/unit/commands/test_teach_command.py`

## Audit Trail

- EXTRACTED: 139 (85%)
- INFERRED: 25 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*