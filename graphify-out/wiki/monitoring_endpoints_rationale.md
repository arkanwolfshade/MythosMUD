# monitoring endpoints rationale

> 53 nodes

## Key Concepts

- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_get_command.py** (29 connections) — `server/commands/inventory_get_command.py`
- **RoomDropManager** (19 connections) — `server/commands/inventory_command_contracts.py`
- **_handle_get_from_room()** (13 connections) — `server/commands/inventory_get_command.py`
- **handle_get_command()** (13 connections) — `server/commands/inventory_get_command.py`
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

- [commands inventory command](commands_inventory_command.md) (18 shared connections)
- [inventory commands command](inventory_commands_command.md) (17 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (10 shared connections)
- [container inventory helpers](container_inventory_helpers.md) (6 shared connections)
- [commands admin mute](commands_admin_mute.md) (5 shared connections)
- [models player rationale](models_player_rationale.md) (4 shared connections)
- [command inventory factories](command_inventory_factories.md) (4 shared connections)
- [world models rationale](world_models_rationale.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [container find inventory](container_find_inventory.md) (2 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_commands.py`

## Audit Trail

- EXTRACTED: 256 (86%)
- INFERRED: 41 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*