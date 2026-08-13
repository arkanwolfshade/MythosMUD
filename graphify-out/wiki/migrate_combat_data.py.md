# migrate_combat_data.py

> 23 nodes

## Key Concepts

- **migrate_combat_data.py** (21 connections) — `server/scripts/migrate_combat_data.py`
- **validate_npc_combat_data()** (13 connections) — `server/schemas/combat/combat_schema.py`
- **_migrate_one_npc()** (9 connections) — `server/scripts/migrate_combat_data.py`
- **Any** (9 connections)
- **migrate_npc_combat_data()** (7 connections) — `server/scripts/migrate_combat_data.py`
- **rollback_migration()** (7 connections) — `server/scripts/migrate_combat_data.py`
- **main()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **_record_npc_error()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **_rollback_one_npc()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **validate_migration_results()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **_validate_one_npc()** (5 connections) — `server/scripts/migrate_combat_data.py`
- **AsyncSession** (5 connections)
- **_npc_has_combat_data()** (3 connections) — `server/scripts/migrate_combat_data.py`
- **_npc_has_full_combat_data()** (3 connections) — `server/scripts/migrate_combat_data.py`
- **test_validate_npc_combat_data()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **Exception** (1 connections)
- **Validate combat data for an NPC definition. Args: npc_definition: NPCDefinition…** (1 connections) — `server/schemas/combat/combat_schema.py`
- **Combat data migration script. This script adds default combat data to existing…** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Migrate combat data for all NPC definitions. Args: session: Database session…** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Validate that migration was successful. Args: session: Database session…** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Rollback combat data migration by removing combat fields. Args: session:…** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Main migration function.** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Test validate_npc_combat_data() validates NPC definition.** (1 connections) — `server/tests/unit/schemas/test_combat_schema.py`

## Relationships

- [test_combat_schema.py](test_combat_schema.py.md) (14 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (6 shared connections)
- [npc_database.py](npc_database.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/schemas/combat/combat_schema.py`
- `server/scripts/migrate_combat_data.py`
- `server/tests/unit/schemas/test_combat_schema.py`

## Audit Trail

- EXTRACTED: 71 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*