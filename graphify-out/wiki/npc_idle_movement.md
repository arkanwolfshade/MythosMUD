# npc idle movement

> 15 nodes

## Key Concepts

- **PlayerSearchService** (10 connections) — `server/game/player_search_service.py`
- **.__init__()** (8 connections) — `server/game/player_service.py`
- **.resolve_player_name()** (4 connections) — `server/game/player_search_service.py`
- **.__init__()** (3 connections) — `server/game/player_search_service.py`
- **.get_online_players()** (3 connections) — `server/game/player_search_service.py`
- **.search_players_by_name()** (3 connections) — `server/game/player_search_service.py`
- **.validate_player_name()** (3 connections) — `server/game/player_search_service.py`
- **Any** (1 connections)
- **Service for player search and validation operations.** (1 connections) — `server/game/player_search_service.py`
- **Initialize with a reference to the player service for data access.** (1 connections) — `server/game/player_search_service.py`
- **Resolve a player name with fuzzy matching and case-insensitive search.** (1 connections) — `server/game/player_search_service.py`
- **Get a list of currently online players.          Note: This is a placeholder imp** (1 connections) — `server/game/player_search_service.py`
- **Search for players by name with fuzzy matching.          This method returns mul** (1 connections) — `server/game/player_search_service.py`
- **Validate a player name for chat system use.          This checks if the name is** (1 connections) — `server/game/player_search_service.py`
- **Initialize the player service with a persistence layer and optional combat servi** (1 connections) — `server/game/player_service.py`

## Relationships

- [Player Stats](Player_Stats.md) (6 shared connections)
- [spell game magic](spell_game_magic.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (1 shared connections)
- [command inventory models](command_inventory_models.md) (1 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (1 shared connections)

## Source Files

- `server/game/player_search_service.py`
- `server/game/player_service.py`

## Audit Trail

- EXTRACTED: 41 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*