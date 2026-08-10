# Whisper Remediation Plan

> 61 nodes

## Key Concepts

- **inventory_command_helpers.py** (48 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **persist_player()** (30 connections) — `server/commands/inventory_command_helpers.py`
- **test_inventory_commands_more_helpers.py** (23 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **test_inventory_commands_persistence_helpers.py** (12 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **Player** (11 connections)
- **add_pickup_to_inventory()** (10 connections) — `server/commands/inventory_command_helpers.py`
- **_pickup_resolve_floor_stack_or_error()** (10 connections) — `server/commands/inventory_pickup_command.py`
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **resolve_pickup_item_index()** (8 connections) — `server/commands/inventory_command_helpers.py`
- **_sync_collect_quests_after_inventory_save()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **ensure_item_instance_for_pickup()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **get_room_manager()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **CommandResponse** (6 connections)
- **_pickup_broadcast_success()** (6 connections) — `server/commands/inventory_pickup_command.py`
- **_player_uuid_for_quest_sync()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **prepare_extracted_stack()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **UUID** (4 connections)
- **_pickup_quantity_or_error()** (4 connections) — `server/commands/inventory_pickup_command.py`
- **test_persist_player_inventory_schema_error()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_persist_player_error()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **_pickup_result_messages()** (3 connections) — `server/commands/inventory_pickup_command.py`
- *... and 36 more nodes in this community*

## Relationships

- [NPC Database Sessions](NPC_Database_Sessions.md) (30 shared connections)
- [Container Sync Remediation](Container_Sync_Remediation.md) (20 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (15 shared connections)
- [FastAPI Auth Integration](FastAPI_Auth_Integration.md) (15 shared connections)
- [Chat Service Whispers](Chat_Service_Whispers.md) (8 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (5 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (5 shared connections)
- [NPC Definition CRUD](NPC_Definition_CRUD.md) (5 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (4 shared connections)
- [Admin NPC Schemas](Admin_NPC_Schemas.md) (4 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`

## Audit Trail

- EXTRACTED: 348 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*