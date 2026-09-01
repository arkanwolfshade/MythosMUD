# Player

> 55 nodes

## Key Concepts

- **Player** (29 connections) — `server/models/game.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **InventoryItem** (18 connections) — `server/models/game.py`
- **WeaponStats** (5 connections) — `server/models/game.py`
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
- **.can_carry_weight()** (3 connections) — `server/models/game.py`
- **._player_stats()** (3 connections) — `server/models/game.py`
- **.remove_item()** (3 connections) — `server/models/game.py`
- **test_inventory_item_creation()** (3 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **test_inventory_item_default_quantity()** (3 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **test_inventory_item_quantity_validation_min()** (3 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **test_player_add_item_default_quantity()** (3 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_add_item_new()** (3 connections) — `server/tests/unit/models/test_game_player.py`
- *... and 30 more nodes in this community*

## Relationships

- [StatusEffect](StatusEffect.md) (10 shared connections)
- [Stats](Stats.md) (9 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (5 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)
- [test_player_schemas.py](test_player_schemas.py.md) (1 shared connections)
- [time.py](time.py.md) (1 shared connections)
- [TargetMatch](TargetMatch.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/models/test_game_inventory_item.py`
- `server/tests/unit/models/test_game_player.py`

## Audit Trail

- EXTRACTED: 110 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*