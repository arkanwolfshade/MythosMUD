# PlayerStateService

> 46 nodes

## Key Concepts

- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- **PlayerSearchService** (10 connections) — `server/game/player_search_service.py`
- **PlayerCreationService** (9 connections) — `server/game/player_creation_service.py`
- **.create_player_with_stats()** (8 connections) — `server/game/player_creation_service.py`
- **.__init__()** (8 connections) — `server/game/player_service.py`
- **.create_player()** (7 connections) — `server/game/player_creation_service.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **._resolve_tutorial_start_room()** (5 connections) — `server/game/player_creation_service.py`
- **.apply_corruption()** (5 connections) — `server/game/player_state_service.py`
- **.apply_fear()** (5 connections) — `server/game/player_state_service.py`
- **.apply_lucidity_loss()** (5 connections) — `server/game/player_state_service.py`
- **.damage_player()** (5 connections) — `server/game/player_state_service.py`
- **.gain_occult_knowledge()** (5 connections) — `server/game/player_state_service.py`
- **.heal_player()** (5 connections) — `server/game/player_state_service.py`
- **.resolve_player_name()** (4 connections) — `server/game/player_search_service.py`
- **UUID** (4 connections)
- **.__init__()** (3 connections) — `server/game/player_creation_service.py`
- **.get_online_players()** (3 connections) — `server/game/player_search_service.py`
- **.__init__()** (3 connections) — `server/game/player_search_service.py`
- **.search_players_by_name()** (3 connections) — `server/game/player_search_service.py`
- **.validate_player_name()** (3 connections) — `server/game/player_search_service.py`
- **.__init__()** (3 connections) — `server/game/player_state_service.py`
- **Any** (1 connections)
- **Stats** (1 connections)
- *... and 21 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (10 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (6 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [Player](Player.md) (4 shared connections)
- [Stats](Stats.md) (3 shared connections)
- [server/models/game.py](server-models-game.py.md) (1 shared connections)
- [PlayerRespawnWrapper](PlayerRespawnWrapper.md) (1 shared connections)

## Source Files

- `server/game/player_creation_service.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`

## Audit Trail

- EXTRACTED: 88 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*