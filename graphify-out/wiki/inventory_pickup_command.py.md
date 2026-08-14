# inventory_pickup_command.py

> 69 nodes

## Key Concepts

- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_get_command.py** (30 connections) — `server/commands/inventory_get_command.py`
- **test_inventory_get_command.py** (25 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **handle_pickup_command()** (17 connections) — `server/commands/inventory_pickup_command.py`
- **RoomDropManager** (16 connections) — `server/commands/inventory_command_contracts.py`
- **handle_get_command()** (16 connections) — `server/commands/inventory_get_command.py`
- **_get_from_container_path()** (15 connections) — `server/commands/inventory_get_command.py`
- **_handle_get_from_room()** (15 connections) — `server/commands/inventory_get_command.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **GetCommandRuntime** (12 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (12 connections) — `server/commands/inventory_get_command.py`
- **_get_transfer_out_of_container()** (11 connections) — `server/commands/inventory_get_command.py`
- **FloorPickupAfterExtract** (10 connections) — `server/commands/inventory_pickup_command.py`
- **asyncio** (10 connections)
- **FloorPickupEnvironment** (9 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupPayload** (9 connections) — `server/commands/inventory_pickup_command.py`
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_command_contracts.py** (9 connections) — `server/commands/inventory_command_contracts.py`
- **resolve_pickup_item_index()** (8 connections) — `server/commands/inventory_command_helpers.py`
- **_pickup_resolve_floor_stack_or_error()** (8 connections) — `server/commands/inventory_pickup_command.py`
- **_get_route_after_validation()** (7 connections) — `server/commands/inventory_get_command.py`
- **_pickup_broadcast_success()** (6 connections) — `server/commands/inventory_pickup_command.py`
- **CommandResponse** (6 connections)
- **prepare_extracted_stack()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **test_get_from_container_path_item_not_in_container()** (5 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- *... and 44 more nodes in this community*

## Relationships

- [inventory_command_helpers.py](inventory_command_helpers.py.md) (31 shared connections)
- [command_result_text](command_result_text.md) (15 shared connections)
- [container_helpers_inventory.py](container_helpers_inventory.py.md) (6 shared connections)
- [Player](Player.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [coerce_int](coerce_int.md) (4 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (4 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (2 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (2 shared connections)

## Source Files

- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_get_command.py`

## Audit Trail

- EXTRACTED: 214 (88%)
- INFERRED: 30 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*