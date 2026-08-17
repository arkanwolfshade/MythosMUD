# test_game_tick_processing.py

> 82 nodes

## Key Concepts

- **test_game_tick_processing.py** (56 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **asyncio** (26 connections)
- **game_tick_loop()** (17 connections) — `server/app/game_tick_processing.py`
- **_app_container()** (13 connections) — `server/app/game_tick_protocols.py`
- **broadcast_tick_event()** (12 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (11 connections) — `server/app/game_tick_corpses.py`
- **process_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **process_combat_tick()** (10 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_corpses.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_corpses.py`
- **process_npc_maintenance()** (8 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (7 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (6 connections) — `server/app/game_tick_corpses.py`
- **reset_current_tick()** (6 connections) — `server/app/game_tick_counter.py`
- **FastAPI** (6 connections)
- **set_current_tick()** (5 connections) — `server/app/game_tick_counter.py`
- **test_get_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_single_player_mp_regeneration()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_reset_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **_CorpseLike** (3 connections) — `server/app/game_tick_corpses.py`
- **.should_run_maintenance()** (3 connections) — `server/config/npc_config.py`
- **test_broadcast_tick_event()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_decayed_corpses_no_persistence()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_decayed_corpses_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_single_decayed_corpse_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 57 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (42 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (11 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (3 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (2 shared connections)
- [container_events.py](container_events.py.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/app/game_tick_counter.py`
- `server/app/game_tick_death.py`
- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/config/npc_config.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 190 (87%)
- INFERRED: 28 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*