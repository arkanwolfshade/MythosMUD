# lucidity commands services

> 13 nodes

## Key Concepts

- **PlayerCreationService** (9 connections) — `server/game/player_creation_service.py`
- **.create_player_with_stats()** (9 connections) — `server/game/player_creation_service.py`
- **.create_player()** (8 connections) — `server/game/player_creation_service.py`
- **._resolve_tutorial_start_room()** (5 connections) — `server/game/player_creation_service.py`
- **UUID** (4 connections)
- **.__init__()** (3 connections) — `server/game/player_creation_service.py`
- **Any** (1 connections)
- **Stats** (1 connections)
- **Service for player creation operations.** (1 connections) — `server/game/player_creation_service.py`
- **Initialize with persistence layer, schema converter, and optional instance manag** (1 connections) — `server/game/player_creation_service.py`
- **Resolve starting room and tutorial instance ID.          For tutorial players, r** (1 connections) — `server/game/player_creation_service.py`
- **Create a new player character.          Args:             name: The player's nam** (1 connections) — `server/game/player_creation_service.py`
- **Create a new player character with specific stats.          Args:             na** (1 connections) — `server/game/player_creation_service.py`

## Relationships

- [Loot Generation](Loot_Generation.md) (5 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)

## Source Files

- `server/game/player_creation_service.py`

## Audit Trail

- EXTRACTED: 42 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*