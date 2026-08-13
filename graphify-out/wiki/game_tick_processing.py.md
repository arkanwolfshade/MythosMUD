# game_tick_processing.py

> 107 nodes

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
- **Any** (8 connections)
- **cleanup_decayed_corpses()** (7 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_update_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (6 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_all_status_effects()** (6 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (6 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (6 connections) — `server/app/game_tick_processing.py`
- **reset_current_tick()** (6 connections) — `server/app/game_tick_processing.py`
- *... and 82 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [_process_session_dp_decay_and_death](_process_session_dp_decay_and_death.md) (12 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (9 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (8 shared connections)
- [lifespan.py](lifespan.py.md) (5 shared connections)
- [players.py](players.py.md) (5 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (4 shared connections)
- [Player](Player.md) (4 shared connections)
- [send_game_event](send_game_event.md) (3 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (3 shared connections)
- [lifecycle_periodic.py](lifecycle_periodic.py.md) (3 shared connections)
- [mock_app](mock_app.md) (3 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 278 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*