# server commands inventory command prototype

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

- [iteminstance](iteminstance.md) (6 shared connections)
- [server commands inventory item matching](server_commands_inventory_item_matching.md) (3 shared connections)
- [server commands equipment helpers normalize](server_commands_equipment_helpers_normalize.md) (3 shared connections)
- [server commands look helpers lookrequest](server_commands_look_helpers_lookrequest.md) (1 shared connections)
- [server commands rescue commands](server_commands_rescue_commands.md) (1 shared connections)
- [server game items constants](server_game_items_constants.md) (1 shared connections)
- [server game items prototype registry](server_game_items_prototype_registry.md) (1 shared connections)
- [object](object.md) (1 shared connections)

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