# Community 562

> 30 nodes

## Key Concepts

- **PickupTestWiring** (22 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_inventory_commands_pickup.py** (17 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command()** (8 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_inventory_capacity_error()** (8 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **asyncio** (8 connections)
- **sample_floor_item_stack()** (7 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **_pickup_with_persist_patch()** (7 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_persist_failure_restores_drop_and_inventory()** (7 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_emits_inventory_updated()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_invalid_index()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_no_room_manager()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_no_target()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_search_term_not_found()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **inventory_has_named_item()** (5 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **InventoryService** (4 connections)
- **Test handle_pickup_command() handles missing target.** (2 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **.__init__()** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **.set_floor_stack()** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **.set_listed_drops()** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **.set_player_inventory()** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **True if inv is a sequence of dict rows containing item_name == name.** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **Single sword stack as returned by list_room_drops / take_room_drop.** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **Standard app.state wiring for handle_pickup_command tests (typed mock surface…** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **Unit tests for handle_pickup_command (split from test_inventory_commands for…** (1 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **Test handle_pickup_command() handles invalid index.** (1 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- *... and 5 more nodes in this community*

## Relationships

- [Community 239](Community_239.md) (14 shared connections)
- [Community 246](Community_246.md) (10 shared connections)
- [Community 811](Community_811.md) (1 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/inventory_commands_test_support.py`
- `server/tests/unit/commands/test_inventory_commands_pickup.py`

## Audit Trail

- EXTRACTED: 69 (83%)
- INFERRED: 14 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*