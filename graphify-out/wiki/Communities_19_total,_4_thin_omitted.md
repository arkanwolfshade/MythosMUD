# Communities (19 total, 4 thin omitted)

> 28 nodes

## Key Concepts

- **migrate_combat_data.py** (29 connections) — `server/scripts/migrate_combat_data.py`
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
- **TypedDict** (3 connections)
- **_npc_has_combat_data()** (2 connections) — `server/scripts/migrate_combat_data.py`
- **_npc_has_full_combat_data()** (2 connections) — `server/scripts/migrate_combat_data.py`
- **_omit_keys()** (2 connections) — `server/scripts/migrate_combat_data.py`
- **_present_keys()** (2 connections) — `server/scripts/migrate_combat_data.py`
- **Exception** (1 connections)
- **Combat data migration script. This script adds default combat data to existing…** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Migrate combat data for all NPC definitions. Args: session: Database session…** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Validate that migration was successful. Args: session: Database session…** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Rollback combat data migration by removing combat fields. Args: session:…** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Main migration function.** (1 connections) — `server/scripts/migrate_combat_data.py`
- *... and 3 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (7 shared connections)
- [HealthService](HealthService.md) (6 shared connections)
- [mock_connection_manager](mock_connection_manager.md) (3 shared connections)
- [Alone Against the Frost (source summary)](Alone_Against_the_Frost_source_summary.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [Bug Report Issue Template](Bug_Report_Issue_Template.md) (1 shared connections)

## Source Files

- `server/scripts/migrate_combat_data.py`

## Audit Trail

- EXTRACTED: 74 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*