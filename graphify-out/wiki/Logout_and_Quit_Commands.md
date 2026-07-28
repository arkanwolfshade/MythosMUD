# Logout and Quit Commands

> 107 nodes · cohesion 0.03

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
- **_disconnect_player_connections()** (8 connections) — `server/commands/logout_commands.py`
- **Any** (8 connections)
- **_update_and_save_player_last_active()** (7 connections) — `server/commands/logout_commands.py`
- **test_clear_corrupted_cache_entry()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_clear_corrupted_cache_entry_no_request()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_clear_corrupted_cache_entry_no_state()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_get_player_position_from_connection_manager()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_get_player_position_from_connection_manager_by_name()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_get_player_position_from_connection_manager_no_manager()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_get_player_position_from_connection_manager_not_found()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_sync_player_position()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_sync_player_position_no_change()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_sync_player_position_none()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_clear_corrupted_cache_entry_no_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_clear_corrupted_cache_entry_no_request()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_clear_corrupted_cache_entry_with_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- *... and 82 more nodes in this community*

## Relationships

- [Logout Command Tests](Logout_Command_Tests.md) (8 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (6 shared connections)
- [Player Cache](Player_Cache.md) (5 shared connections)
- [Who Command Tests](Who_Command_Tests.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (2 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (1 shared connections)

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