# test_websocket_handler_validation_errors.py

> 17 nodes · cohesion 0.12

## Key Concepts

- **asyncio** (20 connections)
- **test_process_tick_regeneration_restores_mp()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_sitting_position()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_item_calculates_max_from_power()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_item_respects_max()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_item_uses_magic_service()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_meditation_at_max()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_meditation_player_not_found()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_meditation_restores_mp()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_meditation() returns error when player not found.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_meditation() returns message when MP already at max.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_meditation() restores MP.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_item() respects max_mp limit.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_item() uses magic_service if available.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_item() calculates max_mp from power if not present.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test process_tick_regeneration() uses REST multiplier for sitting position.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test process_tick_regeneration() restores MP.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Relationships

- [test_get_dead_players_debug_only_when_found](test_get_dead_players_debug_only_when_found.md) (8 shared connections)
- [server/app/__init__.py](server-app-__init__.py.md) (1 shared connections)
- [test_mute_channel_not_found](test_mute_channel_not_found.md) (1 shared connections)
- [test_ensure_player_posture_lying_already_lying](test_ensure_player_posture_lying_already_lying.md) (1 shared connections)
- [test_is_channel_muted_invalid_channel](test_is_channel_muted_invalid_channel.md) (1 shared connections)
- [test_delete_player_preferences_success](test_delete_player_preferences_success.md) (1 shared connections)
- [test_update_default_channel_not_found](test_update_default_channel_not_found.md) (1 shared connections)
- [test_get_muted_channels_success](test_get_muted_channels_success.md) (1 shared connections)
- [test_get_player_preferences_not_found](test_get_player_preferences_not_found.md) (1 shared connections)
- [test_handle_player_death_with_killer_info](test_handle_player_death_with_killer_info.md) (1 shared connections)
- [test_handle_player_death_handles_error](test_handle_player_death_handles_error.md) (1 shared connections)
- [test_clear_player_combat_state_no_service](test_clear_player_combat_state_no_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*