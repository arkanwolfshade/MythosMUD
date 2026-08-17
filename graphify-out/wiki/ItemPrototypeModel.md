# ItemPrototypeModel

> 33 nodes

## Key Concepts

- **ItemPrototypeModel** (39 connections) — `server/game/items/models.py`
- **test_item_prototype_models.py** (15 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **items/models.py** (11 connections) — `server/game/items/models.py`
- **_valid_payload()** (9 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **field_validator** (5 connections)
- **.validate_effect_components()** (3 connections) — `server/game/items/models.py`
- **.validate_flags()** (3 connections) — `server/game/items/models.py`
- **.validate_item_type()** (3 connections) — `server/game/items/models.py`
- **.validate_tags()** (3 connections) — `server/game/items/models.py`
- **.validate_wear_slots()** (3 connections) — `server/game/items/models.py`
- **.all()** (3 connections) — `server/game/items/prototype_registry.py`
- **.find_by_tag()** (3 connections) — `server/game/items/prototype_registry.py`
- **test_item_prototype_accepts_valid_flags()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_accepts_valid_wear_slots()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_normalizes_effect_components_and_tags()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_empty_effect_components()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_invalid_flags()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_invalid_item_type()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_invalid_wear_slots()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_valid_minimal()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **constants.py** (3 connections) — `server/game/items/constants.py`
- **BaseModel** (1 connections)
- **Constants supporting item prototype validation. These enumerations anchor the…** (1 connections) — `server/game/items/constants.py`
- **Pydantic models for item prototype validation. This module defines the…** (1 connections) — `server/game/items/models.py`
- **Validate and normalize effect components. Args: value: The list of effect…** (1 connections) — `server/game/items/models.py`
- *... and 8 more nodes in this community*

## Relationships

- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (13 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (8 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (4 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [test_inventory_command_prototype.py](test_inventory_command_prototype.py.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/items/constants.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/tests/unit/game/items/test_item_prototype_models.py`

## Audit Trail

- EXTRACTED: 67 (79%)
- INFERRED: 18 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*