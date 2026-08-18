# server app game tick corpses

> 29 nodes

## Key Concepts

- **test_game_tick_death.py** (27 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **game_tick_corpses.py** (21 connections) — `server/app/game_tick_corpses.py`
- **cleanup_decayed_corpses()** (12 connections) — `server/app/game_tick_corpses.py`
- **asyncio** (11 connections)
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_corpses.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_corpses.py`
- **_log_cleanup_results()** (7 connections) — `server/app/game_tick_corpses.py`
- **_CorpseLike** (3 connections) — `server/app/game_tick_corpses.py`
- **test_broadcast_tick_event()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_broadcast_tick_event_skips_when_no_players()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_cleanup_decayed_corpses_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_game_tick_loop_cancelled_on_sleep()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_dead_players_moves_to_limbo()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_dp_decay_and_death_with_session()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_mortally_wounded_death_threshold()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_mortally_wounded_skips_active_combat()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_passive_lucidity_flux()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_tick_online_players_counts_successes()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **FastAPI** (3 connections)
- **test_create_corpse_lifecycle_service()** (2 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_log_cleanup_results_warning_path()** (2 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_log_cleanup_results()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Protocol** (1 connections)
- **Decayed corpse cleanup for the game tick loop.** (1 connections) — `server/app/game_tick_corpses.py`
- **Create CorpseLifecycleService or None if persistence is unavailable.** (1 connections) — `server/app/game_tick_corpses.py`
- *... and 4 more nodes in this community*

## Relationships

- [server app game tick counter](server_app_game_tick_counter.md) (10 shared connections)
- [server app game tick status](server_app_game_tick_status.md) (7 shared connections)
- [server app game tick death](server_app_game_tick_death.md) (7 shared connections)
- [server services corpse lifecycle service](server_services_corpse_lifecycle_service.md) (4 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (3 shared connections)
- [server services container websocket events](server_services_container_websocket_events.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server models combat](server_models_combat.md) (2 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (1 shared connections)
- [server app lifespan startup legacy](server_app_lifespan_startup_legacy.md) (1 shared connections)
- [server async persistence](server_async_persistence.md) (1 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (1 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 88 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*