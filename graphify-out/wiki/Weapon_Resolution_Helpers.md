# Weapon Resolution Helpers

> 68 nodes

## Key Concepts

- **migrate_combat_data.py** (21 connections) — `server/scripts/migrate_combat_data.py`
- **test_combat_schema.py** (20 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **CombatSchemaValidationError** (14 connections) — `server/schemas/combat/combat_schema.py`
- **combat_schema.py** (13 connections) — `server/schemas/combat/combat_schema.py`
- **validate_npc_combat_data()** (13 connections) — `server/schemas/combat/combat_schema.py`
- **validate_base_stats_combat_data()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **validate_combat_messages()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **__init__.py** (10 connections) — `server/schemas/combat/__init__.py`
- **validate_behavior_config_combat_data()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **add_default_combat_data_to_stats()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **Any** (9 connections)
- **_migrate_one_npc()** (9 connections) — `server/scripts/migrate_combat_data.py`
- **add_default_combat_data_to_config()** (8 connections) — `server/schemas/combat/combat_schema.py`
- **migrate_npc_combat_data()** (8 connections) — `server/scripts/migrate_combat_data.py`
- **rollback_migration()** (8 connections) — `server/scripts/migrate_combat_data.py`
- **validate_migration_results()** (7 connections) — `server/scripts/migrate_combat_data.py`
- **get_combat_stats_summary()** (6 connections) — `server/schemas/combat/combat_schema.py`
- **_record_npc_error()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **_rollback_one_npc()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **main()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **Any** (5 connections)
- **AsyncSession** (5 connections)
- **_validate_one_npc()** (5 connections) — `server/scripts/migrate_combat_data.py`
- **validate_message_template_variables()** (4 connections) — `server/schemas/combat/combat_schema.py`
- **Draft7Validator** (4 connections)
- *... and 43 more nodes in this community*

## Relationships

- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (9 shared connections)
- [Combat Schema Validation](Combat_Schema_Validation.md) (3 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [Zone Schema Definition](Zone_Schema_Definition.md) (1 shared connections)
- [NPC Definition CRUD](NPC_Definition_CRUD.md) (1 shared connections)

## Source Files

- `server/schemas/combat/__init__.py`
- `server/schemas/combat/combat_schema.py`
- `server/scripts/migrate_combat_data.py`
- `server/tests/unit/schemas/test_combat_schema.py`

## Audit Trail

- EXTRACTED: 284 (95%)
- INFERRED: 15 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*