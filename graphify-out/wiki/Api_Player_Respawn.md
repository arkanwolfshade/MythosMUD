# Api Player Respawn

> 21 nodes · cohesion 0.21

## Key Concepts

- **test_player_respawn_handlers.py** (13 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **respawn_player()** (9 connections) — `server/api/player_respawn.py`
- **respawn_player_from_delirium()** (9 connections) — `server/api/player_respawn.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_generic_500()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_lucidity_keyword()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_must_be_delirious()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_not_found()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_generic_500()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_must_be_dead()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_not_found()** (4 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **Request** (4 connections) — `server/api/player_respawn.py`
- **User** (4 connections) — `server/api/player_respawn.py`
- **Respawn a dead player at their respawn location with full DP.      This endpoint** (2 connections) — `server/api/player_respawn.py`
- **Convert ValidationError to appropriate HTTPException for respawn.      Args:** (2 connections) — `server/api/player_respawn.py`
- **RespawnResponse** (2 connections) — `server/api/player_respawn.py`
- **PlayerService** (2 connections) — `server/api/player_respawn.py`
- **ValidationError** (2 connections) — `server/api/player_respawn.py`
- **Respawn a delirious player at the Sanitarium with restored lucidity.      This e** (1 connections) — `server/api/player_respawn.py`

## Relationships

- [[NPC Admin API]] (15 shared connections)
- [[Container Exception Handlers]] (5 shared connections)
- [[Player Respawn Service]] (1 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`

## Audit Trail

- EXTRACTED: 109 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
