# api/player_respawn.py

> 32 nodes

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
- **players/player_respawn.py** (6 connections) — `server/schemas/players/player_respawn.py`
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
- *... and 7 more nodes in this community*

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (12 shared connections)
- [User](User.md) (6 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [database.py](database.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [players/__init__.py](players-__init__.py.md) (3 shared connections)
- [update_room_position](update_room_position.md) (2 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/schemas/players/player_respawn.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`

## Audit Trail

- EXTRACTED: 162 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*