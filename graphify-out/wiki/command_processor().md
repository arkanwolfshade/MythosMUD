# command processor()

> 23 nodes

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
- **ValidationError** (2 connections)
- **Player respawn API endpoints.  This module handles endpoints for respawning play** (1 connections) — `server/api/player_respawn.py`
- **Convert ValidationError to appropriate HTTPException for respawn.      Args:** (1 connections) — `server/api/player_respawn.py`
- **Convert ValidationError to appropriate HTTPException for delirium respawn.** (1 connections) — `server/api/player_respawn.py`
- **Respawn a delirious player at the Sanitarium with restored lucidity.      This e** (1 connections) — `server/api/player_respawn.py`
- **Respawn a dead player at their respawn location with full DP.      This endpoint** (1 connections) — `server/api/player_respawn.py`
- **Response model for player respawn endpoints.** (1 connections) — `server/schemas/players/player_respawn.py`

## Relationships

- [AbstractContextManager](AbstractContextManager.md) (13 shared connections)
- [.initialize()](initialize%28%29.md) (9 shared connections)
- [close db()](close_db%28%29.md) (6 shared connections)
- [Connection Manager](Connection_Manager.md) (5 shared connections)
- [message handler factory](message_handler_factory.md) (3 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [real time](real_time.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [memory leak metrics](memory_leak_metrics.md) (2 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/schemas/players/player_respawn.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`

## Audit Trail

- EXTRACTED: 135 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*