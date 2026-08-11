# Logging Migration Examples

> 113 nodes

## Key Concepts

- **test_logout_commands.py** (42 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **logout_commands.py** (26 connections) — `server/commands/logout_commands.py`
- **handle_logout_command()** (24 connections) — `server/commands/logout_commands.py`
- **test_logout_commands_helpers.py** (15 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **_get_player_position_from_connection_manager()** (14 connections) — `server/commands/logout_commands.py`
- **Any** (13 connections)
- **_get_player_for_logout()** (13 connections) — `server/commands/logout_commands.py`
- **handle_quit_command()** (13 connections) — `server/commands/logout_commands.py`
- **_clear_corrupted_cache_entry()** (12 connections) — `server/commands/logout_commands.py`
- **_sync_player_position()** (12 connections) — `server/commands/logout_commands.py`
- **_disconnect_player_connections()** (9 connections) — `server/commands/logout_commands.py`
- **_prepare_player_for_logout()** (8 connections) — `server/commands/logout_commands.py`
- **_update_and_save_player_last_active()** (7 connections) — `server/commands/logout_commands.py`
- **_get_app_services()** (4 connections) — `server/commands/logout_commands.py`
- **_resolve_disconnect_player_id()** (4 connections) — `server/commands/logout_commands.py`
- **UUID** (4 connections)
- **_force_disconnect_player()** (4 connections) — `server/commands/logout_commands.py`
- **_mark_quit_intentional()** (4 connections) — `server/commands/logout_commands.py`
- **test_clear_corrupted_cache_entry_with_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_clear_corrupted_cache_entry_no_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_clear_corrupted_cache_entry_no_request()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_persistence()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_corrupted_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_persistence_error()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- *... and 88 more nodes in this community*

## Relationships

- [Container Open Events](Container_Open_Events.md) (9 shared connections)
- [Logout Command Tests](Logout_Command_Tests.md) (8 shared connections)
- [Test Refactoring Summary](Test_Refactoring_Summary.md) (5 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_commands.py`
- `server/tests/unit/commands/test_logout_commands_helpers.py`

## Audit Trail

- EXTRACTED: 391 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*