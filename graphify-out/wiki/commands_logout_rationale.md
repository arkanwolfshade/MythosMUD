# commands logout rationale

> 159 nodes

## Key Concepts

- **test_logout_commands.py** (42 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **handle_logout_command()** (25 connections) — `server/commands/logout_commands.py`
- **logout_commands.py** (20 connections) — `server/commands/logout_commands.py`
- **test_logout_commands_helpers.py** (15 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **get_cached_player()** (15 connections) — `server/utils/player_cache.py`
- **_get_player_position_from_connection_manager()** (14 connections) — `server/commands/logout_commands.py`
- **_get_player_for_logout()** (13 connections) — `server/commands/logout_commands.py`
- **TestLogoutCommand** (13 connections) — `server/tests/unit/commands/test_logout_command.py`
- **cache_player()** (13 connections) — `server/utils/player_cache.py`
- **_clear_corrupted_cache_entry()** (12 connections) — `server/commands/logout_commands.py`
- **_sync_player_position()** (12 connections) — `server/commands/logout_commands.py`
- **test_player_cache.py** (11 connections) — `server/tests/unit/utils/test_player_cache.py`
- **handle_quit_command()** (10 connections) — `server/commands/logout_commands.py`
- **Any** (8 connections)
- **_disconnect_player_connections()** (8 connections) — `server/commands/logout_commands.py`
- **Any** (8 connections)
- **_update_and_save_player_last_active()** (7 connections) — `server/commands/logout_commands.py`
- **player_cache.py** (7 connections) — `server/utils/player_cache.py`
- **_get_request_state()** (6 connections) — `server/utils/player_cache.py`
- **.test_logout_command_success()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_persists_position()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_persistence_error()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_connection_error()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_with_args()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- *... and 134 more nodes in this community*

## Relationships

- [command validation commands](command_validation_commands.md) (5 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [commands who rationale](commands_who_rationale.md) (4 shared connections)
- [commands party examples](commands_party_examples.md) (3 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (2 shared connections)
- [nats services metrics](nats_services_metrics.md) (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_command.py`
- `server/tests/unit/commands/test_logout_commands.py`
- `server/tests/unit/commands/test_logout_commands_helpers.py`
- `server/tests/unit/utils/test_player_cache.py`
- `server/utils/player_cache.py`

## Audit Trail

- EXTRACTED: 508 (96%)
- INFERRED: 19 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*