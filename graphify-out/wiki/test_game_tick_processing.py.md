# test_game_tick_processing.py

> 107 nodes

## Key Concepts

- **test_game_tick_processing.py** (43 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_game_tick_processing_async.py** (21 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **asyncio** (21 connections)
- **game_tick_loop()** (20 connections) — `server/app/game_tick_processing.py`
- **asyncio** (15 connections)
- **process_combat_cleanup()** (10 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (10 connections) — `server/app/game_tick_processing.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (8 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (7 connections) — `server/app/game_tick_corpses.py`
- **process_casting_progress()** (7 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (7 connections)
- **reset_current_tick()** (6 connections) — `server/app/game_tick_counter.py`
- **set_current_tick()** (5 connections) — `server/app/game_tick_counter.py`
- **.should_run_maintenance()** (4 connections) — `server/config/npc_config.py`
- **test_process_combat_tick_no_service()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_combat_tick_success()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_no_damage()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_no_remaining()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_success()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_healing()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_remaining()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_success()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_damage_over_time()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_expired()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- *... and 82 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (59 shared connections)
- [MythosChronicle](MythosChronicle.md) (8 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (4 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (1 shared connections)
- [get_config](get_config.md) (1 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (1 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/app/game_tick_counter.py`
- `server/app/game_tick_processing.py`
- `server/config/npc_config.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 202 (84%)
- INFERRED: 39 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*