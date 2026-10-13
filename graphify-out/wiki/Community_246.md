# Community 246

> 64 nodes

## Key Concepts

- **test_inventory_get_command.py** (30 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **inventory_get_command.py** (29 connections) — `server/commands/inventory_get_command.py`
- **_get_from_container_path()** (17 connections) — `server/commands/inventory_get_command.py`
- **handle_get_command()** (16 connections) — `server/commands/inventory_get_command.py`
- **handle_pickup_command()** (16 connections) — `server/commands/inventory_pickup_command.py`
- **_handle_get_from_room()** (14 connections) — `server/commands/inventory_get_command.py`
- **asyncio** (13 connections)
- **_get_transfer_out_of_container()** (12 connections) — `server/commands/inventory_get_command.py`
- **GetCommandRuntime** (10 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (10 connections) — `server/commands/inventory_get_command.py`
- **complete_pickup_after_floor_extract()** (10 connections) — `server/commands/inventory_pickup_command.py`
- **_pickup_commit_inventory_after_floor_extract()** (8 connections) — `server/commands/inventory_pickup_command.py`
- **test_get_from_container_path_reads_persistence_items_json()** (8 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_from_empty_container_says_item_not_there()** (8 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **FloorPickupAfterExtract** (7 connections) — `server/commands/inventory_pickup_command.py`
- **_get_route_after_validation()** (7 connections) — `server/commands/inventory_get_command.py`
- **FloorPickupEnvironment** (6 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupPayload** (6 connections) — `server/commands/inventory_pickup_command.py`
- **_pickup_resolve_floor_stack_or_error()** (6 connections) — `server/commands/inventory_pickup_command.py`
- **test_get_from_container_path_item_not_in_container()** (6 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_from_container_path_missing_container()** (6 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **CommandResponse** (6 connections)
- **_pickup_broadcast_success()** (5 connections) — `server/commands/inventory_pickup_command.py`
- **_chest_row()** (5 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_command_passes_persistence_to_validation()** (5 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- *... and 39 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (39 shared connections)
- [Community 562](Community_562.md) (10 shared connections)
- [Community 78](Community_78.md) (6 shared connections)
- [Community 239](Community_239.md) (6 shared connections)
- [Community 332](Community_332.md) (3 shared connections)
- [Community 117](Community_117.md) (2 shared connections)
- [Community 441](Community_441.md) (2 shared connections)

## Source Files

- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_get_command.py`

## Audit Trail

- EXTRACTED: 170 (81%)
- INFERRED: 39 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*