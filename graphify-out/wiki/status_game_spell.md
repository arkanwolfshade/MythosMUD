# status game spell

> 16 nodes

## Key Concepts

- **GameTickService** (30 connections) — `server/services/game_tick_service.py`
- **.__init__()** (2 connections) — `server/services/game_tick_service.py`
- **.stop()** (2 connections) — `server/services/game_tick_service.py`
- **.get_tick_count()** (2 connections) — `server/services/game_tick_service.py`
- **.reset_tick_count()** (2 connections) — `server/services/game_tick_service.py`
- **.get_tick_interval()** (2 connections) — `server/services/game_tick_service.py`
- **.set_tick_interval()** (2 connections) — `server/services/game_tick_service.py`
- **.is_service_running()** (2 connections) — `server/services/game_tick_service.py`
- **Service that manages the game tick system.      The game tick system runs at reg** (1 connections) — `server/services/game_tick_service.py`
- **Initialize the GameTickService.          Args:             event_publisher: Even** (1 connections) — `server/services/game_tick_service.py`
- **Stop the game tick service.          Returns:             bool: True if stopped** (1 connections) — `server/services/game_tick_service.py`
- **Get the current tick count.          Returns:             int: Current number of** (1 connections) — `server/services/game_tick_service.py`
- **Reset the tick count to zero.** (1 connections) — `server/services/game_tick_service.py`
- **Get the current tick interval.          Returns:             float: Current tick** (1 connections) — `server/services/game_tick_service.py`
- **Set a new tick interval.          Args:             interval: New tick interval** (1 connections) — `server/services/game_tick_service.py`
- **Check if the service is currently running.          Returns:             bool: T** (1 connections) — `server/services/game_tick_service.py`

## Relationships

- [player persistence repository](player_persistence_repository.md) (8 shared connections)
- [tracked app task](tracked_app_task.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [test_mute_channel_already_muted](test_mute_channel_already_muted.md) (1 shared connections)
- [test_unmute_channel_success](test_unmute_channel_success.md) (1 shared connections)
- [test_is_channel_muted_true](test_is_channel_muted_true.md) (1 shared connections)
- [test_unmute_channel_not_muted](test_unmute_channel_not_muted.md) (1 shared connections)
- [test_delete_player_preferences_database_error](test_delete_player_preferences_database_error.md) (1 shared connections)
- [test_update_default_channel_database_error](test_update_default_channel_database_error.md) (1 shared connections)
- [test_delete_player_preferences_success](test_delete_player_preferences_success.md) (1 shared connections)
- [test_mute_channel_invalid_channel](test_mute_channel_invalid_channel.md) (1 shared connections)
- [test_mute_channel_system_channel](test_mute_channel_system_channel.md) (1 shared connections)

## Source Files

- `server/services/game_tick_service.py`

## Audit Trail

- EXTRACTED: 51 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*