# command_input.py

> 29 nodes

## Key Concepts

- **test_inventory_command_prototype.py** (21 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **infer_equip_slot_from_prototype()** (18 connections) — `server/commands/inventory_command_prototype.py`
- **inventory_command_prototype.py** (13 connections) — `server/commands/inventory_command_prototype.py`
- **prototype_registry_from_request()** (9 connections) — `server/commands/inventory_command_prototype.py`
- **prototype_from_registry()** (8 connections) — `server/commands/inventory_command_prototype.py`
- **.get()** (5 connections) — `server/game/items/prototype_registry.py`
- **_first_normalized_wear_slot()** (3 connections) — `server/commands/inventory_command_prototype.py`
- **test_prototype_from_registry_missing_get()** (3 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_prototype_from_registry_swallows_registry_error()** (3 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **_inventory_prototype_id()** (2 connections) — `server/commands/inventory_command_prototype.py`
- **_wear_slots_from_prototype()** (2 connections) — `server/commands/inventory_command_prototype.py`
- **test_infer_equip_slot_empty_wear_slots()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_infer_equip_slot_from_wear_slots()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_infer_equip_slot_invalid_prototype_id_type()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_infer_equip_slot_missing_prototype()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_infer_equip_slot_no_registry()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_infer_equip_slot_non_inventory_stack()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_infer_equip_slot_non_string_wear_slot()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_infer_equip_slot_uses_item_id()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_prototype_from_registry_returns_prototype()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_prototype_registry_from_request_missing_app()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_prototype_registry_from_request_no_state()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **test_prototype_registry_from_request_returns_registry()** (2 connections) — `server/tests/unit/commands/test_inventory_command_prototype.py`
- **Prototype registry access and equip-slot inference for inventory items.** (1 connections) — `server/commands/inventory_command_prototype.py`
- **Resolve prototype registry from FastAPI-style request (agent-readable…** (1 connections) — `server/commands/inventory_command_prototype.py`
- *... and 4 more nodes in this community*

## Relationships

- [authenticated.ts](authenticated.ts.md) (6 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (3 shared connections)
- [game_tick_status_effects.py](game_tick_status_effects.py.md) (3 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (1 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (1 shared connections)
- [magic_service_completion.py](magic_service_completion.py.md) (1 shared connections)
- [test_alias_expansion.py](test_alias_expansion.py.md) (1 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_prototype.py`
- `server/game/items/prototype_registry.py`
- `server/tests/unit/commands/test_inventory_command_prototype.py`

## Audit Trail

- EXTRACTED: 63 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*