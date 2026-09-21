# game_tick_processing.py

> 124 nodes

## Key Concepts

- **game_tick_processing.py** (60 connections) — `server/app/game_tick_processing.py`
- **game_tick_death.py** (38 connections) — `server/app/game_tick_death.py`
- **game_tick_status_effects.py** (32 connections) — `server/app/game_tick_status_effects.py`
- **test_game_tick_death.py** (32 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **game_tick_protocols.py** (31 connections) — `server/app/game_tick_protocols.py`
- **_TickContainer** (24 connections) — `server/app/game_tick_protocols.py`
- **asyncio** (18 connections)
- **_process_mortally_wounded_player()** (14 connections) — `server/app/game_tick_death.py`
- **_app_container()** (14 connections) — `server/app/game_tick_protocols.py`
- **_process_single_effect()** (14 connections) — `server/app/game_tick_status_effects.py`
- **_validate_app_state_for_status_effects()** (14 connections) — `server/app/game_tick_status_effects.py`
- **broadcast_tick_event()** (13 connections) — `server/app/game_tick_processing.py`
- **_process_damage_over_time_effect()** (13 connections) — `server/app/game_tick_status_effects.py`
- **process_status_effects()** (13 connections) — `server/app/game_tick_status_effects.py`
- **_process_mp_regeneration()** (11 connections) — `server/app/game_tick_death.py`
- **_process_passive_corruption_flux()** (11 connections) — `server/app/game_tick_death.py`
- **_process_heal_over_time_effect()** (11 connections) — `server/app/game_tick_status_effects.py`
- **process_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **_process_session_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **_tick_online_players()** (10 connections) — `server/app/game_tick_protocols.py`
- **process_player_effects_expiration()** (10 connections) — `server/app/game_tick_status_effects.py`
- **Protocol** (10 connections)
- **UUID** (10 connections)
- **_process_single_player_room_flux()** (9 connections) — `server/app/game_tick_death.py`
- **_online_player_ids()** (9 connections) — `server/app/game_tick_protocols.py`
- *... and 99 more nodes in this community*

## Relationships

- [test_game_tick_processing.py](test_game_tick_processing.py.md) (59 shared connections)
- [coerce_int](coerce_int.md) (11 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (10 shared connections)
- [MythosChronicle](MythosChronicle.md) (10 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [Player](Player.md) (7 shared connections)
- [get_config](get_config.md) (6 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (5 shared connections)
- [combat_service.py](combat_service.py.md) (4 shared connections)
- [DatabaseManager](DatabaseManager.md) (3 shared connections)
- [send_game_event](send_game_event.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)

## Source Files

- `server/app/game_tick_death.py`
- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/app/game_tick_status_effects.py`
- `server/tests/unit/app/test_game_tick_death.py`

## Audit Trail

- EXTRACTED: 392 (90%)
- INFERRED: 45 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*