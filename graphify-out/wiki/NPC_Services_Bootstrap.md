# NPC Services Bootstrap

> 57 nodes

## Key Concepts

- **test_combat_schema.py** (20 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **CombatSchemaValidationError** (17 connections) — `server/schemas/combat/combat_schema.py`
- **combat_schema.py** (13 connections) — `server/schemas/combat/combat_schema.py`
- **validate_npc_combat_data()** (13 connections) — `server/schemas/combat/combat_schema.py`
- **validate_base_stats_combat_data()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **validate_combat_messages()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **__init__.py** (10 connections) — `server/schemas/combat/__init__.py`
- **migrate_npc_combat_data()** (10 connections) — `server/scripts/migrate_combat_data.py`
- **validate_behavior_config_combat_data()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **add_default_combat_data_to_stats()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **add_default_combat_data_to_config()** (8 connections) — `server/schemas/combat/combat_schema.py`
- **validate_migration_results()** (8 connections) — `server/scripts/migrate_combat_data.py`
- **rollback_migration()** (7 connections) — `server/scripts/migrate_combat_data.py`
- **get_combat_stats_summary()** (6 connections) — `server/schemas/combat/combat_schema.py`
- **Any** (5 connections)
- **validate_message_template_variables()** (4 connections) — `server/schemas/combat/combat_schema.py`
- **Draft7Validator** (4 connections)
- **test_validate_base_stats_combat_data_missing_required()** (4 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_base_stats_combat_data_invalid_type()** (4 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_combat_messages_missing_required()** (4 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **AsyncSession** (3 connections)
- **Any** (3 connections)
- **test_validate_base_stats_combat_data_valid()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_behavior_config_combat_data_valid()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_combat_messages_valid()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- *... and 32 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (7 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (5 shared connections)
- [command inventory models](command_inventory_models.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)
- [npc population stats](npc_population_stats.md) (1 shared connections)

## Source Files

- `server/schemas/combat/__init__.py`
- `server/schemas/combat/combat_schema.py`
- `server/scripts/migrate_combat_data.py`
- `server/tests/unit/schemas/test_combat_schema.py`

## Audit Trail

- EXTRACTED: 213 (91%)
- INFERRED: 21 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*