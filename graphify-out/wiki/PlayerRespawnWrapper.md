# PlayerRespawnWrapper

> 61 nodes

## Key Concepts

- **PlayerRespawnWrapper** (15 connections) — `server/game/player_respawn_wrapper.py`
- **test_player_respawn_wrapper.py** (13 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- **PlayerSearchService** (10 connections) — `server/game/player_search_service.py`
- **PlayerCreationService** (9 connections) — `server/game/player_creation_service.py`
- **.create_player_with_stats()** (8 connections) — `server/game/player_creation_service.py`
- **.__init__()** (8 connections) — `server/game/player_service.py`
- **.create_player()** (7 connections) — `server/game/player_creation_service.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **.apply_corruption()** (6 connections) — `server/game/player_state_service.py`
- **asyncio** (6 connections)
- **._resolve_tutorial_start_room()** (5 connections) — `server/game/player_creation_service.py`
- **.apply_fear()** (5 connections) — `server/game/player_state_service.py`
- **.apply_lucidity_loss()** (5 connections) — `server/game/player_state_service.py`
- **.damage_player()** (5 connections) — `server/game/player_state_service.py`
- **.gain_occult_knowledge()** (5 connections) — `server/game/player_state_service.py`
- **.heal_player()** (5 connections) — `server/game/player_state_service.py`
- **.respawn_player_by_user_id()** (4 connections) — `server/game/player_respawn_wrapper.py`
- **.respawn_player_from_delirium_by_user_id()** (4 connections) — `server/game/player_respawn_wrapper.py`
- **.resolve_player_name()** (4 connections) — `server/game/player_search_service.py`
- **test_respawn_from_delirium_not_delirious()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_player_not_found()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_success()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_no_players()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- *... and 36 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (27 shared connections)
- [PlayerService](PlayerService.md) (6 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (5 shared connections)
- [Player](Player.md) (2 shared connections)
- [PlayerSchemaConverter](PlayerSchemaConverter.md) (1 shared connections)
- [CorruptionService](CorruptionService.md) (1 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (1 shared connections)

## Source Files

- `server/game/player_creation_service.py`
- `server/game/player_respawn_wrapper.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/tests/unit/game/test_player_respawn_wrapper.py`

## Audit Trail

- EXTRACTED: 120 (90%)
- INFERRED: 14 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*