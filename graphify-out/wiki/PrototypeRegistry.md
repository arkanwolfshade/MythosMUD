# PrototypeRegistry

> 88 nodes

## Key Concepts

- **PrototypeRegistry** (47 connections) — `server/game/items/prototype_registry.py`
- **ItemPrototypeModel** (43 connections) — `server/game/items/models.py`
- **PrototypeRegistryError** (25 connections) — `server/game/items/prototype_registry.py`
- **resolve_weapon_attack_from_equipped()** (25 connections) — `server/game/weapons.py`
- **prototype_registry.py** (22 connections) — `server/game/items/prototype_registry.py`
- **player_schema_converter.py** (21 connections) — `server/game/player_schema_converter.py`
- **test_player_schema_converter_weapon.py** (19 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **weapons.py** (17 connections) — `server/game/weapons.py`
- **test_prototype_registry.py** (17 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_combat_weapon_resolution.py** (12 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **items/models.py** (11 connections) — `server/game/items/models.py`
- **WeaponAttackInfo** (9 connections) — `server/game/weapons.py`
- **validate_prototypes.py** (8 connections) — `server/scripts/validate_prototypes.py`
- **weapon.py** (7 connections) — `server/schemas/game/weapon.py`
- **_prototype_from_equipped_stack()** (6 connections) — `server/game/weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_returns_info_in_range()** (6 connections) — `server/tests/unit/game/test_weapons.py`
- **.get()** (5 connections) — `server/game/items/prototype_registry.py`
- **_make_prototype()** (5 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_resolve_weapon_attack_from_equipped_empty_damage_types_uses_physical()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_no_weapon_metadata_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_registry_error_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_missing_min_max_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_with_modifier()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **Path** (5 connections)
- *... and 63 more nodes in this community*

## Relationships

- [ItemFactory](ItemFactory.md) (13 shared connections)
- [test_item_prototype_models.py](test_item_prototype_models.py.md) (11 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [_weapon_from_prototype_registry](_weapon_from_prototype_registry.md) (8 shared connections)
- [PlayerSchemaConverter](PlayerSchemaConverter.md) (8 shared connections)
- [.load_from_path](load_from_path.md) (7 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (7 shared connections)
- [test_inventory_command_prototype.py](test_inventory_command_prototype.py.md) (6 shared connections)
- [catalog_dml.py](catalog_dml.py.md) (5 shared connections)
- [field_validator](field_validator.md) (5 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (5 shared connections)
- [combat_attack.py](combat_attack.py.md) (3 shared connections)

## Source Files

- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/game/player_schema_converter.py`
- `server/game/weapons.py`
- `server/schemas/game/weapon.py`
- `server/scripts/validate_prototypes.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/items/test_prototype_registry.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 239 (83%)
- INFERRED: 50 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*