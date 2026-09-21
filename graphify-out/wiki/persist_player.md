# persist_player

> 83 nodes

## Key Concepts

- **persist_player()** (29 connections) — `server/commands/inventory_command_helpers.py`
- **test_inventory_helpers_extended.py** (26 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_inventory_commands_more_helpers.py** (23 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **broadcast_room_event()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **asyncio** (15 connections)
- **Player** (11 connections)
- **asyncio** (11 connections)
- **ensure_item_instance_for_pickup()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **_sync_collect_quests_after_inventory_save()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **_collect_progress_sync()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **_player_uuid_for_quest_sync()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **test_persist_player_inventory_schema_error()** (5 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_persist_player_error()** (5 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **test_persist_player_validation_error()** (5 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_broadcast_room_event_exception()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_broadcast_room_event_no_broadcast_method()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_broadcast_room_event_no_connection_manager()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_broadcast_room_event_with_connection_manager()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_broadcast_room_event_with_exclude_player()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_persist_player_generic_exception()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_persist_player_success()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_resolve_player_no_persistence()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_resolve_player_not_found()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_resolve_player_success()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_persist_player_success()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- *... and 58 more nodes in this community*

## Relationships

- [inventory_command_helpers.py](inventory_command_helpers.py.md) (13 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (12 shared connections)
- [test_command_service.py](test_command_service.py.md) (12 shared connections)
- [inventory_pickup_command.py](inventory_pickup_command.py.md) (10 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (5 shared connections)
- [command_result_text](command_result_text.md) (3 shared connections)
- [Player](Player.md) (3 shared connections)
- [admin_summon_command.py](admin_summon_command.py.md) (2 shared connections)
- [QuestService](QuestService.md) (2 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`

## Audit Trail

- EXTRACTED: 193 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*