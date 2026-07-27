# Combat Schema Validation

> 48 nodes · cohesion 0.08

## Key Concepts

- **test_combat_schema.py** (20 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **validate_npc_combat_data()** (13 connections) — `server/schemas/combat/combat_schema.py`
- **combat_schema.py** (12 connections) — `server/schemas/combat/combat_schema.py`
- **CombatSchemaValidationError** (11 connections) — `server/schemas/combat/combat_schema.py`
- **validate_base_stats_combat_data()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **validate_combat_messages()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **__init__.py** (10 connections) — `server/schemas/combat/__init__.py`
- **add_default_combat_data_to_stats()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **validate_behavior_config_combat_data()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **add_default_combat_data_to_config()** (8 connections) — `server/schemas/combat/combat_schema.py`
- **get_combat_stats_summary()** (6 connections) — `server/schemas/combat/combat_schema.py`
- **Any** (5 connections) — `server/schemas/combat/combat_schema.py`
- **validate_message_template_variables()** (4 connections) — `server/schemas/combat/combat_schema.py`
- **Draft7Validator** (4 connections) — `server/schemas/shared/inventory_schema.py`
- **test_add_default_combat_data_to_config()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_add_default_combat_data_to_stats()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_add_default_combat_data_to_stats_preserves_existing()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_get_combat_stats_summary()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_base_stats_combat_data_invalid_type()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_base_stats_combat_data_missing_required()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_base_stats_combat_data_valid()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_behavior_config_combat_data_valid()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_combat_messages_missing_required()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_combat_messages_valid()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_npc_combat_data()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- *... and 23 more nodes in this community*

## Relationships

- [[NPC Database Sessions]] (4 shared connections)
- [[Migrate Combat]] (4 shared connections)
- [[NPC Definition Schemas]] (1 shared connections)
- [[Combat Domain Events]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Combat Messaging Base]] (1 shared connections)
- [[Player Save Preparer]] (1 shared connections)

## Source Files

- `server/schemas/combat/__init__.py`
- `server/schemas/combat/combat_schema.py`
- `server/schemas/shared/inventory_schema.py`
- `server/tests/unit/schemas/test_combat_schema.py`

## Audit Trail

- EXTRACTED: 183 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
