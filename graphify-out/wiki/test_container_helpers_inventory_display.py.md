# test_container_helpers_inventory_display.py

> 29 nodes

## Key Concepts

- **PickupTestWiring** (19 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_inventory_commands_pickup.py** (18 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **inventory_commands_test_support.py** (10 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_handle_pickup_command()** (8 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_inventory_capacity_error()** (8 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_persist_failure_restores_drop_and_inventory()** (7 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **asyncio** (7 connections)
- **sample_floor_item_stack()** (6 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **_pickup_with_persist_patch()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_invalid_index()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_no_room_manager()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_no_target()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_search_term_not_found()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **inventory_has_named_item()** (5 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **Test handle_pickup_command() handles missing target.** (2 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **.__init__()** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **.set_floor_stack()** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **.set_listed_drops()** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **.set_player_inventory()** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **Shared helpers for inventory command unit tests.** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **True if inv is a sequence of dict rows containing item_name == name.** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **Single sword stack as returned by list_room_drops / take_room_drop.** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **Standard app.state wiring for handle_pickup_command tests (typed mock surface…** (1 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **Unit tests for handle_pickup_command (split from test_inventory_commands for…** (1 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **Test handle_pickup_command() handles invalid index.** (1 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- *... and 4 more nodes in this community*

## Relationships

- [GameLogPanel.tsx](GameLogPanel.tsx.md) (12 shared connections)
- [ContainerComponent](ContainerComponent.md) (6 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (6 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (3 shared connections)
- [game_tick_status_effects.py](game_tick_status_effects.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/inventory_commands_test_support.py`
- `server/tests/unit/commands/test_inventory_commands_pickup.py`

## Audit Trail

- EXTRACTED: 71 (88%)
- INFERRED: 10 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*