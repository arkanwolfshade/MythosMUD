# Community 290

> 57 nodes

## Key Concepts

- **Player** (29 connections) — `server/models/game.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **InventoryItem** (15 connections) — `server/models/game.py`
- **test_game_inventory_item.py** (6 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **BaseModel** (5 connections)
- **.add_item()** (4 connections) — `server/models/game.py`
- **._inventory_list()** (4 connections) — `server/models/game.py`
- **test_player_add_item_existing()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_add_status_effect()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_can_carry_weight_false()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_can_carry_weight_true()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_get_active_status_effects()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_get_active_status_effects_all_active()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_item_insufficient_quantity()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_item_removes_when_zero()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_item_success()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_status_effect_success()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **WeaponStats** (3 connections) — `server/models/game.py`
- **.can_carry_weight()** (3 connections) — `server/models/game.py`
- **._player_stats()** (3 connections) — `server/models/game.py`
- **.remove_item()** (3 connections) — `server/models/game.py`
- **test_inventory_item_creation()** (3 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **test_inventory_item_default_quantity()** (3 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **test_inventory_item_quantity_validation_min()** (3 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **test_player_add_item_default_quantity()** (3 connections) — `server/tests/unit/models/test_game_player.py`
- *... and 32 more nodes in this community*

## Relationships

- [Community 590](Community_590.md) (10 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (7 shared connections)
- [Community 150](Community_150.md) (5 shared connections)
- [Character Creation & Professions](Character_Creation_&_Professions.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/models/test_game_inventory_item.py`
- `server/tests/unit/models/test_game_player.py`

## Audit Trail

- EXTRACTED: 107 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*