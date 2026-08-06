# argon2 auth rationale

> 70 nodes

## Key Concepts

- **test_channel_commands.py** (20 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **PlayerPreferencesService** (19 connections) — `server/services/player_preferences_service.py`
- **channel_commands.py** (17 connections) — `server/commands/channel_commands.py`
- **handle_channel_command()** (14 connections) — `server/commands/channel_commands.py`
- **._is_valid_player_id()** (11 connections) — `server/services/player_preferences_service.py`
- **_handle_default_channel_setting()** (10 connections) — `server/commands/channel_commands.py`
- **UUID** (10 connections)
- **_get_persistence_and_player()** (8 connections) — `server/commands/channel_commands.py`
- **_extract_channel_from_command()** (8 connections) — `server/commands/channel_commands.py`
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
- **._is_valid_channel()** (6 connections) — `server/services/player_preferences_service.py`
- **_validate_channel_name()** (5 connections) — `server/commands/channel_commands.py`
- **Any** (4 connections)
- **test_get_persistence_and_player_no_persistence()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_get_persistence_and_player_not_found()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- **test_extract_channel_from_command_direct()** (3 connections) — `server/tests/unit/commands/test_channel_commands.py`
- *... and 45 more nodes in this community*

## Relationships

- [player room realtime](player_room_realtime.md) (12 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [realtime real time](realtime_real_time.md) (2 shared connections)
- [player preferences service](player_preferences_service.md) (2 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)

## Source Files

- `server/commands/channel_commands.py`
- `server/services/player_preferences_service.py`
- `server/tests/unit/commands/test_channel_commands.py`

## Audit Trail

- EXTRACTED: 274 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*