# test_game_tick_processing.py

> 52 nodes

## Key Concepts

- **test_game_tick_processing.py** (43 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **asyncio** (21 connections)
- **_app_container()** (14 connections) — `server/app/game_tick_protocols.py`
- **process_combat_cleanup()** (10 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (10 connections) — `server/app/game_tick_processing.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (8 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (7 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (7 connections)
- **.should_run_maintenance()** (4 connections) — `server/config/npc_config.py`
- **test_process_player_effects_expiration_survives_database_error()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_decayed_corpses_no_persistence()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_single_decayed_corpse_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_get_tick_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_all_status_effects_empty()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_casting_progress_calls_magic_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_combat_cleanup_no_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_combat_cleanup_runs_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_combat_cleanup_skips_off_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_combat_tick_calls_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_damage_over_time_zero_remaining()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_dp_decay_and_death_no_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_heal_over_time_effect()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_npc_maintenance_runs_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_player_effects_expiration_login_warded()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 27 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (27 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (15 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (7 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [reset_current_tick](reset_current_tick.md) (2 shared connections)
- [NPCMaintenanceConfig](NPCMaintenanceConfig.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/config/npc_config.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 126 (88%)
- INFERRED: 18 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*