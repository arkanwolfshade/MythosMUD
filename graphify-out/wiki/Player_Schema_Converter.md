# Player Schema Converter

> 49 nodes · cohesion 0.07

## Key Concepts

- **PlayerSchemaConverter** (20 connections) — `server/game/player_schema_converter.py`
- **test_player_schema_converter_weapon.py** (15 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **_inventory_item_with_weapon()** (12 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_object()** (11 connections) — `server/game/player_schema_converter.py`
- **_weapon_from_prototype_registry()** (11 connections) — `server/game/player_schema_converter.py`
- **Any** (11 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_dict()** (9 connections) — `server/game/player_schema_converter.py`
- **.convert_player_to_schema()** (8 connections) — `server/game/player_schema_converter.py`
- **.get_position_state()** (6 connections) — `server/game/player_schema_converter.py`
- **.check_player_combat_state()** (4 connections) — `server/game/player_schema_converter.py`
- **.compute_derived_stats_fields()** (4 connections) — `server/game/player_schema_converter.py`
- **.get_player_data_methods()** (4 connections) — `server/game/player_schema_converter.py`
- **.get_profession_details()** (4 connections) — `server/game/player_schema_converter.py`
- **test_weapon_from_prototype_registry_missing_prototype_returns_none()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **.__init__()** (3 connections) — `server/game/player_schema_converter.py`
- **test_create_player_read_from_object_enriches_inventory_weapon()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_minimal_dict()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_uses_prototype_id_for_lookup()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_with_registry_weapon()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_empty_prototype_id_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_no_metadata_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_none_registry_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_weapon_present_returns_dict()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **PlayerRead** (3 connections) — `server/game/player_schema_converter.py`
- **Get stats, inventory, and status_effects from player, handling async methods.** (1 connections) — `server/game/player_schema_converter.py`
- *... and 24 more nodes in this community*

## Relationships

- [[NPC Admin API]] (4 shared connections)
- [[Combat Command Handler]] (4 shared connections)
- [[Game Inventory Item]] (2 shared connections)
- [[Player Creation Service]] (2 shared connections)
- [[Character Stats Model]] (2 shared connections)
- [[Status Effect Model]] (2 shared connections)
- [[Weapon Resolution Helpers]] (2 shared connections)

## Source Files

- `server/game/player_schema_converter.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`

## Audit Trail

- EXTRACTED: 173 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
