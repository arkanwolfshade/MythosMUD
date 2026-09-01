# PrototypeRegistryError

> 51 nodes

## Key Concepts

- **PrototypeRegistryError** (25 connections) — `server/game/items/prototype_registry.py`
- **prototype_registry.py** (23 connections) — `server/game/items/prototype_registry.py`
- **player_schema_converter.py** (22 connections) — `server/game/player_schema_converter.py`
- **test_player_schema_converter_weapon.py** (20 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **ItemFactory** (19 connections) — `server/game/items/item_factory.py`
- **item_factory.py** (16 connections) — `server/game/items/item_factory.py`
- **ItemFactoryError** (12 connections) — `server/game/items/item_factory.py`
- **test_item_factory.py** (12 connections) — `server/tests/unit/game/test_item_factory.py`
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **_weapon_from_prototype_registry()** (11 connections) — `server/game/player_schema_converter.py`
- **items/__init__.py** (11 connections) — `server/game/items/__init__.py`
- **weapon.py** (7 connections) — `server/schemas/game/weapon.py`
- **test_create_instance_prototype_not_found()** (4 connections) — `server/tests/unit/game/test_item_factory.py`
- **test_weapon_from_prototype_registry_missing_prototype_returns_none()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **.__init__()** (3 connections) — `server/game/items/item_factory.py`
- **factory()** (3 connections) — `server/tests/unit/game/test_item_factory.py`
- **test_create_instance_invalid_quantity()** (3 connections) — `server/tests/unit/game/test_item_factory.py`
- **test_inventory_item_with_weapon_minimal_dict()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_uses_prototype_id_for_lookup()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_with_registry_weapon()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_empty_prototype_id_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_no_metadata_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_none_registry_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_weapon_present_returns_dict()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_create_instance_success()** (2 connections) — `server/tests/unit/game/test_item_factory.py`
- *... and 26 more nodes in this community*

## Relationships

- [PrototypeRegistry](PrototypeRegistry.md) (12 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (9 shared connections)
- [PlayerSchemaConverter](PlayerSchemaConverter.md) (7 shared connections)
- [admin_summon_command.py](admin_summon_command.py.md) (6 shared connections)
- [test_inventory_command_prototype.py](test_inventory_command_prototype.py.md) (6 shared connections)
- [Player](Player.md) (6 shared connections)
- [initialize_components](initialize_components.md) (5 shared connections)
- [ItemInstance](ItemInstance.md) (5 shared connections)
- [Stats](Stats.md) (5 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [ItemPrototypeModel](ItemPrototypeModel.md) (2 shared connections)

## Source Files

- `server/game/items/__init__.py`
- `server/game/items/item_factory.py`
- `server/game/items/prototype_registry.py`
- `server/game/player_schema_converter.py`
- `server/schemas/game/weapon.py`
- `server/tests/unit/game/test_item_factory.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`

## Audit Trail

- EXTRACTED: 157 (91%)
- INFERRED: 15 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*