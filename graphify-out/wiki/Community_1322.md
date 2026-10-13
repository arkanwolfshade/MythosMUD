# Community 1322

> 8 nodes

## Key Concepts

- **RoomDropManager** (6 connections) — `server/commands/inventory_command_contracts.py`
- **add_pickup_to_inventory()** (6 connections) — `server/commands/inventory_command_helpers.py`
- **.add_room_drop()** (2 connections) — `server/commands/inventory_command_contracts.py`
- **.list_room_drops()** (1 connections) — `server/commands/inventory_command_contracts.py`
- **.take_room_drop()** (1 connections) — `server/commands/inventory_command_contracts.py`
- **Protocol** (1 connections)
- **Narrows room managers for floor drop operations (pickup / get room).** (1 connections) — `server/commands/inventory_command_contracts.py`
- **Add picked up item to inventory, returning updated inventory or error.** (1 connections) — `server/commands/inventory_command_helpers.py`

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Community 131](Community_131.md) (2 shared connections)
- [Community 235](Community_235.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`

## Audit Trail

- EXTRACTED: 11 (92%)
- INFERRED: 1 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*