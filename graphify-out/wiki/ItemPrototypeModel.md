# ItemPrototypeModel

> 59 nodes

## Key Concepts

- **ItemPrototypeModel** (28 connections) — `server/game/items/models.py`
- **resolve_weapon_attack_from_equipped()** (24 connections) — `server/game/weapons.py`
- **prototype_registry.py** (22 connections) — `server/game/items/prototype_registry.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **weapons.py** (17 connections) — `server/game/weapons.py`
- **test_combat_weapon_resolution.py** (12 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **WeaponAttackInfo** (10 connections) — `server/game/weapons.py`
- **items/models.py** (10 connections) — `server/game/items/models.py`
- **field_validator** (5 connections)
- **_prototype_from_equipped_stack()** (4 connections) — `server/game/weapons.py`
- **registry_with_switchblade()** (4 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **switchblade_prototype()** (4 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_resolve_weapon_attack_from_equipped_registry_error_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **.validate_effect_components()** (3 connections) — `server/game/items/models.py`
- **.validate_flags()** (3 connections) — `server/game/items/models.py`
- **.validate_item_type()** (3 connections) — `server/game/items/models.py`
- **.validate_tags()** (3 connections) — `server/game/items/models.py`
- **.validate_wear_slots()** (3 connections) — `server/game/items/models.py`
- **_roll_weapon_attack()** (3 connections) — `server/game/weapons.py`
- **test_weapon_resolution_switchblade_damage_in_range()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_weapon_resolution_switchblade_no_main_hand_returns_none()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_resolve_weapon_attack_from_equipped_empty_damage_types_uses_physical()** (3 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_missing_prototype_id_returns_none()** (3 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_no_weapon_metadata_returns_none()** (3 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_none_registry_returns_none()** (3 connections) — `server/tests/unit/game/test_weapons.py`
- *... and 34 more nodes in this community*

## Relationships

- [PrototypeRegistry](PrototypeRegistry.md) (18 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (11 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_item_prototype_models.py](test_item_prototype_models.py.md) (3 shared connections)
- [test_inventory_command_prototype.py](test_inventory_command_prototype.py.md) (3 shared connections)
- [combat_attack.py](combat_attack.py.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (2 shared connections)
- [player_schema_converter.py](player_schema_converter.py.md) (2 shared connections)

## Source Files

- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/game/weapons.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 141 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*