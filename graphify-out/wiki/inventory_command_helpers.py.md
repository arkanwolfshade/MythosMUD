# inventory_command_helpers.py

> 164 nodes

## Key Concepts

- **inventory_command_helpers.py** (50 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **persist_player()** (29 connections) — `server/commands/inventory_command_helpers.py`
- **test_inventory_helpers_extended.py** (27 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **test_inventory_commands_more_helpers.py** (24 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **broadcast_room_event()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_state()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_player()** (17 connections) — `server/commands/inventory_command_helpers.py`
- **RoomDropManager** (16 connections) — `server/commands/inventory_command_contracts.py`
- **asyncio** (15 connections)
- **handle_drop_command()** (14 connections) — `server/commands/inventory_drop_command.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **test_inventory_commands_persistence_helpers.py** (13 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **_drop_resolve_stack_or_error()** (12 connections) — `server/commands/inventory_drop_command.py`
- **Player** (11 connections)
- **asyncio** (11 connections)
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **_pickup_resolve_floor_stack_or_error()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupAfterExtract** (8 connections) — `server/commands/inventory_pickup_command.py`
- **add_pickup_to_inventory()** (8 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_pickup_item_index()** (8 connections) — `server/commands/inventory_command_helpers.py`
- **ensure_item_instance_for_pickup()** (7 connections) — `server/commands/inventory_command_helpers.py`
- *... and 139 more nodes in this community*

## Relationships

- [command_result_text](command_result_text.md) (27 shared connections)
- [inventory_get_command.py](inventory_get_command.py.md) (15 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (9 shared connections)
- [InventoryService](InventoryService.md) (8 shared connections)
- [inventory_unequip_command.py](inventory_unequip_command.py.md) (8 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (8 shared connections)
- [admin_summon_command.py](admin_summon_command.py.md) (7 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (7 shared connections)
- [AliasStorage](AliasStorage.md) (7 shared connections)
- [coerce_int](coerce_int.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [Player](Player.md) (5 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`

## Audit Trail

- EXTRACTED: 429 (95%)
- INFERRED: 23 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*