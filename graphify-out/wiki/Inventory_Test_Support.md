# Inventory Test Support

> 55 nodes · cohesion 0.06

## Key Concepts

- **test_inventory_commands.py** (19 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **command_result_text()** (17 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **handle_pickup_command()** (17 connections) — `server/commands/inventory_pickup_command.py`
- **test_inventory_commands_pickup.py** (15 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **PickupTestWiring** (10 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **PickupTestWiring** (10 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **inventory_commands_test_support.py** (7 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_handle_pickup_command()** (7 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_inventory_capacity_error()** (7 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **sample_floor_item_stack()** (6 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **_pickup_with_persist_patch()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_persist_failure_restores_drop_and_inventory()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **inventory_has_named_item()** (5 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_handle_pickup_command_invalid_index()** (5 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_no_room_manager()** (5 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_no_target()** (5 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_search_term_not_found()** (5 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_drop_command_broadcasts_room_event_after_persist()** (5 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_drop_command_no_target()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_get_command_no_target()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_inventory_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_put_command_no_target()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **Test handle_ground_command() handles missing target.** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_drop_command()** (3 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_equip_command()** (3 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- *... and 30 more nodes in this community*

## Relationships

- [[Admin Summon Command]] (23 shared connections)
- [[Ground and Rescue Commands]] (5 shared connections)
- [[Inventory Service Helpers]] (4 shared connections)

## Source Files

- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/inventory_commands_test_support.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_inventory_commands_pickup.py`
- `server/tests/unit/commands/test_rescue_commands.py`

## Audit Trail

- EXTRACTED: 197 (89%)
- INFERRED: 25 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
