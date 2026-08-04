# monitoring endpoints rationale

> 36 nodes

## Key Concepts

- **inventory_get_command.py** (30 connections) — `server/commands/inventory_get_command.py`
- **test_inventory_get_command.py** (25 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **_handle_get_from_room()** (17 connections) — `server/commands/inventory_get_command.py`
- **handle_get_command()** (16 connections) — `server/commands/inventory_get_command.py`
- **_get_from_container_path()** (15 connections) — `server/commands/inventory_get_command.py`
- **GetCommandRuntime** (12 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (12 connections) — `server/commands/inventory_get_command.py`
- **_get_transfer_out_of_container()** (11 connections) — `server/commands/inventory_get_command.py`
- **FloorPickupEnvironment** (9 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupPayload** (9 connections) — `server/commands/inventory_pickup_command.py`
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
- **test_handle_get_from_room_index_error()** (3 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_from_room_unresolved_index()** (3 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_from_room_invalid_quantity()** (3 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **Player** (2 connections)
- *... and 11 more nodes in this community*

## Relationships

- [inventory commands command](inventory_commands_command.md) (21 shared connections)
- [combat models rationale](combat_models_rationale.md) (12 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (10 shared connections)
- [container inventory helpers](container_inventory_helpers.md) (5 shared connections)
- [Loot Generation](Loot_Generation.md) (3 shared connections)
- [container find inventory](container_find_inventory.md) (3 shared connections)
- [commands party examples](commands_party_examples.md) (2 shared connections)
- [models player rationale](models_player_rationale.md) (2 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (2 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (1 shared connections)

## Source Files

- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_get_command.py`

## Audit Trail

- EXTRACTED: 191 (85%)
- INFERRED: 34 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*