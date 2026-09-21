# game_tick_processing.py

> 34 nodes

## Key Concepts

- **game_tick_processing.py** (60 connections) — `server/app/game_tick_processing.py`
- **game_tick_status_effects.py** (32 connections) — `server/app/game_tick_status_effects.py`
- **_process_single_effect()** (14 connections) — `server/app/game_tick_status_effects.py`
- **_validate_app_state_for_status_effects()** (14 connections) — `server/app/game_tick_status_effects.py`
- **_process_damage_over_time_effect()** (13 connections) — `server/app/game_tick_status_effects.py`
- **process_status_effects()** (13 connections) — `server/app/game_tick_status_effects.py`
- **_process_heal_over_time_effect()** (11 connections) — `server/app/game_tick_status_effects.py`
- **process_player_effects_expiration()** (10 connections) — `server/app/game_tick_status_effects.py`
- **_process_all_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_update_player_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_validate_and_get_player()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_process_player_status_effects()** (8 connections) — `server/app/game_tick_status_effects.py`
- **FastAPI** (8 connections)
- **Player** (6 connections)
- **_TickConnectionManager** (5 connections) — `server/app/game_tick_protocols.py`
- **_handle_login_warded_expirations()** (5 connections) — `server/app/game_tick_status_effects.py`
- **_tick_broadcast_payload()** (4 connections) — `server/app/game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_container()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **UUID** (2 connections)
- **Game tick processing functions. This module handles all game tick processing…** (1 connections) — `server/app/game_tick_processing.py`
- **Build game_tick event payload (Mythos clock + calendar).** (1 connections) — `server/app/game_tick_processing.py`
- **Status-effect processing for the game tick loop.** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process a single status effect. Returns: Tuple of (updated_effect_dict or None…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Update and save player status effects if changes occurred. Returns: True if…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Validate container and retrieve player by ID. Args: container: Application…** (1 connections) — `server/app/game_tick_status_effects.py`
- *... and 9 more nodes in this community*

## Relationships

- [test_game_tick_processing.py](test_game_tick_processing.py.md) (27 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (20 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (14 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (11 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (8 shared connections)
- [Player](Player.md) (6 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (5 shared connections)
- [Protocol](Protocol.md) (2 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [NPCMaintenanceConfig](NPCMaintenanceConfig.md) (2 shared connections)
- [send_game_event](send_game_event.md) (2 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/app/game_tick_status_effects.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 154 (84%)
- INFERRED: 30 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*