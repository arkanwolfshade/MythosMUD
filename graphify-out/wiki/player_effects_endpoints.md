# player effects endpoints

> 15 nodes

## Key Concepts

- **player_effects.py** (30 connections) — `server/api/player_effects.py`
- **EffectResponse** (12 connections) — `server/schemas/players/player_effects.py`
- **apply_fear()** (11 connections) — `server/api/player_effects.py`
- **apply_corruption()** (11 connections) — `server/api/player_effects.py`
- **damage_player()** (11 connections) — `server/api/player_effects.py`
- **UUID** (7 connections)
- **FastAPIRequest** (6 connections)
- **player_effects.py** (3 connections) — `server/schemas/players/player_effects.py`
- **Player effects API endpoints.  This module handles endpoints for applying variou** (1 connections) — `server/api/player_effects.py`
- **Apply fear to a player.** (1 connections) — `server/api/player_effects.py`
- **Apply corruption to a player.** (1 connections) — `server/api/player_effects.py`
- **Damage a player's health.** (1 connections) — `server/api/player_effects.py`
- **BaseModel** (1 connections)
- **Player effects API response schemas for MythosMUD server.  This module provides** (1 connections) — `server/schemas/players/player_effects.py`
- **Response model for player effect endpoints (lucidity loss, fear, corruption, etc** (1 connections) — `server/schemas/players/player_effects.py`

## Relationships

- [player schemas requests](player_schemas_requests.md) (12 shared connections)
- [auth users rationale](auth_users_rationale.md) (6 shared connections)
- [npc lifecycle combat](npc_lifecycle_combat.md) (5 shared connections)
- [combat messaging service](combat_messaging_service.md) (5 shared connections)
- [Player Stats](Player_Stats.md) (4 shared connections)
- [Exception Containers](Exception_Containers.md) (4 shared connections)
- [magic healing game](magic_healing_game.md) (4 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (2 shared connections)
- [player requests schemas](player_requests_schemas.md) (2 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (2 shared connections)

## Source Files

- `server/api/player_effects.py`
- `server/schemas/players/player_effects.py`

## Audit Trail

- EXTRACTED: 98 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*