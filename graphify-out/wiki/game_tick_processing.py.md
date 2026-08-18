# game_tick_processing.py

> 80 nodes

## Key Concepts

- **game_tick_processing.py** (56 connections) — `server/app/game_tick_processing.py`
- **game_tick_death.py** (34 connections) — `server/app/game_tick_death.py`
- **game_tick_status_effects.py** (30 connections) — `server/app/game_tick_status_effects.py`
- **game_tick_protocols.py** (28 connections) — `server/app/game_tick_protocols.py`
- **_TickContainer** (23 connections) — `server/app/game_tick_protocols.py`
- **_process_single_effect()** (14 connections) — `server/app/game_tick_status_effects.py`
- **_validate_app_state_for_status_effects()** (14 connections) — `server/app/game_tick_status_effects.py`
- **_app_container()** (13 connections) — `server/app/game_tick_protocols.py`
- **_process_damage_over_time_effect()** (13 connections) — `server/app/game_tick_status_effects.py`
- **process_status_effects()** (13 connections) — `server/app/game_tick_status_effects.py`
- **_process_mortally_wounded_player()** (12 connections) — `server/app/game_tick_death.py`
- **_process_mp_regeneration()** (11 connections) — `server/app/game_tick_death.py`
- **_process_heal_over_time_effect()** (11 connections) — `server/app/game_tick_status_effects.py`
- **process_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **_process_session_dp_decay_and_death()** (9 connections) — `server/app/game_tick_death.py`
- **_tick_online_players()** (9 connections) — `server/app/game_tick_protocols.py`
- **_process_all_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_update_player_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **Protocol** (9 connections)
- **UUID** (9 connections)
- **_handle_player_death_threshold()** (8 connections) — `server/app/game_tick_death.py`
- **_online_player_ids()** (8 connections) — `server/app/game_tick_protocols.py`
- **process_player_effects_expiration()** (8 connections) — `server/app/game_tick_status_effects.py`
- **_process_player_status_effects()** (8 connections) — `server/app/game_tick_status_effects.py`
- **FastAPI** (8 connections)
- *... and 55 more nodes in this community*

## Relationships

- [test_game_tick_processing.py](test_game_tick_processing.py.md) (37 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (15 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (14 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [coerce_int](coerce_int.md) (8 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (8 shared connections)
- [_TickDeathService](_TickDeathService.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [get_current_tick](get_current_tick.md) (4 shared connections)
- [CombatParticipant](CombatParticipant.md) (3 shared connections)
- [Player](Player.md) (3 shared connections)
- [LucidityService](LucidityService.md) (3 shared connections)

## Source Files

- `server/app/game_tick_death.py`
- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/app/game_tick_status_effects.py`

## Audit Trail

- EXTRACTED: 285 (89%)
- INFERRED: 36 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*