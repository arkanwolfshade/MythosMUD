# game_tick_status_effects.py

> 72 nodes

## Key Concepts

- **game_tick_status_effects.py** (32 connections) — `server/app/game_tick_status_effects.py`
- **game_tick_protocols.py** (31 connections) — `server/app/game_tick_protocols.py`
- **_TickContainer** (25 connections) — `server/app/game_tick_protocols.py`
- **_process_single_effect()** (14 connections) — `server/app/game_tick_status_effects.py`
- **_validate_app_state_for_status_effects()** (14 connections) — `server/app/game_tick_status_effects.py`
- **_process_damage_over_time_effect()** (13 connections) — `server/app/game_tick_status_effects.py`
- **process_status_effects()** (13 connections) — `server/app/game_tick_status_effects.py`
- **_process_heal_over_time_effect()** (11 connections) — `server/app/game_tick_status_effects.py`
- **process_player_effects_expiration()** (10 connections) — `server/app/game_tick_status_effects.py`
- **Protocol** (10 connections)
- **UUID** (10 connections)
- **_online_player_ids()** (9 connections) — `server/app/game_tick_protocols.py`
- **_process_all_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_update_player_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_validate_and_get_player()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_process_player_status_effects()** (8 connections) — `server/app/game_tick_status_effects.py`
- **FastAPI** (8 connections)
- **_TickCombatService** (6 connections) — `server/app/game_tick_protocols.py`
- **_TickDeathService** (6 connections) — `server/app/game_tick_protocols.py`
- **Player** (6 connections)
- **_TickConnectionManager** (5 connections) — `server/app/game_tick_protocols.py`
- **_TickCorruptionFlux** (5 connections) — `server/app/game_tick_protocols.py`
- **_TickMpRegen** (5 connections) — `server/app/game_tick_protocols.py`
- **_handle_login_warded_expirations()** (5 connections) — `server/app/game_tick_status_effects.py`
- **AsyncSession** (5 connections)
- *... and 47 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (35 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (25 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (13 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (5 shared connections)
- [coerce_int](coerce_int.md) (5 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (3 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/app/game_tick_protocols.py`
- `server/app/game_tick_status_effects.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 203 (87%)
- INFERRED: 30 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*