# tools generate invite

> 16 nodes

## Key Concepts

- **migrate_combat_data.py** (15 connections) — `server/scripts/migrate_combat_data.py`
- **migrate_npc_combat_data()** (10 connections) — `server/scripts/migrate_combat_data.py`
- **add_default_combat_data_to_config()** (8 connections) — `server/schemas/combat/combat_schema.py`
- **validate_migration_results()** (8 connections) — `server/scripts/migrate_combat_data.py`
- **rollback_migration()** (7 connections) — `server/scripts/migrate_combat_data.py`
- **main()** (6 connections) — `server/scripts/migrate_combat_data.py`
- **AsyncSession** (3 connections)
- **Any** (3 connections)
- **test_add_default_combat_data_to_config()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **Add default combat data to behavior_config if not present.      Args:         co** (1 connections) — `server/schemas/combat/combat_schema.py`
- **Combat data migration script.  This script adds default combat data to existing** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Migrate combat data for all NPC definitions.      Args:         session: Databas** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Validate that migration was successful.      Args:         session: Database ses** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Rollback combat data migration by removing combat fields.      Args:         ses** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Main migration function.** (1 connections) — `server/scripts/migrate_combat_data.py`
- **Test add_default_combat_data_to_config() adds defaults.** (1 connections) — `server/tests/unit/schemas/test_combat_schema.py`

## Relationships

- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (14 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)

## Source Files

- `server/schemas/combat/combat_schema.py`
- `server/scripts/migrate_combat_data.py`
- `server/tests/unit/schemas/test_combat_schema.py`

## Audit Trail

- EXTRACTED: 64 (91%)
- INFERRED: 6 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*