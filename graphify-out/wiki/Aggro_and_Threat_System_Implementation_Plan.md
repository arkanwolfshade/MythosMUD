# Aggro and Threat System Implementation Plan

> 9 nodes

## Key Concepts

- **.resolve_player_name()** (4 connections) — `server/game/player_search_service.py`
- **.get_online_players()** (3 connections) — `server/game/player_search_service.py`
- **.search_players_by_name()** (3 connections) — `server/game/player_search_service.py`
- **.validate_player_name()** (3 connections) — `server/game/player_search_service.py`
- **PlayerRead** (3 connections)
- **Search for players by name with fuzzy matching. This method returns multiple…** (1 connections) — `server/game/player_search_service.py`
- **Validate a player name for chat system use. This checks if the name is valid…** (1 connections) — `server/game/player_search_service.py`
- **Resolve a player name with fuzzy matching and case-insensitive search. This…** (1 connections) — `server/game/player_search_service.py`
- **Get a list of currently online players. Note: This is a placeholder…** (1 connections) — `server/game/player_search_service.py`

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)

## Source Files

- `server/game/player_search_service.py`

## Audit Trail

- EXTRACTED: 12 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*