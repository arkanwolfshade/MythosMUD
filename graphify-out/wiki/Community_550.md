# Community 550

> 31 nodes

## Key Concepts

- **game_tick_processing.py** (60 connections) — `server/app/game_tick_processing.py`
- **game_tick_status_effects.py** (24 connections) — `server/app/game_tick_status_effects.py`
- **_process_single_effect()** (14 connections) — `server/app/game_tick_status_effects.py`
- **_validate_app_state_for_status_effects()** (13 connections) — `server/app/game_tick_status_effects.py`
- **_process_damage_over_time_effect()** (12 connections) — `server/app/game_tick_status_effects.py`
- **_process_heal_over_time_effect()** (11 connections) — `server/app/game_tick_status_effects.py`
- **process_status_effects()** (11 connections) — `server/app/game_tick_status_effects.py`
- **_process_all_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **process_player_effects_expiration()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_update_player_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_validate_and_get_player()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_process_player_status_effects()** (8 connections) — `server/app/game_tick_status_effects.py`
- **FastAPI** (8 connections)
- **_TickContainer** (8 connections)
- **Player** (6 connections)
- **_handle_login_warded_expirations()** (4 connections) — `server/app/game_tick_status_effects.py`
- **UUID** (2 connections)
- **_TickConnectionManager** (1 connections)
- **Game tick processing functions. This module handles all game tick processing…** (1 connections) — `server/app/game_tick_processing.py`
- **Status-effect processing for the game tick loop.** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process a single status effect. Returns: Tuple of (updated_effect_dict or None…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Update and save player status effects if changes occurred. Returns: True if…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Validate container and retrieve player by ID. Args: container: Application…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process all status effects for a player. Args: app: FastAPI application…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process status effects for a single player. Returns: True if player was…** (1 connections) — `server/app/game_tick_status_effects.py`
- *... and 6 more nodes in this community*

## Relationships

- [Community 380](Community_380.md) (20 shared connections)
- [Community 425](Community_425.md) (15 shared connections)
- [Community 893](Community_893.md) (10 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (10 shared connections)
- [Community 490](Community_490.md) (9 shared connections)
- [Community 441](Community_441.md) (4 shared connections)
- [Community 46](Community_46.md) (4 shared connections)
- [Community 1107](Community_1107.md) (4 shared connections)
- [Community 95](Community_95.md) (3 shared connections)
- [Community 412](Community_412.md) (3 shared connections)
- [Community 53](Community_53.md) (2 shared connections)
- [Community 41](Community_41.md) (2 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/app/game_tick_status_effects.py`

## Audit Trail

- EXTRACTED: 132 (81%)
- INFERRED: 30 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*