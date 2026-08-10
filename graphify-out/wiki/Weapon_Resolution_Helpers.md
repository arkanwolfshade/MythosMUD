# Weapon Resolution Helpers

> 47 nodes

## Key Concepts

- **test_combat_schema.py** (20 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **CombatSchemaValidationError** (14 connections) — `server/schemas/combat/combat_schema.py`
- **combat_schema.py** (13 connections) — `server/schemas/combat/combat_schema.py`
- **validate_base_stats_combat_data()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **validate_combat_messages()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **__init__.py** (10 connections) — `server/schemas/combat/__init__.py`
- **validate_behavior_config_combat_data()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **add_default_combat_data_to_stats()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **add_default_combat_data_to_config()** (8 connections) — `server/schemas/combat/combat_schema.py`
- **get_combat_stats_summary()** (6 connections) — `server/schemas/combat/combat_schema.py`
- **Any** (5 connections)
- **validate_message_template_variables()** (4 connections) — `server/schemas/combat/combat_schema.py`
- **Draft7Validator** (4 connections)
- **test_validate_base_stats_combat_data_missing_required()** (4 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_base_stats_combat_data_invalid_type()** (4 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_combat_messages_missing_required()** (4 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_base_stats_combat_data_valid()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_behavior_config_combat_data_valid()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_combat_messages_valid()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_add_default_combat_data_to_stats()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_add_default_combat_data_to_stats_preserves_existing()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_add_default_combat_data_to_config()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_npc_combat_data()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_get_combat_stats_summary()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **Combat domain schemas: combat JSON schema validation and defaults.** (1 connections) — `server/schemas/combat/__init__.py`
- *... and 22 more nodes in this community*

## Relationships

- [Test Refactoring Deliverables](Test_Refactoring_Deliverables.md) (14 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)
- [End-to-End Validation](End-to-End_Validation.md) (1 shared connections)
- [NPC Definition CRUD](NPC_Definition_CRUD.md) (1 shared connections)

## Source Files

- `server/schemas/combat/__init__.py`
- `server/schemas/combat/combat_schema.py`
- `server/tests/unit/schemas/test_combat_schema.py`

## Audit Trail

- EXTRACTED: 171 (93%)
- INFERRED: 12 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*