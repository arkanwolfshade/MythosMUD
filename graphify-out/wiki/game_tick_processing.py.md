# game_tick_processing.py

> 44 nodes

## Key Concepts

- **game_tick_processing.py** (83 connections) — `server/app/game_tick_processing.py`
- **_TickContainer** (20 connections) — `server/app/game_tick_processing.py`
- **_process_single_effect()** (15 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (15 connections)
- **_process_damage_over_time_effect()** (14 connections) — `server/app/game_tick_processing.py`
- **_validate_app_state_for_status_effects()** (14 connections) — `server/app/game_tick_processing.py`
- **_app_container()** (10 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (10 connections) — `server/app/game_tick_processing.py`
- **_process_all_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **_process_session_dp_decay_and_death()** (9 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (8 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_dead_players()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_passive_lucidity_flux()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_players()** (6 connections) — `server/app/game_tick_processing.py`
- **_player_in_active_combat()** (5 connections) — `server/app/game_tick_processing.py`
- **test_process_dead_players_moves_to_limbo()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_passive_lucidity_flux()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_connection_manager_is_none()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_container_is_none()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_async_persistence()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_connection_manager()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_container()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_valid()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Game tick processing functions. This module handles all game tick processing…** (1 connections) — `server/app/game_tick_processing.py`
- *... and 19 more nodes in this community*

## Relationships

- [test_game_tick_processing.py](test_game_tick_processing.py.md) (52 shared connections)
- [_process_mortally_wounded_player](_process_mortally_wounded_player.md) (24 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (18 shared connections)
- [_process_mp_regeneration](_process_mp_regeneration.md) (6 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [coerce_int](coerce_int.md) (4 shared connections)
- [CombatInstance](CombatInstance.md) (4 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (2 shared connections)
- [NPCMaintenanceConfig](NPCMaintenanceConfig.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [connection_manager_api.py](connection_manager_api.py.md) (2 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 212 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*