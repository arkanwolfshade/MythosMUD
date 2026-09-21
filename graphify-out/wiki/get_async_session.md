# get_async_session

> 53 nodes

## Key Concepts

- **get_async_session()** (61 connections) — `server/database.py`
- **test_channel_commands.py** (20 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **channel_commands.py** (17 connections) — `server/commands/channel_commands.py`
- **handle_channel_command()** (14 connections) — `server/commands/channel_commands.py`
- **_handle_default_channel_setting()** (10 connections) — `server/commands/channel_commands.py`
- **asyncio** (9 connections)
- **_extract_channel_from_command()** (8 connections) — `server/commands/channel_commands.py`
- **_get_persistence_and_player()** (8 connections) — `server/commands/channel_commands.py`
- **_validate_channel_name()** (5 connections) — `server/commands/channel_commands.py`
- **main()** (4 connections) — `scripts/verify_and_load_seed.py`
- **test_get_persistence_and_player_no_persistence()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_get_persistence_and_player_not_found()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_default_subcommand()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_switch_valid_channel()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_channel_command_usage_when_channel_missing()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_default_channel_setting_invalid_channel()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_default_channel_setting_sqlalchemy_error()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_handle_default_channel_setting_success()** (4 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **verify_and_load_seed.py** (4 connections) — `scripts/verify_and_load_seed.py`
- **Any** (4 connections)
- **add_flavor_text_column()** (3 connections) — `scripts/add_flavor_text_column.py`
- **load_seed_data()** (3 connections) — `scripts/load_seed_using_project_db.py`
- **test_extract_channel_from_command_direct()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_extract_channel_from_command_missing()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- *... and 28 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (8 shared connections)
- [DatabaseError](DatabaseError.md) (8 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (5 shared connections)
- [CorruptionTier](CorruptionTier.md) (4 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [PlayerPreferencesService](PlayerPreferencesService.md) (2 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (2 shared connections)
- [User](User.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (2 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/commands/channel_commands.py`
- `server/database.py`
- `server/tests/unit/commands/test_channel_commands.py`

## Audit Trail

- EXTRACTED: 156 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*