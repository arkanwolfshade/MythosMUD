# PlayerRead

> 31 nodes

## Key Concepts

- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **PlayerCreationService** (9 connections) — `server/game/player_creation_service.py`
- **.create_player_with_stats()** (8 connections) — `server/game/player_creation_service.py`
- **.create_player()** (7 connections) — `server/game/player_creation_service.py`
- **._resolve_tutorial_start_room()** (5 connections) — `server/game/player_creation_service.py`
- **UUID** (4 connections)
- **.__init__()** (3 connections) — `server/game/player_creation_service.py`
- **.get_online_players()** (3 connections) — `server/game/player_search_service.py`
- **.search_players_by_name()** (3 connections) — `server/game/player_search_service.py`
- **.get_online_players()** (3 connections) — `server/game/player_service.py`
- **.get_player_by_name()** (3 connections) — `server/game/player_service.py`
- **.list_players()** (3 connections) — `server/game/player_service.py`
- **.resolve_player_name()** (3 connections) — `server/game/player_service.py`
- **.search_players_by_name()** (3 connections) — `server/game/player_service.py`
- **.resolve_player_name()** (3 connections) — `server/services/target_resolution_service.py`
- **Any** (1 connections)
- **Stats** (1 connections)
- **Create a new player character with specific stats. Args: name: The player's…** (1 connections) — `server/game/player_creation_service.py`
- **Service for player creation operations.** (1 connections) — `server/game/player_creation_service.py`
- **Initialize with persistence layer, schema converter, and optional instance…** (1 connections) — `server/game/player_creation_service.py`
- **Resolve starting room and tutorial instance ID. For tutorial players, returns…** (1 connections) — `server/game/player_creation_service.py`
- **Create a new player character. Args: name: The player's name profession_id: The…** (1 connections) — `server/game/player_creation_service.py`
- **Search for players by name with fuzzy matching. This method returns multiple…** (1 connections) — `server/game/player_search_service.py`
- **Get a list of currently online players. Note: This is a placeholder…** (1 connections) — `server/game/player_search_service.py`
- **Get a player by their name. Args: player_name: The player's name Returns:…** (1 connections) — `server/game/player_service.py`
- *... and 6 more nodes in this community*

## Relationships

- [PlayerService](PlayerService.md) (19 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (6 shared connections)
- [test_player_schemas.py](test_player_schemas.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [server/models/game.py](server-models-game.py.md) (4 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (2 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)
- [players/__init__.py](players-__init__.py.md) (1 shared connections)
- [Stats](Stats.md) (1 shared connections)

## Source Files

- `server/game/player_creation_service.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/schemas/players/player.py`
- `server/services/target_resolution_service.py`

## Audit Trail

- EXTRACTED: 83 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*