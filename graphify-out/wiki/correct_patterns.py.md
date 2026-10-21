# correct_patterns.py

> 42 nodes · cohesion 0.09

## Key Concepts

- **test_channel_commands.py** (20 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **channel_commands.py** (19 connections) — `server/commands/channel_commands.py`
- **handle_channel_command()** (15 connections) — `server/commands/channel_commands.py`
- **_handle_default_channel_setting()** (11 connections) — `server/commands/channel_commands.py`
- **asyncio** (9 connections)
- **_extract_channel_from_command()** (8 connections) — `server/commands/channel_commands.py`
- **_get_persistence_and_player()** (8 connections) — `server/commands/channel_commands.py`
- **_validate_channel_name()** (6 connections) — `server/commands/channel_commands.py`
- **Any** (4 connections)
- **test_get_persistence_and_player_no_persistence()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_get_persistence_and_player_not_found()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_default_subcommand()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_switch_valid_channel()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_usage_when_channel_missing()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_default_channel_setting_invalid_channel()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_default_channel_setting_sqlalchemy_error()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_default_channel_setting_success()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_extract_channel_from_command_direct()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_extract_channel_from_command_missing()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_extract_channel_from_command_parsed_fallback()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_validate_channel_name_invalid()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **Channel management commands for Advanced Chat Channels. This module provides…** (1 connections) — `server/commands/channel_commands.py`
- **Validate channel name. Returns error dict if invalid, None if valid.** (1 connections) — `server/commands/channel_commands.py`
- **Handle the channel command for switching channels or setting default channel.…** (1 connections) — `server/commands/channel_commands.py`
- *... and 17 more nodes in this community*

## Relationships

- [command_parser.py](command_parser.py.md) (10 shared connections)
- [server/tests/conftest.py](server-tests-conftest.py.md) (3 shared connections)
- [ItemFactory](ItemFactory.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)
- [.load_room_data](load_room_data.md) (1 shared connections)

## Source Files

- `server/commands/channel_commands.py`
- `server/tests/unit/commands/test_channel_commands.py`

## Audit Trail

- EXTRACTED: 92 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*