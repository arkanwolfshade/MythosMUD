# Admin NPC Schemas

> 39 nodes

## Key Concepts

- **handle_pickup_command()** (18 connections) — `server/commands/inventory_pickup_command.py`
- **command_result_text()** (17 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **PickupTestWiring** (17 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_inventory_commands_pickup.py** (17 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
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
- **test_handle_drop_command_no_target()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_equip_command_no_target()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **Move an item stack from room drops into the player's inventory.** (1 connections) — `server/commands/inventory_pickup_command.py`
- **.__init__()** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **.set_floor_stack()** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **.set_listed_drops()** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **.set_player_inventory()** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **Shared helpers for inventory command unit tests.** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **Normalize handler result message for assertions.** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- *... and 14 more nodes in this community*

## Relationships

- [Container Sync Remediation](Container_Sync_Remediation.md) (12 shared connections)
- [NATS Connection State Machine](NATS_Connection_State_Machine.md) (9 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (5 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)
- [Container Open Events](Container_Open_Events.md) (1 shared connections)
- [AnyIO vs Asyncio Guide](AnyIO_vs_Asyncio_Guide.md) (1 shared connections)

## Source Files

- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/inventory_commands_test_support.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_inventory_commands_pickup.py`

## Audit Trail

- EXTRACTED: 151 (90%)
- INFERRED: 16 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*