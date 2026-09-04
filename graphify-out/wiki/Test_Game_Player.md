# Test Game Player

> 54 nodes

## Key Concepts

- **Player** (29 connections) — `server/models/game.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **InventoryItem** (18 connections) — `server/models/game.py`
- **test_game_inventory_item.py** (8 connections) — `server/tests/unit/models/test_game_inventory_item.py`
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
- **test_player_remove_item_not_found()** (3 connections) — `server/tests/unit/models/test_game_player.py`
- *... and 29 more nodes in this community*

## Relationships

- [Test Game Status Effect](Test_Game_Status_Effect.md) (9 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (5 shared connections)
- [Game](Game.md) (4 shared connections)
- [Stats Generator](Stats_Generator.md) (4 shared connections)
- [Test Player Schemas](Test_Player_Schemas.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Command Aliases](Command_Aliases.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (1 shared connections)

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