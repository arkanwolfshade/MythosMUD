# migrate_combat_data.py

> 80 nodes

## Key Concepts

- **migrate_combat_data.py** (29 connections) — `server/scripts/migrate_combat_data.py`
- **test_combat_schema.py** (21 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **validate_npc_combat_data()** (13 connections) — `server/schemas/combat/combat_schema.py`
- **combat_schema.py** (13 connections) — `server/schemas/combat/combat_schema.py`
- **CombatSchemaValidationError** (11 connections) — `server/schemas/combat/combat_schema.py`
- **validate_base_stats_combat_data()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **validate_combat_messages()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **combat/__init__.py** (10 connections) — `server/schemas/combat/__init__.py`
- **add_default_combat_data_to_stats()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **validate_behavior_config_combat_data()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **_migrate_one_npc()** (9 connections) — `server/scripts/migrate_combat_data.py`
- **add_default_combat_data_to_config()** (8 connections) — `server/schemas/combat/combat_schema.py`
- **migrate_npc_combat_data()** (7 connections) — `server/scripts/migrate_combat_data.py`
- **rollback_migration()** (7 connections) — `server/scripts/migrate_combat_data.py`
- **_rollback_one_npc()** (7 connections) — `server/scripts/migrate_combat_data.py`
- **get_combat_stats_summary()** (6 connections) — `server/schemas/combat/combat_schema.py`
- **main()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **validate_migration_results()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **MigrationResults** (5 connections) — `server/scripts/migrate_combat_data.py`
- **RollbackResults** (5 connections) — `server/scripts/migrate_combat_data.py`
- **ValidationResults** (5 connections) — `server/scripts/migrate_combat_data.py`
- **_record_npc_error()** (5 connections) — `server/scripts/migrate_combat_data.py`
- **_strip_combat_data_from_npc()** (5 connections) — `server/scripts/migrate_combat_data.py`
- **_validate_one_npc()** (5 connections) — `server/scripts/migrate_combat_data.py`
- **Any** (5 connections)
- *... and 55 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (9 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [npc_database.py](npc_database.py.md) (3 shared connections)
- [CombatMessagingService](CombatMessagingService.md) (1 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (1 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/schemas/combat/__init__.py`
- `server/schemas/combat/combat_schema.py`
- `server/scripts/migrate_combat_data.py`
- `server/tests/unit/schemas/test_combat_schema.py`

## Audit Trail

- EXTRACTED: 168 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*