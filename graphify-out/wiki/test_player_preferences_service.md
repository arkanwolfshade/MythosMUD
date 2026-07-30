# test player preferences service

> 68 nodes

## Key Concepts

- **get_async_session()** (54 connections) — `server/database.py`
- **PlayerChannelPreferences** (30 connections) — `server/models/player.py`
- **PlayerPreferencesService** (19 connections) — `server/services/player_preferences_service.py`
- **channel_commands.py** (16 connections) — `server/commands/channel_commands.py`
- **._is_valid_player_id()** (11 connections) — `server/services/player_preferences_service.py`
- **handle_channel_command()** (10 connections) — `server/commands/channel_commands.py`
- **UUID** (10 connections)
- **fetch_professions()** (9 connections) — `server/async_persistence_direct_queries.py`
- **player_preferences_service.py** (9 connections) — `server/services/player_preferences_service.py`
- **AsyncSession** (8 connections)
- **Any** (8 connections)
- **.update_default_channel()** (8 connections) — `server/services/player_preferences_service.py`
- **.mute_channel()** (8 connections) — `server/services/player_preferences_service.py`
- **.unmute_channel()** (8 connections) — `server/services/player_preferences_service.py`
- **.is_channel_muted()** (8 connections) — `server/services/player_preferences_service.py`
- **.create_player_preferences()** (7 connections) — `server/services/player_preferences_service.py`
- **.get_player_preferences()** (7 connections) — `server/services/player_preferences_service.py`
- **.get_muted_channels()** (7 connections) — `server/services/player_preferences_service.py`
- **.delete_player_preferences()** (7 connections) — `server/services/player_preferences_service.py`
- **_handle_default_channel_setting()** (6 connections) — `server/commands/channel_commands.py`
- **._is_valid_channel()** (6 connections) — `server/services/player_preferences_service.py`
- **_get_persistence_and_player()** (5 connections) — `server/commands/channel_commands.py`
- **load_seed_data()** (4 connections) — `scripts/load_seed_using_project_db.py`
- **Any** (4 connections)
- **_extract_channel_from_command()** (4 connections) — `server/commands/channel_commands.py`
- *... and 43 more nodes in this community*

## Relationships

- [real time](real_time.md) (17 shared connections)
- [metrics](metrics.md) (7 shared connections)
- [Connection Manager](Connection_Manager.md) (7 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (6 shared connections)
- [. init ()](_init_%28%29.md) (6 shared connections)
- [Test get room environment() treats](Test_get_room_environment%28%29_treats.md) (5 shared connections)
- [.initialize()](initialize%28%29.md) (4 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [main()](main%28%29.md) (3 shared connections)
- [test rate limiter utils](test_rate_limiter_utils.md) (3 shared connections)
- [test magic commands](test_magic_commands.md) (2 shared connections)
- [DropResolved](DropResolved.md) (2 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `server/async_persistence_direct_queries.py`
- `server/commands/channel_commands.py`
- `server/database.py`
- `server/models/player.py`
- `server/services/player_preferences_service.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 303 (90%)
- INFERRED: 35 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*