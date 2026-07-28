# Player Combat XP

> 112 nodes · cohesion 0.03

## Key Concepts

- **game.py** (32 connections) — `server/models/game.py`
- **StatusEffect** (32 connections) — `server/models/game.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **Player** (26 connections) — `server/models/game.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **InventoryItem** (19 connections) — `server/models/game.py`
- **test_game_status_effect.py** (13 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_game_enums.py** (11 connections) — `server/tests/unit/models/test_game_enums.py`
- **AttributeType** (8 connections) — `server/models/game.py`
- **WeaponStats** (7 connections) — `server/models/game.py`
- **test_game_inventory_item.py** (6 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **BaseModel** (5 connections)
- **.is_active()** (5 connections) — `server/models/game.py`
- **test_inventory_item_with_weapon_with_registry_weapon()** (5 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **.get_active_status_effects()** (4 connections) — `server/models/game.py`
- **test_create_player_read_from_object_enriches_inventory_weapon()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_minimal_dict()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_quantity_validation_min()** (4 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **test_player_add_item_existing()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_add_status_effect()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_can_carry_weight_false()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_can_carry_weight_true()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_get_active_status_effects()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_get_active_status_effects_all_active()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_item_insufficient_quantity()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- *... and 87 more nodes in this community*

## Relationships

- [Character Stats Model](Character_Stats_Model.md) (35 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (12 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (9 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (8 shared connections)
- [Item System Design](Item_System_Design.md) (5 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (5 shared connections)
- [System Monitoring API](System_Monitoring_API.md) (4 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (3 shared connections)
- [Communication Command Handlers](Communication_Command_Handlers.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Memory Profiler Tools](Memory_Profiler_Tools.md) (2 shared connections)
- [Combat Flee Command](Combat_Flee_Command.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/models/test_game_enums.py`
- `server/tests/unit/models/test_game_inventory_item.py`
- `server/tests/unit/models/test_game_player.py`
- `server/tests/unit/models/test_game_stats_methods.py`
- `server/tests/unit/models/test_game_status_effect.py`

## Audit Trail

- EXTRACTED: 399 (96%)
- INFERRED: 17 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*