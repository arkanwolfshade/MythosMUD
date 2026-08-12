# api/player_respawn.py

> 30 nodes

## Key Concepts

- **api/player_respawn.py** (25 connections) — `server/api/player_respawn.py`
- **test_player_respawn_handlers.py** (14 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **_run_player_respawn()** (10 connections) — `server/api/player_respawn.py`
- **RespawnResponse** (9 connections) — `server/schemas/players/player_respawn.py`
- **respawn_player()** (9 connections) — `server/api/player_respawn.py`
- **respawn_player_from_delirium()** (9 connections) — `server/api/player_respawn.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **Request** (5 connections)
- **RespawnPlayerData** (4 connections) — `server/schemas/players/player_respawn.py`
- **test_handle_delirium_validation_generic_500()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_lucidity_keyword()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_must_be_delirious()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_not_found()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_generic_500()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_must_be_dead()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_not_found()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **post** (2 connections)
- **ValidationError** (2 connections)
- **BaseModel** (2 connections)
- **Any** (1 connections)
- **Player respawn API endpoints. This module handles endpoints for respawning…** (1 connections) — `server/api/player_respawn.py`
- **Respawn a delirious player at the Sanitarium with restored lucidity. This…** (1 connections) — `server/api/player_respawn.py`
- **Respawn a dead player at their respawn location with full DP. This endpoint…** (1 connections) — `server/api/player_respawn.py`
- *... and 5 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (9 shared connections)
- [User](User.md) (6 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (5 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (3 shared connections)
- [players/__init__.py](players-__init__.py.md) (2 shared connections)
- [.get_instance](get_instance.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (1 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/schemas/players/player_respawn.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`

## Audit Trail

- EXTRACTED: 155 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*