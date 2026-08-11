# Combat NPC Lookup

> 97 nodes

## Key Concepts

- **StatusEffect** (32 connections) — `server/models/game.py`
- **Player** (26 connections) — `server/models/game.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **InventoryItem** (19 connections) — `server/models/game.py`
- **test_game_status_effect.py** (13 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **test_game_inventory_item.py** (6 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **.is_active()** (5 connections) — `server/models/game.py`
- **test_inventory_item_with_weapon_with_registry_weapon()** (5 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **.get_active_status_effects()** (4 connections) — `server/models/game.py`
- **.__init__()** (4 connections) — `server/models/invite.py`
- **_npc_alive_and_active()** (4 connections) — `server/npc/idle_movement.py`
- **.is_alive()** (4 connections) — `server/npc/npc_base.py`
- **test_inventory_item_with_weapon_minimal_dict()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
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
- *... and 72 more nodes in this community*

## Relationships

- [Combat Attack Service](Combat_Attack_Service.md) (7 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (7 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (6 shared connections)
- [test_profession_meets_stat_requirements_multiple_not_met](test_profession_meets_stat_requirements_multiple_not_met.md) (5 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (4 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (3 shared connections)
- [System Monitoring API](System_Monitoring_API.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Monitoring Response Models](Monitoring_Response_Models.md) (1 shared connections)
- [Memory Profiler Tools](Memory_Profiler_Tools.md) (1 shared connections)

## Source Files

- `server/game/player_schema_converter.py`
- `server/models/game.py`
- `server/models/invite.py`
- `server/npc/idle_movement.py`
- `server/npc/npc_base.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/models/test_game_inventory_item.py`
- `server/tests/unit/models/test_game_player.py`
- `server/tests/unit/models/test_game_status_effect.py`

## Audit Trail

- EXTRACTED: 306 (95%)
- INFERRED: 17 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*