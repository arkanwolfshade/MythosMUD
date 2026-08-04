# stats game generator

> 27 nodes

## Key Concepts

- **test_inventory_command_prototype.py** (21 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **infer_equip_slot_from_prototype()** (18 connections) — `server/commands/inventory_command_prototype.py`
- **inventory_command_prototype.py** (13 connections) — `server/commands/inventory_command_prototype.py`
- **prototype_registry_from_request()** (8 connections) — `server/commands/inventory_command_prototype.py`
- **prototype_from_registry()** (8 connections) — `server/commands/inventory_command_prototype.py`
- **_first_normalized_wear_slot()** (3 connections) — `server/commands/inventory_command_prototype.py`
- **test_prototype_from_registry_swallows_registry_error()** (3 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **_inventory_prototype_id()** (2 connections) — `server/commands/inventory_command_prototype.py`
- **_wear_slots_from_prototype()** (2 connections) — `server/commands/inventory_command_prototype.py`
- **test_prototype_registry_from_request_missing_app()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_prototype_registry_from_request_returns_registry()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_prototype_from_registry_missing_get()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_prototype_from_registry_returns_prototype()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_infer_equip_slot_non_inventory_stack()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_infer_equip_slot_no_registry()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_infer_equip_slot_from_wear_slots()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_infer_equip_slot_missing_prototype()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_infer_equip_slot_empty_wear_slots()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_prototype_registry_from_request_no_state()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_infer_equip_slot_uses_item_id()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_infer_equip_slot_non_string_wear_slot()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_infer_equip_slot_invalid_prototype_id_type()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **Prototype registry access and equip-slot inference for inventory items.** (1 connections) — `server/commands/inventory_command_prototype.py`
- **Resolve prototype registry from FastAPI-style request (agent-readable indirectio** (1 connections) — `server/commands/inventory_command_prototype.py`
- **Return the prototype object for ``prototype_id``, or None if missing or invalid.** (1 connections) — `server/commands/inventory_command_prototype.py`
- *... and 2 more nodes in this community*

## Relationships

- [npc spawn validator](npc_spawn_validator.md) (5 shared connections)
- [commands inventory command](commands_inventory_command.md) (3 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (3 shared connections)
- [nats services metrics](nats_services_metrics.md) (1 shared connections)
- [combat npc mixin](combat_npc_mixin.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_prototype.py`
- `server/tests/unit/commands/test_inventory_command_prototype.py`

## Audit Trail

- EXTRACTED: 107 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*