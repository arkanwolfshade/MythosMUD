# NATS Anti Patterns Review 2026

> 12 nodes

## Key Concepts

- **migrate_combat_data.py** (15 connections) — `server/scripts/migrate_combat_data.py`
- **migrate_npc_combat_data()** (10 connections) — `server/scripts/migrate_combat_data.py`
- **validate_migration_results()** (8 connections) — `server/scripts/migrate_combat_data.py`
- **rollback_migration()** (7 connections) — `server/scripts/migrate_combat_data.py`
- **main()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **AsyncSession** (3 connections)
- **Any** (3 connections)
- **Combat data migration script.  This script adds default combat data to existing** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Migrate combat data for all NPC definitions.      Args:         session: Databas** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Validate that migration was successful.      Args:         session: Database ses** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Rollback combat data migration by removing combat fields.      Args:         ses** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Main migration function.** (1 connections) — `server/scripts/migrate_combat_data.py`

## Relationships

- [Any](Any.md) (11 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (5 shared connections)
- [test admin commands](test_admin_commands.md) (3 shared connections)
- [world](world.md) (2 shared connections)

## Source Files

- `server/scripts/migrate_combat_data.py`

## Audit Trail

- EXTRACTED: 51 (89%)
- INFERRED: 6 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*