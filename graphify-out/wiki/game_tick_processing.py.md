# game_tick_processing.py

> 32 nodes

## Key Concepts

- **game_tick_processing.py** (56 connections) — `server/app/game_tick_processing.py`
- **game_tick_status_effects.py** (30 connections) — `server/app/game_tick_status_effects.py`
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
- **UUID** (2 connections)
- **Game tick processing functions. This module handles all game tick processing…** (1 connections) — `server/app/game_tick_processing.py`
- **Return currently online player UUIDs, or empty if no connection manager.** (1 connections) — `server/app/game_tick_protocols.py`
- **Status-effect processing for the game tick loop.** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process a single status effect. Returns: Tuple of (updated_effect_dict or None…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Update and save player status effects if changes occurred. Returns: True if…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Validate container and retrieve player by ID. Args: container: Application…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process all status effects for a player. Args: app: FastAPI application…** (1 connections) — `server/app/game_tick_status_effects.py`
- *... and 7 more nodes in this community*

## Relationships

- [game_tick_death.py](game_tick_death.py.md) (20 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (19 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (14 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (12 shared connections)
- [game_tick_protocols.py](game_tick_protocols.py.md) (10 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (8 shared connections)
- [coerce_int](coerce_int.md) (5 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (2 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/app/game_tick_status_effects.py`

## Audit Trail

- EXTRACTED: 148 (84%)
- INFERRED: 29 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*