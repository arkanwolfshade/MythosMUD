# game_tick_processing.py

> 69 nodes

## Key Concepts

- **game_tick_processing.py** (79 connections) — `server/app/game_tick_processing.py`
- **get_mythos_chronicle()** (24 connections) — `server/time/time_service.py`
- **FastAPI** (16 connections)
- **test_game_tick_processing.py** (15 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **game_tick_loop()** (14 connections) — `server/app/game_tick_processing.py`
- **_validate_app_state_for_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (9 connections) — `server/app/game_tick_processing.py`
- **process_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (7 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (6 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_all_status_effects()** (6 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (6 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (6 connections) — `server/app/game_tick_processing.py`
- **reset_current_tick()** (6 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (5 connections) — `server/app/game_tick_processing.py`
- **passive_lucidity_flux_service.py** (5 connections) — `server/services/passive_lucidity_flux_service.py`
- **process_casting_progress()** (4 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (4 connections) — `server/app/game_tick_processing.py`
- **test_get_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_reset_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **_log_cleanup_results()** (3 connections) — `server/app/game_tick_processing.py`
- *... and 44 more nodes in this community*

## Relationships

- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (18 shared connections)
- [_process_session_dp_decay_and_death](_process_session_dp_decay_and_death.md) (10 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [lifespan.py](lifespan.py.md) (6 shared connections)
- [ScheduleService](ScheduleService.md) (5 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (4 shared connections)
- [CombatParticipant](CombatParticipant.md) (4 shared connections)
- [send_game_event](send_game_event.md) (3 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (3 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [lifecycle_periodic.py](lifecycle_periodic.py.md) (3 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/config/npc_config.py`
- `server/services/passive_lucidity_flux_service.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 221 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*