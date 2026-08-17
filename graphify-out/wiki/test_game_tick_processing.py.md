# test_game_tick_processing.py

> 77 nodes

## Key Concepts

- **test_game_tick_processing.py** (72 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **asyncio** (26 connections)
- **game_tick_corpses.py** (20 connections) — `server/app/game_tick_corpses.py`
- **game_tick_loop()** (17 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (15 connections)
- **_validate_app_state_for_status_effects()** (14 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (12 connections) — `server/app/game_tick_processing.py`
- **process_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (11 connections) — `server/app/game_tick_corpses.py`
- **_app_container()** (10 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (10 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (10 connections) — `server/app/game_tick_processing.py`
- **_process_all_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (9 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_corpses.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_corpses.py`
- **process_npc_maintenance()** (8 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (8 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (7 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (6 connections) — `server/app/game_tick_corpses.py`
- **_CorpseLike** (3 connections) — `server/app/game_tick_corpses.py`
- **test_broadcast_tick_event()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_decayed_corpses_no_persistence()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_decayed_corpses_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 52 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (42 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (22 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (4 shared connections)
- [HolidayService](HolidayService.md) (4 shared connections)
- [get_tick_interval](get_tick_interval.md) (3 shared connections)
- [get_current_tick](get_current_tick.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [container_events.py](container_events.py.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 255 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*