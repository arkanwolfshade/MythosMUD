# PlayerCreationService

> 20 nodes

## Key Concepts

- **PlayerCreationService** (12 connections) — `server/game/player_creation_service.py`
- **.create_player_with_stats()** (8 connections) — `server/game/player_creation_service.py`
- **._build_new_player()** (7 connections) — `server/game/player_creation_service.py`
- **.create_player()** (7 connections) — `server/game/player_creation_service.py`
- **UUID** (6 connections)
- **._check_character_limit()** (5 connections) — `server/game/player_creation_service.py`
- **._resolve_tutorial_start_room()** (5 connections) — `server/game/player_creation_service.py`
- **._check_name_available()** (4 connections) — `server/game/player_creation_service.py`
- **.__init__()** (3 connections) — `server/game/player_creation_service.py`
- **Player** (2 connections)
- **Stats** (2 connections)
- **Any** (1 connections)
- **Reject character creation once a user has 3 active characters.** (1 connections) — `server/game/player_creation_service.py`
- **Reject character creation if the (case-insensitive) name is already taken.** (1 connections) — `server/game/player_creation_service.py`
- **Construct a new Player row (stats, tutorial placement, JSONB defaults) ready to…** (1 connections) — `server/game/player_creation_service.py`
- **Create a new player character with specific stats. Args: name: The player's…** (1 connections) — `server/game/player_creation_service.py`
- **Service for player creation operations.** (1 connections) — `server/game/player_creation_service.py`
- **Initialize with persistence layer, schema converter, and optional instance…** (1 connections) — `server/game/player_creation_service.py`
- **Resolve starting room and tutorial instance ID. For tutorial players, returns…** (1 connections) — `server/game/player_creation_service.py`
- **Create a new player character. Args: name: The player's name profession_id: The…** (1 connections) — `server/game/player_creation_service.py`

## Relationships

- [get_logger](get_logger.md) (7 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)

## Source Files

- `server/game/player_creation_service.py`

## Audit Trail

- EXTRACTED: 39 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*