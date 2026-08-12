# inventory_commands.py

> 73 nodes

## Key Concepts

- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **test_inventory_commands.py** (20 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **handle_pickup_command()** (18 connections) — `server/commands/inventory_pickup_command.py`
- **PickupTestWiring** (17 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **command_result_text()** (17 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_inventory_commands_pickup.py** (17 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **handle_unequip_command()** (14 connections) — `server/commands/inventory_unequip_command.py`
- **asyncio** (14 connections)
- **_unequip_run_mutation()** (9 connections) — `server/commands/inventory_unequip_command.py`
- **test_handle_pickup_command()** (8 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_inventory_capacity_error()** (8 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_persist_failure_restores_drop_and_inventory()** (7 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **inventory_commands_test_support.py** (7 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **asyncio** (7 connections)
- **_unequip_success_payload()** (6 connections) — `server/commands/inventory_unequip_command.py`
- **sample_floor_item_stack()** (6 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **_pickup_with_persist_patch()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_invalid_index()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_no_room_manager()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_no_target()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_search_term_not_found()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_drop_command_broadcasts_room_event_after_persist()** (6 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **_unequip_persist_or_rollback()** (5 connections) — `server/commands/inventory_unequip_command.py`
- **inventory_has_named_item()** (5 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_handle_drop_command_no_target()** (5 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- *... and 48 more nodes in this community*

## Relationships

- [persist_player](persist_player.md) (14 shared connections)
- [inventory_pickup_command.py](inventory_pickup_command.py.md) (14 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (13 shared connections)
- [AliasStorage](AliasStorage.md) (11 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (6 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [format_metadata](format_metadata.md) (2 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (1 shared connections)

## Source Files

- `server/commands/inventory_commands.py`
- `server/commands/inventory_pickup_command.py`
- `server/commands/inventory_unequip_command.py`
- `server/tests/unit/commands/inventory_commands_test_support.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_inventory_commands_pickup.py`

## Audit Trail

- EXTRACTED: 319 (92%)
- INFERRED: 28 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*