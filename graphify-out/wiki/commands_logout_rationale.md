# commands logout rationale

> 107 nodes

## Key Concepts

- **test_logout_commands.py** (42 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **handle_logout_command()** (25 connections) — `server/commands/logout_commands.py`
- **logout_commands.py** (20 connections) — `server/commands/logout_commands.py`
- **test_logout_commands_helpers.py** (15 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **_get_player_position_from_connection_manager()** (14 connections) — `server/commands/logout_commands.py`
- **_get_player_for_logout()** (13 connections) — `server/commands/logout_commands.py`
- **_clear_corrupted_cache_entry()** (12 connections) — `server/commands/logout_commands.py`
- **_sync_player_position()** (12 connections) — `server/commands/logout_commands.py`
- **handle_quit_command()** (10 connections) — `server/commands/logout_commands.py`
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

- [logout command commands](logout_command_commands.md) (8 shared connections)
- [player cache rationale](player_cache_rationale.md) (5 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [commands who rationale](commands_who_rationale.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (2 shared connections)
- [commands position system](commands_position_system.md) (1 shared connections)
- [command factories create](command_factories_create.md) (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_commands.py`
- `server/tests/unit/commands/test_logout_commands_helpers.py`

## Audit Trail

- EXTRACTED: 351 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*