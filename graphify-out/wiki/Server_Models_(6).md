# Server Models (6)

> 104 nodes

## Key Concepts

- **game.py** (32 connections) — `server/models/game.py`
- **StatusEffect** (32 connections) — `server/models/game.py`
- **Player** (26 connections) — `server/models/game.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **spell_effects_support.py** (19 connections) — `server/game/magic/spell_effects_support.py`
- **InventoryItem** (19 connections) — `server/models/game.py`
- **test_game_status_effect.py** (13 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **process_stat_modify_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **process_create_object_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **_apply_stat_modify_to_player()** (8 connections) — `server/game/magic/spell_effects_support.py`
- **Any** (6 connections)
- **_create_object_for_room()** (6 connections) — `server/game/magic/spell_effects_support.py`
- **test_game_inventory_item.py** (6 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **_build_stat_modifications()** (5 connections) — `server/game/magic/spell_effects_support.py`
- **_create_object_for_player()** (5 connections) — `server/game/magic/spell_effects_support.py`
- **BaseModel** (5 connections)
- **.is_active()** (5 connections) — `server/models/game.py`
- **apply_stat_modifications()** (4 connections) — `server/game/magic/spell_effects_stats.py`
- **.get_active_status_effects()** (4 connections) — `server/models/game.py`
- **_npc_alive_and_active()** (4 connections) — `server/npc/idle_movement.py`
- **.is_alive()** (4 connections) — `server/npc/npc_base.py`
- **test_inventory_item_quantity_validation_min()** (4 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **test_player_add_item_existing()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_item_success()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_item_removes_when_zero()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- *... and 79 more nodes in this community*

## Relationships

- [Server Game](Server_Game.md) (13 shared connections)
- [Server Game (2)](Server_Game_%282%29.md) (10 shared connections)
- [Server Game (24)](Server_Game_%2824%29.md) (8 shared connections)
- [Server Models (13)](Server_Models_%2813%29.md) (6 shared connections)
- [Server Services](Server_Services.md) (6 shared connections)
- [Server Models (12)](Server_Models_%2812%29.md) (6 shared connections)
- [Server Commands](Server_Commands.md) (5 shared connections)
- [Server Utils](Server_Utils.md) (5 shared connections)
- [Server Api (3)](Server_Api_%283%29.md) (4 shared connections)
- [Server Game (7)](Server_Game_%287%29.md) (3 shared connections)
- [Server Models (14)](Server_Models_%2814%29.md) (2 shared connections)
- [Server Utils (11)](Server_Utils_%2811%29.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_support.py`
- `server/models/game.py`
- `server/npc/idle_movement.py`
- `server/npc/npc_base.py`
- `server/tests/unit/models/test_game_inventory_item.py`
- `server/tests/unit/models/test_game_player.py`
- `server/tests/unit/models/test_game_status_effect.py`

## Audit Trail

- EXTRACTED: 390 (97%)
- INFERRED: 13 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*