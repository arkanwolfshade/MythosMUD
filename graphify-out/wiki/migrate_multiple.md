# migrate_multiple

> 5 nodes

## Key Concepts

- **migrate_multiple()** (4 connections) — `server/scripts/player_inventory_migration.py`
- **migrate_player_inventories()** (4 connections) — `server/scripts/player_inventory_migration.py`
- **Path** (2 connections)
- **Ensure the player_inventories table exists and is populated for existing…** (1 connections) — `server/scripts/player_inventory_migration.py`
- **Run the migration across multiple database paths.** (1 connections) — `server/scripts/player_inventory_migration.py`

## Relationships

- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/scripts/player_inventory_migration.py`

## Audit Trail

- EXTRACTED: 7 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*