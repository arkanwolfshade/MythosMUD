# Container Sync Remediation

> 53 nodes

## Key Concepts

- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_get_command.py** (29 connections) — `server/commands/inventory_get_command.py`
- **RoomDropManager** (19 connections) — `server/commands/inventory_command_contracts.py`
- **handle_get_command()** (14 connections) — `server/commands/inventory_get_command.py`
- **_handle_get_from_room()** (13 connections) — `server/commands/inventory_get_command.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **_get_from_container_path()** (12 connections) — `server/commands/inventory_get_command.py`
- **FloorPickupAfterExtract** (10 connections) — `server/commands/inventory_pickup_command.py`
- **_pickup_resolve_floor_stack_or_error()** (10 connections) — `server/commands/inventory_pickup_command.py`
- **GetCommandRuntime** (9 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (9 connections) — `server/commands/inventory_get_command.py`
- **FloorPickupEnvironment** (9 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupPayload** (9 connections) — `server/commands/inventory_pickup_command.py`
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **resolve_pickup_item_index()** (8 connections) — `server/commands/inventory_command_helpers.py`
- **_get_transfer_out_of_container()** (7 connections) — `server/commands/inventory_get_command.py`
- **_get_route_after_validation()** (7 connections) — `server/commands/inventory_get_command.py`
- **inventory_command_coercion.py** (6 connections) — `server/commands/inventory_command_coercion.py`
- **CommandResponse** (6 connections)
- **_pickup_broadcast_success()** (6 connections) — `server/commands/inventory_pickup_command.py`
- **prepare_extracted_stack()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **CommandResponse** (5 connections)
- **_pickup_quantity_or_error()** (4 connections) — `server/commands/inventory_pickup_command.py`
- **UUID** (3 connections)
- **.__init__()** (3 connections) — `server/commands/inventory_pickup_command.py`
- *... and 28 more nodes in this community*

## Relationships

- [Spell Effect Protocols](Spell_Effect_Protocols.md) (24 shared connections)
- [Admin NPC Schemas](Admin_NPC_Schemas.md) (10 shared connections)
- [Rate Limiter Utilities](Rate_Limiter_Utilities.md) (8 shared connections)
- [Container Open Events](Container_Open_Events.md) (6 shared connections)
- [Container Inventory Ops](Container_Inventory_Ops.md) (5 shared connections)
- [Investigations Sessions Xx](Investigations_Sessions_Xx.md) (4 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Container Inventory Finders](Container_Inventory_Finders.md) (3 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (2 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (2 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (2 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_commands.py`

## Audit Trail

- EXTRACTED: 256 (86%)
- INFERRED: 42 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*