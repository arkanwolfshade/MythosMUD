# player persistence repository

> 16 nodes

## Key Concepts

- **TestGameTickService** (20 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_init_default_interval()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_stop_not_running()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_stop_failure()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_get_tick_interval()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_increments_count()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_publishes_events()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_handles_exceptions()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test suite for GameTickService class.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test GameTickService initialization with default interval.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test stop returns True when not running.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test stop handles exceptions gracefully.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test get_tick_interval returns interval.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test _tick_loop increments tick count.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test _tick_loop publishes game tick events.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test _tick_loop handles exceptions and continues.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`

## Relationships

- [status game spell](status_game_spell.md) (8 shared connections)
- [test_mute_channel_already_muted](test_mute_channel_already_muted.md) (1 shared connections)
- [test_unmute_channel_success](test_unmute_channel_success.md) (1 shared connections)
- [test_is_channel_muted_true](test_is_channel_muted_true.md) (1 shared connections)
- [test_unmute_channel_not_muted](test_unmute_channel_not_muted.md) (1 shared connections)
- [test_delete_player_preferences_database_error](test_delete_player_preferences_database_error.md) (1 shared connections)
- [test_update_default_channel_database_error](test_update_default_channel_database_error.md) (1 shared connections)
- [test_delete_player_preferences_success](test_delete_player_preferences_success.md) (1 shared connections)
- [test_mute_channel_invalid_channel](test_mute_channel_invalid_channel.md) (1 shared connections)
- [test_mute_channel_system_channel](test_mute_channel_system_channel.md) (1 shared connections)
- [room realtime subscription](room_realtime_subscription.md) (1 shared connections)
- [test_get_muted_channels_not_found](test_get_muted_channels_not_found.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_game_tick_service.py`

## Audit Trail

- EXTRACTED: 48 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*