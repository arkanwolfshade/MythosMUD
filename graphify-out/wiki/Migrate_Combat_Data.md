# Migrate Combat Data

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

- [NPC Models](NPC_Models.md) (7 shared connections)
- [Test Npc Database](Test_Npc_Database.md) (3 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Test Combat Messaging Service](Test_Combat_Messaging_Service.md) (1 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (1 shared connections)
- [Test Inventory Helpers Extended](Test_Inventory_Helpers_Extended.md) (1 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

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