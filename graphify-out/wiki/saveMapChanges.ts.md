# saveMapChanges.ts

> 65 nodes · cohesion 0.06

## Key Concepts

- **test_combat_schema.py** (20 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_aggression.py** (15 connections) — `server/tests/unit/schemas/test_aggression.py`
- **combat_schema.py** (14 connections) — `server/schemas/combat/combat_schema.py`
- **validate_npc_combat_data()** (13 connections) — `server/schemas/combat/combat_schema.py`
- **CombatSchemaValidationError** (12 connections) — `server/schemas/combat/combat_schema.py`
- **validate_behavior_config_combat_data()** (12 connections) — `server/schemas/combat/combat_schema.py`
- **validate_base_stats_combat_data()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **validate_combat_messages()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **combat/__init__.py** (10 connections) — `server/schemas/combat/__init__.py`
- **add_default_combat_data_to_stats()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **aggression.py** (8 connections) — `server/schemas/combat/aggression.py`
- **parse_aggression_level()** (8 connections) — `server/schemas/combat/aggression.py`
- **add_default_combat_data_to_config()** (8 connections) — `server/schemas/combat/combat_schema.py`
- **get_combat_stats_summary()** (6 connections) — `server/schemas/combat/combat_schema.py`
- **Any** (5 connections)
- **parametrize** (5 connections)
- **Draft7Validator** (4 connections)
- **validate_message_template_variables()** (4 connections) — `server/schemas/combat/combat_schema.py`
- **test_admin_model_normalises_to_an_int()** (4 connections) — `server/tests/unit/schemas/test_aggression.py`
- **test_catalog_names_land_on_the_ends_of_the_threat_scale()** (4 connections) — `server/tests/unit/schemas/test_aggression.py`
- **test_parse_aggression_level()** (4 connections) — `server/tests/unit/schemas/test_aggression.py`
- **test_admin_model_still_rejects_bad_levels()** (3 connections) — `server/tests/unit/schemas/test_aggression.py`
- **test_combat_schema_accepts_both_spellings()** (3 connections) — `server/tests/unit/schemas/test_aggression.py`
- **test_combat_schema_rejects_everything_else()** (3 connections) — `server/tests/unit/schemas/test_aggression.py`
- **test_add_default_combat_data_to_config()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- *... and 40 more nodes in this community*

## Relationships

- [Test Suite Quality Audit - Executive Summary](Test_Suite_Quality_Audit_-_Executive_Summary.md) (8 shared connections)
- [FollowService](FollowService.md) (3 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (3 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [ADR-026: Item Catalog Metadata Contracts](ADR-026-_Item_Catalog_Metadata_Contracts.md) (1 shared connections)
- [ground_channel.py](ground_channel.py.md) (1 shared connections)
- [ErrorType](ErrorType.md) (1 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)

## Source Files

- `server/schemas/combat/__init__.py`
- `server/schemas/combat/aggression.py`
- `server/schemas/combat/combat_schema.py`
- `server/tests/unit/schemas/test_aggression.py`
- `server/tests/unit/schemas/test_combat_schema.py`

## Audit Trail

- EXTRACTED: 138 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*