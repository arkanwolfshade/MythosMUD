# Container Sync Remediation

> 81 nodes

## Key Concepts

- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_get_command.py** (29 connections) — `server/commands/inventory_get_command.py`
- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **RoomDropManager** (19 connections) — `server/commands/inventory_command_contracts.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **handle_drop_command()** (15 connections) — `server/commands/inventory_drop_command.py`
- **handle_get_command()** (14 connections) — `server/commands/inventory_get_command.py`
- **_handle_get_from_room()** (13 connections) — `server/commands/inventory_get_command.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **_drop_resolve_stack_or_error()** (12 connections) — `server/commands/inventory_drop_command.py`
- **_get_from_container_path()** (12 connections) — `server/commands/inventory_get_command.py`
- **add_pickup_to_inventory()** (10 connections) — `server/commands/inventory_command_helpers.py`
- **FloorPickupAfterExtract** (10 connections) — `server/commands/inventory_pickup_command.py`
- **_pickup_resolve_floor_stack_or_error()** (10 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_command_contracts.py** (9 connections) — `server/commands/inventory_command_contracts.py`
- **GetCommandRuntime** (9 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (9 connections) — `server/commands/inventory_get_command.py`
- **FloorPickupEnvironment** (9 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupPayload** (9 connections) — `server/commands/inventory_pickup_command.py`
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **get_room_manager()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **CommandResponse** (7 connections)
- **_get_transfer_out_of_container()** (7 connections) — `server/commands/inventory_get_command.py`
- *... and 56 more nodes in this community*

## Relationships

- [Container Component Capacity](Container_Component_Capacity.md) (28 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (19 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (14 shared connections)
- [Admin NPC Schemas](Admin_NPC_Schemas.md) (12 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (10 shared connections)
- [Client Event Store](Client_Event_Store.md) (8 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (7 shared connections)
- [NATS Connection State Machine](NATS_Connection_State_Machine.md) (7 shared connections)
- [Container Inventory Ops](Container_Inventory_Ops.md) (7 shared connections)
- [AnyIO vs Asyncio Guide](AnyIO_vs_Asyncio_Guide.md) (5 shared connections)
- [Container Open Events](Container_Open_Events.md) (4 shared connections)
- [NPC Definition CRUD](NPC_Definition_CRUD.md) (2 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_commands.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_commands.py`

## Audit Trail

- EXTRACTED: 426 (89%)
- INFERRED: 55 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*