# game_tick_processing.py

> 76 nodes

## Key Concepts

- **game_tick_processing.py** (60 connections) — `server/app/game_tick_processing.py`
- **test_game_tick_processing.py** (43 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **asyncio** (21 connections)
- **game_tick_loop()** (20 connections) — `server/app/game_tick_processing.py`
- **_app_container()** (14 connections) — `server/app/game_tick_protocols.py`
- **broadcast_tick_event()** (13 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (12 connections) — `server/app/game_tick_corpses.py`
- **process_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **process_combat_cleanup()** (10 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (10 connections) — `server/app/game_tick_processing.py`
- **game_tick_counter.py** (9 connections) — `server/app/game_tick_counter.py`
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_corpses.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_corpses.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (8 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (7 connections) — `server/app/game_tick_corpses.py`
- **process_casting_progress()** (7 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (7 connections)
- **reset_current_tick()** (6 connections) — `server/app/game_tick_counter.py`
- **set_current_tick()** (5 connections) — `server/app/game_tick_counter.py`
- **_tick_broadcast_payload()** (4 connections) — `server/app/game_tick_processing.py`
- **.should_run_maintenance()** (4 connections) — `server/config/npc_config.py`
- **test_get_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_player_effects_expiration_survives_database_error()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_reset_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 51 more nodes in this community*

## Relationships

- [game_tick_status_effects.py](game_tick_status_effects.py.md) (35 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (30 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (9 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (5 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (5 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (4 shared connections)
- [test_lifespan_shutdown.py](test_lifespan_shutdown.py.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/app/game_tick_counter.py`
- `server/app/game_tick_death.py`
- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/config/npc_config.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 246 (94%)
- INFERRED: 17 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*