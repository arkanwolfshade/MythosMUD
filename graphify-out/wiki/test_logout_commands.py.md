# test_logout_commands.py

> 114 nodes

## Key Concepts

- **test_logout_commands.py** (42 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **logout_commands.py** (35 connections) — `server/commands/logout_commands.py`
- **handle_logout_command()** (26 connections) — `server/commands/logout_commands.py`
- **asyncio** (18 connections)
- **_get_player_for_logout()** (17 connections) — `server/commands/logout_commands.py`
- **test_logout_commands_helpers.py** (15 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **_get_player_position_from_connection_manager()** (14 connections) — `server/commands/logout_commands.py`
- **handle_quit_command()** (14 connections) — `server/commands/logout_commands.py`
- **_clear_corrupted_cache_entry()** (12 connections) — `server/commands/logout_commands.py`
- **_sync_player_position()** (12 connections) — `server/commands/logout_commands.py`
- **Any** (12 connections)
- **_disconnect_player_connections()** (9 connections) — `server/commands/logout_commands.py`
- **_is_player_in_combat_for_logout()** (8 connections) — `server/commands/logout_commands.py`
- **_prepare_player_for_logout()** (7 connections) — `server/commands/logout_commands.py`
- **_update_and_save_player_last_active()** (7 connections) — `server/commands/logout_commands.py`
- **_resolve_disconnect_player_id()** (5 connections) — `server/commands/logout_commands.py`
- **_coerce_player_uuid()** (4 connections) — `server/commands/logout_commands.py`
- **_force_disconnect_player()** (4 connections) — `server/commands/logout_commands.py`
- **_get_app_services()** (4 connections) — `server/commands/logout_commands.py`
- **test_disconnect_player_connections_error()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_no_manager()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_success()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_corrupted_cache()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_cache()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- *... and 89 more nodes in this community*

## Relationships

- [TestLogoutCommand](TestLogoutCommand.md) (8 shared connections)
- [get_cached_player](get_cached_player.md) (5 shared connections)
- [Player](Player.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [fixture](fixture.md) (4 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (3 shared connections)
- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) (2 shared connections)
- [.async_persistence](async_persistence.md) (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_commands.py`
- `server/tests/unit/commands/test_logout_commands_helpers.py`

## Audit Trail

- EXTRACTED: 240 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*