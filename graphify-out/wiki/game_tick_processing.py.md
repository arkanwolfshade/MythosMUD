# game_tick_processing.py

> 77 nodes

## Key Concepts

- **game_tick_processing.py** (55 connections) — `server/app/game_tick_processing.py`
- **game_tick_death.py** (34 connections) — `server/app/game_tick_death.py`
- **game_tick_status_effects.py** (29 connections) — `server/app/game_tick_status_effects.py`
- **_TickContainer** (23 connections) — `server/app/game_tick_protocols.py`
- **game_tick_protocols.py** (23 connections) — `server/app/game_tick_protocols.py`
- **_process_single_effect()** (14 connections) — `server/app/game_tick_status_effects.py`
- **_validate_app_state_for_status_effects()** (14 connections) — `server/app/game_tick_status_effects.py`
- **_app_container()** (13 connections) — `server/app/game_tick_protocols.py`
- **_process_damage_over_time_effect()** (13 connections) — `server/app/game_tick_status_effects.py`
- **_process_mortally_wounded_player()** (12 connections) — `server/app/game_tick_death.py`
- **_process_heal_over_time_effect()** (11 connections) — `server/app/game_tick_status_effects.py`
- **process_status_effects()** (11 connections) — `server/app/game_tick_status_effects.py`
- **process_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **_process_mp_regeneration()** (9 connections) — `server/app/game_tick_death.py`
- **_process_session_dp_decay_and_death()** (9 connections) — `server/app/game_tick_death.py`
- **_process_all_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_update_player_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_validate_and_get_player()** (9 connections) — `server/app/game_tick_status_effects.py`
- **Protocol** (9 connections)
- **FastAPI** (9 connections)
- **_handle_player_death_threshold()** (8 connections) — `server/app/game_tick_death.py`
- **process_player_effects_expiration()** (8 connections) — `server/app/game_tick_status_effects.py`
- **_process_player_status_effects()** (8 connections) — `server/app/game_tick_status_effects.py`
- **_process_dead_players()** (7 connections) — `server/app/game_tick_death.py`
- **_process_passive_lucidity_flux()** (7 connections) — `server/app/game_tick_death.py`
- *... and 52 more nodes in this community*

## Relationships

- [test_game_tick_processing.py](test_game_tick_processing.py.md) (44 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (14 shared connections)
- [coerce_int](coerce_int.md) (10 shared connections)
- [UUID](UUID.md) (8 shared connections)
- [pytest.md](pytest.md.md) (6 shared connections)
- [login_grace_period.py](login_grace_period.py.md) (4 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (2 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)

## Source Files

- `server/app/game_tick_death.py`
- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/app/game_tick_status_effects.py`

## Audit Trail

- EXTRACTED: 268 (88%)
- INFERRED: 38 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*