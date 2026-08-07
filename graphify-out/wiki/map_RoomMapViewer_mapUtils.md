# map RoomMapViewer mapUtils

> 48 nodes

## Key Concepts

- **test_game_tick_processing.py** (69 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **FastAPI** (16 connections)
- **game_tick_loop()** (16 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (11 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (10 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (9 connections) — `server/app/game_tick_processing.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_all_status_effects()** (8 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (7 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_passive_lucidity_flux()** (6 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (6 connections) — `server/app/game_tick_processing.py`
- **.should_run_maintenance()** (3 connections) — `server/config/npc_config.py`
- **test_get_tick_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_log_cleanup_results()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_and_get_player_invalid_id()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_and_get_player_success()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_all_status_effects_empty()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_casting_progress_calls_magic_service()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_npc_maintenance_runs_on_interval()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_decayed_corpses_no_persistence()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_dp_decay_and_death_no_service()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 23 more nodes in this community*

## Relationships

- [schemas calendar rationale](schemas_calendar_rationale.md) (33 shared connections)
- [command helpers functions](command_helpers_functions.md) (22 shared connections)
- [database config helpers](database_config_helpers.md) (8 shared connections)
- [commands rest command](commands_rest_command.md) (4 shared connections)
- [game skill service](game_skill_service.md) (3 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [command utility models](command_utility_models.md) (2 shared connections)
- [aggro threat services](aggro_threat_services.md) (2 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (1 shared connections)
- [useWebSocketConnectionTestFixtures useWe](useWebSocketConnectionTestFixtures_useWe.md) (1 shared connections)
- [Game Terminal UI](Game_Terminal_UI.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/config/npc_config.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 245 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*