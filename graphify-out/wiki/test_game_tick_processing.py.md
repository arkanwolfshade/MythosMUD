# test_game_tick_processing.py

> 27 nodes

## Key Concepts

- **test_game_tick_processing.py** (69 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **cleanup_decayed_corpses()** (10 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (6 connections) — `server/app/game_tick_processing.py`
- **reset_current_tick()** (6 connections) — `server/app/game_tick_processing.py`
- **_validate_mp_regeneration_services()** (5 connections) — `server/app/game_tick_processing.py`
- **test_get_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_reset_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_decayed_corpses_no_persistence()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_decayed_corpses_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_single_decayed_corpse_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_get_tick_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_create_corpse_lifecycle_service()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_log_cleanup_results()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_log_cleanup_results_warning_path()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_mp_regeneration_services()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Validate that required services exist for MP regeneration. Args: container:…** (1 connections) — `server/app/game_tick_processing.py`
- **Reset the current tick for testing.** (1 connections) — `server/app/game_tick_processing.py`
- **Create and initialize CorpseLifecycleService. Args: app: FastAPI application…** (1 connections) — `server/app/game_tick_processing.py`
- **Cleanup a single decayed corpse. Args: corpse_service: Corpse lifecycle service…** (1 connections) — `server/app/game_tick_processing.py`
- **Log the results of corpse cleanup. Args: tick_count: Current game tick count…** (1 connections) — `server/app/game_tick_processing.py`
- **Cleanup decayed corpse containers (every 60 ticks = 1 minute).** (1 connections) — `server/app/game_tick_processing.py`
- **Unit tests for game tick processing functions. Tests the game tick processing…** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test get_current_tick returns the current tick value.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 2 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (25 shared connections)
- [_process_mortally_wounded_player](_process_mortally_wounded_player.md) (12 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (8 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [_validate_app_state_for_status_effects](_validate_app_state_for_status_effects.md) (7 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (2 shared connections)
- [process_npc_maintenance](process_npc_maintenance.md) (2 shared connections)
- [_update_player_status_effects](_update_player_status_effects.md) (2 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (1 shared connections)
- [MythosChronicle](MythosChronicle.md) (1 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 112 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*