# persistence rationale player

> 28 nodes

## Key Concepts

- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **PlayerCreate** (10 connections) — `server/schemas/players/player.py`
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
- **Schema for creating a new player.** (1 connections) — `server/schemas/players/player.py`
- **Unit tests for player schemas.  Tests the Pydantic models in player.py module.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Test PlayerBase can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Test PlayerBase validates name length.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Test PlayerCreate can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Test PlayerCreate can have custom stats.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Test PlayerRead can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Test PlayerRead has correct default values.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Test CharacterInfo can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Test CharacterInfo has correct default values.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Test PlayerUpdate can be instantiated with optional fields.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- *... and 3 more nodes in this community*

## Relationships

- [Player Stats](Player_Stats.md) (16 shared connections)
- [System Metrics](System_Metrics.md) (5 shared connections)
- [command inventory models](command_inventory_models.md) (3 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (2 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (1 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (1 shared connections)

## Source Files

- `server/schemas/players/player.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 83 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*