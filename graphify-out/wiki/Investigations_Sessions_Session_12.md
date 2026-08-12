# Investigations Sessions Session

> 11 nodes

## Key Concepts

- **inventory_command_prototype.py** (12 connections) — `server/commands/inventory_command_prototype.py`
- **infer_equip_slot_from_prototype()** (9 connections) — `server/commands/inventory_command_prototype.py`
- **prototype_registry_from_request()** (4 connections) — `server/commands/inventory_command_prototype.py`
- **prototype_from_registry()** (4 connections) — `server/commands/inventory_command_prototype.py`
- **_first_normalized_wear_slot()** (3 connections) — `server/commands/inventory_command_prototype.py`
- **_inventory_prototype_id()** (2 connections) — `server/commands/inventory_command_prototype.py`
- **_wear_slots_from_prototype()** (2 connections) — `server/commands/inventory_command_prototype.py`
- **Prototype registry access and equip-slot inference for inventory items.** (1 connections) — `server/commands/inventory_command_prototype.py`
- **Resolve prototype registry from FastAPI-style request (agent-readable indirectio** (1 connections) — `server/commands/inventory_command_prototype.py`
- **Return the prototype object for ``prototype_id``, or None if missing or invalid.** (1 connections) — `server/commands/inventory_command_prototype.py`
- **Infer equip slot from prototype wear_slots for inventory items.** (1 connections) — `server/commands/inventory_command_prototype.py`

## Relationships

- [Container Component Capacity](Container_Component_Capacity.md) (5 shared connections)
- [NATS Retry Handler](NATS_Retry_Handler.md) (2 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (1 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)
- [NATS Subject Admin API](NATS_Subject_Admin_API.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_prototype.py`

## Audit Trail

- EXTRACTED: 38 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*