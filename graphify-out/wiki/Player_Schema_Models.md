# Player Schema Models

> 31 nodes · cohesion 0.08

## Key Concepts

- **test_player_schemas.py** (20 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **PlayerBase** (11 connections) — `server/schemas/players/player.py`
- **PlayerCreate** (10 connections) — `server/schemas/players/player.py`
- **PlayerUpdate** (9 connections) — `server/schemas/players/player.py`
- **test_player_create_custom_stats()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_read()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_read_defaults()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_character_info()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_character_info_defaults()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_base()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_base_rejects_extra_fields()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_base_validation()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_create()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_create_rejects_extra_fields()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_update()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_update_all_optional()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_user_base()** (3 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **Base user schema with common fields.** (2 connections) — `server/schemas/auth/user.py`
- **Schema for creating a new user.** (2 connections) — `server/schemas/auth/user.py`
- **Test UserBase can be instantiated.** (2 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **Schema for updating player data.** (1 connections) — `server/schemas/players/player.py`
- **Unit tests for player schemas.  Tests the Pydantic models in player.py module.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Test CharacterInfo can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Test CharacterInfo has correct default values.** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Test PlayerBase rejects extra fields (extra='forbid').** (1 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- *... and 6 more nodes in this community*

## Relationships

- [[Admin NPC Schemas]] (17 shared connections)
- [[Invite and User Schemas]] (6 shared connections)
- [[Character Stats Model]] (4 shared connections)
- [[Players API Endpoints]] (3 shared connections)
- [[Player Domain Model]] (1 shared connections)

## Source Files

- `server/schemas/auth/user.py`
- `server/schemas/players/player.py`
- `server/tests/unit/schemas/test_player_schemas.py`
- `server/tests/unit/schemas/test_user_schemas.py`

## Audit Trail

- EXTRACTED: 106 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
