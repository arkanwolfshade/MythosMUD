# validate_calendar.py

> 33 nodes · cohesion 0.12

## Key Concepts

- **PickupTestWiring** (22 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **handle_pickup_command()** (18 connections) — `server/commands/inventory_pickup_command.py`
- **test_inventory_commands_pickup.py** (18 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **inventory_commands_test_support.py** (11 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **asyncio** (8 connections)
- **test_handle_pickup_command()** (8 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_inventory_capacity_error()** (8 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **sample_floor_item_stack()** (7 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **_pickup_with_persist_patch()** (7 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_persist_failure_restores_drop_and_inventory()** (7 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_emits_inventory_updated()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_invalid_index()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_no_room_manager()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_no_target()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_search_term_not_found()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **inventory_has_named_item()** (5 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **Move an item stack from room drops into the player's inventory.** (1 connections) — `server/commands/inventory_pickup_command.py`
- **.__init__()** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **.set_floor_stack()** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **.set_listed_drops()** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **.set_player_inventory()** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **Shared helpers for inventory command unit tests.** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **True if inv is a sequence of dict rows containing item_name == name.** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **Single sword stack as returned by list_room_drops / take_room_drop.** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **Standard app.state wiring for handle_pickup_command tests (typed mock surface…** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- *... and 8 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (13 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (9 shared connections)
- [test_nats_message_handler_chat.py](test_nats_message_handler_chat.py.md) (6 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (3 shared connections)
- [command_parser.py](command_parser.py.md) (2 shared connections)
- [deprecated_patterns.py](deprecated_patterns.py.md) (1 shared connections)
- [test_nats_message_handler_subzone_events.py](test_nats_message_handler_subzone_events.py.md) (1 shared connections)

## Source Files

- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/inventory_commands_test_support.py`
- `server/tests/unit/commands/test_inventory_commands_pickup.py`

## Audit Trail

- EXTRACTED: 89 (88%)
- INFERRED: 12 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*