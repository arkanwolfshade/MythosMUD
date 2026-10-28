# test_nats_message_handler_chat.py

> 46 nodes · cohesion 0.11

## Key Concepts

- **inventory_get_command.py** (34 connections) — `server/commands/inventory_get_command.py`
- **test_inventory_get_command.py** (30 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **_get_from_container_path()** (18 connections) — `server/commands/inventory_get_command.py`
- **handle_get_command()** (18 connections) — `server/commands/inventory_get_command.py`
- **_handle_get_from_room()** (16 connections) — `server/commands/inventory_get_command.py`
- **_get_transfer_out_of_container()** (13 connections) — `server/commands/inventory_get_command.py`
- **asyncio** (13 connections)
- **GetCommandRuntime** (10 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (10 connections) — `server/commands/inventory_get_command.py`
- **test_get_from_container_path_reads_persistence_items_json()** (8 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_from_empty_container_says_item_not_there()** (8 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **_get_route_after_validation()** (7 connections) — `server/commands/inventory_get_command.py`
- **FloorPickupEnvironment** (7 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupPayload** (6 connections) — `server/commands/inventory_pickup_command.py`
- **test_get_from_container_path_item_not_in_container()** (6 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_from_container_path_missing_container()** (6 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **CommandResponse** (5 connections)
- **_chest_row()** (5 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_command_passes_persistence_to_validation()** (5 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_command_uses_pickup_wiring()** (5 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **_container_transfer_messages()** (4 connections) — `server/commands/inventory_get_command.py`
- **test_get_transfer_out_of_container_error()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_transfer_out_of_container_not_success()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_transfer_out_of_container_success()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_from_room_index_error()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- *... and 21 more nodes in this community*

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (23 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (12 shared connections)
- [command_parser.py](command_parser.py.md) (8 shared connections)
- [inventory_item_matching.py](inventory_item_matching.py.md) (6 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (6 shared connections)
- [TargetMatch](TargetMatch.md) (5 shared connections)
- [RoomEventHandler](RoomEventHandler.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [SuccessLevel](SuccessLevel.md) (2 shared connections)
- [FollowService](FollowService.md) (1 shared connections)

## Source Files

- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_get_command.py`

## Audit Trail

- EXTRACTED: 143 (81%)
- INFERRED: 33 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*