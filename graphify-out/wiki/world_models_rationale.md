# world models rationale

> 32 nodes

## Key Concepts

- **test_item.py** (19 connections) — `server/tests/unit/models/test_item.py`
- **.unique_key()** (8 connections) — `server/models/item.py`
- **test_item_prototype_primary_slot_with_slots()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_prototype_primary_slot_single_slot()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_prototype_primary_slot_empty()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_prototype_primary_slot_none()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_instance_apply_flag_new_flag()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_instance_apply_flag_existing_flag()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_instance_apply_flag_multiple_flags()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_instance_apply_flag_preserves_order()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key_different_values()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key_same_instance_different_component()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key_different_instance_same_component()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key_empty_strings()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key_static_method()** (3 connections) — `server/tests/unit/models/test_item.py`
- **Convenience helper for composing uniqueness checks in higher layers.** (1 connections) — `server/models/item.py`
- **Unit tests for item models.  Tests the ItemPrototype, ItemInstance, and ItemComp** (1 connections) — `server/tests/unit/models/test_item.py`
- **Test primary_slot returns first wear slot when slots exist.** (1 connections) — `server/tests/unit/models/test_item.py`
- **Test primary_slot returns the slot when only one exists.** (1 connections) — `server/tests/unit/models/test_item.py`
- **Test primary_slot returns None when no wear slots.** (1 connections) — `server/tests/unit/models/test_item.py`
- **Test primary_slot returns None when wear_slots is None (edge case).** (1 connections) — `server/tests/unit/models/test_item.py`
- **Test apply_flag adds a new flag to flags_override.** (1 connections) — `server/tests/unit/models/test_item.py`
- **Test apply_flag does not duplicate existing flags (idempotent).** (1 connections) — `server/tests/unit/models/test_item.py`
- **Test apply_flag adds flag when other flags exist.** (1 connections) — `server/tests/unit/models/test_item.py`
- *... and 7 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (13 shared connections)

## Source Files

- `server/models/item.py`
- `server/tests/unit/models/test_item.py`

## Audit Trail

- EXTRACTED: 85 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*