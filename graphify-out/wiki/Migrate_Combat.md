# Migrate Combat

> 10 nodes · cohesion 0.29

## Key Concepts

- **migrate_npc_combat_data()** (8 connections) — `server/scripts/migrate_combat_data.py`
- **main()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **validate_migration_results()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **rollback_migration()** (5 connections) — `server/scripts/migrate_combat_data.py`
- **Any** (3 connections) — `server/scripts/migrate_combat_data.py`
- **AsyncSession** (3 connections) — `server/scripts/migrate_combat_data.py`
- **Validate that migration was successful.      Args:         session: Database ses** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Rollback combat data migration by removing combat fields.      Args:         ses** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Migrate combat data for all NPC definitions.      Args:         session: Databas** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Main migration function.** (1 connections) — `server/scripts/migrate_combat_data.py`

## Relationships

- [[NPC Database Sessions]] (5 shared connections)
- [[Combat Schema Validation]] (4 shared connections)

## Source Files

- `server/scripts/migrate_combat_data.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
