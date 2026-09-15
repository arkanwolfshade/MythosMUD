# game_tick_processing.py

> 192 nodes

## Key Concepts

- **game_tick_processing.py** (57 connections) — `server/app/game_tick_processing.py`
- **game_tick_death.py** (38 connections) — `server/app/game_tick_death.py`
- **test_game_tick_processing.py** (38 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **game_tick_protocols.py** (31 connections) — `server/app/game_tick_protocols.py`
- **game_tick_status_effects.py** (30 connections) — `server/app/game_tick_status_effects.py`
- **_TickContainer** (24 connections) — `server/app/game_tick_protocols.py`
- **test_game_tick_processing_async.py** (21 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **game_tick_loop()** (17 connections) — `server/app/game_tick_processing.py`
- **asyncio** (17 connections)
- **get_current_tick()** (16 connections) — `server/app/game_tick_counter.py`
- **asyncio** (15 connections)
- **_process_mortally_wounded_player()** (14 connections) — `server/app/game_tick_death.py`
- **_process_single_effect()** (14 connections) — `server/app/game_tick_status_effects.py`
- **_validate_app_state_for_status_effects()** (14 connections) — `server/app/game_tick_status_effects.py`
- **broadcast_tick_event()** (13 connections) — `server/app/game_tick_processing.py`
- **_app_container()** (13 connections) — `server/app/game_tick_protocols.py`
- **_process_damage_over_time_effect()** (13 connections) — `server/app/game_tick_status_effects.py`
- **process_status_effects()** (13 connections) — `server/app/game_tick_status_effects.py`
- **_process_mp_regeneration()** (11 connections) — `server/app/game_tick_death.py`
- **_process_passive_corruption_flux()** (11 connections) — `server/app/game_tick_death.py`
- **_process_heal_over_time_effect()** (11 connections) — `server/app/game_tick_status_effects.py`
- **process_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **_process_session_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **process_combat_tick()** (10 connections) — `server/app/game_tick_processing.py`
- **_tick_online_players()** (10 connections) — `server/app/game_tick_protocols.py`
- *... and 167 more nodes in this community*

## Relationships

- [test_game_tick_death.py](test_game_tick_death.py.md) (34 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (11 shared connections)
- [coerce_int](coerce_int.md) (10 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [Player](Player.md) (6 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (5 shared connections)
- [players.py](players.py.md) (4 shared connections)
- [event_handler.py](event_handler.py.md) (4 shared connections)
- [combat_attack.py](combat_attack.py.md) (3 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (3 shared connections)
- [send_game_event](send_game_event.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/app/game_tick_death.py`
- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/app/game_tick_status_effects.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 499 (91%)
- INFERRED: 48 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*