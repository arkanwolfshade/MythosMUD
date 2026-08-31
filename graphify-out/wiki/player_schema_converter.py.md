# player_schema_converter.py

> 29 nodes

## Key Concepts

- **player_schema_converter.py** (22 connections) — `server/game/player_schema_converter.py`
- **test_player_schema_converter_weapon.py** (20 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **_weapon_from_prototype_registry()** (11 connections) — `server/game/player_schema_converter.py`
- **weapon.py** (7 connections) — `server/schemas/game/weapon.py`
- **test_create_player_read_from_object_enriches_inventory_weapon()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_missing_prototype_returns_none()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_minimal_dict()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_uses_prototype_id_for_lookup()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_with_registry_weapon()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_empty_prototype_id_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_no_metadata_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_none_registry_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_weapon_present_returns_dict()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **asyncio** (1 connections)
- **Player schema conversion utilities. This module handles conversion of Player…** (1 connections) — `server/game/player_schema_converter.py`
- **Resolve metadata.weapon from prototype registry for a given prototype_id.…** (1 connections) — `server/game/player_schema_converter.py`
- **Build InventoryItem from raw item dict, enriching with weapon stats from…** (1 connections) — `server/game/player_schema_converter.py`
- **Weapon stats schema for MythosMUD. Re-exports WeaponStats from models for API…** (1 connections) — `server/schemas/game/weapon.py`
- **Unit tests for PlayerSchemaConverter weapon stats enrichment.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **When converter has registry, inventory items with weapon prototype get weapon…** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **When registry is None, returns None.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **When prototype_id is empty, returns None.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **When prototype is not found, returns None.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **When prototype has no metadata.weapon, returns None.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- *... and 4 more nodes in this community*

## Relationships

- [pytest.md](pytest.md.md) (12 shared connections)
- [PlayerSchemaConverter](PlayerSchemaConverter.md) (7 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [players/__init__.py](players-__init__.py.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [LootAllRequest](LootAllRequest.md) (1 shared connections)

## Source Files

- `server/game/player_schema_converter.py`
- `server/schemas/game/weapon.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`

## Audit Trail

- EXTRACTED: 74 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*