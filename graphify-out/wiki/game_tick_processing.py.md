# game_tick_processing.py

> 133 nodes

## Key Concepts

- **game_tick_processing.py** (79 connections) — `server/app/game_tick_processing.py`
- **test_game_tick_processing_async.py** (26 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **FastAPI** (16 connections)
- **get_current_tick()** (15 connections) — `server/app/game_tick_processing.py`
- **test_game_tick_processing.py** (15 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **asyncio** (15 connections)
- **game_tick_loop()** (14 connections) — `server/app/game_tick_processing.py`
- **_validate_app_state_for_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **_process_single_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **_process_damage_over_time_effect()** (10 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (9 connections) — `server/app/game_tick_processing.py`
- **process_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_heal_over_time_effect()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_session_dp_decay_and_death()** (8 connections) — `server/app/game_tick_processing.py`
- **Any** (8 connections)
- **cleanup_decayed_corpses()** (7 connections) — `server/app/game_tick_processing.py`
- **_handle_player_death_threshold()** (7 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_player()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_update_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **AsyncSession** (7 connections)
- **_cleanup_single_decayed_corpse()** (6 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (6 connections) — `server/app/game_tick_processing.py`
- *... and 108 more nodes in this community*

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (9 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [lifespan.py](lifespan.py.md) (5 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [MythosChronicle](MythosChronicle.md) (4 shared connections)
- [send_game_event](send_game_event.md) (3 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (3 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (3 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [coerce_int](coerce_int.md) (3 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 311 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*