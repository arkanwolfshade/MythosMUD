# Admin NPC Schemas

> 60 nodes

## Key Concepts

- **test_inventory_commands.py** (20 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **handle_pickup_command()** (18 connections) — `server/commands/inventory_pickup_command.py`
- **command_result_text()** (17 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **PickupTestWiring** (17 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_inventory_commands_pickup.py** (17 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **handle_inventory_command()** (14 connections) — `server/commands/inventory_commands.py`
- **inventory_commands_test_support.py** (7 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_handle_pickup_command()** (7 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_inventory_capacity_error()** (7 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **sample_floor_item_stack()** (6 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **_pickup_with_persist_patch()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_persist_failure_restores_drop_and_inventory()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **inventory_has_named_item()** (5 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_handle_drop_command_broadcasts_room_event_after_persist()** (5 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_pickup_command_no_target()** (5 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_no_room_manager()** (5 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_invalid_index()** (5 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_search_term_not_found()** (5 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_inventory_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_drop_command_no_target()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_equip_command_no_target()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_unequip_command_no_target()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_put_command_no_target()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_get_command_no_target()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_inventory_command()** (3 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- *... and 35 more nodes in this community*

## Relationships

- [Container Sync Remediation](Container_Sync_Remediation.md) (11 shared connections)
- [FastAPI Auth Integration](FastAPI_Auth_Integration.md) (10 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (4 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (4 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (4 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (3 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (2 shared connections)

## Source Files

- `server/commands/inventory_commands.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/inventory_commands_test_support.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_inventory_commands_pickup.py`

## Audit Trail

- EXTRACTED: 215 (90%)
- INFERRED: 25 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*