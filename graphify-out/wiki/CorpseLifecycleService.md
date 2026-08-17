# corpselifecycleservice

> 37 nodes

## Key Concepts

- **test_game_tick_death.py** (22 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **game_tick_loop()** (17 connections) — `server/app/game_tick_processing.py`
- **game_tick_corpses.py** (15 connections) — `server/app/game_tick_corpses.py`
- **cleanup_decayed_corpses()** (12 connections) — `server/app/game_tick_corpses.py`
- **broadcast_tick_event()** (9 connections) — `server/app/game_tick_processing.py`
- **asyncio** (9 connections)
- **_cleanup_single_decayed_corpse()** (7 connections) — `server/app/game_tick_corpses.py`
- **_create_corpse_lifecycle_service()** (7 connections) — `server/app/game_tick_corpses.py`
- **_log_cleanup_results()** (7 connections) — `server/app/game_tick_corpses.py`
- **process_casting_progress()** (7 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (7 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (6 connections)
- **_CorpseLike** (3 connections) — `server/app/game_tick_corpses.py`
- **test_broadcast_tick_event()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_cleanup_decayed_corpses_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_game_tick_loop_cancelled_on_sleep()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_dead_players_moves_to_limbo()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_dp_decay_and_death_with_session()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_mortally_wounded_death_threshold()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_mortally_wounded_skips_active_combat()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_passive_lucidity_flux()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **FastAPI** (3 connections)
- **test_create_corpse_lifecycle_service()** (2 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_log_cleanup_results_warning_path()** (2 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_log_cleanup_results()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 12 more nodes in this community*

## Relationships

- [server app game tick processing](server_app_game_tick_processing.md) (12 shared connections)
- [server app game tick status](server_app_game_tick_status.md) (11 shared connections)
- [playerdpupdated](playerdpupdated.md) (9 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (2 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (2 shared connections)
- [server app lifespan](server_app_lifespan.md) (2 shared connections)
- [server api players](server_api_players.md) (1 shared connections)
- [holidayresolver](holidayresolver.md) (1 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 105 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*