# Combat NPC Lookup

> 129 nodes

## Key Concepts

- **StatusEffect** (32 connections) — `server/models/game.py`
- **Player** (26 connections) — `server/models/game.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **InventoryItem** (19 connections) — `server/models/game.py`
- **test_player_schema_converter_weapon.py** (19 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **test_game_status_effect.py** (13 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **_weapon_from_prototype_registry()** (12 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **Any** (11 connections)
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_dict()** (10 connections) — `server/game/player_schema_converter.py`
- **.convert_player_to_schema()** (8 connections) — `server/game/player_schema_converter.py`
- **WeaponStats** (7 connections) — `server/models/game.py`
- **.get_position_state()** (6 connections) — `server/game/player_schema_converter.py`
- **test_game_inventory_item.py** (6 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **.item_prototype_registry()** (5 connections) — `server/commands/combat_handler.py`
- **.check_player_combat_state()** (5 connections) — `server/game/player_schema_converter.py`
- **.get_profession_details()** (5 connections) — `server/game/player_schema_converter.py`
- **.compute_derived_stats_fields()** (5 connections) — `server/game/player_schema_converter.py`
- **BaseModel** (5 connections)
- **test_inventory_item_with_weapon_with_registry_weapon()** (5 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **.get_player_data_methods()** (4 connections) — `server/game/player_schema_converter.py`
- **.get_active_status_effects()** (4 connections) — `server/models/game.py`
- **test_weapon_from_prototype_registry_missing_prototype_returns_none()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- *... and 104 more nodes in this community*

## Relationships

- [Application Config Settings](Application_Config_Settings.md) (9 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (8 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (6 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (6 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (5 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (5 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (3 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)
- [NPC Movement Integration](NPC_Movement_Integration.md) (2 shared connections)
- [Memory Profiler Tools](Memory_Profiler_Tools.md) (2 shared connections)
- [Npc Services Combat](Npc_Services_Combat.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/game/player_schema_converter.py`
- `server/models/game.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/models/test_game_inventory_item.py`
- `server/tests/unit/models/test_game_player.py`
- `server/tests/unit/models/test_game_status_effect.py`

## Audit Trail

- EXTRACTED: 446 (95%)
- INFERRED: 25 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*