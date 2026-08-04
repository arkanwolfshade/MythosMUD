# models player related

> 53 nodes

## Key Concepts

- **player_service()** (23 connections) — `docs/examples/logging/fastapi_integration.py`
- **test_party_commands.py** (22 connections) — `server/tests/unit/commands/test_party_commands.py`
- **handle_party_command()** (21 connections) — `server/commands/party_commands.py`
- **party_commands.py** (20 connections) — `server/commands/party_commands.py`
- **_party_request()** (11 connections) — `server/tests/unit/commands/test_party_commands.py`
- **Any** (9 connections)
- **_handle_party_chat()** (8 connections) — `server/commands/party_commands.py`
- **_get_party_command_context()** (6 connections) — `server/commands/party_commands.py`
- **_handle_party_invite()** (6 connections) — `server/commands/party_commands.py`
- **_handle_party_kick()** (6 connections) — `server/commands/party_commands.py`
- **_get_member_display()** (6 connections) — `server/commands/party_commands.py`
- **_handle_party_leave()** (5 connections) — `server/commands/party_commands.py`
- **_handle_party_list()** (5 connections) — `server/commands/party_commands.py`
- **_get_container()** (4 connections) — `server/commands/party_commands.py`
- **test_handle_party_command_player_not_in_game()** (4 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_list_not_in_party()** (4 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_list_with_members()** (4 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_leave()** (4 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_invite_no_target()** (4 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_invite_success()** (4 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_kick_not_leader()** (4 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_unknown_subcommand()** (4 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_no_party_service()** (3 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_leave_not_in_party()** (3 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_chat_no_party()** (3 connections) — `server/tests/unit/commands/test_party_commands.py`
- *... and 28 more nodes in this community*

## Relationships

- [target resolution service](target_resolution_service.md) (6 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (5 shared connections)
- [commands whisper command](commands_whisper_command.md) (3 shared connections)
- [command commands aliases](command_commands_aliases.md) (2 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [world loader room](world_loader_room.md) (1 shared connections)
- [command commands handler](command_commands_handler.md) (1 shared connections)
- [combat npc services](combat_npc_services.md) (1 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)
- [container schemas containers](container_schemas_containers.md) (1 shared connections)
- [command models admin](command_models_admin.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/commands/party_commands.py`
- `server/tests/unit/commands/test_party_commands.py`

## Audit Trail

- EXTRACTED: 206 (91%)
- INFERRED: 20 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*