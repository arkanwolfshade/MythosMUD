# Player Creation Service

> 58 nodes · cohesion 0.05

## Key Concepts

- **PlayerStateService** (16 connections) — `server/game/player_state_service.py`
- **PlayerSearchService** (14 connections) — `server/game/player_search_service.py`
- **PlayerCreationService** (13 connections) — `server/game/player_creation_service.py`
- **PlayerRespawnWrapper** (12 connections) — `server/game/player_respawn_wrapper.py`
- **.create_player_with_stats()** (8 connections) — `server/game/player_creation_service.py`
- **.__init__()** (8 connections) — `server/game/player_service.py`
- **.create_player()** (7 connections) — `server/game/player_creation_service.py`
- **Any** (7 connections) — `server/game/player_state_service.py`
- **UUID** (7 connections) — `server/game/player_state_service.py`
- **Stats** (6 connections) — `server/game/player_service.py`
- **._resolve_tutorial_start_room()** (5 connections) — `server/game/player_creation_service.py`
- **.apply_corruption()** (5 connections) — `server/game/player_state_service.py`
- **.apply_fear()** (5 connections) — `server/game/player_state_service.py`
- **.apply_lucidity_loss()** (5 connections) — `server/game/player_state_service.py`
- **.damage_player()** (5 connections) — `server/game/player_state_service.py`
- **.gain_occult_knowledge()** (5 connections) — `server/game/player_state_service.py`
- **.heal_player()** (5 connections) — `server/game/player_state_service.py`
- **.respawn_player_by_user_id()** (4 connections) — `server/game/player_respawn_wrapper.py`
- **.respawn_player_from_delirium_by_user_id()** (4 connections) — `server/game/player_respawn_wrapper.py`
- **.resolve_player_name()** (4 connections) — `server/game/player_search_service.py`
- **UUID** (4 connections) — `server/game/player_creation_service.py`
- **.__init__()** (3 connections) — `server/game/player_creation_service.py`
- **.__init__()** (3 connections) — `server/game/player_respawn_wrapper.py`
- **.get_online_players()** (3 connections) — `server/game/player_search_service.py`
- **.__init__()** (3 connections) — `server/game/player_search_service.py`
- *... and 33 more nodes in this community*

## Relationships

- [[NPC Admin API]] (20 shared connections)
- [[Combat Command Handler]] (19 shared connections)
- [[Player Domain Model]] (2 shared connections)
- [[Player Schema Converter]] (2 shared connections)

## Source Files

- `server/game/player_creation_service.py`
- `server/game/player_respawn_wrapper.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`

## Audit Trail

- EXTRACTED: 180 (88%)
- INFERRED: 25 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
