# test_game_tick_processing.py

> 57 nodes

## Key Concepts

- **test_game_tick_processing.py** (72 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **get_mythos_chronicle()** (27 connections) — `server/time/time_service.py`
- **asyncio** (26 connections)
- **game_tick_corpses.py** (20 connections) — `server/app/game_tick_corpses.py`
- **game_tick_loop()** (17 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (12 connections) — `server/app/game_tick_processing.py`
- **process_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (11 connections) — `server/app/game_tick_corpses.py`
- **process_dp_decay_and_death()** (10 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (9 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_corpses.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_corpses.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (8 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (8 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (6 connections) — `server/app/game_tick_corpses.py`
- **_CorpseLike** (3 connections) — `server/app/game_tick_corpses.py`
- **test_broadcast_tick_event()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_decayed_corpses_no_persistence()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_decayed_corpses_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_single_decayed_corpse_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_game_tick_loop_cancelled_on_sleep()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_get_tick_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_all_status_effects_empty()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_casting_progress_calls_magic_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 32 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (52 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (9 shared connections)
- [_process_mortally_wounded_player](_process_mortally_wounded_player.md) (7 shared connections)
- [_process_mp_regeneration](_process_mp_regeneration.md) (6 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (4 shared connections)
- [lifespan.py](lifespan.py.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [reset_current_tick](reset_current_tick.md) (3 shared connections)
- [CombatInstance](CombatInstance.md) (3 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 237 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*