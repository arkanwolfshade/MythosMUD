# disconnect player connections()

> 107 nodes

## Key Concepts

- **test_logout_commands.py** (42 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **handle_logout_command()** (26 connections) — `server/commands/logout_commands.py`
- **logout_commands.py** (20 connections) — `server/commands/logout_commands.py`
- **test_logout_commands_helpers.py** (15 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **_get_player_position_from_connection_manager()** (14 connections) — `server/commands/logout_commands.py`
- **_get_player_for_logout()** (13 connections) — `server/commands/logout_commands.py`
- **_clear_corrupted_cache_entry()** (12 connections) — `server/commands/logout_commands.py`
- **_sync_player_position()** (12 connections) — `server/commands/logout_commands.py`
- **handle_quit_command()** (11 connections) — `server/commands/logout_commands.py`
- **Any** (8 connections)
- **_disconnect_player_connections()** (8 connections) — `server/commands/logout_commands.py`
- **_update_and_save_player_last_active()** (7 connections) — `server/commands/logout_commands.py`
- **test_clear_corrupted_cache_entry_with_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_clear_corrupted_cache_entry_no_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_clear_corrupted_cache_entry_no_request()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_persistence()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_corrupted_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_persistence_error()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_persistence_returns_coroutine()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_position_from_connection_manager_by_id()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_position_from_connection_manager_by_name()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_position_from_connection_manager_not_found()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_position_from_connection_manager_no_manager()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_sync_player_position_updates_stats()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- *... and 82 more nodes in this community*

## Relationships

- [test logout command](test_logout_command.md) (8 shared connections)
- [.add alias()](add_alias%28%29.md) (5 shared connections)
- [test magic commands](test_magic_commands.md) (3 shared connections)
- [Any](Any.md) (3 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [Player Position Service](Player_Position_Service.md) (2 shared connections)
- [. get persistence from app()](_get_persistence_from_app%28%29.md) (2 shared connections)
- [AuthSlice](AuthSlice.md) (1 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_commands.py`
- `server/tests/unit/commands/test_logout_commands_helpers.py`

## Audit Trail

- EXTRACTED: 351 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*