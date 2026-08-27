# magic_service_completion.py

> 31 nodes

## Key Concepts

- **ItemPrototypeModel** (37 connections) — `server/game/items/models.py`
- **test_item_prototype_models.py** (15 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
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
- **Validate and normalize effect components. Args: value: The list of effect…** (1 connections) — `server/game/items/models.py`
- **Validate and normalize tags. Args: value: The list of tags to validate Returns:…** (1 connections) — `server/game/items/models.py`
- **Validated representation of an item prototype definition. This model keeps the…** (1 connections) — `server/game/items/models.py`
- *... and 6 more nodes in this community*

## Relationships

- [test_npc_combat_integration_service_player_attacks.py](test_npc_combat_integration_service_player_attacks.py.md) (13 shared connections)
- [test_alias_expansion.py](test_alias_expansion.py.md) (7 shared connections)
- [authenticated.ts](authenticated.ts.md) (2 shared connections)
- [command_input.py](command_input.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)

## Source Files

- `server/game/items/constants.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/tests/unit/game/items/test_item_prototype_models.py`

## Audit Trail

- EXTRACTED: 58 (77%)
- INFERRED: 17 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*