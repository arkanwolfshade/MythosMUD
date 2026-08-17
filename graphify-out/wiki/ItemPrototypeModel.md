# ItemPrototypeModel

> 40 nodes

## Key Concepts

- **ItemPrototypeModel** (39 connections) — `server/game/items/models.py`
- **test_item_prototype_models.py** (15 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_combat_weapon_resolution.py** (13 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **items/models.py** (11 connections) — `server/game/items/models.py`
- **_valid_payload()** (9 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **field_validator** (5 connections)
- **registry_with_switchblade()** (4 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **switchblade_prototype()** (4 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **.validate_effect_components()** (3 connections) — `server/game/items/models.py`
- **.validate_flags()** (3 connections) — `server/game/items/models.py`
- **.validate_item_type()** (3 connections) — `server/game/items/models.py`
- **.validate_tags()** (3 connections) — `server/game/items/models.py`
- **.validate_wear_slots()** (3 connections) — `server/game/items/models.py`
- **.all()** (3 connections) — `server/game/items/prototype_registry.py`
- **test_weapon_resolution_switchblade_no_main_hand_returns_none()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_item_prototype_accepts_valid_flags()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_accepts_valid_wear_slots()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_normalizes_effect_components_and_tags()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_empty_effect_components()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_invalid_flags()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_invalid_item_type()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_invalid_wear_slots()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_valid_minimal()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **constants.py** (3 connections) — `server/game/items/constants.py`
- **fixture** (2 connections)
- *... and 15 more nodes in this community*

## Relationships

- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (15 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (10 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (5 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [test_inventory_command_prototype.py](test_inventory_command_prototype.py.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)

## Source Files

- `server/game/items/constants.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/items/test_item_prototype_models.py`

## Audit Trail

- EXTRACTED: 82 (81%)
- INFERRED: 19 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*