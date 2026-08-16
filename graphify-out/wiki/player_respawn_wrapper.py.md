# player_respawn_wrapper.py

> 23 nodes

## Key Concepts

- **player_respawn_wrapper.py** (16 connections) — `server/game/player_respawn_wrapper.py`
- **PlayerRespawnWrapper** (15 connections) — `server/game/player_respawn_wrapper.py`
- **test_player_respawn_wrapper.py** (14 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **spawn_defaults.py** (8 connections) — `server/constants/spawn_defaults.py`
- **asyncio** (6 connections)
- **.respawn_player_by_user_id()** (4 connections) — `server/game/player_respawn_wrapper.py`
- **.respawn_player_from_delirium_by_user_id()** (4 connections) — `server/game/player_respawn_wrapper.py`
- **test_respawn_from_delirium_not_delirious()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_player_not_found()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_success()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_no_players()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_not_dead()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_success()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **.__init__()** (3 connections) — `server/game/player_respawn_wrapper.py`
- **_dead_player()** (3 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **Any** (3 connections)
- **Shared spawn / respawn room identifiers used by gameplay and E2E seed scripts.…** (1 connections) — `server/constants/spawn_defaults.py`
- **Player respawn wrapper service. This module provides wrapper methods for player…** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Respawn a delirious player by user ID. This method handles the complete…** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Wrapper service for player respawn operations.** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Initialize with a persistence layer.** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Respawn a dead player by user ID. This method handles the complete respawn…** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Unit tests for PlayerRespawnWrapper.** (1 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`

## Relationships

- [ValidationError](ValidationError.md) (10 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (3 shared connections)
- [Player](Player.md) (2 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [AuthenticationError](AuthenticationError.md) (1 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (1 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (1 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)
- [LucidityService](LucidityService.md) (1 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (1 shared connections)

## Source Files

- `server/constants/spawn_defaults.py`
- `server/game/player_respawn_wrapper.py`
- `server/tests/unit/game/test_player_respawn_wrapper.py`

## Audit Trail

- EXTRACTED: 58 (84%)
- INFERRED: 11 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*