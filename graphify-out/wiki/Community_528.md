# Community 528

> 32 nodes

## Key Concepts

- **inventory_get_command.py** (30 connections) — `server/commands/inventory_get_command.py`
- **test_inventory_get_command.py** (25 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **handle_get_command()** (16 connections) — `server/commands/inventory_get_command.py`
- **_handle_get_from_room()** (16 connections) — `server/commands/inventory_get_command.py`
- **_get_from_container_path()** (15 connections) — `server/commands/inventory_get_command.py`
- **_get_transfer_out_of_container()** (11 connections) — `server/commands/inventory_get_command.py`
- **asyncio** (10 connections)
- **GetCommandRuntime** (8 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (8 connections) — `server/commands/inventory_get_command.py`
- **_get_route_after_validation()** (7 connections) — `server/commands/inventory_get_command.py`
- **test_get_from_container_path_item_not_in_container()** (6 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_from_container_path_missing_container()** (6 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_command_uses_pickup_wiring()** (5 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **CommandResponse** (5 connections)
- **_container_transfer_messages()** (4 connections) — `server/commands/inventory_get_command.py`
- **test_get_transfer_out_of_container_error()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_transfer_out_of_container_not_success()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_transfer_out_of_container_success()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_from_room_index_error()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_from_room_invalid_quantity()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_from_room_unresolved_index()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_container_transfer_messages()** (2 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **Player** (2 connections)
- **UUID** (2 connections)
- *... and 7 more nodes in this community*

## Relationships

- [Community 159](Community_159.md) (13 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (10 shared connections)
- [Community 101](Community_101.md) (8 shared connections)
- [Community 107](Community_107.md) (5 shared connections)
- [Community 290](Community_290.md) (5 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (5 shared connections)
- [Community 113](Community_113.md) (3 shared connections)
- [Community 75](Community_75.md) (3 shared connections)
- [Community 25](Community_25.md) (2 shared connections)

## Source Files

- `server/commands/inventory_get_command.py`
- `server/tests/unit/commands/test_inventory_get_command.py`

## Audit Trail

- EXTRACTED: 108 (81%)
- INFERRED: 25 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*