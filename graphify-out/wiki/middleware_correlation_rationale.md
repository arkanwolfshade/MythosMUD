# middleware correlation rationale

> 98 nodes

## Key Concepts

- **fastapi_integration.py** (27 connections) — `docs/examples/logging/fastapi_integration.py`
- **player_service()** (23 connections) — `docs/examples/logging/fastapi_integration.py`
- **test_party_commands.py** (22 connections) — `server/tests/unit/commands/test_party_commands.py`
- **handle_party_command()** (21 connections) — `server/commands/party_commands.py`
- **party_commands.py** (20 connections) — `server/commands/party_commands.py`
- **_party_request()** (11 connections) — `server/tests/unit/commands/test_party_commands.py`
- **websocket_endpoint()** (9 connections) — `docs/examples/logging/fastapi_integration.py`
- **Any** (9 connections)
- **update_player_background_task()** (8 connections) — `docs/examples/logging/fastapi_integration.py`
- **_handle_party_chat()** (8 connections) — `server/commands/party_commands.py`
- **HTTPException** (6 connections)
- **upload_avatar()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **_get_party_command_context()** (6 connections) — `server/commands/party_commands.py`
- **_handle_party_invite()** (6 connections) — `server/commands/party_commands.py`
- **_handle_party_kick()** (6 connections) — `server/commands/party_commands.py`
- **_get_member_display()** (6 connections) — `server/commands/party_commands.py`
- **create_player()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **http_exception_handler()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **general_exception_handler()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **update_player_background()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **list_players()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **WebSocket** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **_handle_party_leave()** (5 connections) — `server/commands/party_commands.py`
- **_handle_party_list()** (5 connections) — `server/commands/party_commands.py`
- **Request** (4 connections)
- *... and 73 more nodes in this community*

## Relationships

- [app factory rationale](app_factory_rationale.md) (6 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (6 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (6 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (4 shared connections)
- [Exception Containers](Exception_Containers.md) (3 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [command commands handler](command_commands_handler.md) (2 shared connections)
- [command commands aliases](command_commands_aliases.md) (2 shared connections)
- [character creation service](character_creation_service.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/commands/party_commands.py`
- `server/tests/unit/commands/test_party_commands.py`

## Audit Trail

- EXTRACTED: 346 (93%)
- INFERRED: 26 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*