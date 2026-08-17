# test_game_tick_processing.py

> 83 nodes

## Key Concepts

- **test_game_tick_processing.py** (40 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_game_tick_death.py** (23 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **game_tick_corpses.py** (21 connections) — `server/app/game_tick_corpses.py`
- **game_tick_loop()** (17 connections) — `server/app/game_tick_processing.py`
- **asyncio** (17 connections)
- **cleanup_decayed_corpses()** (12 connections) — `server/app/game_tick_corpses.py`
- **broadcast_tick_event()** (12 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (10 connections) — `server/app/game_tick_processing.py`
- **asyncio** (9 connections)
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_corpses.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_corpses.py`
- **process_npc_maintenance()** (8 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (7 connections) — `server/app/game_tick_corpses.py`
- **process_casting_progress()** (7 connections) — `server/app/game_tick_processing.py`
- **reset_current_tick()** (6 connections) — `server/app/game_tick_counter.py`
- **FastAPI** (6 connections)
- **set_current_tick()** (5 connections) — `server/app/game_tick_counter.py`
- **test_get_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_single_player_mp_regeneration()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_reset_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **_CorpseLike** (3 connections) — `server/app/game_tick_corpses.py`
- **.should_run_maintenance()** (3 connections) — `server/config/npc_config.py`
- **test_broadcast_tick_event()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_cleanup_decayed_corpses_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_game_tick_loop_cancelled_on_sleep()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- *... and 58 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (44 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [combat_service_attack.py](combat_service_attack.py.md) (4 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (3 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/app/game_tick_counter.py`
- `server/app/game_tick_processing.py`
- `server/config/npc_config.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 194 (87%)
- INFERRED: 29 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*