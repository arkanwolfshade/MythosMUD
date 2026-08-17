# server commands party commands

> 52 nodes

## Key Concepts

- **test_party_commands.py** (23 connections) — `server/tests/unit/commands/test_party_commands.py`
- **handle_party_command()** (21 connections) — `server/commands/party_commands.py`
- **party_commands.py** (21 connections) — `server/commands/party_commands.py`
- **asyncio** (13 connections)
- **_party_request()** (11 connections) — `server/tests/unit/commands/test_party_commands.py`
- **Any** (9 connections)
- **_handle_party_chat()** (7 connections) — `server/commands/party_commands.py`
- **_get_member_display()** (6 connections) — `server/commands/party_commands.py`
- **_get_party_command_context()** (6 connections) — `server/commands/party_commands.py`
- **_get_container()** (5 connections) — `server/commands/party_commands.py`
- **_handle_party_invite()** (5 connections) — `server/commands/party_commands.py`
- **_handle_party_kick()** (5 connections) — `server/commands/party_commands.py`
- **_handle_party_leave()** (5 connections) — `server/commands/party_commands.py`
- **_handle_party_list()** (5 connections) — `server/commands/party_commands.py`
- **test_handle_party_command_invite_no_target()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_invite_success()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_kick_not_leader()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_leave()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_list_not_in_party()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_list_with_members()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_player_not_in_game()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_unknown_subcommand()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_get_member_display_invalid_uuid()** (4 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_chat_no_party()** (4 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_chat_success()** (4 connections) — `server/tests/unit/commands/test_party_commands.py`
- *... and 27 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (3 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (3 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (2 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (1 shared connections)
- [aliasrecord](aliasrecord.md) (1 shared connections)
- [server persistence repositories player repository](server_persistence_repositories_player_repository.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/commands/party_commands.py`
- `server/tests/unit/commands/test_party_commands.py`

## Audit Trail

- EXTRACTED: 120 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*