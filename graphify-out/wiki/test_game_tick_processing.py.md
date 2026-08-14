# test_game_tick_processing.py

> 53 nodes

## Key Concepts

- **test_game_tick_processing.py** (69 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **asyncio** (25 connections)
- **game_tick_loop()** (16 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (16 connections)
- **process_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (11 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (10 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (9 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (9 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_all_status_effects()** (8 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (8 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (7 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (6 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (6 connections) — `server/app/game_tick_processing.py`
- **test_broadcast_tick_event()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_decayed_corpses_no_persistence()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_decayed_corpses_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_single_decayed_corpse_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_game_tick_loop_cancelled_on_sleep()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_all_status_effects_empty()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_casting_progress_calls_magic_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 28 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (38 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (22 shared connections)
- [_validate_app_state_for_status_effects](_validate_app_state_for_status_effects.md) (10 shared connections)
- [get_current_tick](get_current_tick.md) (4 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [get_tick_interval](get_tick_interval.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (2 shared connections)
- [broadcast_game_event](broadcast_game_event.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [container_events.py](container_events.py.md) (1 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 202 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*