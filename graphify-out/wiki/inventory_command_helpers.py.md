# inventory_command_helpers.py

> 103 nodes · cohesion 0.03

## Key Concepts

- **inventory_command_helpers.py** (46 connections) — `server/commands/inventory_command_helpers.py`
- **persist_player()** (30 connections) — `server/commands/inventory_command_helpers.py`
- **test_inventory_helpers_extended.py** (26 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_inventory_commands_more_helpers.py** (23 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **broadcast_room_event()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_player()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_state()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **test_inventory_commands_persistence_helpers.py** (12 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **add_pickup_to_inventory()** (10 connections) — `server/commands/inventory_command_helpers.py`
- **Player** (10 connections)
- **_sync_collect_quests_after_inventory_save()** (8 connections) — `server/commands/inventory_command_helpers.py`
- **ensure_item_instance_for_pickup()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **test_inventory_commands_state_helpers.py** (6 connections) — `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- **test_persist_player_inventory_schema_error()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_persist_player_error()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **test_persist_player_validation_error()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_resolve_player_username_error()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_broadcast_room_event_exception()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_broadcast_room_event_no_broadcast_method()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_broadcast_room_event_no_connection_manager()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_broadcast_room_event_with_connection_manager()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_broadcast_room_event_with_exclude_player()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- *... and 78 more nodes in this community*

## Relationships

- [__init__.py](__init__.py.md) (27 shared connections)
- [inventory_pickup_command.py](inventory_pickup_command.py.md) (21 shared connections)
- [inventory_drop_command.py](inventory_drop_command.py.md) (11 shared connections)
- [AliasStorage](AliasStorage.md) (10 shared connections)
- [inventory_put_command.py](inventory_put_command.py.md) (7 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (7 shared connections)
- [Player](Player.md) (5 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (5 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [exceptions.py](exceptions.py.md) (2 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`

## Audit Trail

- EXTRACTED: 438 (98%)
- INFERRED: 11 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*