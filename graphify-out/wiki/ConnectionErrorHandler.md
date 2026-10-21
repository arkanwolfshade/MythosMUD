# ConnectionErrorHandler

> 44 nodes · cohesion 0.08

## Key Concepts

- **test_logout_commands.py** (42 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **handle_logout_command()** (26 connections) — `server/commands/logout_commands.py`
- **asyncio** (18 connections)
- **_get_player_for_logout()** (17 connections) — `server/commands/logout_commands.py`
- **_disconnect_player_connections()** (9 connections) — `server/commands/logout_commands.py`
- **test_get_player_for_logout_persistence_error()** (5 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_quit_command_persistence_error()** (5 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_error()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_no_manager()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_success()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_corrupted_cache()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_cache()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_persistence_returns_coroutine()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_error_handling()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_no_player()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_success()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_syncs_position()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_quit_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_quit_command_success()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_update_and_save_player_last_active_no_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_update_and_save_player_last_active_success()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **Disconnect player from all connections. Args: connection_manager: Connection…** (1 connections) — `server/commands/logout_commands.py`
- **Handle the logout command for cleanly disconnecting from the game. This command…** (1 connections) — `server/commands/logout_commands.py`
- *... and 19 more nodes in this community*

## Relationships

- [test_players_procedures.py](test_players_procedures.py.md) (20 shared connections)
- [Any](Any.md) (9 shared connections)
- [test_admin_summon_command.py](test_admin_summon_command.py.md) (8 shared connections)
- [P4 · Intent Sweep — Core Feature Issues](P4_·_Intent_Sweep_—_Core_Feature_Issues.md) (5 shared connections)
- [test_test_runner_cli.py](test_test_runner_cli.py.md) (4 shared connections)
- [session_factory](session_factory.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (2 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (1 shared connections)
- [test_player_event_handlers_utils.py](test_player_event_handlers_utils.py.md) (1 shared connections)
- [command_parser.py](command_parser.py.md) (1 shared connections)
- [.load_room_data](load_room_data.md) (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_commands.py`

## Audit Trail

- EXTRACTED: 121 (92%)
- INFERRED: 11 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*