# models player related

> 35 nodes

## Key Concepts

- **player_respawn.py** (25 connections) — `server/api/player_respawn.py`
- **test_player_respawn_api.py** (17 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **respawn_player()** (15 connections) — `server/api/player_respawn.py`
- **test_player_respawn_handlers.py** (14 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **respawn_player_from_delirium()** (13 connections) — `server/api/player_respawn.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **_user()** (9 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **RespawnResponse** (8 connections) — `server/schemas/players/player_respawn.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_respawn_player_validation_error()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_from_delirium_not_found()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_not_found()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_handle_respawn_validation_not_found()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_must_be_dead()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_generic_500()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_not_found()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_must_be_delirious()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_lucidity_keyword()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_generic_500()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **Request** (4 connections)
- **test_respawn_player_success()** (4 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_from_delirium_success()** (4 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_unexpected_error()** (4 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_no_session()** (4 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- *... and 10 more nodes in this community*

## Relationships

- [services inventory mutation](services_inventory_mutation.md) (20 shared connections)
- [command inventory models](command_inventory_models.md) (13 shared connections)
- [player requests schemas](player_requests_schemas.md) (5 shared connections)
- [Player Stats](Player_Stats.md) (4 shared connections)
- [useWebSocketConnectionTestFixtures useWe](useWebSocketConnectionTestFixtures_useWe.md) (3 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (3 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (2 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (2 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (1 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/schemas/players/player_respawn.py`
- `server/tests/unit/api/test_player_respawn_api.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`

## Audit Trail

- EXTRACTED: 205 (94%)
- INFERRED: 13 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*