# command parser helpers

> 36 nodes

## Key Concepts

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
- **RespawnPlayerData** (4 connections) — `server/schemas/players/player_respawn.py`
- **test_respawn_player_success()** (4 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_from_delirium_success()** (4 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_unexpected_error()** (4 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_no_session()** (4 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- *... and 11 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (19 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (14 shared connections)
- [Loot Generation](Loot_Generation.md) (9 shared connections)
- [player requests schemas](player_requests_schemas.md) (4 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (2 shared connections)
- [game models stats](game_models_stats.md) (2 shared connections)
- [room game service](room_game_service.md) (2 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (1 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/schemas/players/player_respawn.py`
- `server/tests/unit/api/test_player_respawn_api.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`

## Audit Trail

- EXTRACTED: 186 (93%)
- INFERRED: 13 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*