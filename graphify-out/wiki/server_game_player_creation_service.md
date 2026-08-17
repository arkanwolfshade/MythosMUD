# server game player creation service

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

- [claude rules asyncio](claude_rules_asyncio.md) (14 shared connections)
- [server api character creation](server_api_character_creation.md) (9 shared connections)
- [server api players](server_api_players.md) (5 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (1 shared connections)
- [server game player respawn wrapper](server_game_player_respawn_wrapper.md) (1 shared connections)

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