# Player Model Inventory

> 44 nodes · cohesion 0.06

## Key Concepts

- **Player** (26 connections) — `server/models/game.py`
- **test_game_player.py** (21 connections) — `server/tests/unit/models/test_game_player.py`
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
- **.add_item()** (3 connections) — `server/models/game.py`
- **.remove_status_effect()** (3 connections) — `server/models/game.py`
- **test_player_add_item_default_quantity()** (3 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_add_item_new()** (3 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_item_not_found()** (3 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_status_effect_not_found()** (3 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_update_last_active()** (3 connections) — `server/tests/unit/models/test_game_player.py`
- **.can_carry_weight()** (2 connections) — `server/models/game.py`
- **.remove_item()** (2 connections) — `server/models/game.py`
- **.update_last_active()** (2 connections) — `server/models/game.py`
- **Pydantic Player model for game logic and validation.      This is separate from** (1 connections) — `server/models/game.py`
- **Add an item to the player's inventory.          Args:             item_id: Uniqu** (1 connections) — `server/models/game.py`
- **Remove an item from the player's inventory.          Args:             item_id:** (1 connections) — `server/models/game.py`
- *... and 19 more nodes in this community*

## Relationships

- [[Status Effect Model]] (7 shared connections)
- [[Game Inventory Item]] (6 shared connections)
- [[Character Stats Model]] (3 shared connections)
- [[Game Magic Spell]] (2 shared connections)
- [[Admin NPC Schemas]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/models/test_game_player.py`

## Audit Trail

- EXTRACTED: 136 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
