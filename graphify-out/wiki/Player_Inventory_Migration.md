# Player Inventory Migration

> 9 nodes · cohesion 0.28

## Key Concepts

- **player_inventory_migration.py** (5 connections) — `server/scripts/player_inventory_migration.py`
- **migrate_multiple()** (4 connections) — `server/scripts/player_inventory_migration.py`
- **migrate_player_inventories()** (4 connections) — `server/scripts/player_inventory_migration.py`
- **parse_args()** (2 connections) — `server/scripts/player_inventory_migration.py`
- **Path** (2 connections) — `server/scripts/player_inventory_migration.py`
- **Create and backfill the player_inventories table.** (1 connections) — `server/scripts/player_inventory_migration.py`
- **Ensure the player_inventories table exists and is populated for existing players** (1 connections) — `server/scripts/player_inventory_migration.py`
- **Run the migration across multiple database paths.** (1 connections) — `server/scripts/player_inventory_migration.py`
- **Namespace** (1 connections) — `server/scripts/player_inventory_migration.py`

## Relationships

- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/scripts/player_inventory_migration.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
