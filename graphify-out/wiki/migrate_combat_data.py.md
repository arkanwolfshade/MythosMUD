# migrate_combat_data.py

> 31 nodes

## Key Concepts

- **migrate_combat_data.py** (28 connections) — `server/scripts/migrate_combat_data.py`
- **_migrate_one_npc()** (9 connections) — `server/scripts/migrate_combat_data.py`
- **migrate_npc_combat_data()** (7 connections) — `server/scripts/migrate_combat_data.py`
- **rollback_migration()** (7 connections) — `server/scripts/migrate_combat_data.py`
- **_rollback_one_npc()** (7 connections) — `server/scripts/migrate_combat_data.py`
- **main()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **validate_migration_results()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **MigrationResults** (5 connections) — `server/scripts/migrate_combat_data.py`
- **RollbackResults** (5 connections) — `server/scripts/migrate_combat_data.py`
- **ValidationResults** (5 connections) — `server/scripts/migrate_combat_data.py`
- **_record_npc_error()** (5 connections) — `server/scripts/migrate_combat_data.py`
- **_strip_combat_data_from_npc()** (5 connections) — `server/scripts/migrate_combat_data.py`
- **_validate_one_npc()** (5 connections) — `server/scripts/migrate_combat_data.py`
- **AsyncSession** (5 connections)
- **_MigrationArgs** (3 connections) — `server/scripts/migrate_combat_data.py`
- **TypedDict** (3 connections)
- **_npc_has_combat_data()** (2 connections) — `server/scripts/migrate_combat_data.py`
- **_npc_has_full_combat_data()** (2 connections) — `server/scripts/migrate_combat_data.py`
- **_omit_keys()** (2 connections) — `server/scripts/migrate_combat_data.py`
- **_present_keys()** (2 connections) — `server/scripts/migrate_combat_data.py`
- **Exception** (1 connections)
- **Protocol** (1 connections)
- **Combat data migration script. This script adds default combat data to existing…** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Migrate combat data for all NPC definitions. Args: session: Database session…** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Validate that migration was successful. Args: session: Database session…** (1 connections) — `server/scripts/migrate_combat_data.py`
- *... and 6 more nodes in this community*

## Relationships

- [test_combat_schema.py](test_combat_schema.py.md) (8 shared connections)
- [EventBus](EventBus.md) (7 shared connections)
- [npc_database.py](npc_database.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/scripts/migrate_combat_data.py`

## Audit Trail

- EXTRACTED: 75 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*