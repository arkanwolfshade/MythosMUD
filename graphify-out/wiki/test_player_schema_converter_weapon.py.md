# test_player_schema_converter_weapon.py

> 24 nodes

## Key Concepts

- **test_player_schema_converter_weapon.py** (20 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **_weapon_from_prototype_registry()** (11 connections) — `server/game/player_schema_converter.py`
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
- **WeaponStats** (1 connections)
- **Resolve metadata.weapon from prototype registry for a given prototype_id.…** (1 connections) — `server/game/player_schema_converter.py`
- **Unit tests for PlayerSchemaConverter weapon stats enrichment.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **When converter has registry, inventory items with weapon prototype get weapon…** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **When registry is None, returns None.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **When prototype_id is empty, returns None.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **When prototype is not found, returns None.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **When prototype has no metadata.weapon, returns None.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **When prototype has metadata.weapon, returns weapon dict.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **Build InventoryItem from minimal dict (item_id, quantity) without registry.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **Build InventoryItem with weapon stats when prototype has metadata.weapon.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **When both item_id and prototype_id present, use prototype_id for registry…** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`

## Relationships

- [PlayerSchemaConverter](PlayerSchemaConverter.md) (8 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/player_schema_converter.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`

## Audit Trail

- EXTRACTED: 43 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*