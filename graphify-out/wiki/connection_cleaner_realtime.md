# connection cleaner realtime

> 41 nodes

## Key Concepts

- **ItemPrototypeModel** (39 connections) — `server/game/items/models.py`
- **test_item_prototype_models.py** (13 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_combat_weapon_resolution.py** (12 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **._initialize_item_services()** (10 connections) — `server/container/bundles/game.py`
- **models.py** (9 connections) — `server/game/items/models.py`
- **_valid_payload()** (9 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **._handle_item_prototypes_db_error()** (4 connections) — `server/container/bundles/game.py`
- **test_item_prototype_rejects_invalid_item_type()** (4 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_invalid_flags()** (4 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_invalid_wear_slots()** (4 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_empty_effect_components()** (4 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **constants.py** (3 connections) — `server/game/items/constants.py`
- **.all()** (3 connections) — `server/game/items/prototype_registry.py`
- **switchblade_prototype()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_weapon_resolution_switchblade_no_main_hand_returns_none()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_item_prototype_valid_minimal()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_accepts_valid_flags()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_accepts_valid_wear_slots()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_normalizes_effect_components_and_tags()** (3 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **.validate_item_type()** (2 connections) — `server/game/items/models.py`
- **.validate_flags()** (2 connections) — `server/game/items/models.py`
- **.validate_wear_slots()** (2 connections) — `server/game/items/models.py`
- **.validate_effect_components()** (2 connections) — `server/game/items/models.py`
- **.validate_tags()** (2 connections) — `server/game/items/models.py`
- **Exception** (1 connections)
- *... and 16 more nodes in this community*

## Relationships

- [npc spawn validator](npc_spawn_validator.md) (19 shared connections)
- [combat npc mixin](combat_npc_mixin.md) (12 shared connections)
- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [command inventory models](command_inventory_models.md) (4 shared connections)
- [holiday service services](holiday_service_services.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/game/items/constants.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/items/test_item_prototype_models.py`

## Audit Trail

- EXTRACTED: 150 (92%)
- INFERRED: 13 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*