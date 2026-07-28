# Command Alias Handling

> 39 nodes · cohesion 0.07

## Key Concepts

- **test_item.py** (19 connections) — `server/tests/unit/models/test_item.py`
- **ItemInstance** (11 connections) — `server/models/item.py`
- **.unique_key()** (8 connections) — `server/models/item.py`
- **ItemComponentState** (7 connections) — `server/models/item.py`
- **Base** (3 connections)
- **test_item_component_state_unique_key()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key_different_instance_same_component()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key_different_values()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key_empty_strings()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key_same_instance_different_component()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key_static_method()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_instance_apply_flag_existing_flag()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_instance_apply_flag_multiple_flags()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_instance_apply_flag_new_flag()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_instance_apply_flag_preserves_order()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_prototype_primary_slot_empty()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_prototype_primary_slot_none()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_prototype_primary_slot_single_slot()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_prototype_primary_slot_with_slots()** (3 connections) — `server/tests/unit/models/test_item.py`
- **.apply_flag()** (2 connections) — `server/models/item.py`
- **Idempotently apply a runtime-only flag override.** (1 connections) — `server/models/item.py`
- **Per-instance persisted state for modular item components.** (1 connections) — `server/models/item.py`
- **Convenience helper for composing uniqueness checks in higher layers.** (1 connections) — `server/models/item.py`
- **Runtime representation of an item spawned from a prototype.** (1 connections) — `server/models/item.py`
- **Unit tests for item models.  Tests the ItemPrototype, ItemInstance, and ItemComp** (1 connections) — `server/tests/unit/models/test_item.py`
- *... and 14 more nodes in this community*

## Relationships

- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (11 shared connections)
- [Metadata Npc](Metadata_Npc.md) (2 shared connections)

## Source Files

- `server/models/item.py`
- `server/tests/unit/models/test_item.py`

## Audit Trail

- EXTRACTED: 109 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*