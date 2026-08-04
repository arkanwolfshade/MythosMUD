# argon2 auth rationale

> 41 nodes

## Key Concepts

- **test_channel_commands.py** (20 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **channel_commands.py** (17 connections) — `server/commands/channel_commands.py`
- **handle_channel_command()** (14 connections) — `server/commands/channel_commands.py`
- **_handle_default_channel_setting()** (10 connections) — `server/commands/channel_commands.py`
- **_get_persistence_and_player()** (8 connections) — `server/commands/channel_commands.py`
- **_extract_channel_from_command()** (8 connections) — `server/commands/channel_commands.py`
- **_validate_channel_name()** (5 connections) — `server/commands/channel_commands.py`
- **Any** (4 connections)
- **test_get_persistence_and_player_no_persistence()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_get_persistence_and_player_not_found()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_extract_channel_from_command_direct()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_extract_channel_from_command_parsed_fallback()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_extract_channel_from_command_missing()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_validate_channel_name_invalid()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_usage_when_channel_missing()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_switch_valid_channel()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_default_channel_setting_success()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_default_channel_setting_invalid_channel()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_default_channel_setting_sqlalchemy_error()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_default_subcommand()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **Channel management commands for Advanced Chat Channels.  This module provides ha** (1 connections) — `server/commands/channel_commands.py`
- **Get persistence and player. Returns (persistence, player) or (None, None) if not** (1 connections) — `server/commands/channel_commands.py`
- **Extract channel name from command_data. Returns channel name or None.** (1 connections) — `server/commands/channel_commands.py`
- **Handle setting default channel. Returns result dict or None if not a default com** (1 connections) — `server/commands/channel_commands.py`
- *... and 16 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [commands rescue rationale](commands_rescue_rationale.md) (3 shared connections)
- [commands party examples](commands_party_examples.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)

## Source Files

- `server/commands/channel_commands.py`
- `server/tests/unit/commands/test_channel_commands.py`

## Audit Trail

- EXTRACTED: 144 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*