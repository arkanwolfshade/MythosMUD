# monitoring endpoints rationale

> 69 nodes

## Key Concepts

- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_get_command.py** (30 connections) — `server/commands/inventory_get_command.py`
- **test_inventory_get_command.py** (25 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **RoomDropManager** (19 connections) — `server/commands/inventory_command_contracts.py`
- **_handle_get_from_room()** (17 connections) — `server/commands/inventory_get_command.py`
- **handle_pickup_command()** (17 connections) — `server/commands/inventory_pickup_command.py`
- **handle_get_command()** (16 connections) — `server/commands/inventory_get_command.py`
- **_get_from_container_path()** (15 connections) — `server/commands/inventory_get_command.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **GetCommandRuntime** (12 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (12 connections) — `server/commands/inventory_get_command.py`
- **_get_transfer_out_of_container()** (11 connections) — `server/commands/inventory_get_command.py`
- **add_pickup_to_inventory()** (10 connections) — `server/commands/inventory_command_helpers.py`
- **FloorPickupAfterExtract** (10 connections) — `server/commands/inventory_pickup_command.py`
- **_pickup_resolve_floor_stack_or_error()** (10 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupEnvironment** (9 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupPayload** (9 connections) — `server/commands/inventory_pickup_command.py`
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **resolve_pickup_item_index()** (8 connections) — `server/commands/inventory_command_helpers.py`
- **get_room_manager()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **_get_route_after_validation()** (7 connections) — `server/commands/inventory_get_command.py`
- **CommandResponse** (6 connections)
- **_pickup_broadcast_success()** (6 connections) — `server/commands/inventory_pickup_command.py`
- **prepare_extracted_stack()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **CommandResponse** (5 connections)
- *... and 44 more nodes in this community*

## Relationships

- [commands inventory command](commands_inventory_command.md) (29 shared connections)
- [combat models rationale](combat_models_rationale.md) (14 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (14 shared connections)
- [room conftest toolkit](room_conftest_toolkit.md) (5 shared connections)
- [services admin auth](services_admin_auth.md) (5 shared connections)
- [commands npc admin](commands_npc_admin.md) (4 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (4 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (3 shared connections)
- [Exception Containers](Exception_Containers.md) (2 shared connections)
- [commands whisper command](commands_whisper_command.md) (2 shared connections)
- [container find inventory](container_find_inventory.md) (2 shared connections)

## Source Files

- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_get_command.py`

## Audit Trail

- EXTRACTED: 353 (86%)
- INFERRED: 57 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*