# Any

> 39 nodes

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
- **_get_player_service_from_app()** (5 connections) — `server/commands/admin_setlucidity_command.py`
- **_handle_party_chat()** (5 connections) — `server/commands/party_commands.py`
- **_handle_party_list()** (5 connections) — `server/commands/party_commands.py`
- **_get_container()** (4 connections) — `server/commands/party_commands.py`
- **_get_member_display()** (4 connections) — `server/commands/party_commands.py`
- **_handle_party_leave()** (3 connections) — `server/commands/party_commands.py`
- **test_handle_teach_command()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_target()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Any** (2 connections)
- **Simulate player service.** (1 connections) — `docs/examples/logging/fastapi_integration.py`
- **Get player service from container, fallback to app.state for backward compatibil** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Party commands for MythosMUD.  Handlers for party, party invite <name>, party le** (1 connections) — `server/commands/party_commands.py`
- **Get application container from request.** (1 connections) — `server/commands/party_commands.py`
- **Resolve container, party service, persistence, and current player for party comm** (1 connections) — `server/commands/party_commands.py`
- *... and 14 more nodes in this community*

## Relationships

- [Any](Any.md) (19 shared connections)
- [Player Position Service](Player_Position_Service.md) (7 shared connections)
- [fastapi integration](fastapi_integration.md) (6 shared connections)
- [main()](main%28%29.md) (4 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (2 shared connections)
- [websocket handler app state](websocket_handler_app_state.md) (2 shared connections)
- [admin setlucidity command](admin_setlucidity_command.md) (2 shared connections)
- [combat taunt](combat_taunt.md) (2 shared connections)
- [. get persistence from app()](_get_persistence_from_app%28%29.md) (2 shared connections)
- [admin setstat command](admin_setstat_command.md) (1 shared connections)
- [communication commands support](communication_commands_support.md) (1 shared connections)
- [follow commands](follow_commands.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/commands/admin_setlucidity_command.py`
- `server/commands/party_commands.py`
- `server/commands/teach_command.py`
- `server/tests/unit/commands/test_teach_command.py`

## Audit Trail

- EXTRACTED: 144 (85%)
- INFERRED: 26 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*