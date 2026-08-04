# uuid npc combat

> 45 nodes

## Key Concepts

- **test_item.py** (19 connections) — `server/tests/unit/models/test_item.py`
- **ItemPrototype** (14 connections) — `server/models/item.py`
- **ItemInstance** (11 connections) — `server/models/item.py`
- **item.py** (8 connections) — `server/models/item.py`
- **.unique_key()** (8 connections) — `server/models/item.py`
- **ItemComponentState** (7 connections) — `server/models/item.py`
- **Base** (3 connections)
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
- **.primary_slot()** (2 connections) — `server/models/item.py`
- **.apply_flag()** (2 connections) — `server/models/item.py`
- **SQLAlchemy models for MythosMUD item prototypes, instances, and component state.** (1 connections) — `server/models/item.py`
- **Immutable catalog entry describing a canonical item.** (1 connections) — `server/models/item.py`
- *... and 20 more nodes in this community*

## Relationships

- [world models rationale](world_models_rationale.md) (5 shared connections)
- [task registry app](task_registry_app.md) (4 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [command commands validation](command_commands_validation.md) (1 shared connections)

## Source Files

- `server/models/item.py`
- `server/tests/unit/models/test_item.py`

## Audit Trail

- EXTRACTED: 133 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*