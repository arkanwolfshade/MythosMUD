# test_channel_commands.py

> 42 nodes

## Key Concepts

- **test_channel_commands.py** (21 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **channel_commands.py** (17 connections) — `server/commands/channel_commands.py`
- **handle_channel_command()** (14 connections) — `server/commands/channel_commands.py`
- **_handle_default_channel_setting()** (10 connections) — `server/commands/channel_commands.py`
- **_get_persistence_and_player()** (9 connections) — `server/commands/channel_commands.py`
- **asyncio** (9 connections)
- **_extract_channel_from_command()** (8 connections) — `server/commands/channel_commands.py`
- **_validate_channel_name()** (5 connections) — `server/commands/channel_commands.py`
- **test_get_persistence_and_player_no_persistence()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_get_persistence_and_player_not_found()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_default_subcommand()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_switch_valid_channel()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_usage_when_channel_missing()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_default_channel_setting_invalid_channel()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_default_channel_setting_sqlalchemy_error()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_default_channel_setting_success()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **Any** (4 connections)
- **test_extract_channel_from_command_direct()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_extract_channel_from_command_missing()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_extract_channel_from_command_parsed_fallback()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_validate_channel_name_invalid()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **Channel management commands for Advanced Chat Channels. This module provides…** (1 connections) — `server/commands/channel_commands.py`
- **Validate channel name. Returns error dict if invalid, None if valid.** (1 connections) — `server/commands/channel_commands.py`
- **Handle the channel command for switching channels or setting default channel.…** (1 connections) — `server/commands/channel_commands.py`
- *... and 17 more nodes in this community*

## Relationships

- [command_service.py](command_service.py.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [PlayerPreferencesService](PlayerPreferencesService.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/channel_commands.py`
- `server/tests/unit/commands/test_channel_commands.py`

## Audit Trail

- EXTRACTED: 88 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*