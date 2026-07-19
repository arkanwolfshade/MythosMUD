# Item Model Unit Tests

> 29 nodes · cohesion 0.07

## Key Concepts

- **test_item.py** (18 connections) — `server/tests/unit/models/test_item.py`
- **test_item_instance_apply_flag_existing_flag()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_instance_apply_flag_multiple_flags()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_instance_apply_flag_new_flag()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_instance_apply_flag_preserves_order()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_prototype_primary_slot_empty()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_prototype_primary_slot_none()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_prototype_primary_slot_single_slot()** (3 connections) — `server/tests/unit/models/test_item.py`
- **test_item_prototype_primary_slot_with_slots()** (3 connections) — `server/tests/unit/models/test_item.py`
- **Test unique_key returns different tuples for same instance, different component.** (2 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key()** (2 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key_different_instance_same_component()** (2 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key_different_values()** (2 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key_empty_strings()** (2 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key_same_instance_different_component()** (2 connections) — `server/tests/unit/models/test_item.py`
- **test_item_component_state_unique_key_static_method()** (2 connections) — `server/tests/unit/models/test_item.py`
- **Unit tests for item models.  Tests the ItemPrototype, ItemInstance, and ItemComp** (1 connections) — `server/tests/unit/models/test_item.py`
- **Test unique_key returns different tuples for different inputs.** (1 connections) — `server/tests/unit/models/test_item.py`
- **Test primary_slot returns first wear slot when slots exist.** (1 connections) — `server/tests/unit/models/test_item.py`
- **Test unique_key handles empty strings.** (1 connections) — `server/tests/unit/models/test_item.py`
- **Test unique_key is a static method (can be called without instance).** (1 connections) — `server/tests/unit/models/test_item.py`
- **Test primary_slot returns the slot when only one exists.** (1 connections) — `server/tests/unit/models/test_item.py`
- **Test primary_slot returns None when no wear slots.** (1 connections) — `server/tests/unit/models/test_item.py`
- **Test primary_slot returns None when wear_slots is None (edge case).** (1 connections) — `server/tests/unit/models/test_item.py`
- **Test apply_flag adds a new flag to flags_override.** (1 connections) — `server/tests/unit/models/test_item.py`
- *... and 4 more nodes in this community*

## Relationships

- [[SQLAlchemy Model Base]] (6 shared connections)
- [[Game Service Bundle]] (5 shared connections)

## Source Files

- `server/tests/unit/models/test_item.py`

## Audit Trail

- EXTRACTED: 69 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
