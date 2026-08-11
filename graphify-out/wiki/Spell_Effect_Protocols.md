# Spell Effect Protocols

> 130 nodes

## Key Concepts

- **inventory_command_helpers.py** (48 connections) — `server/commands/inventory_command_helpers.py`
- **persist_player()** (30 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **test_inventory_helpers_extended.py** (26 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_inventory_commands_more_helpers.py** (23 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **inventory_put_command.py** (21 connections) — `server/commands/inventory_put_command.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_state()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_player()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **broadcast_room_event()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **handle_put_command()** (13 connections) — `server/commands/inventory_put_command.py`
- **test_inventory_commands_persistence_helpers.py** (12 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **Player** (11 connections)
- **add_pickup_to_inventory()** (10 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_command_contracts.py** (9 connections) — `server/commands/inventory_command_contracts.py`
- **_put_resolve_container_id()** (9 connections) — `server/commands/inventory_put_command.py`
- **_put_transfer_finish()** (8 connections) — `server/commands/inventory_put_command.py`
- **_sync_collect_quests_after_inventory_save()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **ensure_item_instance_for_pickup()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **_put_run_validated()** (7 connections) — `server/commands/inventory_put_command.py`
- **test_inventory_commands_state_helpers.py** (6 connections) — `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- **_player_uuid_for_quest_sync()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **remove_item_from_inventory()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **UUID** (4 connections)
- *... and 105 more nodes in this community*

## Relationships

- [Container Sync Remediation](Container_Sync_Remediation.md) (24 shared connections)
- [WebSocket Auth Integration](WebSocket_Auth_Integration.md) (16 shared connections)
- [Rate Limiter Utilities](Rate_Limiter_Utilities.md) (15 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (12 shared connections)
- [Container Open Events](Container_Open_Events.md) (12 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (7 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (7 shared connections)
- [NPC Definition CRUD](NPC_Definition_CRUD.md) (7 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (6 shared connections)
- [Admin NPC Schemas](Admin_NPC_Schemas.md) (6 shared connections)
- [Container Inventory Ops](Container_Inventory_Ops.md) (5 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (4 shared connections)

## Source Files

- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_commands.py`
- `server/commands/inventory_put_command.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`

## Audit Trail

- EXTRACTED: 560 (97%)
- INFERRED: 17 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*