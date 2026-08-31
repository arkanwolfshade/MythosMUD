# PlayerSearchService

> 13 nodes

## Key Concepts

- **PlayerSearchService** (10 connections) — `server/game/player_search_service.py`
- **.resolve_player_name()** (4 connections) — `server/game/player_search_service.py`
- **.get_online_players()** (3 connections) — `server/game/player_search_service.py`
- **.__init__()** (3 connections) — `server/game/player_search_service.py`
- **.search_players_by_name()** (3 connections) — `server/game/player_search_service.py`
- **.validate_player_name()** (3 connections) — `server/game/player_search_service.py`
- **Any** (1 connections)
- **Search for players by name with fuzzy matching. This method returns multiple…** (1 connections) — `server/game/player_search_service.py`
- **Validate a player name for chat system use. This checks if the name is valid…** (1 connections) — `server/game/player_search_service.py`
- **Service for player search and validation operations.** (1 connections) — `server/game/player_search_service.py`
- **Initialize with a reference to the player service for data access.** (1 connections) — `server/game/player_search_service.py`
- **Resolve a player name with fuzzy matching and case-insensitive search. This…** (1 connections) — `server/game/player_search_service.py`
- **Get a list of currently online players. Note: This is a placeholder…** (1 connections) — `server/game/player_search_service.py`

## Relationships

- [api/character_creation.py](api-character_creation.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)

## Source Files

- `server/game/player_search_service.py`

## Audit Trail

- EXTRACTED: 19 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*