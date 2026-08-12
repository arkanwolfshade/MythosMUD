# Lucidity Flux Performance Bug

> 26 nodes

## Key Concepts

- **player_respawn.py** (25 connections) — `server/api/player_respawn.py`
- **test_player_respawn_handlers.py** (14 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **_run_player_respawn()** (10 connections) — `server/api/player_respawn.py`
- **RespawnResponse** (9 connections) — `server/schemas/players/player_respawn.py`
- **respawn_player_from_delirium()** (8 connections) — `server/api/player_respawn.py`
- **respawn_player()** (8 connections) — `server/api/player_respawn.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **Request** (5 connections)
- **test_handle_respawn_validation_not_found()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_must_be_dead()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_generic_500()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_not_found()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_must_be_delirious()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_lucidity_keyword()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_generic_500()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **ValidationError** (2 connections)
- **Any** (1 connections)
- **Player respawn API endpoints.  This module handles endpoints for respawning play** (1 connections) — `server/api/player_respawn.py`
- **Convert ValidationError to appropriate HTTPException for respawn.      Args:** (1 connections) — `server/api/player_respawn.py`
- **Convert ValidationError to appropriate HTTPException for delirium respawn.** (1 connections) — `server/api/player_respawn.py`
- **Execute a respawn service call inside a DB session with shared error handling.** (1 connections) — `server/api/player_respawn.py`
- **Respawn a delirious player at the Sanitarium with restored lucidity.      This e** (1 connections) — `server/api/player_respawn.py`
- **Respawn a dead player at their respawn location with full DP.      This endpoint** (1 connections) — `server/api/player_respawn.py`
- *... and 1 more nodes in this community*

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (12 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (9 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (8 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (2 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (2 shared connections)
- [Disconnect Grace Period](Disconnect_Grace_Period.md) (2 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (1 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (1 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/schemas/players/player_respawn.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`

## Audit Trail

- EXTRACTED: 144 (93%)
- INFERRED: 11 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*