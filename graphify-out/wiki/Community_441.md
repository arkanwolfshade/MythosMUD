# Community 441

> 40 nodes

## Key Concepts

- **test_channel_commands.py** (20 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **handle_channel_command()** (13 connections) — `server/commands/channel_commands.py`
- **_handle_default_channel_setting()** (10 connections) — `server/commands/channel_commands.py`
- **asyncio** (9 connections)
- **_extract_channel_from_command()** (8 connections) — `server/commands/channel_commands.py`
- **_get_persistence_and_player()** (8 connections) — `server/commands/channel_commands.py`
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
- **Validate channel name. Returns error dict if invalid, None if valid.** (1 connections) — `server/commands/channel_commands.py`
- **Handle the channel command for switching channels or setting default channel.…** (1 connections) — `server/commands/channel_commands.py`
- **Get persistence and player. Returns (persistence, player) or (None, None) if…** (1 connections) — `server/commands/channel_commands.py`
- **Extract channel name from command_data. Returns channel name or None.** (1 connections) — `server/commands/channel_commands.py`
- *... and 15 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (7 shared connections)
- [Community 442](Community_442.md) (1 shared connections)
- [Community 25](Community_25.md) (1 shared connections)
- [Community 587](Community_587.md) (1 shared connections)

## Source Files

- `server/commands/channel_commands.py`
- `server/tests/unit/commands/test_channel_commands.py`

## Audit Trail

- EXTRACTED: 76 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*