# test_channel_commands.py

> 71 nodes

## Key Concepts

- **test_channel_commands.py** (21 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **PlayerPreferencesService** (19 connections) — `server/services/player_preferences_service.py`
- **channel_commands.py** (17 connections) — `server/commands/channel_commands.py`
- **handle_channel_command()** (14 connections) — `server/commands/channel_commands.py`
- **._is_valid_player_id()** (11 connections) — `server/services/player_preferences_service.py`
- **_handle_default_channel_setting()** (10 connections) — `server/commands/channel_commands.py`
- **UUID** (10 connections)
- **_get_persistence_and_player()** (9 connections) — `server/commands/channel_commands.py`
- **asyncio** (9 connections)
- **_extract_channel_from_command()** (8 connections) — `server/commands/channel_commands.py`
- **Any** (8 connections)
- **AsyncSession** (8 connections)
- **.create_player_preferences()** (7 connections) — `server/services/player_preferences_service.py`
- **.is_channel_muted()** (7 connections) — `server/services/player_preferences_service.py`
- **.mute_channel()** (7 connections) — `server/services/player_preferences_service.py`
- **.unmute_channel()** (7 connections) — `server/services/player_preferences_service.py`
- **.update_default_channel()** (7 connections) — `server/services/player_preferences_service.py`
- **.delete_player_preferences()** (6 connections) — `server/services/player_preferences_service.py`
- **.get_muted_channels()** (6 connections) — `server/services/player_preferences_service.py`
- **.get_player_preferences()** (6 connections) — `server/services/player_preferences_service.py`
- **._is_valid_channel()** (6 connections) — `server/services/player_preferences_service.py`
- **_validate_channel_name()** (5 connections) — `server/commands/channel_commands.py`
- **test_get_persistence_and_player_no_persistence()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_get_persistence_and_player_not_found()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_default_subcommand()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- *... and 46 more nodes in this community*

## Relationships

- [pytest.md](pytest.md.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_player_preferences_service.py](test_player_preferences_service.py.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)

## Source Files

- `server/commands/channel_commands.py`
- `server/services/player_preferences_service.py`
- `server/tests/unit/commands/test_channel_commands.py`

## Audit Trail

- EXTRACTED: 154 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*