# Rest Command Flow

> 103 nodes · cohesion 0.03

## Key Concepts

- **inventory_command_helpers.py** (48 connections) — `server/commands/inventory_command_helpers.py`
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
- **Player** (11 connections)
- **add_pickup_to_inventory()** (10 connections) — `server/commands/inventory_command_helpers.py`
- **ensure_item_instance_for_pickup()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **_sync_collect_quests_after_inventory_save()** (7 connections) — `server/commands/inventory_command_helpers.py`
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

- [Commands Inventory Item](Commands_Inventory_Item.md) (27 shared connections)
- [Admin Summon Command](Admin_Summon_Command.md) (20 shared connections)
- [Deprecated Logging Patterns](Deprecated_Logging_Patterns.md) (11 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (10 shared connections)
- [Player Schema Models](Player_Schema_Models.md) (7 shared connections)
- [Commands Admin Shutdown](Commands_Admin_Shutdown.md) (7 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (5 shared connections)
- [Commands Inventory Display](Commands_Inventory_Display.md) (5 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (3 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (3 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (2 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (2 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`

## Audit Trail

- EXTRACTED: 442 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*