# Game Inventory Item

> 10 nodes · cohesion 0.27

## Key Concepts

- **InventoryItem** (17 connections) — `server/models/game.py`
- **test_game_inventory_item.py** (5 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **test_inventory_item_creation()** (3 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **test_inventory_item_default_quantity()** (3 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **test_inventory_item_quantity_validation_min()** (3 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **Represents an item in a player's inventory.** (1 connections) — `server/models/game.py`
- **Unit tests for InventoryItem model.** (1 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **Test InventoryItem can be created with required fields.** (1 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **Test InventoryItem defaults quantity to 1.** (1 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **Test InventoryItem validates quantity is >= 1.** (1 connections) — `server/tests/unit/models/test_game_inventory_item.py`

## Relationships

- [[Player Model Inventory]] (6 shared connections)
- [[Admin NPC Schemas]] (2 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Player Schema Converter]] (2 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/models/test_game_inventory_item.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
