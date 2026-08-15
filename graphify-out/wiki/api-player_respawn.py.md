# api/player_respawn.py

> 40 nodes

## Key Concepts

- **api/player_respawn.py** (28 connections) — `server/api/player_respawn.py`
- **test_player_respawn_api.py** (17 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **respawn_player()** (15 connections) — `server/api/player_respawn.py`
- **test_player_respawn_handlers.py** (14 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **respawn_player_from_delirium()** (13 connections) — `server/api/player_respawn.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **_run_player_respawn()** (10 connections) — `server/api/player_respawn.py`
- **RespawnResponse** (9 connections) — `server/schemas/players/player_respawn.py`
- **_user()** (9 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **asyncio** (8 connections)
- **test_respawn_player_from_delirium_not_found()** (6 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_not_found()** (6 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_validation_error()** (6 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_delirium_unexpected_error()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_from_delirium_success()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_no_session()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_success()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_unexpected_error()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_handle_delirium_validation_generic_500()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_lucidity_keyword()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_must_be_delirious()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_not_found()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_generic_500()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- *... and 15 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (19 shared connections)
- [ValidationError](ValidationError.md) (13 shared connections)
- [User](User.md) (6 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [players/player_respawn.py](players-player_respawn.py.md) (2 shared connections)
- [get_async_session](get_async_session.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (1 shared connections)
- [test_users.py](test_users.py.md) (1 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/schemas/players/player_respawn.py`
- `server/tests/unit/api/test_player_respawn_api.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`

## Audit Trail

- EXTRACTED: 133 (84%)
- INFERRED: 25 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*