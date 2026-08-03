# monitoring endpoints rationale

> 48 nodes

## Key Concepts

- **inventory_get_command.py** (30 connections) — `server/commands/inventory_get_command.py`
- **test_inventory_get_command.py** (25 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **RoomDropManager** (19 connections) — `server/commands/inventory_command_contracts.py`
- **_handle_get_from_room()** (17 connections) — `server/commands/inventory_get_command.py`
- **handle_get_command()** (16 connections) — `server/commands/inventory_get_command.py`
- **_get_from_container_path()** (15 connections) — `server/commands/inventory_get_command.py`
- **GetCommandRuntime** (12 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (12 connections) — `server/commands/inventory_get_command.py`
- **_get_transfer_out_of_container()** (11 connections) — `server/commands/inventory_get_command.py`
- **FloorPickupAfterExtract** (10 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupEnvironment** (9 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupPayload** (9 connections) — `server/commands/inventory_pickup_command.py`
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **resolve_pickup_item_index()** (8 connections) — `server/commands/inventory_command_helpers.py`
- **_get_route_after_validation()** (7 connections) — `server/commands/inventory_get_command.py`
- **CommandResponse** (5 connections)
- **test_get_from_container_path_missing_container()** (5 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_from_container_path_item_not_in_container()** (5 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **_container_transfer_messages()** (4 connections) — `server/commands/inventory_get_command.py`
- **test_handle_get_command_uses_pickup_wiring()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **UUID** (3 connections)
- **.__init__()** (3 connections) — `server/commands/inventory_pickup_command.py`
- **test_get_transfer_out_of_container_error()** (3 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_transfer_out_of_container_success()** (3 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_transfer_out_of_container_not_success()** (3 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- *... and 23 more nodes in this community*

## Relationships

- [inventory commands command](inventory_commands_command.md) (27 shared connections)
- [world models rationale](world_models_rationale.md) (12 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (12 shared connections)
- [container inventory helpers](container_inventory_helpers.md) (6 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [container find inventory](container_find_inventory.md) (2 shared connections)
- [commands inventory command](commands_inventory_command.md) (1 shared connections)
- [commands position system](commands_position_system.md) (1 shared connections)
- [models player rationale](models_player_rationale.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_get_command.py`

## Audit Trail

- EXTRACTED: 234 (84%)
- INFERRED: 46 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*