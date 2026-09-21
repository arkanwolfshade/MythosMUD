# utility_commands.py

> 35 nodes

## Key Concepts

- **utility_commands.py** (20 connections) — `server/commands/utility_commands.py`
- **who_commands.py** (16 connections) — `server/commands/who_commands.py`
- **filter_players_by_name()** (14 connections) — `server/commands/who_commands.py`
- **handle_who_command()** (14 connections) — `server/commands/who_commands.py`
- **format_player_entry()** (13 connections) — `server/commands/who_commands.py`
- **format_player_location()** (13 connections) — `server/commands/who_commands.py`
- **test_who_commands_helpers.py** (12 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **filter_online_players()** (10 connections) — `server/commands/who_commands.py`
- **format_who_result()** (10 connections) — `server/commands/who_commands.py`
- **get_players_for_who()** (8 connections) — `server/commands/who_commands.py`
- **Any** (6 connections)
- **test_filter_players_by_name_empty_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_filter_players_by_name_found()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_filter_players_by_name_not_found()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_entry()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_entry_admin()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_location_invalid()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_location_valid()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **Utility commands for MythosMUD. This module contains handlers for utility…** (1 connections) — `server/commands/utility_commands.py`
- **Who command handlers and utilities for MythosMUD. This module contains the who…** (1 connections) — `server/commands/who_commands.py`
- **Filter players to only those who are online (active within threshold). Args:…** (1 connections) — `server/commands/who_commands.py`
- **Format the who command result message. Args: players: List of player objects to…** (1 connections) — `server/commands/who_commands.py`
- **Get the list of players to show and the effective filter term. Args:…** (1 connections) — `server/commands/who_commands.py`
- **Filter players by case-insensitive partial name matching. Args: players: List…** (1 connections) — `server/commands/who_commands.py`
- **Handle the who command for listing online players. Args: command_data: Command…** (1 connections) — `server/commands/who_commands.py`
- *... and 10 more nodes in this community*

## Relationships

- [test_who_commands.py](test_who_commands.py.md) (30 shared connections)
- [asyncio](asyncio.md) (9 shared connections)
- [command_service.py](command_service.py.md) (3 shared connections)
- [test_logout_commands.py](test_logout_commands.py.md) (3 shared connections)
- [test_status_commands.py](test_status_commands.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [.state](state.md) (2 shared connections)
- [handle_time_command](handle_time_command.md) (1 shared connections)
- [TestLogoutCommand](TestLogoutCommand.md) (1 shared connections)
- [test_utility_commands_whoami.py](test_utility_commands_whoami.py.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [models/player.py](models-player.py.md) (1 shared connections)

## Source Files

- `server/commands/utility_commands.py`
- `server/commands/who_commands.py`
- `server/tests/unit/commands/test_who_commands_helpers.py`

## Audit Trail

- EXTRACTED: 115 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*