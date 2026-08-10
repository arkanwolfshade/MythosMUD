# Test Refactoring Deliverables

> 21 nodes

## Key Concepts

- **migrate_combat_data.py** (21 connections) — `server/scripts/migrate_combat_data.py`
- **validate_npc_combat_data()** (13 connections) — `server/schemas/combat/combat_schema.py`
- **Any** (9 connections)
- **_migrate_one_npc()** (9 connections) — `server/scripts/migrate_combat_data.py`
- **migrate_npc_combat_data()** (8 connections) — `server/scripts/migrate_combat_data.py`
- **rollback_migration()** (8 connections) — `server/scripts/migrate_combat_data.py`
- **validate_migration_results()** (7 connections) — `server/scripts/migrate_combat_data.py`
- **_record_npc_error()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **_rollback_one_npc()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **main()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **AsyncSession** (5 connections)
- **_validate_one_npc()** (5 connections) — `server/scripts/migrate_combat_data.py`
- **_npc_has_full_combat_data()** (3 connections) — `server/scripts/migrate_combat_data.py`
- **_npc_has_combat_data()** (3 connections) — `server/scripts/migrate_combat_data.py`
- **Validate combat data for an NPC definition.      Args:         npc_definition: N** (1 connections) — `server/schemas/combat/combat_schema.py`
- **Exception** (1 connections)
- **Combat data migration script.  This script adds default combat data to existing** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Migrate combat data for all NPC definitions.      Args:         session: Databas** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Validate that migration was successful.      Args:         session: Database ses** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Rollback combat data migration by removing combat fields.      Args:         ses** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Main migration function.** (1 connections) — `server/scripts/migrate_combat_data.py`

## Relationships

- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (14 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (9 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (3 shared connections)
- [Realtime Errors Error](Realtime_Errors_Error.md) (2 shared connections)

## Source Files

- `server/schemas/combat/combat_schema.py`
- `server/scripts/migrate_combat_data.py`

## Audit Trail

- EXTRACTED: 113 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*