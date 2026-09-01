# test_game_tick_processing.py

> 38 nodes

## Key Concepts

- **test_game_tick_processing.py** (40 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **asyncio** (17 connections)
- **_validate_and_get_player()** (9 connections) — `server/app/game_tick_status_effects.py`
- **test_process_single_player_mp_regeneration()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_decayed_corpses_no_persistence()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_single_decayed_corpse_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_get_tick_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_all_status_effects_empty()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_casting_progress_calls_magic_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_combat_tick_calls_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_damage_over_time_zero_remaining()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_dp_decay_and_death_no_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_heal_over_time_effect()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_npc_maintenance_runs_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_player_effects_expiration_login_warded()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_single_effect_heal_expires()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_status_effects_no_online_players()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_status_effects_with_online_player()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_update_player_status_effects_saves()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_and_get_player_invalid_id()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_and_get_player_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_connection_manager_is_none()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_container_is_none()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_async_persistence()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_connection_manager()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 13 more nodes in this community*

## Relationships

- [game_tick_status_effects.py](game_tick_status_effects.py.md) (18 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (11 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (7 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [User](User.md) (1 shared connections)

## Source Files

- `server/app/game_tick_status_effects.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 78 (80%)
- INFERRED: 20 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*