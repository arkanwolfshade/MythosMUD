# player requests schemas

> 22 nodes

## Key Concepts

- **test_player_requests.py** (29 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **DamageRequest** (12 connections) — `server/schemas/players/player_requests.py`
- **test_lucidity_loss_request_validation()** (4 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_damage_request_validation()** (4 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_create_character_request()** (3 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_create_character_request_name_stripped()** (3 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_roll_stats_request()** (3 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_roll_stats_request_custom()** (3 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_lucidity_loss_request()** (3 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_damage_request()** (3 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_damage_request_custom_type()** (3 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **Request model for damaging a player.** (1 connections) — `server/schemas/players/player_requests.py`
- **Unit tests for player_requests schemas.  Tests the Pydantic models in player_req** (1 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **Test CreateCharacterRequest can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **Test CreateCharacterRequest strips whitespace from name.** (1 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **Test RollStatsRequest can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **Test RollStatsRequest with custom values.** (1 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **Test LucidityLossRequest can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **Test LucidityLossRequest validates amount range.** (1 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **Test DamageRequest can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **Test DamageRequest with custom damage type.** (1 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **Test DamageRequest validates amount range.** (1 connections) — `server/tests/unit/schemas/test_player_requests.py`

## Relationships

- [player schemas requests](player_schemas_requests.md) (5 shared connections)
- [player requests schemas](player_requests_schemas.md) (4 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (4 shared connections)
- [character creation validate](character_creation_validate.md) (3 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (3 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (3 shared connections)
- [npc lifecycle combat](npc_lifecycle_combat.md) (3 shared connections)
- [combat messaging service](combat_messaging_service.md) (3 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [Player Stats](Player_Stats.md) (1 shared connections)

## Source Files

- `server/schemas/players/player_requests.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 79 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*