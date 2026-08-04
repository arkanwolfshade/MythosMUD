# command commands handler

> 34 nodes

## Key Concepts

- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **PlayerBase** (11 connections) — `server/schemas/players/player.py`
- **PlayerCreate** (10 connections) — `server/schemas/players/player.py`
- **CharacterInfo** (10 connections) — `server/schemas/players/player.py`
- **PlayerUpdate** (9 connections) — `server/schemas/players/player.py`
- **test_player_base_validation()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_create()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_create_custom_stats()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_read()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_read_defaults()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_base_rejects_extra_fields()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_create_rejects_extra_fields()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_base()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_character_info()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_character_info_defaults()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_update()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_update_all_optional()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Base player schema with common fields.** (1 connections) — `server/schemas/players/player.py`
- **Schema for creating a new player.** (1 connections) — `server/schemas/players/player.py`
- **Schema for character information in login response.      MULTI-CHARACTER: Lightw** (1 connections) — `server/schemas/players/player.py`
- **Schema for updating player data.** (1 connections) — `server/schemas/players/player.py`
- **Unit tests for player schemas.  Tests the Pydantic models in player.py module.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Test PlayerBase can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Test PlayerBase validates name length.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Test PlayerCreate can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- *... and 9 more nodes in this community*

## Relationships

- [Player Stats](Player_Stats.md) (11 shared connections)
- [command factories communication](command_factories_communication.md) (6 shared connections)
- [player service game](player_service_game.md) (5 shared connections)
- [game models stats](game_models_stats.md) (4 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (2 shared connections)
- [player requests schemas](player_requests_schemas.md) (2 shared connections)

## Source Files

- `server/schemas/players/player.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 113 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*