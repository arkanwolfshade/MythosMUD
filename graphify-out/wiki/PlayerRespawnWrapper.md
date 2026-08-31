# PlayerRespawnWrapper

> 39 nodes

## Key Concepts

- **PlayerRespawnWrapper** (15 connections) — `server/game/player_respawn_wrapper.py`
- **test_player_respawn_wrapper.py** (14 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- **.__init__()** (8 connections) — `server/game/player_service.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **asyncio** (6 connections)
- **.apply_corruption()** (5 connections) — `server/game/player_state_service.py`
- **.apply_fear()** (5 connections) — `server/game/player_state_service.py`
- **.apply_lucidity_loss()** (5 connections) — `server/game/player_state_service.py`
- **.damage_player()** (5 connections) — `server/game/player_state_service.py`
- **.gain_occult_knowledge()** (5 connections) — `server/game/player_state_service.py`
- **.heal_player()** (5 connections) — `server/game/player_state_service.py`
- **.respawn_player_by_user_id()** (4 connections) — `server/game/player_respawn_wrapper.py`
- **.respawn_player_from_delirium_by_user_id()** (4 connections) — `server/game/player_respawn_wrapper.py`
- **test_respawn_from_delirium_not_delirious()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_player_not_found()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_success()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_no_players()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_not_dead()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_success()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **.__init__()** (3 connections) — `server/game/player_respawn_wrapper.py`
- **.__init__()** (3 connections) — `server/game/player_state_service.py`
- **_dead_player()** (3 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **Any** (3 connections)
- *... and 14 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (21 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [PlayerSchemaConverter](PlayerSchemaConverter.md) (1 shared connections)
- [PlayerCreationService](PlayerCreationService.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [LucidityService](LucidityService.md) (1 shared connections)

## Source Files

- `server/game/player_respawn_wrapper.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/tests/unit/game/test_player_respawn_wrapper.py`

## Audit Trail

- EXTRACTED: 81 (87%)
- INFERRED: 12 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*