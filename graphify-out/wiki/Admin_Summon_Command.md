# Admin Summon Command

> 54 nodes · cohesion 0.08

## Key Concepts

- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_get_command.py** (29 connections) — `server/commands/inventory_get_command.py`
- **RoomDropManager** (19 connections) — `server/commands/inventory_command_contracts.py`
- **handle_pickup_command()** (18 connections) — `server/commands/inventory_pickup_command.py`
- **handle_get_command()** (14 connections) — `server/commands/inventory_get_command.py`
- **_handle_get_from_room()** (13 connections) — `server/commands/inventory_get_command.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **_get_from_container_path()** (12 connections) — `server/commands/inventory_get_command.py`
- **FloorPickupAfterExtract** (10 connections) — `server/commands/inventory_pickup_command.py`
- **_pickup_resolve_floor_stack_or_error()** (10 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_command_contracts.py** (9 connections) — `server/commands/inventory_command_contracts.py`
- **GetCommandRuntime** (9 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (9 connections) — `server/commands/inventory_get_command.py`
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupEnvironment** (9 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupPayload** (9 connections) — `server/commands/inventory_pickup_command.py`
- **resolve_pickup_item_index()** (8 connections) — `server/commands/inventory_command_helpers.py`
- **_get_route_after_validation()** (7 connections) — `server/commands/inventory_get_command.py`
- **_get_transfer_out_of_container()** (7 connections) — `server/commands/inventory_get_command.py`
- **_pickup_broadcast_success()** (6 connections) — `server/commands/inventory_pickup_command.py`
- **CommandResponse** (6 connections)
- **prepare_extracted_stack()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **CommandResponse** (5 connections)
- **UUID** (4 connections)
- **_pickup_quantity_or_error()** (4 connections) — `server/commands/inventory_pickup_command.py`
- *... and 29 more nodes in this community*

## Relationships

- [Rest Command Flow](Rest_Command_Flow.md) (20 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (13 shared connections)
- [Combat Messaging Integration](Combat_Messaging_Integration.md) (9 shared connections)
- [Deprecated Logging Patterns](Deprecated_Logging_Patterns.md) (6 shared connections)
- [Commands Inventory Item](Commands_Inventory_Item.md) (6 shared connections)
- [Container Inventory Ops](Container_Inventory_Ops.md) (6 shared connections)
- [Logging Migration Examples](Logging_Migration_Examples.md) (4 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (4 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Container Inventory Finders](Container_Inventory_Finders.md) (2 shared connections)
- [Player Schema Models](Player_Schema_Models.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_commands.py`

## Audit Trail

- EXTRACTED: 273 (85%)
- INFERRED: 49 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*