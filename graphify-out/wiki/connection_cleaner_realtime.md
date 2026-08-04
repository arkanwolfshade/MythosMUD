# connection cleaner realtime

> 32 nodes

## Key Concepts

- **ItemPrototypeModel** (39 connections) — `server/game/items/models.py`
- **test_item_prototype_models.py** (13 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **models.py** (9 connections) — `server/game/items/models.py`
- **_valid_payload()** (9 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_invalid_item_type()** (4 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_invalid_flags()** (4 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_invalid_wear_slots()** (4 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_item_prototype_rejects_empty_effect_components()** (4 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **constants.py** (3 connections) — `server/game/items/constants.py`
- **.find_by_tag()** (3 connections) — `server/game/items/prototype_registry.py`
- **.all()** (3 connections) — `server/game/items/prototype_registry.py`
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
- **Pydantic models for item prototype validation.  This module defines the ItemProt** (1 connections) — `server/game/items/models.py`
- **Validated representation of an item prototype definition.      This model keeps** (1 connections) — `server/game/items/models.py`
- **Validate that item_type is in the allowed list.          Args:             value** (1 connections) — `server/game/items/models.py`
- *... and 7 more nodes in this community*

## Relationships

- [MapView GameClientV2ContainerView Tabbed](MapView_GameClientV2ContainerView_Tabbed.md) (10 shared connections)
- [combat npc mixin](combat_npc_mixin.md) (9 shared connections)
- [npc spawn validator](npc_spawn_validator.md) (5 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (4 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [command commands validation](command_commands_validation.md) (1 shared connections)

## Source Files

- `server/game/items/constants.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/tests/unit/game/items/test_item_prototype_models.py`

## Audit Trail

- EXTRACTED: 117 (91%)
- INFERRED: 12 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*