# Community 159

> 79 nodes

## Key Concepts

- **coerce_int()** (39 connections) — `server/utils/int_coercion.py`
- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **handle_pickup_command()** (17 connections) — `server/commands/inventory_pickup_command.py`
- **RoomDropManager** (16 connections) — `server/commands/inventory_command_contracts.py`
- **handle_drop_command()** (14 connections) — `server/commands/inventory_drop_command.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **_drop_resolve_stack_or_error()** (12 connections) — `server/commands/inventory_drop_command.py`
- **test_inventory_command_coercion.py** (12 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **Player** (11 connections)
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **_pickup_resolve_floor_stack_or_error()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupAfterExtract** (8 connections) — `server/commands/inventory_pickup_command.py`
- **add_pickup_to_inventory()** (8 connections) — `server/commands/inventory_command_helpers.py`
- **FloorPickupEnvironment** (7 connections) — `server/commands/inventory_pickup_command.py`
- **get_room_manager()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **CommandResponse** (7 connections)
- **FloorPickupPayload** (6 connections) — `server/commands/inventory_pickup_command.py`
- **_drop_finish_after_persist()** (6 connections) — `server/commands/inventory_drop_command.py`
- **_drop_parsed_quantity_or_error()** (6 connections) — `server/commands/inventory_drop_command.py`
- **_pickup_broadcast_success()** (6 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_command_coercion.py** (6 connections) — `server/commands/inventory_command_coercion.py`
- **CommandResponse** (6 connections)
- *... and 54 more nodes in this community*

## Relationships

- [Community 75](Community_75.md) (28 shared connections)
- [Community 290](Community_290.md) (16 shared connections)
- [Community 528](Community_528.md) (13 shared connections)
- [Community 101](Community_101.md) (10 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (9 shared connections)
- [Catatonia Status Checks](Catatonia_Status_Checks.md) (7 shared connections)
- [Community 27](Community_27.md) (6 shared connections)
- [Community 25](Community_25.md) (4 shared connections)
- [Community 73](Community_73.md) (4 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (4 shared connections)
- [Community 51](Community_51.md) (3 shared connections)
- [Community 382](Community_382.md) (3 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 241 (91%)
- INFERRED: 23 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*