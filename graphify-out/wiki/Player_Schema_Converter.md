# Player Schema Converter

> 55 nodes

## Key Concepts

- **player_schema_converter.py** (22 connections) — `server/game/player_schema_converter.py`
- **test_player_schema_converter_weapon.py** (20 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **_weapon_from_prototype_registry()** (11 connections) — `server/game/player_schema_converter.py`
- **Any** (11 connections)
- **.create_player_read_from_dict()** (10 connections) — `server/game/player_schema_converter.py`
- **.convert_player_to_schema()** (8 connections) — `server/game/player_schema_converter.py`
- **weapon.py** (7 connections) — `server/schemas/game/weapon.py`
- **.get_position_state()** (6 connections) — `server/game/player_schema_converter.py`
- **WeaponStats** (5 connections) — `server/models/game.py`
- **.item_prototype_registry()** (5 connections) — `server/commands/combat_handler.py`
- **BaseModel** (5 connections)
- **.check_player_combat_state()** (4 connections) — `server/game/player_schema_converter.py`
- **.compute_derived_stats_fields()** (4 connections) — `server/game/player_schema_converter.py`
- **.get_player_data_methods()** (4 connections) — `server/game/player_schema_converter.py`
- **.get_profession_details()** (4 connections) — `server/game/player_schema_converter.py`
- **test_create_player_read_from_object_enriches_inventory_weapon()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_missing_prototype_returns_none()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **.__init__()** (3 connections) — `server/game/player_schema_converter.py`
- **test_inventory_item_with_weapon_minimal_dict()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_uses_prototype_id_for_lookup()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_with_registry_weapon()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_empty_prototype_id_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- *... and 30 more nodes in this community*

## Relationships

- [Test Game Player](Test_Game_Player.md) (5 shared connections)
- [Item Factory](Item_Factory.md) (5 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (4 shared connections)
- [Game](Game.md) (4 shared connections)
- [Test Player Schemas](Test_Player_Schemas.md) (4 shared connections)
- [Stats Generator](Stats_Generator.md) (4 shared connections)
- [Test Game Status Effect](Test_Game_Status_Effect.md) (4 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (3 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Container/Inventory Helpers](Container-Inventory_Helpers.md) (2 shared connections)
- [Combat Handler](Combat_Handler.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/game/player_schema_converter.py`
- `server/models/game.py`
- `server/schemas/game/weapon.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`

## Audit Trail

- EXTRACTED: 129 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*