# test_player_respawn_handlers.py

> 23 nodes

## Key Concepts

- **test_player_respawn_handlers.py** (14 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **_run_player_respawn()** (10 connections) — `server/api/player_respawn.py`
- **respawn_player()** (9 connections) — `server/api/player_respawn.py`
- **respawn_player_from_delirium()** (9 connections) — `server/api/player_respawn.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **Request** (5 connections)
- **test_handle_delirium_validation_generic_500()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_lucidity_keyword()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_must_be_delirious()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_not_found()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_generic_500()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_must_be_dead()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_not_found()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **post** (2 connections)
- **ValidationError** (2 connections)
- **Any** (1 connections)
- **Respawn a delirious player at the Sanitarium with restored lucidity. This…** (1 connections) — `server/api/player_respawn.py`
- **Respawn a dead player at their respawn location with full DP. This endpoint…** (1 connections) — `server/api/player_respawn.py`
- **Convert ValidationError to appropriate HTTPException for respawn. Args: e:…** (1 connections) — `server/api/player_respawn.py`
- **Convert ValidationError to appropriate HTTPException for delirium respawn.…** (1 connections) — `server/api/player_respawn.py`
- **Execute a respawn service call inside a DB session with shared error handling.** (1 connections) — `server/api/player_respawn.py`

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [User](User.md) (5 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (4 shared connections)
- [rooms.py](rooms.py.md) (3 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`

## Audit Trail

- EXTRACTED: 71 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*