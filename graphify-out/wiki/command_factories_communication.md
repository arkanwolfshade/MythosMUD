# command factories communication

> 61 nodes

## Key Concepts

- **Player** (26 connections) — `server/models/game.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **InventoryItem** (19 connections) — `server/models/game.py`
- **WeaponStats** (7 connections) — `server/models/game.py`
- **test_game_inventory_item.py** (6 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **BaseModel** (5 connections)
- **test_inventory_item_with_weapon_with_registry_weapon()** (5 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_minimal_dict()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_create_player_read_from_object_enriches_inventory_weapon()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_quantity_validation_min()** (4 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **test_player_add_item_existing()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_item_success()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_item_removes_when_zero()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_item_insufficient_quantity()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_add_status_effect()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_status_effect_success()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_get_active_status_effects()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_get_active_status_effects_all_active()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_can_carry_weight_true()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_can_carry_weight_false()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **.add_item()** (3 connections) — `server/models/game.py`
- **test_inventory_item_creation()** (3 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **test_inventory_item_default_quantity()** (3 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **test_player_add_item_new()** (3 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_add_item_default_quantity()** (3 connections) — `server/tests/unit/models/test_game_player.py`
- *... and 36 more nodes in this community*

## Relationships

- [player service game](player_service_game.md) (8 shared connections)
- [models invite Any](models_invite_Any.md) (8 shared connections)
- [npc spawn validator](npc_spawn_validator.md) (6 shared connections)
- [combat models rationale](combat_models_rationale.md) (5 shared connections)
- [character creation service](character_creation_service.md) (2 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)
- [profession game service](profession_game_service.md) (1 shared connections)
- [command inventory models](command_inventory_models.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/models/test_game_inventory_item.py`
- `server/tests/unit/models/test_game_player.py`

## Audit Trail

- EXTRACTED: 193 (95%)
- INFERRED: 10 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*