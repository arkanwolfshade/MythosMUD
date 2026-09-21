# test_player_respawn_service.py

> 122 nodes

## Key Concepts

- **test_player_respawn_service.py** (54 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **player_respawn_service.py** (40 connections) — `server/services/player_respawn_service.py`
- **asyncio** (27 connections)
- **player_respawn_wrapper.py** (22 connections) — `server/game/player_respawn_wrapper.py`
- **PlayerRespawnWrapper** (18 connections) — `server/game/player_respawn_wrapper.py`
- **test_player_respawn_wrapper.py** (14 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **spawn_defaults.py** (9 connections) — `server/constants/spawn_defaults.py`
- **.respawn_player_by_user_id()** (7 connections) — `server/game/player_respawn_wrapper.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **asyncio** (7 connections)
- **fixture** (7 connections)
- **.respawn_player_from_delirium_by_user_id()** (6 connections) — `server/game/player_respawn_wrapper.py`
- **_select_dead_player_for_respawn()** (6 connections) — `server/game/player_respawn_wrapper.py`
- **._load_active_players()** (5 connections) — `server/game/player_respawn_wrapper.py`
- **._load_player_for_delirium_respawn()** (5 connections) — `server/game/player_respawn_wrapper.py`
- **_resolve_respawn_room_data()** (5 connections) — `server/game/player_respawn_wrapper.py`
- **test_respawn_player_from_delirium_combat_clear_error()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_database_error()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_success()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_sanitarium_success()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **_is_eligible_for_respawn()** (4 connections) — `server/game/player_respawn_wrapper.py`
- **_dead_player()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_not_delirious()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_player_not_found()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_success()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- *... and 97 more nodes in this community*

## Relationships

- [Player](Player.md) (15 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [ValidationError](ValidationError.md) (13 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (13 shared connections)
- [PlayerLucidity](PlayerLucidity.md) (13 shared connections)
- [DatabaseError](DatabaseError.md) (8 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (4 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (3 shared connections)
- [LucidityService](LucidityService.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (2 shared connections)

## Source Files

- `server/constants/spawn_defaults.py`
- `server/game/player_respawn_wrapper.py`
- `server/services/player_respawn_service.py`
- `server/tests/unit/game/test_player_respawn_wrapper.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 256 (87%)
- INFERRED: 38 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*