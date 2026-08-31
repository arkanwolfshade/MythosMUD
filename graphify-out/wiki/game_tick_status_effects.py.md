# game_tick_status_effects.py

> 71 nodes

## Key Concepts

- **game_tick_status_effects.py** (30 connections) — `server/app/game_tick_status_effects.py`
- **_TickContainer** (23 connections) — `server/app/game_tick_protocols.py`
- **test_game_tick_processing_async.py** (23 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **asyncio** (15 connections)
- **_process_single_effect()** (14 connections) — `server/app/game_tick_status_effects.py`
- **_validate_app_state_for_status_effects()** (14 connections) — `server/app/game_tick_status_effects.py`
- **_process_damage_over_time_effect()** (13 connections) — `server/app/game_tick_status_effects.py`
- **process_status_effects()** (13 connections) — `server/app/game_tick_status_effects.py`
- **_process_heal_over_time_effect()** (11 connections) — `server/app/game_tick_status_effects.py`
- **_process_all_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_update_player_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_validate_and_get_player()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_online_player_ids()** (8 connections) — `server/app/game_tick_protocols.py`
- **process_player_effects_expiration()** (8 connections) — `server/app/game_tick_status_effects.py`
- **_process_player_status_effects()** (8 connections) — `server/app/game_tick_status_effects.py`
- **FastAPI** (8 connections)
- **Player** (6 connections)
- **_TickConnectionManager** (5 connections) — `server/app/game_tick_protocols.py`
- **_handle_login_warded_expirations()** (5 connections) — `server/app/game_tick_status_effects.py`
- **test_process_combat_tick_no_service()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_combat_tick_success()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_no_damage()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_no_remaining()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_success()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_healing()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- *... and 46 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (19 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (16 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (12 shared connections)
- [game_tick_protocols.py](game_tick_protocols.py.md) (8 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (5 shared connections)
- [coerce_int](coerce_int.md) (5 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)

## Source Files

- `server/app/game_tick_protocols.py`
- `server/app/game_tick_status_effects.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 176 (86%)
- INFERRED: 29 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*