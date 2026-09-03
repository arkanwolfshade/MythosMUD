# Test Game Tick Death

> 35 nodes

## Key Concepts

- **test_game_tick_death.py** (28 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **get_mythos_chronicle()** (26 connections) — `server/time/time_service.py`
- **game_tick_corpses.py** (21 connections) — `server/app/game_tick_corpses.py`
- **cleanup_decayed_corpses()** (12 connections) — `server/app/game_tick_corpses.py`
- **asyncio** (12 connections)
- **_tick_online_players()** (9 connections) — `server/app/game_tick_protocols.py`
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_corpses.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_corpses.py`
- **_log_cleanup_results()** (7 connections) — `server/app/game_tick_corpses.py`
- **test_process_mortally_wounded_publishes_dp_decay_to_nats()** (4 connections) — `server/tests/unit/app/test_game_tick_death.py`
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
- *... and 10 more nodes in this community*

## Relationships

- [Game Tick Processing](Game_Tick_Processing.md) (12 shared connections)
- [Test Game Tick Processing](Test_Game_Tick_Processing.md) (7 shared connections)
- [Game Tick Death](Game_Tick_Death.md) (7 shared connections)
- [Time Service](Time_Service.md) (7 shared connections)
- [Test Corpse Lifecycle Service](Test_Corpse_Lifecycle_Service.md) (4 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (4 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (4 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (4 shared connections)
- [Game Tick Protocols](Game_Tick_Protocols.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Test Container Websocket Events](Test_Container_Websocket_Events.md) (2 shared connections)
- [Game Tick Status Effects](Game_Tick_Status_Effects.md) (2 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/app/game_tick_protocols.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 122 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*