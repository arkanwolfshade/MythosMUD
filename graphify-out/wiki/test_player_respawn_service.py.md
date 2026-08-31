# test_player_respawn_service.py

> 89 nodes

## Key Concepts

- **test_player_respawn_service.py** (55 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **player_respawn_service.py** (40 connections) — `server/services/player_respawn_service.py`
- **asyncio** (27 connections)
- **PositionState** (17 connections) — `server/models/game.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **fixture** (7 connections)
- **test_respawn_player_from_delirium_combat_clear_error()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_database_error()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_success()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_sanitarium_success()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **respawn_service()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **respawn_service_no_deps()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **sample_dead_player()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **sample_player()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_custom()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_default()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_player_not_found()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_player_not_found()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_refused_when_not_dead()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_success()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_combat_clear_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_clears_combat_state()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- *... and 64 more nodes in this community*

## Relationships

- [Player](Player.md) (12 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (12 shared connections)
- [LucidityService](LucidityService.md) (12 shared connections)
- [DatabaseError](DatabaseError.md) (8 shared connections)
- [server/models/game.py](server-models-game.py.md) (7 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (7 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (3 shared connections)
- [lucidity.py](lucidity.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (2 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (2 shared connections)
- [coerce_int](coerce_int.md) (2 shared connections)

## Source Files

- `server/models/game.py`
- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 186 (87%)
- INFERRED: 27 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*