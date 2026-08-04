# connection cleaner realtime

> 32 nodes

## Key Concepts

- **ItemPrototypeModel** (39 connections) — `server/game/items/models.py`
- **test_item_prototype_models.py** (13 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **_valid_payload()** (9 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_invalid_item_type()** (4 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_invalid_flags()** (4 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_invalid_wear_slots()** (4 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_empty_effect_components()** (4 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **constants.py** (3 connections) — `server/game/items/constants.py`
- **.find_by_tag()** (3 connections) — `server/game/items/prototype_registry.py`
- **.all()** (3 connections) — `server/game/items/prototype_registry.py`
- **switchblade_prototype()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_item_prototype_valid_minimal()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_accepts_valid_flags()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_accepts_valid_wear_slots()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_normalizes_effect_components_and_tags()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **.validate_item_type()** (2 connections) — `server/game/items/models.py`
- **.validate_flags()** (2 connections) — `server/game/items/models.py`
- **.validate_wear_slots()** (2 connections) — `server/game/items/models.py`
- **.validate_effect_components()** (2 connections) — `server/game/items/models.py`
- **.validate_tags()** (2 connections) — `server/game/items/models.py`
- **Constants supporting item prototype validation.  These enumerations anchor the s** (1 connections) — `server/game/items/constants.py`
- **BaseModel** (1 connections)
- **Validated representation of an item prototype definition.      This model keeps** (1 connections) — `server/game/items/models.py`
- **Validate that item_type is in the allowed list.          Args:             value** (1 connections) — `server/game/items/models.py`
- **Validate that all flags are in the allowed list.          Args:             valu** (1 connections) — `server/game/items/models.py`
- *... and 7 more nodes in this community*

## Relationships

- [MapView GameClientV2ContainerView Tabbed](MapView_GameClientV2ContainerView_Tabbed.md) (17 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (3 shared connections)
- [npc spawn validator](npc_spawn_validator.md) (2 shared connections)
- [combat npc mixin](combat_npc_mixin.md) (2 shared connections)
- [models profession rationale](models_profession_rationale.md) (1 shared connections)

## Source Files

- `server/game/items/constants.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/items/test_item_prototype_models.py`

## Audit Trail

- EXTRACTED: 111 (90%)
- INFERRED: 12 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*