# Community 480

> 37 nodes

## Key Concepts

- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_object()** (11 connections) — `server/game/player_schema_converter.py`
- **Any** (11 connections)
- **.convert_player_to_schema()** (8 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_dict()** (8 connections) — `server/game/player_schema_converter.py`
- **.get_position_state()** (6 connections) — `server/game/player_schema_converter.py`
- **.item_prototype_registry()** (5 connections) — `server/commands/combat_handler.py`
- **.check_player_combat_state()** (4 connections) — `server/game/player_schema_converter.py`
- **.compute_derived_stats_fields()** (4 connections) — `server/game/player_schema_converter.py`
- **.get_player_data_methods()** (4 connections) — `server/game/player_schema_converter.py`
- **.get_profession_details()** (4 connections) — `server/game/player_schema_converter.py`
- **test_create_player_read_from_object_enriches_inventory_weapon()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **.__init__()** (3 connections) — `server/game/player_schema_converter.py`
- **test_inventory_item_with_weapon_minimal_dict()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_uses_prototype_id_for_lookup()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_with_registry_weapon()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **PlayerRead** (3 connections)
- **InventoryItem** (1 connections)
- **PositionState** (1 connections)
- **asyncio** (1 connections)
- **Item prototype registry for command modules.** (1 connections) — `server/commands/combat_handler.py`
- **Get stats, inventory, and status_effects from player, handling async methods.** (1 connections) — `server/game/player_schema_converter.py`
- **Compute derived stats fields (max_dp, max_magic_points, max_lucidity). Returns…** (1 connections) — `server/game/player_schema_converter.py`
- **Get PositionState from position value, with fallback to STANDING.** (1 connections) — `server/game/player_schema_converter.py`
- *... and 12 more nodes in this community*

## Relationships

- [Container API Models](Container_API_Models.md) (8 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (3 shared connections)
- [API Response Models](API_Response_Models.md) (2 shared connections)
- [Community 263](Community_263.md) (1 shared connections)
- [Community 415](Community_415.md) (1 shared connections)
- [Community 207](Community_207.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/game/player_schema_converter.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`

## Audit Trail

- EXTRACTED: 67 (92%)
- INFERRED: 6 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*