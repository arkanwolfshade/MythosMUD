# StatusEffect

> 84 nodes

## Key Concepts

- **StatusEffect** (32 connections) — `server/models/game.py`
- **Player** (29 connections) — `server/models/game.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **InventoryItem** (18 connections) — `server/models/game.py`
- **test_game_status_effect.py** (13 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_game_inventory_item.py** (6 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **._status_effects_list()** (5 connections) — `server/models/game.py`
- **BaseModel** (5 connections)
- **.add_item()** (4 connections) — `server/models/game.py`
- **.add_status_effect()** (4 connections) — `server/models/game.py`
- **.get_active_status_effects()** (4 connections) — `server/models/game.py`
- **._inventory_list()** (4 connections) — `server/models/game.py`
- **.remove_status_effect()** (4 connections) — `server/models/game.py`
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
- *... and 59 more nodes in this community*

## Relationships

- [server/dependencies.py](server-dependencies.py.md) (11 shared connections)
- [TargetType](TargetType.md) (5 shared connections)
- [PlayerSchemaConverter](PlayerSchemaConverter.md) (3 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (3 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [_weapon_from_prototype_registry](_weapon_from_prototype_registry.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/models/test_game_inventory_item.py`
- `server/tests/unit/models/test_game_player.py`
- `server/tests/unit/models/test_game_status_effect.py`

## Audit Trail

- EXTRACTED: 162 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*