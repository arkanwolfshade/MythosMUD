# handle_channel_command

> 11 nodes

## Key Concepts

- **handle_channel_command()** (10 connections) — `server/commands/channel_commands.py`
- **_handle_default_channel_setting()** (6 connections) — `server/commands/channel_commands.py`
- **_get_persistence_and_player()** (5 connections) — `server/commands/channel_commands.py`
- **_extract_channel_from_command()** (4 connections) — `server/commands/channel_commands.py`
- **Any** (4 connections)
- **_validate_channel_name()** (3 connections) — `server/commands/channel_commands.py`
- **Validate channel name. Returns error dict if invalid, None if valid.** (1 connections) — `server/commands/channel_commands.py`
- **Handle the channel command for switching channels or setting default channel.…** (1 connections) — `server/commands/channel_commands.py`
- **Get persistence and player. Returns (persistence, player) or (None, None) if…** (1 connections) — `server/commands/channel_commands.py`
- **Extract channel name from command_data. Returns channel name or None.** (1 connections) — `server/commands/channel_commands.py`
- **Handle setting default channel. Returns result dict or None if not a default…** (1 connections) — `server/commands/channel_commands.py`

## Relationships

- [Player](Player.md) (5 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)
- [PlayerPreferencesService](PlayerPreferencesService.md) (1 shared connections)

## Source Files

- `server/commands/channel_commands.py`

## Audit Trail

- EXTRACTED: 35 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*