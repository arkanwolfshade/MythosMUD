# monitoring endpoints rationale

> 101 nodes

## Key Concepts

- **inventory_command_helpers.py** (48 connections) — `server/commands/inventory_command_helpers.py`
- **persist_player()** (30 connections) — `server/commands/inventory_command_helpers.py`
- **test_inventory_helpers_extended.py** (26 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_inventory_commands_more_helpers.py** (23 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **resolve_state()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_player()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **broadcast_room_event()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **Player** (11 connections)
- **_sync_collect_quests_after_inventory_save()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **ensure_item_instance_for_pickup()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **test_inventory_commands_state_helpers.py** (6 connections) — `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- **_collect_progress_sync()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **_player_uuid_for_quest_sync()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **prepare_extracted_stack()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **remove_item_from_inventory()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **UUID** (4 connections)
- **test_persist_player_inventory_schema_error()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_persist_player_validation_error()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_resolve_player_username_error()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_resolve_state_with_app()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_resolve_state_no_app()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_resolve_state_no_state()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_resolve_player_success()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_resolve_player_no_persistence()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- *... and 76 more nodes in this community*

## Relationships

- [database helpers infrastructure](database_helpers_infrastructure.md) (32 shared connections)
- [task registry app](task_registry_app.md) (12 shared connections)
- [shutdown command commands](shutdown_command_commands.md) (7 shared connections)
- [player cache rationale](player_cache_rationale.md) (6 shared connections)
- [useDraggablePanelInteractions draggableP](useDraggablePanelInteractions_draggableP.md) (6 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (5 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (5 shared connections)
- [game weapon player](game_weapon_player.md) (4 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (4 shared connections)
- [nats services service](nats_services_service.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [command inventory models](command_inventory_models.md) (2 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`

## Audit Trail

- EXTRACTED: 398 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*