# Community 385

> 45 nodes

## Key Concepts

- **test_game_tick_processing.py** (40 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **asyncio** (21 connections)
- **_validate_app_state_for_status_effects()** (14 connections) — `server/app/game_tick_status_effects.py`
- **process_combat_cleanup()** (9 connections) — `server/app/game_tick_processing.py`
- **test_process_player_effects_expiration_survives_database_error()** (5 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_get_tick_interval()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_combat_cleanup_runs_on_interval()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_combat_cleanup_skips_off_interval()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_npc_maintenance_runs_on_interval()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_player_effects_expiration_login_warded()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_status_effects_with_online_player()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_decayed_corpses_no_persistence()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_single_decayed_corpse_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_all_status_effects_empty()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_casting_progress_calls_magic_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_combat_cleanup_no_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_combat_tick_calls_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_damage_over_time_zero_remaining()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_dp_decay_and_death_no_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_heal_over_time_effect()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_single_effect_heal_expires()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_status_effects_no_online_players()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_update_player_status_effects_saves()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_and_get_player_invalid_id()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_and_get_player_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 20 more nodes in this community*

## Relationships

- [Community 883](Community_883.md) (12 shared connections)
- [Community 831](Community_831.md) (12 shared connections)
- [Community 38](Community_38.md) (9 shared connections)
- [Community 370](Community_370.md) (6 shared connections)
- [Community 386](Community_386.md) (3 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (2 shared connections)
- [Community 268](Community_268.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/app/game_tick_status_effects.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 91 (77%)
- INFERRED: 27 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*