# server commands logout commands

> 65 nodes

## Key Concepts

- **test_logout_commands.py** (43 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **logout_commands.py** (26 connections) — `server/commands/logout_commands.py`
- **handle_logout_command()** (24 connections) — `server/commands/logout_commands.py`
- **asyncio** (18 connections)
- **_get_player_for_logout()** (13 connections) — `server/commands/logout_commands.py`
- **handle_quit_command()** (13 connections) — `server/commands/logout_commands.py`
- **Any** (13 connections)
- **_clear_corrupted_cache_entry()** (12 connections) — `server/commands/logout_commands.py`
- **_disconnect_player_connections()** (9 connections) — `server/commands/logout_commands.py`
- **_prepare_player_for_logout()** (7 connections) — `server/commands/logout_commands.py`
- **_update_and_save_player_last_active()** (7 connections) — `server/commands/logout_commands.py`
- **_force_disconnect_player()** (4 connections) — `server/commands/logout_commands.py`
- **_get_app_services()** (4 connections) — `server/commands/logout_commands.py`
- **_resolve_disconnect_player_id()** (4 connections) — `server/commands/logout_commands.py`
- **test_disconnect_player_connections_error()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_no_manager()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_success()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_corrupted_cache()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_cache()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_persistence_error()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_persistence_returns_coroutine()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_error_handling()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_no_player()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- *... and 40 more nodes in this community*

## Relationships

- [server commands logout commands get](server_commands_logout_commands_get.md) (20 shared connections)
- [server tests unit commands test](server_tests_unit_commands_test.md) (12 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (5 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (4 shared connections)
- [server commands utility commands](server_commands_utility_commands.md) (3 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [aliasrecord](aliasrecord.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_commands.py`

## Audit Trail

- EXTRACTED: 170 (93%)
- INFERRED: 12 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*