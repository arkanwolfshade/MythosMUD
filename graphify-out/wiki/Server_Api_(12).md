# Server Api (12)

> 25 nodes

## Key Concepts

- **player_respawn.py** (24 connections) — `server/api/player_respawn.py`
- **test_player_respawn_handlers.py** (14 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **respawn_player_from_delirium()** (9 connections) — `server/api/player_respawn.py`
- **respawn_player()** (9 connections) — `server/api/player_respawn.py`
- **RespawnResponse** (8 connections) — `server/schemas/players/player_respawn.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_not_found()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_must_be_dead()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_generic_500()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_not_found()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_must_be_delirious()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_lucidity_keyword()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_generic_500()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **Request** (4 connections)
- **RespawnPlayerData** (4 connections) — `server/schemas/players/player_respawn.py`
- **ValidationError** (2 connections)
- **Convert ValidationError to appropriate HTTPException for respawn.      Args:** (2 connections) — `server/api/player_respawn.py`
- **BaseModel** (2 connections)
- **Player respawn API endpoints.  This module handles endpoints for respawning play** (1 connections) — `server/api/player_respawn.py`
- **Respawn a delirious player at the Sanitarium with restored lucidity.      This e** (1 connections) — `server/api/player_respawn.py`
- **Respawn a dead player at their respawn location with full DP.      This endpoint** (1 connections) — `server/api/player_respawn.py`
- **Simplified player data returned in respawn responses.** (1 connections) — `server/schemas/players/player_respawn.py`
- **Response model for player respawn endpoints.** (1 connections) — `server/schemas/players/player_respawn.py`

## Relationships

- [Server Admin](Server_Admin.md) (16 shared connections)
- [Server Api](Server_Api.md) (13 shared connections)
- [Server Utils](Server_Utils.md) (9 shared connections)
- [Server Api (3)](Server_Api_%283%29.md) (4 shared connections)
- [Server Services](Server_Services.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Schemas](Server_Schemas.md) (2 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (1 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (1 shared connections)
- [Server Game](Server_Game.md) (1 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/schemas/players/player_respawn.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`

## Audit Trail

- EXTRACTED: 142 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*